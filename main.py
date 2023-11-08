import requests

img_url = 'https://www.interfax.ru/ftproot/photos/photostory/2022/04/29/week/week7_1100.jpg'
video_url = 'https://youtube.com/shorts/PWThMaYckmU?si=aSfAGiDGm4Lq1rlu'
def download_img(url=''):
    try:
        response = requests.get(url=url)
        with open('req_img', 'wb') as file:
            file.write(response.content)
        return 'Img successfully downloaded!'

    except Exception as _ex:
        return 'Upps... Chech the URL please!'


def download_video(url=''):
    try:
        response = requests.get(url=url)
        with open('req_video', 'wb') as file:
            file.write(response.content)
        return 'Img successfully downloaded!'

    except Exception as _ex:
        return 'Upps... Chech the URL please!'



def main():
   # print(download_img(url=img_url))
    print(download_video(url=video_url))

if __name__ == '__main__':
    main()

