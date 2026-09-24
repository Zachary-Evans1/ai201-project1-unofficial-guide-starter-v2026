from __future__ import annotations

import re
from typing import Iterable

def _normalize_text(text: str | None) -> str:
    """Normalize text by lowercasing and removing punctuation."""
    if not text:
        return ""
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return " ".join(text.split())

def judge(question: str, expects: str, answer: str | None, results) -> bool:
    """Judge the answer against the expected answer."""
    normalized_expects = _normalize_text(expects)
    normalized_answer = _normalize_text(answer)

    expected_words = normalized_expects.split()
    answer_words = normalized_answer.split()

    return all(word in answer_words for word in expected_words)