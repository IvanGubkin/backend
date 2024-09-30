from django.contrib import admin

from .models import Orders, Category, Client, ClientStatus, State, Priority


admin.site.register(Orders)
admin.site.register(Category)
admin.site.register(Client)
admin.site.register(ClientStatus)
admin.site.register(State)
admin.site.register(Priority)

