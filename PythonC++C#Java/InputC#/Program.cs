using System;

class Program
{
    static void Main()
    {
        // Solicitando o nome
        Console.Write("Informe o seu nome: ");
        string nome = Console.ReadLine();  // Lê o nome do usuário
        
        // Solicitando a idade
        Console.Write("Informe a sua idade: ");
        int idade = int.Parse(Console.ReadLine());  // Lê a idade do usuário como um inteiro
        
        // Exibindo a mensagem formatada
        Console.WriteLine($"Olá, seu nome é: {nome} e a sua idade é: {idade}");
    }
}

