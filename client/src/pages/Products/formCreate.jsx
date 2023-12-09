import { useForm, Form } from 'react-hook-form'

function Select() {
    return <select>
        <option value="0">Sin descuento</option>
        <option value="5">%5</option>
        <option value="10">%10</option>
        <option value="15">%15</option>
        <option value="20">%20</option>
        <option value="25">%25</option>
        <option value="30">%30</option>
        <option value="35">%35</option>
        <option value="40">%40</option>
        <option value="45">%45</option>
        <option value="50">%50</option>
        <option value="60">%60</option>
    </select>
}

function FormCreate() {
    const { register, handleSubmit, formState: { errors } } = useForm()

    return <form action='http://localhost:8000/api/products/' method='post' >
        <label htmlFor="name">Nombre Producto</label>
        <input type="text" {...register('name', {
            required: { value: true, message: 'El nombre del producto es requerido' },
            minLength: { value: 5, message: 'El nombre es demasiado corto, 5 caracteres como mínimo' },
            maxLength: { value: 100, message: 'El nombre es demasiado largo, 100 caracteres máximo' }
        })} />
        {errors.name && <span>{errors.name.message}</span>}
        <label htmlFor="description">Descripción</label>
        <textarea cols="30" rows="10" {...register('description', {
            required: { value: true, message: 'Escribe una descripción del producto' },
            minLength: { value: 25, message: 'Descripción demasiado corta, 25 caracteres mínimo' }
        })} >
        </textarea>
        {errors.description && <span>{errors.description.message}</span>}
        <label htmlFor="price">Precio</label>
        <input type="number" {...register('price', {
            required: { value: true, message: 'El precio del producto es obligatorio' },
            min: { value: 990, message: 'El precio es muy bajo' }
        })} />
        {errors.price && <span>{errors.price.message}</span>}
        <label htmlFor="stock">Stock Disponible</label>
        <input type="number" defaultValue={0} {...register('stock', {
            required: { value: true, message: 'El stock del producto es obligatorio' },
        })} />
        {errors.stock && <span>{errors.stock.message}</span>}
        <label htmlFor="discount">Descuento</label>
        <Select />
        <input type="submit" value="Crear Producto" />
    </form>
}

export default FormCreate