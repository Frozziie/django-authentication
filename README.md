# Login and Registration
## Functionality
- Log in
- Create Account
- Log out
- Reset password
- Change password

## Installing

### Clone the project

```
git clone https://github.com/Frozziie/django-authentication-v2.git
```

### Install dependencies & activate virtualenv

```
1. Install
pip install virtualenv

2. Create virtual environment
virtualenv <name>

3. Activate
<name>\Scripts\activate

4. Dependencies
pip install -r requirements/local.txt | production.txt
```

### Configure the settings (connection to the database, connection to an SMTP server, and other options)

- Edit `django-authentication/settings/base.py` if you want to change general settings.

- Edit `django-authentication/settings/local.py` if you want to develop the project.

- Edit `django-authentication/settings/production.py` if you want to run the project in production.

**Don't forget to change which settings are you going to use in manage.py.**

### Apply migrations

```
python manage.py migrate
```

### Running

#### A development server

Just run this command:

```
python manage.py runserver
```