# ML_end2end_projects


## 1. Air Fare Prediction
Predict Air Fare with Random Forest Regression.

1. Data: Training and Test datasets are located in directory /data
2. Run the notebook: AirFare_Prediction_using_RandomForest.ipynb:
   - Data wrangling,
   - Exploratory data analysis (EDA),
   - Feature selection (find the impotant features with sklearn.ensemble ExtraTreesRegressor),
   - Train a RandomForestRegressor model,
   - Fine-tune the hyperparameters of the Random Forrest Regressor using RandomizedSearchCV,
   - Predict the airfare price with test dataset
   - Save the RandomForestRegressor model (RFRegressor_Model_AirFare_Prediction.pkl)
3. Buid a webapp with Flask:
   - Install Flask (https://linuxize.com/post/how-to-install-flask-on-ubuntu-20-04/)
   - To import numpy, pandas etc... Need to be inside (venv) of Flask. then:  pip3 install numpy,  pip3 install scikit-learn,  pip3 install pandas etc...
   - cd to the directory that contains "app.py"
   - Run the "app.py" (e.g: python3 app.py)
   - Open http://127.0.0.1:5000/ in browser.




## 2. Car Price Prediction
Predict (second-hand) Car Price with Random Forest Regression.

1. Data: Training and Test datasets are located in directory /data
2. Run the notebook: Car_Price_Prediction_using_RandomForestRegressor.ipynb:
   - Data wrangling,
   - Exploratory data analysis (EDA),
   - Feature selection (find the impotant features with sklearn.ensemble ExtraTreesRegressor),
   - Train a RandomForestRegressor model,
   - Fine-tune the hyperparameters of the Random Forrest Regressor using RandomizedSearchCV,
   - Predict the car price with test dataset
   - Save the RandomForestRegressor model (RFRegressor_Model_Car_Price.pkl)
3. Buid a webapp with Flask:
   - Install Flask (https://linuxize.com/post/how-to-install-flask-on-ubuntu-20-04/)
   - To import numpy, pandas etc... Need to be inside (venv) of Flask. then:  pip3 install numpy,  pip3 install scikit-learn,  pip3 install pandas etc...
   - cd to the directory that contains "app.py"
   - Run the "app.py" (e.g: python3 app.py)
   - Open http://127.0.0.1:5000/ in browser.
