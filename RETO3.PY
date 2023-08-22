Productos=[{'id':123,'Nombre':'Libreta','Precio':12.500,'id_cat':1},{'id':345,'Nombre':'Jabon','Precio':10.500,'id_cat':2}]
Categorias=[{'id':1,'Nombre':'Utiles Escolares'},{'id':2,'Nombre':'Aseo'}]

Resultante=[]

for producto in Productos:
    producto_id = producto['id']
    producto_nombre = producto['Nombre']
    categoria_id = producto['id_cat']
    
    for categoria in Categorias:
        if categoria['id'] == categoria_id:
            categoria_nombre = categoria['Nombre']
            break
    
    Resultante.append({
        'id': producto_id,
        'Producto': producto_nombre,
        'Categoria': categoria_nombre
    })

print(Resultante)