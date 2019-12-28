from django.contrib import admin



from .models import AuthorProfile, Paper, Review, Department, MyMessage, Liked 




admin.site.register(AuthorProfile)

admin.site.register(Paper)

admin.site.register(Review)

admin.site.register(Department)

admin.site.register(MyMessage)

admin.site.register(Liked)


