import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk
# from gi.repository import Gio

class MediaListItem(Gtk.Label):
    def __init__(self, data, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_text(data)
        self.set_justify(Gtk.Justification.LEFT)
        try:
            self.set_margin_start(10)
        except AttributeError:
            self.set_margin_left(10)
        self.set_width_chars(20)

