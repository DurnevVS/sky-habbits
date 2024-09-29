from rest_framework.response import Response
from rest_framework.views import APIView


class HabbitsListAPIView(APIView):
    def get(self, request):
        return Response({"message": "Habbits list"})
