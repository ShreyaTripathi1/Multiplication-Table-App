from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    table = None
    number = None
    error = None
    
    if request.method == 'POST':
        try:
            number = float(request.form['number'])
            table = [(i, number * i) for i in range(1, 11)]
        except ValueError:
            error = "Please enter a valid number."
    
    return render_template('index.html', table=table, number=number, error=error)

if __name__ == '__main__':
    app.run(debug=True)