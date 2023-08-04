from flask import Flask

# Import Flask to allow us to create our app

# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# (PAUL NOTES) @ is the the decorator and .route is the METHOD
# (PAUL NOTES) The "@" decorator associates this route with the function immediately following
@app.route("/")
def hello_world():
    return "Hello Paul's World!"


@app.route("/success")
def success():
    return "success"


@app.route("/hello/<name>")
def hello(name):
    print(name)
    return "Hello, " + name


# (PAUL NOTES)for a route '/users/____/____', two parameters in the url get passed as username and id


@app.route("/users/<username>/<id>")
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id


# (PAUL NOTES) The localhost:5000 part of the route determines which server to call upon. The rest of the route, including the "/", tells the server which function should be invoked.


# Here the second parameter is cast into an integer before being passed to the function
@app.route("/hello/<name>/<int:num>")
def hellox(name, num):
    return f"Hello, {name * num}"


# (PAUL NOTES) Ensure this file is being run directly and not from a different module
if __name__ == "__main__":
    app.run(debug=True)
# (PAUL NOTES)--ONLY ADD WHILE IN DEVELOPING. to turn debug off just take the debug=True out of the parameter
# (PAUL NOTES)if the port 5000 is already in use for another flask project use the following solution in the app.run (parameter)
#       app.run(debug=True, host="localhost", port=8000)
