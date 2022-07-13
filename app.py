from flask import Flask, request, jsonify
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)

messages = {}

@app.route('/message', methods = ['POST'])
def register_message():
    topic = request.get_json()['topic']
    message = request.get_json()['message']

    print(topic)
    print(message)

    if topic not in messages.keys():
        messages[topic] = []

    messages[topic].append(message)

    return 'success'

@app.route('/message/<topic>', methods = ['GET'])
def load_messages(topic):
    if topic not in messages.keys():
        return 'No messages from this topic'
    else:
        topic_messages = messages[topic]

    return jsonify(topic_messages)


def create_app():
    app = Flask(__name__)

    return app

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug = True)