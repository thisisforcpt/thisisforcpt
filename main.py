from flask import Flask
from flask import render_template
from flask import request
import database_manager as dbHandler

app = Flask(__name__)

@app.route('/main.html', methods=['GET'])
@app.route('/', methods=['POST', 'GET'])
def index():
  return render_template('/main.html')

@app.route('/aboutsoccer.html', methods=['GET'])
@app.route('/', methods=['POST', 'GET'])
def aboutsoccer():
    return render_template('/aboutsoccer.html')

@app.route('/rules.html', methods=['GET'])
@app.route('/', methods=['POST', 'GET'])
def rules():
    return render_template('/rules.html')


@app.route('/friends.html', methods=['GET'])
def friends():
    return render_template('friends.html')

@app.route('/buyhajcoin.html', methods=['GET'])
def buyhajcoin():
    return render_template('buyhajcoin.html')

@app.route('/contactus.html', methods=['GET'])
def contactus():
    return render_template('contactus.html')

@app.route('/signup.html', methods=['GET'])
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5100)

# hajmedia sign up

@app.route('/1hajcoinpurchase.png', methods=['GET'])
def hajcoin_image():
    return app.send_static_file('1hajcoinpurchase.png')

@app.route('/2hajcoinpurchase.png', methods=['GET'])
def hajcoin_image():
    return app.send_static_file('2hajcoinpurchase.png')

@app.route('/3hajcoinpurchase.png', methods=['GET'])
def hajcoin_image():
    return app.send_static_file('3hajcoinpurchase.png')

# posts

import sqlite3
import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/main.html')
def main():
    conn = sqlite3.connect('data_source.db')
    c = conn.cursor()

    # Get 100 random posts
    c.execute("SELECT * FROM hajmediaposts")
    all_posts = c.fetchall()
    conn.close()

    # Randomly select 100 posts
    random.shuffle(all_posts)
    posts = all_posts[:100]

    # Format posts as list of dictionaries
    post_list = [{
        'user_id': p[0],
        'username': p[1],
        'content': p[2],
        'date': p[3],
        'likes': p[4],
        'comments': p[5],
        'shares': p[6],
        'hashtags': p[7],
        'tagged_users': p[8]
    } for p in posts]

    return render_template('main.html', posts=post_list)