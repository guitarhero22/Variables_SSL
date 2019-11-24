from django.urls import path


from . import views

urlpatterns = [
    path("create", views.create, name="create"),
    path("deactivate", views.deactivate, name="deactivate"),
    path('', views.home, name="home"),
    path("respond", views.respond, name='respond'),
    path('answer', views.answer, name='answer'),
    path('build', views.build, name='build'),
    path('add_q/<form_code>/<q_type>/', views.add_q, name='add_q')
]
