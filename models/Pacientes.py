import mysql.connector

from App import pacientes
from ..Coneccion import ConeccionDB

class Pacientes:
    def __init__(self,id,nombre,apellido,fecha_nacimiento,correo,telefono,direccion):
        self.id=id
        self.nombre=nombre
        self.apellido=apellido
        self.fecha_nacimiento=fecha_nacimiento
        self.correo=correo
        self.telefono=telefono
        self.direccion=direccion
    
       
        
    def crearPaciente(cls,paciente)    :
        try:
            coneccion=ConeccionDB()
            sql="""INSERT INTO clinica.pacientes (nombre,apellido,fecha_nacimiento,correo,telefono,direccion)VALUES(%s,%s,%s,%s,%s);"""
            val=(paciente.nombre,paciente.apellido,paciente.fecha_nacimiento,paciente.correo,paciente.telefono,paciente.direccion)            
            coneccion.execute_query(sql,val)
            coneccion.close_coneccion()
        except Exception as e:
            print(e)
            
    def consultarPaciente(cls,id)        :
        try:
            coneccion=ConeccionDB()
            sql="""SELECT * FROM clinica.pacientes WHERE id=%s"""
            val=(id)
            paciente=coneccion.execute_query(sql,val)
            
            coneccion.close_coneccion()
            return paciente
        except Exception as e:
            print(e)
    def mostrarPacientes(cls)        :
        coneccion=ConeccionDB()
        sql='SELECT * FROM clinica.pacientes;'
        resultado=coneccion.execute_query(sql)
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
    def modificarPacientes(cls,id)    :
        try:
            coneccion=ConeccionDB()
            sql="""UPDATE clinica.pacientes SET nombre=%s,apellido=%s,fecha_n
            acimiento=%s,correo=%s,telefono=%s,direccion=%s WHERE id=%s"""
            val=(pacientes.nombre,pacientes.apellido,pacientes.fecha_nacimiento,pacientes.correo,pacientes.telefono,pacientes.direccion,id)
            coneccion.execute_query(sql,val)
            coneccion.close_coneccion()
        except Exception as e:
            print(e)
    def eliminarPaciente(cls,id)        :
        try:
            coneccion=ConeccionDB()
            sql="""DELETE FROM clinica.pacientes WHERE id=%s"""
            val=(id)
            coneccion.execute_query(sql,val)
            coneccion.close_coneccion()
        except Exception as e:
            print(e)
            
            
        
        
Pacientes.mostrarPacientes()        
    
    
    
   