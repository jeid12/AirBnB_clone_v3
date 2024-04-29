from flask import Flask
from api.v1 import views as app_views
from models import storage

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_db(exception):
    """Close the database connection"""
    storage.close()

if __name__ == "__main__":
    import os
    
    # Set host and port from environment variables or default values
    host = os.environ.get("HBNB_API_HOST", "0.0.0.0")
    port = int(os.environ.get("HBNB_API_PORT", 5000))
    
    # Run the Flask server
    app.run(host=host, port=port, threaded=True)

