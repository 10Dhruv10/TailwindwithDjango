from django.contrib import admin
from .models import ChaiVariety, ChaiReview, ChaiCertificate, Store

class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 2

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date')
    inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varieties', )

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai_varieties', 'certificate_number')

admin.site.register(ChaiVariety, ChaiVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)
