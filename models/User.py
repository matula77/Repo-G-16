from Coneccion import ConeccionDB

class User:
    def __init__(self,id,nombre,correo,password ):
        self.id=id
        self.nombre=nombre
        self.correo=correo
        self.password=password
        def __str__(self):
            return f"User(id={self.id},nombre={self.nombre},correo={self.correo}"
        
    @classmethod
    def crear_usuario(self,usuario)    :
        try:
            coneccion=ConeccionDB.get_coneccion()
            sql="INSERT INTO usuario (nombre,correo,password) VALUES (%s,%s,%s);"
            val=(usuario.nombre,usuario.correo,usuario.password)
            coneccion.execute_query(sql,val)
            
            return True
        except Exception as e:
            print(e)
            
    @classmethod
    def consultar_user(id)        :
        coneccion=ConeccionDB.get_coneccion()
        sql="SELECT * FROM usuario WHERE id=%s;"
        val=(id)
        coneccion.execute_query(sql,val)
        return True
        
        
    @classmethod        
    def todos_user():
        query='SELECT actor_id,first_name,last_name,last_update FROM sakila.actor ;'    
        coneccion=ConeccionDB.get_coneccion()
        coneccion.execute_query(query)
        return True

    @classmethod        
    def modificar_user(self,user)            :
        try:
            coneccion=ConeccionDB.get_coneccion()
            sql="UPDATE usuario SET nombre=%s,correo=%s,password=%s WHERE id=%s"    
            val=(user.nombre,user.correo,user.password,user.id)
            coneccion.execute_query(sql,val)
            return True
        except Exception as e:
            print(e)
    @classmethod
    def eliminar_user(self,id)            :
        
            coneccion=ConeccionDB.get_coneccion()
            sql="DELETE FROM usuario WHERE id=%s"
            val=(id)
            coneccion.execute_query(sql,val)
            return True
    
    consultar_user(1)    
    todos_user()
    crear_usuario('miguel','example@correo.com',123)
            
    
    