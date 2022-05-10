# copies anchors from current font to other font
# This script adjusts the x position of the anchors based on the 
# possible difference of the widths in source and target font.
# Open two UFOs, the top most font is source, the other is the target

fonts = AllFonts()
font = CurrentFont()

# Also replace any anhors in accents, like "_top" in "acute" 
replaceAnchorsInAccentsAlso = False

# very crude manual addition to x postion for italic fonts
# italicTweak = 40 

for f in fonts:
    if f != font:
        otherFont = f
print(font.info.familyName, font.info.styleName, ">", otherFont.info.familyName, otherFont.info.styleName)
n = 0
glyphs = ''
print('\r# Anchors \r')
for g in font:
    if g.anchors and g.name in otherFont:
        for a in g.anchors:
            aName = a.name
            aX = a.position[0]
            aY = a.position[1]
            if otherFont[g.name].width != 0 or font[g.name].width != 0:
                factor = (otherFont[g.name].width / font[g.name].width) # difference by scale factor
            else:
                factor = 1
            aX = round(aX * factor) # applying factor
            #print(g.name, aName, aX, aY)
            # if "Italic" in otherFont.info.styleName:
            #    aX =  aX + italicTweak
            if replaceAnchorsInAccentsAlso == True:
                otherFont[g.name].clearAnchors()
                otherFont[g.name].appendAnchor(aName, (aX, aY))
                glyphs = glyphs+'\r'+g.name+' '
                n = n+1
            if replaceAnchorsInAccentsAlso == False:
                if aName[0] is not "_":
                    otherFont[g.name].clearAnchors()
                    otherFont[g.name].appendAnchor(aName, (aX, aY))
                    glyphs = glyphs+'\r'+g.name+' '
                    n = n+1
    elif g.anchors and g.name not in otherFont:
        print(g.name, "# Source glyph contains anchor but glyph not in otherFont")
otherFont.changed()
#print font
#print('# added anchors in: '+glyphs)
print(n, 'anchors added')
#print(font.info.familyName, font.info.styleName, '# done')
print('# done')
