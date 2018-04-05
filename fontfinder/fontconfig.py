import subprocess as sp

PROPERTIES = {
    'file': str,
    'family': str,
    'style': str,
    'fullname': str,
    'slant': int,
    'weight': int,
    'size': float,
    'width': int,
    'fontversion': int,
}


def query_font_database(name=None, **kwargs):
    query = ''
    if name is not None:
        query += f'{name}'

    if not kwargs:
        kwargs['style'] = 'Regular'

    for prop, value in kwargs.items():
        query += f':{prop}={value}'

    if not query:
        query = ':'

    call = [
        'fc-list',
        query
    ]
    call.extend(PROPERTIES)
    output = sp.check_output(call).decode()

    return sort_fonts((map(parse_font_line, output.splitlines())))


def parse_font_line(line):
    properties = list(map(str.strip, line.split(':')))

    d = {'file': properties[0]}
    d['family'] = properties[1].split(',')[0]

    for prop in properties[2:]:
        k, v = prop.split('=')
        d[k] = PROPERTIES[k](v)
    if 'style' in d:
        d['style'] = d['style'].split(',')
    return d


def sort_key(font):
    return (
        font['family'],
        len(font['style']),
        font['fullname'],
        font['fontversion'],
    )


def sort_fonts(fonts):
    return sorted(fonts, key=sort_key)
