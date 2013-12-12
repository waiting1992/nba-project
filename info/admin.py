from django.contrib import admin

# Register your models here.

from info.models import Player, Team, Coach

admin.site.register(Player)
admin.site.register(Coach)
admin.site.register(Team)
