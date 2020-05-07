# deep-fake-detection

# install
1. Open your terminal and go to somewhere you want to create project.
1. Write `git clone https://github.com/ondyari/FaceForensics` and press Enter.
1. download model from this [link](https://data.lip6.fr/cadene/pretrainedmodels/xception-b5690688.pth) and copy it to `FaceForensics/classification/network`.
1. In this directory, open the file `model.py` and change `/home/ondyari/.torch/models/xception-b5690688.pth` to `<Your project directory>/FaceForensics/classification/network/xception-b5690688.pth`.
1. Write `git clone https://github.com/mhomidi/deep-fake-detection.git` and press Enter.
1. create a `virtualenv` by Python 3.6 and put the source of your Python to it:
1. Install virtual environment for python.
1. Write `virtualenv -p python3.6 .venv` and press Enter.
1. Write `source .venv/bin/activate` and press Enter.
1. Write `cd deep-fake-detection` and press Enter.
1. Write `pip3 install -r requirements.txt` and press Enter.
1. It takes some minutes to install packages.
1. Write `python manage.py makemigrations` and press Enter.
1. Write `python manage.py migrate` and press Enter.
1. Write `python manage.py runserver` and press Enter.
