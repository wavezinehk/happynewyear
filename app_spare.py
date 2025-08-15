from flask import Flask, render_template, jsonify
import random
import json
import os

app = Flask(__name__)

# 設置絕對路徑
json_file_path = os.path.join(os.path.dirname(__file__), '4words.json')

# 讀取電影名稱資料
with open(json_file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 選擇四字電影名稱
def get_random_movie():
    four_word_movies = [entry["電影"] for entry in data if len(entry["電影"]) == 4]
    return random.choice(four_word_movies)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/draw')
def draw():
    # 隨機選擇四字電影名稱
    movie = get_random_movie()
    return jsonify({"movie": movie})

if __name__ == '__main__':
    app.run(debug=True)