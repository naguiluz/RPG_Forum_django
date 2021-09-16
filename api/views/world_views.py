from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.world import World
from ..serializers import WorldSerializer

# Create your views here.
class Worlds(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = WorldSerializer
    def get(self, request):
        """Index request"""
        # Get all the worlds:
        # worlds = World.objects.all()
        # Filter the worlds by owner, so you can only see your owned worlds
        worlds = World.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = WorldSerializer(worlds, many=True).data
        return Response({ 'worlds': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['world']['owner'] = request.user.id
        # Serialize/create world
        world = WorldSerializer(data=request.data['world'])
        # If the world data is valid according to our serializer...
        if world.is_valid():
            # Save the created world & send a response
            world.save()
            return Response({ 'world': world.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(world.errors, status=status.HTTP_400_BAD_REQUEST)

class WorldDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the world to show
        world = get_object_or_404(World, pk=pk)
        # Only want to show owned worlds?
        if request.user != world.owner:
            raise PermissionDenied('Unauthorized, you do not own this world')

        # Run the data through the serializer so it's formatted
        data = WorldSerializer(world).data
        return Response({ 'world': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate world to delete
        world = get_object_or_404(World, pk=pk)
        # Check the world's owner against the user making this request
        if request.user != world.owner:
            raise PermissionDenied('Unauthorized, you do not own this world')
        # Only delete if the user owns the  world
        world.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate World
        # get_object_or_404 returns a object representation of our World
        world = get_object_or_404(World, pk=pk)
        # Check the world's owner against the user making this request
        if request.user != world.owner:
            raise PermissionDenied('Unauthorized, you do not own this world')

        # Ensure the owner field is set to the current user's ID
        request.data['world']['owner'] = request.user.id
        # Validate updates with serializer
        data = WorldSerializer(world, data=request.data['world'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
