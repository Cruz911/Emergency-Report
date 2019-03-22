from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.button import Button
from plyer import call
from kivy.properties import StringProperty

class MakeCallButton(Button):
    tel = StringProperty()

    def call(self, *args):
        call.makecall(tel=self.tel)

class ReportScreen(BoxLayout):
	pass

class RootScreenApp(App):
    def build(self):
        return ReportScreen


if __name__ == "__main__":
	RootScreenApp().run()


