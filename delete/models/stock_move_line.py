from odoo import fields, models


class ProductCategory(models.Model):
    _inherit = 'product.category'

    def action(self):
        for rec in self:
            rec.unlink()
