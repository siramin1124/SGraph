from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
#from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout


class ButtonApp(App):
    def build(self):
        return FloatLayout()


if __name__ == "__main__":
    # kvfile().run()
    ButtonApp().run()
