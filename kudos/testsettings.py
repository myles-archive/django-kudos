DEBUG = True
DEBUG_TEMPLATE = True
SITE_ID = 1
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': '/tmp/asgard-kudos-devel.db'
	}
}
INSTALLED_APPS = [
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.admin',
	'django.contrib.sites',
	'django.contrib.flatpages',
	
	'kudos',
]
ROOT_URLCONF = 'kudos.testurls'
MIDDLEWARE_CLASSES += (
	'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)