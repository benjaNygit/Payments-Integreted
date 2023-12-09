import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'
import FormCreate from '../pages/Products/formCreate'

function Navigate() {
    return (
        <>
            <Link to='/products/create'>Crear Producto</Link>
        </>
    )
}

function Navbar() {
    return (
        <BrowserRouter>
            <Navigate />
            <Routes>
                <Route path='/products/create' element={<FormCreate />} />
            </Routes>
        </BrowserRouter>
    )
}

export default Navbar