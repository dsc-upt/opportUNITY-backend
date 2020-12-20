from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from django.utils.html import format_html

from administration.models import User, ExampleModel, Organisation, Partner, Faq, Opportunity, MenuItem, Article, \
    Newsletter, WantToHelp, \
    OpportunityCategory, UserProfile
from administration.admin_site import admin_site


@admin.register(User, site=admin_site)
class UserAdmin(BaseUserAdmin):
    pass


@admin.register(Group, site=admin_site)
class GroupAdmin(GroupAdmin):
    pass


class BaseModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


@admin.register(ExampleModel, site=admin_site)
class ExampleModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age')


@admin.register(Partner, site=admin_site)
class PartnerAdmin(BaseModelAdmin):
    list_display = ('name', 'slug', 'website', 'logo', 'is_published')
    list_filter = ('is_published', 'created', 'updated')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Faq, site=admin_site)
class FaqAdmin(BaseModelAdmin):
    list_display = ('question', 'answer', 'is_published')
    list_filter = ('is_published', 'created', 'updated')
    search_fields = ('question', 'answer')
    list_editable = ('is_published',)


@admin.register(Organisation, site=admin_site)
class OrganisationAdmin(BaseModelAdmin):
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Opportunity, site=admin_site)
class OpportunityAdmin(BaseModelAdmin):
    list_display = ('name', 'show_org_url', 'deadline', 'show_opp_url', 'description')
    list_filter = ('deadline', 'organisation')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

    def show_opp_url(self, obj):
        return format_html(f"<a href='{obj.url}'>{obj.url}</a>")

    show_opp_url.short_description = "url"

    def show_org_url(self, obj):
        return format_html(f"<a href='{obj.organisation.get_absolute_url()}'>{obj.organisation.name}</a>")

    show_org_url.short_description = "organisation"


@admin.register(MenuItem, site=admin_site)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'link', 'image', 'parent')
    list_filter = ('parent',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Article, site=admin_site)
class ArticleAdmin(BaseModelAdmin):
    list_display = ('title', 'slug', 'image', 'description', 'is_published', 'created')
    list_filter = ('is_published', 'created', 'updated')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Newsletter, site=admin_site)
class NewsletterAdmin(BaseModelAdmin):
    list_display = ('email', 'slug', 'other', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('email',)
    prepopulated_fields = {'slug': ('email',)}


@admin.register(WantToHelp, site=admin_site)
class WantToHelpAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_filter = ('name', 'email')
    search_fields = ('email',)


@admin.register(OpportunityCategory, site=admin_site)
class OpportunityCategoryAdmin(BaseModelAdmin):
    list_display = ('name', 'slug', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(UserProfile, site=admin_site)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'organisation', 'description')
    list_filter = ('organisation',)
    search_fields = ('user', 'organization')

# admin_site.register(ExampleModel, ExampleModelAdmin)
# admin_site.register(User, UserAdmin)
# admin_site.register(Group, GroupAdmin)
# admin_site.register(Partner, PartnerAdmin)
# admin_site.register(Faq, FaqAdmin)
# admin_site.register(Organisation, OrganisationAdmin)
# admin_site.register(Opportunity, OpportunityAdmin)
# admin_site.register(MenuItem, MenuItemAdmin)
# admin_site.register(Article, ArticleAdmin)
# admin_site.register(Newsletter, NewsletterAdmin)
# admin_site.register(WantToHelp, WantToHelpAdmin)
# admin_site.register(OpportunityCategory, OpportunityCategoryAdmin)
# admin_site.register(UserProfile, UserProfileAdmin)
