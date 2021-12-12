// Ingreso de datos

var Num1 = prompt("Ingresa primer número");
var Num2 = prompt("Ingresa segundo número");

// Manejo de variables string a int

var num = parseInt(Num1);
var numm = parseInt(Num2);

// Ingreso de operacion
var Operacion = prompt("¿Qué operación deseas hacer?");

// Variable resultado
var ResultadoOperacion = null;
var TextoFinal = null;

// Identificacion de operación
if (Operacion == "+") {
  ResultadoOperacion = num + numm;
  texto = "El resultado de la operacion es " + ResultadoOperacion;
} else if (Operacion == "-") {
  ResultadoOperacion = num - numm;
  texto = "El resultado de la operacion es " + ResultadoOperacion;
} else if (Operacion == "*") {
  ResultadoOperacion = num * numm;
  texto = "El resultado de la operacion es " + ResultadoOperacion;
} else if (Operacion == "/") {
  ResultadoOperacion = num / numm;
  texto = "El resultado de la operacion es " + ResultadoOperacion;
} else {
  texto = "Cuidado vaquero!";
}

alert(texto);
console.log(texto);
