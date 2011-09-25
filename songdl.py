import urllib
from BeautifulSoup import BeautifulSoup as bs
ans='y'
while ans=='y' or ans=='Y':
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
   
   #geeting the song name
   songnamelist=soup.findAll('td',width="370",rowspan="3")
   a=len(songnamelist)
   a1=0
   if a<15:
      a1=a
   elif a>15 or a==15:
      a1=15
   for i in range(a1):
      
      song=str(songnamelist[i])
      tagdivide=list(song)
      count1=0
      b=len(tagdivide)
      for j in range(b):
         if count1==3:
            break
         elif tagdivide[j]=='>':
            count1=count1+1
            
      count2=0
      for k in range(b):
         if count2==4:
            break
         elif tagdivide[k]=='<':
            count2=count2+1
      print str(i+1)+">  "+song[j:k-1]
      print ""
      
   #download urls
   x=len(redirecturllist)
   if x==0:
      print "no song found with such name , try using another keywords !!!"
   else :
      if x>15:
         z=15
      else:
         z=x
      
      finalurl1=range(z)
      for i in range(z):
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
      choice = -1 
      while choice<1 or choice >z:
         choice=input("enter the source number(1 to 10) (Recommended Choice is : Choice 1): ")
      
      urlchoice=finalurl1[choice-1]
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

      #print finalurl
      songurl=urllib.urlopen(finalurl).geturl()
      #print songurl

      path=raw_input("where to save file");
      f=open(path+songname+".mp3",'wb')
      f.write(urllib.urlopen(finalurl).read())
      f.close()
      print "done , saved in " + path
      ans=raw_input("want to download any other song (y/n) :")
