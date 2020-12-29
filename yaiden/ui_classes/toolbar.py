from gi.repository import Gtk


class Toolbar(Gtk.Toolbar):
    def __init__(self):
        super().__init__()

        # defaults
        self.set_orientation(Gtk.Orientation.VERTICAL)
        self.set_style(Gtk.ToolbarStyle.ICONS)

        # hide button
        self.button_hide = Gtk.ToolButton()
        self.button_hide.set_icon_name('sidebar-hide-symbolic')
        self.add(self.button_hide)

        # files button
        self.button_files = Gtk.ToolButton()
        self.button_files.set_icon_name('folder-visiting-symbolic')
        self.add(self.button_files)

    def connect_buttons(self, sidebar):
        self.button_hide.connect('clicked', sidebar.hide_stack)
        self.button_files.connect('clicked', sidebar.reveal_stack)
