# recipe-or-so

## A HTML & CSS Project

A simple recipe site based on a YouTube tutorial:

[FreeCodeCamp.org](https://youtu.be/-8LTPIJBGwQ?si=A6fow5dNDeIBtu2w)

## Why Flask?

I didn’t want to copy-paste everything manually, so I set up a simple Flask app for templating.  
Later, I might expand it into a fully functional web app.

## How to Install & Use

### 1. Clone the Repository
```bash
git clone https://github.com/ChippisTraining/recipe-or-so.git
cd recipe-or-so
```

### 2. Create a Virtual Environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux or macOS
source venv/bin/activate

# On Windows
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# To exit the virtual environment
deactivate
```

### 3. Set Up the Environment File
- Copy or rename `.env.example` to `.env`
- Configure settings as needed

### 4. Start the Web App
```bash
python3 app.py
```

Now, you can access the web app at:  
[http://127.0.0.1:8000](http://127.0.0.1:8000)

Or at your chosen address if you modified the `.env` settings.
