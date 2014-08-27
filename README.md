ipy_notify
==========

Notifications for long-running ipython commands

Installation
------------

Copy `ipy_notify.py` to `~/.ipython/extensions/`.

Usage
-----

In an IPython notebook, run

```
%load_ext ipy_notify
```

A button will appear; you should click on it and then enable desktop notifications if your browser asks. Then test it:

```
import time
time.sleep(5)
```

Tab away from the page. In about five seconds, a popup will appear; click on it and your browser will re-focus the IPython tab.
