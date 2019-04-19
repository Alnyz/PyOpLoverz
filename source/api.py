from . import *
import traceback

class OpzApi(SearchOpLoverz, LastedOpLoverz, StreamOpLoverz, Request):
	def __init__(self, return_as = "dict"):
		self.return_as = return_as
		super().__init__()
		
	def search_anime(self, query: str, page=1):
		data = self.detailed(query, page)
		if self.return_as == "dict":
			return data
		if self.return_as == "rpc":
			r = SearchOp()
			r.read(data)
			return r
		else:
			raise Exception("Makse sure your add right value for returning")
			
	def detail_anime(self, urls:list or str = None):
		data = self.get_stream(urls)
		if self.return_as == "dict":
			return data
		if self.return_as == "rpc":
			r = StreamOp()
			r.read(data)
			return r
		else:
			raise Exception("Makse sure your add right value for returning")
			
	def multi_detail(self, query: str, page: int = 1):
		#this may make your result getting slow
		#this will returned all data at one page
		#TODO: just using dict result for this, make you easy to parse this
		self.find_url_stream(query, page)
		for i in self.multi_stream():
			return i
	
	def lasted_anime(self, page: int = 1):
		data = self.lasted(page)
		if self.return_as == "dict":
			return data
		if self.return_as == "rpc":
			r = LastedOp()
			r.read(data)
			return r
		else:
			raise Exception("Makse sure your add right value for returning")