import React from 'react'
import ReactDOM from 'react-dom/client'
import Navbar from './components/navbar'
import ProductsList from './pages/Products/ProductsList'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <>
      <Navbar />
      <ProductsList />
    </>
  </React.StrictMode>,
)
