
"""
Created on Mon Oct  7 18:06:02 2019

@author: 18127
"""
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as imgplt
import numpy as np
            #importing image and necessary functions
imgname = input('Enter the image filename: ')
img = Image.open(imgname, 'r')
mat = np.asarray(img)
            #defining the image with a user input, opening it to read, and converting it to a matrix.
height = mat.shape[0]
width = mat.shape[1]
            #defining the height and width from the matrix.

def Rot(mat):
    check = True
    
    while check == True:
        r = input('Enter "mirror" or the desired rotation amount in degrees: ')  #calling for user input so the code knows which rotation/mirror to perform.
        
        if r == "90":
            check = False
            newmat = np.zeros((width,height,3),dtype=np.uint8)  #creating a new matrix to edit.
            for i in range(0,width):
                for j in range(0,height):
                    newmat[i][j] = mat[height-j-1][i]   #Switching the width and height and inverting the height to complete the rotation.
              
        elif r == "180":
            check = False
            newmat = np.zeros((height,width,3),dtype=np.uint8)   #creating a new matrix to edit.
            for i in range(0,height):
                for j in range(0,width):
                    newmat[height-1-i][width-1-j] = mat[i][j]   #inverting both the height and width to complete the rotation.
       
        elif r == "270":
            check = False
            newmat = np.zeros((width,height,3),dtype=np.uint8)   #creating a new matrix to edit.
            for i in range(0,width):
                for j in range(0,height):
                    newmat[width-1-i][j] = mat[j][i]   #Switching the width and height and inverting the width to complete the rotation.
            
        elif r == "mirror":
            check = False
            newmat = np.zeros((height,width,3),dtype=np.uint8)   #creating a new matrix to edit.
            for i in range(0,height):
                for j in range(0,width):
                    newmat[i][width-1-j] = mat[i][j]   #inverting the width to complete the mirror.
        
        else:
            print('Error: Invalid Rotation Value')   #printing an error and asking for an input again if it is an invalid value.
    return newmat

newmat = Rot(mat)   #calling the function.
plt.imshow(newmat)   #displaying the image in the console.
imgplt.imsave("new.jpg",newmat)   #saving the new image as a jpg file.


