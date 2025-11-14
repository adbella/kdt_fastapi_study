import pandas as pd
from fastapi import FastAPI

app = FastAPI(docs_url='/api/docs', openapi_url='/api/openapi.json')

DATA = pd.DataFrame(
    {
        "speaker": ["user", "bot", "user", "bot"],
        "duration_sec": [1.2, 2.5, 1.8, 2.2],
        "intent": ["greeting", "welcome", "question", "answer"],
    }
)

def build_summary() -> dict:
    """Dataframe의 기본 통계를 딕셔너리로 변환합니다."""
    summary = DATA.describe(include="all").fillna("-")
    return summary.to_dict()

@app.get("/stats/summary")
def summary_endpoint() -> dict:
    return {"raw": DATA.to_dict(orient="records"), "summary": build_summary()}

if __name__ == "__main__":
    # uvicorn --reload example.02.02_pandas_summary:app
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8888)