# main.py
from flask import Flask, render_template, jsonify
app = Flask(__name__, static_url_path='')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/profile')
def api_profile():
    data = {}
    data['name'] = "test"
    data['department'] = "test"
    data['avatar'] = "https://img.alicdn.com/tfs/TB1L6tBXQyWBuNjy0FpXXassXXa-80-80.png"
    data['userid'] = 10001
    return jsonify(status='SUCCESS', data=data)


if __name__ == '__main__':
    app.run(host="0.0.0.0",
            port=5000,
            debug=True)
