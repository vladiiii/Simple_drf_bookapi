from rest_framework import serializers
from book_api.models import Book
from django.forms import ValidationError


class BookSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = Book
        field = "__all__"

    def validate_title(self, value):
        if value == "Diet Coke":
            raise ValidationError("No Diet Coke Pls")
        return value

    def validate(self, data):
        if data["number_of_pages"] > 200 and data["quantity"] > 200:
            raise ValidationError("Too heavy for inventory")
        return data

    def get_description(self, data):
        return "The name of the book" + data.title + "and it's" + str(data.number_of_pages) + "long"
