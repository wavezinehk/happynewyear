from flask import Flask, render_template, jsonify, request
import random
import json
import os

app = Flask(__name__)

# 設置絕對路徑
json_file_path = os.path.join(os.path.dirname(__file__), '4words.json')

# 讀取電影名稱資料
with open(json_file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 選擇電影名稱，根據條件過濾
def get_filtered_movies(movie_type, filter_value):
    filtered_movies = [entry for entry in data if len(entry["電影"]) == 4]  # 確保只有四字電影
    
    if movie_type == '精選':  # 確保使用正確的繁體字
        filtered_movies = [entry for entry in filtered_movies if entry.get("精選", 0) == 1]
    
    if filter_value == 'holiday':  # 過濾賀歲片
        filtered_movies = [entry for entry in filtered_movies if entry.get("賀歲片", 0) == 1]
    
    if filter_value == 'recent':  # 過濾近年電影
        filtered_movies = [entry for entry in filtered_movies if entry.get("年份", 0) >= 2019]
    
    return filtered_movies

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/draw')
def draw():
    movie_type = request.args.get('type', '精選')  # 取得片名庫選擇
    filter_value = request.args.get('filter', None)  # 取得過濾條件

    # 根據條件過濾電影
    filtered_movies = get_filtered_movies(movie_type, filter_value)
    movies = [entry["電影"] for entry in filtered_movies]
    return jsonify({"movies": movies})

if __name__ == '__main__':
    app.run(debug=True)
