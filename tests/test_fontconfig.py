def test_query_database_droid():
    from fontfinder import query_fontconfig_database

    fonts = query_fontconfig_database('DejaVu Sans')

    assert all(f['family'] == 'DejaVu Sans' for f in fonts)
    assert fonts[0]['fullname'] == 'DejaVu Sans'


def test_query_database_dejavu():
    from fontfinder import query_fontconfig_database

    fonts = query_fontconfig_database('Droid Sans')

    assert all(f['family'] == 'Droid Sans' for f in fonts)
    assert fonts[0]['fullname'] == 'Droid Sans'


def test_query_database_dejavu_bold():
    from fontfinder import query_fontconfig_database

    fonts = query_fontconfig_database('DejaVu Sans', style='Bold')

    assert all(f['family'] == 'DejaVu Sans' for f in fonts)
    assert fonts[0]['fullname'] == 'DejaVu Sans Bold'


def test_findfont():
    from fontfinder import find_font

    assert find_font('Deja Vu Sans')
