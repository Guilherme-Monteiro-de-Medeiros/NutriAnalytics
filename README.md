# nutricionista
Aplicativo para um site de Nutricionista

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="/Styles/Style.css" rel="stylesheet">
    <title>Nutricionista Guilherme</title>
    <link rel="stylesheet" href="styles.css">
    
    </head>
<body>
    <!-- Cabeçalho -->
    <header>
        <img src="components/Images/Logo.webp" height="200" width="300" line-height= "15px">
        <div id="title">
            <h1>Nutricionista Guilherme Monteiro</h1>
        </div>
        
        <nav>
            <ul>
                <li><a href="#sobre">Sobre</a></li>
                <li><a href="#servicos">Serviços</a></li>
                <li><a href="#beneficios">Benefícios</a></li>
                <li><a href="#contato">Contato</a></li>
            </ul>
        </nav>
        <a href="#contato" class="cta-button">Agende sua consulta</a>
    </header>

    <!-- Faixa 1: Sobre a Nutricionista -->
    <section id="sobre" class="section">
        <div class="container">
            
            <div class="text">
                <h2>Sobre Mim</h2>
                <img src= "components/Images/foto-nutricionista.jpg" width="300px" height="200">
                <p>Olá! Me chamo Guilherme Monteiro, nutricionista com 8 anos de experiência. Meu foco é ajudar você a alcançar uma vida mais saudável através de planos alimentares personalizados e acompanhamento nutricional.</p>
            </div>
        </div>
    </section>

    <!-- Faixa 2: Serviços -->
    <section id="servicos" class="section">
        <h2>Serviços Oferecidos</h2>
        <div class="servicos-container">
            <div class="servico">
                <h3>Consultas Presenciais e Online</h3>
                <img src="components/Images/icone presencial.jpg" width="80px" height="80px" alt="Ícone Plano">
                <img src="components/Images/ícone-online.webp" width="80px" height="80px">
            </div>
            <div class="servico">
                <h3>Planos Alimentares Personalizados</h3>
                <img src="components/Images/icone plano alimentar.jpg" width="80px" height="80px">
            </div>
            <div class="servico">
                <h3>Acompanhamento Nutricional</h3>
                <img src="components/Images/Acompanhamento nutricional.webp"width="80px" height="80px">
            </div>
        </div>
    </section>

    <!-- Faixa 3: Benefícios -->
    <section id="beneficios" class="section">
        <h2>Vantagens e Benefícios</h2>
        <div class="beneficios-container">
            <div class="beneficio">
                <p>Saúde melhorada e mais energia no dia a dia.</p>
            </div>
            <div class="beneficio">
                <p>Emagrecimento saudável e sustentável.</p>
            </div>
        </div>
        <div class="depoimentos-container">
            <div class="depoimento">
                <p>"Graças ao Nutricionista Guilherme Monteiro, consegui melhorar minha alimentação e qualidade de vida!" - Fabio da Conceição</p>
            </div>
            <div class="depoimento">
                <p>"Recomendo demais! Atendimento excelente e resultados incríveis." - Raquel Pereira</p>
            </div>
        </div>
    </section>

    <!-- Faixa 4: Formulário de Contato -->
    <section id="contato" class="section">
        <h2>Entre em Contato</h2>
        <form>
            <input type="text" placeholder="Nome" required>
            <input type="email" placeholder="E-mail" required>
            <input type="tel" placeholder="Telefone" required>
            <textarea placeholder="Mensagem (opcional)"></textarea>
            <button type="submit">Enviar mensagem</button>
        </form>
    </section>
   
    <!-- Rodapé -->
    <footer>
        <div class="contato">
            <p>E-mail: guilherme.nutri@nutricionista.com</p>
            <p>Telefone: (11) 99999-9999</p>
            <p>Endereço: Rua Gaston, 123 - São Paulo, SP</p>
        </div>
        <div class="redes-sociais">
            <a href="#">
                <img src="components/Images/Insta.webp" width="80px" height="80px">
            </a>
            <a href="#">
                <img src="components/Images/Zap.webp" width="80px" height="80px">
            </a>
            <a href="#">
                <img src="components/Images/Linke.webp" width="80px" height="80px">
            </a>
        </div>
        <div class="direitos">
            <p>© 2023 Nutricionista Guilherme Monteiro. Todos os direitos reservados.</p>
        </div>
    </footer>
</body>
</html>
