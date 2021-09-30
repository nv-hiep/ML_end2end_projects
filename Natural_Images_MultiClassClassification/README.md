# MultiClass Classification with CNN Model

## Class Prediction - Single Object in An Image
- Predict Class of a single object in an image with the use of CNN Model
- Use Class-Weight to deal with the Imbalanced Dataset
- Build a webapp with Flask
- Deploy the Model With Flask on Heroku

1. Data:
   - Movie posters dataset can be found here: https://www.kaggle.com/prasunroy/natural-images
   - Kaggle API Command:
      $ ! kaggle datasets download -d prasunroy/natural-images
2. Run the Notebook: MultiClass_Classification_with_CNN.ipynb
   - Train a CNN model for MultiClass Classification using Class-Weights for Imbalanced Dataset
   - Predict the Class of an object in an iamge
   - Save the CNN model and the model weight (MCC_model_classweight.json and MCC_model_classweight_weight.h5) in directory /model
3. Buid a webapp with Flask:
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
   - Check the app via: https://multiclass-clsf-object-class.herokuapp.com/