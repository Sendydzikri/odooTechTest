from odoo import _, models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError

class productTemplate(models.Model):
    _inherit = 'product.template'

    is_rent= fields.Boolean(string = "Is Rental")
    count_rent = fields.Integer(string = 'Count Rent', compute = '_count_reserved')

    @api.depends('is_rent')
    def _count_reserved(self):
        for rec in self:
            if rec.is_rent :
                rec.count_rent = self.env['product.template'].search_count([('is_rent', '=', True)])

    def action_sale_order(self):
        return {
            'views': [
                (self.env.ref('sale.view_order_tree').id, 'tree'),
                (self.env.ref('sale.view_order_form').id, 'form'),
            ],
            'type': 'ir.actions.act_window',
            'name': 'Sale Order',
            'view_mode': 'tree,form',
            'res_model': 'sale.order',
        }


