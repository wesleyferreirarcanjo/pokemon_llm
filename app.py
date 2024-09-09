from flask import Flask
from question.views import question_blueprint

app = Flask(__name__)
app.register_blueprint(question_blueprint)

if __name__ == '__main__':
    app.run(debug=True)