import os
from dj_db2.settings import BASE_DIR

SECRET_KEY = '-6y_1n$o1jcf0*07)7db2c2g2*rh(lqg6rwrcc8$t6ilbok5l!'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}