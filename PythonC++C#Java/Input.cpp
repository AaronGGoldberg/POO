//print ('Informe o seu nome')
//nome = input ()
//print ('informe a sua idade')
//idade = int(input())
//print (f 'Olá, seu nome é: {nome} e a sua idade é: {idade}')

#include <iostream>
#include <string> // Para usar a classe string

using namespace std;

int main() {
    string nome; // Variável para armazenar o nome
    int idade;   // Variável para armazenar a idade
    
    cout << "Informe o seu nome: ";
    getline(std::cin, nome); // Usando getline para ler o nome completo, incluindo espaços
    
    cout << "Informe a sua idade: ";
    cin >> idade; // Lê a idade como um número inteiro
    
    cout << "Olá, seu nome é: " << nome << " e a sua idade é: " << idade << std::endl;

    return 0;
}