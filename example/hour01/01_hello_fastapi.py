from fastapi import FastAPI

app = FastAPI(docs_url='/api/docs',openapi_url='/api/openapi.json')

@app.get("/hello")
def say_hello() -> dict:
    return {"message": "Hello, fastapi leaarners!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8888)