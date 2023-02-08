from odoo import api, fields, models


# transient model, this model is only for logic because don't save anything in the database and are used it for
# pop up windows

class CancelAppointmentWizard(models.TransientModel):
    _name = "cancel.appointment.wizard"
    _description = "Cancel Appointment Wizard"

    appointment_id = fields.Many2one('hospital.appointment', string="Appointment")
    reason = fields.Text(string="Reason")

    def action_cancel(self):
        return
