
default: all

all: kodim

kodim:
	pushd data/external/kodim; curl -O http://r0k.us/graphics/kodak/kodak/kodim[01-24].png; popd

