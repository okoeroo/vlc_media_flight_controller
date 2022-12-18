import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk
from gi.repository import Gio

from gui.MediaList import MediaListItem


class VLCMediaControllerGUI(Gtk.Application):
    __gtype_name__ = "VLCMediaControllerGUI"

    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            application_id="nl.koeroo.vlc.media.controller.gui",
            flags=Gio.ApplicationFlags.HANDLES_COMMAND_LINE,
            **kwargs
        )

        # Builder
        self.builder = Gtk.Builder()
        self.builder.add_from_file("gui/vlc_media_controller.glade")
        self.builder.connect_signals(self)

        # Connect objects
        self.mainWindow = self.builder.get_object("main")
        self.mainWindow.connect("destroy", self.on_Destroy)
        
        self.listmedia = self.builder.get_object("listboxMedia")

        label = MediaListItem("test 1")
        self.listmedia.add(label)

        label = MediaListItem("test 2")
        self.listmedia.add(label)

        # View
        self.mainWindow.show_all()


    def on_Destroy(self, *args):
        print("Destroy button")

        # App quit
        print("Quit")
        Gtk.main_quit()
    