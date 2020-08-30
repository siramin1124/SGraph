from kivy.app import App
#from kivy.uix.label import Label
#from kivy.uix.button import Button
from kivy.uix.widget import Widget


class Widgets(Widget):
    def on_touch_down(self, touch):
        print("Click!", touch.spos)

    def on_touch_up(self, touch):
        print("Released!", touch.spos)

    def on_touch_move(self, touch):
        print("Mouce move!", touch)


class ButtonApp(App):
    def build(self):
        return Widgets()


if __name__ == "__main__":
    # kvfile().run()
    ButtonApp().run()
