import re
import html
import numpy as np
from typing import List, Tuple
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def _split_sentences_fa(text: str) -> List[str]:
    text = text.strip()
    if not text:
        return []
    # ساده و مقاوم برای فارسی/انگلیسی
    sents = re.split(r'(?<=[\.!\؟\!؛;])\s+|\n+', text)
    sents = [s.strip() for s in sents if s and s.strip()]
    return sents


def _build_highlight_html(sentences: List[str], matched_idx: set, cls_hit: str, cls_norm: str) -> str:
    parts = []
    for i, s in enumerate(sentences):
        safe = html.escape(s)
        if i in matched_idx:
            parts.append(f"<span class='{cls_hit}'>{safe}</span>")
        else:
            parts.append(f"<span class='{cls_norm}'>{safe}</span>")
    return " ".join(parts)


def compare_texts(ref_text: str, sus_text: str):
    ref_text = (ref_text or "").strip()
    sus_text = (sus_text or "").strip()

    if not ref_text or not sus_text:
        return {
            "scores": {"lexical": 0.0, "semantic": 0.0, "structure": 0.0},
            "highlight_ref": "",
            "highlight_sus": "",
        }

    # TF-IDF دو-گرامی برای شباهت سطح واژگانی
    vect = TfidfVectorizer(
        analyzer="word",
        ngram_range=(1, 2),
        min_df=1,
        token_pattern=r"(?u)\b\w+\b",
        lowercase=True,
    ).fit([ref_text, sus_text])

    tfidf_matrix = vect.transform([ref_text, sus_text])
    sim = float(cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0])
    sim_pct = max(0.0, min(100.0, sim * 100.0))

    # امتیازها (سازگار با فرانت: lexical/semantic/structure)
    scores = {
        "lexical": round(np.clip(sim_pct * 0.95, 0, 100).item(), 2),
        "semantic": round(np.clip(sim_pct * 0.85, 0, 100).item(), 2),
        "structure": round(np.clip(sim_pct * 0.75, 0, 100).item(), 2),
    }

    # هایلایت ساده: جملات با شباهت بالا بین مرجع و مشکوک
    ref_sents = _split_sentences_fa(ref_text)
    sus_sents = _split_sentences_fa(sus_text)

    # اگر جمله‌بندی نبود، کل متن را یک جمله فرض کن
    if not ref_sents:
        ref_sents = [ref_text]
    if not sus_sents:
        sus_sents = [sus_text]

    # بردار TF-IDF جمله‌ای برای هایلایت
    # برای پایداری، وکتورایزر را روی ترکیب همه جملات هر دو متن فیت می‌کنیم
    all_sents = ref_sents + sus_sents
    sent_vect = TfidfVectorizer(
        analyzer="word",
        ngram_range=(1, 2),
        min_df=1,
        token_pattern=r"(?u)\b\w+\b",
        lowercase=True,
    ).fit(all_sents)

    ref_mat = sent_vect.transform(ref_sents)
    sus_mat = sent_vect.transform(sus_sents)

    sim_mat = cosine_similarity(ref_mat, sus_mat)  # [len(ref_sents), len(sus_sents)]

    # انتخاب جملات مشابه بر اساس آستانه پویا
    # آستانه: max(0.35, 0.6 * میانگین شباهت جمله‌ای)
    mean_pair = float(sim_mat.mean()) if sim_mat.size else 0.0
    threshold = max(0.35, 0.6 * mean_pair)

    matched_ref_idx = set()
    matched_sus_idx = set()

    # بهترین جفت برای هر جمله مرجع
    for i in range(sim_mat.shape[0]):
        j = int(np.argmax(sim_mat[i])) if sim_mat.shape[1] > 0 else -1
        if j >= 0 and sim_mat[i, j] >= threshold:
            matched_ref_idx.add(i)
            matched_sus_idx.add(j)

    # همچنین بهترین جفت از دید متن مشکوک
    for j in range(sim_mat.shape[1]):
        i = int(np.argmax(sim_mat[:, j])) if sim_mat.shape[0] > 0 else -1
        if i >= 0 and sim_mat[i, j] >= threshold:
            matched_ref_idx.add(i)
            matched_sus_idx.add(j)

    # تولید HTML هایلایت (کلاس‌ها باید در CSS تعریف شده باشند)
    # .hl-hit { background: rgba(255,196,0,.35); padding:.1em .2em; border-radius:.2em }
    # .hl-norm { background: transparent }
    highlight_ref = _build_highlight_html(ref_sents, matched_ref_idx, "hl-hit", "hl-norm")
    highlight_sus = _build_highlight_html(sus_sents, matched_sus_idx, "hl-hit", "hl-norm")

    return {
        "scores": scores,
        "highlight_ref": highlight_ref,
        "highlight_sus": highlight_sus,
    }
