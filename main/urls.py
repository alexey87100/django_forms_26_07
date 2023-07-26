from django.urls import path

from .views import index, profiles_by_skill
from .views import add_profile, add_profile_model_form
from .views import ProfileAddView, ProfileCreateView, ProfileUpdateView

app_name = 'main'

urlpatterns = [
    path('', index, name='main_page'),
    path('skill/<slug:slug>/', profiles_by_skill, name='skill_page'),
    # path('add_profile/', add_profile, name="add_profile"),
    path('add_profile/', add_profile_model_form, name="add_profile"),
    # path('add_profile/', ProfileCreateView.as_view(), name="add_profile"),
    path('edit_profile/<int:profile_id>/', ProfileUpdateView.as_view(), name='edit_profile')
]
