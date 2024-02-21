{
    "name": "Saldo App",
    "description": "Aplicacion web para registart ingresos y egresos",
    "version": "1.0",
    "depends": ["base", "mail"],
    "data": [
        'views/views.xml',
        'security/ir_model_acces.xml'
    ],
    "assets": {
        'web.assets_backend': [
            "saldo_app/static/css/style.css"
        ]
    }
}