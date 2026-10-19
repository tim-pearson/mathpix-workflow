#!/usr/bin/env python3
import sys
import pymupdf

MARKERS = [
    b"Copyright Material",
    b"Review Copy",
]

def remove_bt_block(stream: bytes, marker: bytes) -> bytes:
    """Remove every BT...ET block that contains the marker."""
    while marker in stream:
        idx = stream.find(marker)
        bt = stream.rfind(b"BT", 0, idx)
        et = stream.find(b"ET", idx)
        if bt == -1 or et == -1:
            break
        stream = stream[:bt] + stream[et + 2:]
    return stream

def remove_watermarks(src: str):
    dst = src.replace(".pdf", "-clean.pdf")
    doc = pymupdf.open(src)
    removed = 0

    for xref in range(1, doc.xref_length()):
        stream = doc.xref_stream(xref)
        if not stream:
            continue
        new_stream = stream
        for marker in MARKERS:
            if marker in new_stream:
                new_stream = remove_bt_block(new_stream, marker)
        if new_stream != stream:
            doc.update_stream(xref, new_stream)
            removed += 1

    doc.ez_save(dst)
    print(f"Modified {removed} streams → {dst}")

    # Verify
    doc2 = pymupdf.open(dst)
    for marker in MARKERS:
        for xref in range(1, doc2.xref_length()):
            s = doc2.xref_stream(xref)
            if s and marker in s:
                print(f"  WARNING: {marker!r} still in xref {xref}")
                break

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file.pdf>")
        sys.exit(1)
    remove_watermarks(sys.argv[1])   
