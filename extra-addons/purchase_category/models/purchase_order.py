from odoo import models, fields

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    purchase_category_id = fields.Many2one(
        comodel_name="purchase.category",
        string="Categoría de Compra"
    )
