import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def get_quiz_data():
  with open('quiz_data.json', 'r') as f:
    

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))