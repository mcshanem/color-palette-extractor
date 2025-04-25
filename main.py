from flask import Flask

# Create Flask app
app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello Web!'


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
