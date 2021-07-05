from odoo import fields, api, models

class ProductAttributeValue(models.Model):
    _inherit = 'product.attribute.value'

    product_surface_color_variant = fields.Binary(string='Surface Color', help="here you can set product surface color images", required=True)


class ProductTemplateAttributeValue(models.Model):
    _inherit = 'product.template.attribute.value'

    product_surface_color_variant = fields.Binary(related='product_attribute_value_id.product_surface_color_variant')
class ProductAttribute(models.Model):
    _inherit = 'product.attribute'

    display_type = fields.Selection(selection_add=[('surfacecolor', 'Surface Color')], ondelete={'surfacecolor':'cascade'})
