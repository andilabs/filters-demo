from django.db import models


class Colour(models.Model):
    colour = models.CharField(max_length=100)
    colour_code = models.CharField(max_length=100,null=True,blank=True)

    def __unicode__(self):
        return u'%s' %self.colour


class Material(models.Model):
    material = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' %self.material


class Size(models.Model):
    value = models.CharField(unique=True, max_length=4)

    def __unicode__(self):
        return self.value


class Product(models.Model):
    product_name = models.CharField(max_length=500)
    product_color = models.ForeignKey(Colour,related_name='productcolor')
    product_material = models.ForeignKey(Material)

    def __str__(self):
        return "{} ({}, {})".format(self.product_name, self.product_color, self.product_material)


class Stock(models.Model):
    product = models.ForeignKey('Product', related_name='details')
    size = models.ForeignKey('Size')
    stock = models.IntegerField(default=1)
    items_sold = models.IntegerField(default=0)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return "{product_name}({material}, {color}) @size: {size}, available {available} out of: {stock}".format(
            product_name=self.size.value,
            material=self.product.product_material.material,
            color=self.product.product_color.colour,
            size=self.size.value,
            available=self.stock-self.items_sold,
            stock=self.stock
        )


