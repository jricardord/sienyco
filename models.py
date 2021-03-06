# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class VentaPrecio(models.Model):
    precio_id = models.IntegerField(primary_key=True)
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
    id = models.IntegerField(primary_key=True)
    factura_id = models.CharField(max_length=100)
    categoria_id = models.IntegerField()
    marca_id = models.IntegerField(blank=True, null=True)
    proveedor_id = models.IntegerField()
    tienda_id = models.IntegerField()
    p = models.ForeignKey('Productos', models.DO_NOTHING)
    nombre_producto = models.CharField(max_length=100)
    precio_producto = models.DecimalField(max_digits=25, decimal_places=4)
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
    precio_compra_producto = models.DecimalField(max_digits=25, decimal_places=4, blank=True, null=True)
    total_productos = models.DecimalField(max_digits=25, decimal_places=4)
    factura_compra_id = models.CharField(max_length=100, blank=True, null=True)
    print_counter = models.IntegerField(blank=True, null=True)
    print_counter_time = models.DateTimeField(blank=True, null=True)
    printed_by = models.IntegerField(blank=True, null=True)
    cantidad_regresada = models.DecimalField(max_digits=25, decimal_places=4, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venta_prod'


class VentaInfo(models.Model):
    venta_id = models.IntegerField(primary_key=True)
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

    class Meta:
        managed = False
        db_table = 'venta_info'


