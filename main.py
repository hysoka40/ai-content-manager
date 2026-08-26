import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import google.generativeai as genai

# إعداد مفتاح API الخاص بـ Gemini
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "ضع_مفتاح_الـ_API_هنا")
genai.configure(api_key=GEMINI_API_KEY)

app = FastAPI()

class ContentRequest(BaseModel):
    topic: str

@app.post("/generate")
def generate_content(req: ContentRequest):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"اكتب محتوى إبداعي ومفصل حول الموضوع التالي: {req.topic}"
        response = model.generate_content(prompt)
        return {"result": response.text}
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
            <input type="text" id="topic" placeholder="مثال: قصة خيالية عن رائد فضاء...">
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
