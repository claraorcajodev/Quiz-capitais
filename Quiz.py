import random
import os

# Lista de perguntas do quiz, com estrutura de dados aprimorada.
questions = [
    {
        "question": "Qual é a capital da França?",
        "options": ["Paris", "Londres", "Berlim", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Qual é a capital do Japão?",
        "options": ["Seul", "Tóquio", "Pequim", "Bangkok"],
        "answer": "Tóquio"
    },
    {
        "question": "Qual é a capital do Brasil?",
        "options": ["Brasília", "Rio de Janeiro", "São Paulo", "Salvador"],
        "answer": "Brasília"
    },
    {
        "question": "Qual é a capital da Itália?",
        "options": ["Roma", "Milão", "Veneza", "Florença"],
        "answer": "Roma"
    },
    {
        "question": "Qual é a capital da Austrália?",
        "options": ["Sydney", "Melbourne", "Canberra", "Brisbane"],
        "answer": "Canberra"
    }
]

def print_separator(char="=", length=50):
    """Imprime uma linha separadora para organizar a interface."""
    print(char * length)

def clear_screen():
    """Função para limpar a tela do terminal (funciona em Windows, Mac e Linux)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def ask_question(question_data):
    """Exibe uma única pergunta com formatação visual e valida a resposta."""
    print_separator()
    print(f"  {question_data['question']}\n")

    correct_answer_text = question_data["answer"]
    shuffled_options = question_data["options"][:]
    random.shuffle(shuffled_options)

    answer_letters = ["A", "B", "C", "D"]
    for i, option in enumerate(shuffled_options):
        print(f"  {answer_letters[i]}) {option}")

    print() # Linha em branco para criar espaço antes da divisória
    print_separator()

    while True:
        user_answer = input("\n  >> Sua resposta (A, B, C ou D): ").strip().upper()
        if user_answer in answer_letters:
            break
        else:
            print("  Resposta inválida. Por favor, escolha uma das opções.")

    is_correct = (user_answer == answer_letters[shuffled_options.index(correct_answer_text)])
    
    return is_correct, user_answer, correct_answer_text

def main():
    """Função principal que executa o fluxo do quiz com visual melhorado."""
    clear_screen()
    
    # --- Banner de Boas-Vindas ---
    print_separator("*", 50)
    print("      Bem-vindo ao Quiz de Capitais do Mundo!")
    print_separator("*", 50)
    input("\nPressione Enter para começar...")
    
    score = 0
    user_answers = []

    random.shuffle(questions)

    for q_data in questions:
        clear_screen()
        is_correct, user_answer_letter, correct_answer_text = ask_question(q_data)
        
        user_answers.append({
            "question": q_data["question"],
            "user_choice": user_answer_letter,
            "correct_answer": correct_answer_text,
            "is_correct": is_correct
        })

        if is_correct:
            print("\n  ✨ Resposta Correta! ✨\n")
        else:
            print(f"\n  ❌ Resposta Errada! A resposta correta era: {correct_answer_text}.\n")
        
        print_separator()
        # Adicionado \n para criar espaço antes do input
        input("\nPressione Enter para a próxima pergunta...")
        
    # --- Tela Final com Resumo ---
    clear_screen()
    print_separator("*", 50)
    print("                   FIM DE JOGO")
    print_separator("*", 50)
    
    print(f"\n  Sua pontuação final: {score} de {len(questions)} acertos.\n")

    print("--- Resumo das suas respostas ---\n")
    for result in user_answers:
        status = "✅ Correto" if result['is_correct'] else f"❌ Incorreto"
        
        print_separator("-", 40)
        print(f"  Pergunta: {result['question']}")
        print(f"  Sua escolha: {result['user_choice']} | Status: {status}")
        if not result['is_correct']:
            print(f"  Resposta Certa: {result['correct_answer']}")

    print_separator("-", 40)
    input("\n\nPressione Enter para fechar o programa...")

# Garante que a função main() só seja executada quando o script é rodado diretamente.
if __name__ == "__main__":
    main()