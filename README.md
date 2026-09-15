# F3D demos collection

These demos are assumed to be run on an Arch Linux computer.

## Assets

Assets must be downloaded using the following script:

```sh
./download-assets.sh
```

## Required packages

Install the following packages:

```sh
sudo pacman -S npm scrcpy
```

## Preparation

Install npm dependencies required to run web demos:

```sh
npm --prefix ./demo-07-android-n-web install
``` 

## Build and install f3d package

The following custom package contains the unmerged FFMPEG feature.
Consider removing it when integrated into `f3d-git` or after 4.0 release.


```sh
PKGDEST="/tmp/pkg" SRCDEST="/tmp/src/" SRCPKGDEST="/tmp/srcpkg" makepkg -sifcC
```
