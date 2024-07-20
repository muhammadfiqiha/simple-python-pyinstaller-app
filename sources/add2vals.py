# '''
# A simple command line tool that takes 2 values and adds them together using
# the calc.py library's 'add2' function.
# '''

# import sys
# import calc

# argnumbers = len(sys.argv) - 1

# if argnumbers == 2 :
#     print("")
#     print("The result is " + str(calc.add2(str(sys.argv[1]), str(sys.argv[2]))))
#     print("")
#     sys.exit(0)

# if argnumbers != 2 :
#     print("")
#     print("You entered " + str(argnumbers) + " value/s.")
#     print("")
#     print("Usage: 'add2vals X Y' where X and Y are individual values.")
#     print("       If add2vals is not in your path, usage is './add2vals X Y'.")
#     print("       If unbundled, usage is 'python add2vals.py X Y'.")
#     print("")
#     sys.exit(1)

from flask import Flask, request, jsonify
import calc, pandas

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