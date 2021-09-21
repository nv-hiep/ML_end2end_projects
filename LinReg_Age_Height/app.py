from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import pickle


app = Flask(__name__)

# Model
filename = 'model/LinReg_Age_Height.pkl'
with open(filename, 'rb') as f:
    model = pickle.load(f)

# Data
data = pd.read_pickle('data/AgesAndHeights.pkl')
ages = data['Age'].tolist()
heights = data['Height'].tolist()

# Predict - to plot line
y_line = model.predict(np.array(ages).reshape(-1,1))
y_line =y_line.tolist()



@app.route('/')
def home():
    age = 0.00
    prediction_text = "..."    

    return render_template("index.html",
           labels = ages,
           values = heights,
           y_line = y_line,
           prediction_text = prediction_text,
           age = age)





@app.route("/predict", methods = ["GET", "POST"])
def predict():
    if request.method == "POST":

        age = float(request.form["age"]) # age of the ...
        
        X_in = np.array([age]).reshape(1,-1)
        pred = model.predict(X_in)
        pred = round(pred[0], 1)

        return render_template("index.html",
               prediction_text = "{} cm".format(pred),
               labels = [age] + ages,
               values = [pred] + heights,
               y_line = [pred] + y_line,
               age = age)
    
    age = 0.00
    prediction_text = "..."
    return render_template("index.html",
           labels = ages,
           values = heights,
           y_line = y_line,
           prediction_text = prediction_text,
           age = age)









@app.route('/plot')
def plot():
    data = [
    ("01-01-2020", 1597),
    ("02-01-2020", 1465),
    ("03-01-2020", 1908),
    ("04-01-2020", 896),
    ("05-01-2020", 755),
    ("06-01-2020", 423),
    ("07-01-2020", 1100),
    ("08-01-2020", 1235),
    ("09-01-2020", 1536),
    ("10-01-2020", 1498),
    ("11-01-2020", 1623),
    ("12-01-2020", 2121)
    ]

    x = [row[0] for row in data]
    y = [row[1] for row in data]

    return render_template("graph.html", labels=x, values=y)

if __name__ == '__main__':
    app.debug = True
    app.run()