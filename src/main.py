"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, render_template, jsonify, redirect
from flask_cors import CORS, cross_origin
from jobs import get_jobs
import os
# Init app
app = Flask(__name__)
CORS(app)


# routing TODO make another file for routing
@app.route('/api/jobs', methods=['GET', 'POST'])
def api_get_jobs():
    jobs = get_jobs()
    return jsonify(jobs)


@app.route("/")
@app.route("/home")
def home():
    return redirect("http://localhost:3000")


if __name__ == '__main__':
    app.run(debug=True)

