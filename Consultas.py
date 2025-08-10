import flet as ft
from pyairtable.orm  import Model, fields
import principal as pr


class usuario(Model):
    clave=fields.TextField("clave")
    contraseña=fields.TextField("contraseña")
    nombre=fields.TextField("nombre")
    admin=fields.IntegerField("admin")

    class Meta:
        api_key="patZ3kb1eB1w02mEm.41c741e34acc12fe60f3181c19707ce6defbfe5b1cad78356138b94dd8eb31c6"
        base_id="appsHAOsh2bvzhdfM"
        table_name="usuario"


def main (page: ft.Page):
    def regresar (e:ft.ControlEvent):
        page.clean()
        pr.main(page)

    #configuracion de la pagina
    page.title="Consultas"
    page.theme_mode="light"
    page.horizontal_alignment="center"
    page.appbar=ft.AppBar(title=ft.Text("Lista de usuarios"),center_title=True,leading=ft.Icon("people"),bgcolor="green",color="white")
    page.window.width=600
    page.window.height=700
    # Obtener todos los usuarios desde Airtable
    usuarios = usuario.all()

    # Crear la tabla
    tabla_usuarios = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Clave")),
            ft.DataColumn(ft.Text("Contraseña")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Admin")),
        ],
        rows=[]
    )

     # Llenar la tabla con los datos obtenidos
    for u in usuarios:
        tabla_usuarios.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(u.clave))),
                    ft.DataCell(ft.Text(str(u.contraseña))),
                    ft.DataCell(ft.Text(u.nombre)),
                    ft.DataCell(ft.Text(str(u.admin))),
                ]
            )
        )

    #Componentes de la pagina 
    btn_regresar=ft.ElevatedButton("Regresar",on_click=regresar)
    page.add(tabla_usuarios,btn_regresar)


    #Actualizar la pagina
    page.update()

#Inicio de la aplicación 
if __name__=="__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)


