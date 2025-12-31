from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Augmented Analytical Dashboards Backend is running"
    })

@app.route("/health")
def health_check():
    return jsonify({
        "status": "OK",
        "service": "Backend API"
    })

if __name__ == "__main__":
    app.run(debug=True)
