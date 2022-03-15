from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

imgFolder = os.path.join('static','images')

app.config['UPLOAD_FOLDER'] = imgFolder

@app.route('/')
def index():
    pen = os.path.join(app.config['UPLOAD_FOLDER'], 'pen.png')
    tri = os.path.join(app.config['UPLOAD_FOLDER'], 'tri.png')
    return render_template('index.html', img1 = pen, img2 = tri)
    # return "Hello World"
    

if __name__ == "__main__":
     app.run(debug=True)