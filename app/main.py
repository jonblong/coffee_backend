from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required
from . import db
from .models import Drink, DrinkType

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/add_drink')
@login_required
def add_drink():
    drink_types = DrinkType.query.all()
    return render_template('add_drink.html', drinktypes=drink_types)

@main.route('/add_drink', methods=['POST'])
@login_required
def add_drink_post():
    drinktype_id = request.form.get('drink_type_id')
    note = request.form.get('note')
    new_drink = Drink(drinktype_id=drinktype_id, note=note)

    db.session.add(new_drink)
    db.session.commit()
    
    return render_template('index.html')

@main.route('/add_drinktype')
@login_required
def add_drinktype():
    return render_template('add_drinktype.html')

@main.route('/add_drinktype', methods=['POST'])
@login_required
def add_drinktype_post():
    name = request.form.get('name')

    drink_type = DrinkType.query.filter_by(name=name).first()

    if drink_type:
        flash('Drink type already exists!')
        return redirect(url_for('main.add_drinktype'))

    new_drink_type = DrinkType(name=name)

    db.session.add(new_drink_type)
    db.session.commit()

    return redirect(url_for('main.add_drink'))

@main.route('/get_drinks')
def get_drinks():
    drinks = Drink.query.all()

    return jsonify(json_list = [d.toJSON() for d in drinks])