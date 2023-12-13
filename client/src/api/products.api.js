import axios from 'axios'

export const getAllProducts = () => {
    return axios.get('http://localhost:8000/products/api/v1/products/')
}
