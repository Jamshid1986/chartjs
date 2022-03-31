from django.contrib import admin


from .models import Post, EV, BEV

# Register your models here.
admin.site.register(Post)

admin.site.register(EV)

@admin.register(BEV)
class BEVAdmin(admin.ModelAdmin):
    list_display = ['year', 'bev_country', 'ownership']