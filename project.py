from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.properties import StringProperty
from plyer import call

Builder.load_string('''
#:import COLOR kivy.utils.get_color_from_hex
#: import Platform kivy.utils.platform
#:set RED "#F94A69"
#:set GREEN "#06A5AB"

#: import Platform kivy.utils.platform
<CallInterface>:
    orientation: 'vertical'
    Label:
    BoxLayout:
        size_hint_y: None
        size: (400,100)
        MakeCallButton:
            tel: "0777740504"
            text: 'Report via Call'
            on_release: self.call()
            font_name: "Roboto"
            font_size: min(self.height, self.width) / 4
            bold: True
            background_normal: "./images/button_normal.png"
            background_down: "./images/button_down.png"
            background_color: COLOR("#0066BA")
            border: (2, 2, 2, 2)


    Label:

''')


class CallInterface(BoxLayout):
    pass

class getTel():
    def mytel(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.numbers
        self.collection = self.db.harare_south
        self.tel = self.collection.find_one({"location_name":"Marimba"})
        return self.tel


class DialCallButton(Button):

    def dial(self, *args):
        call.dialcall()


class MakeCallButton(Button):
    tel = StringProperty()

    def call(self, *args):
        call.makecall(tel=self.tel)


class CallApp(App):

    def build(self):
        return CallInterface()

    def on_pause(self):
        return True


if __name__ == "__main__":
    app = CallApp()
    app.run()
