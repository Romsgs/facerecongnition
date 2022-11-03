import os      # For File Manipulations like get paths, rename
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import faceApp
app = Flask(__name__)
app.secret_key = "secret key"  # for encrypting the session
# It will allow below 16MB contents only, you can change it
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
path = os.getcwd()  # path/home/romulo/Documentos/qesh/faceRecon
print("this is path" + path)
# file Upload
# /home/romulo/Documentos/qesh/faceRecon/uploads
UPLOAD_FOLDER = os.path.join(path, 'uploads')
print("this is UPLOAD_FOLDER " + UPLOAD_FOLDER)
# Make directory if "uploads" folder not exists
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/', methods=['POST'])
def upload_file():
    file1 = ""
    file2 = ""
    if request.method == 'POST':

        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)

        files = request.files.getlist('files[]')

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    for i in range(len(files)):
        print('print i > ',i)
        if i == 0:
            file1 = os.path.join(
                app.config['UPLOAD_FOLDER'], files[i].filename)
        if i == 1:
            file2 = os.path.join(
                app.config['UPLOAD_FOLDER'], files[i].filename)
    print(file1, file2)
    result = faceApp.verify(file1, file2)
    flash('File(s) successfully uploaded')
    return result


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)
