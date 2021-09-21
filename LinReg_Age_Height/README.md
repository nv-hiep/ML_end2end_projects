# ML_Flask_Predict_Height

## Height Prediction
- Predict Height based on Age with the use of Linear Regression Model.
- Build a webapp with Flask
- Plot charts with ChartJs
- Deploy the Model With Flask on Heroku

1. Data: in directory /data
2. Run the notebook: Linear_Regression.ipynb:
   - Data wrangling,
   - Train a Linear Regressor model,
   - Predict the Height with test dataset
   - Save the Linear Regressor model (LinReg_Age_Height.pkl) in directory /model
3. Buid a webapp with Flask, and plot Charts with ChartJs:
   - Install Flask (https://linuxize.com/post/how-to-install-flask-on-ubuntu-20-04/)
   - To import numpy, pandas etc... Need to be inside (venv) of Flask. then:  pip3 install numpy,  pip3 install scikit-learn,  pip3 install pandas etc...
   - cd to the directory that contains "app.py"
   - Run the "app.py" (e.g: python3 app.py)
   - Open http://127.0.0.1:5000/ on localhost in browser.
4. Upload to Github
   - Upload the project to Github
   - Include the files: Procfile, requirements.txt, runtime.txt
5. Deploy the App on Heroku
   - Signup for an account on Heroku
   - Create a new app
   - Connect to Github in "Deployment method"
   - Deploy the App (click on "Deploy Branch")
   - Check the app via: https://ml-flask-age-height-linreg.herokuapp.com/