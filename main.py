
from fastapi import FastAPI
from routes.route import router
app = FastAPI() 

@app.get('/')
def getmain():
    return 'hi python api res'

app.include_router(router)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)