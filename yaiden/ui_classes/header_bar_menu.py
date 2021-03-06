# SPDX-FileCopyrightText: 2020-2021 Stephan Lachnit <stephanlachnit@debian.org>
#
# SPDX-License-Identifier: EUPL-1.2

from gettext import gettext as _

from gi.repository import Gtk

from .preferences_window import PreferencesWindow
from .about_dialog import AboutDialog


class MenuButton(Gtk.MenuButton):
    def __init__(self):
        super().__init__()

        # preferences window
        self.menu_preferences = Gtk.MenuItem()
        self.menu_preferences.set_label(_('Preferences'))
        self.menu_preferences.connect('activate', PreferencesWindow.show_from_widget)

        # about dialog
        self.menu_about = Gtk.MenuItem()
        self.menu_about.set_label(_('About'))
        self.menu_about.connect('activate', AboutDialog.show_from_widget)

        # populate and show menu
        self.menu = Gtk.Menu()
        self.menu.append(self.menu_preferences)
        self.menu.append(self.menu_about)
        self.set_popup(self.menu)
        self.menu.show_all()
