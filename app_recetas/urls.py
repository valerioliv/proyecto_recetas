from django.urls import path
from app_recetas import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio , name='inicio'),
    path('recetas/', views.recetas , name='recetas'),
    path('nueva_receta/', views.nueva_receta , name='nueva_receta'),
    path('busqueda_receta/', views.busqueda_receta , name='busqueda_receta'),
    path('buscar_receta/', views.buscar_receta , name='buscar_receta'),
    path('modificar_receta/<str:nombre>', views.modificar_receta , name='modificar_receta'),
    path('modificar_receta/', views.modificar_receta , name='modificar_receta'),
    path('ingredientes/', views.ingredientes , name= 'ingredientes'),
    path('nuevo_ingrediente/', views.nuevo_ingrediente , name='nuevo_ingrediente'),
    path('borrar_ingrediente/<int:id_in>', views.borrar_ingrediente , name='borrar_ingrediente'),
    path('modificar_ingrediente/<str:nombre>', views.modificar_ingrediente , name='modificar_ingrediente'),
    path('modificar_ingrediente/', views.modificar_ingrediente , name='modificar_ingrediente'), 
    path('contacto/', views.contacto , name='contacto'),
    path('login/', views.login_request , name= 'login'),
    path('register/', views.register , name= 'register'),
    path('logout/', LogoutView.as_view(template_name="logout.html") , name = 'logout'),
    path('editar/', views.editar_perfil , name = 'editar'),
    path('about/', views.about , name='about'),
]