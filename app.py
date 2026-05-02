from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/patients')
def patients():
    return render_template('patient.html')

if __name__ == "__main__":
    app.run(debug=True)
    # demo change