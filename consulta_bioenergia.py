import flet as ft
from pyairtable.orm  import Model, fields
import principal as pr

class Bioenergia(Model):
    cultivo=fields.TextField("cultivo")
    parte=fields.TextField("parte")
    cantidad=fields.FloatField("cantidad")
    area=fields.FloatField("area")
    energia=fields.FloatField("energia")
    municipio=fields.SelectField("municipio")
    latitud=fields.FloatField("latitud")
    longitud=fields.FloatField("longitud")

    class Meta:
        api_key="patZ3kb1eB1w02mEm.41c741e34acc12fe60f3181c19707ce6defbfe5b1cad78356138b94dd8eb31c6"
        base_id="appsHAOsh2bvzhdfM"
        table_name="bioenergia"

def main (page: ft.Page):

    def regresar (e:ft.ControlEvent):
        page.clean()
        pr.main(page)

    #configuracion de la pagina
    page.title="Consultas de Bioenergía"
    page.theme_mode="light"
    page.horizontal_alignment="center"
    page.appbar=ft.AppBar(title=ft.Text("Lista de productos"),center_title=True,leading=ft.Icon("people"),bgcolor="green",color="white")
    page.window.width=600
    page.window.height=700
    # Obtener todos los productos desde Airtable
    bioenergias = Bioenergia.all()

    # Crear la tabla
    tabla_bioenergias = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Cultivo")),
            ft.DataColumn(ft.Text("Parte")),
            ft.DataColumn(ft.Text("Cantidad")),
            ft.DataColumn(ft.Text("Area")),
            ft.DataColumn(ft.Text("Energía")),
            ft.DataColumn(ft.Text("Municipio")),
            ft.DataColumn(ft.Text("Latitud")),
            ft.DataColumn(ft.Text("Longitud")),
        ],
        rows=[]
    )

     # Llenar la tabla con los datos obtenidos
    for u in bioenergias:
        tabla_bioenergias.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(u.cultivo)),
                    ft.DataCell(ft.Text(u.parte)),
                    ft.DataCell(ft.Text(str(u.cantidad))),
                    ft.DataCell(ft.Text(str(u.area))),
                    ft.DataCell(ft.Text(str(u.energia))),
                    ft.DataCell(ft.Text(u.municipio)),
                    ft.DataCell(ft.Text(str(u.latitud))),
                    ft.DataCell(ft.Text(str(u.longitud)))
                ]
            )
        )

    #Componentes de la pagina 
    btn_regresar=ft.ElevatedButton("Regresar",on_click=regresar)
    page.add(tabla_bioenergias,btn_regresar)


    #Actualizar la pagina
    page.update()

#Inicio de la aplicación 
if __name__=="__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)


