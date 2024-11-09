
    
    //tabla de multiplicar
    var num=parseInt(prompt("ingrese el valor para sacar su tabla de multiplicar", 0));
     if (num<1){
        console.log("valores mayores a 0");
        num=parseInt(prompt("ingrese el valor para sacar su tabla de multiplicar", 0));
  }

    function calculadora (num){
        let y=1;
        let mul="";

        while(y<=10){
            mul=num*y;
            console.log (num+ "*" +y+ "=" +mul);
            y++;
        }
    }
    calculadora (num);


    //ED
    let n1=parseInt(prompt("Ingrese el primer número:"));
    let n2=parseInt(prompt("Ingrese el segundo número:"));

    if (n1>=n2) {
        console.log("El primer número debe ser menor que el segundo");
        n1=parseInt(prompt("Ingrese el primer número:"));
        n2=parseInt(prompt("Ingrese el segundo número:"));
    }
    for (let i=n1 + 1; i<n2; i++){
        console.log("ED-" +i);
    }


    //pares e impares
    let n3=parseInt(prompt("Ingrese el primer número:"));
    let n4=parseInt(prompt("Ingrese el segundo número:"));
    const numero=[n3, n4];

    
    for (let i=0; i<numero.length; i++){
        if (numero[i]%2==0){
            console.log(numero[i]+ " es par");
        }else{
            console.log(numero[i]+ " es impar");
        }
    }
          
        

      
      
      