#from pyairtable import Api
from pyairtable.orm import Model
from pyairtable.orm import fields


class usuario(Model):
    clave=fields.TextField("clave")
    contraseña=fields.TextField("contraseña")
    nombre=fields.TextField("nombre")
    admin=fields.IntegerField("admin")

    class Meta:
        api_key="patZ3kb1eB1w02mEm.41c741e34acc12fe60f3181c19707ce6defbfe5b1cad78356138b94dd8eb31c6"
        base_id="appsHAOsh2bvzhdfM"
        table_name="usuario"

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
    
#Inicio de la aplicación 
if __name__=="__main__":
    ft.app(target=main,view=ft.AppView.WEB_BROWSER)

#cacao=Bioenergia(cultivo="cacao",parte="tallo",cantidad=20.2,area=12.5,energia=45.6,municipio="Coatzacalcos",latitud=18.578963,longitud=80.478963)

#cacao.save()
#nuevo=usuario(clave="222H16044",contraseña="Montejo",nombre="Olicristel",admin=0)

#nuevo.save()

#api=Api("patZ3kb1eB1w02mEm.41c741e34acc12fe60f3181c19707ce6defbfe5b1cad78356138b94dd8eb31c6")
#tabla=api.table("appsHAOsh2bvzhdfM","usuario")




#ALTAS
#yo={'clave': 'chavez', 'contraseña': 'chavez', 'nombre':'Olicristel Montejo', 'admin':1}
#table.create(yo)
#registros=tabla.all()
#for r in registros:
  #  print (r["fields"])


