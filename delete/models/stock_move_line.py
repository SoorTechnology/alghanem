from odoo import fields, models


class ProductCategory(models.Model):
    _inherit = 'product.template'

    def action(self):
        for rec in self:
            rec.categ_id = 102
