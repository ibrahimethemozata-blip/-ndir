#!/usr/bin/env python3
"""MiniDil: basit bir oyuncak programlama dili yorumlayıcısı.

Desteklenen komutlar:
- LET <degisken> = <ifade>
- PRINT <ifade>
- INPUT <degisken>
- IF <ifade> THEN <komut>
- GOTO <satir_no>
- END

İfadeler: sayılar, değişkenler ve + - * / işlemleri.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class RuntimeState:
    variables: Dict[str, float]
    line_index: int = 0
    ended: bool = False


class MiniDilError(Exception):
    pass


class MiniDilInterpreter:
    def __init__(self) -> None:
        self.state = RuntimeState(variables={})

    def run(self, source: str) -> None:
        lines = [line.strip() for line in source.splitlines() if line.strip() and not line.strip().startswith("#")]
        self.state = RuntimeState(variables={})

        while self.state.line_index < len(lines) and not self.state.ended:
            command = lines[self.state.line_index]
            next_index = self.state.line_index + 1
            self._execute(command, lines)
            if self.state.line_index == next_index - 1:
                self.state.line_index = next_index

    def _execute(self, line: str, lines: List[str]) -> None:
        if line.startswith("LET "):
            self._handle_let(line[4:])
            return
        if line.startswith("PRINT "):
            value = self._eval_expr(line[6:])
            if value.is_integer():
                print(int(value))
            else:
                print(value)
            return
        if line.startswith("INPUT "):
            name = line[6:].strip()
            raw = input(f"{name}? ")
            try:
                self.state.variables[name] = float(raw)
            except ValueError as exc:
                raise MiniDilError(f"INPUT sayısal değer olmalı: {raw}") from exc
            return
        if line.startswith("IF "):
            self._handle_if(line[3:], lines)
            return
        if line.startswith("GOTO "):
            target = int(self._eval_expr(line[5:]))
            if target < 1 or target > len(lines):
                raise MiniDilError(f"GOTO satır aralığı dışında: {target}")
            self.state.line_index = target - 1
            return
        if line == "END":
            self.state.ended = True
            return
        raise MiniDilError(f"Bilinmeyen komut: {line}")

    def _handle_let(self, expr: str) -> None:
        if "=" not in expr:
            raise MiniDilError("LET için '=' gerekli")
        name, value_expr = expr.split("=", 1)
        name = name.strip()
        if not name.isidentifier():
            raise MiniDilError(f"Geçersiz değişken adı: {name}")
        self.state.variables[name] = self._eval_expr(value_expr.strip())

    def _handle_if(self, expr: str, lines: List[str]) -> None:
        if " THEN " not in expr:
            raise MiniDilError("IF için THEN gerekli")
        cond_expr, then_command = expr.split(" THEN ", 1)
        if self._eval_expr(cond_expr.strip()) != 0:
            # Tek satırlık komut çalıştırılır.
            old_index = self.state.line_index
            self._execute(then_command.strip(), lines)
            # IF içindeki komut satır göstergesini değiştirmediyse dış akışa bırak.
            if self.state.line_index != old_index:
                return

    def _eval_expr(self, expr: str) -> float:
        safe_scope = {k: v for k, v in self.state.variables.items()}
        allowed = set("0123456789+-*/(). _abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        if any(ch not in allowed for ch in expr):
            raise MiniDilError(f"İfadede geçersiz karakter var: {expr}")
        try:
            value = eval(expr, {"__builtins__": {}}, safe_scope)
        except Exception as exc:  # Bilerek kullanıcı ifadesini yakalıyoruz.
            raise MiniDilError(f"İfade çözümlenemedi: {expr}") from exc
        if not isinstance(value, (int, float)):
            raise MiniDilError("İfade sayısal sonuç üretmeli")
        return float(value)


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="MiniDil yorumlayıcısı")
    parser.add_argument("source", help=".mini uzantılı kaynak dosyası")
    args = parser.parse_args()

    with open(args.source, "r", encoding="utf-8") as f:
        code = f.read()

    MiniDilInterpreter().run(code)


if __name__ == "__main__":
    main()
