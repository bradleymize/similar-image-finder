const express = require('express')
const app = express()
const port = 3000

const SD_MOUNTED_IMAGE_DIRECTORY = "/mnt/sd-outputs"

app.use('/', express.static('www'));
app.use('/images', express.static(SD_MOUNTED_IMAGE_DIRECTORY));

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})