# -*- coding: utf-8 -*-
{
    'name': "form_readonly",

    'summary': """
        Form readonly module""",

    'description': """
    English:
        Set the readonly attribute of the form based on the readonly_domain field of the model.
        ps:
        readonly_domain = fields.Char(string='只读域', default="[('sq_state','!=','draft')]")，
        When the value of the sq_state field is not equal to draft, the form is readonly.
        note：The form that requires this feature needs to add a readonly_domain field in the form.
    Chinese:
        根据模型的readonly_domain字段，设置表单的只读属性。
        比如：readonly_domain = fields.Char(string='只读域', default="[('sq_state','!=','draft')]")，
        表示当sq_state字段的值不等于draft时，表单只读。
        备注：需要使用该功能的表单，需要在表单中添加readonly_domain字段。
    """,

    'author': "JIIECHEN",
    'license': 'AGPL-3',
    'category': 'Custom/Custom',
    'version': '16.0.1.0.0',

    'depends': ['base', 'web'],
    'assets': {
        'web.assets_backend': [
            '/form_readonly/static/src/js/form_controller.js',
            '/form_readonly/static/src/js/form_renderer.js',
        ]
    },
    'installable': True,
    # 'images': ['static/description/banner.png'],
}
