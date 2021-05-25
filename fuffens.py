import marko
from glob import glob
from flask import Flask, render_template, redirect
app = Flask(__name__)

def parse(src):
    with open(src) as f:
        lines = f.readlines()
        content = []
        variables = {}
        for line in lines:
            if not line.startswith("/"):
                content.append(line)
            if line.startswith("///"):
                _, tag, rest = line.split(" ", 2)
                variables[tag[:-1]] = rest.strip()

        if "author" not in variables:
            variables["author"] = "Edvard Thörnros"

        assert("title" in variables)
        assert("first" in variables)
        assert("last" in variables)

        variables["content"] = marko.convert("".join(content))
        return variables

def render_med(src, **args):
    variables = parse(src)
    template = variables.get("template") or "simple.html"
    return render_template(template, **variables, **args)


@app.route('/favicon.ico')
def favicon():
    return redirect("static/favicon.ico", 301)

@app.route('/')
def index():
    return render_med("pages/about.md")

@app.route('/thoughts.html')
def thoughts():
    def parse_tought(src):
        variables = parse(src)
        variables["path"] = f"thoughts/{src.split('/')[-1][:-2]}html"
        return variables

    t = map(parse_tought, glob("pages/thoughts/*.md"))
    return render_med("pages/thoughts.md", thoughts=list(t))

@app.route('/<a>/<b>.html')
def other_nested(a, b):
    return render_med(f"pages/{a}/{b}.md")

@app.route('/<a>.html')
def other(a):
    return render_med(f"pages/{a}.md")

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, static="static")
