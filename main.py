from flask import Flask, jsonify, request, json
from model.twit import Twit

twits = []

app = Flask(__name__)

@app.route('/ping', methods = ['GET'])
def ping():
    return jsonify({'response': 'success'})

@app.route('/twit', methods = ['POST'])
def create_twit():
    '''
    {'body': 'Some text', 'author': '@somewho'}
    '''
    twit_js = request.get_json()

    if not twit_js or 'body' not in twit_js or 'author' not in twit_js:
        return jsonify({"error": "Missing 'body' or 'author'"}), 400

    twit = Twit(twit_js['body'], twit_js['author'])
    twits.append(twit.to_dict())
    return jsonify({'status': 'success'})



@app.route('/twit', methods = ['GET'])
def read_twit():
    return jsonify({'twits': twits})

@app.route('/twit/<int:twit_id>', methods=['PUT'])
def update_twit(twit_id: int):
    """
    PUT /twit/0
    {
        "body": "Обновлённый текст",
        "author": "@john_new"
    }
    """
    if twit_id >= len(twits) or twit_id < 0:
        return jsonify({"error": "Twit not found"}), 404

    twit_js = request.get_json()

    current = twits[twit_id]

    # Обновляем поля
    if 'body' in twit_js:
        current['body'] = twit_js['body']
    if 'author' in twit_js:
        current['author'] = twit_js['author']

    return jsonify({"status": "updated", "twit": current}), 200

@app.route('/twit/<int:twit_id>', methods=['DELETE'])
def delete_twit(twit_id: int):
    """
    DELETE /twit/0
    """
    if twit_id >= len(twits) or twit_id < 0:
        return jsonify({"error": "Twit not found"}), 404

    deleted = twits.pop(twit_id)
    return jsonify({"status": "deleted", "twit": deleted}), 200

if __name__ == '__main__':
    app.run(debug = True, host="0.0.0.0", port=8002)