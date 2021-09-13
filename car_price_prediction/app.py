from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("model/RFRegressor_Model_Car_Price.pkl", "rb"))
# Present_Price   Years   Kms_Driven  Owner   Fuel_Type_Diesel    Seller_Type_Individual  Transmission_Manual


seller_types = {0:"Dealer", 1:"Individual"}
seller_type = {'selected': 0}

fuel_types = {0:"Petrol", 1:"Diesel", 2:"CNG"}
fuel_type = {'selected': 0}

transmissions = {0:"Automatic", 1:"Manual"}
transmission = {'selected': 0}

# year = pd.datetime.now().year - 1
years = 1
showroom_price = ""
km_driven = ""
owners = 1




@app.route("/")
@cross_origin()
def home():
    return render_template("index.html",
        years = years, showroom_price = showroom_price,
        km_driven = km_driven, owners = owners,
        fuel_types = fuel_types, fuel_type = fuel_type,
        seller_types = seller_types, seller_type = seller_type,
        transmissions = transmissions, transmission = transmission)



@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        years = int(request.form["years"]) # age of the car
        showroom_price = float(request.form["showroom_price"]) / 1000.
        km_driven = float(request.form["km"])
        owners = int(request.form["owners"])


        seller = int(request.form["seller_type"])
        seller_type = {'selected': seller}


        trans = int(request.form["transmission"])
        transmission = {'selected': trans}


        # fuel_type
        fuel_type = int(request.form["fuel_type"])
        fuel_type_list = [0, 0, 0] # petrol, diesel and CNG
        fuel_type_list[fuel_type] = 1
        fuel_type = {'selected': fuel_type}
        fuel_petrol, fuel_diesel, fuel_cng = fuel_type_list

        # if ():
        #     return render_template("index.html", prediction_text="ABC XYZ!",
        #         year = year, showroom_price = showroom_price,
        #         km_driven = km_driven, owners = owners,
        #         fuel_types = fuel_types, fuel_type = fuel_type,
        #         seller_types = seller_types, seller_type = seller_type,
        #         transmissions = transmissions, transmission = transmission)

        
        prediction = model.predict([[
            showroom_price,
            years,
            km_driven,
            owners,
            fuel_diesel,
            seller,
            trans
            ]])

        output = round(prediction[0],2) * 1000.

        return render_template('index.html', prediction_text="$ {}".format(output),
            years = years, showroom_price = showroom_price*1000.,
            km_driven = km_driven, owners = owners,
            fuel_types = fuel_types, fuel_type = fuel_type,
            seller_types = seller_types, seller_type = seller_type,
            transmissions = transmissions, transmission = transmission)


    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)
