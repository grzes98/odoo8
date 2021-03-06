# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Grzegorz Marczyński
#    Copyright 2015 QAQA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Auto CC/BCC for Odoo outgoing mail server',
    'summary': """
Automatically copy recipients into the emails Odoo sends. This module allows you to
define a list of email addresses added as Cc or Bcc when Odoo sends an email.
    """,
    'version': '1.1',
    'author': "QAQA",
    'maintainer': 'QAQA',
    'category': 'CRM',
    'license': 'AGPL-3',
    'depends': ['base'],
    'website': 'http://www.qaqa.pl',
    'data': [
        'view/ir_mail_server_view.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False
}
