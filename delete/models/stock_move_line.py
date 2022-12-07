from odoo import fields, models


class ProductCategory(models.Model):
    _inherit = 'product.category'

    def delete(self):
        for rec in self:
            rec.unlink()
