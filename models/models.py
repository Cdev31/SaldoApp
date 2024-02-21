from odoo import fields, models


class Movimiento( models.Model ):
    _name = "sa.movimiento"
    _description = "Movimiento"
    _inherit = "mail.thread" 

    name = fields.Char( string="Nombre" )
    type_move = fields.Selection(
        selection=[
            ("ingreso", "Ingreso"), 
            ("gastos", "Gastos")]
            )
    date = fields.Datetime( string="Fecha" )
    amount = fields.Float( string="Monto", track_visibility="onchange" )
    receipt_image = fields.Binary( string="Foto del recibo" )
    notas = fields.Html("Notas")
    currency_id = fields.Many2many("res.currency")

    user_id = fields.Many2one( "res.users", string="Usuario" )
    category_id = fields.Many2one( "sa.categoria", string="Categoria" )
    etiquetas_ids = fields.Many2many( "sa.etiqueta", "sa_ta_tag_move", "move_id","etiqueta_id" )

class Categoria( models.Model ):
    _name = "sa.categoria"
    _description = "Categoria"

    name = fields.Char( string="Nombre" )


class Etiqueta( models.Model ):
    _name = "sa.etiqueta"
    _description = "Etiquetas"

    name = fields.Char( string="Nombre" )


class ResUser( models.Model ):
    _inherit = "res.users"

    movimiento_ids = fields.One2many( "sa.movimiento", "user_id" )    