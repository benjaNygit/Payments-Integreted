import React from 'react'
import ReactDOM from 'react-dom/client'
import Navbar from './components/navbar'
import FormCreate from './pages/Products/formCreate'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <>
      <Navbar />
      <h1>Hello World!</h1>
      <FormCreate />
    </>
  </React.StrictMode>,
)
