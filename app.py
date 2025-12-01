from flask import Flask, render_template, url_for, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/service_worker.js')
def service_worker():
    return send_from_directory('.', 'service_worker.js')

if __name__ == "__main__":
    app.run(debug=True)
