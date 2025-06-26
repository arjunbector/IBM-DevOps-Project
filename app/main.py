from flask import Blueprint, jsonify, request
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time
import os

bp = Blueprint('main', __name__)

# Prometheus metrics
REQUEST_COUNT = Counter('flask_requests_total', 'Total Flask requests', ['method', 'endpoint'])
REQUEST_DURATION = Histogram('flask_request_duration_seconds', 'Flask request duration')

@bp.before_request
def before_request():
    request.start_time = time.time()

@bp.after_request
def after_request(response):
    REQUEST_COUNT.labels(method=request.method, endpoint=request.endpoint).inc()
    if hasattr(request, 'start_time'):
        REQUEST_DURATION.observe(time.time() - request.start_time)
    return response

@bp.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return jsonify({
        'message': 'Flask DevOps Pipeline',
        'version': '1.0.0',
        'timestamp': time.time()
    })

@bp.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

@bp.route('/api/users', methods=['GET'])
def get_users():
    users = [
        {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'},
        {'id': 2, 'name': 'Jane Smith', 'email': 'jane@example.com'},
        {'id': 3, 'name': 'Alice Johnson', 'email': 'alicejohn@example.com'}
    ]
    return jsonify({'users': users})

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)