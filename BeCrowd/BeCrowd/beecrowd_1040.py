def result(n1, n2, n3, n4):
    sum = float((2*n1)+(3*n2)+(4*n3)+(1*n4))
    avg = float(sum/(2+3+4+1))
    print(f'Media: {avg:.1f}')
    if avg >= 7.0:
        print('Aluno aprovado.')
    elif avg < 5.0:
        print('Aluno reprovado.')
    elif avg >= 5.0 and avg <6.9:
        print('Aluno em exame.')
        n5 = float(input())
        final_result = (avg+n5)/2
        print(f'Nota do exame: {n5:.1f}')
        if final_result >= 5.0:
            print('Aluno aprovado.')
        elif final_result <= 4.9:
            print('Aluno reprovado.')
        print(f'Media final: {final_result:.1f}')
n1, n2, n3, n4 = map(float, input().split())
result(n1, n2, n3, n4)
