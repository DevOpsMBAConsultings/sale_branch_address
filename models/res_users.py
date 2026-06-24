from odoo import fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    x_branch_address_id = fields.Many2one(
        comodel_name='res.partner',
        string='Dirección de Sucursal',
        domain="[('type', 'in', ['other', 'delivery', 'invoice', 'contact'])]",
        help='Dirección de la sucursal que aparecerá en las cotizaciones '
             'cuando este usuario sea el vendedor.',
    )
