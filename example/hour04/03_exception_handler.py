from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI(docs_url='/api/docs', openapi_url='/api/openapi.json')
              
class TooShortError(ValueError):
    """사용자 정의 예외."""

def validate_length(text: str) -> str:
    if len(text) < 3:
        raise TooShortError("text is too short")
    return text

@app.exception_handler(TooShortError)
async def short_error_handler(_: Request, exc: TooShortError) -> JSONResponse:
    return JSONResponse(status_code=422, content={"detail": str(exc)})

@app.get("/validate")
def validate_endpoint(text: str) -> dict:
    return {"validated": validate_length(text)}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8888)