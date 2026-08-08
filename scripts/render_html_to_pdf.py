#!/usr/bin/env python3
"""Render an HTML CV or resume to PDF using WeasyPrint.

Usage:
    python render_html_to_pdf.py input.html output.pdf [base_dir]

Use ``base_dir`` to resolve candidate-supplied relative fonts or images. The script
prints the page count so the document can be checked against the requested length.
"""
import sys
from pathlib import Path


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    inp = Path(sys.argv[1]).resolve()
    out = Path(sys.argv[2]).resolve()
    base = Path(sys.argv[3]).resolve() if len(sys.argv) > 3 else inp.parent

    from weasyprint import HTML
    HTML(filename=str(inp), base_url=str(base) + "/").write_pdf(str(out))

    try:
        import pypdf
        n = len(pypdf.PdfReader(str(out)).pages)
        print(f"OK: {out} ({n} page{'s' if n != 1 else ''})")
    except Exception:
        print(f"OK: {out}")


if __name__ == "__main__":
    main()
