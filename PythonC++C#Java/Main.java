import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Criando o scanner para leitura de dados do usuário
        Scanner scanner = new Scanner(System.in);
        
        // Solicitando o nome
        System.out.print("Informe o seu nome: ");
        String nome = scanner.nextLine();  // Lê o nome do usuário
        
        // Solicitando a idade
        System.out.print("Informe a sua idade: ");
        int idade = scanner.nextInt();  // Lê a idade do usuário como um inteiro
        
        // Exibindo a mensagem formatada
        System.out.printf("Olá, seu nome é: %s e a sua idade é: %d\n", nome, idade);
        
        // Fechar o scanner
        scanner.close();
    }
}
