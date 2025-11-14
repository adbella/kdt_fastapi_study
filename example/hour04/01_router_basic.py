# 'APIRouter'로 라우트 분리
from fastapi import APIRouter, FastAPI

router = APIRouter(prefix="/intents", tags=["intents"])

def list_intents() -> list[str]:
    """지원하는 의도 목록을 반환합니다."""
    return ["greeting", "question", "answer", "feedback"]

@router.get("/")
def intents_endspoints() -> dict:
    return {"intents": list_intents()}

app = FastAPI(docs_url='/api/docs', openapi_url='/api/openapi.json')
app.include_router(router)

if __name__ == "__main__":
    # uvicorn -- reload example.hour04.01_router_basics:app
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8888)