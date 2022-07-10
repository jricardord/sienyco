from django.contrib import admin
from django.utils.html import format_html
from .models import *

# Register your models here.
admin.site.register(Clientes)
#admin.site.register(Cajas)
admin.site.register(Marcas)
admin.site.register(Proveedores)
admin.site.register(Gastos)
admin.site.register(MetodosPago)
admin.site.register(Productos)
admin.site.register(Pagos)

@admin.register(VentaProd)
class VentasAdmin(admin.ModelAdmin):
    list_display=('nombre_producto','total_productos','precio_producto','precio_compra_producto',)

@admin.register(ProductosEnTienda)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ('p', 'precio_compra', 'precio_venta','cantidad_en_inventario','cantidad_alerta','Alerta','link',)
    #list_filter=('p',)
    #search_fields=('p',)

    def link(self, obj):
        return format_html("<a href='admin/{}' >ir</a>", obj.id)
        #ejemplo de como hacer un link, no se usara de esta aplicacion
        #para usar imagenes usar un <img src={} width="100" height="100" />, obj.campo.url