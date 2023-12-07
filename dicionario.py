"""
cliente = { 
    "nome" : "Jose",
    "idade" : "45anos",
    "email" : "zevolpato@gmail.com"
}

#print(type(cliente))
#print(cliente)
print(cliente["nome"])
#cliente["nome"] = "Joao" # troquei o nome
cliente.update({ "nome" : "maria"})
print(cliente["nome"])
cliente.update({"cpf" : "12312312312"})
print(cliente)

aluno = {
    "nome" : "mateus",
    "email" : "mateus@gmail.com",
    "fone" : ["12983213232","12987676765"],
    "cursos" : ["Tecnico em internet", "Python"]
}
aluno["cursos"][1] = "Python Fundamentos"

print(aluno["cursos"][1].upper())

#Qual é o segundo cursos que o mateus faz?
"""
alunos = {
        "aluno1" : { 
            "nome" : "mateus",
            "email" : "mateus@gmail.com",
            "fone" : ["12983213232","12987676765"],
            "cursos" : ["Tecnico em internet", "Python"]
        },
        "aluno2": {
            "nome" : "mateus2",
            "email" : "mateus@gmail.com",
            "fone" : ["12983213232","12987676765"],
            "cursos" : ["Tecnico em internet", "Python"]
        }
}
alunos["aluno2"]["nome"] = "ze"
print(type(alunos))
print(alunos)



#aluno["cursos"][1] = "Python Fundamentos"

#print(aluno["cursos"][1].upper())