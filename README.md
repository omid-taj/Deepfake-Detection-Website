# deep-fake-detection

# install
1. Open your terminal and go to somewhere you want to create project.
1. Write `git clone https://github.com/ondyari/FaceForensics` and press Enter.
1. download model from this [link](https://data.lip6.fr/cadene/pretrainedmodels/xception-b5690688.pth) and copy it to `FaceForensics/classification/network`.
1. In this directory, open the file `model.py` and change `/home/ondyari/.torch/models/xception-b5690688.pth` to `<Your project directory>/FaceForensics/classification/network/xception-b5690688.pth`.
1. Write `git clone https://github.com/omid-taj/Deepfake-Detection-Website.git` and press Enter.
1. create a `virtualenv` by Python 3.6 and put the source of your Python to it:(via pip or homebrew)
1. Install virtual environment for python.
1. Write `virtualenv -p python3.6 .venv` and press Enter.
1. Write `source .venv/bin/activate` and press Enter.
1. Write `cd deep-fake-detection` and press Enter.
1. Write `pip3 install -r requirements.txt` and press Enter.
1. It takes some minutes to install packages.
1. Write `python manage.py makemigrations` and press Enter.
1. Write `python manage.py migrate` and press Enter.
1. Write `python manage.py runserver` and press Enter.
16. Open your browser and type localhost:8000.
17. You will be redirected to the main login page of the website.
18. If you already have an account login with your credentials and if not, click on sign up below the login button.
19. After you are logged in you will be redirected to the evaluation page. 
20. Find the file on your laptop and click on the Evaluate button.
21. You will see the name of your file and (preparing) beside it.The file is being evaluated.
22. Once the evaluation is finished the name will be changed to a blue link on the website that you can download(you will have to reload).


