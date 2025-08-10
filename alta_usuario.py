import flet as ft 
import principal as pr
from airtable import usuario 

def main(page: ft.Page):
    
    def cancelar(e:ft.ControlEvent):
        page.clean()
        pr.main(page)

    def guardar(e: ft.ControlEvent):
        # Leer valores
        clave = txt_clave.value.strip()
        contraseña = txt_contraseña.value.strip()
        confirmar = txt_contraseña2.value.strip()
        nombre = txt_nombre.value.strip()
        admin = 1 if chk_admin.value else 0

        # Validar que las contraseñas coincidan
        if contraseña != confirmar:
            print("Error: Las contraseñas no coinciden")
            return

        # Guardar en Airtable
        try:
            nuevo_usuario = usuario(clave=clave, contraseña=contraseña, nombre=nombre, admin=admin)
            nuevo_usuario.save()
            print("¡Usuario guardado correctamente!")

        except Exception as err:
            print(f"Error al guardar usuario: {err}")

    #Configuracion de la pagina
    page.title="Atlas"
    page.theme_mode="light"
    page.window.width=600
    page.window.height=700
    page.appbar=ft.AppBar(title=ft.Text("Nuevo usuario"),center_title=True,leading=ft.Icon("person_add"),color="white",bgcolor="green")



    #Componetes de la pagina 
    txt_clave=ft.TextField(label="Clave del usuario")
    espacio1 = ft.Container(height=10)  # Espacio entre campos
    txt_contraseña=ft.TextField(label="Contraseña",password=True, can_reveal_password=True)
    espacio2 = ft.Container(height=10)  # Espacio entre campos
    txt_contraseña2=ft.TextField(label="Confirmar contraseña", password=True, can_reveal_password=True)
    espacio3 = ft.Container(height=10)  # Espacio entre campos
    txt_nombre=ft.TextField(label="Nombre completo")
    espacio4 = ft.Container(height=10)  # Espacio entre campos
    chk_admin=ft.Checkbox(label="Es administrador?")
    espacio5 = ft.Container(height=10)  # Espacio entre campos
    btn_guardar=ft.FilledButton(text="Guardar",icon="save",bgcolor="green",on_click=guardar)
    btn_cancelar=ft.FilledButton(text="Cancelar",icon="cancel",bgcolor="green",on_click=cancelar)
    fila=ft.Row(controls=[btn_guardar,btn_cancelar])
    
    #Añadir componentes a la pagina
    page.add(txt_clave, espacio1,txt_contraseña,espacio2,txt_contraseña2,espacio3,txt_nombre,espacio4,chk_admin,espacio5,fila)
    #Actualizar la pagina
    #page.update()
#Inicio de la aplicación 
if __name__=="__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)


