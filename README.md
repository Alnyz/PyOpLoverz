# PyOpLoverz💓
_Unofficial wrapper from oploverz.in, this will get detail and stream about anime_

[![CodeFactor](https://www.codefactor.io/repository/github/dyseo/pyoploverz/badge/master)](https://www.codefactor.io/repository/github/dyseo/pyoploverz/overview/master) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/f70e4ca74d0547419cd01872335ae59d)](https://www.codacy.com/app/dyseo/PyOpLoverz?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dyseo/PyOpLoverz&amp;utm_campaign=Badge_Grade) [![Build Status](https://travis-ci.org/dyseo/PyOpLoverz.svg?branch=master)](https://travis-ci.org/dyseo/PyOpLoverz) [![License](https://img.shields.io/badge/MIT-License-blue.svg)]() [![Version](https://img.shields.io/badge/Version-0.0.1-red.svg)](https://github.com/dyseo/PyOpLoverz) [![Python](https://img.shields.io/badge/Python-3.6%20%7C%203.7-brightgreen.svg)](pytho.org) [![Pypi](https://img.shields.io/badge/PyPi-0.0.1-blue.svg)](https://pypi.org/project/pyoploverz/)

## Installing

**Using clone**


1. `git clone https://github.com/dyseo/PyOpLoverz`
2. `cd PyOpLoverz`
3. `python3 setup.py install`

**From pypi**

- `pip install pyoploverz`

## Example
```python
from pyoploverz import OpzApi

query = "naruto"
page = 1
ex_url = "https://www.oploverz.in/boruto-naruto-next-generations-90-subtitle-indonesia/"

api = OpzApi(return_as="rpc")
#change 'return_as' to 'dict' if you want result as dict
```

### Search anime with query
```python
print(api.search_anime(query=query, page=page))
```
### Get detail from url anime
```python
print(api.detail_anime(urls=url))
```
### Get lasted update
```python
print(api.lasted_anime(page=page))
```

### Get all data from one page
```python
print(api.multi_detail(query=query, page=page))
#NOTE: i recommend this method only using dict for returning.
#rpc style make it hard for parsing
```

![Sample](https://github.com/dyseo/PyOpLoverz/blob/master/Screenshot_20190419_202033.png)

_Tested at 19:30 Fri 4,2019 Search method using rpc style_

## Author
[Dyseo](line.me/ti/p/~line.bngsad) / [Alnyz](https://www.instagram.com/alnyz69/)
