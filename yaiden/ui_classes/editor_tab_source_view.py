from gi.repository import Gtk, GtkSource, Gio, GLib


class TabSourceView(Gtk.ScrolledWindow):
    def __init__(self, file_path):
        super().__init__()

        # defaults
        self.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

        # source file
        self.file_path = file_path
        self.gio_file = Gio.File.new_for_path(self.file_path)
        self.source_file = GtkSource.File()
        self.source_file.set_location(self.gio_file)

        # buffer and language
        self.buffer = GtkSource.Buffer()
        self.buffer.set_implicit_trailing_newline(False)
        lang_mgr = GtkSource.LanguageManager.get_default()
        self.buffer.set_language(lang_mgr.guess_language(self.file_path, None))

        # file loader
        self.file_loader = GtkSource.FileLoader(buffer=self.buffer, file=self.source_file)
        self.file_loader.load_async(
            GLib.PRIORITY_DEFAULT,
            None,
            None,
            None,
            None,
            None,
        )

        # file saver
        self.file_saver = GtkSource.FileSaver(buffer=self.buffer, file=self.source_file)

        # source view
        self.source_view = GtkSource.View()
        self.source_view.set_buffer(self.buffer)
        self.source_view.set_vexpand(True)
        self.source_view.set_hexpand(True)
        self.add(self.source_view)

        # source view default
        # TODO: from settings
        self.source_view.set_monospace(True)
        self.source_view.set_highlight_current_line(True)
        self.source_view.set_show_line_numbers(True)
        self.source_view.set_show_right_margin(True)
        self.source_view.set_show_line_marks(True)
        self.source_view.set_right_margin_position(119)
        self.source_view.set_background_pattern(GtkSource.BackgroundPatternType.GRID)

        # keyboard shortcuts
        # accel_group = Gtk.AccelGroup()
        # key, mod = Gtk.accelerator_parse('<Control>S')
        # save_button.add_accelerator('clicked', accel_group, key, mod, Gtk.AccelFlags.VISIBLE)
        # save_button.connect('on-save', self.save)

        # show since not initialized with main window
        self.show_all()

    @staticmethod
    def new(file_path):
        # pylint: disable=arguments-differ
        return TabSourceView(file_path)

    def save(self):
        self.file_saver.save_async(
            GLib.PRIORITY_DEFAULT,
            None,
            None,
            None,
            None,
            None,
        )
        # TODO: Re-guess on saving for new files? Needs testing
        # lang_mgr = GtkSource.LanguageManager.get_default()
        # self.buffer.set_language(lang_mgr.guess_language(self.file_path, None))
