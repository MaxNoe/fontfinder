import subprocess as sp

from .fontconfig import query_font_database

__all__ = ['find_font', 'query_font_database']

try:
    sp.check_output(['which', 'fc-list'])
except sp.CalledProcessError:
    raise OSError(
        'This module currently only supports systems using "fontconfig"'
    )


def find_font(name, **kwargs):
    try:
        return query_font_database(name, **kwargs)[0]['file']
    except IndexError:
        query = ','.join(f'{k}={v}' for k, v in kwargs.items())
        if query:
            raise OSError(f'Font "{name}" with properties {query} not found')
        else:
            raise OSError(f'Font "{name}" not found')
