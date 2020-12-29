#!/usr/bin/python3

import gi
gi.require_version('Gtk', '3.0')  # TODO: move to Gtk4
gi.require_version('GLib', '2.0')
gi.require_version('Handy', '1')
gi.require_version('GtkSource', '4')
gi.require_version('Gio', '2.0')
gi.require_version('Vte', '2.91')
gi.require_version('GdkPixbuf', '2.0')


def main():
    # pylint: disable=import-outside-toplevel,no-name-in-module
    import sys
    from yaiden.application import Application

    app = Application()
    ret = app.run(sys.argv)
    sys.exit(ret)


if __name__ == '__main__':
    main()
