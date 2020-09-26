from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from baseclass.screen_login import ScreenLogin
from baseclass.screen_home import ScreenHome

Window.size = (350, 550)


class Oasis(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'DeepOrange'
        self.theme_cls.primary_hue = "900"

        return Builder.load_file("main.kv")

if __name__=='__main__':
    Oasis().run()
