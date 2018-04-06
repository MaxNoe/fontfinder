import subprocess as sp
import warnings

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


def has_fontconfig():
    result = sp.run(['which', 'fc-list'], stdout=sp.PIPE, stderr=sp.PIPE)
    return result.returncode == 0


def query_fontconfig_database(
    family=None,
    style=None,
    weight=None,
    slant=None,
    **kwargs
):
    '''
    Query the fontconfig database.
    This is a thin wrapper around `fc-list`.

    Parameters
    ----------
    family: str
        Search for fonts of this family
    style: str
        Filter by style, e.g. 'Bold Italic'
    weight: str or int
        Filter by weight, which can be a string, e.g. "Thin", "Bold" or
        the integer weight.
    slant: str
        'roman', 'italic' or 'oblique'
    **kwargs:
        Filter by other font properties, see `man fc-list` for details.
    '''
    query = ''
    if family is not None:
        query += f'{family}'

    if style is not None and (weight is not None or slant is not None):
        warnings.warn('`style` will override `weight` and `slant`')

    if style:
        kwargs['style'] = style

    if weight:
        kwargs['weight'] = weight

    if slant:
        kwargs['slant'] = slant

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
    lines = output.splitlines()

    return _sort_fonts(map(_parse_font_line, lines))


def _parse_font_line(line):
    properties = list(map(str.strip, line.split(':')))

    d = {'file': properties[0]}
    d['family'] = properties[1].split(',')[0]

    for prop in properties[2:]:
        k, v = prop.split('=')
        d[k] = PROPERTIES[k](v)
    if 'style' in d:
        d['style'] = d['style'].split(',')
    return d


def _sort_key(font):
    return (
        font['family'],
        'Regular' not in font['style'] and 'Book' not in font['style'],
        len(font['style']),
        len(font['fullname']),
        font['fullname'],
        -font['fontversion'],
    )


def _sort_fonts(fonts):
    return sorted(fonts, key=_sort_key)
