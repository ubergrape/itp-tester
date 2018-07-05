from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    to = request.args.get('to')
    redirect_to = redirect(to, code=302)
    response = app.make_response(redirect_to)
    response.set_cookie('tracking_id', value='314159265359')

    return response
