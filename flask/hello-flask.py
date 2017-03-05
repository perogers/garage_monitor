from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<link rel=\"shortcut icon\" href=\"{{ url_for('static', filename='favicon.ico') }}\">Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
