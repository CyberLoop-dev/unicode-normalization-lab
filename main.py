#!/usr/bin/env python3
"""Compare Unicode normalization forms and inspect their code points."""
import argparse
import json
import sys
import unicodedata

FORMS = ("NFC", "NFD", "NFKC", "NFKD")

def describe(text):
    return [
        {"character": char, "codepoint": f"U+{ord(char):04X}",
         "name": unicodedata.name(char, "UNNAMED"),
         "category": unicodedata.category(char)}
        for char in text
    ]

def analyze(text):
    result = {}
    for form in FORMS:
        normalized = unicodedata.normalize(form, text)
        result[form] = {
            "normalized": normalized,
            "changed": normalized != text,
            "length": len(normalized),
            "codepoints": describe(normalized),
        }
    return result

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("text", nargs="?", help="text to inspect; stdin when omitted")
    parser.add_argument("--form", choices=FORMS, help="print only the selected normalized text")
    args = parser.parse_args()
    value = args.text if args.text is not None else sys.stdin.read()
    if args.form:
        print(unicodedata.normalize(args.form, value), end="")
    else:
        print(json.dumps(analyze(value), indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
