from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

class ContentRequest(BaseModel):
    topic: str

@app.post("/generate")
def generate_content(req: ContentRequest):
    # هنا يمكنك ربط API خارجي مثل OpenAI أو Gemini مستقبلاً
    generated_text = f"✨ تم إنشاء المحتوى بنجاح لموضوع: '{req.topic}'\n\n- نقطة رئيسية 1: تحليل وإعداد الاستراتيجية.\n- نقطة رئيسية 2: التنفيذ والتوليد التلقائي.\n- نقطة رئيسية 3: المراجعة والنشر."
    return {"result": generated_text}

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
            body { font-family: system-ui, sans-serif; background: #0f172a; color: white; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }
            .card { background: #1e293b; padding: 2rem; border-radius: 1rem; box-shadow: 0 10px 25px rgba(0,0,0,0.5); max-width: 450px; width: 90%; text-align: center; }
            h1 { color: #38bdf8; margin-bottom: 0.5rem; font-size: 1.5rem; }
            input { width: 100%; padding: 10px; margin: 15px 0; border-radius: 0.5rem; border: 1px solid #334155; background: #0f172a; color: white; box-sizing: border-box; }
            button { background: #0284c7; color: white; border: none; padding: 10px 20px; border-radius: 0.5rem; font-size: 1rem; cursor: pointer; width: 100%; }
            button:hover { background: #0369a1; }
            #output { margin-top: 15px; padding: 10px; background: #0f172a; border-radius: 0.5rem; text-align: right; white-space: pre-line; color: #e2e8f0; display: none; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>AI Content Manager</h1>
            <p style="color:#94a3b8; font-size:0.9rem;">أدخل موضوع المحتوى لتوليده بالذكاء الاصطناعي</p>
            <input type="text" id="topic" placeholder="مثال: خطة تسويقية لمشروع جديد...">
            <button onclick="generate()">توليد المحتوى</button>
            <div id="output"></div>
        </div>
        <script>
            async function generate() {
                const topic = document.getElementById('topic').value;
                if(!topic) return alert('يرجى كتابة موضوع أولاً');
                const out = document.getElementById('output');
                out.style.display = 'block';
                out.innerText = 'جاري التوليد...';
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
