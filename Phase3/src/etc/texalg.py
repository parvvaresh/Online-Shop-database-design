"""
Latex Algorithm Converter
- Convert "algorithmic" notations to "algpseudocode"
- Convert "algpseudocode" notations to "algorithmic"
"""

D = (
    ('STATE', 'State'),
    ('ENDIF', 'EndIf'),
    ('ENDWHILE', 'EndWhile'),
    ('ENDFOR', 'EndFor'),
    ('ELSIF', 'ElsIf'),
    ('IF', 'If'),
    ('WHILE', 'While'),
    ('FOR', 'For'),
    ('ELSE', 'Else'),
    ('REQUIRE', 'Require'),
    ('ENSURE', 'Ensure'),
    ('COMMENT', 'Comment'),
)

with open('input.tex', 'r', encoding='utf-8') as f:
    ctx = f.read()

alp = ctx
alg = ctx

for d in D:
    alp = alp.replace('\\' + d[0], '\\' + d[1])
    alg = alg.replace('\\' + d[1], '\\' + d[0])

with open('algpseudocode.tex', 'w', encoding='utf-8') as f:
    f.write(alp)

with open('algorithmic.tex', 'w', encoding='utf-8') as f:
    f.write(alg)
