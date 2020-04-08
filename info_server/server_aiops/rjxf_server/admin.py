from django.contrib import admin

# Register your models here.
from . import models

class FlowAdmin(admin.ModelAdmin):
    list_display = (
        'date'
        , 'rjxf_id'
        , 'rjxf_txt'
        , 'file_name'
        , 'file_size'
        , 'rjxf_run_date'
        , 'rjxf_stat'
        , 'rjxf_num_count'
        , 'make_date'
        , 'make_oper'
        , 'update_date'
        , 'update_oper'
    )  # list
    search_fields = (
        'rjxf_id',
        'file_size',
        'file_name',
        'rjxf_txt',
    )
    # fields = ('rjxf_id', 'rjxf_type') @

admin.site.register(models.flow, FlowAdmin)

class file_dir(admin.ModelAdmin):
    list_display = ('name', 'name_ch')  # list
admin.site.register(models.file_dir, file_dir)
#admin.site.register(models.flow)

class ftp_path(admin.ModelAdmin):
    list_display = ('ftp_id', 'ftp_pwd')
admin.site.register(models.ftp_path, ftp_path)