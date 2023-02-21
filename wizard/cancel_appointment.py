import datetime

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


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
        if self.env.context.get("active_id"):
            res['appointment_id'] = self.env.context.get('active_id')
        return res

    # the domain help us to filter the record based in some condition, to have more than one we have to put like this
    # domain=[(''), ('')] to put false in the condition you have tu put False and if we don't put anything
    # will be an and operation and if we want a or operation will be like this domain=['|', (''), ('')]
    appointment_id = fields.Many2one(comodel_name='hospital.appointment', string="Appointment"
                                     , domain=[('state', '=', 'draft')])
    reason = fields.Text(string="Reason")
    date_cancel = fields.Date(string="Cancel Date")

    def action_cancel(self):
        if self.appointment_id.booking_date == fields.Date.today():
            raise ValidationError(_("Sorry, cancellation is not Allow on the same day of booking"))
        return
