from flask import Flask, render_template, send_from_directory
import os
import random

app = Flask(__name__)

# Define the path to the images directory (outside "static")
IMAGE_FOLDER = os.path.join(app.root_path, "images")

# Get list of image files
images = [f for f in os.listdir(IMAGE_FOLDER) if f.endswith(('png', 'jpg', 'jpeg', 'gif'))]

@app.route('/')
def index():
    if images:
        image_filename = random.choice(images)  # Pick a random image
    else:
        image_filename = None

    return render_template('index.html', image_filename=image_filename)

# Route to serve images from the "images/" folder
@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
