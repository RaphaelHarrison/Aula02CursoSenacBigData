# atividade 2:calcule 4 notas de um aluno, faça a media e printe na tela

print("Digite as 4 notas dos alunos e receba sua média")
nota1 = float(input("Entre com a primeira nota: "))
nota2 = float(input("Entre com a segunda nota: "))
nota3 = float(input("Entre com a terceira nota: "))
nota4 = float(input("Entre com a quarta nota: "))

media = (nota1+nota2+nota3+nota4) / 4

print(f"A média do aluno é {media:.2f}")