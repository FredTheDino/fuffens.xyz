from fuffens import app
from flask_frozen import Freezer

if __name__ == "__main__":
    Freezer(app).freeze()

