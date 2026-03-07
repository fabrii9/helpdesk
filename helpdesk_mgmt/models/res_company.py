# Copyright 2022 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Company(models.Model):
    _inherit = "res.company"

    helpdesk_mgmt_portal_select_team = fields.Boolean(
        string="Seleccionar equipo en portal de Mesa de Ayuda"
    )
    helpdesk_mgmt_portal_team_id_required = fields.Boolean(
        string="Campo Equipo requerido en portal de Mesa de Ayuda",
        default=True,
    )
    helpdesk_mgmt_portal_category_id_required = fields.Boolean(
        string="Campo Categoría requerido en portal de Mesa de Ayuda",
        default=True,
    )
    helpdesk_mgmt_duplicate_tracking = fields.Boolean(
        string="Habilitar seguimiento de tickets duplicados", default=False
    )
    helpdesk_mgmt_duplicate_ticket_stage_id = fields.Many2one(
        comodel_name="helpdesk.ticket.stage",
        string="Mover tickets duplicados a esta etapa",
        default=False,
    )
    helpdesk_mgmt_ticket_auto_assign = fields.Boolean(
        string="Auto asignar tickets",
        default=True,
    )
