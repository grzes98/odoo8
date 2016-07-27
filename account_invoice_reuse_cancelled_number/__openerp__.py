# -*- encoding: utf-8 -*-
##############################################################################
#
#    Author: Grzegorz Marczyński
#    Copyright 2016 QAQA
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
    'name': "Reuse Cancelled Invoice Number",
    'version': '8.0.0.1.0',
    'category': 'Accounting & Finance',
    'summary': "Allows to reuse cancelled invoice number on specific invoices",
    'description': """
This module allows to reuse the cancelled invoice numbers.<br>
On invoice draft it displays a button that triggers a wizard wit the list of cancelled invoices with set internal_number field.<br>
If user selects an invoice, its number and date will be used as invoice (and move) number and date.
    """,
    'author': "QAQA",
    'website': 'http://www.qaqa.pl',
    'license': 'AGPL-3',
    "depends": [
        'account'
    ],
    "data": [
        'invoice_view.xml'
    ],
    "active": False,
    "installable": True,
    "application": False,
}
