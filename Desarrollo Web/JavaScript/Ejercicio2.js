// Ingreso de datos

var Num1 = prompt("Ingresa valor maximo");

// Manejo de variables string a int

var num = parseInt(Num1);
var Pares = new Array(0);


for (let i = 0; i < num; i++) {
    if (i % 2 == 0){
        print(i)
        Pares.push(i)
    }
       
  }


alert(Pares);
console.log(Pares);
