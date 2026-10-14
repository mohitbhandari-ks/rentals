// Copyright (c) 2026, BWH and contributors
// For license information, please see license.txt

frappe.ui.form.on("Vehicle_Custom", {
	refresh(frm) {
        frm.get_field("summary").$wrapper.empty();
	},
    get_summary(frm){
        frm.get_field("summary").$wrapper.append("<h2>Here is you summary</h2>")
    }
});
