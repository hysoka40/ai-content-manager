from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AI Content Manager</title>
        <style>
            body { font-family: system-ui, sans-serif; background: #0f172a; color: white; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; text-align: center; }
            .card { background: #1e293b; padding: 2rem; border-radius: 1rem; box-shadow: 0 10px 25px rgba(0,0,0,0.5); max-width: 400px; width: 90%; }
            h1 { color: #38bdf8; margin-bottom: 0.5rem; }
            p { color: #94a3b8; }
            button { background: #0284c7; color: white; border: none; padding: 10px 20px; border-radius: 0.5rem; font-size: 1rem; cursor: pointer; margin-top: 1rem; }
            button:hover { background: #0369a1; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>AI Content Manager</h1>
            <p>منصتك لإدارة وتوليد المحتوى بالذكاء الاصطناعي تعمل الآن بنجاح!</p>
            <button onclick="alert('التطبيق متصل بالخادم بنجاح!')">تجربة النظام</button>
        </div>
    </body>
    </html>
    """
