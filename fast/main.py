from fastapi import FastAPI
app =FastAPI()

@app.get('/')
def home():
    return "Hello from fastapi!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)