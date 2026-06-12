"""
Flask Web Application Starter Code

This is the starting point for building your first Flask web application.
Complete the tasks in the assignment to build out the functionality.

To run this app:
1. Install Flask: pip install flask
2. Run the app: python starter-code.py
3. Visit http://localhost:5000 in your browser
"""

from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Store feedback in memory (resets when app restarts)
feedback_list = []


# TODO: Task 1 - Create your first Flask routes
# Create a home route that returns "Welcome to My Flask App!"
@app.route('/')
def home():
    pass  # Replace with your code


# TODO: Create an about route that returns "This is my first web application"
@app.route('/about')
def about():
    pass  # Replace with your code


# TODO: Create a dynamic greet route that takes a name parameter
@app.route('/greet/<name>')
def greet(name):
    pass  # Replace with your code


# TODO: Task 2 - Use HTML templates
# Modify the home() function to render home.html template
# Modify the greet() function to render greet.html template with the name and current timestamp


# TODO: Task 3 - Build a feedback form
# Create a route for displaying the feedback form (GET request)
@app.route('/feedback', methods=['GET'])
def feedback_form():
    pass  # Replace with your code


# Create a route for processing the feedback form (POST request)
@app.route('/feedback', methods=['POST'])
def submit_feedback():
    pass  # Replace with your code


# Create a route for displaying all feedback
@app.route('/feedback-list')
def feedback_list_page():
    pass  # Replace with your code


if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True, host='localhost', port=5000)
