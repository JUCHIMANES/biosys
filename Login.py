import flet as ft  
#import modelo as md #solo es local 
#import airtable as at 
import principal as pr
#Funcion principal 

def main (page: ft.Page):

    """def validar_usuario(e: ft.ControlEvent):
        #Validar campos 
        usuario=txt_usuario.value
        contraseña=txt_contraseña.value
        snackbar = ft.SnackBar(ft.Text("Introduce tu usuario"), bgcolor="blue", show_close_icon=True)
        if usuario == "":
            snackbar.content = (ft.Text("Introduce tu usuario"))
            page.open(snackbar)
            return
            
        elif contraseña == "":
            snackbar.content = (ft.Text("Introduce tu contraseña"))
            page.open(snackbar)
            return


        #verificar usuario en la base de datos
        #x= md.Usuario.select().where(
        #    md.Usuario.clave == usuario,
         #   md.Usuario.contraseña == contraseña
        #) 

        filtro=at.Usuario.usuario.eq(usuario)
        x=at.usuario.all(formula=filtro)

        if len(x) == 0:
            snackbar.content = ft.Text("Credenciales incorrectas")
            page.open(snackbar)
        else:
            page.clean()
            pr .clean(page)"""


    def ingresar (e: ft.ControlEvent):
        page.clean()
        pr.main(page)


    #configuración de la pagina 
    page.there_mode="light"
    page.horizontal_alignment="center"
    page.title="Inicio de Sesión"
    page.window.width=600
    page.window.height=700

    #Componentes de la pagina
    logo=ft.Icon("person", size=150, color="green")
    txt_bienvenido=ft.Text("Bienvenid@",size=38,color="green")
    txt_usuario=ft.TextField(label="Username/correo",width=300)
    espacio1 = ft.Container(height=10)  # Espacio entre campos
    txt_contraseña=ft.TextField(label="Contraseña", password=True, can_reveal_password=True,width=300)
    espacio2 = ft.Container(height=10)  # Espacio entre campos
    btn_login=ft.FilledButton(text="Iniciar Sesion", icon=ft.Icons.LOGIN, width=250,bgcolor="green",on_click=ingresar)

    page.add(logo,txt_bienvenido,txt_usuario,espacio1,txt_contraseña,espacio2,btn_login)
    #Actualizar la pagina
    page.update()

#Inicio de la aplicación 
if __name__=="__main__":
    ft.app(target=main)

