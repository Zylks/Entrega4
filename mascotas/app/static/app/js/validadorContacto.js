$.validator.addMethod("terminaPor", function(value, element, parametro){

    if(value.endsWith(parametro)){
        return true;
    }
    return false;

}, "Debe terminar por {0}")



$("#contacto").validate({
    rules: {
        nombre: {
            required: true,
            minlength: 3,
            maxlength: 50 
        },
        correo: {
            required: true,
            email: true,
            terminaPor: "gmail.com"
        },
        telefono: {
            required: true
        },
        mensaje: {
            required: true,
            minlength: 10,
            maxlength: 500 
        }

    }
})




$("#boton").click(function(){
    if($("#contacto").valid() == false){
        return;
    }
    let nombre = $("#nombre").val()
    let correo = $("#correo").val()
    let telefono = $("#telefono").val()
    let mensaje = $("#mensaje").val()
})