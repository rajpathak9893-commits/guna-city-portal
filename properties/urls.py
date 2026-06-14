from django.urls import path

from .views import (
    property_list,
    add_property,
    property_detail,
    delete_property
)

urlpatterns = [

    path(
        '',
        property_list,
        name='property_list'
    ),

    path(
        'add/',
        add_property,
        name='add_property'
    ),

    path(
        '<int:id>/',
        property_detail,
        name='property_detail'
    ),

    path(
        'delete/<int:id>/',
        delete_property,
        name='delete_property'
    ),

]