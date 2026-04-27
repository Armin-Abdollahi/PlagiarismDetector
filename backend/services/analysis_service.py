from models import compare_texts, preprocess_for_similarity


def analyze_texts(reference_text: str, suspect_text: str) -> dict:
    ref_processed = preprocess_for_similarity(reference_text)
    sus_processed = preprocess_for_similarity(suspect_text)

    result = compare_texts(ref_processed, sus_processed)

    return {
        "scores": result.get("scores", {
            "lexical": 0.0,
            "semantic": 0.0,
            "structure": 0.0
        }),
        "highlight_ref": result.get("highlight_ref", ""),
        "highlight_sus": result.get("highlight_sus", "")
    }
