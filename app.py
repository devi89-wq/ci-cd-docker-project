from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Render a beautiful HTML page instead of plain text
    return render_template('index.html')

if __name__ == '__main__':
    # Running the app on 0.0.0.0 so it can be accessed from outside the container
    app.run(host='0.0.0.0', port=5000)
def test_basic():
assert 1 + 1 == 2
