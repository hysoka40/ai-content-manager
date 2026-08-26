
# تشغيل المساعد من الهاتف عبر Cloud

## الخيار المقترح: Render
1. أنشئ حساباً في Render.
2. ارفع المشروع إلى GitHub.
3. في Render اختر New Web Service.
4. اربط مستودع GitHub.
5. Build Command:
   pip install -r requirements.txt
6. Start Command:
   uvicorn app.main:app --host 0.0.0.0 --port $PORT
7. Deploy.
8. افتح رابط الخدمة من Android Chrome.
9. اختر "Add to Home screen" لإضافته كأنه تطبيق.

## قبل الإنتاج
- غيّر AI_PROVIDER من mock إلى مزود AI حقيقي.
- أضف OAuth للمنصات.
- استخدم PostgreSQL بدلاً من SQLite عند النشر.
- أضف تسجيل دخول للمستخدم.
- اترك AUTO_PUBLISH=false حتى تختبر النظام.
