from flask import Flask, render_template, request
from sqlalchemy import create_engine
import sqlalchemy 
import json
app = Flask(__name__	,template_folder='template')


engine = create_engine('postgresql://postgres:newpassword@localhost:5432/postgres')
meta = sqlalchemy.MetaData(bind=engine, reflect=True)





meta = MetaData(db)  
film_table = Table('films', meta,  
                       Column('title', String),
                       Column('director', String),
                       Column('year', String))

with db.connect() as conn:

    # Create
    film_table.create()
    insert_statement = film_table.insert().values(title="Doctor Strange", director="Scott Derrickson", year="2016")
    conn.execute(insert_statement)

    # Read
    select_statement = film_table.select()
    result_set = conn.execute(select_statement)
    for r in result_set:
        print(r)

    # Update
    update_statement = film_table.update().where(film_table.c.year=="2016").values(title = "Some2016Film")
    conn.execute(update_statement)

    # Delete
    delete_statement = film_table.delete().where(film_table.c.year == "2016")
    conn.execute(delete_statement)








   curl localhost:5000/insert -d @data.json -H 'Content-Type: application/json'
