# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from itertools import zip_longest, chain, repeat
from concurrent.futures import ThreadPoolExecutor

URL = "https://www.oploverz.in"
header = {
		"User-Agent":"python-requests/2.21.0",
	}

class Request(object):
	def __init__(self, headers: set or dict = None, proxy: set or dict = None):
		self._req = requests.Session()
		self.headers = headers
		if self.headers is None:
			self._req.headers.update(header)
		self.proxy = proxy

	def _request(self, search=None, page=1):
		with self._req as s:
			if search != None:
				r = s.get(f"{URL}/page/{page}/?s={search}&post_type=post", proxies=self.proxy if self.proxy is not None else None)
			else:
				r = s.get(f"{URL}/page/{page}/", proxies = self.proxy if self.proxy != None else None)
			if r.ok:
				soup = BeautifulSoup(r.text, "lxml")
				body = soup.find("div", class_="right").find("div", class_="lts")
				selected = body.select("ul > li")
				return selected

class LastedOpLoverz(Request):
	def __init__(self):
		super(LastedOpLoverz, self).__init__()

	def lasted(self, page):
		ret = self._request(page)
		data = {"result":[]}
		for i in ret:
			prebody = i.find("div", class_="dtl")
			href = prebody.find("h2").find("a")
			rilis = prebody.find_all("span")[2].text
			data["result"].append({
				"title":href.text,
				"url":href["href"],
				"release":rilis.strip()
			})
		return data

class StreamOpLoverz(Request):
	def __init__(self, workers=50):
		self.workers = workers
		self.urls = []
		super(StreamOpLoverz, self).__init__()

	def find_url_stream(self, query, page):
		data = self._request(query, page)
		for p in data:
			ret = p.find("div", class_="dtl")
			url = ret.find("h2").find("a")["href"]
			self.urls.append(url)
		return self.urls

	def multi_stream(self):
		with ThreadPoolExecutor(max_workers=self.workers) as pool:
			lists = list(pool.map(self.get_stream, self.urls))
			return lists

	def this_info(self, data):
		ret = {}
		info = data.find("div", class_="animeinfo")
		thumb = info.find("img")["src"]
		detail = info.find_all("span")[:4]
		sinopsis = data.find("div", class_="sinop").text
		for i in detail:
			t , h= i.text.split(":")
			ret.update({
				"sinopis":sinopsis,
				"thumb":thumb,
				t.lower():h
			})
		return ret

	def get_stream(self, list_url: str or list):
		data = {"stream":"", "info":{},"list_downloads":[]}
		r = self._req.get(list_url)
		if r.ok:
			soup = BeautifulSoup(r.text, "lxml")
			post_body = soup.find("div", class_="postbody")
			stream_body = post_body.find("div", attrs={"id":"embed"})
			stream = stream_body.find("div", class_="embedholder").find("iframe").get("src")
			dwl = post_body.find("div", class_="soraddl op-download")
			info = self.this_info(post_body)
			ex = ["480p","720p","720p_10bit", "1080p"]
			for item, ext in zip_longest(dwl.find_all("div", class_="soraurl list-download"), ex):		
				href = item.find_all("a")
				title = [i.text.lower().replace(" ","_") for i in href]
				url = [i["href"] for i in href]
				data["stream"] = stream
				data["info"] = info
				#make it simple, Reff https://stackoverflow.com/a/23030666
				data["list_downloads"].append({
					ext.strip():[
					dict(zip(title, chain(url, repeat(None))))
					]
				})
			return data

class SearchOpLoverz(Request):
	def __init__(self):
		super(SearchOpLoverz, self).__init__()

	def detailed(self, search, page):
		select = self._request(search, page)
		data = {"amount":len(select),"results":[]}
		for i in select:
			prebody = i.find("div", class_="dtl")
			href = prebody.find("h2").find("a")
			rilis = prebody.find_all("span")[2].text
			data["results"].append({
				"title":href.text,
				"url":href["href"],
				"release":rilis.strip()
				})
		return data