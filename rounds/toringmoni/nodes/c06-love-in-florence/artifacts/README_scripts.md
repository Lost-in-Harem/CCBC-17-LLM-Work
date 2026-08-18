# Scripts in this directory

| file | purpose |
| --- | --- |
| `extract_puzzle.py` | unpacks the three SingleFile self-extracting-ZIP pages in `input/` and prints the six stanzas + 26 markers |
| `puzzle_text.md` | byte-verified transcription of the puzzle statement |
| `marker_scan.py` | **superseded** — scanner for the abandoned "hidden city anagram" family |
| `global_sweep_results.txt` | **superseded** — output of that family |
| `lex.py` | dictionaries: `words_alpha`, google-10k common words, GeoNames places, and `loanwords.txt` |
| `loanwords.txt` | hand-built list of音译外来词 (loanwords with famous Chinese 雅译) |
| `free80.py` | minimum-carrier decomposition of each stanza under model M80 |
| `assign.py` | marker→carrier assignment DP under model M80 (one carrier per marker, length = that marker's denominator) |

`lex.py` expects `words_alpha.txt`, `google10k.txt`, `cities15000.txt` in the same
directory; they are downloaded into the gitignored `work/` dir, so copy them next to
these scripts (or run the scripts from `work/`) before use.
