# Image To Text Converter With Tesseract-OCR

## Image To Text Converter
- Convert text within an image to text, then save the text as PDF (using Tesseract-OCR)
- Build a webapp with Flask
- Deploy the Model With Flask on Heroku


## 1. Buid a webapp with Flask:
   - Install Flask (https://linuxize.com/post/how-to-install-flask-on-ubuntu-20-04/)
   - $ python3 -m venv Flask/
   - $ source ./Flask/bin/activate
   - $ cd Flask/
   - $ pip3 install Flask
   - $ mkdir img2text_ocr
   - $ cd img2text_ocr

   - To import numpy, pandas etc... Need to activate (venv) of Flask. then:  pip3 install numpy,  pip3 install scikit-learn,  pip3 install pandas etc...
   - Refer to "requirements.txt" for details of dependencies
   - cd to the directory that contains "app.py"
   - Add a file: ".flaskenv" containing:
   
      FLASK_APP=app.py
      
      FLASK_ENV=development
   
   - touch .env
   - touch .flaskenv

   - vim .flaskenv

     then add:

     FLASK_APP=app.py  # or whatever your app name

     FLASK_ENV=development # or production

   - Note:
      - Add this to app.py when deploying ONLY (For pytesseract on Heroku): "  pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'   "
   - Run the "app.py" (e.g: flask run)
   - Open http://127.0.0.1:5000/ on localhost in browser.

## 2. Upload to Github
   - Upload the project to Github, including the files: Procfile, requirements.txt, runtime.txt, Aptfile

### a. Procfile:
   - web: gunicorn app:app

### b. Aptfile
   - tesseract-ocr
   - tesseract-ocr-eng
   - libsm6
   - libxrender1
   - libfontconfig1
   - libice6

### c. requirements.txt (List dependepcies: pip3 freeze > requirements.txt)
- click==8.0.3
- Flask==1.1.2
- fpdf==1.7.2
- itsdangerous==2.0.1
- Jinja2==2.11.2
- MarkupSafe==2.0.1
- numpy==1.21.2
- opencv-python==4.5.3.56
- opencv-python-headless==4.5.3.56
- python-multipart==0.0.5
- Pillow==8.3.2
- pytesseract==0.3.8
- python-dotenv==0.19.1
- six==1.16.0
- typing-extensions==3.10.0.2
- gunicorn==20.1.0
- python-dateutil==2.8.1
- pytz==2021.1
- retrying==1.3.3
- threadpoolctl==2.1.0
- Werkzeug==1.0.1
- protobuf==3.18.0

### d. runtime.txt
- python-3.8.10

## 3. Deploy the App on Heroku
   - Prepare: Procfile, requirements.txt, runtime.txt, Aptfile (see above for details of these files)
   - Signup for an account on Heroku
   - Create a new app
   - New app will be located in "/app" on Heroku
   - In Settings:
      Add 02 Buildpacks:
      1. https://github.com/heroku/heroku-buildpack-apt
      2. heroku/python

      3. Add Config Vars:
      
      TESSDATA_PREFIX = ./.apt/usr/share/tesseract-ocr/4.00/tessdata

   - Connect to Github in "Deployment method"
   - Deploy the App (click on "Deploy Branch")
   - Check the app via: https://img-to-text-ocr.herokuapp.com/
   - If error: Check logs for details: 
      - $ heroku logs --tail
   - If error: heroku stack (heroku-20) has bad compatibility with tesseract. You may need to change heroku stack from 20 to 18 using command:

      - $ heroku stack:set heroku-18

Then Redeploy!

## Connect to Heroku using Heroku ICL
- $ heroku login
- $ heroku git:remote -a img-to-text-ocr
- $ heroku run bash
- $ pwd -> Output: /app
- $ which tesseract ->
  Ouput: "/app/.apt/usr/bin/tesseract"
- $ find -iname tessdata ->
  Ouput:   /app/.apt/usr/share/tesseract-ocr/4.00/tessdata


## For deploying on Heroku, need to install dependencies listed in Aptfile:
- gunicorn

- tesseract-ocr
- tesseract-ocr-eng
- libsm6
- libxrender1
- libfontconfig1
- libice6