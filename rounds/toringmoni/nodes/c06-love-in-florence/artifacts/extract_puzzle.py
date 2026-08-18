#!/usr/bin/env python3
"""Recover the puzzle statement from the SingleFile-ZIP captures in input/.

Each input/*.html is a self-extracting SingleFile page: a small HTML/JS shell
followed by a ZIP archive (local header 'PK\\x03\\x04' .. EOCD 'PK\\x05\\x06').
The real page is index.html inside that archive.

Usage (from the Node directory):
    python3 artifacts/extract_puzzle.py            # -> work/sfz/<name>/ + text
    python3 artifacts/extract_puzzle.py OUTDIR
"""
import io, os, re, sys, zipfile
from html.parser import HTMLParser

SKIP = {'script', 'style', 'title', 'noscript'}
BLOCK = {'br', 'p', 'div', 'li', 'tr', 'h1', 'h2', 'h3', 'h4', 'section', 'article', 'span'}


class Visible(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip = 0
        self.out = []

    def handle_starttag(self, tag, attrs):
        if tag in SKIP:
            self.skip += 1
        elif tag in BLOCK:
            self.out.append('\n')

    def handle_endtag(self, tag):
        if tag in SKIP and self.skip:
            self.skip -= 1
        elif tag in BLOCK:
            self.out.append('\n')

    def handle_data(self, data):
        if not self.skip:
            self.out.append(data)


def visible_text(html):
    p = Visible()
    p.feed(html)
    txt = re.sub(r'[ \t ]+', ' ', ''.join(p.out))
    return re.sub(r'\n\s*\n+', '\n', txt).strip()


def unpack(path, outdir):
    data = open(path, 'rb').read()
    start, end = data.find(b'PK\x03\x04'), data.rfind(b'PK\x05\x06')
    if start < 0 or end < 0:
        raise SystemExit(f'{path}: no embedded zip')
    z = zipfile.ZipFile(io.BytesIO(data[start:end + 22]))
    z.extractall(outdir)
    return os.path.join(outdir, 'index.html')


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else 'work/sfz'
    for name in sorted(os.listdir('input')):
        if not name.endswith('.html'):
            continue
        out = os.path.join(root, name[:-5])
        os.makedirs(out, exist_ok=True)
        index = unpack(os.path.join('input', name), out)
        html = open(index, encoding='utf-8', errors='replace').read()
        txt = visible_text(html)
        open(out + '.txt', 'w', encoding='utf-8').write(txt + '\n')
        print(f'{name} -> {out}/  ({len(txt)} chars of visible text)')
        # the poem itself lives in <p class=tg-poem-stanza> blocks
        for i, st in enumerate(re.findall(r'<p class=tg-poem-stanza>(.*?)</p>', html, re.S), 1):
            lines = re.findall(r'<span>(.*?)</span>', st, re.S)
            print(f'  stanza {i}: {lines[0]}')
            print(f'            markers: {" ".join(lines[1:])}')


if __name__ == '__main__':
    main()
