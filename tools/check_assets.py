#!/usr/bin/env python3
"""Check a static GitHub Pages checkout of Maremon Survivors (stdlib only)."""
import argparse
import json
import pathlib
import re
import sys
root=pathlib.Path(__file__).resolve().parents[1]
html=root.joinpath('index.html')
if not html.is_file():
    sys.exit('ERROR: index.html missing')
text=html.read_text(encoding='utf-8')
script=root.joinpath('game.js')
if not script.is_file():
    sys.exit('ERROR: game.js missing')
code=script.read_text(encoding='utf-8')
errors=[]; warnings=[]
if '<meta charset="utf-8">' not in text:
    errors.append('UTF-8 charset declaration missing')
if not (root/'styles.css').is_file():
    errors.append('styles.css missing')
if './game.js' not in text or './styles.css' not in text:
    errors.append('missing relative CSS/JS references')
if 'const BUILD_VERSION=' not in code:
    errors.append('Build version missing')
for ident in ['embeddedArt', 'embeddedSfx', 'BGM_FILES']:
    m=re.search(r'const\s+'+ident+r'\s*=\s*(\{[^;]*\})\s*;',code)
    if not m:
        errors.append(ident+' mapping missing')
        continue
    try:
        mapping=json.loads(m.group(1))
    except json.JSONDecodeError as ex:
        errors.append(ident+': invalid mapping: '+str(ex))
        continue
    if ident=='BGM_FILES':
        paths=['music/'+v for v in mapping.values()]
    else:
        paths=list(mapping.values())
    missing=[p for p in paths if not (root/p).is_file()]
    if ident=='BGM_FILES' and not (root/'music').exists():
        warnings.append('BGM optional package not installed (site still playable without music)')
    elif missing:
        errors.append(f'{ident}: {len(missing)} missing: '+', '.join(missing[:6]))
    print(f'{ident}: {len(paths)-len(missing)}/{len(paths)} present')
# v406 stage pilot deliberately loads its art from a separate illustrated atlas.
new_area_assets=['floor_ruins_dunes.webp','floor_ruins_gate.webp','floor_ruins_street.webp','floor_ruins_relief.webp','floor_ruins_temple.webp','floor_ruins_vault.webp','floor_ruins_abyss.webp','ruins_arch.webp','ruins_column.webp','ruins_fallen.webp','ruins_shrine.webp','ruins_altar.webp','ruins_obelisk.webp','ruins_stoneheap.webp','xp_ruins_crystal.png','preview_ruins_remake.jpg']
for art in new_area_assets:
    if not (root/'assets'/'environment'/art).is_file(): errors.append('pilot asset missing: '+art)
print('ruins pilot art:',len(new_area_assets)-sum(not (root/'assets'/'environment'/art).is_file() for art in new_area_assets),'/',len(new_area_assets))
if errors:
    for e in errors: print('ERROR:',e,file=sys.stderr)
    sys.exit(1)
for warning in warnings: print('WARNING:',warning)
print('PASS: static site files and UTF-8 are valid')
