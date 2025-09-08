import logging
import os


logger = logging.getLogger(__name__)


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    punctuation = ',.!:;?'
    end = size + 1
    page_text = text[start:end]
    page_size = len(page_text)
    
    while size >= 0:
        if page_text[size] in punctuation:
            if size > 0 and (page_text[size-1] in punctuation or page_text[page_size] in punctuation):
                size -= 1
                continue
            break
        else:
            break

    return page_text, page_size


def prepare_book(path: str, page_size: int = 1050) -> dict[int, str]:
    book = {}

    # ...

    return book