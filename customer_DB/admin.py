from django.contrib import admin
from customer_DB.models import Details, Measurements

# Register your models here.
class DetailsAdmin(admin.ModelAdmin):
    pass

class MeasurementsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Details, DetailsAdmin)
admin.site.register(Measurements, MeasurementsAdmin)