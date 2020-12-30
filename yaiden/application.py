from gettext import gettext as _

from gi.repository import Gtk, GLib

from yaiden.ui_classes.main_window import MainWindow


class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # program name and id
        self.set_application_id('io.github.stephanlachnit.yaiden')
        GLib.set_prgname('yaiden')
        GLib.set_application_name(_('Yaiden'))

        # keep track of main window
        self.main_window = None

    def do_activate(self):
        # Only allow one main window per application
        # pylint: disable=arguments-differ
        if self.main_window is None:
            self.main_window = MainWindow(self)
        self.main_window.present()
