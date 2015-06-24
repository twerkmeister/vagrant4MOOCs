from flask import Flask, render_template, request
app = Flask(__name__)

# TODO @login_required

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/get_vagrantfile')
def get_vagrant_file():
    # get parameters from url parameter: ?username=<username>&key=<key>
    username = request.args.get('username', 'haxxor')
    key = request.args.get('key', 'tz-safe-password')
    return render_template('Python-101/Vagrantfile', username=username,
            key=key)

@app.route('/get_vagrantfile_url/<username>/<key>')
def get_vagrant_file_url(username, key):
    # get parameters from path
    return render_template('Python-101/Vagrantfile', username=username, key=key)

if __name__ == '__main__':
    app.secret_key =
    b"\xe9w,3\xbdIQ\x96}V\x01\xcb\xc2)\xfd\xddphg^%m\xcc\xdb6\x07\x00:h\xed\xce\xba\xf0\xf5\xa1\x8e\xde*\xafa\xcf\xe9\xc8y1\xbb\x07\x08\xcf\x92cYG\xf5\x0e\xca_\xc5\xf8\xf8\xc6\xf5\x9c.Y\xd7\xd7\xa0\xa0\xf7\x13\x8f\xfc\xf3jQ\\\xb8\x8az\xf7~\xaa\xd2\xd4lc\xcc\xb3\xc0D\xbc9\x9av\xf9\x1f:\x01'"
    app.run(host='0.0.0.0', port=5000, debug=True)

