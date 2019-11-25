from django.urls import path


from . import views

urlpatterns = [
    path("create", views.create, name="create"),
    path("deactivate", views.deactivate, name="deactivate"),
    path('', views.home, name="home"),
    path("respond", views.respond, name='respond'),
    path('answer/<form_name>/', views.answer, name='answer'),
    path('/answer/<form_name>/', views.answer, name='answer'),
    path('build/<form_name>', views.build, name='build'),
    path('add_q/<form_name>/<q_type>/', views.add_q, name='add_q'),
    path('/add_q/<form_name>/<q_type>/', views.add_q, name='add_q'),
    path('/add_opt/<q_id>/<opt_type>/', views.add_opt, name='add_opt'),
    path('add_opt/<q_id>/<opt_type>/', views.add_opt, name='add_opt'),
    path('see/<form_name>', views.see, name='see'),

]
