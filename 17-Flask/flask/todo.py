from flask import Flask, jsonify, request
app = Flask(__name__)

#Initialize Data in my todo-list
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]

@app.route('/')
def home():
    return "Welcome To The Sample To DO List App"

#Get: Retrieve all the items
@app.route('/items', methods = ['GET'])
def get_items():
    return jsonify(items)  

#Retreive a specific item by Id
@app.route('/items/<int:item_id>', methods = ['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"})
    return jsonify(item)



if __name__ == '__main__':
    app.run(debug=True)