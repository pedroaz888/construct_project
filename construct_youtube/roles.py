from rolepermissions.roles import AbstractUserRole

class Gerente(AbstractUserRole):
    available_permissinos ={
        'cadastrar_produtos': True,
        'liberar_descontos': True,
        'cadastrar_vendedor': True,
        'excluir_vendedor': True,

    }

class Vendedor(AbstractUserRole):
    available_permissions = {
        'realizar_vendas': True,
        'cadastrar_produtos':True,

    }