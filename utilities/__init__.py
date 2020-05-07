import os

from django.core.files.storage import FileSystemStorage

import threading
from DeepFake.settings import BASE_DIR
from detection.models import File


def save_file(file, user):
    fs = FileSystemStorage()
    filename = fs.save(file.name, file)
    uploaded_file_url = fs.url(filename)
    file = File.objects.create(url=uploaded_file_url, owner=user)
    filename = uploaded_file_url.split('/')[-1]
    filename = filename.split('.')[0] + '.avi'
    file.name = filename
    file.save()
    try:
        x = threading.Thread(target=convert_file, args=(uploaded_file_url, ))
        x.start()
    except:
        print('Problem in starting thread')


def convert_file(uploaded_file_url):
    file = File.objects.filter(url=uploaded_file_url)
    file = file[0] if file else None
    if not file:
        return
    filename = uploaded_file_url.split('/')[-1]
    filename = filename.split('.')[0] + '.avi'
    os.system('python ../FaceForensics/classification/detect_from_video.py -i .' + uploaded_file_url +
              ' -o ./media/results/')
    file.result = '/media/results/' + filename
    file.name = filename
    file.save()

