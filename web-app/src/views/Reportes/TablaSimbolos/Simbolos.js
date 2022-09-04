import React from "react";
import Button from 'react-bootstrap/Button';

function Simbolos(){

  var simbolos = []
    const generarSimbolos = () => {
        fetch('http://127.0.0.1:5000/api/simbolos', {
          method: 'POST',
          headers: {
            'Content-Type':'application/json'
          }
        })
          .then(resp => resp.json())
          .then(data => {
            console.log("simbolos");
            simbolos = data.simbolos
          })
          .catch(console.error);
    }

    function createTable(){
      let myTable = document.querySelector('#table');
      let headers = ['ID', 'Tipo Simbolo', 'Tipo Dato', 'Ambito'];
      let table = document.getElementById("tabla_errores");
      if (table != null) {
        table.remove();
      }
      table = document.createElement('table');
      table.classList.add("fl-table");
      table.setAttribute('id', 'tabla_errores');
      myTable.classList.add("table-wrapper")
      let headerRow = document.createElement('tr');
  
      headers.forEach(headerText => {
        let header = document.createElement('th')
        let textNode = document.createTextNode(headerText)
        header.appendChild(textNode)
        headerRow.appendChild(header)
      })
      
      table.appendChild(headerRow)
  
      simbolos.forEach(error =>{
        if (error["token"] !== ''){
          let row = document.createElement('tr')

          let cell = document.createElement('td')
          let textNode = document.createTextNode(error["id"])
          cell.appendChild(textNode)

          let cell2 = document.createElement('td')
          textNode = document.createTextNode(error["simbolo"])
          cell2.appendChild(textNode)

          let cell6 = document.createElement('td')
          textNode = document.createTextNode(error["tipo"])
          cell6.appendChild(textNode)

          let cell3 = document.createElement('td')
          textNode = document.createTextNode(error["ambito"])
          cell3.appendChild(textNode)

          row.appendChild(cell)
          row.appendChild(cell2)
          row.appendChild(cell6)
          row.appendChild(cell3)
          table.appendChild(row)

        }
      })
  
      myTable.appendChild(table)
    }

    return (
        <div className="grid grid-cols-1 text-white mt-6 gap-4 place-items-stretch h-48 p-8">
            <Button variant="primary" size="lg" onClick={generarSimbolos}>Generar Reporte</Button>
            <Button variant="primary" size="lg" onClick={createTable}>Crear Tabla</Button>
            <div className='flex max-w-[100rem] justify-center items-center mt-6 p-4'>
              <div className='flex w-full flex-col gap-5'>
                <div id="table"></div>
              </div>
            </div>
        </div>
    )
}

export default Simbolos;