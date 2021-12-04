from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask import request
from flask import jsonify


app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["1000 per day"]
)
app.config['JSON_SORT_KEYS'] = False
@app.route("/api/badge/<id>",methods=['GET'])
@limiter.limit("1000 per day")
def badge(id):
    #id = request.args['id']
    dictToReturn = {
    "name":  f"YGG SEA Badge #{id}",
    "image": "ipfs://QmQgQ9RKmXNTk5Fhfs8rPQbb5sj4rarqYCX4YA7aYV3FTP",
    "description": "YGG SEA Badge NFT",
    "attributes": [
        {
            "trait_type": "Rarity",
            "value": "Common"
        }
    ]
}
    response = jsonify(dictToReturn)
    try:
        return response
    except KeyError:
        return "Invalid input"
if __name__ == '__main__':
    app.run(debug=True)
