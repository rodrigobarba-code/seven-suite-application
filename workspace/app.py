# Imports
from config import DevelopmentConfig
# Imports

# Flask import
from flask_restful import Api, Resource
from flask_mysqldb import MySQL
from flask import *
# Flask import

# Models import
from models.model_region import ModelRegion
# Models import

# Entities import
from models.entities.region import Region

# Entities import


app = Flask(__name__)
api = Api(app)

db = MySQL(app)


@app.route('/')
def index():
    return render_template('public/home.html')


@app.route('/routers')
def routers():
    return render_template('public/routers.html')


@app.route('/regions')
def regions():
    return render_template('public/regions.html')

@app.route('/home')
def home():
    return render_template('public/home.html')

@app.route('/sites')
def sites():
    return render_template('public/sites.html')


if __name__ == '__main__':
    app.config.from_object(DevelopmentConfig)
    app.run(port=81, debug=True)
