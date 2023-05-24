from django.urls import path
from new_war_time import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.users, name='users'),
    path('military_personnel/', views.military_personnel, name='military_personnel'),
    path('game/', views.game, name='game'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)