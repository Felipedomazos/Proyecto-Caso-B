from django.urls import URLPattern, path
from .views import Interfaz, Fundacion, Nosotros, Hortalizas, Aromaticas, MacetasGrandes, MacetasPequenas, FertilizantesInorganicos, FertilizantesOrganicos, Productos, agregar_producto, eliminar_producto, listar_productos, modificar_producto
from MiWeb import views

urlpatterns = [
    path('', Interfaz,name="Interfaz"),
    path('fundacion/', Fundacion,name="fundacion"),
    path('nosotros/', Nosotros,name="nosotros"),
    path('hortalizas/', Hortalizas,name="hortalizas"),
    path('aromaticas/', Aromaticas,name="aromaticas"),
    path('macetasgrandes/', MacetasGrandes,name="macetasgrandes"),
    path('macetaspequenas/', MacetasPequenas,name="macetaspequenas"),
    path('fertilizantesinorganicos/', FertilizantesInorganicos,name="fertilizantesinorganicos"),
    path('fertilizantesorganicos/', FertilizantesOrganicos,name="fertilizantesorganicos"),
    path('productos/', Productos,name="productos"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-productos/', listar_productos, name="listar_productos"),
    path('modificar-producto/<idProducto>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<idProducto>/', eliminar_producto, name="eliminar_producto"),
]