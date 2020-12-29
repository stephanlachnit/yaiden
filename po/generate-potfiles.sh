#!/bin/sh

cd "$(dirname "$(realpath "$0")")/.."

echo "# generated on $(date -u -Iseconds)" > ./po/POTFILES

echo "" >> ./po/POTFILES
echo "data/io.github.stephanlachnit.yaiden.desktop" >> ./po/POTFILES
echo "data/io.github.stephanlachnit.yaiden.metainfo.xml" >> ./po/POTFILES

echo "" >> ./po/POTFILES
find yaiden -name '*.py' | LC_ALL=C sort >> ./po/POTFILES
