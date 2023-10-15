from rest_framework import serializers
from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор привычки"""
    class Meta:
        model = Habit
        fields = '__all__'


class HabitCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания привычки"""
    class Meta:
        model = Habit
        fields = '__all__'

    def validate(self, data):

        if data.get('linked') and data.get('reward'):
            raise serializers.ValidationError({
                'message_error': "Нельзя одновременно выбрать 'Связанную привычку' "
                                 "и 'Вознаграждение'."
            })

        elif data.get('execution_time').minute >= 2:
            raise serializers.ValidationError({
                'message_error': "Время выполнения должно быть не больше 120 секунд"
            })

        elif data.get('period') > 7:
            raise serializers.ValidationError({
                'message_error': "Нельзя выполнять привычку реже, чем 1 раз в 7 дней."
            })

        elif data.get('linked'):
            if not data.get('linked').is_pleasant:
                raise serializers.ValidationError({
                    'message_error': "В связанные привычки могут попадать только привычки "
                                     "с признаком приятной привычки."
                })

        elif data.get('is_pleasant'):
            if data.get('linked') or data.get('reward'):
                raise serializers.ValidationError({
                    'message_error': "Нельзя выбрать 'Связанную привычку' и 'Вознаграждение' для приятной привычки."
                })
        return data
