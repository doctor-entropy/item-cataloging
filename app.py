from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Hardware, Item, Images

engine = create_engine('sqlite:///hardware.db', connect_args={'check_same_thread':False})
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def welcome_page():

	hardware = session.query(Hardware).filter_by().all()

	return render_template('welcome.html', hardware=hardware)

@app.route('/<int:hardware_id>')
def items_page(hardware_id):

	items = session.query(Item).filter_by(hardware_id=hardware_id).all()

	return render_template('items.html', items=items)

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=8888)
