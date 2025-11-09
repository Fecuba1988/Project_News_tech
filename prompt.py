prompt_pro_agente = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Newsletter Tech & AI</title>
  <style>
    body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
    h2 { font-size: 1.4em; margin-top: 30px; }
    h2 span { font-size: 1.6em; }
    strong { font-weight: bold; }
    ul { margin: 0; padding-left: 20px; }
    li { margin-bottom: 8px; }
    .section { border-top: 2px solid #ccc; padding-top: 15px; margin-top: 20px; }
  </style>
</head>
<body>

  <h1>📧 <strong>NEWSLETTER TECH & AI | Edição [DATA]</strong></h1>

  <p>Olá, inovador(a)! 🤖</p>
  <p>Chegou sua dose diária de insights sobre Inteligência Artificial e tecnologia aplicada aos negócios.<br>
  Aqui estão as novidades, tendências e oportunidades que estão moldando o futuro do trabalho e da inovação.</p>

  <div class="section">
    <h2><span>🚀</span> <strong>DESTAQUES DO DIA</strong></h2>
    <ul>
      <li><strong>[Manchete 1 atraente]</strong></li>
      <li><strong>[Manchete 2 atraente]</strong></li>
      <li><strong>[Manchete 3 atraente]</strong></li>
      <li><strong>[Manchete 4 atraente]</strong></li>
    </ul>
  </div>

  <div class="section">
    <h2><span>🧠</span> <strong>TENDÊNCIAS E AVANÇOS EM INTELIGÊNCIA ARTIFICIAL</strong></h2>
    <p><strong>Resumo:</strong> [Principais novidades em modelos de IA, pesquisas, lançamentos e impacto regulatório.]</p>
    <p><strong>Principais Notícias:</strong></p>
    <ul>
      <li><strong>[Manchete curta]</strong> - Resumo (até 3 linhas) - Fonte: [nome] - <a href="[URL COMPLETA]">[URL COMPLETA]</a></li>
      <li><strong>[Manchete curta]</strong> - Resumo (até 3 linhas) - Fonte: [nome] - <a href="[URL COMPLETA]">[URL COMPLETA]</a></li>
      <li><strong>[Manchete curta]</strong> - Resumo (até 3 linhas) - Fonte: [nome] - <a href="[URL COMPLETA]">[URL COMPLETA]</a></li>
    </ul>
  </div>

  <div class="section">
    <h2><span>🏦</span> <strong>IA NOS NEGÓCIOS E MERCADO CORPORATIVO</strong></h2>
    <p><strong>Resumo:</strong> [Como empresas aplicam IA em marketing, finanças, RH, operações bancárias e atendimento; cases e ROI.]</p>
    <p><strong>Casos e Implementações:</strong></p>
    <ul>
      <li><strong>[Título do case]</strong> - Resumo (até 3 linhas) - Fonte: [nome] - <a href="[URL COMPLETA]">[URL COMPLETA]</a></li>
      <li><strong>[Título do case]</strong> - Resumo (até 3 linhas) - Fonte: [nome] - <a href="[URL COMPLETA]">[URL COMPLETA]</a></li>
      <li><strong>[Título do case]</strong> - Resumo (até 3 linhas) - Fonte: [nome] - <a href="[URL COMPLETA]">[URL COMPLETA]</a></li>
      <li><strong>[Título do case]</strong> - Resumo (até 3 linhas) - Fonte: [nome] - <a href="[URL COMPLETA]">[URL COMPLETA]</a></li>
    </ul>
  </div>

  <div class="section">
    <h2><span>🎓</span> <strong>CURSOS, FERRAMENTAS E RECURSOS DE APRENDIZADO</strong></h2>
    <p><strong>Resumo:</strong> [Principais cursos, certificações, webinars, ferramentas e plataformas de IA e automação.]</p>
    <p><strong>Destaques da Semana:</strong></p>
    <ul>
      <li><strong>[Curso/Ferramenta]</strong> - Breve descrição (até 3 linhas) - Fonte: [nome] - <a href="[URL COMPLETA]">[URL COMPLETA]</a></li>
      <li><strong>[Curso/Ferramenta]</strong> - Breve descrição (até 3 linhas) - Fonte: [nome] - <a href="[URL COMPLETA]">[URL COMPLETA]</a></li>
      <li><strong>[Curso/Ferramenta]</strong> - Breve descrição (até 3 linhas) - Fonte: [nome] - <a href="[URL COMPLETA]">[URL COMPLETA]</a></li>
      <li><strong>[Curso/Ferramenta]</strong> - Breve descrição (até 3 linhas) - Fonte: [nome] - <a href="[URL COMPLETA]">[URL COMPLETA]</a></li>
    </ul>
  </div>

  <div class="section">
    <h2><span>📈</span> <strong>MERCADO DE TRABALHO E OPORTUNIDADES</strong></h2>
    <p><strong>Resumo:</strong> [Tendências em vagas, salários, novas funções com IA e perfis mais buscados.]</p>
    <p><strong>Notícias e Insights:</strong></p>
    <ul>
      <li><strong>[Título]</strong> - Resumo (até 3 linhas) - Fonte: [nome] - <a href="[URL COMPLETA]">[URL COMPLETA]</a></li>
      <li><strong>[Título]</strong> - Resumo (até 3 linhas) - Fonte: [nome] - <a href="[URL COMPLETA]">[URL COMPLETA]</a></li>
      <li><strong>[Título]</strong> - Resumo (até 3 linhas) - Fonte: [nome] - <a href="[URL COMPLETA]">[URL COMPLETA]</a></li>
    </ul>
  </div>

  <div class="section">
    <h2><span>🎯</span> <strong>OPORTUNIDADES E INSIGHTS PRÁTICOS</strong></h2>
    <ul>
      <li><strong>Recomendação 1:</strong> [Ação clara e rápida] — <strong>Risco:</strong> [breve]</li>
      <li><strong>Recomendação 2:</strong> [Ação clara e rápida] — <strong>Risco:</strong> [breve]</li>
      <li><strong>Recomendação 3:</strong> [Ação clara e rápida] — <strong>Risco:</strong> [breve]</li>
    </ul>
  </div>

  <div class="section">
    <h2><span>📊</span> <strong>DADOS E INDICADORES DO SETOR</strong></h2>
    <ul>
      <li><strong>Investimentos globais em IA (últimos 30 dias):</strong> US$ X,XX bi — Fonte: [nome] - <a href="[URL COMPLETA]">[URL COMPLETA]</a></li>
      <li><strong>Startups de IA no Brasil:</strong> X empresas — Fonte: [nome] - <a href="[URL COMPLETA]">[URL COMPLETA]</a></li>
      <li><strong>Principais tendências de busca em IA:</strong> [lista curta] — Fonte: [nome] - <a href="[URL COMPLETA]">[URL COMPLETA]</a></li>
      <li><strong>Regulamentação e marcos legais:</strong> [Resumo breve] — Fonte: [nome] - <a href="[URL COMPLETA]">[URL COMPLETA]</a></li>
    </ul>
  </div>

  <p>🤝 <strong>ATÉ A PRÓXIMA!</strong></p>
  <p>👥 Newsletter Tech & AI — NEWSTECH</p>

</body>
</html>
"""
