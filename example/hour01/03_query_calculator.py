from fastapi import FastAPI

# FastAPI 문서 페이지 경로를 /api/docs,
# 스펙 JSON 경로를 /api/openapi.json으로 지정하는 설정.
app = FastAPI(docs_url='/api/docs', openapi_url='/api/openapi.josn')

def add_numbers(a: float, b: float) -> dict:
    """두 수의 합과 차를 반환합니다."""
    return {"sum":a + b, "difference": a - b}
@app.get("/math/add")
def add_endpoint(a :float = 0.0, b: float =0.0) -> dict:
    return add_numbers(a,b)

if __name__ == "__main__":
    # uvicorn --reload exmaple.hour01.03_query_calculator:app
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8888)