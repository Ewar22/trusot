from odoo import fields, models

# este modelo nos permite asignar una categoria al usario
class ResUser(models.Model):
    # hereda del modelo de usuarios existente
    _inherit = 'res.users'

    purchase_category_ids = fields.Many2many(
        comodel_name="purchase.category",           # modelo relacionado: purchase.category
        relation="res_users_purchase_category_rel", # nombre de la tabla intermedia en la base de datos
        column1="user_id",                          # columna que apunta al usuario
        column2="category_id",                      # columna que apunta a la categoría
        string="Categorías de Compra"               # nombre visible en la vista de usuarios
    )
