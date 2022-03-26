from rest_framework import serializers
from .models import Order

from django.forms.models import model_to_dict

from rest_framework.utils import html, model_meta, representation

class OrderSerializer(serializers.ModelSerializer):

    # def _user(self, obj):
    #     request = self.context.get('request', None)
    #     if request:
    #         return model_to_dict(request.user)

    # owner = serializers.SerializerMethodField('_user')
    # owner = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='username'
    # )

    owner = serializers.StringRelatedField(many=False)
    id = serializers.IntegerField(read_only=True)

    class Meta:

        model = Order
        # fields = '__all__'
        fields = ['id', 'resquest_date', 'product', 'quantity', 'owner']
        read_only_fields = (('resquest_date', True))
        depth = 1

    def create(self, validated_data):

        ModelClass = self.Meta.model
        info = model_meta.get_field_info(ModelClass)
        
        for field_name, relation_info in info.relations.items():
            if relation_info.to_many and (field_name in validated_data):
                print(field_name, " - ", validated_data.pop(field_name))
                # many_to_many[field_name] = validated_data.pop(field_name)

        aux = super().create(validated_data)

        # set owner to current user (the one that made the request)
        aux.owner = self.context['request'].user
        aux.save()

        return aux

    # def save(self, **kwargs):
    #     aux = super().save(**kwargs)
        
    #     print("\n\nolha o owner", aux.owner)

    #     return aux