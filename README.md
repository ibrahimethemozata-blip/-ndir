# MiniDil

Bu repoda sıfırdan yazılmış, **çok basit bir oyuncak programlama dili** bulunuyor: `MiniDil`.

## Özellikler
- Değişken tanımlama: `LET`
- Ekrana yazdırma: `PRINT`
- Kullanıcıdan sayı alma: `INPUT`
- Koşul çalıştırma: `IF ... THEN ...`
- Akış kontrolü: `GOTO`
- Program sonlandırma: `END`

## Kurulum
Python 3.10+ yeterlidir.

## Kullanım
```bash
python3 minidil.py examples/toplama.mini
```

## Dil Sözdizimi

### Değişken atama
```text
LET x = 10
LET y = x * 2 + 5
```

### Yazdırma
```text
PRINT x
PRINT x + y
```

### Koşul
```text
IF x THEN PRINT x
```

### Satıra atlama
`GOTO` satırlar 1'den başlar.

```text
GOTO 3
```

## Örnek Program
`examples/toplama.mini`

```text
LET a = 5
LET b = 7
LET toplam = a + b
PRINT toplam
END
```
