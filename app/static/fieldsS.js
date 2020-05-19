
$(document).ready(function() {

    $("#d2_hidden_soft").hide();
    $("#d3_hidden").hide();
    $("#d6_hidden").hide();
    $("#d7_hidden_soft").hide();
    $("#d8_hidden").hide();
    $("#d10_hidden").hide();
    $("#d10_2_hidden").hide();
    $("#d16_hidden").hide();
    $("#d18_hidden").hide();

    $("#d2-4").on("change", function() {
        if ($("#d2-4").prop("checked"))
            $("#d2_hidden_soft").show();
        else
           $("#d2_hidden_soft").hide();
    });

    $("#d3-0").on("change", function() {
        $("#d3_hidden").show();
    });
    $("#d3-1").on("change", function() {
        $("#d3_hidden").hide();
    });
    $("#d3-2").on("change", function() {
        $("#d3_hidden").hide();
    });

    $("#d6-0").on("change", function() {
        $("#d6_hidden").show();
    });
    $("#d6-1").on("change", function() {
        $("#d6_hidden").hide();
    });

    $("#d7-0").on("change", function() {
        $("#d7_hidden_soft").show();
    });
    $("#d7-1").on("change", function() {
        $("#d7_hidden_soft").hide();
        $("#d8_hidden").hide();
    });

    $("#d8-0").on("change", function() {
        if ($("#d8-0").prop("checked"))
            $("#d8_hidden").show();
        else
            $("#d8_hidden").hide();
    });

    $("#d10-0").on("change", function() {
        $("#d10_hidden").show();
    });
    $("#d10-1").on("change", function() {
        $("#d10_hidden").hide();
        $("#d10_2_hidden").hide();
    });

    $("#d10_1-3").on("change", function() {
        $("#d10_2_hidden").show();
    });
    $("#d10_1-0").on("change", function() {
        $("#d10_2_hidden").hide();
    });
    $("#d10_1-1").on("change", function() {
        $("#d10_2_hidden").hide();
    });
    $("#d10_1-2").on("change", function() {
        $("#d10_2_hidden").hide();
    });

    $("#d16-3").on("change", function() {
        if($("#d16-3").prop("checked"))
            $("#d16_hidden").show();
        else
            $("#d16_hidden").hide();
    });

    $("#d18-0").on("change", function() {
        $("#d18_hidden").show();
    });
    $("#d18-1").on("change", function() {
        $("#d18_hidden").hide();
    });

});