from flask import Flask, render_template, request, jsonify

from ipv4 import is_valid_ipv4
from ipv6 import is_valid_ipv6


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/validate", methods=["POST"])
def validate():

    data = request.get_json()

    version = data.get("version")
    ip = data.get("ip")

    if version == "4":
        result = is_valid_ipv4(ip)
        valid = "is valid" in result
    elif version == "6":
        result = is_valid_ipv6(ip)
        valid = "is valid" in result
    else:

        result = "Invalid IP version."
        valid = False
    return jsonify({
        "valid": valid,
        "message": result.strip()
    })

if __name__ == "__main__":
    app.run(debug=True)
