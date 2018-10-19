from flask import Flask, jsonify
from flask_pymongo import PyMongo

app =Flask(__name__)

app.config['MONGO_DBNAME'] = 'scr_db'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/scr_db'

mongo = PyMongo(app)

@app.route('/api/flask/get_record', methods=['GET'])
def get_record():
    record = mongo.db.testCollection.find_one()
    if record:
        output = {'text': record['text'], 'author': record['author'], 'tags': record['tags']}
    else:
        output = 'No records'
    return jsonify({'result': output})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    
