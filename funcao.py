alunos = {
    "aluno1" : {
        "nome" : "jose",
        "idade" : "45"
    },
}

def inserirAluno(name,nome,idade):
    alunos.update({name : { "nome" : nome, "idade" : idade}}) 

var1 = input("insira o nome : ")
var2 = input("insira o nome do aluno: ")
var3 = input("insira a idade: ")

inserirAluno(var1,var2,var3)
print(alunos)