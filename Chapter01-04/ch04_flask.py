from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello,Flask!"

@app.route('/ads/<int:ads_id>')
def show_post(ads_id):    
    return 'Adversiting id %d' % ads_id

