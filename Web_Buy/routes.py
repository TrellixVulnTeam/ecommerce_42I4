from flask import Flask, Blueprint, session, render_template, request, redirect, jsonify
from routes import register_blueprint
app = Flask(__name__)
app = register_blueprint(app)
#from flask_session import Session

#SESSION_TYPE = 'filesystem'
#app.config.from_object(__name__)
#Session(app)
#from uuid import uuid4


@app.route('/')
def home():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)