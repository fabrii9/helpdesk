# Copyright (C) 2024 Cetmix OÜ
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import ast

from odoo import api, fields, models
from odoo.fields import Command


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    helpdesk_available_model_ids = fields.Many2many(
        comodel_name="ir.model",
        domain="[('transient', '=', False)]",
        string="Modelos disponibles",
        help="Modelos disponibles para establecer registro fuente en ticket de mesa de ayuda",
    )

    def set_values(self):
        super().set_values()
        ICPSudo = self.env["ir.config_parameter"].sudo()
        ICPSudo.set_param(
            "helpdesk_mgmt_activity.helpdesk_available_model_ids",
            str(self.helpdesk_available_model_ids.ids),
        )
        return

    @api.model
    def get_values(self):
        res = super().get_values()
        ICPSudo = self.env["ir.config_parameter"].sudo()
        helpdesk_available_model_ids = ICPSudo.get_param(
            "helpdesk_mgmt_activity.helpdesk_available_model_ids", False
        )
        if helpdesk_available_model_ids:
            ids_list = ast.literal_eval(helpdesk_available_model_ids)
            if ids_list:
                res.update(
                    helpdesk_available_model_ids=[Command.set(ids_list)]
                )
        return res
