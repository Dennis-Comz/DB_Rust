import React from "react";
import { Console } from "../../components/Console/Console";
import { Button } from 'react-bootstrap';
import { useState } from 'react';
import '../../index.css'

const initialCode = '//COLOCA TU CODIGO RUST AQUÍ'

function Main(){
    const [code, setCode] = useState(initialCode);
    const [consoleText, setConsoleText] = useState('');
  
    const ejecutarHandler = () => {
  
      fetch('http://127.0.0.1:5000/api/interpretar', {
        method: 'POST',
        body: JSON.stringify({instrucciones:code}),
        headers: {
          'Content-Type':'application/json'
        }
      })
        .then(resp => resp.json())
        .then(data => {
          setConsoleText(data.resultado)
        })
        .catch(console.error);
    }
  
    const clearHandler = () => {
      setConsoleText('');
    }

    return (
        <div className="d-flex fill flex-column justify-content-start mt-6 p-3">
            <div className="text-white flex justify-evenly text-xl">
                <div>Entrada</div>
                <div></div>
                <div>Salida</div>
            </div>
            <div className='row flex-grow-1'>
                <Console code={code} setCode={setCode}>
                <Button
                    className='mt-3 bg-indigo-700'
                    variant="success"
                    onClick={ejecutarHandler}
                >Ejecutar</Button>{' '}
                </ Console>
                <Console readOnly code={consoleText} setCode={setConsoleText}>
                <Button
                    className='mt-3 bg-indigo-700'
                    variant="danger"
                    onClick={clearHandler}
                >Clear</Button>{' '}
                </Console>
            </div>
        </div>
    )
}

export default Main;