import urllib
from BeautifulSoup import BeautifulSoup as bs
songname=raw_input("enter the song name in a specific song (like for yaaron dosti enter yaaron-dosti)")
url1="http://justfreemp3.com/search/mp3/1/"+songname+".html"
soup=bs(urllib.urlopen(url1).read())
redirecturl=str(soup.find('a',rel="nofollow"))
list1=list(redirecturl)
for i in range(1000):
  if list1[i]=='h' and list1[i+1]=='r' and list1[i+2]=='e'and list1[i+3]=='f'and list1[i+4]=='='and list1[i+5]=='"':
    break
for j in range(1000):
  if list1[j]=='r' and list1[j+1]=='e' and list1[j+2]=='c'and list1[j+3]=='t'and list1[j+4]=='"':
    break

finalurl1=redirecturl[i+6:j+4]
#print finalurl1
finallist1=list(finalurl1)
for i in range(1000):
  if finallist1[i]=='a' and finallist1[i+1]=='m' and finallist1[i+2]=='p' and finallist1[i+3]==';':
    break
finalurl2=finalurl1[0:i]+finalurl1[i+4:]
finallist2=list(finalurl2)
for i in range(1000):
  if finallist2[i]=='a' and finallist2[i+1]=='m' and finallist2[i+2]=='p' and finallist2[i+3]==';':
    break
finalurl=finalurl2[0:i]+finalurl2[i+4:]

#print finalurl
songurl=urllib.urlopen(finalurl).geturl()
#print songurl

path=raw_input("where to save file");
f=open(path+"songdownloaded.mp3",'wb')
f.write(urllib.urlopen(finalurl).read())
f.close()
print "done , saved in " + path  

