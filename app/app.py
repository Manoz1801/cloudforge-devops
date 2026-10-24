from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>CloudForge</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #101827;
                color: white;
                text-align: center;
                padding: 80px 20px;
            }
            .card {
                max-width: 600px;
                margin: auto;
                padding: 35px;
                background: #1e293b;
                border-radius: 15px;
            }
            h1 { color: #38bdf8; }
            .status { color: #4ade80; }
            code { color: #fbbf24; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>CloudForge</h1>
            <h2>Cloud-Native Deployment Platform</h2>
            <p class="status">Application is running!</p>
            <p>Containerized with Docker.</p>
            <p>Ready for Kubernetes deployment.</p>
            <p>Health endpoint: <code>/health</code></p>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
EOF
