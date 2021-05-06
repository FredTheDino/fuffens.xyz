import marko
from flask import Flask, render_template
app = Flask(__name__)

def render_content(lines):
    lines = "".join(f"<h2>{line[1:-1]}</h2>\n\n" if line.startswith("# ") else line for line in lines).strip()
    lines.replace(" ", "\n</p>blargh<p>\n")
    return lines + "</p>"

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
def hello_world():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_med("about.med")


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, static="static")
