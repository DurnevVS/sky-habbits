from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from .serializers import HabbitsSerializer
from .models import Habbit


class HabbitsViewSet(ModelViewSet):
    """
    В наборе данных только привычки пользователя, от которого пришел запрос
    """

    serializer_class = HabbitsSerializer

    def get_queryset(self):
        return Habbit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PublicHabbitsListAPIView(ListAPIView):
    """
    Все привычки с выборкой "is_public" = True
    """

    serializer_class = HabbitsSerializer
    permission_classes = ()
    queryset = Habbit.objects.filter(is_public=True)
