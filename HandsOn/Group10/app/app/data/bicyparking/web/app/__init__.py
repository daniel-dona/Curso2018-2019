# Import flask and template operators
from flask import Flask, render_template

# Import Bootstrap
from flask_bootstrap import Bootstrap

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

Bootstrap(app)

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (auth)
from app.public.controllers import public as public
from app.locator.controllers import locator as locator

# Register blueprint(s)
app.register_blueprint(public)
app.register_blueprint(locator)
# app.register_blueprint(xyz_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()

