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
<<<<<<< HEAD
    app.run(debug=True)
=======
    app.run(debug=True)
>>>>>>> 9e62bb2b9a96479aa3d4eb5b4f3bfc11e757998d
