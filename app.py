from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', image_path="images/uma.jpg")  # Change to your image name

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
