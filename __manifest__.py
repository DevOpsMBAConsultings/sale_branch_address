{
    'name': 'Sale Branch Address',
    'version': '18.0.1.0.0',
    'summary': 'Dirección de sucursal por vendedor en cotizaciones',
    'description': """
        Permite asignar una dirección de sucursal a cada vendedor.
        Al crear una cotización, la dirección de la sucursal del vendedor
        se imprime en el reporte en lugar de la dirección principal de la compañía.
    """,
    'author': 'MBA Consultings',
    'website': 'https://mbaconsultings.com',
    'category': 'Sales',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_users_views.xml',
        'views/sale_order_views.xml',
        'report/sale_report_templates.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
