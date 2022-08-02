import React from "react";
import Button from 'react-bootstrap/Button';

function BaseDatos(){
    const generarBaseDatos = () => {
        fetch('http://127.0.0.1:5000/api/base_datos', {
          method: 'POST',
          headers: {
            'Content-Type':'application/json'
          }
        })
          .then(resp => resp.json())
          .then(data => {
            console.log("result");
          })
          .catch(console.error);
    }

    return (
        <div className="grid grid-cols-1 text-white mt-6 gap-4 place-items-stretch h-48 p-8">
            <Button variant="primary" size="lg" onClick={generarBaseDatos}>Generar Reporte</Button>
            <div>Aca va la tabla base de datos</div>
        </div>
    )
}

export default BaseDatos;