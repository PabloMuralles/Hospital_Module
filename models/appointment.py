from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = "mail.thread", 'mail.activity.mixin'
    _description = "Hospital Appointment"
    _rec_name = "name"  # this if to show the name in the appointment/record because if we don't use this the
    # module put appointment/hospital.appointment,1 for example
    # this rec name will be display when we use the active_id in the same way the rec_name will be display in the
    # many2one fields

    name = fields.Char(string="Name", required=True, readonly=True, default='New')
    patient_id = fields.Many2one(comodel_name="hospital.patient", string="Patient")  # this field it's to connect
    # other module with this so when we search a patient in the appointment will appear all only to select one
    # the other thing it's that comodel_name it's to specify the model that make the references
    gender = fields.Selection(related="patient_id.gender")  # this is for
    # bring the gender of the patient based on the filed patient_id, so we can access to all the fild of the patient
    # it the "." by default this field will be read only if we want to make changes we have to add readonly=False
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now())
    booking_date = fields.Date(string="Booking Date", default=fields.Date.today())  # in de video used .context_today
    # but this function gave me a problem, so I use today
    ref = fields.Char(string='Reference', help="References of the patient record")  # if I use readonly to this will
    # not be stored on the database and not will show in the form view when we put save
    prescription = fields.Html(string="Prescription")  # this is how to define an HTML field, this field will be like
    # a textbox to put text this field it's for the priority start for an appointment this will appear in the form view
    #  to put the level of the priority of this appointment
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority")
    # this field will help us to set a status of the appointments like the status of the orders in other modules
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')], default='draft', string="Status", required=True, tracking=True)
    doctor_id = fields.Many2one(comodel_name='res.users', string='Doctor')
    # one2many field always need to finish in ids because have multiple records
    # in this field I can't put comodel_name only this way
    pharmacy_line_ids = fields.One2many('appointment.pharmacy.lines', 'appointment_id', string='Pharmacy Line')
    hide_sales_price = fields.Boolean(string="Hide Sales Price")

    @api.model
    def create(self, vals_list):
        vals_list['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        return super(HospitalAppointment, self).create(vals_list)

    # this will execute when we delete some record, this is necessary when we don't want to delete some record
    # because are in some state that if we delete affect the logic business
    def unlink(self):
        if self.state == "done":
            raise ValidationError(_("You can not delete appointment with Done Status"))
        return super(HospitalAppointment, self).unlink()

    # define an onchange function, this will help when we select the patient automatically set the references that have
    # the patient
    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

    # this function it's for the button type object we need a function with the same name of the button
    def action_test(self):
        print("Button Clicked!")
        # show a rainbow with a message
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Click Successfully',
                'type': 'rainbow_man',
            }
        }

    def action_in_consultation(self):
        for record in self:
            record.state = 'in_consultation'

    def action_done(self):
        for record in self:
            record.state = 'done'

    def action_cancel(self):
        # this is an odoo method to get an action
        # for me was not error with .read()[0]
        action = self.env.ref('om_hospital.action_cancel_appointment').read()[0]
        return action

    def action_draft(self):
        for record in self:
            record.state = 'draft'



