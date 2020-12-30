import os.path


class FileOpener():
    # borg pattern, basically a singleton
    # pylint: disable=method-hidden,attribute-defined-outside-init
    __monostate = dict()

    def __init__(self):
        self.__dict__ = FileOpener.__monostate

    def construct_widget(self, _file_path):
        pass

    def set_notebook(self, notebook):
        self.notebook = notebook

    def set_opening_widget_constructor(self, constructor):
        self.construct_widget = constructor

    def open(self, file_path):
        widget = self.construct_widget(file_path)
        self.notebook.open_widget(widget, os.path.basename(file_path))
