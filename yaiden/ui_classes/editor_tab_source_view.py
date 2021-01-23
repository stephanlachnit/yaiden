from gettext import gettext as _

from gi.repository import Gtk, GtkSource, Gio, GLib


class TabSourceViewOverlay(Gtk.Overlay):
    def __init__(self, file_path):
        super().__init__()

        # scrolled window
        self.scrolled_window = Gtk.ScrolledWindow()
        self.scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        self.add(self.scrolled_window)

        # source view
        self.source_view = TabSourceView(file_path)
        self.scrolled_window.add(self.source_view)

        # source view menu button
        self.menu_button = TabSourceViewMenuButton()
        self.menu_button.set_halign(Gtk.Align.END)
        self.menu_button.set_valign(Gtk.Align.END)
        self.add_overlay(self.menu_button)

        # show since not initialized with main window
        self.show_all()

    @staticmethod
    def new(file_path):
        # pylint: disable=arguments-differ
        return TabSourceViewOverlay(file_path)


class TabSourceView(GtkSource.View):
    def __init__(self, file_path):
        super().__init__()

        # defaults
        self.set_vexpand(True)
        self.set_hexpand(True)

        # source view settings
        # TODO: from settings
        self.set_monospace(True)
        self.set_highlight_current_line(True)
        self.set_show_line_numbers(True)
        self.set_show_right_margin(True)
        self.set_show_line_marks(True)
        self.set_right_margin_position(119)
        self.set_background_pattern(GtkSource.BackgroundPatternType.GRID)

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
        self.set_buffer(self.buffer)

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

        # keyboard shortcuts
        # accel_group = Gtk.AccelGroup()
        # key, mod = Gtk.accelerator_parse('<Control>S')
        # save_button.add_accelerator('clicked', accel_group, key, mod, Gtk.AccelFlags.VISIBLE)
        # save_button.connect('on-save', self.save)

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


class TabSourceViewMenuButton(Gtk.MenuButton):
    def __init__(self):
        super().__init__()

        # defaults
        self.set_direction(Gtk.ArrowType.UP)

        # save button
        self.menu_save = Gtk.MenuItem()
        self.menu_save.set_label(_('Save'))

        # populate and show menu
        self.menu = Gtk.Menu()
        self.menu.append(self.menu_save)
        self.set_popup(self.menu)
        self.menu.show_all()
