# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


# transient model will not store data in te db will be in other place
class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    # to save this fild will have to put config parameter and this will create a new entry inside the ir.confi.parameter
    # with the name that we put in the config_parameter
    cancel_days = fields.Integer(string='Cancel Days', config_parameter="om_hospital.cancel_day")
