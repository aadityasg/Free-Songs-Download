###importing modules
import urllib
from BeautifulSoup import BeautifulSoup as bs

###songs name input from the user
songname=raw_input("enter the song name : ")
songnamelist=list(songname)
x=len(songnamelist)
songnamesrch=''
for i in range(x):
   if songnamelist[i]==' ':
      songnamelist[i]='-'
   songnamesrch=songnamesrch+songnamelist[i]

###searching the song
url1="http://justfreemp3.com/search/mp3/1/"+songnamesrch+".html"
soup=bs(urllib.urlopen(url1).read())
redirecturl=str(soup.find('a',rel="nofollow"))
list1=list(redirecturl)

###getting the perfect mp3 source url and removing the unwanted things
for i in range(1000):
  if list1[i]=='h' and list1[i+1]=='r' and list1[i+2]=='e'and list1[i+3]=='f'and list1[i+4]=='='and list1[i+5]=='"':
    break
for j in range(1000):
  if list1[j]=='r' and list1[j+1]=='e' and list1[j+2]=='c'and list1[j+3]=='t'and list1[j+4]=='"':
    break

finalurl1=redirecturl[i+6:j+4]
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
songurl=urllib.urlopen(finalurl).geturl()

###input from user for getting the path where file will be saved
path=raw_input("where to save file :");

###writing the song to a file i.e. saving it somewhere
f=open(path+songname+".mp3",'wb')
f.write(urllib.urlopen(finalurl).read())
f.close()
print "done , saved in " + path  

###end of program

