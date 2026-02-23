# TürkçePy

Bu proje, **Python tabanlı Türkçe bir mini programlama dili** örneğidir.

`turkce_dil.py`, Türkçe anahtar kelimeleri Python anahtar kelimelerine çevirir ve kodu çalıştırır.

## Kurulum

Ek bir bağımlılık yoktur; Python 3.10+ yeterlidir.

## Kullanım

### 1) Dosyadan çalıştırma

```bash
python3 turkce_dil.py ornek.trpy
```

### 2) Komut satırından kod çalıştırma

```bash
python3 turkce_dil.py --kod 'yaz("Merhaba TürkçePy")'
```

## Desteklenen anahtar kelimeler

- `yaz` -> `print`
- `eğer` -> `if`
- `değilse` / `degilse` -> `else`
- `iken` -> `while`
- `için` -> `for`
- `aralık` -> `range`
- `işlev` -> `def`
- `döndür` -> `return`
- `sınıf` -> `class`
- `doğru` -> `True`
- `yanlış` -> `False`
- `hiçbiri` -> `None`
- `ve` -> `and`
- `veya` -> `or`
- `değil` -> `not`
- `geç` -> `pass`
- `devam` -> `continue`
- `kır` -> `break`

> Not: Bu bir eğitim amaçlı mini yorumlayıcıdır. Kaynak kod, Python'a çevrilip doğrudan `exec` ile çalıştırılır.
