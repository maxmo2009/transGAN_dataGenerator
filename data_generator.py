import numpy as np 
import matplotlib.pyplot as plt
from random import randint
from skimage.filters import gaussian
from skimage.draw import circle
from skimage.util import random_noise





def generate_A(size = (256,256),k = 100):


  x_data, y_data = np.ogrid[-np.pi:np.pi:256j, -np.pi:np.pi:256j]
  data_list = []
  label_list = []

  for i in range(0,k):
    label_A = np.zeros(size, dtype=np.int32)
    #generate texture
    r = np.sin(np.exp((np.sin(x_data*randint(1,5))**2 + np.cos(y_data*randint(1,5))**2)))
 
    # draw a circle on data and label
    rr, cc = circle(randint(120,136), randint(120,136), randint(50,80))
    r[rr,cc] = 0
    label_A[rr,cc] = 1

    r = random_noise(gaussian(r,sigma = 3))/r.max()

    data_list.append(r)
    label_list.append(label_A)
    

  np.save('data_a.npy', np.array(data_list))
  np.save('label_a.npy', np.array(label_list))

    # plt.imshow(r,cmap='Greys', interpolation='nearest')
    # plt.savefig(str(i)+'_A_data.png')
    # plt.imshow(label_A,cmap='Greys', interpolation='nearest')
    # plt.savefig(str(i)+'_A_label.png')

def generate_B(size = (256,256),k=100):
  x_data, y_data = np.ogrid[-np.pi:np.pi:256j, -3*np.pi:3*np.pi:256j]
  data_list = []
  label_list = []
  for i in range(0,k):
    label_B = np.zeros(size, dtype=np.int32)
    #generate texture
    r = np.sin(x_data + randint(1,10)) - np.cos(y_data + randint(1,10))
    r = r/r.max()
    # draw a circle on data and label
    rr, cc = circle(randint(120,136), randint(120,136), randint(50,80))
    r[rr,cc] = 0
    label_B[rr,cc] = 1
     
    r = random_noise(gaussian(r,sigma = 3))/r.max()

    data_list.append(r)
    label_list.append(label_B)

  print np.array(data_list).shape
  np.save('data_b.npy', np.array(data_list))
  np.save('label_b.npy', np.array(label_list))
    

    # plt.imshow(r,cmap='Greys', interpolation='nearest')
    # plt.savefig(str(i)+'_B_data.png')
    # plt.imshow(label_B,cmap='Greys', interpolation='nearest')
    # plt.savefig(str(i)+'_B_label.png')


generate_A()
generate_B()

