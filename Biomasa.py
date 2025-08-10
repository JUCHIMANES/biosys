import flet as ft
from airtable import Bioenergia
import principal as pr
import re

def main(page: ft.Page):
    page.title = "Biomasa"
    page.window_width = 900
    page.window_height = 600
    page.padding = 20

    # Municipios de Tabasco
    municipios_tabasco = [
        "Balancán", "Cárdenas", "Centla", "Centro", "Comalcalco",
        "Cunduacán", "Emiliano Zapata", "Huimanguillo", "Jalapa",
        "Jalpa de Méndez", "Jonuta", "Macuspana", "Nacajuca",
        "Paraíso", "Tacotalpa", "Teapa", "Tenosique"
    ]

    # ----------- PRIMERA FILA (3 columnas) -----------------
    cultivo_dropdown = ft.Dropdown(
        options=[ft.dropdown.Option(c) for c in [
            "Caña de Azúcar", "Cacao", "Maíz", "Coco", "Plátano"
        ]],
        width=200
    )

    parte_dropdown = ft.Dropdown(
        options=[ft.dropdown.Option(p) for p in [
            "Hoja", "Tallo", "Cáscara", "Bagazo", "Rastrojo"
        ]],
        width=200
    )

    municipio_dropdown = ft.Dropdown(
        options=[ft.dropdown.Option(m) for m in municipios_tabasco],
        width=200
    )


    # Creamos los TextField y los asignamos a variables para usarlos luego
    cantidad_tf = ft.TextField(width=100, hint_text="Ej: 20.23")
    area_tf = ft.TextField(width=100, hint_text="Ej: 150.23")
    energia_tf = ft.TextField(width=100, hint_text="Ej: 5.23")
    latitud_tf = ft.TextField(width=100, hint_text="Ej: 20.232425")
    longitud_tf = ft.TextField(width=100, hint_text="Ej: 20.238963")

    fila_superior = ft.Row([
        ft.Column([
            ft.Text("Cultivo origen", size=16, weight=ft.FontWeight.BOLD),
            cultivo_dropdown
        ], alignment=ft.MainAxisAlignment.START),

        ft.Column([
            ft.Text("Parte aprovechada", size=16, weight=ft.FontWeight.BOLD),
            parte_dropdown
        ], alignment=ft.MainAxisAlignment.START),

        ft.Column([
            ft.Text("Municipio", size=16, weight=ft.FontWeight.BOLD),
            municipio_dropdown
        ], alignment=ft.MainAxisAlignment.START),
    ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY
    )

    # ----------- SEGUNDA FILA (datos numéricos) -----------------
    # Columna izquierda: cantidad, humedad, área, contenido energético
    columna_datos_izquierda = ft.Column([
        ft.Row([ft.Text("Cantidad (ton)", width=130), cantidad_tf]),
        ft.Row([ft.Text("Área cultivada", width=130), area_tf]),
        ft.Row([ft.Text("Contenido energético", width=130), energia_tf])
    ], spacing=10)

    # Columna derecha: coordenadas (latitud y longitud)
    columna_datos_derecha = ft.Column([
        ft.Text("Coordenadas", size=14, weight=ft.FontWeight.BOLD),
        ft.Row([ft.Text("Latitud", width=80), latitud_tf]),
        ft.Row([ft.Text("Longitud", width=80), longitud_tf])
    ], spacing=10)

    fila_inferior = ft.Row([
        columna_datos_izquierda,
        columna_datos_derecha
    ], alignment=ft.MainAxisAlignment.SPACE_EVENLY, spacing=60)

     # --- Aquí definimos las funciones para botones ---
    
    

    def guardar(e:ft.ControlEvent):
        cultivo = cultivo_dropdown.value
        parte = parte_dropdown.value
        municipio = municipio_dropdown.value
        cantidad_str = cantidad_tf.value
        area_str = area_tf.value
        energia_str = energia_tf.value
        latitud_str = latitud_tf.value
        longitud_str = longitud_tf.value

        if not all([cultivo, parte, municipio, cantidad_str, area_str, energia_str, latitud_str, longitud_str]):
            print("Por favor, llena todos los campos.")
            return
        
        regex_2dec = r"^\d+(\.\d{1,2})?$"
        regex_6dec = r"^\-?\d+(\.\d{6})$"

        if not re.match(regex_2dec, cantidad_str):
           print("Cantidad debe tener máximo 2 decimales.")
           return
        
        if not re.match(regex_2dec, area_str):
            print("Área debe tener máximo 2 decimales.")
            return
        
        if not re.match(regex_2dec, energia_str):
            print("Contenido energético debe tener máximo 2 decimales.")
            return
        
        if not re.match(regex_6dec, latitud_str):
            print("Latitud debe tener exactamente 6 decimales.")
            return
        
        if not re.match(regex_6dec, longitud_str):
            print("Longitud debe tener exactamente 6 decimales.")
            return
        
        try:
            cantidad = float(cantidad_str)
            area = float(area_str)
            energia = float(energia_str)
            latitud = float(latitud_str)
            longitud = float(longitud_str)

            nuevo_registro = Bioenergia(
                cultivo=cultivo,
                parte=parte,
                municipio=municipio,
                cantidad=cantidad,
                area=area,
                energia=energia,
                latitud=latitud,
                longitud=longitud
            )
            nuevo_registro.save()
            print("Datos guardados correctamente en Airtable")
       
        except ValueError:
            print("Error: Asegúrate de que los valores numéricos sean correctos.")
        except Exception as err:
            print(f"Error al guardar los datos: {err}")

    def cancelar(e:ft.ControlEvent):
        page.clean()
        pr.main(page)

    # --- Crear los botones ---
    btn_guardar = ft.FilledButton(text="Guardar", icon="save", bgcolor="green", on_click=guardar)
    btn_cancelar = ft.FilledButton(text="Cancelar", icon="cancel", bgcolor="green", on_click=cancelar)
    fila_botones = ft.Row(controls=[btn_guardar, btn_cancelar], alignment=ft.MainAxisAlignment.CENTER, spacing=20)
    

    # ----------- AÑADIMOS A LA PAGINA -----------------
    page.add(
        ft.Column([
            ft.Container(
                content=ft.Text("Biomasa", size=26, weight=ft.FontWeight.BOLD),
                alignment=ft.alignment.center,
                bgcolor="green",
                padding=10
            ),
            fila_superior,
            ft.Divider(height=20, color="transparent"),
            fila_inferior,
            ft.Container(height=100),
            fila_botones
        ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=25,
            expand=True
        )
    )

#Inicio de la aplicación 
if __name__=="__main__":
    ft.app(target=main,view=ft.AppView.WEB_BROWSER)





