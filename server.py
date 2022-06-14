from flask import Flask, render_template, redirect, request
app = Flask(__name__)

poll_info= []


@app.route("/")
def hello_world():
    print(poll_info)
    return render_template("index.html")


@app.route("/get_info", methods=['POST'])
def get_info():
    new_poll= {
        "Name": request.form["name"],
        "Dojo location": request.form["dojo_location"],
        "Language": request.form["language"],
        "Comment": request.form["comment"]
    }
    poll_info.append(new_poll)
    return redirect("/render_info")

@app.route("/render_info")
def render_info():
    return render_template("poll.html", poll_info = poll_info)

@app.route("/home")
def homepage():
    return redirect("/")



if __name__ == "__main__":
    app.run(debug = True)