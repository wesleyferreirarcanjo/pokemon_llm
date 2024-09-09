from flask import Blueprint, render_template

question_blueprint = Blueprint('question', __name__, template_folder='templates')


@question_blueprint.route('/question')
def question_view():
    return "hello world"