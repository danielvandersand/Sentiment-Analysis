from flask import Flask
from views import views
from flask_sqlalchemy import SQLAlchemy
#from flask_login import UserMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'  # SQLite database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db = SQLAlchemy(app)
app.register_blueprint(views, url_prefix='/')
app.app_context().push()

if __name__ == '__main__':
    app.run(debug=True, port=8000)



