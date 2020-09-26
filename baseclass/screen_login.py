from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from zeep import Client

class ScreenLogin(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()

    def change_theme(self, checkbox, value):
        if value:
            self.app.theme_cls.theme_style = "Dark"
        else:
            self.app.theme_cls.theme_style = "Light"

    def validar_acceso(self, usuario, password):
        client = Client('http://leda:85/Authentication.svc?wsdl')
        result = client.service.login(usuario, password, '07671171-adb0-410b-b5ec-ffc1bb894752')
        print(result)
        if result == "Ok":
            self.manager.current = "scr_home"
        else:
            self.ids["error"].text = f'{result}'



