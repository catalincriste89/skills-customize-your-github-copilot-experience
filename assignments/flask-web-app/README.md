# 📘 Assignment: Building Your First Web Application with Flask

## 🎯 Objective

Learn the fundamentals of web development by building a simple web application using Flask. You'll create routes, render HTML templates, and handle user input through web forms.

## 📝 Tasks

### 🛠️ Task 1: Create Your First Flask App with Routing

#### Description
Build a Flask application with multiple routes that respond to different URLs. This task teaches you the basics of web servers and URL routing.

#### Requirements
Completed program should:

- Create a Flask application instance
- Define a home route (`/`) that returns "Welcome to My Flask App!"
- Define an about route (`/about`) that returns "This is my first web application"
- Define a dynamic route (`/greet/<name>`) that greets the user by name (e.g., `/greet/Alice` returns "Hello, Alice!")
- Run the Flask development server without errors

**Example interaction:**
```
Visit http://localhost:5000/ → "Welcome to My Flask App!"
Visit http://localhost:5000/about → "This is my first web application"
Visit http://localhost:5000/greet/Bob → "Hello, Bob!"
```


### 🛠️ Task 2: Use HTML Templates for Your Pages

#### Description
Replace plain text responses with proper HTML templates. Learn how Flask's templating engine (Jinja2) makes building dynamic web pages easier.

#### Requirements
Completed program should:

- Create a `templates/` folder in your project directory
- Create `home.html` template for the home page with a title, heading, and a list of navigation links
- Create `greet.html` template that displays a personalized greeting and the current timestamp
- Use Jinja2 variable substitution to pass data from your Python code to HTML templates
- Render templates using `render_template()` for both the home and greet routes

**Example structure:**
```
project/
├── app.py
├── templates/
│   ├── home.html
│   └── greet.html
```


### 🛠️ Task 3: Build a Simple Form and Handle Input

#### Description
Create an interactive form where users can submit data. Learn how to handle HTTP POST requests and process form data in Flask.

#### Requirements
Completed program should:

- Create a `feedback.html` template with an HTML form that collects user feedback (name and comment fields)
- Create a `/feedback` GET route that displays the form
- Create a `/feedback` POST route that processes the form submission
- Store the feedback (in memory is fine for this assignment) and display a confirmation message with the user's name
- Display a list of all submitted feedback on a `/feedback-list` page

**Example interaction:**
```
User visits /feedback → form is displayed
User submits form → confirmation message: "Thanks, [name], for your feedback!"
User visits /feedback-list → all feedback is displayed
```
