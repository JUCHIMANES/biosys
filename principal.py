import flet as ft 
import alta_usuario as al 
import Consultas as c
import main as m
import Biomasa as b
import consulta_bioenergia as cb 

def main (page: ft.Page):
    def mostrar_registro(e:ft.ControlEvent):
        page.clean()
        al.main(page)
    
    def mostrar_consulta(e:ft.ControlEvent):
        page.clean()
        c.main(page)
    
    def mostrar_registrobioenergia(e:ft.ControlEvent):
        page.clean()
        b.main(page)
    
    def consultabioenergia(e:ft.ControlEvent):
        page.clean()
        cb.main(page)
    
    def inicio (e:ft.ControlEvent):
        page.clean()
        m.main(page) 
    

    #configuracion de la pagina
    page.title="Menu principal"
    page.theme_mode="light"
    page.appbar=ft.AppBar(
        title=ft.Text("Sistema de gestion de bioenergias"),
        leading=ft.Icon("energy_savings_leaf"),
        color="white",
        bgcolor="green"
    )

    #Componentes de la pagina 
    btn_registro=ft.ElevatedButton("Registro de usuario",on_click=mostrar_registro)
    btn_registrobioenergia=ft.ElevatedButton("Registro de Bioenergía",on_click=mostrar_registrobioenergia)
    btn_consultas=ft.ElevatedButton("Consulta de usuarios",on_click=mostrar_consulta)
    btn_consultabioenergia=ft.ElevatedButton("Consulta de Bioenergías",on_click=consultabioenergia)
    btn_salir=ft.FilledButton(text="Salir",icon="LOGOUT", width=250,bgcolor="green",on_click=inicio)
    
    #Añadir a la pagina 
    page.add(btn_registro,btn_registrobioenergia,btn_consultas,btn_consultabioenergia,btn_salir)
    page.update()

#Inicio de la aplicación 
if __name__=="__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
