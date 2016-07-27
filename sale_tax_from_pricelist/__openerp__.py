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
    "name": "Taxes from pricelists (tax included/excluded prices)",
    "version": "8.0",
    "author": "QAQA",
    "website": "http://www.qaqa.pl",
    "sequence": 0,
    "certificate": "",
    "license": "",
    "depends": ["sale","product"],
    "category": "Sale",
    "complexity": "easy",
    "description": """
Set sale-line tax from a pricelist. It allows one to set different taxes to different pricelists and in consequence:
* remove taxes from international or tax-free sales
* set taxes that are included in prices (for b2c sales) for some partners and tax excluded prices for other (for b2b sales)
Here is how to make tax included prices for some partners:
* add a new tax that is included in price (accounting / taxes / taxes -> included in price)
* set this tax on a new pricelist
* make prices on the pricelist tax-included
* attach this pricelist to a partner
    """,
    "demo": [
    ],
    "data": [
        "pricelist.xml",
    ],
    "images": [
    ],
    "auto_install": False,
    "installable": True,
    "application": False,

}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: