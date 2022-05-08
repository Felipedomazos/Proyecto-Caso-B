
$.validator.addMethod("terminaPor", function(value, element, parametro){

    if(value.endsWith(parametro)){
        return true;
    }

    return false;
}, "Debe terminar por {0}")




$("#formulario_registro").validate({
    rules: {
        email: {
            required: true,
            email: true,
            terminaPor: "gmail.com"
        },
        contra: {
            required: true,
            minLength: 5, 
            maxLength: 30
        },
        direccion: {
            required: true
        },
        ciudad: {
            required: true,
            minLength: 4,
            maxLength: 50
        },
        zipcode: {
            required: true,
            number: true
        },
        region: {
            required: true
        },
        terminos: {
            required: true
        }
    }

})




$("#guardar").click(function() {
    if($("#formulario_registro").valid() == false) {
        return;
    }
    let email = $("#email").val()
    let contra = $("#contra").val()
    let direccion = $("#direccion").val()
    let ciudad = $("#ciudad").val()
    let zipcode = $("#zipcode").val()
    let region = $("#region").val()
    let terminos = $("#terminos").is(":checked")

})