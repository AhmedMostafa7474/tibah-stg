from rest_framework import serializers

from reviews.models import Review,ContactUS


class ReviewSerializer(serializers.ModelSerializer):
      class Meta:
            model = Review
            fields = '__all__'


class ContactUsSerializer(serializers.ModelSerializer):
      class Meta:
            model = ContactUS
            fields = '__all__'