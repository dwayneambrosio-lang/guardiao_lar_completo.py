texto_gerado = chat_completion.choices[0].message.content

        # 3. Criação do Link Manual da Google Agenda (Template)
        titulo_evento = "Estudo em Família - Guardião do Lar"
        link_agenda = f"https://calendar.google.com/calendar/render?action=TEMPLATE&text={titulo_evento.replace(' ', '+')}"

        # 4. Grava o resultado num arquivo de relatório local (Temporário no GitHub)
        nome_arquivo = f"relatorio_{datetime.now().strftime('%Y-%m-%d')}.txt"
        
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            f.write(f"--- RELATÓRIO DO GUARDIÃO DA FAMÍLIA ---\n")
            f.write(f"Data: {datetime.now().strftime('%d/%m/%Y')}\n\n")
            f.write(f"TEXTO DIÁRIO GERADO:\n{texto_gerado}\n\n")
            f.write(f"LINK PARA ADICIONAR À AGENDA:\n{link_agenda}\n")

        print("====================================================")
        print(f"SUCESSO! RELATÓRIO DISPONÍVEL NO PAINEL:")
        print("====================================================")
        print(texto_gerado)
        print("====================================================")

    except Exception as e:
        print(f"Erro crítico durante a execução: {e}")

if __name__ == "__main__":
    executar_tarefa_familia()
