# SPDX-FileCopyrightText: 2020-2021 Stephan Lachnit <stephanlachnit@protonmail.com>
#
# SPDX-License-Identifier: EUPL-1.2

from gettext import gettext as _

from gi.repository import Gtk


class AboutDialog(Gtk.AboutDialog):
    def __init__(self):
        super().__init__()

        # icon
        # TODO: why needed? Should be loaded from Gtk.Window
        self.set_logo_icon_name('io.github.stephanlachnit.yaiden')

        # version
        self.set_version('v1')

        # website
        self.set_website('https://github.com/stephanlachnit/yaiden')
        self.set_website_label(_('Repository'))

        # copyright
        self.set_copyright('2020 Stephan Lachnit')
        self.set_license_type(Gtk.License.CUSTOM)
        self.set_license('EUPL-1.2')

    @staticmethod
    def show_from_widget(_widget):
        about_dialog = AboutDialog()
        about_dialog.show()
