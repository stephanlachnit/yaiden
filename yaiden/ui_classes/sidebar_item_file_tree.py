import os
from operator import itemgetter

from gi.repository import Gtk, GdkPixbuf

from ..file_opener import FileOpener


class FileTree(Gtk.ScrolledWindow):
    def __init__(self):
        super().__init__()

        # defaults
        self.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        self.set_size_request(200, -1)

        # tree view
        self.tree_view = Gtk.TreeView()
        self.add(self.tree_view)

        # icons
        icon_theme = Gtk.IconTheme.get_default()
        self.icon_file = icon_theme.load_icon('folder-documents', 24, Gtk.IconLookupFlags.FORCE_SYMBOLIC)
        self.icon_folder = icon_theme.load_icon('folder', 24, Gtk.IconLookupFlags.FORCE_SYMBOLIC)

        # tree store: name, icon, full path and is_dir
        self.tree_store = Gtk.TreeStore(str, GdkPixbuf.Pixbuf, str, bool)
        self.tree_view.set_model(self.tree_store)

        # populate tree store
        self.path_iter(None, os.getcwd())

        # column rendering
        cellrenderertext = Gtk.CellRendererText()
        cellrendererpixbuf = Gtk.CellRendererPixbuf()
        treeviewcolumn = Gtk.TreeViewColumn('Files')
        treeviewcolumn.pack_start(cellrendererpixbuf, False)
        treeviewcolumn.pack_start(cellrenderertext, True)
        treeviewcolumn.add_attribute(cellrendererpixbuf, 'pixbuf', 1)
        treeviewcolumn.add_attribute(cellrenderertext, 'text', 0)
        self.tree_view.append_column(treeviewcolumn)
        self.tree_view.connect('row-activated', self.on_row_activated)

    def on_row_activated(self, tree_view, path, _column):
        model = tree_view.get_model()
        tree_iter = model.get_iter(path)
        is_dir = model.get_value(tree_iter, 3)
        if is_dir:
            if self.tree_view.row_expanded(path):
                self.tree_view.collapse_row(path)
            else:
                self.tree_view.expand_row(path, False)
        else:
            file_path = model.get_value(tree_iter, 2)
            file_opener = FileOpener()
            file_opener.open(file_path)

    def path_iter(self, parent, folder):
        files = []
        folders = []
        # get (unsorted) content of a folder
        for dir_entry in os.scandir(folder):
            if dir_entry.is_dir():
                folders.append((dir_entry.name, dir_entry.path))
            else:
                files.append((dir_entry.name, dir_entry.path))
        # sort folders after name, add them and iterate on folder
        folders = sorted(folders, key=itemgetter(0))
        for folder_tuple in folders:
            new_parent = self.tree_store.append(parent, [folder_tuple[0], self.icon_folder, folder_tuple[1], True])
            self.path_iter(new_parent, folder_tuple[1])
        # sort folders after name and add them
        files = sorted(files, key=itemgetter(0))
        for file_tuple in files:
            self.tree_store.append(parent, [file_tuple[0], self.icon_file, file_tuple[1], False])
