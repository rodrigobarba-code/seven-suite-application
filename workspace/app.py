from flask_restful import Api, Resource
from flask_mysqldb import MySQL
from flask import *

app = Flask(__name__)
api = Api(app)
@app.route('/')
def index():
    return render_template('public/home.html')

@app.route('/routers')
def routers():
    return render_template('public/routers.html')

if __name__ == '__main__':
    app.run(debug=True)