from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'this is the home page'

if __name__=='01_basic_app':
    app.run(debug=True)