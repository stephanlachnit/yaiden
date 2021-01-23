<!--
# SPDX-FileCopyrightText: 2020-2021 Stephan Lachnit <stephanlachnit@protonmail.com>
#
# SPDX-License-Identifier: CC0-1.0
-->

# Yaiden
[![GitHub Actions Status](https://github.com/stephanlachnit/yaiden/workflows/Build%20and%20test/badge.svg)](https://github.com/stephanlachnit/yaiden/actions?query=workflow%3A%22Build+and+test%22)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/stephanlachnit/yaiden.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/stephanlachnit/yaiden/context:python)
[![REUSE status](https://api.reuse.software/badge/github.com/stephanlachnit/yaiden)](https://api.reuse.software/info/github.com/stephanlachnit/yaiden)
## Terminal focused Gtk based IDE
Yaiden is the IDE that puts the terminal in its focus, letting you focus on your work.

**Yaiden is still a WIP and lacks basically every feature you expect from an IDE.**

- Clean UI: thanks to the Gtk implementation, Yaiden has a high content-to-screen ratio.
- Lightweight: offloads almost everything to GtkSource, keeping the implementation small.
- No-Annoyance: no notifications asking for your feedback or recommending you extensions.

![Screenshot](https://raw.githubusercontent.com/stephanlachnit/yaiden/master/docs/screenshot.png)

## Development
I don't have big plans for Yaiden (yet), it's just a side project I do for fun to learn the Gtk bindings for Python. Don't expect much from feature requests when you can't provide a PR for them yourself. That being said, if you want to help out, you're more than welcome to do so!

## Current features
- Loading files from its working directory
- Syntax highlighting

## Requirements (Debian package names)
### Building
`meson gettext appstream`
### Running
`gir1.2-gtk-3.0 gir1.2-glib-2.0 gir1.2-handy-1 gir1.2-gtksource-4 gir1.2-vte-2.91 gir1.2-gdkpixbuf-2.0 adwaita-icon-theme`
### Testing
`flake8 pylint python3-enchant apsell desktop-file-utils`

## License
This project is licensed under the rather unknown European Union Public License 1.2, a license from the European Commission which is comparable to the AGPL but with linking freedom. It has been officially translated to 23 languages and is OSI and FSF approved.
