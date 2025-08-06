from fastapi import FastAPI


app = FastAPI(version='v1')


@app.get("/")
def root_head():
    return {'status': 'ok'}