import os

from gi.repository import Gtk, Vte, GLib


class TerminalRevealer(Gtk.Revealer):
    def __init__(self):
        super().__init__()

        # defaults
        self.set_reveal_child(True)
        self.set_transition_type(Gtk.RevealerTransitionType.SLIDE_UP)

        # scrolled window
        self.scrolled_window = Gtk.ScrolledWindow()
        self.scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        self.add(self.scrolled_window)

        # terminal
        self.terminal = Vte.Terminal()
        self.scrolled_window.add(self.terminal)

        # terminal init
        self.terminal.spawn_sync(
            Vte.PtyFlags.DEFAULT,
            os.environ['HOME'],  # TODO: or workspace dir
            [os.environ['SHELL']],
            None,
            GLib.SpawnFlags.DEFAULT,
            None,
            None,
            None,
        )
