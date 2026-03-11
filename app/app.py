from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>🚀 DevOps AI Project</h1>
    <p>My CI/CD Pipeline is running!</p>
    '''

@app.route('/health')
def health():
    return {
        "status": "healthy",
        "message": "App is running fine!"
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)