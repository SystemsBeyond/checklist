/**
* Controle da função de menu
*/
function init_collapse(){
    $('.toggler-abre').on('click', function () {
        $('#sidebar').toggleClass('active');
        // close dropdowns
        $('.collapse.in').toggleClass('in');
        // and also adjust aria-expanded attributes we use for the open/closed arrows
        // in our CSS
        $('a[aria-expanded=true]').attr('aria-expanded', 'false');
        $('.toggler-abre').hide();
    });

    $('.fechar').on('click', function () {
        $('#sidebar').toggleClass('active');
        $('.toggler-abre').show();
    });
};

$(document).ready(function () {
    /* Inativa botao toggler*/
    $('.toggler-abre').hide();
    /*Inicializa controle do menu*/
    init_collapse();
});
