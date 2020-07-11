import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'premierLeague'
app.config["MONGO_URI"] = 'mongodb+srv://root:Password20@myfirstcluster-ay9fk.mongodb.net/premierLeague?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_clubs')
def get_clubs():
    return render_template("landing-page.html", clubs=mongo.db.Clubs.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)

