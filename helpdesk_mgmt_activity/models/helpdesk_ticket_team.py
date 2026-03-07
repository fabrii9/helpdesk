# Copyright (C) 2024 Cetmix OÜ
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class HelpdeskTicketTeam(models.Model):
    _inherit = "helpdesk.ticket.team"

    allow_set_activity = fields.Boolean(
        string="Establecer actividades",
        help="Disponible para establecer actividad en el registro fuente desde el ticket",
    )
    activity_stage_id = fields.Many2one(
        comodel_name="helpdesk.ticket.stage",
        string="Etapa de actividad completada",
        domain="['|', ('team_ids', 'in, []'), ('team_ids', 'in', [id])]",
        help="Mover el ticket cuando la actividad en el registro fuente est\u00e9 completada",
    )
