// Ejercicio 4


function media(arrayNum){
    var Resultado = 0;
    // Variable para almacenar cantidad de elementos del array
    var CantidadElementos = 0;
    // Variable para almacenar todos los numeros del array
    var Numeros = 0;
    CantidadElementos = Object.keys(arrayNum).length;

    for (var i = 0; i<arrayNum.length; i++){
        Numeros += arrayNum[i];
     
    }

    Resultado = Numeros/CantidadElementos
   
    // Se muestra el resultado
    console.log(Resultado)
    
}


const Array1 = [1,10,15,20]
// Se hace llamado a la función con el array a comprobar
console.log(media(Array1))