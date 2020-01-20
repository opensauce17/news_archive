from flask import render_template, request, url_for, redirect, message_flashed, flash, jsonify, session, Blueprint


main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():

    return render_template('main/index.html')


@main.route('/country', methods=['GET', 'POST'])
def country():

    country = request.args.get('country')

    if country == "za":
        return render_template('za/index.html')

    if country == "us":
        return render_template('za/index.html')


