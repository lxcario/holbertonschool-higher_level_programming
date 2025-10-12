#!/usr/bin/python3
"""Module containing simple Flask web application"""
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route('/')
def home():
    return 'Welcome to the Flask API!'


@app.route('/data')
def data():
    return jsonify(list(users))


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    if data is None or data.get('username') is None:
        return jsonify({'error': 'Username is required'}), 400
    user = {
        'username': data.get('username'),
        'name': data.get('name'),
        'age': data.get('age'),
        'city': data.get('city')
    }
    users[user.get('username')] = user
    return jsonify({'message': 'User added', 'user': user}), 201


@app.route('/status')
def status():
    return 'OK'


@app.route('/users/<username>')
def username(username):
    if username is None:
        return jsonify({'error': 'Username is required'}), 400
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])


if __name__ == "__main__":
    app.run()
