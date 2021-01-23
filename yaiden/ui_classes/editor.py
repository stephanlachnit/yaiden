from gi.repository import Gtk

from ..file_opener import FileOpener
from .editor_notebook import Notebook
from .editor_tab_source_view import TabSourceViewOverlay
from .editor_terminal import TerminalRevealer


class Editor(Gtk.VPaned):
    def __init__(self):
        super().__init__()

        # initial position
        self.set_position(400)

        # notebook
        self.notebook = Notebook()
        self.pack1(self.notebook, True, False)

        # terminal
        # TODO: multiple terminals ?
        self.terminal_revealer = TerminalRevealer()
        self.pack2(self.terminal_revealer, False, False)

        # file opener
        file_opener = FileOpener()
        file_opener.set_notebook(self.notebook)
        file_opener.set_opening_widget_constructor(TabSourceViewOverlay.new)
