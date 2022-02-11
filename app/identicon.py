'''
Identicon generator API.
'''
from flask import Flask, Response, request, render_template

from identicon_generator import create_image


app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/getimage/<string:value>")
def get_image(value):
    size = request.args.get("size", '')
    image = create_image(value, size)
    return Response(image, mimetype="image/png")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
