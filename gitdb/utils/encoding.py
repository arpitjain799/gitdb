from gitdb.utils import compat

if compat.PY3:
    text_type = str
else:
    text_type = unicode


def force_bytes(data, encoding="ascii"):
    if isinstance(data, bytes):
        return data

    if isinstance(data, str):
        return data.encode(encoding)

    return data


def force_text(data, encoding="utf-8"):
    if isinstance(data, text_type):
        return data

    if isinstance(data, bytes):
        return data.decode(encoding)

    if compat.PY3:
        return text_type(data, encoding)
    else:
        return text_type(data)
