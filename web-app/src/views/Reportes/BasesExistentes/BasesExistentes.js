import React from "react";
import Button from 'react-bootstrap/Button';

function BasesExistentes(){
    const generarBasesExistentes = () => {
        fetch('http://127.0.0.1:5000/api/existentes', {
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
            <Button variant="primary" size="lg" onClick={generarBasesExistentes}>Generar Reporte</Button>
            <div>Aca va la tabla bases existentes</div>
        </div>
    )
}

export default BasesExistentes;