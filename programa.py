idade = int(input('Digite o valor numérico referente à idade: '))
f = str(input('Digite o formato da idade: (a - Anos, d - Dias)'))
esp = str(input('Digite a especialidade do paciente: (C - Cardíaco, N - Neurológico ou Nd - Nenhum)'))

if (idade <= 28 and f == 'd' and esp == 'Nd'):
    print('UTI Neonatal')
elif (idade > 28 and f == 'a' or 'd' and esp == 'Nd'):
    print('UTI Pediátrica')
elif (idade >= 20 and f == 'a' and esp == 'Nd'):
    print('UTI Adulto')
if (idade <= 28 and f == 'd' and esp == 'C'):
    print('UTI Cardíaco')
elif (idade > 28 and f == 'a' or 'd' and esp == 'C'):
    print('UTI Cardíaco')
elif (idade >= 20 and f == 'a' and esp == 'C'):
    print('UTI Cardíaco')
if (idade <= 28 and f == 'd' and esp == 'N'):
    print('UTI Neurológico')
elif (idade > 28 and f == 'a' or 'd' and esp == 'N'):
    print('UTI Neurológico')
elif (idade >= 20 and f == 'a' and esp == 'N'):
    print('UTI Neurológico')