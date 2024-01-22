import sys
from datetime import datetime, timedelta, timezone
import jwt
import pytz
import sqlite3
import secrets
import string
from flask import Flask, render_template, request, jsonify, make_response, send_from_directory, g

# ================================================================= Flask app =================================================================

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/robots.txt', methods=['GET'])
def robots_txt():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Vulnerable SQL query
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cur = get_db().cursor()
        cur.execute(query)
        result = cur.fetchone()

        if result:
            # Token creation time in UTC
            issued_at_utc = datetime.now(timezone.utc)
            expires_at_utc = issued_at_utc + timedelta(minutes=1)

            # Convert to Singapore timezone
            sg_timezone = pytz.timezone('Asia/Singapore')
            issued_at_sg = issued_at_utc.astimezone(sg_timezone)
            expires_at_sg = expires_at_utc.astimezone(sg_timezone)

            # Format and write token creation and expiration times
            fmt = '%Y-%b-%d %I:%M:%S%p'
            sys.stdout.write(f'Token Issued At: {issued_at_sg.strftime(fmt)}\n')
            sys.stdout.write(f'Token Expires At: {expires_at_sg.strftime(fmt)}\n')
            sys.stdout.write(f'Secret Key used for Providing New Token: {SECRET_KEY}\n')
            sys.stdout.flush()

            token = jwt.encode({
                'role': 'non-admin',
                'iat': issued_at_utc.timestamp(),
                'exp': expires_at_utc.timestamp(),
            }, SECRET_KEY, algorithm='HS256')
            response = make_response(jsonify({'message': 'Login successful'}))
            response.set_cookie('auth_token', token, httponly=True)
            return response
        else:
            return "Invalid credentials", 401

    return render_template('login.html')


@app.route('/api', methods=['GET'])
@app.route('/api/', methods=['GET'])
def api_unavailable():
    return "Service Unavailable", 503


@app.route('/api/key', methods=['GET'])
def api_key():
    token = request.cookies.get('auth_token')
    if not token:
        return "Unauthorized", 403

    try:
        jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        sys.stdout.write(f'Accessed API Key: {SECRET_KEY}\n')
        sys.stdout.flush()
        return SECRET_KEY
    except jwt.ExpiredSignatureError:
        return "Token expired", 401
    except:
        return "Unauthorized", 403


@app.route('/admin', methods=['GET'])
def admin():
    token = request.cookies.get('auth_token')
    if not token:
        return "Unauthorized", 403
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        if data['role'] == 'admin':
            sys.stdout.write(f'Secret Key on Token Verification: {SECRET_KEY}\n')
            sys.stdout.flush()
            return FLAG
        else:
            return "Unauthorized", 403
    except:
        return "Unauthorized", 403

# ================================================================= SQLite =================================================================

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# ================================================================= Generate Token =================================================================

def generate_secret_key(length=24):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))

# ================================================================= Global Configuration =================================================================

DATABASE = './database.db'
FLAG = "LNC24{5imp1e_Bu7_N0t_Simpl3}"
SECRET_KEY = generate_secret_key()

# =========================================================================================================================================================

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)