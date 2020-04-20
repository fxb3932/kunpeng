from django.contrib import admin

# Register your models here.
from . import models

class ConfigAdmin(admin.ModelAdmin):
    list_display = (
        'plat_id'
        , 'plat_name'
        , 'name_ch'
        , 'name'
        , 'user'
        , 'sys'
        , 'ip'
        , 'team'
        , 'worker'
        , 'bank'
        , 'port'
        , 'ver'

    )  # list
    search_fields = (
        'plat_name',
        'ip',
        'name_ch',
        'name',
    )

admin.site.register(models.config, ConfigAdmin)

class config_discoveryAdmin(admin.ModelAdmin):
    list_display = (
        'plat'
        , 'bank_id'
        , 'bank_no'
        , 'bank_name'
        , 'bank_group'
    )  # list
admin.site.register(models.config_discovery, config_discoveryAdmin)


# admin.site.register(models.cmdb_config_discovery)
# class c_configAdmin(admin.ModelAdmin):
#     list_display = (
#         'plat_id'
#         , 'app_server'
#         , 'bank'
#     )  # list
# admin.site.register(models.c_config, c_configAdmin)
# admin.site.register(models.c_config)
admin.site.register(models.c_config_v1)

admin.site.register(models.i_plat)
admin.site.register(models.i_bank)
admin.site.register(models.i_plat_ver)
admin.site.register(models.i_app_server)
admin.site.register(models.i_agent_ver)
admin.site.register(models.i_app_type)
admin.site.register(models.i_app_stat)
admin.site.register(models.i_initiate_bank)
admin.site.register(models.i_app_mode)
admin.site.register(models.i_app_team)

class user_info(admin.ModelAdmin):
    list_display = ('first_name', 'qq_no', 'group', 'score')  # list
admin.site.register(models.user_info, user_info)

class i_user_group(admin.ModelAdmin):
    list_display = ('code', 'name')  # list
admin.site.register(models.i_user_group, i_user_group)

class action(admin.ModelAdmin):
    list_display = ('app_type', 'action_type', 'info_id', 'score', 'oper', 'date', 'text')  # list
admin.site.register(models.action, action)

class action_app_type(admin.ModelAdmin):
    list_display = ('code', 'name')  # list
admin.site.register(models.action_app_type, action_app_type)

class action_type(admin.ModelAdmin):
    list_display = ('code', 'name', 'score')  # list
admin.site.register(models.action_type, action_type)

# class productAdmin(admin.ModelAdmin):
#     list_display = (
#         'name'
#         , 'name_ch'
#         , 'bank'
#     )  # list
# admin.site.register(models.product, productAdmin)
# admin.site.register(models.bank)
# admin.site.register(models.server)

