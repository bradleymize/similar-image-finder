docker run ^
  -it ^
  --rm ^
  -p 3000:3000 ^
  --volume %cd%:/usr/src/app ^
  --volume D:\Programs\stable-diffusion-webui\outputs:/mnt/sd-outputs ^
  --workdir /usr/src/app/server ^
  node:18 npm run server