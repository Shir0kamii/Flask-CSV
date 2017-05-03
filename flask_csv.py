from io import BytesIO

from flask import send_file


def send_csv(iterable, filename):
    buf = BytesIO()
    for line in iterable:
        buf.write(str(line).encode("utf-8"))
    buf.seek(0)
    return send_file(buf, attachment_filename=filename, as_attachment=True)
