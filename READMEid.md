# PyOpLoverz💓
_Unofficial wrapper dari oploverz.in, ini akan memberikan detail dan streaming tentang anime_

[![CodeFactor](https://www.codefactor.io/repository/github/dyseo/pyoploverz/badge/master)](https://www.codefactor.io/repository/github/dyseo/pyoploverz/overview/master) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/f70e4ca74d0547419cd01872335ae59d)](https://www.codacy.com/app/dyseo/PyOpLoverz?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dyseo/PyOpLoverz&amp;utm_campaign=Badge_Grade) [![Build Status](https://travis-ci.org/dyseo/PyOpLoverz.svg?branch=master)](https://travis-ci.org/dyseo/PyOpLoverz) [![License](https://img.shields.io/badge/MIT-License-blue.svg)]() [![Version](https://img.shields.io/badge/Version-0.0.4-orange.svg)](https://github.com/dyseo/PyOpLoverz) [![Python](https://img.shields.io/badge/Python-3.6%20%7C%203.7-brightgreen.svg)](pytho.org) [![Pypi](https://img.shields.io/badge/PyPi-0.0.4-blue.svg)](https://pypi.org/project/pyoploverz/)

## Bahasa
[English](https://github.com/dyseo/PyOpLoverz/blob/master/README.md) | [indonesia](https://github.com/dyseo/PyOpLoverz/blob/master/READMEid.md)

___
## Pemasangan
**Menggunakan clone**
1. `git clone https://github.com/dyseo/PyOpLoverz`
2. `cd PyOpLpverz`
3. `python3 setup.py install`

**Dari pypi**
- `pip install pyoploverz`

## Contoh
```python
from pyoploverz import OpzApi

query = "naruto"
page = 1
ex_url = "https://www.oploverz.in/boruto-naruto-next-generations-90-subtitle-indonesia/"

api = OpzApi(return_as="rpc")
#ubah 'return_as' menjadi 'dict' jika kamu mau output berupa dict
```

### Mencari anime dengan keyword
```python
print(api.search_anime(query=query, page=page))
```
### Mendapatkan detail anime dari url
```python
print(api.detail_anime(urls=url))
```
### Mendapatkan update terbaru
```python
print(api.lasted_anime(page=page))
```

### Mendapatkan semua data dari satu halaman
```python
print(api.multi_detail(query=query, page=page))
#NOTE: saya merokendasikan method ini hanya menggunakan dict untuk hasil.
#rpc membuat ini susah untun di olah
```

![Sample](https://github.com/dyseo/PyOpLoverz/blob/master/Screenshot_20190419_202033.png)

_Percobaan pada 19:30 Jum 4,2019 Search method menggunakan rpc_
 
## Author
[Dyseo](line.me/ti/p/~line.bngsad) / [Alnyz](https://www.instagram.com/alnyz69/)