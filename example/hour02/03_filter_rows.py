import pandas as pd
from fastapi import FastAPI

app = FastAPI(docs_url='/api/docs', openapi_url='/api/openapi.json')

CHAT_LOG =pd.DataFrame(
    {
        "turn": [1, 2, 3, 4, 5],
        "speaker": ["user", "bot", "user", "bot", "user"],
        "intent": ["greeting", "welcome", "question", "answer", "feedback"], 
    }
)

def filter_by_intent(intent: str) -> list[dict]:
    """특정 의도(intent)만 선택합니다."""
    filtered = CHAT_LOG.loc[CHAT_LOG["intent"] == intent]
    return filtered.to_dict(orient="records")

@app.get("/chat/filer")
def filter_endpoint(intent: str) -> dict:
    return {"intent": intent, "records": filter_by_intent(intent)}

if __name__ == "__main__":
    # uvicorn --reload example.hour02.03_filter_rows:app
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8888)