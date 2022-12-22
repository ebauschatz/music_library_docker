SECRET_KEY = 'jgqh+cii^%s%!gz8g2c#zd)^dn0^^i*fq-$#)&#vse^y6&&aw*k3)thcw'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_django',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'music-library-database',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}