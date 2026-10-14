// Copyright (c) 2026, BWH and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
	refresh(frm) {
        if (frm.doc.status === "New") {
            frm.add_custom_button(__("Accept"), ()=> { 
                frm.set_value("status", "Accepted");
                frm.save();
            },"Actions");
        
            frm.add_custom_button(__("Reject"), ()=> { 
                frm.set_value("status", "Rejected");
                frm.save();
            },"Actions");
        }
}});


