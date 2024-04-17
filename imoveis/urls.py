from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from imoveis.views import sobre, cadastrar_imovel, excluir_imovel, login_view, logout_view, lista_imoveis

urlpatterns = [
   path('sobre/', sobre, name='sobre'),
   path('cadastrar_imovel/', cadastrar_imovel, name='cadastrar_imovel'),
   path('lista_imoveis/', lista_imoveis, name='lista_imoveis'),
   path('excluir_imovel/<int:imovel_id>/', excluir_imovel, name='excluir_imovel'),
   path('', login_view, name='login'),
   path('logout/', logout_view, name='logout'),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

