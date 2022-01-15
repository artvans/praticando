'''

PYTHON - BASICO

1 - Introdução

* A linguagem de programação Python foi criada em 1991 por Guido Van Rossumem, com a
finalidade de ser uma linguagem simples e de fácil compreensão.

* A especificação da linguagem é mantida pela empresa Python
Software Foundation (PSF)

2 - variaveis


*  Variáveis são pequenos espaços de memória, utilizados para armazenar e manipular dados.

  Em Python, os tipos de dados básicos são :

     tipo inteiro (armazena números inteiros)

     tipo float (armazena números em formato decimal )

     tipo string (armazena um conjunto de caracteres).

     tipo boolean (armazena valores logico true or false)


  Cada variável pode armazenar apenas um tipo de dado a cada instante

  A atribuição de valor para uma variável pode ser feita
  utilizando o comando input(input()), que
  solicita ao usuário o valor a ser atribuído à variável


  O comando input()input(), sempre vai retornar uma s tring. Nesse caso, para retornar dados do tipo
  inteiro ou float, é preciso converter o tipo do valor lido Para isso, utiliza se o int string para
  converter para o tipo inteiro, ou float string para converter para o tipo float.

  Em python as variaveis de vem começar com letra, nao podeter espação entre as palavras, nao pode
  usar palavras reservadas do python, por convesção toda minusculas.

  ver PEP 8


3 - Strings

    * Uma string é uma sequência de caracteres simples. Na linguagem Python, as strings são utilizadas
      com aspas simples ( (''... '') ou aspas duplas (Para exibir uma string , utiliza se o comando
      print().


    * Concatenação de strings:
      Para concatenar strings, utiliza-se o operador +

    * Manipulação de strings: ver os diversos metodos

    * fatiamento de strings: string[limite inf:limite sup]
      strings começa com indice 0

4 - numeros

    Os quatro tipos numéricos simples, utilizados em Python, são:
    * números inteiros (int)
    * números longos (long)
    * números decimais (float)
    * números complexos (complex).


    A linguagem Python também possui operadores aritméticos, lógicos, de comparação

5 - listas

   Lista é um conjunto sequencial de valores, onde cada valor é identificado através de um índice.
   O primeiro valor tem índice 0. Uma lista em Python é declara da da seguinte forma:

   Nome_Lista = [ valor1, valor2, ...,valorN]
   Uma lista pode ter valores de qualquer tipo, incluindo outras listas .

6 - tuplas

    * Tupla, assim como a Lista é um conjunto sequencial de valores, onde cada valor é identificado
      através de um índice. A principal diferença entre elas é que as tuplas são imutáveis, ou seja, seus
      elementos não podem ser alterados. Dentre as utilidades das tuplas , destacam se as operações de
      empacotamento e desempacotamento de valores. Uma tupla em Python é declara da da seguinte forma:

      Nome_tupla = (valor1, valor2, ..., valorN)

7 - dicionarios

    * Dicionário é um conjunto de valores, onde cada valor é associado a uma chave de acesso.
      Um dicionário em Python é declara do da seguinte forma:

      Nome_dicionario = { chave1 : valor1,  chave2 : valor 2, chave3 : valor3,..., chaveN : valorN}

8 - estrutura de decisao

     * As estruturas de decisão permitem alterar o curso do fluxo de execução de um programa, de acordo
       com o valor (Verdadeiro/Falso) de um teste lógico. Em Python temos as seguintes estruturas de decisão

             if (se)
             if..else (se..senão)
             if..elif..else (se..senão..senão se)

9 - estrutura de repetição

    A Estrutura de repetição é utilizada para executar uma mesma sequência de comandos várias vezes.
    A repetição está associada ou a uma condição, que indica se deve continuar ou não a ou a um
    a sequência de valores, que determina quantas vezes a sequência deve ser repetida. As estruturas
    de repetição são conhecidas também como laços loops

    No laço while o trecho de código da repetição está associado a uma condição . Enquanto a condição
    tiver valor verdadeiro , o trecho é executado. Quando a condição passa a ter valor falso , a repetição
    termina.


    Sintaxe:
        while <condição>:
          <Bloco de comandos>


10 - funções

11 - biblioteca

    * As bibliotecas armazenam funções pré definidas que podem ser utilizados em qualquer momento
      do programa. Em Python muitas bibliotecas são instalad as por padrão junto com o programa. Para
      usar uma biblioteca , deve se utilizar o comando import:

      Exemplo:
          # importar a biblioteca de funções matemáticas:

                import math
                print( math.factorial(6))

          # Pode se importar uma função específica da biblioteca:

                from math import factorial
                print(factorial(6))







'''