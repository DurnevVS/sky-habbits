from rest_framework import serializers


class TelegramWidgetSerializer(serializers.Serializer):
    size = serializers.ChoiceField(
        choices=("small", "medium", "large"), default="large"
    )
    radius = serializers.IntegerField(min_value=0, max_value=20, default=20)
