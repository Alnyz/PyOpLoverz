from source import *

q = "naruto"
page = 1
url = "https://www.oploverz.in/boruto-naruto-next-generations-90-subtitle-indonesia/"

api = OpzApi(return_as="rpc")

def ex_search():
	print(api.search_anime(q, page))

def ex_detail_one_url():
	print(api.detail_anime(url))

def ex_all_in_one():
	print(api.multi_detail(q, page))

def ex_lasted():
	print(api.lasted_anime(page))
