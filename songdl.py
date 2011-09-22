#importing necessary files
import urllib
from BeautifulSoup import BeautifulSoup as bs

#get the song name from the user
songname=raw_input("enter the song name : ")
songnamelist=list(songname)
x=len(songnamelist)
songnamesrch=''
for i in range(x):
   if songnamelist[i]==' ':
      songnamelist[i]='-'
   songnamesrch=songnamesrch+songnamelist[i]

url1="http://justfreemp3.com/search/mp3/1/"+songnamesrch+".html"
print url1
soup=bs(urllib.urlopen(url1).read())
redirecturllist=soup.findAll('a',rel="nofollow",target="_blank")

#find total number of urls
x=len(redirecturllist)

#select top 10 urls only for better display
finalurl1=range(10)
for i in range(10):
  redirecturl=str(redirecturllist[i])
  list1=list(redirecturl)
  y=len(list1)
  j=0
  for j in range(y):
    if list1[j]=='h' and list1[j+1]=='r' and list1[j+2]=='e'and list1[j+3]=='f'and list1[j+4]=='='and list1[j+5]=='"':
      break
  k=0
  for k in range(y):
    if list1[k]=='r' and list1[k+1]=='e' and list1[k+2]=='c'and list1[k+3]=='t'and list1[k+4]=='"':
      break
  redirecturl=redirecturl[j+6:k+4]
  finalurl1[i]=redirecturl
  print str(i+1)+" > " + finalurl1[i]              ##displaying all the 10 choices(sources available)
  print ""

#choice out of 10 any 1
choice=input("enter the source number(1 to 10)(I recommend choice 1) : ")
urlchoice=finalurl1[choice-1]

#getting the url in proper form
finallist1=list(urlchoice)
for i in range(1000):
  if finallist1[i]=='a' and finallist1[i+1]=='m' and finallist1[i+2]=='p' and finallist1[i+3]==';':
    break
finalurl2=urlchoice[0:i]+urlchoice[i+4:]
finallist2=list(finalurl2)
for i in range(1000):
  if finallist2[i]=='a' and finallist2[i+1]=='m' and finallist2[i+2]=='p' and finallist2[i+3]==';':
    break
finalurl=finalurl2[0:i]+finalurl2[i+4:]
songurl=urllib.urlopen(finalurl).geturl()

#input from user to get the path where file will be saved
path=raw_input("where to save file");
f=open(path+songname+".mp3",'wb')
f.write(urllib.urlopen(finalurl).read())
f.close()
print "done , saved in " + path  

#porogram complete
