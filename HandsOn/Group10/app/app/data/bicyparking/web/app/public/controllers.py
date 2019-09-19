# Import flask dependencies
from flask import Blueprint, request, render_template, g, session

# Define the blueprint: 'auth', set its url prefix: app.url/auth
public = Blueprint('public', __name__, url_prefix='/')


# Set the route and accepted methods
@public.route('/', methods=['GET'])
def index():
    return render_template("public/index.html",)


