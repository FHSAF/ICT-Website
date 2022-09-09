from django.contrib import admin
from .models import BlogsModel, BodyModel, CommentModel, Packages

admin.site.register(BlogsModel)
admin.site.register(BodyModel)
admin.site.register(CommentModel)
admin.site.register(Packages)
