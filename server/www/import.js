async function main() {
    let response = await fetch('./images.json');
    let json = await response.json();
    // console.log(json);
    appendResults(generateHtml(json));
}

function generateHtml(json) {
    const rowsHtml = [];
    for (const item of json) {
        const origHtml = getOriginalHtml(item);

        item.matches.sort((a, b) => a.parameterRatio - b.parameterRatio)

        const similarItemsHtml = [];

        for (const match of item.matches) {
            similarItemsHtml.push(getMatchHtml(match));
        }

        rowsHtml.push(buildRowHtml(origHtml, similarItemsHtml.join('\n')));
    }
    return rowsHtml.join('\n');
}

function getOriginalHtml(item) {
    return `  <div class="original">
    <img class="sd-image" title="${item.name}" src="${item.name}">
    <div>${item.width} x ${item.height}</div>
  </div>`
}

function getMatchHtml(item) {
    return `    <div class="similar-img">
      <img class="sd-image" title="${item.name}" src="${item.name}">
      <div>${item.width} x ${item.height} (${item.parameterRatio})</div>
      <div>${item.promptDiff}</div>
    </div>`
}

function buildRowHtml(originalHtml, similarHtml) {
    return `<div class="row">
${originalHtml}
  <div class="similar">
${similarHtml}
  </div>
</div>`
}

function appendResults(htmlString) {
    const resultDiv = document.getElementById("results");
    resultDiv.textContent = "";

    const parser = new DOMParser();
    const doc = parser.parseFromString(htmlString, 'text/html');

    resultDiv.appendChild(doc.body);
}

await main();