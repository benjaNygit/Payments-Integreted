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
        <div>{products.map(product => <h1 key={product.id}>{product.name}</h1>)}</div>
    )
}

export default ProductsList