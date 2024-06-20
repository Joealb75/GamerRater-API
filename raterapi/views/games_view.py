from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import serializers
from raterapi.models import Game
from .gameCategories_view import CategorySerializer

class GameSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()
    category = CategorySerializer(many=True)  

    def get_is_owner(self, obj):
        return self.context["request"].user == obj.user
    
    class Meta:
        model = Game
        fields = [
            "id",
            "title",
            "description",
            "designer",
            "yearReleased", 
            "numberOfPlayers", 
            "timeToPlay", 
            "ageRating", 
            "averageRating", 
            "category",
            "is_owner",
        ]

class GameViewSet(viewsets.ViewSet):

    def list(self, request):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True, context={"request": request})
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game, many=True, context={"request": request})
            return Response(serializer.data)
        
        except Game.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def create(self, request):
        title = request.data.get("title")

        game = Game.objects.create(
            user = request.user,
            title = title,

        )