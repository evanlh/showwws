from flask import Flask, request, session, jsonify, render_template
app = Flask(__name__)

@app.route("/v1/shows", methods = ['GET', 'POST'])
def shows():
    if request.method == "POST":
        pass
    else:
        pass

@app.route("/")
def index():
    return render_template('layout.html')

if __name__ == "__main__":
    app.run()

