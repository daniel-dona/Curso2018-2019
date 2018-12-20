import os

# Statement for enabling the development environment
DEBUG = True

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'mysql://bicy:parking@db/bicyparking?charset=utf8'


# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

WTF_CSRF_ENABLED = True

WTF_CSRF_SECRET_KEY = 'a random string'

# Secret key for signing cookies
SECRET_KEY = '@A:e^R2}mRa5{MM~Tj.)A::JQ!N&9>8Pqr7,#?74nJQT;J9#`**EtCCQ([tyBV6{'
SECURITY_PASSWORD_SALT = '];#heT}9#.j"L?Z?AeD!rtZm6%+$x_>8BHL:>+xQ6Vftg6yXs]vZ<J5Pts+8w\e&'


HOSTNAME = 'http://localhost:8080'


