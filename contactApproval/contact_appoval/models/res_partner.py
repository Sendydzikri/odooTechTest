from odoo import _, models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError

class resPartner(models.Model):
    _inherit = 'res.partner'


    status = fields.Selection([
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('cancelled','Cancelled')
    ], copy=False,default = 'draft', string='Status')

    approver_id = fields.Many2one('res.users',readOnly = True, string = "Approver", default = lambda self: self.env.uid)

    def action_approve(self):
        self.ensure_one()
        if self.status == "approved":
            raise UserError(_("Data already approved"))
        else:
            self.status = "approved"

    def action_cancel(self):
        self.ensure_one()
        if self.status == "cancelled":
            raise UserError(_("Data Already Cancelled"))
        elif self.status == "approved":
            raise UserError(_("Data Cannot Be Cancelled"))
        else:
            self.status = "cancelled"

    def action_reset(self):
        self.ensure_one()
        if self.status == "draft":
            raise UserError(_("Data Cannot Be Reset"))
        else:
            self.status = "draft"