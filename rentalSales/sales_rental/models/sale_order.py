from odoo import models,fields,api,_


class saleOrder(models.Model):
    _inherit = 'sale.order'

    rental_return_date = fields.Datetime(string =  "Rental Return Date")
    rental_start_date = fields.Datetime(string =  "Rental Start Date")
    is_rental_order = fields.Boolean(string = "Is Rental Order")
    duration_days = fields.Integer(string = 'Duration Days', compute = "_compute_duration_days")

    rental_status = fields.Selection([
        ('draft', 'Draft'),
        ('returned', 'Returned'),
        ('cancelled', 'Cancelled'),
        ('reserved', 'Reserved'),
    ], copy=False, default='draft', string='Rental Status')


    def action_confirm(self):
        ovr = super(saleOrder, self).action_confirm()
        for rec in self:
            if rec.is_rental_order:
                today = fields.Datetime.now()
                if rec.rental_start_date <= today <= rec.rental_return_date:
                    rec.rental_status = 'reserved'
        return ovr

    def action_reserved(self):
        for rec in self:
            rec.rental_status = 'reserved'

    def action_turn_in(self):
        for rec in self:
            rec.rental_status = 'returned'

    @api.onchange('rental_return_date')
    def _onchange_rental_return_date(self):
        isPriorThanStartDate = self.rental_return_date >= self.rental_start_date
        if not isPriorThanStartDate:
            self.rental_return_date = False
            return  {"warning": {"title": _("Warning"), "message": _("Return date must higher than start date")}}

    @api.depends('rental_start_date', 'rental_return_date')
    def _compute_duration_days(self):
        for rec in self:
            if rec.rental_start_date and rec.rental_return_date:
                duration = rec.rental_return_date - rec.rental_start_date
                rec.duration_days = max(duration.days, 0)
            else:
                rec.duration_days = 0

    #RESET FORM RENTAL ORDER WHEN NON ACTIVATED
    @api.onchange('is_rental_order')
    def _onchange_rental_order(self):
        if not self.is_rental_order:
            self.rental_status = "draft"
            self.rental_return_date = ""
            self.rental_start_date = ""
