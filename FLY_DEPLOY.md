# Fly.io Deployment Guide

## Prerequisites
Install Fly.io CLI:
- **Windows**: `powershell -Command "iwr https://fly.io/install.ps1 -useb | iex"`
- **Mac/Linux**: `curl -L https://fly.io/install.sh | sh`

## Step 1: Sign Up
```bash
fly auth signup
```
Or login if you have an account:
```bash
fly auth login
```

## Step 2: Launch App
```bash
cd catalyst_project
fly launch --no-deploy
```
- Choose app name (or press Enter for auto-generated)
- Select region (choose closest to you)
- Don't add PostgreSQL (we're using SQLite)
- Don't deploy yet

## Step 3: Set Secrets
```bash
fly secrets set SECRET_KEY="your-secret-key-here"
fly secrets set DEBUG=False
```

Generate a secret key:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## Step 4: Deploy
```bash
fly deploy
```

## Step 5: Create Admin User
```bash
fly ssh console
python manage.py createsuperuser
exit
```

## Your App URL
Your app will be live at: `https://YOUR-APP-NAME.fly.dev`

## Useful Commands
- **View logs**: `fly logs`
- **Check status**: `fly status`
- **Open app**: `fly open`
- **SSH into app**: `fly ssh console`
- **Redeploy**: `fly deploy`

## Free Tier Limits
- 3 shared-cpu-1x VMs with 256MB RAM
- 160GB outbound data transfer
- Generous free allowance

## Troubleshooting
If deployment fails:
1. Check logs: `fly logs`
2. Verify secrets: `fly secrets list`
3. Check app status: `fly status`
