from couchdb import *
#conexión a la BD:

def insertar(db):
    print("1. Refugio")
    print("2. Animal")
    print("3. Donacion")
    print("4. Solicitud")
    op = input("Seleccione opcion:")
    if(op=="1"):
        nit = input("ingrese el nit")
        rep = input("ingrese el representante")
        fondos = input("ingrese fondos")
        db.save({"nit":{nit},"rep_legal":{rep},"fondos":{fondos}})
    elif(op=="2"):
        nombre=input('Ingrese nombre')
        raza=input('Ingrese raza')
        edad=int(input('Ingrese edad'))
        sexo=str(input('Ingrese sexo (M/F)'))
        if((sexo=='m' or sexo == 'M')):
            sexo='Macho'
        else:
            sexoo='Hembra'
    elif(op=="3"):
        idd=input('Ingrese ID del refugio')
        monto=float(input('Ingrese monto'))
        donaciones={idd,monto}
    else:
        idd=input()
    insertar()

    pass

def consultar(db: couchdb.database ): 
    nit = input("Digite Nit para buscar: ")
    result = db.view("refugios", "NIT", key=nit)
    if not nit in listado["nit"]:
        print ("No existe un usuario con ese NIT.")
    
    
    

def update(db):
    print ("Actualizar datos de un documento") 
    iddoc = raw_input ("Indique el id del documento que desea actualizar : ")
    newdata = {}
    newkey = raw_input ("indique la llave que desee actualizar : ")
    newvalue = raw_input ("indique el nuevo valor : ")
    newdata[newkey] = newvalue
    db.update ({iddoc: {iddoc}}, newdata)
    
    #doc_creado["fondos"] = 1000000.0
    #db.save(doc_creado)
    #print(doc_creado)
    
    pass

def delete(db):
    # Elimina todos los documentos en una base de datos
    for i in range(len(db)):
        print(i, db[i])
    print ("Eliminar documento")
    iddoc = int(raw_input ("Indique el indice del documento a eliminar : "))
    iddoc = input ("Indique el id del documento a eliminar : ")
    db._delete([iddoc], bulk=True )
    db.delete ([iddoc])
    db.bulk_docs({iddoc})

    print("ingrese el id a borrar")
    doc_borrar = input("ingrese id")
    db.delete(doc_borrar)
    pass


# vistas del refugio



#view = db.create_view('my_view', 'function(doc) {
#  emit(doc.nit, doc.rep_legal);
#}')
#print(view)
#vistas de perro
view = {
  "_id": "_design/my_view",
  "views": {
    "my_view": {
      "map": "function(doc) { emit(doc.nombre, doc); }"
    }
  }
}
db.save(view)
#vista donacion
view = {
  "_id": "_design/my_view",
  "views": {
    "my_view": {
      "map": "function(doc) { emit(doc.donacion, doc); }"
    }
  }
}
db.save(view)

# vista peticiones adopcion 
view = {
    "_id": "_design/my_view",
    "views": {
        "my_view": {
            "map": "function(doc) { emit(doc.animal_id, doc.aprobada); }"
        }
    }
}
db.save(view)

#Operaciones del crud:
# (1) Insert: creación de un documento
#información de dos refugios:
db.save({"_id":"1","nit":"98989898","rep_legal":"Diego L","fondos":0.0})
db.save({"_id":"2","nit":"50505050","rep_legal":"Diana L","fondos":0.0})

db.save({"_id":"1000","nombre":"toby","especie":"perro","edad":12, "esterilizado":True, "adoptado":False})
db.save({"_id":"1001","nombre":"luna","especie":"gato","edad":10, "esterilizado":True, "adoptado":False})
db.save({"_id":"1002","nombre":"max","especie":"perro","edad":8, "esterilizado":True, "adoptado":True})
db.save({"_id":"1003","nombre":"mia","especie":"gato","edad":6, "esterilizado":False, "adoptado":False})
db.save({"_id":"1004","nombre":"rocky","especie":"perro","edad":4, "esterilizado":True, "adoptado":True})
db.save({"_id":"1005","nombre":"luna","especie":"gato","edad":2, "esterilizado":False, "adoptado":False})
db.save({"_id":"1006","nombre":"Toby","especie":"Perro","edad":12,"esterilizado":True,"adoptado":False})
db.save({"_id":"1007","nombre":"Luna","especie":"Gato","edad":10,"esterilizado":True,"adoptado":False})
db.save({"_id":"1008","nombre":"Max","especie":"Perro","edad":8,"esterilizado":True,"adoptado":True})
db.save({"_id":"1009","nombre":"Mia","especie":"Gato","edad":6,"esterilizado":False,"adoptado":False})
db.save({"_id":"1010","nombre":"Rocky","especie":"Perro","edad":4,"esterilizado":True,"adoptado":True})
db.save({"_id":"1011","nombre":"Luna","especie":"Gato","edad":2,"esterilizado":False,"adoptado":False})

db.save({"_id":"1012","donacion":"Alimento","valor":10000})
db.save({"_id":"1013","donacion":"Medicina","valor":5000})
db.save({"_id":"1014","donacion":"Dinero","valor":20000})

db.save({"_id":"a1015","animal_id":"1006","aprobada":True})
db.save({"_id":"a1016","animal_id":"1007","aprobada":False})
db.save({"_id":"a1017","animal_id":"1008","aprobada":True})
db.save({"_id":"a1018","animal_id":"1009","aprobada":False})
db.save({"_id":"a1019","animal_id":"1010","aprobada":True})
db.save({"_id":"a1020","animal_id":"1011","aprobada":False})

# (2)  Select: selección de un documento por un determinado valor de llave ("_id")
doc = db.get("1001")

# (3) Update: Modificación de un documento previamente consultado:
doc["nombre"] = "Toby"
db.save(doc)
# (4) Delete:Borrado de un documento existente
db.delete("1001")

#main del modulo:
if __name__ == "__main__":
    #menu de opciones

    user = "admin"
    pwd = "admin"
    host = "127.0.0.1"
    port = "5984"

    couch_server  = couchdb.Server("http://admin:admin@127.0.0.1:5984/")

    db_name = "refugio_animales"
    print("1. Insertar")
    print("2. Consultar")
    print("3. Actualizar")
    print("4. Eliminar")
    sel = input ("Seleccione uno")
    if(sel=="1"):
        insertar(db)
    elif(sel=="2"):
        consultar(db)
    elif(sel=="3"):
        update(db)
    else:
        delete(db)

        

    global db
    db = couch_server[db_name]