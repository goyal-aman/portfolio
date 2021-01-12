from django.contrib import admin

# local imports 
from timeline.models import Card, Link
# Register your models here.
admin.site.register(Card)
admin.site.register(Link)
