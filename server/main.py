from datetime import datetime

from flask import Flask, Response, request, redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    to = request.args.get('to')
    redirect_to = redirect(to, code=302)
    response = app.make_response(redirect_to)
    response.set_cookie('tracking_id', value=str(datetime.utcnow()))

    return response



@app.route('/test')
def test():
    cookie = request.cookies.get("tracking_id")

    text = "tracking_id=%s now=%s" % (cookie, datetime.utcnow())
    response = Response(response=text)

    return response
