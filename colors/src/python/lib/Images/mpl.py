from matplotlib import pyplot as plt
import numpy as np
import cv2
import urllib

def show_cv2_img(img:np.ndarray)->None:
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    show_img(img)

def show_img(img:np.ndarray)->None:
    plt.axis('off')
    plt.imshow(img)

def show_img_url(url:str)->None:
    url_response = urllib.request.urlopen(url)
    img = np.array(bytearray(url_response.read()), dtype=np.uint8)
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    show_cv2_img(img)