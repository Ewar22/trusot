
{
    'name': 'Purchase Order',
    'description': 'categoría de compra', 
    'author': 'Eduard Montano',
    'category': 'Purchase',
    'version': '16.0.0.1',
    'depends': ['base','purchase'],
    'data': [
        'security/group.xml',
        'security/ir.model.access.csv',
        'security/purchase_category_security.xml',
        'views/purchase_category_view.xml',
        'views/res_users_views.xml',
        'views/purchase_order_views.xml' 
        
    ],
    'license': 'AGPL-3',
    'application': True,
    'installable': True,
    'auto_install': False,
}