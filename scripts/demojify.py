#!/usr/bin/env python2

import fontforge, glob, os, re, sys

for path in glob.glob('src/*.sfd'):
    font_name = os.path.splitext(os.path.basename(path))[0]
    font = fontforge.open(path)
    sys.stdout.write('Clearing glyphs from %(font)s: ' % {'font': font_name})
    total = 0
    for glyph in font.glyphs():
        if 0x1F000 <= glyph.originalgid < 0x1FFFF:
            if total > 0:
                sys.stdout.write(' , ')
            else:
                print
            sys.stdout.write('%(glyph)s %(char)s' % {'glyph': glyph.glyphname,
                                                     'char': unichr(glyph.unicode)})
            glyph.clear()
            total += 1
    if total == 0:
        sys.stdout.write('No emojis found')
    else:
        print
        sys.stdout.write('Cleared %(total)i emojis from %(font)s' % \
                         {'total': total, 'font': font_name})
    print
    font.save()
