from django.contrib import admin
from . import models

# Register your models here.
class infoAdmin(admin.ModelAdmin):
    list_display = (
        'id'
        , 'title'
        , 'answer_oper'
        , 't_stat'
        , 't_channel'
        , 't_type'
        , 'info_check_flag'
        , 't_close'
        , 'trans_code'
        , 'trans_err'
        , 'input_date'
        , 'answer_date'
        , 'update_date'
    )  # list
    search_fields = (
        'id',
        'title',
        'problem_info',
        'problem_answer',
    )
    # fields = ('rjxf_id', 'rjxf_type') @

admin.site.register(models.info, infoAdmin)

class info_statAdmin(admin.ModelAdmin):
    list_display = (
        'id'
        , 'stat_id'
        , 'stat_name'
    )  # list
    # fields = ('rjxf_id', 'rjxf_type') @

admin.site.register(models.info_stat, info_statAdmin)

class channelAdmin(admin.ModelAdmin):
    list_display = (
        'id'
        , 'code'
        , 'name'
    )  # list

admin.site.register(models.info_channel, channelAdmin)
admin.site.register(models.info_close)

class typeAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')  # list
admin.site.register(models.info_type, typeAdmin)

class info_comments(admin.ModelAdmin):
    list_display = ('id','name', 'i_stat', 'update_oper', 'update_date')  # list
    search_fields = ('id','name','update_oper',)
admin.site.register(models.info_comments, info_comments)
# admin.site.register(models.info_comments)
class info_comments_stat(admin.ModelAdmin):
    list_display = ('code', 'name')  # list
admin.site.register(models.info_comments_stat, info_comments_stat)

class action(admin.ModelAdmin):
    list_display = ('type', 'text', 'oper', 'date')  # list
    search_fields = (
        'text',
        'oper',
        'date',
    )
admin.site.register(models.action, action)

class action_type(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'score')  # list
admin.site.register(models.action_type, action_type)