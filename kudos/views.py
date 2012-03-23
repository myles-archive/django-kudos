from datetime import datetime

from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseNotAllowed, HttpResponseRedirect

from kudos.models import Kudos


class GiveKudosView(View):
	
	@csrf_exempt
	def dispatch(self, *args, **kwargs):
		return super(GiveKudosView, self).dispatch(*args, **kwargs)
	
	def post(self, request, *args, **kwargs):
		content_type = ContentType.objects.get(app_label=request.POST.get('app_label'), model=request.POST.get('model'))
		content_object = content_type.get_object_for_this_type(pk=request.POST.get('object_pk'))
		
		if request.user.is_authenticated():
			kudos = Kudos.objects.create(content_object=content_object, date_added=datetime.now(), user=request.user)
		else:
			kudos = Kudos.objects.create(content_object=content_object, date_added=datetime.now())
		
		return HttpResponseRedirect(content_object.get_absolute_url())