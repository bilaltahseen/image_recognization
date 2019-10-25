import requests
import cv2
import urllib.request
import re
import os
from bs4 import BeautifulSoup

key = cv2.waitKey(1)
webcam = cv2.VideoCapture(1)


def image_recg(image):

    t_val = image
    g_url = 'https://www.google.com/searchbyimage/upload'
    multipart = {
        'encoded_image': (t_val, open(t_val, 'rb')),
        'image_content': ''
    }
    headers = {
        'User-agent':
        'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
    }
    response2 = requests.post(g_url, files=multipart, allow_redirects=False)
    searchUrl = response2.headers['Location']
    s = requests.get(searchUrl, headers=headers).text
    soup = BeautifulSoup(s, 'html5lib')
    print('Possible Image Target..')
    print(soup.find('a', class_='fKDtNb').text)


while True:
    check, frame = webcam.read()
    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(1)
    if key == ord('s'):
        temp_file_name = 'temp_image_search.jpeg'
        cv2.imwrite(filename=temp_file_name, img=frame)
        W = 500
        oriimg = cv2.imread(temp_file_name)
        height, width, depth = oriimg.shape
        imgScale = W / width
        newX, newY = oriimg.shape[1] * imgScale, oriimg.shape[0] * imgScale
        newimg = cv2.resize(oriimg, (int(newX), int(newY)))
        cv2.imwrite(temp_file_name, newimg)
        webcam.release()
        cv2.destroyAllWindows()
        image_recg(temp_file_name)

        break
    elif key == ord('q'):
        webcam.release()
        cv2.destroyAllWindows()
        break
