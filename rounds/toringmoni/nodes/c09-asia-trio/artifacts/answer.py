"""Reproduce the extraction: section number + row label -> A1Z26 -> ring -> PAINTBRUSH."""
ROWS = [
    ('KR (top-right)',  '李箱 烏瞰圖 / 오감도', [('+5', 14, 5), ('+1', 7, 1), ('+7', 9, 7)]),
    ('JP (bottom-right)','宮沢賢治 春と修羅',   [('-3', 4, -3), ('+4', 5, 4), ('+8', 6, 8)]),
    ('CN (left)',       '北岛 白日梦',          [('+7', 13, 7), ('-6', 8, -6), ('+6', 12, 6), ('+2', 19, 2)]),
]
ring = ''
for panel, work, rows in ROWS:
    seg = ''
    for label, sec, delta in rows:
        v = sec + delta
        assert 1 <= v <= 26, (label, v)
        seg += chr(64 + v)
        print(f'{panel:18s} {work:22s} row {label:3s}  {sec:2d}{delta:+d} = {v:2d} -> {chr(64+v)}')
    print(f'{"":18s} segment = {seg}\n')
    ring += seg
print('ring, in the marker cycle order KR -> JP -> CN :', ring)
for i in range(len(ring)):
    r = ring[i:] + ring[:i]
    if r == 'PAINTBRUSH':
        print(f'rotate {i} places -> {r}')
