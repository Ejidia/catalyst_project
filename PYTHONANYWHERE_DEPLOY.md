# PythonAnywhere Deployment Guide

## Step 1: Create PythonAnywhere Account
1. Go to https://www.pythonanywhere.com
2. Sign up for a free Beginner account
3. Confirm your email

## Step 2: Clone Your Repository
1. Go to "Consoles" tab → Start a new "Bash" console
2. Run these commands:
```bash
git clone https://github.com/Ejidia/catalyst_project.git
cd catalyst_project
```

## Step 3: Create Virtual Environment
```bash
mkvirtualenv --python=/usr/bin/python3.10 myenv
pip install -r requirements.txt
```

## Step 4: Configure Web App
1. Go to "Web" tab → "Add a new web app"
2. Choose "Manual configuration"
3. Select "Python 3.10"

## Step 5: Configure WSGI File
1. In "Web" tab, click on WSGI configuration file link
2. Delete all content and replace with content from `pythonanywhere_wsgi.py`
3. Replace `YOUR_USERNAME` with your PythonAnywhere username
4. Save the file

## Step 6: Set Static Files
In "Web" tab, add these static file mappings:
- URL: `/static/`
- Directory: `/home/YOUR_USERNAME/catalyst_project/staticfiles`

## Step 7: Run Migrations and Collect Static
In Bash console:
```bash
cd ~/catalyst_project
python manage.py migrate
python manage.py collectstatic --noinput
```

## Step 8: Create Admin User
```bash
python manage.py createsuperuser
```
Follow prompts to create admin account.

## Step 9: Set Environment Variables (Optional)
In "Web" tab, scroll to "Environment variables" section:
- Add `SECRET_KEY` with a secure random string
- Add `DEBUG` = `False` for production

## Step 10: Reload Web App
Click the green "Reload" button in "Web" tab

Your app will be live at: `https://YOUR_USERNAME.pythonanywhere.com`

## Important Notes:
- Free tier has limitations (daily CPU quota, no custom domain)
- Database file location: `/home/YOUR_USERNAME/catalyst_project/db.sqlite3`
- To update code: `git pull` in bash console, then reload web app
- Check error logs in "Web" tab → "Log files" section
