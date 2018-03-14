import datetime as dt

# Import SQL Alchemy
import sqlalchemy
from sqlalchemy.sql import func
from sqlalchemy.orm import Session

# Import and establish Base for which classes will be constructed 
from sqlalchemy.ext.automap import automap_base

Base = automap_base()

engine = sqlalchemy.create_engine("sqlite:///sql/hawaii.sqlite", echo = False)
session = Session(bind = engine)

Base.prepare(engine, reflect = True)

engine = sqlalchemy.create_engine("sqlite:///sql/hawaii.sqlite", echo = False)
session = Session(bind = engine)

Measurement = Base.classes.prcp_measurements
Station = Base.classes.stations
Temp_Measurement = Base.classes.temp_measurements

test_1 = "test"
test_2 = session.query(Station)

data_first_date = session.query(Measurement.date).order_by(Measurement.date).first()

data_last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()

analysis_length = 365
analysis_end = dt.datetime.strptime(data_last_date[0] , "%Y-%m-%d")
analysis_end_str = data_last_date[0]
analysis_begin = dt.datetime.strptime(data_last_date[0] , "%Y-%m-%d") - dt.timedelta(analysis_length)

prcp_results = session.query(Measurement)\
    .filter(Measurement.date > analysis_begin)\
    .filter(Measurement.date < analysis_end)
    
temp_results = session.query(Temp_Measurement)\
    .filter(Temp_Measurement.date > analysis_begin)\
    .filter(Temp_Measurement.date < analysis_end)

caps = "  }   ]  "
    
def precipitation():
    prcp_dict = {}
    for result in prcp_results:
        prcp_dict[result.date] = result.prcp       
    return(prcp_dict)

def stations():
    station_list = []
    results = session.query(Station.station_id)
    for station in results:
        station_list.append(station.station_id)
    return station_list
    
def tobs():
    temp_data = {}
    for result in temp_results:
        temp_data[result.measurement_id] = {"date": result.date, "station_id": result.station_id, "temp": result.tobs}
   
    return temp_data
    
def temp_for_range(start_date, end_date = analysis_end_str):
    try:
        start_date_dt = dt.datetime.strptime(start_date , "%Y-%m-%d")
    except ValueError:
        return {"14014": "Start Date value needs to be written YYYY-MM-DD"}
    try:
        end_date_dt = dt.datetime.strptime(end_date , "%Y-%m-%d")
    except ValueError:
        return {"14014": "End Date value needs to be written YYYY-MM-DD"}
    temps = session.query(func.max(Temp_Measurement.tobs).label("TMAX"),\
                         func.min(Temp_Measurement.tobs).label("TMIN"),\
                         func.avg(Temp_Measurement.tobs).label("TAVG"))\
        .filter(Temp_Measurement.date >= start_date_dt)\
        .filter(Temp_Measurement.date <= end_date_dt).all()[0]
    
    return {"TMAX": temps[0], "TMIN": temps[1],
            "TAVG": float("{0:.1f}".format(temps[2])),
            "start_date": start_date, "end_date": end_date}
    
    
    
    
    
    
    
    
    
    
    
    
    