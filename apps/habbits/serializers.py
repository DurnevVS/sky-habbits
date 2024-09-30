from rest_framework import serializers
from .models import Habbit


def validate_reward_and_reward_habbit_choice(habbit: Habbit):
    if habbit.is_beneficial and bool(habbit.reward) == bool(habbit.reward_habbit):
        raise serializers.ValidationError(
            'У полезной привычки нужно указать только "reward" или "reward_habbit"'
        )

def non_beneficial_habbit_cant_have_reward(habbit: Habbit):
    if not habbit.is_beneficial and habbit.reward or habbit.reward_habbit:
        raise serializers.ValidationError(
            "У приятной привычки не может быть никакой награды"
        )

def reward_habbit_must_be_non_beneficial(habbit: Habbit):
    if habbit.reward_habbit and habbit.reward_habbit.is_beneficial:
        raise serializers.ValidationError(
            "Наградой не может быть полезная привычка"
        )

    
class HabbitsSerializer(serializers.ModelSerializer):
    action_time_seconds = serializers.IntegerField(min_value=0, max_value=120)
    period_days = serializers.IntegerField(min_value=1, max_value=7)

    class Meta:
        model = Habbit
        fields = "__all__"
        extra_kwargs = {"user": {"read_only": True}}

    def validate(self, attrs):
        habbit = Habbit(**attrs)
        validate_reward_and_reward_habbit_choice(habbit)
        non_beneficial_habbit_cant_have_reward(habbit)
        reward_habbit_must_be_non_beneficial(habbit)
        return attrs
