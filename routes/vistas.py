from flask import jsonify, render_template
from flask import request
from Coneccion import ConeccionDB   

from App import app

from models import Pacientes 
from models import User
from models import Turnos
from models import Profecionales

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/user',methods=['POST'])
def crear_usuario():
    sql="insert into clinica.usuarios(email,clave)values(%s,%s);"
    params=request.args.get("email",""),request.args.get("clave","")
    ConeccionDB.execute_query(sql,params)
    
    return {"msg":"Usuario creado con exito"},201

@app.route('/modificar <int:id_user>',methods=['PUT'])    
def modificar_user(id_usuario):
    sql="update clinica.user set email=%s,clave=%s where id_user=%s"
    params=request.args.get("email",""),request.args.get("clave",""),id_usuario
    ConeccionDB.execute_query(sql,params)
    return {"msg":"Usuario modificado con exito"},200
    
@app.route('/usuarios',methods=['get','post'])
def mostrar_user():
    sql="select id,nombre,correo,password from clinica.usuarios;"
    resultados=ConeccionDB.fetch_all(sql)
    usuarios=[]
    for resultado in resultados:
        usuarios.append({
            'ID':resultado[0],
            'Nombre':resultado[1],
            'correo':resultado[2],
            'password':resultado[3]
            })
    return usuarios,200
@app.route('/profecionales',methods=['GET'])
def mostrar_profecionales():
        sql="select id,nombre,apellido,especialidad,correo,telefono from clinica.profesionales;"
        results=ConeccionDB.fetch_all(sql)
        profesionales=[]
        for result in results:
            profesionales.append({
                'ID':result[0],
                'nombre':result[1],
                'apellido':result[2],
                'especialidad':result[3],
                'correo':result[4],
                'Telefono':result[5]
                })
            
        return profesionales,200
    
        
@app.route('/pacientes')    
def pacientes():
        sql="select id,nombre,apellido,correo,telefono from clinica.pacientes;"
        results=ConeccionDB.fetch_all(sql)
        pacientes=[]
        for result in results:
            pacientes.append({
                 'ID':result[0],
            'nombre':result[1],
            'apellido':result[2],
            'correo':result[3],
            'telefono':result[4]                         
                
                })
        return pacientes,200
@app.route('/pacientest')    
def turnosp():
    sql="select id,paciente_id,profesional_id,fecha,hora,motivo from clinica.turnos;"
    results=ConeccionDB.fetch_all(sql)
    turnos=[]
    for result in results:
        turnos.append({
            'ID':result[0],
                'paciente_id':result[1],
                'profecional_id':result[2],
                'fecha':result[3],
                'hora':result[4],
                'motivo':result[5]
            
            })
    return turnos,200
