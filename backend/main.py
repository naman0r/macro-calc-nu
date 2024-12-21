from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/hello_world", methods=["GET"])
def hello_world():
    return jsonify("HELLO WORLD")

if __name__ == '__main__':
   app.run(port=4000)