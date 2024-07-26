# Rhythmbox hide on obscured plugin

A Rhythmbox3 plugin made to auto hide window once it was obscured.

Written in python3, drawing on project [palfrey/rhythmbox-tray-icon](https://github.com/palfrey/rhythmbox-tray-icon).

And thanks for [pgi-docs](https://lazka.github.io/pgi-docs/).

---

## story

Intuitively, some people want to banish the player window to the tray when listening to music playing in the background.
If that doesn't work, minimizing to the panel is also acceptable.

But  maybe in order to comply with the design philosophy of gnome, Rhythmbox itself lacks the tray iconify function,
then Gnome hides the minimized button of the window by default. And even if you click minimize somehow,
the window will still appear in the overview to interfere with your selection.

Thanks to Rhythmbox for implementing the mpris interface, we can inspect and control it in the media controller in the
notification area. And most importantly, we can regain the player window by clicking on the media controller!

So the media controller is a awesome and super large-size, ready-made tray icon, and now the only thing left to do is
***how to hide the window***. Of course, ***with this extremely simple plugin***, now you know.

---

## install

I don't know how to tell github to automatically expand the string in the README to generate a URL pointing to the path
in the repository, so please install it manually:

1. Create a new directory under the path `${HOME}/.local/share/rhythmbox/plugins/`, which can be called `hiddenobscured`
   or something else.
2. Download the two files with the suffix `.py` and `.plugin` in the repository, to the directory created by step 1.
3. Toward `Rhythmbox > Preferences > Plugin` menu, find `'Hide On Obscured',` and check to enable it.

---

## usage

After successfully enabling this plugin, the Rhythm window will be hidden once it is obscured by other full-screen windows
or the user manually clicks to minimize it.

At this time, you can click the notification area in the panel. If Rhythmbox has the `mpris` plugin enabled and the desktop
system supports media controllers for this interface, it will generally be displayed here. Click on an empty area on the
media controller to regain the hidden window.

---

## notice

There will be a little delay before hide, but it's not intentional. Besides, being obscured by a full-screen window does
not always reliably trigger auto-hide of the window.

For gnome-shell users, it is recommended to use [media-controls](https://github.com/sakithb/media-controls) or [media-progress](https://github.com/Krypion17/media-progress) extensions to enrich the functionality
of the media controller.

*(Although they have not yet implemented a button to close the player, who knows in the future?)*

---
