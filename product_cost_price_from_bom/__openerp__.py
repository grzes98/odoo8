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
    "name": "Cost prices per product variant from BOM",
    "version": "8.0",
    "author": "QAQA",
    "website": "http://www.qaqa.pl",
    "sequence": 0,
    "certificate": "",
    "license": "",
    "depends": ["stock_account", 'mrp'],
    "category": "Stock",
    "complexity": "easy",
    "description": """
Cost prices per product variant from BOM.
    """,
    "demo": [
    ],
    "data": [
        "product_view.xml",
    ],
    "images": [
    ],
    "auto_install": False,
    "installable": True,
    "application": False,

}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: