from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from baseclass.conexion import conexion
from kivymd.uix.menu import MDDropdownMenu

class ScreenHome(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()

        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT municipio FROM oasis.municipios;")
                municipios = cursor.fetchall()

        except Exception as e:
            print("Ocurrió un error al consultar: ", e)
        finally:
            conexion.close()

        menu_items = [{f"{i[0]}" for i in municipios}]

