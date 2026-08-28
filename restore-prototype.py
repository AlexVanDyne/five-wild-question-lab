#!/usr/bin/env python3
"""Restore the standalone prototype from repository-safe compressed chunks."""
from pathlib import Path
import base64, gzip

root = Path(__file__).resolve().parent
parts = sorted((root / "prototype-parts").glob("part-*.txt"))
if not parts:
    raise SystemExit("No prototype parts found.")
payload = "".join(p.read_text().strip() for p in parts)
out = root / "Five_Wild_Question_Lab.html"
out.write_bytes(gzip.decompress(base64.b64decode(payload)))
print(f"Restored {out.name} ({out.stat().st_size:,} bytes)")
