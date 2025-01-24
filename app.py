from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    image_path = url_for('static', filename='images/uma.jpg')  # Correct way to reference static files
    return render_template('index.html', image_path=image_path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
