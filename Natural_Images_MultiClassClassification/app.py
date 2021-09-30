import os
from flask import Flask, request, render_template, flash, redirect, url_for
from werkzeug.utils import secure_filename

import numpy as np

from keras.models import model_from_json
from keras.preprocessing import image

# Initiate the app
app = Flask(__name__)

# For session
app.secret_key = 'adahsdusagsagdakdi7quiwuwiqiuqiuqjasbd978dy698d709udjadjka'
app.config['SESSION_TYPE'] = 'filesystem'


# For uploading images
UPLOAD_FOLDER = 'static/img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
MAX_CONTENT_LENGTH = 1 * 1024 * 1024                # 1MB app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  


# load json and create model
json_file = open('model/MCC_model_classweight.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

# load weights into new model
loaded_model.load_weights("model/MCC_model_classweight_weight.h5")

# All 8 classes
CLASSES = np.array(['airplane', 'car', 'cat', 'dog', 'flower', 'fruit', 'motorbike', 'person'])

# target size
SIZE = 224


def predict(img_list: list) -> dict:
    """Predict the Genres of Movies using their Poster Images

    Args:
        img_list ([list]): [List of image filenames]

    Returns:
        [dict]: [Dictionary of image filenames and their predicted Genres]
    """
    ret = {}
    for xfile in img_list:
        img = image.load_img(
            os.path.join(app.config['UPLOAD_FOLDER'], xfile),
            target_size=(SIZE, SIZE, 3)
        )
        img = image.img_to_array(img)
        img = img/255.


        # Reshape the image into Batch style [batch, Size, Size, channel]
        img = img.reshape(1,SIZE,SIZE,3)

        # Probability of each label
        predicted_prob = loaded_model.predict(img)

        # Sort the predicted_probability (decending order) and take the indexes
        indexes = np.argsort(predicted_prob[0])[::-1]


        # predicted_prob[0][indexes]
        # classes[indexes]
        # print(CLASSES[indexes][:5])

        ret[xfile] = [ CLASSES[indexes][:3], 100*np.round(predicted_prob[0][indexes][:3], 3) ]
    
    return ret




def is_allowed_file(filename: str) -> bool:
    """Check if the file is allowed

    Args:
        filename ([string]): [String of Filename]

    Returns:
        [boolean]: [True/False]
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



def del_items() -> None:
    """Delete all image files in UPLOAD FOLDER

    Returns:
        [None]
    """
    for x in os.listdir(UPLOAD_FOLDER):
        os.remove(os.path.join(UPLOAD_FOLDER, x))
    return None





# HTML
TITLE = "DL Flask: Object Class Prediction - MultiClass Classification With CNN"
FRAME_TITLE = "MultiClass Classification With CNN"
PURPOSE_TITLE = "Predict Class of a Single Object in an Image"
NOTE = "Please select an image containing a single object of these 08 classes: airplane, car, cat, dog, flower, fruit, motorbike, person"


@app.route('/')
def home():
    del_items()
    return render_template("index.html",
                           title = TITLE,
                           frame_title = FRAME_TITLE,
                           purpose_title = PURPOSE_TITLE,
                           note = NOTE
                        )





@app.route("/classify", methods = ["GET", "POST"])
def classify():
    if request.method == "POST":

        # check if the post request has the file part
        if 'files[]' not in request.files:
            flash("No file part! Add file input to the form.", "danger")
            return redirect(url_for('home')) # or return redirect(request.url) if want to go back /predict
        
        # file = request.files['file']
        files = request.files.getlist('files[]')
        if len(files) == 1 and files[0].filename == '':
            flash("No selected file! Please choose file(s) to upload.", "danger")
            return redirect(request.url)
        
        if len(files) > 3:
            flash("Too many files! Please select 3 files at max", "danger")
            return redirect(request.url)

        # MAX_CONTENT_LENGTH
        sizes = np.array([len(file.read()) for file in files])
        if np.any(sizes > MAX_CONTENT_LENGTH):
            flash("Files are too large! Please select files with size < " + str(MAX_CONTENT_LENGTH/1024./1024.) + ' MB', "danger")
            return redirect(request.url)

        filenames = []
        for file in files:
            if file and is_allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.seek(0)  # Need to have this to avoid files with 0 bytes
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                filenames.append(filename)
        
        msg = "Success! Files uploaded!" if len(files) > 1 else "Success! File uploaded!"
        flash(msg, "success")


        results = predict(filenames)

        print(results)

        return render_template(
            "classification.html",
            filenames = filenames,
            results = results,
            title = TITLE,
            frame_title = FRAME_TITLE,
            purpose_title = PURPOSE_TITLE,
            note = NOTE,
            zip = zip
        )
    
    return render_template("index.html",
                           title = TITLE,
                           frame_title = FRAME_TITLE,
                           purpose_title = PURPOSE_TITLE,
                           note = NOTE
                        )









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