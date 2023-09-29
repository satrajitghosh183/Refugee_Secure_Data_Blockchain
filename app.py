from flask import Flask, render_template, request, jsonify
import cv2
from PIL import Image
import numpy as np
import os
import csv

app = Flask(__name__)

# Create the uploads folder if it doesn't exist
os.makedirs('uploads', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture', methods=['POST'])
def capture():
    try:
        # Access the webcam and capture an image
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()

        # Save the captured image
        image_path = os.path.join('uploads', 'captured_image.jpg')
        cv2.imwrite(image_path, frame)

        # Extract data from the form
        name = request.form.get('name')
        nationality = request.form.get('nationality')
        contact = request.form.get('contact')

        # Prepare data for CSV
        data = [name, nationality, contact, image_path]

        # Write data to a CSV file
        csv_file = 'data.csv'
        header = ['Name', 'Nationality', 'Contact', 'Image_Path']
        is_new_file = not os.path.exists(csv_file)

        with open(csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            if is_new_file:
                writer.writerow(header)
            writer.writerow(data)

        return jsonify({'message': 'Image captured and data saved successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})
# ... (previous code)

@app.route('/display')
def display():
    data = []

    # Read data from the CSV file
    with open('data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    return render_template('display.html', data=data)

@app.route('/search', methods=['POST'])
def search():
    contact_to_find = request.form.get('contact_to_find')

    # Read data from the CSV file
    data = []
    with open('data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    # Search for the contact number
    found_entries = []
    for entry in data:
        if entry['Contact'] == contact_to_find:
            found_entries.append(entry)

    return render_template('display.html', data=found_entries)


if __name__ == '__main__':
    app.run(debug=True)
