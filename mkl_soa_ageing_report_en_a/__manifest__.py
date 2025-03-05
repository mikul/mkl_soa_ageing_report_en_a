{
    'name': 'Customer Statement with Ageing Report (Enterprise)',
    'version': '2.3.2',

    'category': 'Accounting',
    'summary': 'Detailed Customer Statement with Ageing and Transaction History for Enterprise ',
    'description': """
Customer Statement of Account Report

This app provides a professional report that can be printed directly from the customer record in Odoo. 
It allows users to generate a detailed customer statement of account with the following features:

- **Date Range Selection**: Easily select the coverage period for the statement.
- **Account Summary**: Includes opening balance, total invoiced amount, payments received, and the balance due.
- **Ageing**: Shows current up to 90 Days past due.
- **Transaction History**: Displays a chronological list of transactions (invoices and payments) with details and running balance computation.
- **Integrated Reporting**: The report is accessible directly under the customer record, streamlining access for accountants and sales representatives.
- **Misc. Entry Opening Balance**: Captures Partner Misc. Entry for Opening Balance.

This app is ideal for businesses that want to provide clear and concise statements to their customers.
""",
    'price': 30.00,
    'currency': 'EUR',
    'license': 'OPL-1',
    'author': 'Mikul Buncha',
    'company': 'Mikool Inc',
    'depends': ['accountant','base'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_config_settings_view.xml',
        'report/customer_statement_template.xml',
        'report/customer_statement_report.xml',
        'wizard/customer_statement_wizard_view.xml',
    ],
    'images': ['static/description/banner.png'],  # Optional: include a banner image for the Odoo App Store
    'installable': True,
    'application': False,
    'auto_install': False,
}