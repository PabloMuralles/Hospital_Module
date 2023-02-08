from odoo import models, fields, api


class SalesOrder(models.Model):
    _inherit = 'sale.order'

    # this fild will be added to the model sale.order
    confirm_user_id = fields.Many2one('res.users', string='Confirmed User')

    # we have tu put de definition of the function the same of the other module with all the parameters
    # with this we can inherit a function
    def action_confirm(self):
        # firsts will execute all the code here and then will go to execute the code to the other function
        # if we want to change the order only have to change the order of the code lines
        print("Success--------------------------------------")
        super(SalesOrder, self).action_confirm()
        # how to set the confirmation user with code
        self.confirm_user_id = self.env.user



