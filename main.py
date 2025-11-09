from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
from email.message import EmailMessage
import os, smtplib
from datetime import datetime

# Carrega variáveis de ambiente
load_dotenv()
EMAIL_ADDRESS= os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
DESTINATARIOS = os.getenv("DESTINATARIOS", "")

def envia_email_tool(assunto, conteudo):
    """Envio de emails"""
    try:
        msg= EmailMessage()
        msg['Subject']= assunto
        msg['From']= EMAIL_ADDRESS
        
        # Normaliza a string, separa por vírgula e remove espaços vazios
        bcc_list = [addr.strip() for addr in DESTINATARIOS.split(',') if addr.strip()]

        # Campo To visível mínimo (pode ser o próprio remetente ou um rótulo)
        if bcc_list:
            msg['To'] = "Undisclosed recipients <{}>".format(EMAIL_ADDRESS)
            msg['Bcc'] = ', '.join(bcc_list)
        else:
            return "Erro: não há destinatários configurados em DESTINATARIOS"  
        
        msg.set_content(conteudo, charset='utf-8')

        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            
            # enviar explicitando a lista completa de endereços (To + Bcc)
            all_recipients = [EMAIL_ADDRESS] + bcc_list
            smtp.send_message(msg, to_addrs=all_recipients)
        
        return "Email enviado com sucesso!!!"

    except Exception as e:
        return f'Erro: {e}'

agente = Agent(
    model=OpenAIChat(id="gpt-4.1-mini"),
    tools=[TavilyTools(), envia_email_tool],
    debug_mode=False
)

    
if __name__ == '__main__':
    from prompt import prompt_pro_agente
    agora = datetime.now()

    print("Executando a newsletter...")

    try:
        # Adiciona a data atual ao prompt
        prompt_data = f"DATA: {agora:%d/%m/%y}\n\n {prompt_pro_agente}"
        agente.run(prompt_data)
        print("Newsletter enviada!!!")
    
    except Exception as e:
        print(f"Erro: {e}")
        # O script falhará, o que é desejável para que o GitHub Actions reporte o erro.
        exit(1)
