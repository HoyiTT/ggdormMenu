from flask import Flask, render_template,send_file

app = Flask(__name__)

@app.route('/manifest.json')
def serve_manifest():
    return send_file('manifest.json', mimetype='application/manifest+json')

@app.route('/static/sw.js')
def serve_sw():
    return send_file('static/sw.js', mimetype='application/javascript')


@app.route('/')
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

