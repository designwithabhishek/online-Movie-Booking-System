from django.contrib import admin
from  .models import Auditorium,Show,Reviews,Movies,Layouts,Audi_layout,Cast,Mapper
from  django.core.exceptions import ValidationError
# Register your models here.
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name','message')
class AuditoriumAdmin(admin.ModelAdmin):
    list_display = ('audi_name', 'seat_count','audi_type')
class ShowAdmin(admin.ModelAdmin):
    list_display = ('movies','price','start_time','auditorium','end_time','date')
    fields = ['movies','price','start_time','end_time','date','auditorium']

class Audi_layoutAdmin(admin.ModelAdmin):
    list_display =('auditorium','seat_number','row')
admin.site.register(Auditorium,AuditoriumAdmin)
admin.site.register(Movies)
admin.site.register(Show,ShowAdmin)
admin.site.register(Audi_layout,Audi_layoutAdmin)
admin.site.register(Layouts)
admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(Cast)
admin.site.register(Mapper)