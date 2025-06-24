from flask import Flask, request, render_template, send_from_directory
import os
from src.detect import detect

app = Flask(__name__)
UPLOAD = 'uploads'
os.makedirs(UPLOAD, exist_ok=True)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        file = request.files['image']
        path = os.path.join(UPLOAD, file.filename)
        file.save(path)
        results = detect(path, model_path='models/weights/best.pt')
        saved = results[0].masks.data if results else None
        return render_template('index.html', img_out=os.path.basename(results[0].path[0]))
    return render_template('index.html')

@app.route('/uploads/<path:filename>')
def uploads(filename):
    return send_from_directory('models/logs/detect', filename)

if __name__=='__main__':
    app.run(debug=True)