# recipe-or-so

## a html & css project

a simple recipe side via a yt turial

[freeCodeCamp.org](https://youtu.be/-8LTPIJBGwQ?si=A6fow5dNDeIBtu2w)

## why flask

i didnt want to copy paste all so i setup a simple flask app for templating
later i maybe make it work

## how to use

1. clone the repo
```bash
git clone https://github.com/ChippisTraining/recipe-or-so.git
cd recipe-or-so.git
```

2. create the venv
```bash
# create venv
python3 -m venv venv

# activate venv
# on linux or mac
source venv/bin/activate

# on windows
.\venv\Scripts\activate

# install modules
pip install -r requirements.txt

# to exit venv
deactivate
```

3. create the env file
you need to copy/rename the .env.example file to/as .env

4. start the web app
```bash
python3 app.py
```

then you can acces the web app under
[127.0.0.1:8000](127.0.0.1:8000)

or when you changed the .env under your chosen
