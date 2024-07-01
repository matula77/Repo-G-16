import mysql.connector     
from mysql.connector.errors import DatabaseError  



class ConeccionDB:
    _coneccion=None
    @classmethod
    def get_coneccion(cls):
        if cls._coneccion is None:
            try:
                cls._coneccion=mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                port='3306',
                password='123456',
                database='clinica'
                )
                print("coneccion exitosa")
            except DatabaseError as err:
                print('Error al conectar a la base de datos',err)    
        return cls._coneccion
    
    @classmethod
    def execute_query(cls,query,params=None):
        cursor=cls.get_coneccion().cursor()
        cursor.execute(query,params)
        cls._coneccion.commit()
        return cursor
    
    @classmethod
    def fetch_one(cls,query,params=None):
        cursor=cls.get_coneccion().cursor()
        cursor.execute(query,params)
        return cursor.fetchone()
    @classmethod
    def fetch_all(cls,query,params=None):
        cursor=cls.get_coneccion().cursor()
        cursor.execute(query,params)
        return cursor.fetchall()
    @classmethod
    def close_coneccion(cls):
        if cls._coneccion is not None:
            cls._coneccion.close()
            print("Coneccion terminada")
            cls._coneccion=None
            
            
   
        
        
ConeccionDB.get_coneccion()

ConeccionDB.close_coneccion()
    
            
        
        
        
        