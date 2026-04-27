from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <body>
        <h1>Hello from Azure App Service</h1>
        <p>Deployment successful.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
