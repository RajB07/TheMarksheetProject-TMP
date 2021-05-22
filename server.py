from flask import Flask, render_template, request, redirect, send_file, flash, send_from_directory, abort
import os
from werkzeug.utils import secure_filename
import main

app = Flask(__name__)
app.secret_key =''    #add secret key 


@app.route('/')  # This is nothing but to define the parameters in the URL
def hello_world():
    return render_template('index.html')


@app.route('/<string:page_name>')  # **Refer comment below
def main_page(page_name):
    return render_template(page_name)

# I've only done changes to form of index.html. Have to do it to the rest as well.

#adding  paths 
app.config["PDF_UPLOADS"] = ""
app.config["ALLOWED_PDF_EXTENSIONS"] = ["PDF"]
app.config["MAX_PDF_FILESIZE"] = 50 * 1024 * 1024
app.config["CSV_FILEPATH"] = "


def allowed_pdf(filename):

    # We only want files with a . in the filename
    if not "." in filename:
        return False

    # Split the extension from the filename
    ext = filename.rsplit(".", 1)[1]

    # Check if the extension is in ALLOWED_PDF_EXTENSIONS
    if ext.upper() in app.config["ALLOWED_PDF_EXTENSIONS"]:
        return True
    else:
        return False


def allowed_pdf_filesize(filesize):

    if int(filesize) <= app.config["MAX_PDF_FILESIZE"]:
        return True
    else:
        return False


@app.route("/upload-pdf", methods=["GET", "POST"])
def upload_pdf():

    if request.method == "POST":

        if request.files:

            if "filesize" in request.cookies:

                if not allowed_pdf_filesize(request.cookies["filesize"]):
                    print("Filesize exceeded maximum limit")
                    flash('File size exceeds maximum limit', 'danger')
                    return redirect(request.url)

                pdf = request.files["pdf"]

                if pdf.filename == "":
                    print("No filename")
                    flash('No file uploaded or invalid file name', 'danger')
                    return redirect(request.url)

                if allowed_pdf(pdf.filename):
                    global filename
                    filename = secure_filename(pdf.filename)

                    pdf.save(os.path.join(
                        app.config["PDF_UPLOADS"], filename))

                    print("PDF saved")

                    file_path = os.path.join(
                        app.config["PDF_UPLOADS"], filename)
                    print(file_path)
                    print(filename)

                    main.run_main(file_path, filename)

                    return render_template('/download_csv.html', data="static/csv-json-txt/" + filename[:-4] + "_" + "student_data.json")

                else:
                    print("That file extension is not allowed")
                    flash('Please upload a PDF.', 'danger')
                    return redirect(request.url)

    return render_template("/upload_pdf.html")


# @app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
# def download(filename):
#     uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
#     return send_from_directory(directory=uploads, filename=filename)

# @app.route('/thisone_student_data.csv')
# def download_file():
#     print(filename)
#     try:
#         return send_file("static/csv-json-txt/"+filename[:-4]+'_' + "student_data.csv", as_attachment=False)
#         # return send_from_directory(app.config["CSV_FILEPATH"], filename=filename, as_attachment=True)
#     except FileNotFoundError:
#         abort(404)


@app.route("/download", methods=["GET", "POST"])
def download_file():
    if "file_name" in request.cookies:
        print(request.cookies["file_name"])
        p = "static/csv-json-txt/" + \
            request.cookies["file_name"].replace(
                '.pdf', '').replace(' ', '_') + "_" + "student_data.csv"

        return send_file(p, as_attachment=True)

    # @app.route('/<filename>')
    # def download_file():
    #     p = filename[:-4]+'_' + "student_data.csv"
    #     print(p)
    #     return send_file(p, as_attachment=True)
