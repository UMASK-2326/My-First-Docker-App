from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# Path to the images directory
IMAGE_FOLDER = "images"

# List of image filenames from the folder
images = [f for f in os.listdir(IMAGE_FOLDER) if f.endswith(('png', 'jpg', 'jpeg', 'gif'))]

@app.route('/')
def index():
    if images:
        image_path = os.path.join(IMAGE_FOLDER, random.choice(images))  # Select a random image
    else:
        image_path = None  # No images found

    return render_template('index.html', image_path=image_path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
