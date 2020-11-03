from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Global varibale for storing todos
todos = []

@app.route("/")
def tasks():
	return render_template("tasks.html", todos=todos)
# We need to specify additional methods, since route by default
# accepts just GET!
@app.route("/add", methods=["GET", "POST"])
def add():
	# If get, just show the content
	if request.method == "GET":
		return render_template("add.html")
		# if POST, grab the data from the form
	else:
		# grab task from post request
		todo = request.form.get("task")
		# append to the array
		todos.append(todo)
		# redirect to home page where tasks are shown
		return redirect("/")

