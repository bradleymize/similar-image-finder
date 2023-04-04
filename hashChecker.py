import base64

from difPy import dif
import json
import os
from PIL import Image
from difflib import SequenceMatcher

JSON_FILE = "results.json"

if not os.path.exists(JSON_FILE):
    # search = dif(r'D:\Programs\stable-diffusion-webui\outputs\txt2img-images\2023-03-11', similarity='similar')
    search = dif(r'D:\Programs\stable-diffusion-webui\outputs\txt2img-images', similarity='similar')
    f = open(JSON_FILE, "w")
    f.write(json.dumps(search.__dict__, indent=4))
    f.close()

f = open(JSON_FILE, "r")
results = json.load(f)
f.close()

images = []

for original in results["result"].values():
    origLocationParts = original['location'].split("\\")
    startingLocation = origLocationParts.index("outputs")
    image = {'name': f"images/{'/'.join(origLocationParts[startingLocation+1:len(origLocationParts)])}", 'matches': []}

    img_data = Image.open(original['location'])
    image['width'] = img_data.width
    image['height'] = img_data.height
    img_data.load()
    image['parameters'] = img_data.info["parameters"]

    for match in original["matches"].values():
        matchLocationParts = match['location'].split("\\")
        matchStart = matchLocationParts.index("outputs")
        match_data = {
            'name': f"images/{'/'.join(matchLocationParts[matchStart+1:len(matchLocationParts)])}",
            'mse': match['mse']
        }

        img_data = Image.open(match['location'])
        match_data['width'] = img_data.width
        match_data['height'] = img_data.height
        img_data.load()
        match_data['parameters'] = img_data.info["parameters"]
        s = SequenceMatcher(None, match_data['parameters'], image['parameters'])
        match_data['parameterRatio'] = s.ratio()
        match_data['promptDiff'] = ""
        for tag, i1, i2, j1, j2 in s.get_opcodes():
            if tag == 'equal':
                # print(f"Equal: ({j1} - {j2}) {image['parameters'][j1:j2]}")
                match_data['promptDiff'] += f'<span class="same">{image["parameters"][j1:j2]}</span>'
            elif tag == 'insert':
                # print(f"Insert: ({j1} - {j2}) {image['parameters'][j1:j2]}")
                match_data['promptDiff'] += f'<span class="del">{image["parameters"][j1:j2]}</span>'
            elif tag == 'delete':
                # print(f"Delete: ({i1} - {i2}) {match_data['parameters'][i1:i2]}")
                match_data['promptDiff'] += f'<span class="ins">{match_data["parameters"][i1:i2]}</span>'


        image['matches'].append(match_data)

    images.append(image)


f = open('server/www/images.json', 'w')
f.write(json.dumps(images, indent=4))
f.close()
