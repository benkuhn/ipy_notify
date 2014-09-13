import IPython.display

import datetime
import os
import subprocess

NOTIFY_SCRIPT = IPython.display.HTML("""
<script id="notification-script">
if (Notification.permission == 'granted') {
    var notification = new Notification("IPython command finished", {
        icon: "http://icons.iconarchive.com/icons/cornmanthe3rd/plex/512/Other-python-icon.png",
        body: IPython.notebook.notebook_name
    });
    notification.onclick = function () {
        window.focus();
    }
    // don't execute again if we open the window again
    var script = document.getElementById("notification-script");
    script.parentElement.removeChild(script);
}
</script>
""")

ACTIVATE_SCRIPT = IPython.display.HTML("""
<button class="notify_button" onclick="Notification.requestPermission(); $('.notify_button').hide();" style="display:none;">
  Show notifications
</button>
<script>
if (Notification.permission == 'default') {
    $('.notify_button').show();
}
</script>
""")

class Timer(object):
    def __init__(self, shell):
        self.shell = shell
        self.functions = [
            ('pre_execute', self.pre_execute),
            ('post_execute', self.post_execute),
        ]
        self.time = None
        IPython.display.display(ACTIVATE_SCRIPT)

    def pre_execute(self):
        self.time = datetime.datetime.now()

    def post_execute(self):
        if self.time is None:
            return
        then = self.time
        self.time = None
        now = datetime.datetime.now()
        diff = (now - then)
        if diff > datetime.timedelta(seconds=5):
            IPython.display.display(NOTIFY_SCRIPT)

timer = None

def load_ipython_extension(ipython):
    global timer
    timer = Timer(ipython)
    for hook, fn in timer.functions:
        ipython.events.register(hook, fn)

def unload_ipython_extension(ipython):
    for hook, fn in timer.functions:
        ipython.events.unregister(hook, fn)
