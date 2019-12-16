#Aideen Byrne Big Project
#!flask/bin/python
from flask import Flask, jsonify, request, abort
from vinylDAO import vinylDAO

# Create the application instance
app = Flask(__name__, static_url_path='', static_folder='.')

#curl "http://127.0.0.1:5000/vinyl"
@app.route('/vinyl')
def getALL():
    results = vinylDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/vinyl/2"
@app.route('/vinyl/<int:id>')
def findById(id):
    foundVinyl = vinylDAO.findByID(id)
    return jsonify(foundVinyl)

@app.route('/vinyl', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    vinyl = {
        "Artist": request.json['Artist'],
        "Title": request.json['Title'],
        "Label": request.json['Label'],
        "Price": request.json['Price'],
    }
    values =(vinyl['Artist'],vinyl['Title'],vinyl['Label'],vinyl['Price'])
    newId = vinylDAO.create(values)
    vinyl['id'] = newId
    return jsonify(vinyl)


#curl -i -H "Content-Type: application/json" -X PUT http://127.0.0.1:5000/vinyl/1 -d "{\"Title\":\"X\"}"
@app.route('/vinyl/<int:id>', methods=['PUT'])
def update(id): 
    foundVinyl = vinylDAO.findByID(id)
    if not foundVinyl:
        abort (404)
   
    if not request.json:
        abort (400)
    reqJson = request.json

    if 'Price' in reqJson and type (reqJson['Price']) is not int:
        abort (400)
    if 'Artist' in reqJson:
        foundVinyl['Artist'] = reqJson['Artist']
    if 'Title' in reqJson:
        foundVinyl['Title'] = reqJson['Title']
    if 'Label' in reqJson:
        foundVinyl['Label'] = reqJson['Label']
    if 'Price' in reqJson:
        foundVinyl['Price'] = reqJson['Price']
    values = (foundVinyl['Artist'], foundVinyl['Title'], foundVinyl['Label'], foundVinyl['Price'], foundVinyl['id'])
    vinylDAO.update(values)
    return jsonify(foundVinyl)

# curl -X DELETE "http://127.0.0.1:5000/vinyl/1"
@app.route('/vinyl/<int:id>', methods=["DELETE"])
def delete(id):
    vinylDAO.delete(id)
    return jsonify({"done":True})


if __name__ == '__main__':
    app.run(debug=True)
