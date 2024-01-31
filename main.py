
# Import Flask and other necessary modules
from flask import Flask, render_template, redirect, url_for

# Create a Flask application
app = Flask(__name__)

# Define the routes and connect them to their respective HTML files
@app.route("/")
def home():
    """Render the home page."""
    return render_template("index.html")

@app.route("/features")
def features():
    """Render the page showcasing XF-27's features."""
    return render_template("features.html")

@app.route("/gallery")
def gallery():
    """Render the gallery page displaying XF-27 images and videos."""
    return render_template("gallery.html")

@app.route("/contact")
def contact():
    """Render the contact page with a form for inquiries."""
    return render_template("contact.html")

@app.route("/explore-more")
def explore_more():
    """Redirect to a page with more information about XF-27."""
    return redirect(url_for("more_info"))

# Define an additional route for more information about the XF-27
@app.route("/more-info")
def more_info():
    """Render the page providing more details about the XF-27."""
    return render_template("more_info.html")

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
