import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from modules.cleaner import clean_csv

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["ALLOWED_EXTENSIONS"] = {"csv"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return redirect(url_for("index"))

    file = request.files["file"]

    if file.filename == "" or not allowed_file(file.filename):
        return redirect(url_for("index"))

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(filepath)

    # Run cleaner
    cleaned_df, clean_report = clean_csv(filepath)

    # Save cleaned CSV
    cleaned_path = os.path.join(app.config["UPLOAD_FOLDER"], "cleaned_" + filename)
    cleaned_df.to_csv(cleaned_path, index=False)

if __name__ == "__main__":
    app.run(debug=True)