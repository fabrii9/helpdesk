# Copyright 2024 Onestein
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Fusión de Tickets de Mesa de Ayuda",
    "summary": "Asistente para fusionar tickets de mesa de ayuda",
    "version": "19.0.1.0.0",
    "author": "Onestein, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/helpdesk",
    "license": "AGPL-3",
    "category": "After-Sales",
    "depends": ["helpdesk_mgmt"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/helpdesk_ticket_merge_views.xml",
    ],
    "installable": True,
}
