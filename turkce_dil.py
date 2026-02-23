#!/usr/bin/env python3
"""Türkçe anahtar kelimeler kullanan Python tabanlı mini bir dil yorumlayıcısı."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

KEYWORD_MAP = {
    "yaz": "print",
    "eğer": "if",
    "degilse": "else",
    "değilse": "else",
    "iken": "while",
    "için": "for",
    "aralık": "range",
    "işlev": "def",
    "döndür": "return",
    "sınıf": "class",
    "doğru": "True",
    "yanlış": "False",
    "hiçbiri": "None",
    "ve": "and",
    "veya": "or",
    "değil": "not",
    "geç": "pass",
    "devam": "continue",
    "kır": "break",
}

PATTERN = re.compile(r"\b(" + "|".join(re.escape(key) for key in KEYWORD_MAP) + r")\b")


def translate_source(source: str) -> str:
    """Türkçe anahtar kelimeleri Python karşılıklarına çevirir."""

    return PATTERN.sub(lambda m: KEYWORD_MAP[m.group(0)], source)


def run_source(source: str, filename: str = "<turkce>") -> None:
    """Çevrilen kodu güvenli olmayan ancak basit bir çalışma ortamında çalıştırır."""

    translated = translate_source(source)
    compiled = compile(translated, filename, "exec")
    namespace: dict[str, object] = {"__name__": "__main__"}
    exec(compiled, namespace)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Türkçe sözdizimine sahip Python tabanlı mini dil çalıştırıcısı"
    )
    parser.add_argument("dosya", nargs="?", help="Çalıştırılacak .trpy dosya yolu")
    parser.add_argument(
        "-k",
        "--kod",
        help="Dosya yerine doğrudan komut satırından Türkçe kod ver",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])

    if not args.dosya and not args.kod:
        print("Hata: bir dosya yolu ya da --kod verilmelidir.", file=sys.stderr)
        return 2

    try:
        if args.kod:
            run_source(args.kod, filename="<komut_satiri>")
            return 0

        source_path = Path(args.dosya)
        source = source_path.read_text(encoding="utf-8")
        run_source(source, filename=str(source_path))
        return 0
    except FileNotFoundError:
        print(f"Hata: dosya bulunamadı: {args.dosya}", file=sys.stderr)
        return 1
    except SyntaxError as exc:
        print(f"Sözdizimi hatası: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:  # çalışma zamanı hatalarını net göstermek için
        print(f"Çalışma zamanı hatası: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
