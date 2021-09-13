from flask import Flask, Blueprint, session, render_template, request, redirect, jsonify
from routes import register_blueprint
# from flask.ext.session import Session

app = Flask(__name__)
app.secret_key = '6e394b70-c269-4fd1-8dfc-d34665270296'
app = register_blueprint(app)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
