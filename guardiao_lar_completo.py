import os
from datetime import datetime
from groq import Groq

def executar_tarefa_familia():
    print(f"\n[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] Iniciando a tarefa da família na nuvem...")

    try:
        # Busca a chave de forma segura direto do cofre do GitHub
        api_key = os.environ.get("GROQ_API_KEY")
        if not api_key:
            raise ValueError("A chave GROQ_API_KEY nao foi encontrada nos Secrets do GitHub!")

        client = Groq(api_key=api_key)

        prompt_comando = (
            "Gere uma mensagem curta, poderosa e inspiradora de liderança familiar "
            "e incentivo espiritual para o dia de hoje. Inclua uma calorosa exortação "
            "para a leitura do texto diário e estudo em família na JW Library ou JW.ORG."
        )

        print("Chamando a API da Groq para gerar o texto...")
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt_comando}],
            model="llama-3.1-8b-instant",
        )

        texto_gerado = chat_completion.choices[0].message.content

        titulo_evento = "Estudo em Família - Guardião do Lar"
        link_agenda = f"https://calendar.google.com/calendar/render?action=TEMPLATE&text={titulo_evento.replace(' ', '+')}"

        nome_arquivo = f"relatorio_{datetime.now().strftime('%Y-%m-%d')}.txt"
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            f.write(f"--- RELATÓRIO DO GUARDIÃO DA FAMÍLIA ---\n")
            f.write(f"Data: {datetime.now().strftime('%d/%m/%Y')}\n\n")
            f.write(f"TEXTO DIÁRIO GERADO:\n{texto_gerado}\n\n")
            f.write(f"LINK PARA ADICIONAR À AGENDA:\n{link_agenda}\n")

        print("====================================================")
        print("SUCESSO! RELATÓRIO DISPONÍVEL NO PAINEL:")
        print("====================================================")
        print(texto_gerado)
        print("====================================================")

    except Exception as e:
        print(f"Erro crítico durante a execução: {e}")

if __name__ == "__main__":
    executar_tarefa_familia()
