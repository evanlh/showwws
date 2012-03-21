from flask import Flask, request, session, render_template
app = Flask(__name__)

@app.route("/")
def showws():
    return render_template('layout.html')

if __name__ == "__main__":
    app.run()

