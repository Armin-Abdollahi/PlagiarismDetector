def safe_text(value: str) -> str:
    return (value or "").strip()


def to_percentage(value: float) -> float:
    try:
        return round(max(0.0, min(100.0, float(value))), 2)
    except:
        return 0.0


def build_response(scores: dict, highlight_ref: str, highlight_sus: str) -> dict:
    return {
        "scores": {
            "lexical": to_percentage(scores.get("lexical", 0)),
            "semantic": to_percentage(scores.get("semantic", 0)),
            "structure": to_percentage(scores.get("structure", 0))
        },
        "highlight_ref": highlight_ref or "",
        "highlight_sus": highlight_sus or ""
    }
