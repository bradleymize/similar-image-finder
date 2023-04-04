# Usage #

This assumes you already have Python 3.10.6 (or equivalent) installed as per Automatic1111. 

1. Install python dependencies with `pip install -r requirements.txt`
2. Update `hashChecker.py` to point to the Automatic1111 output directory of your choice
3. Run `python hashChecker.py` to generate both the `results.json` file (containing identified
   duplicate and similar images), and the `server/www/images.json` file (containing a processed
   form of `results.json` use for rendering the static site)
4. Run `npm i` in the `server` folder
5. Update the path in `server.bat` to the same path used in step 2
6. Run `server.bat` (or equivalent docker command)
7. Navigate to `http://localhost:3000` to view the identified duplicate and/or similar images,
   complete with prompt diff