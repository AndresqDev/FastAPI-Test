from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/login/static",
          StaticFiles(directory="login/static"),
          name="login/static")


def read_file(file_path):
  with open(file_path, 'r') as file:
    content = file.read()
  return content


@app.post("/login/")
async def loginup(username: str = Form(...), password: str = Form(...)):
  if (username.lower() == "user" and password == "pass"):
    return HTMLResponse(content=read_file("login/static/1.5.2.html"),
                        status_code=200)
  else:
    return HTMLResponse(content=read_file("login/static/login.html"),
                        status_code=200)


@app.get("/")
async def root():
  return HTMLResponse(content=read_file("login/static/login.html"),
                      status_code=200)
