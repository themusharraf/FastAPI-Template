from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

colors = [{"name": "red", "type": "HTML"}, {"name": "Blue", "type": "Python"}]


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("main.html", {"request": request, "user": "All nc", "colors": colors})


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000,)
