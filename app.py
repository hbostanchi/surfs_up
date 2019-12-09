# Import dependencies.
import pandas as pd
import numpy as np
import datetime as dt
# Get the dependencies we need for SQLAlchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
# Add the code to import the dependencies that we need for Flask
from flask import Flask, jsonify
# Set up our database engine for the Flask application
engine = create_engine("sqlite:///hawaii.sqlite")
# Reflect the database into our classes.
Base = automap_base()
# Reflect the database
Base.prepare(engine, reflect=True)
# Create a variable for each of the classes so that we can reference them later
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create a session link from Python to our database
session = Session(engine)
# Define our Flask app
app = Flask(__name__)
# Define the welcome route


@app.route("/")
def welcome():
    return(
        f"Welcome to the Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start/end<br/>"
)

@app.route("/api/v1.0/precipitation")
def precipitation():
        prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
        precipitation = session.query(Measurement.date, Measurement.prcp).\
		filter(Measurement.date >= prev_year).all()
        precip = {date: prcp for date, prcp in precipitation}
        return jsonify(precip)

@app.route("/api/v1.0/stations")
def stations():
        results = session.query(Station.station).all()
        stations = list(np.ravel(results))
        return jsonify(stations)



@app.route("/api/v1.0/tobs")
def temp_monthly():
        prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

        results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()

        temps = list(np.ravel(results))
        return jsonify(temps)

        #"/api/v1.0/temp/2019-12-06/"
        #"/api/v1.0/temp/2019-12-06/2020-12-06"
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>") 
def stats(start, end=None):

        sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs),  func.max(Measurement.tobs)]

        #If the user, used a URL, that matched the route @app.route("/api/v1.0/temp/<start>")
        # That meanst he suer did not provide an <end> variable; which means the Python `end` parrameter, will have a *default* value
        # What is that default value? None; so if end is None; then "not end" will 

#(not None) ---> True
#(None is not None) --> False
        if not end:
                results = session.query(*sel).\
                        filter(Measurement.date >= start).\
                        all()
                temps = list(np.ravel(results))
                return jsonify(temps)
        #end is not None
        else:
                results = session.query(*sel).\
                                filter(Measurement.date >= start).\
                                filter(Measurement.date <= end).\
                                all()
                temps = list(np.ravel(results))
                return jsonify(temps)

