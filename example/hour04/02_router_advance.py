from fastapi import APIRouter, FastAPI

router_car = APIRouter(prefix="/api/car", tags=["car"])
router_train = APIRouter(prefix="/api/train", tags=["train"])

def get_start() -> dict:
    return {"function": "start"}

def get_go() -> dict:
    return {"function": "go"}

def get_back() -> dict:
    return {"function": "back"}

def get_end() -> dict:
    return {"function": "end"}

@router_car.get("/start")
def car_start() -> dict:
    return get_start()

@router_car.get("/go")
def car_go() -> dict:
    return get_go()

@router_car.get("/back")
def car_back() -> dict:
    return get_back()

@router_car.get("/end")
def car_end() -> dict:
    return get_end()

@router_train.get("/start")
def train_start() -> dict:
    return get_start()

@router_train.get("/go")
def train_go() -> dict:
    return get_go()

@router_train.get("/back")
def train_back() -> dict:
    return get_back()

@router_train.get("/end")
def train_end() -> dict:
    return get_end()

app = FastAPI(docs_url='/api/docs', openapi_url='/api/openapi.json')
app.include_router(router_car)
app.include_router(router_train)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8888)