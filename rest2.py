#Aideen Byrne Big Project
#!flask/bin/python
from flask import Flask, jsonify,  request, abort, make_response

# Create the application instance
app = Flask(__name__,
            static_url_path='', 
            static_folder='../')

vinyl = [
    {
        "id":1,
        "Artist":"Sleep",
        "Title":"Holy Mountain",
        "Label":"Southern Lord",
        "Price":200
    },
    {
       "id":2,
        "Artist":"High On Fire",
        "Title":"Luminiferous",
        "Label":"Southern Lord",
        "Price":40
    },
    {
       "id":3,
        "Artist":"At The Gates",
        "Title":"Slaughter of the Soul",
        "Label":"Disfear",
        "Price":25
    }
]
nextID = 4

# Create a URL route in our application for "/"
#@app.route('/')
#def home():

#    return "Hello World!"

#curl "http://127.0.0.1:5000/"
@app.route('/vinyl')
def getALL():
    return jsonify(vinyl)

#curl "http://127.0.0.1:5000/vinyl/2"
@app.route('/vinyl/<int:id>')
def findById(id):
    foundVinyl = list(filter(lambda v: v['id'] == id, vinyl))
    if len(foundVinyl) == 0:
        return jsonify ({}), 204

    return jsonify(foundVinyl[0])

@app.route('/vinyl', methods=['POST'])
def create():
    global nextID
    if not request.json:
        abort (400)
        #other checking for formatting (more marks!)
        book = {
            "id": nextID,
            "Artist": request.json['Artist'],
            "Title": request.json['Title'],
            "Label": request.json['Label'],
            "Price": request.json['Price'],
    }
    nextID +=1
    vinyl.append(vinyl)
    return jsonify(book)

#curl -i -H "Content-Type: application/json" -X PUT http://127.0.0.1:5000/vinyl/1 -d "{\"Title\":\"X\"}"
@app.route('/vinyl/<int:id>', methods=["PUT"])
def update(id): 
    foundVinyl = list(filter(lambda t: t['id'] == id, vinyl))
    if (len(foundVinyl) == 0):
        abort (404)
    foundVinyl = foundVinyl[0]
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
    
    return jsonify(foundVinyl)

# curl -X DELETE "http://127.0.0.1:5000/vinyl/1"
@app.route('/vinyl/<int:id>', methods=["DELETE"])
def delete(id):
    foundVinyl = list(filter(lambda t: t['id'] == id, vinyl))
    if (len(foundVinyl) == 0):
        abort (404)
    vinyl.remove(foundVinyl[0])
    return jsonify({"done":True})


if __name__ == '__main__':
    app.run(debug=True)

