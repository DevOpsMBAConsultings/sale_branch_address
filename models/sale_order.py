from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    x_branch_address_id = fields.Many2one(
        comodel_name='res.partner',
        string='Dirección de Sucursal',
        help='Se completa automáticamente según la sucursal del vendedor. '
             'Se imprimirá en la cotización en lugar de la dirección principal.',
    )

    @api.onchange('user_id')
    def _onchange_user_id_branch_address(self):
        """Al cambiar el vendedor, actualiza la dirección de sucursal."""
        if self.user_id and self.user_id.x_branch_address_id:
            self.x_branch_address_id = self.user_id.x_branch_address_id
        else:
            self.x_branch_address_id = False

    @api.model_create_multi
    def create(self, vals_list):
        """Al crear la cotización, asigna la sucursal del vendedor si no viene ya."""
        for vals in vals_list:
            if not vals.get('x_branch_address_id'):
                user_id = vals.get('user_id') or self.env.user.id
                user = self.env['res.users'].browse(user_id)
                if user.x_branch_address_id:
                    vals['x_branch_address_id'] = user.x_branch_address_id.id
        return super().create(vals_list)
