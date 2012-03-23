from django.conf.urls.defaults import patterns, url

from kudos import views

urlpatterns = patterns('',
	url(r'give/$',
		view = views.GiveKudosView.as_view(),
		name = 'kudos_give',
	),
)