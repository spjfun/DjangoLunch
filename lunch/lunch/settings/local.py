from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pb^(lfh$s4m@$jb5jzliax5g*_rlt3!&54n#y)(n!w^-nji_wb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True



# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(BASE_DIR), 'db.sqlite3'),
    }
}