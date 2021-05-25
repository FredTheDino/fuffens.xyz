from fuffens import app
from flask_frozen import Freezer
from glob import glob



if __name__ == "__main__":
    freezer = Freezer(app)

    @freezer.register_generator
    def other():
        for page in glob("pages/*.md"):
            yield { 'a': page[6:-3] }

    @freezer.register_generator
    def other_nested():
        for page in glob("pages/*/*.md"):
            a, b = page[6:-3].split("/")
            yield { 'a': a, 'b': b }

    freezer.freeze()

