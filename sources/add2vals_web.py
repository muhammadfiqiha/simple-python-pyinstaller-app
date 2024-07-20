from flask import Flask, request, jsonify
import calc

app = Flask(__name__)

@app.route('/add2vals', methods=['POST'])
def add2vals():
    data = request.json
    x = data.get('x')
    y = data.get('y')
    if x is None or y is None:
        return jsonify({'error': 'Missing parameters'}), 400
    try:
        result = float(x) + float(y)
        return jsonify({'result': result})
    except ValueError:
        return jsonify({'error': 'Invalid parameters'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)