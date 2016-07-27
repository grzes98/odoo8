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

from openerp.osv import fields, osv

class ir_mail_server(osv.osv):
    _inherit = "ir.mail_server"
    _columns = {
        'remove_reply_to': fields.boolean('Remove Reply-to main address', default=False, help="Remove reply-to main address in message header"),
        'auto_CC_addresses': fields.text('Auto CC addresses', default="", help="Comma-separated list of auto CC addresses"),
        'auto_BCC_addresses': fields.text('Auto BCC addresses', default="", help="Comma-separated list of auto BCC addresses"),
    }

    def send_email(self, cr, uid, message, mail_server_id=None, smtp_server=None, smtp_port=None,
               smtp_user=None, smtp_password=None, smtp_encryption=None, smtp_debug=False,
               context=None):

        ir_mail_server_pool = self.pool.get('ir.mail_server')

        if not mail_server_id:
            mail_server_id = ir_mail_server_pool.search(cr, uid, [])[0]

        server = ir_mail_server_pool.browse(cr, uid, mail_server_id)

        if server.remove_reply_to:
              del message['Reply-to']
              message['Reply-to'] = message['From']

        if server.auto_BCC_addresses:
            if not message['Bcc']:
                message['Bcc'] = server.auto_BCC_addresses
            else:
                bcc = message['Bcc']
                del message['Bcc']
                message['Bcc'] = bcc + "," + server.auto_BCC_addresses

        if server.auto_CC_addresses:
            if not message['Cc']:
                message['Cc'] = server.auto_CC_addresses
            else:
                cc = message['Cc']
                del message['Cc']
                message['Cc'] = cc + "," + server.auto_CC_addresses

        return super(ir_mail_server, self).send_email(cr, uid, message, mail_server_id, smtp_server, smtp_port,
               smtp_user, smtp_password, smtp_encryption, smtp_debug,
               context)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: