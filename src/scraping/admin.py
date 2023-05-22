from django.contrib import admin
from .models import City, Metro, Declaration, Error, Url

admin.site.register(City)
admin.site.register(Metro)
admin.site.register(Declaration)
admin.site.register(Error)
admin.site.register(Url)
