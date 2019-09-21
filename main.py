from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

if __name__ == '__main__':
    #if code is changed, the web app will automatically reload
    app.run(host='127.0.0.1', port=8080, debug='true')
