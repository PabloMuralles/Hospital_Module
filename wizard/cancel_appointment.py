import datetime

from odoo import api, fields, models


# transient model, this model is only for logic because don't save anything in the database and are used it for
# pop up windows

class CancelAppointmentWizard(models.TransientModel):
    _name = "cancel.appointment.wizard"
    _description = "Cancel Appointment Wizard"

    # when we inherit the get function we have to put next to the definition of the class
    @api.model
    def default_get(self, fields):
        res = super(CancelAppointmentWizard, self).default_get(fields)
        res['date_cancel'] = datetime.date.today()
        # how to pass data between views
        print("---------------------", self.env.context)
        print("---------------------", self.env.context.get('active_id'))
        if self.env.context.get("active_id"):
            # with this I obtain the value of the function get_name and in the video only the ref
            # so it´s important to search with and how to solve to put only the ref
            test1 = self.env.context.get('active_id')
            res['appointment_id'] = test1
            # res['appointment_id'] = self.env['hospital.appointment'].browse(self.env.context.get('name'))
        return res

    appointment_id = fields.Many2one(comodel_name='hospital.appointment', string="Appointment")
    reason = fields.Text(string="Reason")
    date_cancel = fields.Date(string="Cancel Date")

    def action_cancel(self):
        return
