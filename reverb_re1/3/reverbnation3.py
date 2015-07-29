import threading
import urllib.request
import os
import re
import time
import json
import sys

class Facebook(object):

	while True:
		try:

			def wget(self,url):
				#self.url = url 
				self.data = os.popen('wget -qO- %s'% url).read()
				return self.data

			def wget_sepcial(self,url):
				self.data = os.popen('wget  -qO- --header="Accept: text/html" --user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0"  %s'% url).read()
				return self.data

			def curl(self,url):

				self.url = url 
				self.data = os.popen('curl --silent --user-agent "Mozilla/4.73 [en] (X11; U; Linux 2.2.15 i686)" %s >/dev/null'% self.url).read()
				return self.data

				#print (self.data)

			def curl_special(self,url):

				self.url = url 
				self.data = os.popen('curl -O %s >/dev/null'% self.url).read()
				return self.data

			def urllib(self,url):
				filename = "cookies.txt"
				self.url = url 
				headers = {}
				headers={'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'}
				req = urllib.request.Request(url, headers = headers)
				resp = urllib.request.urlopen(req)
				self.data = resp.read()

		except:
			continue
			time.sleep(3)
		break


class Out(Facebook):

	def links_extract(self):
		f1 = open('artist_links','w')
		data = self.data 
		data = str(data)
		#print (data)

		if re.search(r'(?ms)<url><loc>([^<]*)<',data):
			links = re.findall(r'(?ms)<url><loc>([^<]*)<',data)
			for link in links:
				f1.write(link+"\n")
				print (link)

	def from_main(self):
		f1 = open('artist_links_all','a')
		data = self.data 
		data = str(data)
		print (data)

		if re.search(r'(?ms)profile\_url\"\:\"([^\"]*)\"',data):
			links = re.findall(r'(?ms)profile\_url\"\:\"([^\"]*)\"',data)
			for link in links:
				if re.search(r'^http\:\/\/',link):
					f1.write(link+"\n")
					print (link)
				else:
					url = re.sub(r'^','%s'% "http://www.reverbnation.com",link)
					f1.write(url+"\n")
					print (url)

	def manual_links(self):
		f1 = open('manual_urls','r+')
		for li in f1:
			if re.search(r'^htt',li):
				lin = re.sub(r"\s*","",li)
				print (lin)
				output.wget(lin)
				output.from_main()

	def artist_urls_extract_manual(self):
		a = [1,2,3,4,5,6,7,8,9,10,11,12]
		f = 0
		f2 = open('manual_urls','a')
		for year in range(1,5):
			f= f+1
			if f == 1:
				y = 2012
			if f == 2:
				y = 2013
			if f == 3:
				y = 2014
			if f == 4:
				y = 2015

			for m in a:
				for d in range(1,32):
					#print ("%s %s"% (f,l)
					print ("http://www.reverbnation.com/main/featured_on/more/%s_%s_%s"% (y,m,d))
					f2.write("http://www.reverbnation.com/main/featured_on/more/%s_%s_%s"% (y,m,d)+"\n")

	def dedup(self):
		with open('artist_final_urls') as result:
			uniqlines = set(result.readlines())
			with open('artist_dedup_urls', 'w') as rmdup:
				rmdup.writelines(set(uniqlines))

	def crawl_fb_urls(self,sleep):
		f1 = open('artist_dedup_urls1','r+')
		f2 = open('facebook_crawled_urls','a')
		f3 = open('crawled_email1','a')
		f4 = open('facebook_urls_crawl_report.json','a')
		for aurls in f1:
			time.sleep(sleep)
			if re.search(r'^htt',aurls):
				lin = re.sub(r"\s*","",aurls)
				print (lin)
				output.wget(lin)
				data = self.data 
				data = str(data)
				#print (data)

				if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
					email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)[0]
					if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',email):
						email = re.sub(r'nr\@context\".*','',email)
						f3.write(email+"\n")
						print (email)
				if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
					email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
					for mail in email:
						if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',mail):
							mail = re.sub(r'nr\@context\".*','',mail)
							f3.write(mail+"\n")
							print (mail)
				if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
					must = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
					for mail in must:
						if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',mail):
							mail = re.sub(r'nr\@context\".*','',mail)
							f3.write(mail+"\n")
							print (mail)
				if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',data):
					ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[^\.]*[\.]*\w+(?:[\w\.\+]*))',data)[0]
					ear = re.sub(r'nr\@context\".*','',ear)
					f3.write(ear+"\n")
					print (ear)
				if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',data):
					ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[^\.]*[\.]*\w+(?:[\w\.\+]*))',data)
					for mail in ear:
						if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',mail):
							mail = re.sub(r'nr\@context\".*','',mail)
							f3.write(mail+"\n")
							print (mail)
				if re.search(r'(?ms)data\-href\=\"(http\:\/\/www\.fa[^\"]*)\"\sdata\-layout',data):
					link = re.findall(r'(?ms)data\-href\=\"(http\:\/\/www\.fa[^\"]*)\"\sdata\-layout',data)
					for fb in link:
						url = re.sub(r'\?.*','',fb)
						fb = re.sub(r"\s.*","",fb)
						if re.search(r'^htt',url):
							fb_cac = re.sub(r'\?.*','',fb)
							fb_cac = re.sub(r'.*sharer\.php$','',fb_cac)
							fb_cac = re.sub(r'.*\/2008\/fbml$','',fb_cac)
							f2.write(fb_cac+"\n")
							f4.write("{\""+lin+"\" => \""+fb_cac+"\"}"+"\n")
							print (fb_cac)
				if re.search(r'(?ms)<li\sclass\=\"websites\sfacebook\"><a\shref\=\"([^\"]*)\"',data):
					link = re.findall(r'(?ms)<li\sclass\=\"websites\sfacebook\"><a\shref\=\"([^\"]*)\"',data)
					for fb in link:
						url = re.sub(r'\?.*','',fb)
						url = re.sub(r"\s.*","",fb)
						if re.search(r'^htt',url):
							fb_cac = re.sub(r'\?.*','',fb)
							fb_cac = re.sub(r'.*sharer\.php$','',fb_cac)
							fb_cac = re.sub(r'.*\/2008\/fbml$','',fb_cac)
							f2.write(fb_cac+"\n")
							f4.write("{\""+lin+"\" => \""+fb_cac+"\"}"+"\n")
							print (fb_cac)
				if re.search(r'(?ms)\<a\shref\=\"([^\"]*)\"\starget\=\"[^\"]*\"\stitle\=\"Facebook\"\s\>',data):
					link = re.findall(r'(?ms)\<a\shref\=\"([^\"]*)\"\starget\=\"[^\"]*\"\stitle\=\"Facebook\"\s\>',data)
					for fb in link:
						url = re.sub(r'\?.*','',fb)
						url = re.sub(r"\s.*","",fb)
						if re.search(r'^htt',url):
							fb_cac = re.sub(r'\?.*','',fb)
							fb_cac = re.sub(r'.*sharer\.php$','',fb_cac)
							fb_cac = re.sub(r'.*\/2008\/fbml$','',fb_cac)
							f2.write(fb_cac+"\n")
							f4.write("{\""+lin+"\" => \""+fb_cac+"\"}"+"\n")
							print (fb_cac)
				if re.search(r'(?ms)(http\:\/\/www\.facebook.com[^\"]*)\"',data):
					link = re.findall(r'(?ms)(http\:\/\/www\.facebook.com[^\"]*)\"',data)
					for fb in link:
						url = re.sub(r'\?.*','',fb)
						url = re.sub(r"\s.*","",fb)
						if re.search(r'^htt',url):
							fb_cac = re.sub(r'\?.*','',fb)
							fb_cac = re.sub(r'.*sharer\.php$','',fb_cac)
							fb_cac = re.sub(r'.*\/2008\/fbml$','',fb_cac)
							f2.write(fb_cac+"\n")
							f4.write("{\""+lin+"\" => \""+fb_cac+"\"}"+"\n")
							print (fb_cac)
						   # if re.search(r'(?ms)^http:\/\/www\.facebook\.com\/[^\w\-\_\.]+$',fb_cac):
							   # p = re.compile(r'(^http:\/\/www\.facebook\.com\/[^\w\-\_\.]+)', re.DOTALL | re.IGNORECASE)
							   # test_str = fb_cac
							   # subst = r"\1\/about\?section\=contact\-info"
							   # result = re.sub(p, subst, test_str)
							   # f2.write(result+"\n")
							   # print (result)
						   # elif re.search(r'(?ms)^http:\/\/www\.facebook\.com.*pages',fb_cac):
							#    p = re.compile(r'(^http:\/\/www\.facebook\.com\/[^\w\-\_\.]+)', re.DOTALL | re.IGNORECASE)
							 #   test_str = fb_cac
							  #  subst = r"\1\/about\?section\=contact\-info"
							  #  result = re.sub(p, subst, test_str)
							   # f2.write(result+"\n")
							   # print (result)
				else: 

					f4.write("{\""+lin+"\" => \""+"not found"+"\"}"+"\n")

	def crawl_fb_artist_bio(self,sleep):
		#data = <h2 class="page_location_name">
		f2 = open('facebook_crawled_urls','a')
		f3 = open('crawled_email1','a')
		f4 = open('facebook_urls_crawl_report.json','a')
		a = 4200000
		while True:
			a = a + 1
			aurls = "https://www.reverbnation.com/artist_%s/bio" % a
			if re.search(r'^htt',aurls):
				lin = re.sub(r"\s*","",aurls)
				print (lin)
				try:
					output.wget_sepcial(aurls)
					data = self.data 
					data = str(data)
				#print (data)
					length = len(data)
				#print (length)
				#print (data)
					#if a == 3800000:
					if a == 4300000:
						#771735
						break
					#print ("hi")
					else:
						if re.search(r'(?ms)websites\sartistwebsite\"><a\shref\=\"([^\"]*)\"',data):
							link = re.findall(r'(?ms)websites\sartistwebsite\"><a\shref\=\"([^\"]*)\"',data)
							for fb in link:
								url = re.sub(r'\?.*','',fb)
								url = re.sub(r"\s.*","",fb)
								if re.search(r'^htt',url):
									fb_cac = re.sub(r'\?.*','',fb)
									fb_cac = re.sub(r'.*sharer\.php$','',fb_cac)
									fb_cac = re.sub(r'.*\/2008\/fbml$','',fb_cac)
									f2.write(fb_cac+"\n")
									f4.write("{\""+lin+"\" => \""+fb_cac+"\"}"+"\n")
									print (fb_cac)
									output.crawl_fb_again(fb_cac,sleep)

						else: 

							f4.write("{\""+lin+"\" => \""+"not found"+"\"}"+"\n")

						if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
							email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)[0]
							if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',email):
								email = re.sub(r'(.*)\/',r"\1",email)
								f3.write(email+"\n")
								#f4.write("{\""+lin+"\" => \""+email+"\"}"+"\n")
								print (email)

						if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
							email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
							for mail in email:
								if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
									mail = re.sub(r'(.*)\/',r"\1",mail)
									f3.write(mail+"\n")
									#f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
									print (mail)
						if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
							must = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
							for mail in must:
								if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
									mail = re.sub(r'(.*)\/',r"\1",mail)
									f3.write(mail+"\n")
									#f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
									print (mail)

						if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+]*))',data):
							ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)[0]
							ear = re.sub(r'(.*)\/',r"\1",ear)
							f3.write(ear+"\n")
							#f4.write("{\""+lin+"\" => \""+ear+"\"}"+"\n")
							print (ear)

						if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',data):
							ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)
							for mail in ear:
								if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+\_\-]*)',mail):
									mail = re.sub(r'(.*)\/',r"\1",mail)
									f3.write(mail+"\n")
									#f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
									print (mail)
						   # if re.search(r'(?ms)^http:\/\/www\.facebook\.com\/[^\w\-\_\.]+$',fb_cac):
							   # p = re.compile(r'(^http:\/\/www\.facebook\.com\/[^\w\-\_\.]+)', re.DOTALL | re.IGNORECASE)
							   # test_str = fb_cac
							   # subst = r"\1\/about\?section\=contact\-info"
							   # result = re.sub(p, subst, test_str)
							   # f2.write(result+"\n")
							   # print (result)
						   # elif re.search(r'(?ms)^http:\/\/www\.facebook\.com.*pages',fb_cac):
							#    p = re.compile(r'(^http:\/\/www\.facebook\.com\/[^\w\-\_\.]+)', re.DOTALL | re.IGNORECASE)
							 #   test_str = fb_cac
							  #  subst = r"\1\/about\?section\=contact\-info"
							  #  result = re.sub(p, subst, test_str)
							   # f2.write(result+"\n")
							   # print (result)

				except Exception: 
					pass    
		#output.dedup_urls1()

	#def dedup_urls1(self):
	 #   with open('facebook_crawled_urls') as result:
	  #      uniqlines = set(result.readlines())
	   #     with open('facebook_crawled_urls', 'w') as rmdup:
		#        rmdup.writelines(set(uniqlines))

	def crawl_fb_again(self,url,sleep):
		#f1 = open('facebook_crawled_urls','r+')
		f2 = open('facebook_crawled_again','a')
		f3 = open('crawled_email1','a')
		f4 = open('crawled_email_ugly','a')
		f5 = open('facebook-crawled_email_ids_report.json','a')
		if re.search(r'^\w',url):
			lin = re.sub(r"\s*","",url)
			#print (lin)
			try:
				url_lin = re.sub(r'(.*?\/)',r"\1",lin)
				#print (url_lin)
				output.wget_sepcial(lin)
				data = self.data 
				data = str(data)
				#print (data)
				#print (data)

				if re.search(r'(?ms)og\:url\"\scontent\=\"([^\"]*)\"',data):
					email = re.findall(r'(?ms)og\:url\"\scontent\=\"([^\"]*)\"',data)
					for fb in email:
						url = re.sub(r'\?.*','',fb)
						if re.search(r'^htt',url):
							fb_cac = re.sub(r'\?.*','',fb)
							fb_cac = re.sub(r'.*sharer\.php$','',fb_cac)
							fb_cac = re.sub(r'.*\/2008\/fbml$','',fb_cac)
							f2.write(fb_cac+"\n")
							print (fb_cac)
							time.sleep(sleep)
							if re.search(r'^\w',fb_cac):
								try:                                                                                             
									output.wget_sepcial(url)
									data = self.data 
									data = str(data)
									#print (data)
									if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
										email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)[0]
										if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',email):
											email = re.sub(r'(.*)\/',r"\1",email)
											f3.write(email+"\n")
											#f4.write("{\""+lin+"\" => \""+email+"\"}"+"\n")
											print (email)

									if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
										email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
										for mail in email:
											if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
												mail = re.sub(r'(.*)\/',r"\1",mail)
												f3.write(mail+"\n")
									#f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
												print (mail)
									if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
										must = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
										for mail in must:
											if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
												mail = re.sub(r'(.*)\/',r"\1",mail)
												f3.write(mail+"\n")
									#f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
												print (mail)

									if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+]*))',data):
										ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)[0]
										ear = re.sub(r'(.*)\/',r"\1",ear)
										f3.write(ear+"\n")
							#f4.write("{\""+lin+"\" => \""+ear+"\"}"+"\n")
										print (ear)

									if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',data):
										ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)
										for mail in ear:
											if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+\_\-]*)',mail):
												mail = re.sub(r'(.*)\/',r"\1",mail)
												f3.write(mail+"\n")
									#f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
												print (mail)

									if re.search(r'(?msi)<a\s*href\=\"([^\"]*\/contact.*?[^\"]*)\"',data):
										ear = re.findall(r'(?msi)<a\s*href\=\"([^\"]*\/contact.*?[^\"]*)\"',data)
										if re.search(r'(?ms)^\/',ear[0]):
											ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
											print (ear)
											output.link_again(ear,sleep)
										else:
											print (ear)
											output.link_again(ear[0],sleep)

									if re.search(r'(?msi)<a\s*href\=\"([^\"]*\/about.*?[^\"]*)\"',data):
										ear = re.findall(r'(?msi)<a\s*href\=\"([^\"]*\/about.*?[^\"]*)\"',data)
										if re.search(r'(?ms)^\/',ear[0]):
											ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
											print (ear)
											output.link_again(ear,sleep)
										else:
											print (ear[0])
											output.link_again(ear[0],sleep)

								except Exception: 
									pass    

									#else:
									 #   url = fb_cac+second  
									  #  print (url)
									   # try:                                                                                               
										#    output.wget_sepcial(url)
										 #   data = self.data 
										  #  data = str(data)
										   # if re.search(r'(?ms)class\=\"\_50f4\"\>([^\<]*\&\#064\;.*?[^<]*)<\/div>',data):
											#    link = re.findall(r'(?ms)class\=\"\_50f4\"\>([^\<]*\&\#064\;.*?[^<]*)<\/div>',data)
											 #   for mail in link:
											  #      mail = re.sub(r'\&\#064\;','@',mail)
											   #     f4.write(mail+"\n")
												#    fmail = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',mail)
												 #   for smail in fmail:

												  #      f3.write(smail+"\n")
												   #     f5.write("{\""+lin+"\" => \""+smail+"\"}"+"\n")
													#    print (smail)
										#except Exception: 
										 #   pass    

				else: 
					print ("not found")
					f5.write("{\""+lin+"\" => \""+"not found"+"\"}"+"\n")
			except Exception: 
				pass   

		if re.search(r'^\w',url):
			lin = re.sub(r"\s*","",url)
			print (lin)
			try:
				url_lin = re.sub(r'(.*?\/)',r"\1",lin)
				#print (url_lin)
				output.wget_sepcial(lin)
				data = self.data 
				data = str(data) 
				#print (data)

				if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
					email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)[0]
					if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',email):
						email = re.sub(r'(.*)\/',r"\1",email)
						f3.write(email+"\n")
											#f4.write("{\""+lin+"\" => \""+email+"\"}"+"\n")
						print (email)

				if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
					email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
					for mail in email:
						if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
							mail = re.sub(r'(.*)\/',r"\1",mail)
							f3.write(mail+"\n")
									#f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
							print (mail)
				if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
					must = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
					for mail in must:
						if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
							mail = re.sub(r'(.*)\/',r"\1",mail)
							f3.write(mail+"\n")
									#f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
							print (mail)

				if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+]*))',data):
					ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)[0]
					ear = re.sub(r'(.*)\/',r"\1",ear)
					f3.write(ear+"\n")
							#f4.write("{\""+lin+"\" => \""+ear+"\"}"+"\n")
					print (ear)

				if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',data):
					ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)
					for mail in ear:
						if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+\_\-]*)',mail):
							mail = re.sub(r'(.*)\/',r"\1",mail)
							f3.write(mail+"\n")

				if re.search(r'(?msi)<a\s*href\=\"([^\"]*\/contact.*?[^\"]*)\"',data):
					print ("yes")
					ear = re.findall(r'(?msi)<a\s*href\=\"([^\"]*\/contact.*?[^\"]*)\"',data)
					#print (ear)
					if re.search(r'(?ms)^\/',ear[0]):
						ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
						print (ear)
						output.link_again(ear,sleep)
					else:
						print (ear)
						output.link_again(ear[0],sleep)

				if re.search(r'(?msi)<a\s*href\=\"([^\"]*\/about.*?[^\"]*)\"',data):
					ear = re.findall(r'(?msi)<a\s*href\=\"([^\"]*\/about.*?[^\"]*)\"',data)
					if re.search(r'(?ms)^\/',ear[0]):
						ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
						print (ear)
						output.link_again(ear,sleep)
					else:
						print (ear)
						output.link_again(ear[0],sleep)

			except Exception: 
				pass  

	def link_again(self,url,sleep):
		f2 = open('facebook_crawled_again','a')
		f3 = open('crawled_email1','a')
		f4 = open('crawled_email_ugly','a')
		f5 = open('facebook-crawled_email_ids_report.json','a')

		if re.search(r'^\w',url):
			lin = re.sub(r"\s*","",url)
			print (lin)
			try:
				output.wget_sepcial(lin)
				data = self.data 
				data = str(data) 

				if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
					email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)[0]
					if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',email):
						email = re.sub(r'(.*)\/',r"\1",email)
						f3.write(email+"\n")
											#f4.write("{\""+lin+"\" => \""+email+"\"}"+"\n")
						print (email)

				if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
					email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
					for mail in email:
						if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
							mail = re.sub(r'(.*)\/',r"\1",mail)
							f3.write(mail+"\n")
									#f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
							print (mail)
				if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
					must = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
					for mail in must:
						if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
							mail = re.sub(r'(.*)\/',r"\1",mail)
							f3.write(mail+"\n")
									#f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
							print (mail)

				if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+]*))',data):
					ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)[0]
					ear = re.sub(r'(.*)\/',r"\1",ear)
					f3.write(ear+"\n")
							#f4.write("{\""+lin+"\" => \""+ear+"\"}"+"\n")
					print (ear)

				if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',data):
					ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)
					for mail in ear:
						if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+\_\-]*)',mail):
							mail = re.sub(r'(.*)\/',r"\1",mail)
							f3.write(mail+"\n")

			except Exception: 
				pass  

	#def dedup_email(self):
	 #   with open('crawled_email1') as result:
	  #     uniqlines = set(result.readlines())
	   #     with open('crawled_email1', 'w') as rmdup:
		#        rmdup.writelines(set(uniqlines))



												


sleep = 2
output = Out()

#f1 = open('artist_links','r+')
#f2 = open('artist_canacolized','w')
#for li in f1:
 #   if re.search(r'^htt',li):
  #      lin = re.sub(r"\s*","",li)
   #     if re.search(r'^http.*\.com\/[\w\-\_]+$',lin):
	#        f2.write(lin+"\n")
	 #       print (lin)


#output.wget("http://reverbnation-http-public-production.s3.amazonaws.com/sitemap.xml")
#output.wget("http://www.reverbnation.com/main/crowd_picks")
#output.links_extract()
#output.manual_links()
#output.from_main()
#output.dedup()
#output.crawl_fb_urls(sleep)
#output.crawl_fb_artist_bio(sleep)
#output.crawl_fb_again(sleep)
#output.dedup_email()

output.crawl_fb_artist_bio(sleep)
