// Copyright (c) 2026, BWH and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Booking", {
	refresh(frm) {
        console.log("Refresh called");
	},
    rate(frm) {
        frm.trigger("update_total_amount");
    },
    update_total_amount(frm) {
        console.log("update_total_amount");
        total_distance = 0;
        frm.doc.items.forEach((item) => {
            total_distance += item.distance;
        });
        const amount = total_distance * frm.doc.rate;
        frm.set_value("total_amount", amount);
    }
});

frappe.ui.form.on("Ride Booking Item", {
    refresh(frm) {
        console.log("Refresh Ride Booking Item called");
    },
    distance(frm, cdt, cdn) {
        frm.trigger("update_total_amount");
    },
    items_remove(frm, cdt, cdn) {
        frm.trigger("update_total_amount");
    }
});
