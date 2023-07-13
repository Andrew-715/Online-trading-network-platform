from django.contrib import admin
from django.db.models import QuerySet
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from core.models import Retail, Factory, \
    PrivateBusinessman, Storage, Contacts, Products


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'contacts')


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('email', 'country', 'city')
    list_filter = ('city',)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    pass


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ('name', 'provider', 'view_provider_link', 'arrears_over_provider')
    actions = ['clear_arrears_over_provider']

    def view_provider_link(self, obj):
        url = (
                reverse('admin:core_factory_changelist')
                + '?'
                + urlencode({'id': f'{obj.provider_id}'})
        )
        return format_html('<a href="{}"> Factory info</a>', url)

    view_provider_link.short_description = 'Factory'

    @admin.action(description='Очистить задолженность перед поставщиком')
    def clear_arrears_over_provider(self, request, queryset: QuerySet):
        count_deleted = queryset.update(arrears_over_provider=0)
        self.message_user(
            request,
            f'Было очищено {count_deleted} задолженностей'
        )


@admin.register(Retail)
class RetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'provider', 'view_provider_link', 'arrears_over_provider')
    actions = ['clear_arrears_over_provider']

    def view_provider_link(self, obj):
        url = (
                reverse('admin:core_storage_changelist')
                + '?'
                + urlencode({'id': f'{obj.provider_id}'})
        )
        return format_html('<a href="{}"> Storage info</a>', url)

    view_provider_link.short_description = 'Storage'

    @admin.action(description='Очистить задолженность перед поставщиком')
    def clear_arrears_over_provider(self, request, queryset: QuerySet):
        count_deleted = queryset.update(arrears_over_provider=0)
        self.message_user(
            request,
            f'Было очищено {count_deleted} задолженностей'
        )


@admin.register(PrivateBusinessman)
class PrivateBusinessmanAdmin(admin.ModelAdmin):
    list_display = ('name', 'provider', 'view_provider_link', 'arrears_over_provider')
    actions = ['clear_arrears_over_provider']

    def view_provider_link(self, obj):
        url = (
                reverse('admin:core_storage_changelist')
                + '?'
                + urlencode({'id': f'{obj.provider_id}'})
        )
        return format_html('<a href="{}"> Storage info</a>', url)

    view_provider_link.short_description = 'Storage'

    @admin.action(description='Очистить задолженность перед поставщиком')
    def clear_arrears_over_provider(self, request, queryset: QuerySet):
        count_deleted = queryset.update(arrears_over_provider=0)
        self.message_user(
            request,
            f'Было очищено {count_deleted} задолженностей'
        )
