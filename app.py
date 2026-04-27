from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello from Azure App Service 🚀</h1>
    <p>Deployment Center GitHub deployment is successful.</p>
    """

if __name__ == "__main__":
    app.run()
