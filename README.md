# fontfinder [![Build Status](https://travis-ci.org/MaxNoe/fontfinder.svg?branch=master)](https://travis-ci.org/MaxNoe/fontfinder)

Find the full path of a font by it's properties, e.g. display name

```python
>>> from fontfinder import find_fond
>>> find_font('Deja Vu Sans')
'/usr/share/fonts/TTF/DejaVuSans.ttf'
>>> find_font('DejaVu Sans', weight='Bold')
'/usr/share/fonts/TTF/DejaVuSans-Bold.ttf'
>>> find_font('DejaVu Serif', style='Bold Italic')
'/usr/share/fonts/TTF/DejaVuSerif-BoldItalic.ttf'
```
