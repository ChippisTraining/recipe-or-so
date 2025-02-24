from flask import Blueprint, send_from_directory, jsonify
import os

api = Blueprint('api', __name__)

@api.route('/files/imgs/<path:filename>')
def fetch_images(filename):
    return send_from_directory(os.path.join('public', 'imgs'), filename)

@api.errorhandler(404)
def not_found(e):
    return jsonify({'code': 404, 'msg': 'not found'})
