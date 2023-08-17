from flask import Flask, redirect, url_for, request, render_template
from AddToDb import saveStudentDetails, saveStudentImages
from main import compatible_image, resize_image
import os

app = Flask(__name__)
current_directory = os.path.dirname(os.path.abspath(__file__))
# root path
@app.route('/')
def root():
   return "Hello World"

# *********************************** student details ********************************************
# get student detail form
@app.route('/add-form', methods = ['GET'])
def save_student():
      return render_template('add-form.html')

# post student detail form
@app.route('/save-student', methods = ['POST'])
def save():
    if 'image' not in request.files:
        return "No image part in the request", 400
    image = request.files['image']

    key = request.form['key']
    name = request.form['name']
    starting_year = request.form['starting_year']
    year = request.form['year']
    print(image, key, starting_year, year)

    # Save the uploaded image to a file
    folder = "Database/Images"
    path = f"{folder}/{key}.png"
    image.save(path)

    print("Image saved")

    # check image compatibility
    if compatible_image(path):
        resize_image(path)
        saveStudentDetails(key, name, starting_year, year)  #save student details
        saveStudentImages()  # save image
    else:
        print("Not compatible")
    return redirect(url_for('save_student'))


if __name__ == '__main__':
   app.run(debug = True)