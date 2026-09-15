# Demo 05: Offscreen & automation

Explain that F3D can be used offscreen and used into automation pipeline.
Technically, that's how thumbnails are generated on Windows and Linux.

- Run `f3d ../assets/bristleback_dota_fan-art.glb --resolution=300,300 --no-background --output=/tmp/out.png`

Explain that it's possible to output an image sequence:

- Run `f3d ../assets/bristleback_dota_fan-art.glb --animation-autoplay --output=/tmp/out_{frame}.png`

It's also possible to out a video directly:

- Run `f3d ../assets/bristleback_dota_fan-art.glb --animation-autoplay --output-video=/tmp/out.h264`

That's raw h264 frames, use ffmpeg and piping to create a classic mp4 container file

- Run `f3d ../assets/bristleback_dota_fan-art.glb --animation-autoplay --output-video=- | ffmpeg -i - /tmp/out.mp4`
