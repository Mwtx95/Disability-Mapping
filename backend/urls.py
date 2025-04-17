from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'disabled-persons', views.DisabledPersonViewSet)

# The API URLs are now determined automatically by the router
urlpatterns = [
    # Keep the original template view for the map
    path('', views.map_view, name='map_view'),
    
    # Include the REST framework URLs
    path('api/', include(router.urls)),
    
    # Legacy API endpoints (can be deprecated once frontend is updated)
    path('add/', views.add_person, name='add_person'),
    path('people/', views.get_people, name='get_people'),
    path('disability-types/', views.get_disability_types, name='get_disability_types'),
]
