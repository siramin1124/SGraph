# coding: utf-8

# kivyの宣言
from kivy.app import App

# ボタンなのどの使用
from kivy.uix.label import Label

from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Username : "))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text="Password : "))
        self.password = TextInput(nultiline=False, password=True)
        self.add_widget(self.password)


class IntroKivy(App):
    def build(self):
        return LoginScreen()


if __name__ == "__main__":
    IntroKivy().run()
