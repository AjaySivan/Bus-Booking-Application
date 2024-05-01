from django.contrib import admin
from .models import * 

admin.site.register(User)
admin.site.register(Seat)
admin.site.register(Stop)
admin.site.register(Fare)
admin.site.register(Bus)
admin.site.register(Booking)


