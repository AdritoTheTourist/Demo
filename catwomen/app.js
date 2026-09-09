let form = document.querySelector("form")

form.addEventListener("submit" , function(a){

    a.preventDefault();
    
})

let p = document.querySelector("p")

let inp = document.querySelector("input")
    
 inp.addEventListener("input" , function(){


    console.log(this.value)
    p.innerText = this.value
    console.log(p)
     
 })

