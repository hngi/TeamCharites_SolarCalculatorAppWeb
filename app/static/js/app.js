$("document").ready(function(){
    $("#result").click(function(){
        var total_power = $("#tpc").val();
        var solar_panel_power = $("#spp").val();
        var battery_voltage = $("#bv").val();
        var days_of_autonomy = $("#doa").val();
        $.ajax({
            url: "https://charites-solarcalculator.herokuapp.com/result/",
            type: "GET",
            contentType: "application/json",
            data: JSON.stringify({"total_power": total_power, "solar_panel_power":solar_panel_power,
            "battery_voltage":battery_voltage, "days_of_autonomy":days_of_autonomy})
        }).done(function(data) {
            console.log(data);
        });
    });
});

