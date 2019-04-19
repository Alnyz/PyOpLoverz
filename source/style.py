# -*- coding: utf-8 -*-
from .base import Response
from .util import LastedOpLoverz, SearchOpLoverz
from itertools import zip_longest
class LastedResponse(Response):
	def __init__(self,title=None, url=None, release=None):
		super().__init__()
		self.title = title
		self.url = url
		self.release = release
		
	def read(self, obj):
		self.title = obj.get("title", None)
		self.url = obj.get("title", None)
		self.release = obj.get("release", None)
		
class LastedOp(Response):
	def __init__(self, result=None):
		super().__init__()
		self.result = result
		
	def read(self, obj): 
		for k in obj.get("result", []):
			if self.result == None:
				self.result = []
			r = LastedResponse()
			r.read(k)
			self.result.append(r)

class SearchResponse(Response):
	def __init__(self, title=None, url=None, release=None):
		super().__init__()
		self.title = title
		self.url = url
		self.release =release
	
	def read(self, obj):
		self.title = obj.get("title", None)
		self.url = obj.get("url", None)
		self.release = obj.get("release", None)
		
class SearchOp(Response):
	def __init__(self, results=None, amount=None):
		super().__init__()
		self.results = results
		self.amount = amount

	def read(self, obj):
		self.amount = obj.get("amount", None)
		for k in obj.get("results", []):
			if self.results == None:
				self.results = []
			r = SearchResponse()
			r.read(k)
			self.results.append(r)

class StreamDownload(Response):
	def __init__(self,
						google=None,
						nofile=None,
						uptobox=None,
						zippyshare=None,
						megaup=None,
						elsfile=None,
						download=None):
		super().__init__()
		self.google = google
		self.nofile = nofile
		self.zippyshare = zippyshare
		self.megaup = megaup
		self.download = download
		self.elsfile = elsfile
		
	def read(self, obj):		
		for i in obj:
			for k in obj[i]:
				self.google = k.get("google_drive", None)
				self.elsfile = k.get("elsfile", None)
				self.zippyshare = k.get("zippyshare", None)
				self.megaup = k.get("megaup", None)
				self.nofile = k.get("nofile", None)
				self.download = k.get("download", None)
				
class StreamInfo(Response):
	def __init__(self,
					sinopsis=None,
					thumb=None,
					status=None,
					tipe=None,
					durasi=None,
					genre=None):
		super().__init__()
		self.sinopsis = sinopsis
		self.thumb = thumb
		self.status = status
		self.tipe = tipe
		self.durasi = durasi
		self.genre = genre
		
	def read(self, obj):
		self.sinopsis = obj.get("sinopsis", None)
		self.thumb = obj.get("thumb", None)
		self.status = obj.get("status", None)
		self.tipe = obj.get("tipe", None)
		self.durasi = obj.get("durasi", None)
		self.genre = obj.get("genre", None)
	
class StreamOp(Response):
	def __init__(self, stream=None, info=None, list_downloads=None):
		super().__init__()
		self.stream = stream
		self.info = info
		self.list_downloads = list_downloads
	
	def read(self, obj):
		self.stream = obj.get("stream", None)
		info = StreamInfo()
		info.read(obj.get("info",None))
		self.info = info
		for k in obj.get("list_downloads",[]):
			if self.list_downloads == None:
				self.list_downloads = []
			r = StreamDownload()
			r.read(k)
			self.list_downloads.append(r)