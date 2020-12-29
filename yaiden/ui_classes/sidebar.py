from gi.repository import Gtk

from yaiden.ui_classes.sidebar_item_file_tree import FileTree


class Sidebar(Gtk.Revealer):
    def __init__(self, hpaned):
        super().__init__()

        # defaults
        self.set_reveal_child(False)
        self.set_transition_type(Gtk.RevealerTransitionType.SLIDE_RIGHT)

        # store paned
        self.hpaned = hpaned

        # stack
        self.stack = Gtk.Stack()
        self.add(self.stack)

        # file_tree item
        self.file_tree = FileTree()
        self.stack.add_named(self.file_tree, 'file_tree')

    # hide the stack
    def hide_stack(self, _widget):
        self.set_reveal_child(False)

        # make sure paned is at the left most position
        self.hpaned.set_position(-1)

    # reveal the stack
    def reveal_stack(self, _widget):
        if not self.get_reveal_child():
            self.set_reveal_child(True)
