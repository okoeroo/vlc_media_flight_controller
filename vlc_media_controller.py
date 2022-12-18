#!/usr/bin/env python3

import gi
gi.require_version('Gst', '1.0')
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk
from gi.repository import Gst
from gui.VLCMediaController import VLCMediaControllerGUI


Gst.init(None)
Gst.init_check(None)
        
if __name__ == '__main__':
    fsg = VLCMediaControllerGUI()
    Gtk.main()
    print("Finished")