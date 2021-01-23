from gettext import dgettext

from gi.repository import Gtk

from .preferences_window import PreferencesWindow
from .about_dialog import AboutDialog


class MenuButton(Gtk.MenuButton):
    def __init__(self):
        super().__init__()

        # preferences window
        self.menu_preferences = Gtk.MenuItem()
        self.menu_preferences.set_use_underline(True)
        self.menu_preferences.set_label(dgettext('gtk30', '_Preferences'))  # TODO: gtk40
        self.menu_preferences.connect('activate', PreferencesWindow.show_from_widget)

        # about dialog
        self.menu_about = Gtk.MenuItem()
        self.menu_about.set_use_underline(True)
        self.menu_about.set_label(dgettext('gtk30', '_About'))  # TODO: gtk40
        self.menu_about.connect('activate', AboutDialog.show_from_widget)

        # populate and show menu
        self.menu = Gtk.Menu()
        self.menu.append(self.menu_preferences)
        self.menu.append(self.menu_about)
        self.set_popup(self.menu)
        self.menu.show_all()
