from flask import Flask, render_template,request
from Coneccion import ConeccionDB    


app = Flask(__name__)

from routes.vistas import *

    
if __name__=="__name__":
    app.run(debug=True)
    
    
    