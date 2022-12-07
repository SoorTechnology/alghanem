from odoo import fields, models


class ProductCategory(models.Model):
    _inherit = 'product.template'

    def delete(self):
        for rec in self:
            rec.categ_id = 102
