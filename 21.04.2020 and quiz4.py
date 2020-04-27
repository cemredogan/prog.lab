
# coding: utf-8

# In[54]:


#HEAP IMPLEMENT.
#heap bir kuyruk yapısıdır.liste üzerinde arama ,çıkarma,ekleme vs. işlemleri yapılır.
#buradaki array bir diziyi ,i ise index i temsil eder
def min_heapfy(array,i):#iki değeri karşılaştır karşılaştırırken sınırı geçme ve en küçük değeri min olarak belirle.
    left=2*i+1 #sol çocuk
    right=2*i+2 #sağ çocuk
    length=len(array)-1
    smallest=i #i nin bulunduğu nokta
    if left<=length and array[i]>array[left]:
        smallest=left
    if right<=length and array[smallest]>array[right]:
        smallest=right
    if smallest!=i:
        array[i],array[smallest]=array[smallest],array[i]
        min_heapfy(array,i)#exchange yaptığı değerle tekrar kendisini çağırır.


# In[55]:


def build_min_heap(array):#arrayde ki bütün elemanlar için çağırıyoruz.parametre olarak diziyi alıyor
    for i in reversed(range(len(array)//2)):#reversed() fonksiyonu tersten başlamasını sağlar
        min_heapfy(array,i)


# In[56]:


my_array_1=[8,10,3,4,7,15,1,2,16]


# In[57]:


build_min_heap(my_array_1)
print(my_array_1)


# In[58]:


def insert(array,i):#elemanı heape ekler
    array.append(i)#diziye ekliyoruz
    length = len(array)-1
    if length<=0:
        print("heap  boş")
        return    
    parent = (length-1)//2
    while parent>=0 and array[parent] > array[length]:
        array[parent],array[length] = array[length],array[parent]            
        length = parent
        parent = (length-1)//2
    


# In[59]:


def remove(eleman):#son elemanı siler
    length = len(eleman)
    if length<=0: #heap in boş olup olmadığını kontrol ediyoruz.
        print("HEAP BOS")
        return
    eleman.pop() #pop () fonksiyonu sondaki elemanı çıkarır


# In[60]:


remove(my_array_1)
print(my_array_1)
insert(my_array_1,122)
insert(my_array_1,42)
insert(my_array_1,33)
print(my_array_1)
remove(my_array_1)
print(my_array_1)


# In[61]:


#heap sort
def heapSort(array):#sıralama yapar
    array=array.copy() #copy() fonksiyonu ile arrayi kopyalayıp aldık
    build_min_heap(array)#heapi oluşturduk
    sorted_array=[]#aldığımız sayıları atacağımız boş dizi
    for _ in range(len(array)):
        array[0],array[-1]=array[-1],array[0]
        sorted_array.append(array.pop())#pop sondakini çıkarır 
        min_heapfy(array,0)
    return sorted_array
    


# In[62]:


my_array_2=heapSort(my_array_1)
print(my_array_1,my_array_2)

