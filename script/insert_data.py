#this file will insert last year's crash data into mongodb database "crashes" with collection name "geolocation"
import cookielib, urllib, urllib2, re, sys, datetime, subprocess, pymongo
from pyPdf import PdfFileWriter, PdfFileReader
from pymongo import MongoClient

def savePDFDateAsTmpFile(matched_filename):
  pdfurl = "http://crash.raleighpd.org/" + matched_filename
  cj = cookielib.CookieJar()
  opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
  request = urllib2.Request(pdfurl)
  f = opener.open(request)
  data = f.read()
  f.close()
  opener.close()
  savedFileName = matched_filename.split("/")[-1]
  FILE = open(savedFileName, "w")
  FILE.write(data)
  FILE.close()
  return savedFileName

def getGeolocationFromPDF(savedFileName, geolocation, date):
  subprocess.call(["pdftotext", savedFileName, "tmp.txt"])
  content = ""
  try:
    with open("tmp.txt", 'r') as myfile:
      content = myfile.read()
    code_pattern = re.compile("[+-]?\d+\.\d+[NWES]")
    matched_code = code_pattern.findall(content)
    if matched_code != None and len(matched_code) == 2:
      print matched_code[0][:-1] + " " + matched_code[1][:-1]
      geolocation.insert({"lat": matched_code[0][:-1], "lng":matched_code[1][:-1], "date":date})
    subprocess.call(["rm", "tmp.txt"])
    subprocess.call(["rm", savedFileName])
  except IOError:
    pass

def findGeolocation(content, geolocation, date):
  filename_pattern = re.compile("files/.*.pdf")
  for matched_filename in re.findall(filename_pattern, content):
    savedFileName = savePDFDateAsTmpFile(matched_filename)
    getGeolocationFromPDF(savedFileName, geolocation, date)

def processRequests(url, num_days, geolocation):
  base = datetime.datetime.today()
  dateList = [ base - datetime.timedelta(days=x) for x in range(1, num_days) ]
  for date in dateList:
    params = {
      'date' : date.strftime('%m/%d/%y')
    }
    cookie_jar = cookielib.LWPCookieJar()
    cookie = urllib2.HTTPCookieProcessor(cookie_jar)
    opener = urllib2.build_opener(cookie)
    req = urllib2.Request(url, urllib.urlencode(params))
    res = opener.open(req)
    content = res.read()
    print date.strftime('%m/%d/%y')
    findGeolocation(content, geolocation, date.strftime('%m/%d/%y'))

def main():
  client = MongoClient()
  geolocation = client.crashes.geolocation
  processRequests("http://crash.raleighpd.org/default.php", 365, geolocation)

if __name__ == '__main__':
  main()