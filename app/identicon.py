'''
Identicon generator API.
'''
from flask import Flask, Response


app = Flask(__name__)

def main_route(arg_name):
    image = b"image_data"
    return Response(image, mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
