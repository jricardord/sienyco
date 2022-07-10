from django.db import models
from django.utils import timezone
from django.template.defaultfilters import truncatechars

# Create your models here.

class MetodosPago(models.Model):
    metodo_pago_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50)
    detalles = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metodos_pago'
        ordering=['nombre']
    
    def __str__(self):
        return self.nombre + '-> ' + self.detalles


class Pagos(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipo = models.CharField(max_length=20)
    es_beneficio = models.IntegerField()
    ocultar = models.IntegerField()
    tienda_id = models.IntegerField()
    factura_id = models.CharField(max_length=100, blank=True, null=True)
    no_referencia = models.CharField(max_length=100, blank=True, null=True)
    metodo_pago = models.ForeignKey('MetodosPago', models.DO_NOTHING, blank=True, null=True)
    transaccion_id = models.CharField(max_length=50, blank=True, null=True)
    capital = models.DecimalField(max_digits=25, decimal_places=4)
    monto = models.DecimalField(max_digits=25, decimal_places=4)
    detalles = models.TextField(blank=True, null=True)
    attachment = models.TextField(blank=True, null=True)
    nota = models.TextField(blank=True, null=True)
    total_pago = models.DecimalField(max_digits=25, decimal_places=4, blank=True, null=True)
    pos_saldo = models.DecimalField(max_digits=25, decimal_places=4, blank=True, null=True)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pagos'
    
    def __str__(self):
        return self.factura_id


class Cajas(models.Model):
    caja_id = models.IntegerField(primary_key=True)
    nombre_caja = models.CharField(max_length=100, verbose_name="Caja")
    codigo = models.CharField(max_length=55, blank=True, null=True)
    detalles = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cajas'

    def __str__(self):
        return self.nombre_caja


class Marcas(models.Model):
    marca_id = models.IntegerField(primary_key=True)
    nombre_marca = models.CharField(max_length=100, verbose_name='Marca')
    codigo = models.CharField(max_length=100)
    detalles = models.TextField(blank=True, null=True)
    imagen_marca = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marcas'
        ordering = ['nombre_marca']
    
    def __str__(self):
        return self.nombre_marca


class Categorias(models.Model):
    categoria_id = models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=60, verbose_name='Categoría')
    detalles = models.TextField(blank=True, null=True)
    imagen_categoria = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorias'
    
    def __str__(self):
        return self.nombre_categoria


class Clientes(models.Model):
    cliente_id = models.BigAutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=100, verbose_name='Cliente')
    email = models.CharField(max_length=100, blank=True, null=True)
    movil = models.CharField(max_length=14, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    nacio = models.DateField(blank=True, null=True)
    sexo = models.IntegerField()
    edad = models.IntegerField(blank=True, null=True)
    gtin = models.CharField(max_length=100, blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)
    tiene_tarjeta_regalo = models.IntegerField()
    password = models.CharField(max_length=100, blank=True, null=True)
    raw_password = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    estatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clientes'
        verbose_name_plural='Clientes'

    def __str__(self):
        return self.nombre_cliente

class Proveedores(models.Model):
    proveedor_id = models.IntegerField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=100)
    codigo = models.CharField(max_length=55, blank=True, null=True)
    movil = models.CharField(max_length=14, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    gtin = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=55, blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)
    detalles = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'proveedores'
    
    def __str__(self):
        return self.nombre_proveedor


class CategoriaGastos(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=60)
    category_slug = models.CharField(max_length=60)
    parent_id = models.IntegerField()
    detalles = models.TextField(blank=True, null=True)
    sell_return = models.IntegerField()
    sell_delete = models.IntegerField()
    loan_delete = models.IntegerField()
    loan_payment = models.IntegerField()
    giftcard_sell_delete = models.IntegerField()
    topup_delete = models.IntegerField()
    product_purchase = models.IntegerField()
    stock_transfer = models.IntegerField()
    due_paid = models.IntegerField()
    estatus = models.IntegerField()
    is_hide = models.IntegerField()
    sort_order = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categoria_gastos'


