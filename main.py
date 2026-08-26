import json
import urllib.request
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

# ضع المفتاح النصي الذي نسخته من Google AI Studio بين القوسين
GEMINI_API_KEY = "ألصق_مفتاح_API_هنا"

class ContentRequest(BaseModel):
    topic: str

@app.post("/generate")
def generate_content(req: ContentRequest):
    if not GEMINI_API_KEY or GEMINI_API_KEY == "ألصق_مفتاح_API_هنا":
        return {"result": f"✨ تم استلام موضوعك: '{req.topic}'.\n\n(يرجى استبدال نص المفتاح بـ API Key الحقيقي داخل main.py)."}

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{"parts": [{"text": f"اكتب قصصاً أو محتوى مفصلاً وإبداعياً باللغة العربية حول: {req.topic}"}]}]
    }

    try:
        req_data = json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(url, data=req_data, headers=headers)
        with urllib.request.urlopen(request) as response:
            res_json = json.loads(response.read().decode("utf-8"))
            generated_text = res_json["candidates"][0]["content"]["parts"][0]["text"]
            return {"result": generated_text}
    except Exception as e:
        return {"result": f"حدث خطأ أثناء الاتصال بالذكاء الاصطناعي: {str(e)}"}

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
            body { font-family: system-ui, sans-serif; background: #0f172a; color: white; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; padding: 10px; }
            .card { background: #1e293b; padding: 2rem; border-radius: 1rem; box-shadow: 0 10px 25px rgba(0,0,0,0.5); max-width: 500px; width: 100%; text-align: center; }
            h1 { color: #38bdf8; margin-bottom: 0.5rem; font-size: 1.5rem; }
            input { width: 100%; padding: 12px; margin: 15px 0; border-radius: 0.5rem; border: 1px solid #334155; background: #0f172a; color: white; box-sizing: border-box; }
            button { background: #0284c7; color: white; border: none; padding: 12px; border-radius: 0.5rem; font-size: 1rem; cursor: pointer; width: 100%; font-weight: bold; }
            button:hover { background: #0369a1; }
            #output { margin-top: 15px; padding: 15px; background: #0f172a; border-radius: 0.5rem; text-align: right; white-space: pre-line; color: #e2e8f0; display: none; max-height: 300px; overflow-y: auto; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>AI Content Manager</h1>
            <p style="color:#94a3b8; font-size:0.9rem;">أدخل الموضوع لتوليد النص بواسطة Gemini AI</p>
            <input type="text" id="topic" placeholder="مثال: قصة خيالية أو واقعية...">
            <button onclick="generate()">توليد المحتوى</button>
            <div id="output"></div>
        </div>
        <script>
            async function generate() {
                const topic = document.getElementById('topic').value;
                if(!topic) return alert('يرجى كتابة موضوع أولاً');
                const out = document.getElementById('output');
                out.style.display = 'block';
                out.innerText = '⏳ جاري كتابة المحتوى بواسطة الذكاء الاصطناعي...';
                const res = await fetch('/generate', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({topic})
                });
                const data = await res.json();
                out.innerText = data.result;
            }
        </script>
    </body>
    </html>
    """
