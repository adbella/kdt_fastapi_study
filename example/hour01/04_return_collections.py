from fastapi import FastAPI

app = FastAPI(docs_url='/api/docs', openapi_url='/api/openapi.json')

COURSE_TOPICS = ["fastapi_intro", "http-basics", "json", "unicorn"]

def get_course_topics() -> dict:
    """강의 토픽을 리스트로 제공하고, 리스트 개수 카운트."""
    return {"topics": COURSE_TOPICS, "count": len(COURSE_TOPICS)}

@app.get("/course/topics")
def topics_endpoint() -> dict:
    return get_course_topics()

if __name__ == "__main__":
    # uvicorn --reload example.hour01.04_return_collections:app
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8888)