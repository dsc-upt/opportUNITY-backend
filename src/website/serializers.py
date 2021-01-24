from typing import List, Dict

from django.db.models import QuerySet
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from website.models import Faq, Partner, MenuItem, Article, Newsletter, WantToHelp, Contact, Setting


class NewsletterSerializer(ModelSerializer):
    class Meta:
        model = Newsletter
        fields = '__all__'


class FaqSerializer(ModelSerializer):
    class Meta:
        fields = 'id', 'question', 'answer'
        model = Faq


class PartnerSerializer(ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'


class MenuItemSerializer(ModelSerializer):
    children = SerializerMethodField('get_children')

    @staticmethod
    def get_children(menu_item: MenuItem):
        qs: QuerySet[MenuItem] = MenuItem.objects.filter(parent=menu_item)
        serializer = MenuItemSerializer(instance=qs, many=True, read_only=True)
        return serializer.data

    class Meta:
        model = MenuItem
        exclude = ('parent', 'id')


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class WantToHelpSerializer(ModelSerializer):
    class Meta:
        model = WantToHelp
        fields = '__all__'


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        exclude = 'created', 'updated', 'id'


class SettingSerializer(ModelSerializer):
    class Meta:
        model = Setting
        fields = '__all__'
