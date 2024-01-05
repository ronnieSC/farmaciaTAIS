var resp ;
var prods ;
var l=1;


function cloneRow() {
    var row = document.getElementById("rowToClone");
    var table = document.getElementById("tableToModify"); 
      var clone = row.cloneNode(true);
      clone.id = "nuevo_row_"+l;
    clone.className = "nuevo_row_class";
      table.appendChild(clone);
    var new_row=document.getElementById("nuevo_row_"+l);
    new_row.cells[0].children[0].id='new_product_'+l;
    new_row.cells[1].children[0].id='new_descripcion_'+l;
    new_row.cells[2].children[0].id='new_cantidad_'+l;
    new_row.cells[3].children[0].id='new_precio_'+l;
    new_row.cells[1].children[0].value="vacio";
    new_row.cells[3].children[0].value="0";
    l=l+1;
}

function resetRows() {
    var elements = document.getElementsByClassName("nuevo_row_class");
    while(elements.length > 0){
        var parent = elements[0].parentNode;
        parent.removeChild(elements[0]);
    }
    l=1;
}
function delete_select(selid){
    var select = document.getElementById(selid);
    var length = select.options.length;
    for (i = length-1; i >= 0; i--) {
          select.options[i] = null;
    }
}
function fill_by_select(myid,desiredcombo){
    var selactual=document.getElementById(myid)
    for(var i = 0; i < resp.length; i += 1){
           var result = resp[i];  
           if(result.id == selactual.value){
            document.getElementById('dir').value=result.direccion;
            document.getElementById('email').value=result.email;	
            var j;
            var selectcliente=document.getElementById(desiredcombo);
            for (j=0;j<selectcliente.length; j += 1){
                if (selectcliente.options[j].value==selactual.value){
                    break;
                }
            }
            document.getElementById(desiredcombo).selectedIndex=j;
            document.getElementById('telefono').value=result.telefono;
           }
    }
}
function get_price(myid){
    get_last_number(myid);
    var last_char=get_last_number(myid);
    var quantity=document.getElementById(myid).value; 
    var get_producto_value=document.getElementById('new_product_'+last_char).value; 
    for(var i = 0; i < prods.length; i += 1){
           var result = prods[i];  
           if(result.id == get_producto_value){
               document.getElementById('new_precio_'+last_char).value=(result.precio*quantity);
               sum_all();
           }
    }
}
function get_last_number(str){
    const regex = /(?!.*_)(.*[0-9]$)/gm;
    let m;

    while ((m = regex.exec(str)) !== null) {
        if (m.index === regex.lastIndex) {
            regex.lastIndex++;
        }
    return (m[0]);
    }
}
function sum_all(){
    var elements = document.getElementsByClassName("precios_a_sumar");
    var h=0;
    var sum=0;
    while(elements.length > h){
        sum=sum+parseInt(elements[h].value);
        h=h+1;
    }
    document.getElementById('total').value=sum;
}
function fill_by_select_prod(myid){
    var selactual=document.getElementById(myid);
    var last_char=get_last_number(myid);
    delete_select('new_cantidad_'+last_char);
    var sel = document.getElementById('new_cantidad_'+last_char);
    var opt = document.createElement('option');
    opt.appendChild( document.createTextNode("0") );
    opt.value = 0; 
    sel.appendChild(opt);
    for(var i = 0; i < prods.length; i += 1){
           var result = prods[i];  
           if(result.id == selactual.value){
            document.getElementById('new_precio_'+last_char).value=0;
            document.getElementById('new_descripcion_'+last_char).value=result.descripcion;	
            if (result.cantidad >=1){
                for (var i = 1; i <= result.cantidad ; i++) {
                    var sel = document.getElementById('new_cantidad_'+last_char);
                    var opt = document.createElement('option');
                    opt.appendChild( document.createTextNode(i) );
                    opt.value = i; 
                    sel.appendChild(opt);
                }
            }
            
           }
    }
}
function create_table(){
    
}
function OnloadDoc1() {
    
    var xhttp=new XMLHttpRequest();
    xhttp.onreadystatechange=function(){
      if (this.readyState == 4 && this.status==200)  { 
        prods =JSON.parse(this.responseText);
        console.log(prods);
        for (var i = 0; i < prods.length; i++) {
            var sel = document.getElementById('new_product_0');
            var opt = document.createElement('option');
            opt.appendChild( document.createTextNode(prods[i].nombre) );
            opt.value = prods[i].id; 
            sel.appendChild(opt);
              }
        }
       };
    xhttp.open("GET", "/producto/query/", true);
    xhttp.send();

}
function OnloadDoc() {
    OnloadDoc1();
    var xhttp=new XMLHttpRequest();
    xhttp.onreadystatechange=function(){
      if (this.readyState == 4 && this.status==200)  { 
        resp =JSON.parse(this.responseText);
        console.log(resp);
       
        //delete_select('cli');
        
        //delete_select('dni');
        for (var i = 0; i < resp.length; i++) {
            var sel = document.getElementById('cli');
            var opt = document.createElement('option');
            opt.appendChild( document.createTextNode(resp[i].nombres+" "+resp[i].apellidos) );
            opt.value = resp[i].id; 
            sel.appendChild(opt); 
            sel = document.getElementById('dni');
            opt = document.createElement('option');
            opt.appendChild( document.createTextNode(resp[i].DNI) );
            opt.value = resp[i].id; 
            sel.appendChild(opt); 
              }
        }
       };
    xhttp.open("GET", "/cliente/query/", true);
    xhttp.send();

}