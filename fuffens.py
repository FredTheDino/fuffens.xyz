import marko
from flask import Flask, render_template
app = Flask(__name__)

def render_med(src):
    with open(f"pages/{src}") as f:
        lines = f.readlines()
        content = []
        variables = {}
        for line in lines:
            if not line.startswith("/"):
                content.append(line)
            if line.startswith("///"):
                _, tag, rest = line.split(" ", 2)
                variables[tag[:-1]] = rest.strip()

        variables["content"] = marko.convert("".join(content))
        # TODO(ed): Check for expected tags
        return render_template(variables["template"] or "base.html", **variables)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<other>')
def other(other):
    return render_med(other + ".md")

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, static="static")
