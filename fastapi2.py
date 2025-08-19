import logging
from logging.handlers import RotatingFileHandler
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()
fake_users_db = {}

# Configuración del logger
logger = logging.getLogger("fastapi_logger")
logger.setLevel(logging.INFO)

log_path = "/fastapi_logs/fastapi2.log"
handler = RotatingFileHandler(
    log_path,
    maxBytes=5*1024*1024,  # 5 MB por archivo
    backupCount=3           # Mantener 3 archivos de backup
)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <h2>Register</h2>
    <form action="/register" method="post">
        <label>Username:</label><input type="text" name="username"><br><br>
        <label>Password:</label><input type="password" name="password"><br><br>
        <input type="submit" value="Register">
    </form>
    """

@app.post("/register")
async def register(username: str = Form(...), password: str = Form(...)):
    if username in fake_users_db:
        logger.info(f"Usuario ya existente: {username}")
        return {"message": "El usuario ya existe\n"}
    fake_users_db[username] = password
    logger.info(f"Usuario registrado: {username}")
    return {"message": f"Usuario {username} registrado correctamente\n"}
