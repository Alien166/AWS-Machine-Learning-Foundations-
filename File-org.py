#!/usr/bin/env python
# coding: utf-8

# In[1]:


defintion = """"
computer file is a resource for recording data on a computer storage device, primarily identified by its filename. Just as words can be written on paper, so can data be written to a computer file. Files can be shared with and transferred between computers and mobile devices via removable media, networks, or the Internet.
Different types of computer files are designed for different purposes. A file may be designed to store an image, a written message, a video, a program, or any wide variety of other kinds of data. Certain files can store multiple data types at once. """


# In[3]:


open("Book.txt","w").write(defintion)


# In[5]:


text=open("Book.txt","r")
print(text.read())


# In[10]:


p1=open("Book.txt")
for i in p1:
    print(i)


# In[11]:


txt ="         Hi"
print(txt)
txt="                Hi"
print(txt.strip())
txt="!!!!!!!!Hi!!!!!!!!!"
print(txt.strip("!"))


# In[12]:


p1=open("Book.txt")
for i in p1:
    print(i.strip())


# In[13]:


txt = "one one was a race horse"
x = txt.replace("one","three")
print(x)

txt = "one one was a race horse,two two was one"
x= txt.replace("one","three",2)
print(x)


# In[ ]:




