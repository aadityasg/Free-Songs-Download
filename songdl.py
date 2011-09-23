#including import modules
import urllib
from BeautifulSoup import BeautifulSoup as bs

#one can use do-while , i used while so ket ans='y' for the first time !!
ans='y'
while ans=='y' or ans=='Y':
   songname=raw_input("enter the song name : ")
   songnamelist=list(songname)
   
   #getting the songname in the desired form

   x=len(songnamelist)
   songnamesrch=''
   for i in range(x):
      if songnamelist[i]==' ':
         songnamelist[i]='-'
      songnamesrch=songnamesrch+songnamelist[i]
   
   #seearching the song on the website !!
   
   url1="http://justfreemp3.com/search/mp3/1/"+songnamesrch+".html"
   print url1
   soup=bs(urllib.urlopen(url1).read())
   redirecturllist=soup.findAll('a',rel="nofollow",target="_blank")
   
   #finding the total number or sources found and displaying them
   x=len(redirecturllist)
   if x==0:
      print "no song found with such name , try using another keywords !!!"
   else :
      if x>10:
         z=10
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
        print str(i+1)+" > " + finalurl1[i]
        print ""
      
      #again you can use do-while loop
      choice = -1 
      while choice<1 or choice >z:
         choice=input("enter the source number(1 to 10) (Recommended Choice is : Choice 1): ")
      
      #getting the url that user selected
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
      songurl=urllib.urlopen(finalurl).geturl()
    
      #geting the path of the destination folder
      path=raw_input("where to save file");
      f=open(path+songname+".mp3",'wb')
      f.write(urllib.urlopen(finalurl).read())
      f.close()
      print "done , saved in " + path
      
      #checks if user wants to download any more songs or not !!
      ans=raw_input("want to download any other song (y/n) :")