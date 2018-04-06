from .fontconfig import has_fontconfig, query_fontconfig_database

__all__ = ['find_font', 'query_fontconfig_database']

if not has_fontconfig():
    raise OSError(
        'This module currently only supports systems using "fontconfig"'
    )


def find_font(name, **kwargs):
    try:
        return query_fontconfig_database(name, **kwargs)[0]['file']
    except IndexError:
        query = ','.join(f'{k}={v}' for k, v in kwargs.items())
        if query:
            raise OSError(f'Font "{name}" with properties {query} not found')
        else:
            raise OSError(f'Font "{name}" not found')
