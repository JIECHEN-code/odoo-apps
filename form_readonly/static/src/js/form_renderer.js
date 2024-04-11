/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { FormRenderer } from "@web/views/form/form_renderer";
import { evalDomain } from "@web/views/utils";

patch(FormRenderer.prototype, "based_on_state_readonly_form", {
    setup() {
        this._super(...arguments);
        // 如果this.props.record.data包含readonly_domain属性
        // 则根据readonly_domain属性的值，判断是否进入readonly模式
        if (this.props.record.data.readonly_domain) {
            const readonly_domain = this.props.record.data.readonly_domain;
            const domain = evalDomain(readonly_domain, this.props.record.model.root.evalContext);
            if (domain) {
                this.props.record.mode = "readonly";
            }
        }
    },
})