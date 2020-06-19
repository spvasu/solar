from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from contactEmailScript import sendEmail
import MySQLdb.cursors, sys
import smtplib
import re

app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'your secret key'

#database connection details
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'asulab'
app.config['MYSQL_DB'] = 'solarpvdb'

# Intialize MySQL
mysql = MySQL(app)

@app.route("/", methods=['GET'])
def main():
    return render_template("home.html")


#about page logic
@app.route("/about")
def about():
    return render_template("about.html")


#contact page logic
@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['txtName']
        email = request.form['txtEmail']
        phone = request.form['txtPhone']
        msg = request.form['txtMsg']

        #testing, printing to console in browser
        #https://stackoverflow.com/questions/32550487/how-to-print-from-flask-app-route-to-python-console
        print('This is a TEST MESSAGE', file=sys.stderr)
        print('Username: %s', name, file=sys.stderr)
        print('Phone: %s', phone, file=sys.stderr)
        print('Email: %s', email, file=sys.stderr)
        print('Msg: %s', msg, file=sys.stderr)

        sendEmail(name, email, phone, msg)
        print('Email was sen!t', file=sys.stderr)

        return redirect('contactCompleted.html')



    else:
        return render_template("contact.html")


#registration page logic
@app.route("/registration")
def registration():
    return render_template("registration.html")

#login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():

    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:

        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']

        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM customers WHERE Cemail = %s AND cPassword = %s', (username, password))

        # Fetch one record and return result
        currentUser = cursor.fetchone()

        # If account exists in accounts table in out database
        if currentUser:

            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = currentUser['id']
            session['username'] = currentUser['username']

            # Redirect to home page
            return 'Logged in successfully!'

        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'

    else:
        return render_template("login.html")


# http://localhost:5000/python/logout - this will be the logout page
@app.route('/logout')
def logout():

    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))


if __name__ == "__main__":
    app.run()
