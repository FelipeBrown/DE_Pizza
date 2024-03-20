from pizza import Pizza

print("INGREDIENTES:")
print("Ingredientes carne:", Pizza.ingredientes_carne)
print("Ingredientes vegetales:", Pizza.ingredientes_vegetales)
print("Tipos de masa:", Pizza.tipos_masa)

print("\n¿Tenemos disponible ['salsa de tomate', 'salsa bbq']?")
print(Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

mi_pedido = Pizza()
mi_pedido.hacer_pedido()

print("\nIngredientes de la pizza:")
print("Ingrediente proteico:", mi_pedido.ingrediente_proteico)
print("Primer ingrediente vegetal:", mi_pedido.primer_ingrediente_vegetal)
print("Segundo ingrediente vegetal:", mi_pedido.segundo_ingrediente_vegetal)
print("Tipo de masa:", mi_pedido.tipo_masa)
print("¿Es válida la pizza?", mi_pedido.es_valida)