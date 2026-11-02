from flask import Flask, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/')
def hello():
    app.logger.info("hello request received")
    return jsonify({"message": "Hello, World!"})

@app.route('/health')
def health():
    app.logger.info("healthcheck request received")
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)

