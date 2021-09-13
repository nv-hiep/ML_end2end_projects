from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("model/RFRegressor_Model_AirFare_Prediction.pkl", "rb"))


sources = {0:"Delhi", 1:"Kolkata", 2:"Mumbai", 3:"Chennai"}
source = {'selected': 0}

destinations = {0:"Cochin", 1:"Delhi", 2:"New Delhi", 3:"Hyderabad", 4:"Kolkata"}
destination = {'selected': 0}

nstops = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4"}
nstop = {'selected': 0}

airlines = {3:"Jet Airways", 2:"IndiGo", 0:"Air India", 5:"Multiple carriers",
            7:"SpiceJet", 9:"Vistara", 11:"Air Asia", 1:"GoAir",
            6:"Multiple carriers Premium economy", 4:"Jet Airways Business",
            10:"Vistara Premium economy", 8:"Trujet"}  
airline = {'selected': 0}

dep_time = ""
arr_time = ""


@app.route("/")
@cross_origin()
def home():
    return render_template("home.html",
        sources = sources, source = source,
        destinations = destinations, destination = destination,
        nstops = nstops, nstop = nstop,
        airlines = airlines, airline = airline,
        dep_time = dep_time, arr_time = arr_time)



@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        dep_time = request.form["Dep_Time"]
        arr_time = request.form["Arrival_Time"]

        # flight_day
        flight_day = int(pd.to_datetime(dep_time, format="%Y-%m-%dT%H:%M").day)
        flight_month = int(pd.to_datetime(dep_time, format ="%Y-%m-%dT%H:%M").month)
        flight_dayofweek = int(pd.to_datetime(dep_time, format ="%Y-%m-%dT%H:%M").dayofweek)

        # Departure
        dep_hour = int(pd.to_datetime(dep_time, format ="%Y-%m-%dT%H:%M").hour)
        dep_min = int(pd.to_datetime(dep_time, format ="%Y-%m-%dT%H:%M").minute)


        # Arrival
        arr_hour = int(pd.to_datetime(arr_time, format ="%Y-%m-%dT%H:%M").hour)
        arr_min = int(pd.to_datetime(arr_time, format ="%Y-%m-%dT%H:%M").minute)

        # Duration
        duration_hours = pd.Timedelta(pd.to_datetime(arr_time, format ="%Y-%m-%dT%H:%M") - pd.to_datetime(dep_time, format ="%Y-%m-%dT%H:%M")).seconds / 3600.

        # Total Stops
        Total_stops = int(request.form["stops"])
        nstop = {'selected': Total_stops}

        # Airline
        airline = int(request.form['airline'])
        airline_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        airline_list[airline] = 1
        airline = {'selected': airline}  

        Air_India, GoAir, IndiGo, Jet_Airways, Jet_Airways_Business, Multiple_carriers,\
        Multiple_carriers_Premium_economy, SpiceJet, Trujet, Vistara, Vistara_Premium_economy, Air_Asia = airline_list      


        # Source
        source = int(request.form["source"])
        source_list = [0, 0, 0, 0]
        source_list[source] = 1
        source = {'selected': source}
        s_Delhi, s_Kolkata, s_Mumbai, s_Chennai = source_list


        # Destinations
        destination = int(request.form["destination"])
        dest_list = [0, 0, 0, 0, 0]
        dest_list[destination] = 1
        destination = {'selected': destination}
        d_Cochin, d_Delhi, d_New_Delhi, d_Hyderabad, d_Kolkata = dest_list

        if arr_time <= dep_time:
            return render_template("home.html", prediction_text="Departure time must be before the arrival time!",
                sources = sources, source = source,
                destinations = destinations, destination = destination,
                nstops = nstops, nstop = nstop,
                airlines = airlines, airline = airline,
                dep_time = dep_time, arr_time = arr_time)


        
        prediction = model.predict([[
            Total_stops,
            flight_day,
            flight_month,
            flight_dayofweek,
            dep_hour,
            dep_min,
            arr_hour,
            arr_min,
            duration_hours,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            s_Chennai,
            s_Delhi,
            s_Kolkata,
            s_Mumbai,
            d_Cochin,
            d_Delhi,
            d_Hyderabad,
            d_Kolkata,
            d_New_Delhi
        ]])

        output = round(prediction[0],2)

        return render_template('home.html', prediction_text="$ {}".format(output),
            sources = sources, source = source,
            destinations = destinations, destination = destination,
            nstops = nstops, nstop = nstop,
            airlines = airlines, airline = airline,
            dep_time = dep_time, arr_time = arr_time)


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)
