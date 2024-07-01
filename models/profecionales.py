
from Coneccion import ConeccionDB

class Profesionales:
    def __init__(self,id,nombre,apellido,especialidad ,correo,telefono ):
        self.id=id
        self.nombre=nombre
        self.apellido=apellido
        self.especialidad=especialidad
        self.correo=correo
        self.telefono=telefono
        
        
        @classmethod
        def insertarProfe(cls,profesional
        ):
            try:
               coneccion=ConeccionDB
                        
               sql="INSERT INTO clinica.profecionales (nombre,apellido,especialidad,correo,telefono)VALUES ('%s','%s','%s','%s','%s');"
               val=(profesional
               .nombre,profesional
               .apellido,profesional
               .especialidad,profesional
               .correo,profesional
               .telefono)
               coneccion.execute_query(sql,val)
               coneccion.commit()
               return True
            except Exception as e:
                print(e)
        @classmethod        
        def modificarProfe(self,prof):
            try:
                coneccion=ConeccionDB
                sql="UPDATE clinica.profecionales SET nombre=%s,apellido=%s,especialidad=%s,correo=%s,telefono=%s WHERE id=%s;"    
                val=(prof.nombre,prof.apellido,prof.especialidad,prof.correo,prof.telefono,prof.id)
                    
                coneccion.execute_query(sql,val)
                coneccion.commit()
                return True
            except Exception as e:
                print(e)      
        @classmethod
        def consultarProfe(cls,id):
            sql="select * from clinica.profesional where id=%s;"
            val=(id)
            resultado=ConeccionDB.execute.fetch_one(sql,val)
            if resultado is not None:
                return{
                    "id":resultado[0],
                    "nombre":resultado[1],
                    "apellido":resultado[2],
                    "especialidad":resultado[3],
                    "correo":resultado[4],
                    "telefono":resultado[5]
                    
                }
            else:
                return None
            
        @classmethod
        def todosProfe(cls):
            query='SELECT * FROM clinica.profecionales ;'    
            coneccion=ConeccionDB()
            coneccion.execute_query.fetch_all(query)
            return True
        @classmethod      
        def eliminarProfe(cls,id):
            coneccion=ConeccionDB()
            sql="DELETE FROM clinica.profecionales WHERE id=%s"
            val=(id)
            coneccion.execute_query(sql,val)
            return True
Profesionales.todosProfe()
Profesionales.consultarProfe(1)
            