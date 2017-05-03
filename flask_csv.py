from io import BytesIO, StringIO

from csvalidate import ValidatedWriter
from flask import send_file


def send_csv(iterable, filename, fields=None, schema=None, delimiter=',',
             **kwargs):
    buf = StringIO()
    writer_cls = ValidatedWriter
    if schema:
        writer_cls = ValidatedWriter.from_schema(schema)
    writer = writer_cls(buf, fields, delimiter=delimiter)
    writer.writeheader()
    for line in iterable:
        writer.writerow(line)
    buf.seek(0)
    buf = BytesIO(buf.read().encode("utf-8"))
    return send_file(buf, attachment_filename=filename, as_attachment=True,
                     **kwargs)
