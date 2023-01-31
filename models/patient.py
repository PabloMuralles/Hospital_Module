from datetime import date
from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"  # odoo will create a table with this name example hospital_patient
    _inherit = "mail.thread", 'mail.activity.mixin'  # this inherits it's to can use the chatter in the form view
    # then we have to add the dependencies in the manifest in views, we have to se in what module it's define the
    # class that we are inherit to put this module in the dependence
    _description = "HospitalPatient"
    # _rec_name = "name" in this case we don't need a rec name because the modele have a field name so odoo automatically use this

    # how to create the field in the database of this table patient
    name = fields.Char(string='Name', tracking=True) #the tracking it's to show the changes of the filed in the chatter section, we need to have activeted the chatter
    date_of_birth = fields.Date(string="Date of Birth")
    ref = fields.Char(string='Reference')
    age = fields.Integer(string='Age', compute="_compute_age", tracking=True) # if we want to store the this computed fild store=True
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', tracking=True, default='female')
    active = fields.Boolean(string="Active", default=True)  # this field is to put the option archive or unarchive in odoo view

    #how to define a function in a model
    #this funtion it's for a computed fild, a computed fild will not stored in the databese this field will be calculate all the times
    #so this means that will take server resources
    @api.depends('date_of_birth') # this decorator it's to compute the fild when we change or set the date of birth in the form view becuase if we don't put this the funtion will compute when we sabe the patient, we can have multiple depends filds and we have to follow this syntax @api.depends('date_of_birth', 'name')
    def _compute_age(self):
        for record in self:
            if record.date_of_birth:
                record.age = date.today().year - record.date_of_birth.year
            else:
                record.age = 0