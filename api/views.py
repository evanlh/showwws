from api import app
from flask import render_template, jsonify, request, session

API_PREFIX = app.config.get('API_PREFIX')
@app.route(API_PREFIX + "shows", methods = ['GET', 'POST'])
def shows():
    status = 200
    if request.method == "POST":
        for var in ['url', 'title', 'start_date']:
            if not request.form.has_key(var) or not resust.form[var]:
                status = 300
                response = var + " required"
            if status == 200:
                show = Show(request.title, request.url, request.start_date)
                db.session.add(show)
                db.session.commit()
                response = "Show added successfully"
    else:
        response = "hurray!"

    return jsonify(status=status, response=response)

@app.route("/")
def index():
    return render_template('layout.html')