class Gastos(models.Model):
    id = models.IntegerField(primary_key=True)
    tienda_id = models.IntegerField()
    no_referencia = models.CharField(max_length=100, blank=True, null=True)
    id_categoria = models.ForeignKey(CategoriaGastos, models.DO_NOTHING, db_column='id_categoria')
    motivo = models.CharField(max_length=255)
    cantidad = models.DecimalField(max_digits=25, decimal_places=4)
    retornable = models.CharField(max_length=2)
    notas = models.TextField()
    attachment = models.CharField(max_length=100, blank=True, null=True)
    estatus = models.IntegerField()
    created_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gastos'
    
    def __str__(self):
        return self.motivo


class Productos(models.Model):
    p_id = models.IntegerField(primary_key=True)
    tipo_producto = models.CharField(max_length=8, verbose_name='Tipo producto')
    codigo = models.CharField(max_length=50, blank=True, null=True)
    hsn_code = models.CharField(max_length=100, blank=True, null=True)
    codigo_barra = models.CharField(max_length=50, blank=True, null=True, verbose_name='Código de barra')
    nombre_producto = models.CharField(max_length=100, verbose_name='Nombre producto')
    categoria = models.ForeignKey(Categorias, models.DO_NOTHING)
    id_unidad = models.IntegerField()
    p_image = models.CharField(max_length=250, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos'
        ordering=['nombre_producto']
    
    def __str__(self):
        return self.nombre_producto


class TasaImpuestoProductos(models.Model):
    impuesto_id = models.IntegerField(primary_key=True)
    nombre_impuesto = models.CharField(max_length=55)
    codigo = models.CharField(max_length=55, blank=True, null=True)
    tasa_impuesto = models.DecimalField(max_digits=25, decimal_places=4)
    estatus = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tasa_impuesto_productos'


class ProductosEnTienda(models.Model):
    id = models.IntegerField(primary_key=True)
    p = models.ForeignKey(Productos, models.DO_NOTHING)
    tienda_id = models.IntegerField()
    precio_compra = models.FloatField()
    precio_venta = models.FloatField()
    cantidad_en_inventario = models.DecimalField(max_digits=25, decimal_places=4)
    cantidad_alerta = models.DecimalField(max_digits=25, decimal_places=4)
    proveedor = models.ForeignKey('Proveedores', models.DO_NOTHING)
    marca = models.ForeignKey(Marcas, models.DO_NOTHING, blank=True, null=True)
    caja_id = models.IntegerField(blank=True, null=True)
    impuesto = models.ForeignKey('TasaImpuestoProductos', models.DO_NOTHING, blank=True, null=True)
    tax_method = models.CharField(max_length=55)
    preference = models.TextField(blank=True, null=True)
    e_date = models.DateField(blank=True, null=True)
    p_date = models.DateField()
    estatus = models.IntegerField()
    sort_order = models.IntegerField()

    @property
    def Alerta(self):
        return self.cantidad_en_inventario - self.cantidad_alerta

    class Meta:
        managed = False
        db_table = 'productos_en_tienda'
    
    def __str__(self):
        return self.p


class VentaPrecio(models.Model):
    precio_id = models.BigAutoField(primary_key=True)
    factura_id = models.CharField(max_length=100)
    tienda_id = models.IntegerField()
    subtotal = models.DecimalField(max_digits=25, decimal_places=4, blank=True, null=True)
    tipo_descuento = models.CharField(max_length=10)
    monto_descuento = models.DecimalField(max_digits=25, decimal_places=4, blank=True, null=True)
    monto_interes = models.DecimalField(max_digits=25, decimal_places=4)
    porcentaje_interes = models.IntegerField()
    impuesto_producto = models.DecimalField(max_digits=25, decimal_places=4)
    orden_impuesto = models.DecimalField(max_digits=25, decimal_places=4, blank=True, null=True)
    cgst = models.DecimalField(max_digits=25, decimal_places=4, blank=True, null=True)
    sgst = models.DecimalField(max_digits=25, decimal_places=4, blank=True, null=True)
    igst = models.DecimalField(max_digits=25, decimal_places=4, blank=True, null=True)
    total_precio_compra = models.DecimalField(max_digits=25, decimal_places=4)
    tipo_envio = models.CharField(max_length=10)
    monto_envio = models.DecimalField(max_digits=25, decimal_places=4, blank=True, null=True)
    otros_cobros = models.DecimalField(max_digits=25, decimal_places=4)
    monto_apagar = models.DecimalField(max_digits=25, decimal_places=4, blank=True, null=True)
    monto_pagado = models.DecimalField(max_digits=25, decimal_places=4)
    debe = models.DecimalField(max_digits=25, decimal_places=4)
    debe_pagado = models.DecimalField(max_digits=25, decimal_places=4)
    monto_regresado = models.DecimalField(max_digits=25, decimal_places=4)
    balance = models.DecimalField(max_digits=25, decimal_places=4, blank=True, null=True)
    beneficio = models.DecimalField(max_digits=25, decimal_places=4)
    debe_previo = models.DecimalField(max_digits=25, decimal_places=4)
    debe_pagado_previo = models.DecimalField(max_digits=25, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'venta_precio'


class VentaProd(models.Model):
    id = models.BigAutoField(primary_key=True)
    factura_id = models.CharField(max_length=100)
    categoria_id = models.IntegerField()
    marca_id = models.IntegerField(blank=True, null=True)
    proveedor_id = models.IntegerField()
    tienda_id = models.IntegerField()
    p = models.ForeignKey('Productos', models.DO_NOTHING)
    nombre_producto = models.CharField(max_length=100)
    precio_producto = models.DecimalField(max_digits=25, decimal_places=4, verbose_name='$ producto')
    descuento_producto = models.DecimalField(max_digits=25, decimal_places=4)
    impuesto_producto = models.DecimalField(max_digits=25, decimal_places=4)
    metodo_impuesto = models.CharField(max_length=9, blank=True, null=True)
    tasa_impuesto = models.IntegerField(blank=True, null=True)
    impuesto = models.CharField(max_length=55, blank=True, null=True)
    gst = models.CharField(max_length=20, blank=True, null=True)
    cgst = models.DecimalField(max_digits=25, decimal_places=4, blank=True, null=True)
    sgst = models.DecimalField(max_digits=25, decimal_places=4, blank=True, null=True)
    igst = models.DecimalField(max_digits=25, decimal_places=4, blank=True, null=True)
    cantidad_productos = models.DecimalField(max_digits=25, decimal_places=4)
    precio_compra_producto = models.DecimalField(max_digits=25, decimal_places=4, blank=True, null=True, verbose_name='$ compra')
    total_productos = models.DecimalField(max_digits=25, decimal_places=4, verbose_name='Tot Prods')
    factura_compra_id = models.CharField(max_length=100, blank=True, null=True)
    print_counter = models.IntegerField(blank=True, null=True)
    print_counter_time = models.DateTimeField(blank=True, null=True)
    printed_by = models.IntegerField(blank=True, null=True)
    cantidad_regresada = models.DecimalField(max_digits=25, decimal_places=4, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venta_prod'
        verbose_name_plural='Ventas productos'

    @property
    def Producto(self):
        return truncatechars(self.nombre_producto, 100)
    
    def __str__(self):
        return self.nombre_producto


class VentaInfo(models.Model):
    venta_id = models.BigAutoField(primary_key=True)
    factura_id = models.CharField(max_length=100)
    edit_counter = models.IntegerField()
    tipo = models.CharField(max_length=4)
    tienda_id = models.IntegerField()
    cliente_id = models.IntegerField()
    movil_cliente = models.CharField(max_length=20, blank=True, null=True)
    ref_factura_id = models.CharField(max_length=100, blank=True, null=True)
    ref_user_id = models.IntegerField()
    nota_factura = models.TextField(blank=True, null=True)
    total_prods = models.SmallIntegerField(blank=True, null=True)
    es_entregado = models.IntegerField()
    estatus = models.IntegerField()
    metodo_pago = models.ForeignKey('MetodosPago', models.DO_NOTHING, blank=True, null=True)
    estatus_pago = models.CharField(max_length=20, blank=True, null=True)
    estatus_verificado = models.IntegerField()
    creado_por = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    @property
    def Creado(self):
        return (timezone.now() - self.created_at).days

    class Meta:
        managed = False
        db_table = 'venta_info'
        verbose_name_plural='Información de ventas'