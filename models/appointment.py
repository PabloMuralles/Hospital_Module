from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = "mail.thread", 'mail.activity.mixin'
    _description = "Hospital Appointment"

    patient_id = fields.Many2one(comodel_name="hospital.patient", string="Patient")  # this field it's to connect
    # other module with this so when we search a patient in the appointment will appear all only to select one
    # the other thing it's that comodel_name it's to specify the model that make the references
    gender = fields.Selection(related="patient_id.gender")  # this is for
    # bring the gender of the patient based on the filed patient_id, so we can access to all the fild of the patient
    # it the "." by default this field will be read only if we want to make changes we have to add readonly=Falsejj
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now())
    booking_date = fields.Date(string="Booking Date",
                               default=fields.Date.today())  # in de video used .context_today but
    # this function gave me a problem so I use today
