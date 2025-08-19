import logging
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

logger = logging.getLogger("fastapi_logger")
logger.setLevel(logging.INFO)

log_path = "/fastapi_logs/fastapi1.log"
handler = logging.FileHandler(log_path, mode="a")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

@app.get("/", response_class=HTMLResponse)
async def login_form():
    return """
    <h2>Login</h2>
    <form action="/login" method="post">
        <label>Username:</label><input type="text" name="username"><br><br>
        <label>Password:</label><input type="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
    """

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    if username == "admin" and password == "1234":
        logger.info(f"Sesión iniciada: {username}")
        handler.flush()  
        return {"message": f"Bienvenido, {username}!"}
    return {"message": "Usuario o contraseña incorrectos"}
