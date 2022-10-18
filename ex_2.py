import threading
import os
from urllib import request
from urllib.error import HTTPError
from urllib.parse import urlparse


class NewThread(threading.Thread):
    def __init__(self, thread_number, url):
        threading.Thread.__init__(self)
        self.url = url
        self.name = "Thread #%s" % (thread_number + 1)
        self.start()

    def run(self):
        # перевіряємо чи є файл по url
        try:
            # парсимо url, та беремо звідти ім'я файлу
            a = urlparse(self.url)
            filename = os.path.basename(a.path)
            print("Thread %s is downloading - %s" % (self.name, filename))

            # завантажуємо файл
            request.urlretrieve(self.url, filename)
        except HTTPError:
            print("ERROR!!! (%s). File not found on this url: %s" % (self.name, self.url))
            # pass

def load_files(file_urls):
    for i, url in enumerate(file_urls):
        NewThread(i, url)


if __name__ == "__main__":
    urls = ["https://www.irs.gov/pub/irs-pdf/f1040.pdf",
            "https://www.irs.gov/pub/irs-pdf/f1040a.pdf",
            "https://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
            "https://www.irs.gov/pub/irs-pdf/f1040es.pdf",
            "https://www.irs.gov/pub/irs-pdf/f1040sb.pdf"
            ]
    load_files(urls)

