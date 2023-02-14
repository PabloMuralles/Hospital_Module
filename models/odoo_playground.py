from odoo import api, fields, models


class OdooPlayGround(models.Model):
    _name = "odoo.playground"
    _description = "Odoo PlayGround"

    DEFAULT_ENV_VARIABLES = """# Available variables:
    #   -self: Current Object
    #   -self.env: Odoo Environment on which the action is triggered
    #   -self.env.user: Return the current user (as an instance)
    #   -self.env.is_system: Return whether the current user has group "Setting", or is in superuser mode.
    #   -self.env.is_admin: Return whether the current user has group "Access Rights", or is in superuser mode.
    #   -self.env.is_superuser: Return whether the environment is in superuser mode.
    #   -self.env.company: Return the current company (as a instance)
    #   -self.env.companies: Return a recordset of the enable companies by the user
    #   -self.env.lang: Retunr the current language code \n\n\n"""

    model_id = fields.Many2one('ir.model', string="Model")
    code = fields.Text(string="Code", default=DEFAULT_ENV_VARIABLES)
    result = fields.Text(string="Result")

    def action_execute(self):
        try:
            if self.model_id:
                model = self.env[self.model_id.model]
            else:
                model = self
        except Exception as e:
            self.result = str(e)
