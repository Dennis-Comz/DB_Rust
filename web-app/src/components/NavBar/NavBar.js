import React from "react";
import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import NavDropdown from 'react-bootstrap/NavDropdown';
import logo from './Logo/rust.png';
import {Link} from "react-router-dom";

function NavBar(){
    return (
        <Navbar className="bg-indigo-700" variant="dark">
        <Container>
            <Navbar.Brand href="#home">
                <img alt="" src={logo} width="100" height="100" className="d-inline-block align-top" />{' '}
          </Navbar.Brand>
          <Nav className="me-auto text-xl font-bold text-white">
            <Nav.Link ><Link to="/">DB-RUST</Link></Nav.Link>
            <NavDropdown title="Reportes" id="basic-nav-dropdown">
              <NavDropdown.Item ><Link to="/reporte/simbolos">Tabla de Símbolos</Link></NavDropdown.Item>
              <NavDropdown.Item ><Link to="/reporte/errores">Reporte de Errores</Link></NavDropdown.Item>
              <NavDropdown.Item ><Link to="/reporte/bases_existentes">Bases de Datos Existentes</Link></NavDropdown.Item>
              <NavDropdown.Item ><Link to="/reporte/base_datos">Base de Datos</Link></NavDropdown.Item>
            </NavDropdown>
            <Nav.Link><Link to="/about">About</Link></Nav.Link>
          </Nav>
        </Container>
      </Navbar>
    )
}

export default NavBar;