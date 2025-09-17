from odoo import models, fields

# Extensión del modelo purchase.order para asociar cada orden de compra a una categoría
#modelo en cual podemos asiciar una orden a una categorias
class PurchaseOrder(models.Model):
    # heredamos el modelo para poder asigar una catogoria
    _inherit = "purchase.order"  
    

    purchase_category_id = fields.Many2one(
        comodel_name="purchase.category",  
        string="Categoría de Compra"       
    )
