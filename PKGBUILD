export GIT_LFS_SKIP_SMUDGE=1

_pkgname=f3d
pkgname=f3d-video-git
pkgver=39517f45
pkgrel=1
pkgdesc='A fast and minimalist 3D viewer'
arch=(x86_64)
url="https://github.com/Meakk/${_pkgname}"
license=(BSD-3-Clause)
depends=(alembic
         assimp
         draco
         ffmpeg
         libwebp
         netcdf
         nlohmann-json
         opencascade
         openexr
         openvdb
         ospray
         pdal
         usd
         verdict
         vtk)
makedepends=(cmake
             fast_float
             git
             ninja)
source=("git+https://github.com/Meakk/${_pkgname}.git#branch=video")
sha256sums=('SKIP')

pkgver() {
  cd "${srcdir}/${_pkgname}"
  git describe --tags --long --always --dirty 2>/dev/null | sed 's/^v//; s/-/./g'
}

provides=("$_pkgname=${pkgver%%.g*}")
conflicts=("$_pkgname")

build() {
  cd "${srcdir}/${_pkgname}"
  export CXXFLAGS+=' -ffat-lto-objects'
  local _cmake_options=(
    -G Ninja
    -S "${srcdir}/${_pkgname}"
    -B build
    -D CMAKE_INSTALL_PREFIX=/usr
    -D CMAKE_BUILD_TYPE=None
    -D F3D_MODULE_RAYTRACING=On
    -D F3D_MODULE_EXR=On
    -D F3D_MODULE_FFMPEG=On
    -D F3D_MODULE_WEBP=On
    -D F3D_PLUGINS_STATIC_BUILD=On
    -D F3D_PLUGIN_BUILD_ALEMBIC=On
    -D F3D_PLUGIN_BUILD_ASSIMP=On
    -D F3D_PLUGIN_BUILD_DRACO=On
    -D F3D_PLUGIN_BUILD_HDF=On
    -D F3D_PLUGIN_BUILD_OCCT=On
    -D F3D_PLUGIN_BUILD_PDAL=On
    -D F3D_PLUGIN_BUILD_USD=On
    -D F3D_PLUGIN_BUILD_VDB=On
  )
  cmake "${_cmake_options[@]}"
  cmake --build build
}

package() {
  cd "${srcdir}/${_pkgname}"
  DESTDIR="$pkgdir" cmake --install build
  DESTDIR="$pkgdir" cmake --install build --component mimetypes
  DESTDIR="$pkgdir" cmake --install build --component sdk
  DESTDIR="$pkgdir" cmake --install build --component configuration
  install -Dm0644 -t "$pkgdir/usr/share/licenses/$pkgname/" LICENSE.md
}
