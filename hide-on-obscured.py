# -*- coding: utf-8 -*-
#
# +++++++++++++++++++++++++++++++++++++++++
# There is no copyright© claim on this file
# +++++++++++++++++++++++++++++++++++++++++
#
# Attention:
# This script makes the window hidden when it was completely occuluded or minimized.
# There is no GDK_WINDOW_STATE_ICONIFIED in the 'pgi-docs/Gdk-3.0/enums.html#Gdk.EventType.WINDOW_STATE',
# and it is not obtained in practice, so it is hard to distinguish between being occluded and minimized.
#
# Before enabling this script, please make sure you have enabled the mpris (or similar) plugin too
# so that you can click the media controller from the notification area to retrieve the hidden window.
# Otherwise you may have to terminate the program running in the background via the console.
# 2024/07/26


from gi.repository import GObject, Peas, Gtk, Gdk

class HideOnObscured(GObject.Object, Peas.Activatable):

    object = GObject.property(type=GObject.GObject)

    def __init__(self):
        super(self.__class__).__init__()

    def cb_obscured_handler(self, widget, event):
        if event.state & Gdk.VisibilityState.FULLY_OBSCURED:
                self.window.hide()
        return True

    def do_activate(self):
        self.window = self.object.get_property("window")
        self.id_obscured_handler = self.window.connect("visibility-notify-event", self.cb_obscured_handler)

    def do_deactivate(self):
        self.window.disconnect(self.id_obscured_handler)
