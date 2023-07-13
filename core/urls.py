from django.urls import path

from core.views.contacts import ContactsListView, ContactsRetrieveView, \
    ContactsUpdateView, ContactsCreateView, ContactsDestroyView
from core.views.factory import FactoryListView, FactoryRetrieveView, \
    FactoryUpdateView, FactoryCreateView, FactoryDestroyView
from core.views.privatebusinessman import PrivateBusinessmanListView, \
    PrivateBusinessmanRetrieveView, PrivateBusinessmanUpdateView, \
    PrivateBusinessmanCreateView, PrivateBusinessmanDestroyView
from core.views.products import ProductsListView, ProductsRetrieveView, \
    ProductsUpdateView, ProductsCreateView, ProductsDestroyView
from core.views.retail import RetailListView, RetailRetrieveView, \
    RetailUpdateView, RetailCreateView, RetailDestroyView
from core.views.storage import StorageListView, StorageRetrieveView, \
    StorageUpdateView, StorageCreateView, StorageDestroyView

urlpatterns = [
    # Storage View
    path('storage/', StorageListView.as_view(), name='storage_list'),
    path('storage/<int:pk>/', StorageRetrieveView.as_view(), name='storage_detail'),
    path('storage/update/<int:pk>/', StorageUpdateView.as_view(), name='storage_update'),
    path('storage/create/', StorageCreateView.as_view(), name='storage_create'),
    path('storage/delete/<int:pk>/', StorageDestroyView.as_view(), name='storage_destroy'),
    # Contacts View
    path('contacts/', ContactsListView.as_view(), name='contacts_list'),
    path('contacts/<int:pk>/', ContactsRetrieveView.as_view(), name='contacts_detail'),
    path('contacts/update/<int:pk>/', ContactsUpdateView.as_view(), name='contacts_update'),
    path('contacts/create/', ContactsCreateView.as_view(), name='contacts_create'),
    path('contacts/delete/<int:pk>/', ContactsDestroyView.as_view(), name='contacts_destroy'),
    # Products View
    path('products/', ProductsListView.as_view(), name='products_list'),
    path('products/<int:pk>/', ProductsRetrieveView.as_view(), name='products_detail'),
    path('products/update/<int:pk>/', ProductsUpdateView.as_view(), name='products_update'),
    path('products/create/', ProductsCreateView.as_view(), name='products_create'),
    path('products/delete/<int:pk>/', ProductsDestroyView.as_view(), name='products_destroy'),
    # Factory View
    path('factory/', FactoryListView.as_view(), name='factory_list'),
    path('factory/<int:pk>/', FactoryRetrieveView.as_view(), name='factory_detail'),
    path('factory/update/<int:pk>/', FactoryUpdateView.as_view(), name='factory_update'),
    path('factory/create/', FactoryCreateView.as_view(), name='factory_create'),
    path('factory/delete/<int:pk>/', FactoryDestroyView.as_view(), name='factory_destroy'),
    # Retail View
    path('retail/', RetailListView.as_view(), name='retail_list'),
    path('retail/<int:pk>/', RetailRetrieveView.as_view(), name='retail_detail'),
    path('retail/update/<int:pk>/', RetailUpdateView.as_view(), name='retail_update'),
    path('retail/create/', RetailCreateView.as_view(), name='retail_create'),
    path('retail/delete/<int:pk>/', RetailDestroyView.as_view(), name='retail_destroy'),
    # Private Businessman View
    path('pb/', PrivateBusinessmanListView.as_view(), name='private_businessman_list'),
    path('pb/<int:pk>/', PrivateBusinessmanRetrieveView.as_view(), name='private_businessman_detail'),
    path('pb/update/<int:pk>/', PrivateBusinessmanUpdateView.as_view(), name='private_businessman_update'),
    path('pb/create/', PrivateBusinessmanCreateView.as_view(), name='private_businessman_create'),
    path('pb/delete/<int:pk>/', PrivateBusinessmanDestroyView.as_view(), name='private_businessman_destroy'),
]
