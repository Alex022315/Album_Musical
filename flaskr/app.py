from flaskr import create_app
from .modelos import db, Cancion, Usuario, Album, Medio
from flask_restful import Api
from .modelos import AlbumSchema
from .vistas import VistaCanciones, VistaCancion
import enum
from flaskr .vistas import VistaCanciones


@app.route('/lista_canciones')
def lista_canciones():
    canciones = [cancion_schema.dump(cancion) for cancion in Cancion.query.all()]
    return render_template('./vistas/VistaCanciones.html', canciones=canciones)



app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api= Api(app)
api.add_resource(VistaCanciones,'/canciones')
api.add_resource(VistaCancion,'/canciones/<int:id_cancion>')



