from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from db_config import get_db_connection

app = Flask(__name__, template_folder="../templates", static_folder="../static")
CORS(app)

# ---------------------------
# LOGIN PAGE
# ---------------------------
@app.route('/')
def login_page():
    return render_template("login.html")


# ---------------------------
# DASHBOARD PAGE
# ---------------------------
@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


# ---------------------------
# PAGE ROUTES
# ---------------------------
@app.route('/hotels_page')
def hotels_page():
    return render_template("hotels.html")


@app.route('/places_page')
def places_page():
    return render_template("places.html")


@app.route('/guides_page')
def guides_page():
    return render_template("guides.html")


@app.route('/transport_page')
def transport_page():
    return render_template("transport.html")


@app.route('/reviews_page')
def reviews_page():
    return render_template("reviews.html")


@app.route('/budget_page')
def budget_page():
    return render_template("budget.html")


@app.route('/queries_page')
def queries_page():
    return render_template("queries.html")


# ---------------------------
# LOGIN API
# ---------------------------
@app.route('/login', methods=['POST'])
def login():

    data = request.json
    email = data['email']
    password = data['password']

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    sql = "SELECT * FROM Users WHERE email=%s AND password=%s"
    cursor.execute(sql, (email, password))

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user:
        return jsonify({"status": "success", "user": user})
    else:
        return jsonify({"status": "fail"})


# ---------------------------
# HOTELS API
# ---------------------------
@app.route('/hotels')
def get_hotels():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM Hotels")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(data)


# ---------------------------
# PLACES API
# ---------------------------
@app.route('/places')
def get_places():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM Places")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(data)


# ---------------------------
# GUIDES API
# ---------------------------
@app.route('/guides')
def get_guides():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM Tourist_Guides")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(data)


# ---------------------------
# TRANSPORT API
# ---------------------------
@app.route('/transport')
def get_transport():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM Transport")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(data)


# ---------------------------
# REVIEWS API
# ---------------------------
@app.route('/reviews')
def get_reviews():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM Reviews")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(data)


# ---------------------------
# BUDGET API
# ---------------------------
@app.route('/budget')
def get_budget():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM Budget_Planner")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(data)


# ---------------------------
# QUERY EXECUTION API
# ---------------------------
@app.route('/run_query', methods=['POST'])
def run_query():

    data = request.json
    query = data['query']

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(result)


# ---------------------------
# RUN SERVER
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True)