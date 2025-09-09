import logging


logger = logging.getLogger(__name__)


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    end = start + size
    fragment = text[start:end]
    last_punct_idx = 0

    if end < len(text) and text[end] in '.,:;!?':
        fragment = fragment.rsplit(' ', 1)[0]

    for idx, char in enumerate(fragment, 1):
        if char in '.,:;!?':
            last_punct_idx = idx

    page_text = fragment[:last_punct_idx]
    return page_text, len(page_text)


def prepare_book(path: str, page_size: int = 1050) -> dict[int, str]:
    start = 0
    page_namber = 1
    book = {}

    with open(path, 'r', encoding="utf-8") as files:
        text = files.read()

    while start < len(text):
        page_text, length = _get_part_text(text, start, page_size)
        if page_text:
            book.setdefault(page_namber, page_text.lstrip())
            page_namber += 1
            start += length
        else:
            break
        
    return book