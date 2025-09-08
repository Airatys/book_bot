import logging
import os


logger = logging.getLogger(__name__)


def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    end = start + page_size
    fragment = text[start:end]
    last_punct_idx = 0

    if end < len(text) and text[end] in '.,:;!?':
        fragment = fragment.rsplit(' ', 1)[0]

    for idx, char in enumerate(fragment, 1):
        if char in '.,:;!?':
            last_punct_idx = idx

    result = fragment[:last_punct_idx]
    return result, len(result)
