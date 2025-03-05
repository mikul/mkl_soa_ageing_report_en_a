from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'


    default_soa_opening_account_id = fields.Many2one(
        'account.account',
        string="Default AR Account",
        company_dependent=True,  
        default_model='en.ageing.customer.statement.wizard'
    )

    default_soa_opening_journal_id = fields.Many2one(
        'account.journal',
        string="Default Journal",
        company_dependent=True,  
        default_model='en.ageing.customer.statement.wizard'
    )


