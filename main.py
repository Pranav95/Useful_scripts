from flask import Flask 
import psycopg2
from flask import request
from flask_sqlalchemy import SQLAlchemy
from ast import literal_eval

from flask import json
app = Flask(__name__)




app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:newpassword@localhost:5432/postgres'
db = SQLAlchemy(app)


class Orders(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.String(70), primary_key=True)
    product_name = db.Column(db.String(100))
    is_shipped = db.Column(db.Boolean)
    inventory = db.Column(db.Integer)

    def __init__(self, id, name, is_shipped, inventory):
        self.id = id
        self.product_name = name
        self.is_shipped = is_shipped
        self.inventory = inventory
        





@app.route('/insert',methods = ['POST'])
def postDatabase():
	if request.method == 'POST':
		try:

			data = request.data
			data = json.loads(data)	
			print("HERE")
			print(data)
			
			# for d in data:
			# 	try:
			# 		order = Orders(id = d['id'],name = d['product_name'],is_shipped = d['is_shipped'],inventory = d['inventory'])
			# 		#order  = Orders.query.filter_by(id=d['id']).first()
			# 		db.session.add(order)
			# 	except Exception as e:
			# 		print(str(e))
			# 		return "Failed to insert"
		except Exception as e:
			print(str(e))
	db.session.commit()
	return "YES"

@app.route('/')
def mainFunction():
	return "HELLO"



if __name__ == "__main__":
	app.run()	