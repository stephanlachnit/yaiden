# SPDX-FileCopyrightText: 2020-2021 Stephan Lachnit <stephanlachnit@protonmail.com>
#
# SPDX-License-Identifier: EUPL-1.2

from gettext import dgettext

from gi.repository import Gtk

from .header_bar_menu import MenuButton


class HeaderBar(Gtk.HeaderBar):
    def __init__(self):
        super().__init__()

        # defaults
        self.set_title('Yaiden')
        self.set_show_close_button(True)

        # workspace button
        self.workspace_button = Gtk.Button()
        self.workspace_button.set_use_underline(True)
        self.workspace_button.set_label(dgettext('gtk30', '_Open'))  # TODO: gtk40
        self.pack_start(self.workspace_button)

        # menu button
        self.menu_button = MenuButton()
        self.pack_end(self.menu_button)
