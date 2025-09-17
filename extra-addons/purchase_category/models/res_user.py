from odoo import fields, models

class ResUser(models.Model):
    _inherit = 'res.users'

    purchase_category_ids = fields.Many2many(
        comodel_name="purchase.category",
        relation="res_users_purchase_category_rel",
        column1="user_id",
        column2="category_id",
        string="Categorías de Compra"
    )