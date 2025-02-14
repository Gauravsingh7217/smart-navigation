from flask import Flask, render_template

from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    return render_template('index.html')  # Make sure the template folder is set correctly

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
