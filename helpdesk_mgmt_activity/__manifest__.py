# Copyright (C) 2024 Cetmix OÜ
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Actividad de Mesa de Ayuda",
    "summary": "Crear Actividades para registros de Odoo desde la Mesa de Ayuda",
    "version": "19.0.1.0.0",
    "license": "AGPL-3",
    "author": "Cetmix OÜ, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/helpdesk",
    "depends": ["helpdesk_mgmt"],
    "data": [
        "views/res_config_settings_views.xml",
        "views/helpdesk_ticket_view.xml",
        "views/mail_activity_views.xml",
        "views/helpdesk_ticket_team_views.xml",
    ],
    "application": False,
}
