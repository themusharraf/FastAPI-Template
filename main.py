from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

colors = [{"name": "red", "type": "HTML"}, {"name": "Blue", "type": "Python"}]


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("main.html", {"request": request, "user": "All nc", "colors": colors})
