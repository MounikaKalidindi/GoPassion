from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Categories)
admin.site.register(Sub_Categories)
admin.site.register(Sub_Categories1)
admin.site.register(Categories_Sub_Categories_Mapping)
admin.site.register(Sub_Categories_Sub_Categories1_Mapping)
admin.site.register(Tutorials)
admin.site.register(FeedBack)
admin.site.register(Posts)
admin.site.register(Advertisements)
admin.site.register(Profile)
admin.site.register(Followers)

