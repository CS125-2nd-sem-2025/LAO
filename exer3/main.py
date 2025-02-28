from fastapi import FastAPI, Request
import platform
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def welcome_page():
    return """
    <html>
        <head>
            <title>OS Info API</title>
        </head>
        <body>
            <h1>Welcome!</h1>
            <p>Select an option below:</p>
            <ul>
                <li><a href="/os">Get OS</a></li>
                <li><a href="/version">Get OS Version</a></li>
                <li><a href="/ip">Get IP Address</a></li>
                <li><a href="/all">Get All Info</a></li>
            </ul>
        </body>
    </html>
    """

@app.get("/os")
def get_os():
    return {"os": platform.system()}

@app.get("/version")
def get_version():
    return {"version": platform.version()}

@app.get("/ip")
def get_ip(request: Request):
    client_host = request.client.host if request.client else "Unknown"
    return {"ip": client_host}

@app.get("/all")
def get_all(request: Request):
    return {
        "os": platform.system(),
        "version": platform.version(),
        "ip": request.client.host if request.client else "Unknown"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
