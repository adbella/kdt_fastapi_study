# 반복 데이터(list) 검증 후 요약 응답
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(docs_url='/api/docs', openapi_url='/api/openapi.json')

class BatchScores(BaseModel):
    # 기본으로 보일 example 값 추가해놓음
    scores: List[float] = Field([0.1, 0.2, 0.3, 0.4], description="0~1 사이 점수")

def summarize_scores(payload: BatchScores) -> dict:
    """점수  리스트의 평균과 최고점을 계산합니다."""
    if not payload.scores:
        return {"count": 0, "mean": None, "max": None}
    total = sum(payload.scores)
    count = len(payload.scores)
    return {"count" :count, "mean": total / count, "max": max(payload.scores)}

@app.post("/scores/summary")
def scores_endpoint(payload: BatchScores) -> dict:
    return summarize_scores(payload)

if __name__ == "__main__":
    # uvicorn --reload example.hour03.02_list_validation:app
    import uvicorn
    
    uvicorn.run(app, host="127.0.0.1", port=8888)
