from flask import Blueprint, send_from_directory
import os

api = Blueprint('api', __name__)

@api.route('/files/<path:filename>')
def fetch_files(filename):
    return send_from_directory(os.path.join('dynamic', 'imgs'), filename)
