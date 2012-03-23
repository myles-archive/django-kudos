from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType

class Kudos(models.Model):
	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = generic.GenericForeignKey()
	
	user = models.ForeignKeyField(User, blank=True, null=True)
	
	date_added = models.DateTimeField(_('date added'), auto_now_add=True)
	
	class Meta:
		verbose_name = _('kudos')
		verbose_name_plaural = _('kudos')
		db_table = 'kudos'
		ordering = ('-date_added',)
		get_latest_by = 'date_added'
	
	def __unicode__(self):
		return _(u"Kudos for %s" % self.content_object.__unicode__)