from calendar import month_abbr
import os
import re
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import Actor, Movie, setup_db
from auth import AuthError, requires_auth

def create_app(test_config=None):

  # create and configure the app
  app = Flask(__name__)

  # Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  CORS(app, resources={r"/api/*": {"origins": "*"}})
  setup_db(app)


  # Use the after_request decorator to set Access-Control-Allow
  @app.after_request
  def after_request(response):
      response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
      response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
      return response

  # ROUTES

  @app.route('/')
  def get_greeting():
      excited = os.environ['EXCITED']
      greeting = "Hello" 
      if excited == 'true': greeting = greeting + "!!!!!"
      return greeting

  @app.route('/actors')
  @requires_auth('get:actors')
  def get_actors(payload):
      """
      This function will return all actors on the asting agency in short format. 
      """

      actors = Actor.query.all()

      # get the format of actors
      actors_short = [actor.format() for actor in actors]

      result = {
          'success':True,
          'actors': actors_short
      }

      return jsonify(result), 200

  @app.route('/movies')
  @requires_auth('get:movies')
  def get_movies(payload):
      """
      This function will return all movies on the asting agency in short format. 
      """

      movies = Movie.query.all()

      # get the format of movies
      movies_short = [movie.format() for movie in movies]

      result = {
          'success':True,
          'movies': movies_short
      }

      return jsonify(result), 200

  @app.route('/actors', methods=['POST'])
  @requires_auth('post:actors')
  def add_actor(payload):
      """
      This function will add a new actor in the ceinma. 
      """
      # fetch request as json object
      data = request.get_json()

      name = data.get('name', None)
      age = data.get('age', None)
      gender = data.get('gender', None)

      new_actor = Actor(
          name = name,
          age = age,
          gender = gender
      )

      new_actor.insert()

      result = {
          'success': True,
          'actor': new_actor.format() 
      }

      return jsonify(result), 200
  
  @app.route('/movies', methods=['POST'])
  @requires_auth('post:movies')
  def add_movie(payload):
      """
      This function will add a new movie in the ceinma. 
      """
      # fetch request as json object
      data = request.get_json()

      title = data.get('title',None)
      release = data.get('release_date',None)

      new_movie = Movie(
          title = title,
          release_date = release,
      )

      new_movie.insert()

      result = {
          'success': True,
          'movie': new_movie.format() 
      }

      return jsonify(result), 200

  @app.route('/actors/<int:actor_id>', methods=['PATCH'])
  @requires_auth('patch:actors')
  def update_actor(payload, actor_id):
    """
    This function will update the actor details in the asting agency. 
    """
    # fetch request as json object
    data = request.get_json()

    new_name = data.get('name', None)
    new_age = data.get('age', None)
    new_gender = data.get('gender', None)

    actor = Actor.query.filter(Actor.id == actor_id).first()

    if actor is None:
        abort(404)
    
    if new_name:
      actor.name = data.get('name', None)
    if new_age:
      actor.age = data.get('age', None)
    if new_gender:
      actor.gender = data.get('gender', None)

    if new_name or new_age or new_gender:
        actor.update()

    result = {
        'success': True,
        'actor': actor.format()
    }

    return jsonify(result), 200

  @app.route('/movies/<int:movie_id>', methods=['PATCH'])
  @requires_auth('patch:movies')
  def update_movie(payload, movie_id):
    """
    This function will update the movie details in the asting agency. 
    """
    # fetch request as json object
    data = request.get_json()

    new_title = data.get('title', None)
    new_release = data.get('release_date', None)

    movie = Movie.query.filter(Movie.id == movie_id).first()

    if movie is None:
        abort(404)
    
    if new_title:
      movie.name = data.get('title',None)
    if new_release:
      movie.release_date = data.get('release_date', None)

    if new_title or new_release:
        movie.update()

    result = {
        'success': True,
        'movie': movie.format()
    }

    return jsonify(result), 200

  @app.route('/actors/<int:actor_id>', methods=['DELETE'])
  @requires_auth('delete:actors')
  def delete_actor(payload, actor_id):
    """
    This function will delete an actor in the asting agency. 
    """
    actor = Actor.query.filter(Actor.id == actor_id).first()

    if actor is None:
        abort(404)

    actor.delete()

    result = {
        'success': True,
        'delete': actor_id
    }

    return jsonify(result), 200

  @app.route('/movies/<int:movie_id>', methods=['DELETE'])
  @requires_auth('delete:movies')
  def delete_movie(payload, movie_id):
    """
    This function will delete a movie in the asting agency. 
    """
    movie = Movie.query.filter(Movie.id == movie_id).first()

    if movie is None:
        abort(404)

    movie.delete()

    result = {
        'success': True,
        'delete': movie_id
    }

    return jsonify(result), 200

  # Error Handling

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
        'success': False,
        'error': 400,
        'message': 'Bad Request'
    }), 400

  @app.errorhandler(401)
  def unauthorized(error):
    return jsonify({
        'success': False,
        'error': 401,
        'message': 'unauthorized'
    }), 401
    
  @app.errorhandler(AuthError)
  def auth_error(error):
    return jsonify({
        'success': False,
        'error': error.status_code,
        'message': error.error['description']
    }), error.status_code

  return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)