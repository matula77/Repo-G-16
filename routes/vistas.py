from flask import jsonify, render_template
from flask import request

from App import app

from models import Pacientes 
from models import User
from models import turnos
from models import profecionales

@app.route('/')
def inicio():
    return render_template('index.html')
