from django.contrib import admin as a

from .models import *

a.site.register(Note)
a.site.register(Folder)
a.site.register(Photo)