from django.contrib import admin
from noticeBoard.models import AdminNotice
# Register your models here.
# admin.site.register(AdminNotice)
@admin.register(AdminNotice)
class AdminNoticeAdmin(admin.ModelAdmin):
    list_display = ('id', 'notice', 'date')
