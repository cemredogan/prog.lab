
# coding: utf-8

# In[12]:


def get_words(): #kelimeleri ayırdık dosyaları 1 ile 10 aralıgında okuttuk
    my_list=[]
    for i in range(1,3): #dosya aralığını siz belirleyebilirsiniz
        with open("{}.txt".format(i),"r",encoding="utf-8") as f:
            contents=f.read()
            words=contents.split()
            for word in words:
                my_list.append(word)
    return my_list


def get_hist(my_list): #kelimelerin kaç kere kullanıldığının histogramını bulduk
    wordHist={}
    for w in my_list:
        if w in wordHist.keys():
            wordHist[w]=wordHist[w]+1
        else:
            wordHist[w]=1
    return wordHist

list=get_words()
a=get_hist(list)
#print(a)
#print(list)

def sonrakiKelimeler(my_list,text): #sonra gelecek kelimelerin tahmini
    words=text.split()
    lenwords=len(words)
    lenWordList = len(my_list)
    nextword1=[]

    if lenwords>6:
        print("LÜTFEN 5 KELİMEDEN FAZLA GİRMEYİNİZ.")

    else:
        for i in range(lenWordList-lenwords):
            for j in range(lenwords):
                if my_list[i]==words[j]:
                    i+=1
                    if(j==lenwords-1):
                        nextword1.append(my_list[i])
    return nextword1

##########YAZILMAK İSTENİLEN KELİMELER BURAYA YAZILMALI TXT. DOSYASINDAKİ YAZIM İLE AYNI OLMALI....
x=sonrakiKelimeler(get_words(),"her eylemin bir sonucu vardır buna göre hareket edilmelidir.") 
print(x)


y=get_hist(x) #gelecek en yüksek kelimenin histogramı
print(y)

