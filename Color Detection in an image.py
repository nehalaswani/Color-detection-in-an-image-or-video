#!/usr/bin/env python
# coding: utf-8

# # THE SPARK FOUNDATION
# ## IOT AND COMPUTER VISION
# ### TASK: Implement an image color detector which identifies all the colors in an image

# Importing necessary libraries

# In[1]:


import cv2
import numpy as np
import pandas as pd
from PIL import Image 


# Image we are using for color detection

# In[2]:


Image.open('/Users/dell/Desktop/color1.jpg') 


# Reading image using cv2

# In[3]:


img = cv2.imread('/Users/dell/Desktop/color1.jpg')
img=cv2.resize(img,(700,500))

clicked = False
r = g = b = xpos = ypos = 0


# Reading csv file with pandas and giving names to each column

# In[4]:


index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv(r'C:\Users\dell\Desktop\colors.csv', names=index, header=None)


# Function to calculate minimum distance from all colors and get the most matching color

# In[5]:


def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname 


# Function to get x,y coordinates of mouse double click 

# In[6]:


def draw_function(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)


# In[7]:


cv2.namedWindow('color detection')
cv2.setMouseCallback('color detection',draw_function)
while(1):

    cv2.imshow("color detection",img)
    if (clicked):
   
        #cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle 
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)

        #Creating text string to display( Color name and RGB values )
        text = getColorName(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        
        #cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)

        #For very light colours we will display text in black colour
        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
        clicked=False

    if cv2.waitKey(20) & 0xFF ==27:
        break
    
cv2.destroyAllWindows()


# In[ ]:




