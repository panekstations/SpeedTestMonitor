import pyspeedtest
import rumps

# This SpeedTest Monitor app was created by https://github.com/panekstations


st = pyspeedtest.SpeedTest()
con = st.host
print(con)

timerdelay = 10
pingspeed = " ms"
displayspeed = " mbps"
icontodisplay = "lighticon.png"

# TODO change timing


def ping_timer(menu_item):
    def ping(timer):
        pn = st.ping()
        menu_item.title = 'Ping: ' + str(round(pn,1)) + pingspeed
    return rumps.Timer(ping, timerdelay)

def up_timer(menu_item):
    def upld(timer):
        pn = st.download() / 1000000
        menu_item.title = 'Down: ' + str(round(pn,2)) + displayspeed
    return rumps.Timer(upld, timerdelay)

def down_timer(menu_item):
    def dnld(timer):
        pn = st.upload() / 1000000
        menu_item.title = 'Up: ' + str(round(pn,2)) + displayspeed
    return rumps.Timer(dnld, timerdelay)

def serv_timer(menu_item):
    def serv(timer):
        pn = st._host()
        menu_item.title = str(pn)
    return rumps.Timer(serv, timerdelay)

class AwesomeStatusBarApp(rumps.App):
    def __init__(self):
        super(AwesomeStatusBarApp, self).__init__(name="SpeedTest Monitor", icon=icontodisplay)
        self.ping_item = rumps.MenuItem("Ping: N/A ms")
        self.down_item = rumps.MenuItem("Down: N/A mbps")
        self.up_item = rumps.MenuItem("Up: N/A mbps")
        self.serv_item = rumps.MenuItem(f"Server: {con}")
        ping_timer(self.ping_item).start()
        down_timer(self.down_item).start()
        up_timer(self.up_item).start()
        serv_timer(self.serv_item).start()

        self.menu = [self.ping_item, self.down_item, self.up_item, self.serv_item]

if __name__ == "__main__":
    AwesomeStatusBarApp().run()
