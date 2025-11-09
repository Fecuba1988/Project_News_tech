1.  Crie um novo repositório público ou privado no GitHub (ex: `newsletter-tech-ia`).
2.  Faça o *upload* de todos os arquivos e pastas contidos no `news_financeira` para a raiz deste novo repositório.

### Passo 2: Configurar os Secrets do Repositório

O GitHub Actions usa **Secrets** para armazenar informações sensíveis (como chaves de API e senhas) de forma segura.

1.  No seu repositório, vá para **Settings** (Configurações).
2.  No menu lateral, clique em **Security** (Segurança) > **Secrets and variables** (Segredos e variáveis) > **Actions**.
3.  Clique em **New repository secret** (Novo segredo do repositório) e adicione os seguintes segredos, um por um:

| Nome do Secret | Descrição | Exemplo de Valor |
| :--- | :--- | :--- |
| `OPENAI_API_KEY` | Sua chave de API para o modelo GPT. | `sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` |
| `TAVILY_API_KEY` | Sua chave de API para a ferramenta de busca Tavily. | `tvly-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` |
| `EMAIL_ADDRESS` | O endereço de e-mail que enviará a newsletter (remetente). | `seu.email@gmail.com` |
| `EMAIL_PASSWORD` | A senha de aplicativo (App Password) do seu e-mail. **Importante:** Se você usa Gmail, você deve gerar uma [Senha de Aplicativo] em vez da sua senha normal. | `abcd efgh ijkl mnop` |
| `DESTINATARIOS` | A lista de e-mails dos destinatários, separados por vírgula. | `destinatario1@email.com, destinatario2@email.com` |

> **Nota sobre Senha de Aplicativo (Gmail):** Para usar o Gmail com `smtplib`, você precisa ativar a verificação em duas etapas e, em seguida, gerar uma "Senha de Aplicativo" específica para este projeto. A senha de aplicativo é usada no lugar da sua senha normal.

## 3. Como Funciona a Automação

O arquivo `.github/workflows/daily_newsletter.yml` configura a automação:

*   **Gatilho Diário (`schedule`):** O script está configurado para rodar todos os dias às **10:00 AM (UTC)**. Você pode editar o arquivo `daily_newsletter.yml` para ajustar o horário se necessário.
    ```yaml
    on:
      schedule:
        - cron: '0 10 * * *' # 10:00 AM UTC
    ```
*   **Gatilho Manual (`workflow_dispatch`):** Você pode iniciar a newsletter manualmente a qualquer momento.
    1.  No seu repositório, vá para a aba **Actions** (Ações).
    2.  Clique no workflow **Daily Newsletter** no menu lateral.
    3.  Clique no botão **Run workflow** (Executar workflow) e depois em **Run workflow** novamente.

Após a execução, você pode verificar o status e os logs do envio na mesma aba **Actions**.
