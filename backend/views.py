from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .models import DisabledPerson
from .serializers import DisabledPersonSerializer

# Common disability types for new registrations
DISABILITY_TYPES = [
    'Visual Impairment',
    'Hearing Impairment',
    'Physical Disability',
    'Cognitive Disability',
    'Multiple Disabilities',
    'Other'
]

class DisabledPersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows disabled persons to be viewed or edited.
    """
    queryset = DisabledPerson.objects.all()
    serializer_class = DisabledPersonSerializer
    
    @action(detail=False, methods=['get'])
    def disability_types(self, request):
        """API endpoint to get all disability types for filtering"""
        # Combine predefined types with database types
        disability_types = DISABILITY_TYPES.copy()
        
        # Add any custom types from database
        db_types = DisabledPerson.objects.values_list('disability_type', flat=True).distinct()
        for db_type in db_types:
            if db_type and db_type not in disability_types:
                disability_types.append(db_type)
        
        return Response({'types': disability_types})

# Keep the original template view for the map
def map_view(request):
    # Get disability types from both the predefined list and existing records
    disability_types = DISABILITY_TYPES.copy()
    
    # Add any custom types from the database that aren't in our predefined list
    db_types = DisabledPerson.objects.values_list('disability_type', flat=True).distinct()
    for db_type in db_types:
        if db_type and db_type not in disability_types:
            disability_types.append(db_type)
    
    return render(request, 'map.html', {'disability_types': disability_types})

# Legacy API endpoints that can be used alongside REST framework
# These can be deprecated once the frontend is updated to use the new API

@api_view(['POST'])
def add_person(request):
    """Legacy endpoint for adding a person"""
    serializer = DisabledPersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 'success'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_people(request):
    """Legacy endpoint for getting all people"""
    people = DisabledPerson.objects.all()
    serializer = DisabledPersonSerializer(people, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_disability_types(request):
    """Legacy endpoint for getting disability types"""
    # Combine predefined types with database types
    disability_types = DISABILITY_TYPES.copy()
    
    # Add any custom types from database
    db_types = DisabledPerson.objects.values_list('disability_type', flat=True).distinct()
    for db_type in db_types:
        if db_type and db_type not in disability_types:
            disability_types.append(db_type)
    
    return Response({'types': disability_types})
