from flask import Flask, render_template

app = Flask(__name__)

@app.route('/exito')
def exito():
    return render_template('exito.html')

if __name__ == '__main__':
    app.run()