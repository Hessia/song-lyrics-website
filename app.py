from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

def get_db_connection():
    conn = sqlite3.connect('songs.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    conn = get_db_connection()
    genres = conn.execute('SELECT DISTINCT genre FROM songs').fetchall()
    conn.close()
    return render_template('home.html', genres=genres)

@app.route('/genre/<genre>')
def genre_page(genre):
    conn = get_db_connection()
    songs = conn.execute('SELECT * FROM songs WHERE genre = ?', (genre,)).fetchall()
    conn.close()
    return render_template('genre.html', genre=genre, songs=songs)

@app.route('/song/<int:song_id>')
def song_page(song_id):
    conn = get_db_connection()
    song = conn.execute('SELECT * FROM songs WHERE id = ?', (song_id,)).fetchone()
    conn.close()
    return render_template('song.html', song=song)

@app.route('/search')
def search():
    query = request.args.get('query')
    conn = get_db_connection()
    results = conn.execute("SELECT * FROM songs WHERE title LIKE ? OR artist LIKE ?", 
                           (f'%{query}%', f'%{query}%')).fetchall()
    conn.close()
    return render_template('search_results.html', query=query, results=results)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        conn.close()
        flash('Sign up successful!', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()
        
        if user and user['password'] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash("Logged out.")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
