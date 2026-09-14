#!/usr/bin/env bash
set -eu

# Add the filenames you want to download here, for example:
# filenames=("model.glb" "texture.png")
filenames=(
  "eta_asm.stp"
  "counter.splat"
  "backpack.vti"
  "bristleback_dota_fan-art.glb"
  "FlightHelmet.glb"
  "skull.vti"
  "future_parking_2k.hdr"
  "hikers_cave_2k.hdr"
  "202.vtp"
)

mkdir -p assets

for filename in "${filenames[@]}"; do
  if [ -f "assets/$filename" ]; then
    echo "Skipping $filename, already exists."
    continue
  fi

  url="https://f3d.app/data/$filename"
  echo "Downloading $url"
  curl -fL --create-dirs -o "assets/$filename" "$url"
done

echo "Finished downloading assets to ./assets"
