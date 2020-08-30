from kivy.app import App
#from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Line


class DrawInput(Widget):
    def on_touch_down(self, touch):
        print("Click!", touch.spos)
        with self.canvas:
            touch.ud["Sen"] = Line(points=(touch.x, touch.y))

    def on_touch_up(self, touch):
        print(touch.ud["Sen"].points)

    def on_touch_move(self, touch):
        touch.ud["Sen"].points += touch.x, touch.y


class ButtonApp(App):
    def build(self):
        return DrawInput()


if __name__ == "__main__":
    # kvfile().run()
    ButtonApp().run()
