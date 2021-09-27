from flask import render_template
import connexion

# Creating application instance
app = connexion.App(__name__, specification_dir="./")

# Read swagger .yml file to configure API endpoints
app.add_api("swagger.yml")

# Creating URL route for home page "/"
@app.route("/")         # Decorator for "/" URL to associate w/following function
def home():
    """
    Respond to request for home page
    
    :return:    rendered template home.html
    """
    return render_template("home.html")

if __name__== "__main__":
    app.run(debug=True)
    