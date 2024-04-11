# -*- coding: utf-8 -*-
{
    'name': "form_readonly",

    'summary': """
        表单只读模块""",

    'description': """
        根据模型的readonly_domain字段，设置表单的只读属性。
        比如：readonly_domain = fields.Char(string='只读域', default="[('sq_state','!=','draft')]")，
        表示当sq_state字段的值不等于draft时，表单只读。
        备注：需要使用该功能的表单，需要在表单中添加readonly_domain字段。
    """,

    'author': "JIIECHEN",
    'website': "https://www.kyber-platform.com/",

    'category': '铠铂云-插件/Kyber-Plugin',
    'version': '0.1',

    'depends': ['base', 'web'],
    'assets': {
        'web.assets_backend': [
            '/form_readonly/static/src/js/form_controller.js',
            '/form_readonly/static/src/js/form_renderer.js',
        ]
    },
}
