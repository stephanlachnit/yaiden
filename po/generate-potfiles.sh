#!/bin/sh
#
# SPDX-FileCopyrightText: 2020-2021 Stephan Lachnit <stephanlachnit@protonmail.com>
#
# SPDX-License-Identifier: CC0-1.0

cd "$(dirname "$(realpath "$0")")/.."

echo "# generated on $(date -u -Iseconds)" > ./po/POTFILES
echo "#" >> ./po/POTFILES
echo "# SPDX-FileCopyrightText: 2020-2021 Stephan Lachnit <stephanlachnit@protonmail.com>" >> ./po/POTFILES
echo "#" >> ./po/POTFILES
echo "# SPDX-License-Identifier: CC0-1.0" >> ./po/POTFILES

echo "" >> ./po/POTFILES
echo "data/io.github.stephanlachnit.yaiden.desktop" >> ./po/POTFILES
echo "data/io.github.stephanlachnit.yaiden.metainfo.xml" >> ./po/POTFILES

echo "" >> ./po/POTFILES
find yaiden -name '*.py' | LC_ALL=C sort >> ./po/POTFILES
