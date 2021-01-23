# SPDX-FileCopyrightText: 2020-2021 Stephan Lachnit <stephanlachnit@protonmail.com>
#
# SPDX-License-Identifier: EUPL-1.2

from gi.repository import Gtk


class Notebook(Gtk.Notebook):
    def __init__(self):
        super().__init__()

        self.set_scrollable(True)

    def open_widget(self, widget, title):
        # close button and label
        close_button = Gtk.Button.new_from_icon_name('window-close-symbolic', Gtk.IconSize.SMALL_TOOLBAR)
        close_button.set_relief(Gtk.ReliefStyle.NONE)
        label = Gtk.Label(title)

        # box for button and label
        hbox = Gtk.HBox()
        hbox.pack_start(label, False, False, 0)
        hbox.pack_end(close_button, False, False, 0)
        hbox.show_all()

        # add new tab
        page = self.append_page(widget, hbox)
        self.set_current_page(page)
        self.set_tab_reorderable(widget, True)
        self.set_tab_detachable(widget, True)

        # connect closing action
        def close(_widget):
            # TODO: widget.on_close()
            self.remove_page(self.page_num(widget))
        close_button.connect('clicked', close)
