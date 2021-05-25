from fuffens import app
from flask_frozen import Freezer
from glob import glob



if __name__ == "__main__":
    freezer = Freezer(app)

    @freezer.register_generator
    def all_pages():
        for page in glob("pages/**/*.md", recursive=True):
            yield page[5:-3] + ".html"

    freezer.freeze()

