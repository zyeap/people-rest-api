from flask import (
    Flask,
    render_template
)

# Creating Flask application instance
app = Flask(__name__, template_folder="templates")

# Creating URL route for home page "/"
@app.route('/')         # Decorator for "/" URL to associate w/following function
def home():
    """
    Respond to request for home page
    
    :return:    rendered template home.html
    """
    return render_template('home.html')

if __name__== '__main__':
    app.run(debug=True)
