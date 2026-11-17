# UTJES Submission — بيانات جاهزة للنسخ في نموذج الرفع

## الملفان المطلوبان (شرط المجلة: ملفان)

| # | الملف | الوصف |
|---|---|---|
| 1 | `TinyML_IDS_UTJES_Submission_v1.docx` | **بكامل بيانات المؤلفة** (الاسم، الجهة، الإيميل) |
| 2 | `TinyML_IDS_UTJES_Submission_v1_ANONYMOUS.docx` | **مُعمّاة** — بلا أي معلومة عن المؤلفة (للمراجعة المزدوجة) |

⚠️ ارفعي **الملفين معاً**. النسخة المُعمّاة نُظّفت أيضاً من بيانات Word المخفية (كانت تحمل الاسم).

---

## Title (للنسخ في خانة العنوان)

```
Lightweight Explainable TinyML Framework for AIoT Intrusion Detection: Integrating TinyCNN, Post-Training Quantization, and SHAP Analysis
```

## Section
```
Articles
```

## Abstract (للنسخ في خانة الملخّص)

```
Kilobytes. That's the memory budget that is available on a microcontroller-class AIoT node, and it's the ceiling within which intrusion detection systems must operate if they are to run at the edge at all. We confront this limitation directly by offering a lightweight and explainable TinyML framework validated on the CICIoT2023 dataset. A feature pipeline — zero-variance elimination, correlation pruning, then Random Forest importance ranking — reduced 47 traffic features to a compact set of 20. Two TinyML architectures are developed and compared: a lightweight multilayer perceptron (MLP, 1,217 parameters) and a one-dimensional convolutional neural network (TinyCNN, 2,401 parameters), both converted to quantized TensorFlow Lite models. The TinyCNN achieves 99.22% accuracy and 99.21% F1-score on a balanced evaluation subset (representing an upper bound for performance; see Section 3.3), with ROC-AUC of 0.9981 and PR-AUC of 0.9985, a deployment size of 7.27 KB (an 8.2× compression over the original floating-point model), and an average software-profiled inference latency of 0.0102 ms — 37% below the MLP at statistically comparable accuracy. Multi-seed robustness evaluation across five independent random seed configurations confirmed highly stable predictive behavior with accuracy of 0.9922 ± 0.0004 and F1-score of 0.9921 ± 0.0004. SHAP analysis points to rst_count, IAT, Number, and Variance as the features doing most of the work behind the model's intrusion decisions. The agreement with known attack signatures suggests the model learned something real, not just dataset artifacts. Accurate, explainable, deployment-ready IDS models can fit inside the memory and compute budget of microcontroller-class AIoT hardware. We do not claim more than that.
```

## Keywords (10)
```
TinyML; AIoT; Intrusion Detection System; TinyCNN; TensorFlow Lite; Quantization; Explainable AI; SHAP; CICIoT2023; Edge Security
```

## بيانات المؤلفة (للنموذج، لا للملف المُعمّى)
- الاسم: Suad Shatti Azeez
- الجهة: Department of Information Technology, Ministry of Education, Baghdad, Iraq
- الإيميل: suad.hr06@gmail.com

---

## حالة قائمة شروط المجلة

| الشرط | الحالة |
|---|---|
| اتّباع قالب المجلة بدقّة | ✅ مطابَق (جرد شامل للحدود والأنماط والترقيم) |
| **ملفان: بالبيانات + بلا بيانات** | ✅ جاهزان |
| عدم النشر مسبقاً / موافقة المؤلفين | ✅ إقرارك (ورقة أصلية) |
| مواد نُشرت في مؤتمرات | ✅ لا ينطبق |
| روابط/DOI للمراجع | ✅ 20 من 21 (المرجع [3] كتاب — الشرط "حيث توفّرت") |
| نص أحادي التباعد، بلا تسطير | ✅ صفر تسطير · تباعد 1.05 (قيمة القالب نفسه) |
| الأشكال والجداول داخل النص | ✅ 6 أشكال + 4 جداول = 10 (الحد الأقصى) |
| عدد الكلمات ≤ 7,500 | ✅ ~3,975 |
| المراجع ≤ 40 | ✅ 21 |
| التشابه < 20% | ✅ 4% |

### 🔴 نقطة واحدة تحتاج قرارك
حجم الخط في **قالب المجلة نفسه = 10.5pt**، بينما نص القائمة يقول "10-point". أبقيتُه 10.5 مطابقاً للقالب (لأن الشرط الأول يقول "يجب اتّباع القالب بدقّة"). إن أردتِ 10pt حرفياً، أخبريني وأغيّره في دقيقة — لكن ذلك سيخالف القالب.

### 🔴 قبل الرفع — أُذكّرك بالمعلّق
- **علم "Hidden Text"** في فحص Turnitin السابق أُصلح على نسخة `V15_clean` لكن هذه المخطوطة بُنيت من قالب المجلة (جداول جديدة بنص أسود) — لا نص أبيض فيها. **يُستحسن فحص Turnitin أخير على ملف التقديم النهائي** للتأكد من زوال العلم ومن نسبة الذكاء.
- نموذج Declaration Form + سيرة المؤلفة (ملف منفصل) — مطلوبان من المجلة، تُعدّهما أنتِ.
