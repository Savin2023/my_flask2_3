from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
  
@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        state = request.form.get('state')
        number = request.form.get('number')
        return redirect(url_for('form_out', state=state, number=number))
    return render_template('index.html')

  
@app.route('/form_out')
def form_out():
    state = request.args.get('state', None)
    number = request.args.get('number', None)
    return render_template('form_out.html', state=state, number=number)  


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
    #app.run()