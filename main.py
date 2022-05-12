from crud import *

creation_object = {"nome": "Melancia", "preco": 20.00, "categoria": "frutas",
                   "marca": None, "descricao": "sem semente", "desconto": None}

update_object = {"desconto": 0.01}


crud_projects = CrudProducts()

# EXEMPLOS DE USO - CRUD PARA PRODUTOS
#crud_projects.create(creation_object)
#crud_projects.get_by_id(1)
#crud_projects.get_all()
#crud_projects.update_by_id(8, update_object)
#crud_projects.delete_by_id(8)