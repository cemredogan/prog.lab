
# coding: utf-8

# In[25]:


import csv
import sys

file=open("input_hw_2.csv","r+",encoding="utf-8")
read=file.read() #dosyayı okudum
print(read)


# In[33]:


a=read.split(";") #split yapabilmen için listede olmaması lazim . 
print(a)
tarih = []
for i in range(3,len(a),3): #aylara eriştim
    tarih.append(a[i].split("-"))

print(tarih[0][1])


# In[40]:


cikis_ayi= []
for i in range(len(tarih)): #çıkış aylarına gittim
    cikis_ayi.append(tarih[i][1])
print(cikis_ayi)


# In[41]:


def my_frequency_with_dict(list): #frekansı hesapladım
    frequency_dict={}
    for item in list:
        if(item in frequency_dict):
            frequency_dict[item]=frequency_dict[item]+1
        else:
            frequency_dict[item]=1
    return frequency_dict


# In[76]:


frekans_cıkıs_ay=my_frequency_with_dict(cikis_ayi) #cıkış ay frekansları
print(frekans_cıkıs_ay)


# In[96]:


liste_ay=frekans_cıkıs_ay.values() #sözlükteki değerleri listeye attım ortalama hesabı için


# In[97]:


liste_ay


# In[98]:


def ortalama (my_list):
    toplam=0
    s=0
    for item in my_list:
        s=s+1
        toplam=item+toplam
        ort=toplam/s
        
    return ort


# In[99]:


liste_ay_ort=ortalama(liste_ay)
print(liste_ay_ort)


# In[100]:


sırala=sorted(liste_ay) #median bulabilmek için listeyi sıraladım
print(sırala)


# In[101]:


def my_median(my_list):
    n=len(my_list)
    if n%2==1:
        middle=int(n/2)+1
        median=my_list[middle]
    else:
        middle_1=int(n/2)-1
        middle_2=middle_1+1
        median=(my_list[middle_1]+my_list[middle_2])/2
    return median


# In[102]:


ay_median=my_median(sırala)
print(ay_median)


# In[110]:


with open("170401017_hw_2_output.txt","w",encoding="utf-8") as dosya:
 dosya.write("MEDYAN:"+ str(ay_median) + "\n")
 dosya.write("ORTALAMA:"+ str(liste_ay_ort))

