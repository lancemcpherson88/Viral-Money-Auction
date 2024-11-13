from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
import time

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect('auction.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS bids (
            id INTEGER PRIMARY KEY,
            user TEXT,
            amount REAL,
            timestamp INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database when starting the server
init_db()

@app.route('/')
def auction():
    # Fetch the highest bid
    conn = sqlite3.connect('auction.db')
    c = conn.cursor()
    c.execute('SELECT user, amount FROM bids ORDER BY amount DESC LIMIT 1')
    highest_bid = c.fetchone()
    conn.close()

    return render_template('auction.html', highest_bid=highest_bid)

@app.route('/bid', methods=['POST'])
def place_bid():
    user = request.form['user']
    amount = float(request.form['amount'])

    # Insert new bid
    conn = sqlite3.connect('auction.db')
    c = conn.cursor()
    c.execute('INSERT INTO bids (user, amount, timestamp) VALUES (?, ?, ?)', 
              (user, amount, int(time.time())))
    conn.commit()
    conn.close()

    return redirect(url_for('auction'))

@app.route('/api/bids', methods=['GET'])
def get_bids():
    conn = sqlite3.connect('auction.db')
    c = conn.cursor()
    c.execute('SELECT user, amount FROM bids ORDER BY amount DESC')
    bids = c.fetchall()
    conn.close()
    return jsonify(bids)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
