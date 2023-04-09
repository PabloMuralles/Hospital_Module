from datetime import date
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = "hospital.patient"  # odoo will create a table with this name example hospital_patient
    _inherit = "mail.thread", 'mail.activity.mixin'  # this inherits it's to can use the chatter in the form view
    # then we have to add the dependencies in the manifest in views, we have to se in what module it's define the
    # class that we are inherit to put this module in the dependence
    _description = "HospitalPatient"
    # _rec_name = "name" in this case we don't need a rec name because the model have a field name so odoo
    # automatically use this

    # how to create the field in the database of this table patient
    name = fields.Char(string='Name', tracking=True)  # the tracking it's to show the changes of the filed in the
    # chatter section, we need to have activated the chatter
    date_of_birth = fields.Date(string="Date of Birth")
    ref = fields.Char(string='Reference')
    age = fields.Integer(string='Age', compute="_compute_age", tracking=True)  # if we want to store the this
    # computed fild store=True
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', tracking=True,
                              default='female')
    active = fields.Boolean(string="Active", default=True)  # this field is to put the option archive or unarchived
    # in odoo view
    image = fields.Image(string="Image")
    # many2many field we have to end with ids because we can save multiple values in this field
    # for this field don't save anything in this model this will create a separate table in de database
    # in this case create a table named hospital_patient_patient_tag_rel
    tag_ids = fields.Many2many(comodel_name="patient.tag", string="Tags")
    # stored computed field
    appointment_count = fields.Integer(string="Appointment Count", compute='_compute_appointment_count', store=True)
    # we don't have field in this model to have a depends on recompute the field appointment_count, so
    # to create a new field one2many with patient_id because one patient can have many appointments
    # that means that when we create a new appointment this field will change and then tigger to compute function
    appointment_ids = fields.One2many('hospital.appointment', 'patient_id', string="Appointments")
    parent = fields.Char(string="Parent")
    marital_status = fields.Selection([('married', 'Married'), ('single', 'Single')], string="Marital Status",
                                      tracking=True)
    partner_name = fields.Char(string="Partner Name")

    # to stored computed field is important to choose the correct field to depends for recompute de field
    @api.depends('appointment_ids')
    def _compute_appointment_count(self):
        for record in self:
            # this if for search in other module using the orm_method
            record.appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', record.id)])

    # how to define a python constrain, to name de function use _check_name of the field
    # if we have multiple field we can do this @api.constrains('date_of_birth','gender')
    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for record in self:
            if record.date_of_birth and record.date_of_birth > fields.Date.today():
                raise ValidationError(_("The entered date is not acceptable!"))

    # how to define a function in a model
    # this function it's for a computed fild, a computed fild will not store in the database
    # this field will be calculated all the times so this means that will take server resources
    @api.depends('date_of_birth')  # this decorator it's to compute the fild when we change or set the date of birth
    # in the form view because if we don't put this the function will compute when we save the patient, we can have
    # multiple depends on fields, and we have to follow this syntax @api.depends('date_of_birth', 'name')
    def _compute_age(self):
        for record in self:
            if record.date_of_birth:
                record.age = date.today().year - record.date_of_birth.year
            else:
                # whom_odoo_inheritance at happen if a put a string message here?
                record.age = 0

    # this decorator will trigger on a deleting a record and prevent to delete a patient when have appointments
    # the at_unistall=False it's to don't execute when we are uninstalling the module
    @api.ondelete(at_uninstall=False)
    def _check_appointments(self):
        for record in self:
            if record.appointment_ids:
                raise ValidationError(_("You can not delete a patient with appointments!"))

    # in de video use only vals but only work with vals_list, in this come all the field of the model
    # so we can access and make changes if it's necessary
    @api.model
    def create(self, vals_list):
        # the code of the sequence it's to identify the sequence of the model and bring the information
        vals_list['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals_list)

    # this function override the write function, the write function works when we create a new record, and then
    # we edit this record
    def write(self, vals):
        if not self.ref and not vals.get('ref'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).write(vals)

    # the original name_get function return the rec name of the model or the textual definition
    # will return a textual representation for the record in self. We don't use super in this because we are going
    # to re define the function for our module so the original will not execute
    def name_get(self):
        patient_list = []
        for record in self:
            name = '[' + str(record.ref) + '] ' + str(record.name)
            patient_list.append((record.id, name))
            # we can simplify the 4 line of code like this
            # return  [ (record.id, "[%s]%s" %(record.ref, record.name)) for record in self]
        return patient_list
