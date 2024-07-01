from Coneccion import ConeccionDB

class Turnos:
    def __init__(self,id,paciente_id,profecional_id,fecha,hora,motivo):
        self.id=id
        self.paciente_id=paciente_id
        self.profecional_id=profecional_id
        self.fecha=fecha
        self.hora=hora
        self.motivo=motivo
        
        def insertarTurno(self, turno):
            coneccion=ConeccionDB()
            sql = "INSERT INTO clinica.turnos (paciente_id,Medico_id,fecha, hora, estado) VALUES (%s, %s, %s, %s,%s)"
            val = (turno.paciente_id, turno.profecional_id,turno.fecha, turno.hora,turno.estado)
            coneccion.execute_query(sql, val)
        def modificarTurno(cls,turnos)    :
            sql = "UPDATE clinica.turnos SET paciente_id=%s,Medico_id=%s,fecha=%s, hora=%s, estado=%s WHERE id=%s"
            val = (turnos.paciente_id,id.profecional_is,turnos.fecha,turnos.hora,turnos.motivo,turnos.id)
            self.conexion.cursor.execute(sql, val)
            
        def mostrarTurnos(cls):
            coneccion=ConeccionDB()
            sql = "SELECT * FROM clinica.turnos"
            self.conexion.cursor.execute(sql)
            turnos=coneccion.fetchall(sql)
            turno=[]
            for(turno in turnos):
                turno.append(Turnos(turno[0],turno[1],turno[2])
                                                            
             
        
            
            
            