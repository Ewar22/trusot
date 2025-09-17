from odoo import fields, models


# modelo que usaremos para poder crear una ctegorias
class PurchaseCategory(models.Model):
    _name = "purchase.category"
    _description = "Category For Purchase"
    name = fields.Char(string="name")
    description = fields.Text(string="description")
