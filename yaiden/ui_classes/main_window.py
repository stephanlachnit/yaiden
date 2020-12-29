from gi.repository import Gtk

from yaiden.ui_classes.header_bar import HeaderBar
from yaiden.ui_classes.toolbar import Toolbar
from yaiden.ui_classes.sidebar import Sidebar
from yaiden.ui_classes.editor import Editor


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, application):
        super().__init__(application=application)

        # defaults
        self.set_default_size(1200, 700)
        self.maximize()

        # icon
        self.set_default_icon_name('io.github.stephanlachnit.yaiden')

        # header bar
        self.header_bar = HeaderBar()
        self.set_titlebar(self.header_bar)

        # horizontal box for toolbar and sidebar + editor paned
        self.hbox = Gtk.HBox()
        self.add(self.hbox)

        # toolbar
        self.toolbar = Toolbar()
        self.hbox.pack_start(self.toolbar, False, False, 0)

        # horizontal paned for sidebar and editor
        # TODO: make paned unusable if stack is hidden
        self.hpaned = Gtk.HPaned()
        self.hbox.pack_end(self.hpaned, True, True, 0)

        # sidebar
        self.sidebar = Sidebar(self.hpaned)
        self.hpaned.pack1(self.sidebar, False, False)

        # connect toolbar buttons
        self.toolbar.connect_buttons(self.sidebar)

        # editor
        self.editor = Editor()
        self.hpaned.pack2(self.editor, True, False)

        # always show main window
        self.show_all()
