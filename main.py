import csv
from flask import Flask, jsonify, request
all_movies = []
with open ('movies.csv' , encoding = 'utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
app = Flask(__name__)
@app.route('/get-movies')

def get_movie():
    return jsonify({
        'data' : all_movies[0],
        'status' : 'success',
    })

@app.route('/liked-movie' , methods = ['POST'])

def liked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movie.append(movie)
    return jsonify({
        'status' : 'success'
    }), 201 

@app.route('/unliked-movie' , methods = ['POST'])

def unliked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    unliked_movie.append(movie)
    return jsonify({
        'status' : 'success'
    }), 201

@app.route('/didnotwatch-movie' , methods = ['POST'])

def didnotwatch_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    didnotwatch_movie.append(movie)
    return jsonify({
        'status' : 'success'
    }), 201

if __name__ == '__main__':
    app.run()