import { useEffect, useState } from "react"
import { getAllProducts } from "../../api/products.api"

function ProductsList() {
    const [products, setProducts] = useState([])

    useEffect(() => {
        async function loadProducts() {
            const response = await getAllProducts()
            setProducts(response.data)
        }
        loadProducts()
    }, [])
    return (
        <div>{products.map(product => <ProductsCard key={product.id} product={product}/>)}</div>
    )
}

function ProductsCard({ product }) {
    return (
        <fieldset>
            <legend>{product.name}</legend>
            <p><span>Descripción</span> {product.description}</p>
            <p><span>Precio</span> {product.price}</p>
            <p><span>Cantidad Disponible</span> {product.stock}</p>
            <p><span>Descuento</span> %{product.discount}</p>
        </fieldset>
    )
}

export default ProductsList