
# coding: utf-8

# In[1]:


import sympy as sym #kütüphaneleri çağırdık sembol için
from sympy import Symbol,factorial
from sympy import pprint


# In[2]:


x=Symbol("x") #x,n ve p yi sembolleştirdik
n=Symbol("n")
p=Symbol("p")


# In[3]:


part_0=sym.factorial(n)/(sym.factorial(x)*sym.factorial(n-x)) #formülün ilk parçası
pprint(part_0)


# In[4]:


part_1=p**x #formülün ikinci parçası
pprint(part_1)


# In[5]:


part_2=(1-p)**(n-x) #formülün üçüncü parçası
pprint(part_2)


# In[6]:


my_f=(part_0*part_1*part_2) #formülün partlarını birleştirip oluşturduk
pprint(my_f)


# In[8]:


get_ipython().run_line_magic('matplotlib', 'inline #çizim için gerekli olan kütüphaneler')
import matplotlib.pyplot as plt


# In[11]:


x_values=[] #değerleri oluşturduk
y_values=[]
for value in range (0,50): #döngü ile aralığı belirledik 0 ile 50
    y=my_f.subs({p:0.5,n:50,x:value},title="Binomial Distribution") #p ve n ye değer atadık
    y_values.append(y) 
    x_values.append(value)
    print(value,y)


# In[12]:


plt.plot(x_values,y_values) #değerleri (x_values,y_values) tanımladıktan sonra çizim için fonksiyona yollarız
plt.show() #çizimi görüntüler

