from odoo import api, fields, models


class AppointmentPharmacyLince(models.Model):
    _name = "appointment.pharmacy.lines"
    _description = "Appointment Pharmacy Lince"

    # to use this model it's important to add the model to the depends on the manifest file and then update the app
    # list in odoo
    product_id = fields.Many2one(comodel_name="product.product", required=True)
    # this related because the product have a price, so we bring this price and the name of the attribute
    # we have so it in the product in developer mode or in the table
    price_unit = fields.Float(related='product_id.list_price')
    qty = fields.Integer(string="Quantity", default=1)
    # to have a field one2many we need to have a field many2one to link the lines to the appointment
    appointment_id = fields.Many2one(comodel_name='hospital.appointment', string='Appointment')
