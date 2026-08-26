# AI Content Manager MVP

FastAPI dashboard لإدارة دورة المحتوى: Generate -> Review -> Approve -> Publish -> Audit.

النسخة الحالية آمنة: النشر الحقيقي غير مفعّل، وتستخدم Mock Publisher.
بعد الاختبار يمكن ربط APIs الرسمية للمنصات.

## تشغيل
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload

افتح http://127.0.0.1:8000

## ملاحظات
- لا تضع مفاتيح API داخل الكود.
- المحتوى يبدأ بحالة pending_approval.
- لا يوجد نشر حقيقي في هذه النسخة.
- أضف OAuth/API adapters بعد اختيار الحسابات والمنصات.

## 🕵️ Crime & Mystery Story Generator
يدعم الخيال والوقائع الموثقة والقضايا غير المحلولة، مع Hook وInvestigation وTwist واقتراح مشاهد وSafety Label.

## 🔎 Research Agent
تمت إضافة Research Agent مبدئي:
Research Query → Research Brief → Sources → Fact-check checklist → Content.

مهم: النسخة الحالية لا تدعي التحقق التلقائي من صحة الأخبار؛ هي طبقة آمنة لتجهيز البحث.
المرحلة الإنتاجية التالية هي ربط Search API رسمي + Page Fetcher + Evidence Extractor + Fact Checker، ثم تمرير الأدلة إلى مولد السيناريو.

## 📱 Mobile / Cloud
تم تجهيز Dashboard ليكون Mobile-first وإضافة `render.yaml` و`DEPLOY_MOBILE.md`.
يمكن نشره على Cloud ثم فتحه من الهاتف وإضافته إلى الشاشة الرئيسية.
النشر الحقيقي للمنصات ما زال مقفلاً افتراضياً حتى تتم إضافة OAuth وواجهات APIs الرسمية.
