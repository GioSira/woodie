
$(document).ready(function() {

    $("#d2_hidden").hide();
    $("#d12_hidden").hide();
    $("#d7_hidden").hide();

    $("#d7-1").prop('checked',true);

        $("#d2_4-0").on("change", function() {
        $("#d2_hidden").show();
    });
    $("#d2_4-1").on("change", function() {
        $("#d2_hidden").hide();
        $("#d2_5-0").prop('checked',false);
        $("#d2_5-1").prop('checked',false);
        $("#d2_5-2").prop('checked',false);
        $("#d2_5-3").prop('checked',false);
        $("#d2_5-4").prop('checked',false);
    });

    $("#d11-0").on("change", function() {
        $("#d12_hidden").show();
    });
    $("#d11-1").on("change", function() {
        $("#d12_hidden").hide();
        $("#d12-0").prop('checked',false);
        $("#d12-1").prop('checked',false);
        $("#d12-2").prop('checked',false);
    });

    $("#d6-2").on("change", function() {
        $("#d7-1").prop('checked',false);
        $("#d7_hidden").show();
    });
    $("#d6-0").on("change", function() {
         $("#d7_hidden").hide();
         $("#d7-0").prop('checked',false);
         $("#d7-1").prop('checked',true);
    });
    $("#d6-1").on("change", function() {
         $("#d7_hidden").hide();
         $("#d7-0").prop('checked',false);
         $("#d7-1").prop('checked',true);
    });
    $("#d6-3").on("change", function() {
         $("#d7_hidden").hide();
         $("#d7-0").prop('checked',false);
         $("#d7-1").prop('checked',true);
    });

});