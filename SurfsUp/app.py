#import dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
from flask import Flask,jsonify
import numpy as np
import datetime as dt

# create engine to hawaii.sqlite
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#create an app
app = Flask(__name__)



# Homepage route
@app.route("/")
def home():
    """List all available routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
    )
# precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():  
    #Convert the query results to a dictionary using `date` 
    # as the key and `prcp` as the value"""
    #creating a session link and querying the db   
    session = Session(engine)
    rain_data = session.query(Measurement.date, func.avg(Measurement.prcp))\
        .group_by(Measurement.date)\
        .order_by(Measurement.date)\
        .all()
    # creat an empty list and date as key and prcp as value       
    rain_dict = {}
    for row in rain_data:
        date = row[0]
        prcp = row[1]
        rain_dict[date] = prcp
    #Return the json representation of the dictionary
    return jsonify(rain_dict)




# stations route
@app.route("/api/v1.0/stations")
def stations():  
    #creating a session link and querying the db   
    session = Session(engine)
    #query for a list of the stations
    station_list = session.query(Station.station).all()
    # Convert list of tuples into normal list
    stations = list(np.ravel(station_list))
    #Return the json representation
    return jsonify(stations)



@app.route("/api/v1.0/tobs")
def tobs(): 
    #creating a session link and querying the db 
    session = Session(engine)
    #creating variable for previous year
    last_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    #Query the dates and temperature observations of the most active station for the previous year of data
    active_station = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.station == 'USC00519281').filter(Measurement.date >= last_year).all()
    # Convert list of tuples into normal list
    most_active = list(np.ravel(active_station))
    #Return the json representation
    return jsonify(most_active)


@app.route("/api/v1.0/<start>")
def start_date(start=None): 
    start = dt.datetime.strptime(start, "%m-%d-%Y")
    #creating a session link and querying the db
    session = Session(engine)
    ##creating a query that returns the start date
    query = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))\
    .group_by(Measurement.date).order_by(Measurement.date).filter(Measurement.date >= start).all()
    # Convert list of tuples into normal list
    query = list(np.ravel(query))
    #Return the json representation
    return jsonify(query)


@app.route("/api/v1.0/<start>/<end>")
def start_end(start=None, end=None): 
    start = dt.datetime.strptime(start, "%m-%d-%Y")
    end = dt.datetime.strptime(end, "%m-%d-%Y")
    #creating a session link and querying the db
    session = Session(engine)
    #creating a query that returns the start and end date entered
    query = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))\
    .group_by(Measurement.date).order_by(Measurement.date).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    # Convert list of tuples into normal list
    query = list(np.ravel(query))
    #Return the json representation
    return jsonify(query)

if __name__ == "__main__":
    app.run(debug=True)