from django.contrib import admin

# Register your models here.
from .models import Link,User

admin.site.register(Link)
admin.site.register(User)