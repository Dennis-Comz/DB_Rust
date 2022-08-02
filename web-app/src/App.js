import React from "react";
import Main from "./views/Main/Main"
import NavBar from './components/NavBar/NavBar';
import About from './views/About/About';
import BaseDatos from './views/Reportes/BaseDatos/BaseDatos';
import BasesExistentes from './views/Reportes/BasesExistentes/BasesExistentes';
import Errores from './views/Reportes/Errores/Errores';
import Simbolos from './views/Reportes/TablaSimbolos/Simbolos';
import {Routes, Route} from "react-router-dom";
import './App.css';

function App() {
  return (
    <div className="App">
      <NavBar />
      <Routes>
        <Route path="/" element={<Main />} />
        <Route path="/about" element={<About />} />
        <Route path="/reporte/simbolos" element={<Simbolos />} />
        <Route path="/reporte/errores" element={<Errores />} />
        <Route path="/reporte/bases_existentes" element={<BasesExistentes />} />
        <Route path="/reporte/base_datos" element={<BaseDatos />} />
      </Routes>
    </div>
  );
}

export default App;