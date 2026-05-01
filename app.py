from flask import Flask, render_template, request, redirect

app = Flask(__name__)

patients = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/patients', methods=['GET', 'POST'])
def patient():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        disease = request.form['disease']

        patients.append({
            "name": name,
            "age": age,
            "disease": disease
        })

        return redirect('/patients')

    return render_template('patients.html', patients=patients)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', total=len(patients))

if __name__ == "__main__":
    app.run(debug=True)
