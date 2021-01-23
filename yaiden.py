#!/usr/bin/python3
#
# SPDX-FileCopyrightText: 2020-2021 Stephan Lachnit <stephanlachnit@protonmail.com>
#
# SPDX-License-Identifier: EUPL-1.2

import sys

import gi
gi.require_version('Gtk', '3.0')  # TODO: move to Gtk4
gi.require_version('GLib', '2.0')
gi.require_version('Handy', '1')
gi.require_version('GtkSource', '4')
gi.require_version('Gio', '2.0')
gi.require_version('Vte', '2.91')
gi.require_version('GdkPixbuf', '2.0')

from yaiden import application # pylint: disable=wrong-import-position


if __name__ == '__main__':
    app = application.Application()
    ret = app.run(sys.argv)
    sys.exit(ret)
