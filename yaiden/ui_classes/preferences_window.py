# SPDX-FileCopyrightText: 2020-2021 Stephan Lachnit <stephanlachnit@debian.org>
#
# SPDX-License-Identifier: EUPL-1.2

from gi.repository import Handy


class PreferencesWindow(Handy.PreferencesWindow):
    def __init__(self):
        super().__init__()

        self.something = None

    @staticmethod
    def show_from_widget(_widget):
        preferences_window = PreferencesWindow()
        preferences_window.show()
