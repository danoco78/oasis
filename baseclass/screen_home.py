from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from baseclass.conexion import conexion

class ScreenHome(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()

        try:
            with conexion.cursor() as cursor:
                # En este caso no necesitamos limpiar ningún dato
                cursor.execute("SELECT municipio FROM oasis.municipios;")

                # Con fetchall traemos todas las filas
                municipios = cursor.fetchall()

                # Recorrer e imprimir
                for municipio in municipios:
                    print(municipio)
        except Exception as e:
            print("Ocurrió un error al consultar: ", e)
        finally:
            conexion.close()

        menu_items = [{"text": f"{i[0]}"} for i in municipios]
"""
        menu_municipio = MDDropdownMenu(
            caller=self.ids.drop_item,
            items=menu_items,
            position="center",
            width_mult=10,
        )

        menu_municipio.bind(on_release=self.set_item)


    def set_item(self, instance_menu, instance_menu_item):
        self.ids.municipios.set_item(instance_menu_item.text)
        self.menu.dismiss()
"""