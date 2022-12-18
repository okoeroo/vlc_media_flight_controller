#!/usr/bin/env python3

import os
import sys
import numpy as np
import threading
import json
import time

# Serial
from threading import Timer

sys.path.insert(0, '..')


TERMINATOR = '\0'
TERMINATOR = '\r\n'


import gi

gi.require_version('Gdk', '3.0')
gi.require_version("Gtk", "3.0")
gi.require_version('Gst', '1.0')
gi.require_version('GstVideo', '1.0')

from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import Gst
from gi.repository import GLib
from gi.repository import Gio
from gi.repository import GstVideo
from gi.repository import GObject


Gst.init(None)
Gst.init_check(None)




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
        self.mainWindow.show_all()


    def on_Destroy(self, *args):
        print("Destroy button")

        # App quit
        print("Quit")
        Gtk.main_quit()
    
        
if __name__ == '__main__':
    fsg = VLCMediaControllerGUI()
    Gtk.main()
    print("Finished")