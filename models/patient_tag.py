from odoo import api, fields, models


class PatientTag(models.Model):
    _name = "patient.tag"
    _description = "Patient Tag"

    name = fields.Char(string="Name", rquired=True)
    active = fields.Boolean(string="Active", default=True)
    color = fields.Integer(string="Color")
    color_2 = fields.Char(string="Color 2")
    sequence = fields.Integer(string="Sequence")

    # sql constraints: first the name of the constraint can be anything you want then the constraint and finally
    # the message, in some case if exist data that violate the constraints maybe will not work the constraint
    _sql_constraints = [
        ('unique_tag_name', 'unique (name, active)', 'Name must be unique.'),
        ('check_sequence', 'check (sequence > 0)', 'Sequence must be non zero positive number'),
    ]

