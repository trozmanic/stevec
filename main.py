from flask import Flask, render_template, redirect, url_for, request, jsonify

list = []

reviewList = []

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/newCounter")
def newCounter():
    info = request.args.get('count')
    global list
    global reviewList = []

    if info == "new":
        x = len(list)
        list.append(0)
        reviewList.append(0)
        return jsonify(result=x)

@app.route("/minus")
def minus():
    global list
    index =int(request.args.get('index'))
    list[index] = list[index] - 1

    return jsonify(result=list[index])

@app.route("/plus")
def plus():
    global list
    index =int(request.args.get('index'))
    list[index] = list[index] + 1

    return jsonify(result=list[index])

@app.route("/refresh")
def refresh():
    global list
    index =int(request.args.get('index'))

    return jsonify(result=list[index])

@app.route("/test/<int:value>")
def test(value):
    global list
    x = list[value]
    return render_template("counter.html", variable=x, variable2=value)
    
'''
@app.route("/review/<int:id>")
def review(id):

@app.route("/end/<int:id>/<int:vhod>")
def end(id, vhod):
    global list
'''

if __name__ == "__main__":
    app.run(debug=True)
