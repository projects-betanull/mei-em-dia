import os, datetime, html
OUT=".."; CHECKOUT="https://pay.kiwify.com.br/IJghjr7"; BASE="https://projects-betanull.github.io/mei-em-dia"
SITE="MEI em Dia"; HOJE=datetime.date.today().isoformat()
CSS="""*{box-sizing:border-box}body{margin:0;font-family:system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif;color:#1f2937;line-height:1.65;background:#fafaf9}
header{background:#1f6f5c;color:#fff;padding:14px 20px}header a{color:#fff;text-decoration:none;font-weight:700;font-size:1.15rem}
main{max-width:760px;margin:0 auto;padding:24px 20px 60px}h1{font-size:1.9rem;line-height:1.25;margin:.4em 0}h2{margin-top:1.8em;color:#1f6f5c}
a{color:#1f6f5c}.cta{background:#e3f1ec;border:1px solid #b7dccd;border-radius:12px;padding:20px;margin:32px 0}
.cta strong{font-size:1.1rem}.btn{display:inline-block;background:#1f6f5c;color:#fff!important;padding:12px 22px;border-radius:8px;text-decoration:none;font-weight:700;margin-top:10px}
table{border-collapse:collapse;width:100%;margin:16px 0}td,th{border:1px solid #d1d5db;padding:8px;text-align:left}th{background:#f3f4f6}
.lista a{display:block;padding:14px 0;border-bottom:1px solid #e5e7eb;font-weight:600;text-decoration:none}.lista span{display:block;font-weight:400;color:#6b7280;font-size:.95rem}
footer{text-align:center;color:#6b7280;font-size:.85rem;padding:30px 20px;border-top:1px solid #e5e7eb}.aviso{font-size:.85rem;color:#6b7280}"""
CHECKOUT2="https://pay.kiwify.com.br/YThmb2o"
def cta(prod="mei"):
    if prod=="fin": return f"""<div class="cta" style="background:#e8ebf7;border-color:#c5cbeb"><strong>Planilha Financeira Pessoal 2027: faça isso no automático</strong>
<p>Orçamento por categoria com alerta quando estoura, controle de dívidas, metas de economia e painel com gráficos. Funciona no Excel e no Google Planilhas.</p>
<a class="btn" style="background:#3b4a9c" href="{CHECKOUT2}" rel="nofollow">Quero a planilha por R$ 24,90</a></div>"""
    return f"""<div class="cta"><strong>Planilha MEI 2027: controle tudo isso automaticamente</strong>
<p>Relatório mensal pronto para imprimir, alerta do limite de R$ 81 mil, controle do DAS e valores da DASN-SIMEI calculados. Funciona no Excel e no Google Planilhas.</p>
<a class="btn" href="{CHECKOUT}" rel="nofollow">Quero a planilha por R$ 29,90</a></div>"""
def page(slug,title,desc,body,article=True):
    url=f"{BASE}/{slug}" if slug else f"{BASE}/"
    ld=f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"{html.escape(title)}","dateModified":"{HOJE}","publisher":{{"@type":"Organization","name":"{SITE}"}}}}</script>' if article else ""
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="google-site-verification" content="w_NTN5a5cFI9a-yrtXuVR_EZzN4_bGfdlxHHK1rwZHU"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}"><link rel="canonical" href="{url}">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:type" content="article">
<style>{CSS}</style>{ld}</head><body><header><a href="{BASE}/">{SITE}</a></header><main>{body}</main>
<footer>{SITE} — guias práticos para o Microempreendedor Individual.<br>Conteúdo informativo; confirme sempre no Portal do Empreendedor (gov.br/mei) ou com um contador.</footer></body></html>"""

A=[]
A.append(("limite-mei-2027","Limite do MEI em 2027: quanto pode faturar e o que acontece se passar",
"Entenda o limite de faturamento do MEI, o cálculo proporcional para quem abriu no meio do ano e a regra dos 20% de excesso.",
"""<h1>Limite do MEI em 2027: quanto pode faturar e o que acontece se passar</h1>
<p>O limite de faturamento do MEI é de <strong>R$ 81.000 por ano</strong>, valor em vigor desde 2018. Existem projetos no Congresso para aumentar esse teto, mas enquanto nenhum for aprovado e sancionado, vale o valor atual.</p>
<h2>Existe limite mensal?</h2>
<p>Não. O controle é anual. A média de <strong>R$ 6.750 por mês</strong> é só uma referência: você pode faturar R$ 10 mil em dezembro e R$ 3 mil em fevereiro, desde que a soma do ano não passe do limite.</p>
<h2>Limite proporcional no ano de abertura</h2>
<p>Quem abre o MEI durante o ano tem limite proporcional: <strong>R$ 6.750 multiplicado pelo número de meses de atividade</strong>, contando o mês de abertura.</p>
<table><tr><th>Mês de abertura</th><th>Meses</th><th>Limite no ano</th></tr>
<tr><td>Janeiro</td><td>12</td><td>R$ 81.000</td></tr><tr><td>Abril</td><td>9</td><td>R$ 60.750</td></tr>
<tr><td>Julho</td><td>6</td><td>R$ 40.500</td></tr><tr><td>Outubro</td><td>3</td><td>R$ 20.250</td></tr></table>
<h2>Passei do limite. E agora?</h2>
<p><strong>Excesso de até 20%</strong> (até R$ 97.200 no ano cheio): você continua MEI até dezembro, paga um DAS complementar sobre o valor que passou e, a partir de janeiro, vira Microempresa (ME).</p>
<p><strong>Excesso acima de 20%</strong>: o desenquadramento é retroativo a janeiro do ano em que passou. Os impostos de todo o ano são recalculados como ME, com juros e multa. É o cenário mais caro, e o motivo de acompanhar o faturamento mês a mês.</p>
<h2>O que entra no cálculo</h2>
<p>Conta o <strong>faturamento bruto</strong>: tudo o que você recebeu com vendas e serviços, com ou sem nota fiscal, sem descontar despesas. Por isso o controle precisa somar todas as entradas, não só as notas emitidas.</p>
<h2>Como não ser pego de surpresa</h2>
<ul><li>Lance cada receita assim que ela entrar.</li><li>Confira todo mês quanto do limite já foi usado.</li><li>Ao passar de 80% do limite, planeje os meses seguintes ou converse com um contador sobre virar ME.</li></ul>
"""))
A.append(("relatorio-mensal-de-receitas-brutas-mei","Relatório Mensal de Receitas Brutas do MEI: o que é e como preencher",
"O que é o relatório mensal de receitas brutas, quem precisa fazer, prazo, como preencher cada campo e por quanto tempo guardar.",
"""<h1>Relatório Mensal de Receitas Brutas do MEI: o que é e como preencher</h1>
<p>O Relatório Mensal de Receitas Brutas é um resumo de tudo o que o MEI faturou no mês. É obrigatório para todo MEI, mas <strong>não é enviado ao governo</strong>: você preenche, assina e guarda, junto com as notas fiscais de compras e de vendas do mês.</p>
<h2>Prazo</h2>
<p>O relatório de cada mês deve ser preenchido até o <strong>dia 20 do mês seguinte</strong>. Guarde os relatórios e as notas por <strong>5 anos</strong>: em caso de fiscalização, eles são a prova do seu faturamento.</p>
<h2>Como o relatório é dividido</h2>
<p>São três blocos, um para cada tipo de receita. Em cada bloco você informa quanto recebeu com nota fiscal e sem nota fiscal:</p>
<table><tr><th>Bloco</th><th>Para quem</th></tr>
<tr><td>Revenda de mercadorias (comércio)</td><td>Quem compra e revende produtos</td></tr>
<tr><td>Venda de produtos industrializados (indústria)</td><td>Quem fabrica o que vende</td></tr>
<tr><td>Prestação de serviços</td><td>Quem vende serviços</td></tr></table>
<p>No final vem o <strong>total geral do mês</strong>, que é a soma dos três blocos. Se você só presta serviços, deixa os outros zerados.</p>
<h2>Com ou sem nota fiscal?</h2>
<p>Hoje o MEI não precisa emitir nota fiscal quando vende para pessoa física (consumidor final), a não ser que o cliente peça. Para empresas (CNPJ), a nota é obrigatória. Na prestação de serviços, a nota é a NFS-e no padrão nacional. Mesmo sem nota, a receita entra no relatório e conta para o limite anual. Atenção: a Reforma Tributária prevê ampliar a exigência de nota a partir de 2027 (veja o <a href="https://projects-betanull.github.io/mei-em-dia/nota-fiscal-mei/">guia de nota fiscal</a>).</p>
<h2>Erros comuns</h2>
<ul><li>Lançar só o que teve nota e esquecer as vendas em dinheiro ou Pix.</li><li>Descontar despesas: o relatório é de receita <em>bruta</em>.</li><li>Deixar para preencher tudo em maio, na hora da declaração anual.</li></ul>
"""))
A.append(("das-mei-valor-vencimento","DAS MEI: valor, vencimento e o que acontece se atrasar",
"Como é calculado o DAS do MEI, quando vence, como pagar e o que acontece se você atrasar ou deixar de pagar.",
"""<h1>DAS MEI: valor, vencimento e o que acontece se atrasar</h1>
<p>O DAS (Documento de Arrecadação do Simples Nacional) é o imposto mensal fixo do MEI. Ele é pago mesmo nos meses sem faturamento.</p>
<h2>Quanto custa</h2>
<p>O valor é a soma de três partes:</p>
<ul><li><strong>INSS:</strong> 5% do salário mínimo vigente. Garante aposentadoria, auxílio-doença e salário-maternidade.</li>
<li><strong>ICMS: R$ 1</strong>, para comércio e indústria.</li><li><strong>ISS: R$ 5</strong>, para serviços.</li></ul>
<p>Com o salário mínimo de 2026 (R$ 1.621), a parte do INSS é de R$ 81,05. Os valores mensais ficam assim:</p>
<table><tr><th>Atividade</th><th>DAS 2026</th></tr><tr><td>Comércio e indústria</td><td>R$ 82,05</td></tr>
<tr><td>Serviços</td><td>R$ 86,05</td></tr><tr><td>Comércio e serviços</td><td>R$ 87,05</td></tr></table>
<p>Como depende do salário mínimo, o DAS muda todo ano: o valor novo vale a partir da guia de janeiro (paga em fevereiro). Confira sempre o valor exato no Portal do Empreendedor ou no app MEI.</p>
<h2>Vencimento</h2>
<p>O DAS vence no <strong>dia 20 de cada mês</strong> e se refere ao mês anterior. Exemplo: o DAS de março vence em 20 de abril. Se cair em fim de semana ou feriado, o prazo passa para o dia útil seguinte.</p>
<h2>Como pagar</h2>
<p>Gere a guia no Portal do Empreendedor (gov.br/mei) ou no app MEI e pague por Pix, boleto ou débito automático.</p>
<h2>E se atrasar?</h2>
<ul><li>Multa de 0,33% por dia de atraso, limitada a 20%, mais juros Selic.</li><li>O tempo sem pagamento não conta para os benefícios do INSS.</li>
<li>Dívidas acumuladas podem ir para a Dívida Ativa e o CNPJ pode ser cancelado.</li></ul>
<p>Se tiver guias atrasadas, é possível parcelar a dívida pelo próprio portal.</p>
"""))
A.append(("dasn-simei-declaracao-anual-mei","DASN-SIMEI: como fazer a declaração anual do MEI sem erro",
"Prazo da DASN-SIMEI, quais valores informar, multa por atraso e como deixar os números prontos ao longo do ano.",
"""<h1>DASN-SIMEI: como fazer a declaração anual do MEI sem erro</h1>
<p>A DASN-SIMEI é a declaração anual do MEI. Nela você informa quanto faturou no ano anterior. Mesmo quem não faturou nada precisa entregar.</p>
<h2>Prazo</h2>
<p>Até <strong>31 de maio</strong> de cada ano, referente ao ano anterior. A entrega é feita no Portal do Empreendedor (gov.br/mei).</p>
<h2>O que você vai informar</h2>
<table><tr><th>Campo</th><th>De onde vem</th></tr>
<tr><td>Receita bruta total do ano</td><td>Soma dos 12 relatórios mensais</td></tr>
<tr><td>Parte de comércio e indústria</td><td>Blocos de revenda e indústria</td></tr>
<tr><td>Parte de serviços</td><td>Bloco de prestação de serviços</td></tr>
<tr><td>Teve empregado?</td><td>Sim ou Não</td></tr></table>
<p>Quem preencheu os relatórios mensais em dia já tem tudo pronto: é só somar.</p>
<h2>Multa por atraso</h2>
<p>A entrega fora do prazo gera multa de 2% ao mês sobre os impostos do período, com <strong>mínimo de R$ 50</strong> (com desconto se pagar logo). Também bloqueia a emissão das guias DAS até a declaração ser entregue.</p>
<h2>Erros que mais acontecem</h2>
<ul><li>Informar só o valor das notas emitidas.</li><li>Informar o lucro em vez do faturamento bruto.</li><li>Misturar receitas de comércio e de serviços.</li></ul>
"""))
A.append(("nota-fiscal-mei","Nota fiscal MEI: quando é obrigatória e como emitir (e o que muda em 2027)",
"Quando o MEI precisa emitir nota fiscal, a diferença entre NFS-e e NF-e, como emitir pelo emissor nacional e a mudança prevista para 2027.",
"""<h1>Nota fiscal MEI: quando é obrigatória e como emitir (e o que muda em 2027)</h1>
<p>Nota fiscal é uma das maiores dúvidas de quem é MEI. A regra geral é simples, mas existe uma mudança importante prevista para 2027 que vale acompanhar desde já.</p>
<h2>Quando a nota é obrigatória hoje</h2>
<table><tr><th>Situação</th><th>Nota fiscal</th></tr>
<tr><td>Venda ou serviço para empresa (CNPJ)</td><td>Obrigatória</td></tr>
<tr><td>Venda ou serviço para órgão público</td><td>Obrigatória</td></tr>
<tr><td>Venda ou serviço para pessoa física (CPF)</td><td>Só se o cliente pedir</td></tr></table>
<p>Mesmo quando a nota não é obrigatória, o valor recebido conta como faturamento e entra no relatório mensal e no limite anual de R$ 81 mil.</p>
<h2>NFS-e ou NF-e?</h2>
<ul><li><strong>NFS-e (serviços):</strong> o MEI prestador de serviços emite pelo <strong>Emissor Nacional da NFS-e</strong> (site nfse.gov.br ou app NFS-e Mobile), com login gov.br. É gratuito.</li>
<li><strong>NF-e (produtos):</strong> quem vende mercadorias emite a nota de produto, que depende de credenciamento na Secretaria da Fazenda do seu estado e de um sistema emissor autorizado.</li></ul>
<p>Quem vende produtos e serviços pode precisar dos dois tipos.</p>
<h2>Como emitir a NFS-e, passo a passo</h2>
<ol><li>Acesse o Emissor Nacional com sua conta gov.br (nível prata ou ouro).</li>
<li>No primeiro acesso, confira os dados do seu CNPJ.</li>
<li>Clique em emitir nota e informe os dados do cliente (CPF ou CNPJ).</li>
<li>Escolha o código do serviço que corresponde ao que você fez, descreva o serviço e informe o valor.</li>
<li>Confira tudo e emita. O PDF e o XML ficam salvos no sistema.</li></ol>
<p>Dica: cadastre como favoritos os clientes e serviços que se repetem. A emissão cai para menos de um minuto.</p>
<h2>O que muda em 2027</h2>
<p>Com a Reforma Tributária, o cronograma em discussão prevê que a emissão de nota fiscal passe a ser exigida em praticamente todas as operações do MEI, inclusive vendas e serviços para pessoa física, a partir de 2027. As regras finais ainda podem ser ajustadas, então acompanhe pelo Portal do Empreendedor. Na prática, quem já se acostumar a emitir nota em toda venda e a registrar tudo no controle mensal vai sentir muito menos a mudança.</p>
<h2>Erros comuns</h2>
<ul><li>Não emitir para empresas por achar que é opcional.</li><li>Usar um código de serviço que não corresponde à atividade.</li>
<li>Lançar no controle só o que teve nota e esquecer vendas por Pix ou dinheiro.</li></ul>
"""))
A.append(("mei-pode-ter-funcionario","MEI pode ter funcionário? Regras, custo e como contratar",
"Quantos funcionários o MEI pode ter, qual salário pode pagar, encargos de 3% de INSS e 8% de FGTS e quanto custa contratar em 2026.",
"""<h1>MEI pode ter funcionário? Regras, custo e como contratar</h1>
<p>Sim. O MEI pode contratar <strong>um único funcionário</strong> com carteira assinada (Lei Complementar 123/2006, art. 18-C). Mas há regras de salário e encargos que precisam caber no seu caixa.</p>
<h2>As regras</h2>
<ul><li><strong>Apenas 1 empregado.</strong> Contratar o segundo tira a empresa do MEI.</li>
<li><strong>Salário:</strong> o salário mínimo nacional ou o piso da categoria profissional.</li>
<li>O funcionário tem todos os direitos da CLT: férias com 1/3, 13º, FGTS, vale-transporte, aviso prévio.</li>
<li>O registro é feito pelo <strong>eSocial</strong> (módulo simplificado), antes de a pessoa começar a trabalhar.</li></ul>
<h2>Quanto custa por mês</h2>
<p>Sobre o salário, o MEI paga <strong>3% de INSS patronal</strong> e <strong>8% de FGTS</strong>. Os dois são pagos em uma guia única gerada pelo eSocial (DAE). Exemplo com o salário mínimo de 2026 (R$ 1.621):</p>
<table><tr><th>Item</th><th>Valor mensal</th></tr>
<tr><td>Salário</td><td>R$ 1.621,00</td></tr><tr><td>INSS patronal (3%)</td><td>R$ 48,63</td></tr>
<tr><td>FGTS (8%)</td><td>R$ 129,68</td></tr><tr><td><strong>Total direto</strong></td><td><strong>R$ 1.799,31</strong></td></tr></table>
<p>O INSS do próprio empregado (7,5% na faixa do salário mínimo) é descontado do salário dele, não é custo extra seu.</p>
<h2>O custo que muita gente esquece</h2>
<p>Além do mês a mês, separe todo mês uma reserva para 13º salário, férias com 1/3 e o FGTS sobre eles. Na prática, isso acrescenta cerca de <strong>20% a 25%</strong> ao custo. Considere também vale-transporte e uma provisão para a multa de 40% do FGTS em caso de demissão sem justa causa.</p>
<h2>Vale a pena contratar?</h2>
<p>Faça a conta com seus números: o funcionário precisa gerar mais lucro do que custa. Se seu lucro médio mensal for de R$ 3 mil, por exemplo, um custo total perto de R$ 2.200 consome quase tudo. Olhe o lucro dos últimos meses, não só o faturamento.</p>
<p>Lembre também do limite de R$ 81 mil por ano: crescer com funcionário costuma aproximar o MEI do teto. Se isso for acontecer, vale conversar com um contador sobre virar Microempresa.</p>
"""))
A.append(("controle-financeiro-mei","Controle financeiro do MEI: como organizar o dinheiro do seu negócio",
"Passo a passo simples para o MEI controlar receitas, despesas e lucro, separar o dinheiro pessoal e não estourar o limite anual.",
"""<h1>Controle financeiro do MEI: como organizar o dinheiro do seu negócio</h1>
<p>Muitos MEIs faturam bem e mesmo assim sentem que o dinheiro some. Quase sempre o problema é falta de controle, não de vendas. A boa notícia: um controle simples, feito com constância, já resolve.</p>
<h2>1. Separe a conta da empresa da conta pessoal</h2>
<p>Abra uma conta PJ (muitos bancos digitais oferecem conta gratuita para MEI) e use-a só para o negócio. Recebimentos de clientes entram nela; gastos do negócio saem dela. Misturar as duas é o erro número um.</p>
<h2>2. Defina quanto você vai tirar para você</h2>
<p>Em vez de pegar dinheiro do caixa sempre que precisar, estabeleça uma retirada fixa por mês, como se fosse um salário. O que sobra fica no negócio para reposição, imprevistos e investimento.</p>
<h2>3. Registre toda entrada e saída</h2>
<p>Cada venda e cada gasto vira uma linha: data, tipo (receita ou despesa), categoria, valor. Para receitas, anote também se teve nota fiscal e se é comércio, indústria ou serviço. É isso que monta o relatório mensal obrigatório.</p>
<h2>4. Use categorias de despesa</h2>
<p>Mercadorias, DAS, aluguel, internet, transporte, anúncios, taxas de maquininha. Com categorias, você descobre para onde o dinheiro vai e onde dá para cortar.</p>
<h2>5. Feche o mês</h2>
<p>Até o dia 20 do mês seguinte, faça três coisas: preencha o relatório mensal de receitas brutas, pague o DAS e olhe o resultado:</p>
<table><tr><th>Indicador</th><th>Como calcular</th></tr>
<tr><td>Lucro do mês</td><td>Receitas − despesas</td></tr>
<tr><td>Margem</td><td>Lucro ÷ receitas</td></tr>
<tr><td>Uso do limite</td><td>Faturamento acumulado ÷ R$ 81.000</td></tr></table>
<h2>6. Acompanhe o limite anual</h2>
<p>Passar do limite em mais de 20% gera desenquadramento retroativo e impostos com multa. Acompanhando mês a mês, você vê o problema chegando com antecedência.</p>
<h2>Planilha ou aplicativo?</h2>
<p>Aplicativos de gestão costumam cobrar mensalidade. Uma planilha bem montada faz o essencial de graça depois de pronta, funciona no celular e os dados ficam com você.</p>
"""))
A.append(("separar-dinheiro-pessoal-e-da-empresa-mei","Como o MEI separa o dinheiro pessoal do da empresa (e quanto pode retirar)",
"Por que misturar contas prejudica o MEI, como definir sua retirada mensal, se o lucro do MEI paga imposto de renda e como organizar na prática.",
"""<h1>Como o MEI separa o dinheiro pessoal do da empresa (e quanto pode retirar)</h1>
<p>No MEI, a empresa e a pessoa usam o mesmo nome e, muitas vezes, a mesma conta. Por isso é tão fácil misturar tudo. O resultado: você não sabe se o negócio dá lucro, nem quanto pode gastar sem descapitalizar a empresa.</p>
<h2>Por que separar</h2>
<ul><li>Saber o lucro real do negócio.</li><li>Ter dinheiro para repor estoque e pagar o DAS.</li>
<li>Comprovar renda com mais facilidade (extratos da conta PJ).</li><li>Ter as contas organizadas se o negócio crescer e virar Microempresa.</li></ul>
<h2>Quanto posso retirar?</h2>
<p>Não existe valor fixo por lei. Um jeito prático:</p>
<ol><li>Calcule o lucro médio dos últimos 3 meses (receitas − despesas).</li>
<li>Defina sua retirada mensal em torno de 60% a 70% desse lucro.</li>
<li>Deixe o restante na conta da empresa como reserva e capital de giro.</li></ol>
<p>Exemplo: lucro médio de R$ 4.000 → retirada de R$ 2.600, com R$ 1.400 ficando no negócio. Revise o valor a cada trimestre.</p>
<h2>A retirada paga imposto de renda?</h2>
<p>Parte do lucro do MEI é isenta de imposto de renda na pessoa física, conforme percentuais que variam com a atividade (8% para comércio e indústria, 32% para serviços em geral, aplicados sobre a receita bruta), e essa parte pode crescer se você comprovar o lucro com escrituração. O que passar disso pode ser tributável. Se você tem outras rendas ou retiradas altas, vale conferir com um contador na época da declaração.</p>
<h2>Como organizar na prática</h2>
<ul><li>Receba sempre na conta PJ, inclusive o Pix dos clientes.</li><li>Pague as contas do negócio sempre pela conta PJ.</li>
<li>Faça uma única transferência por mês para a sua conta pessoal: sua retirada.</li>
<li>Registre essa transferência no controle como "retirada do dono", não como despesa do negócio, para enxergar o lucro real.</li></ul>
"""))
A.append(("planilha-relatorio-mensal-mei-gratis","Planilha grátis: Relatório Mensal de Receitas Brutas do MEI",
"Baixe grátis a planilha do Relatório Mensal de Receitas Brutas do MEI, pronta para preencher e imprimir, no Excel ou Google Planilhas.",
"""<h1>Planilha grátis: Relatório Mensal de Receitas Brutas do MEI</h1>
<p>Todo MEI precisa preencher e guardar o Relatório Mensal de Receitas Brutas. Para facilitar, montamos uma planilha gratuita com os 12 meses do ano: você digita os valores de cada mês e o relatório fica pronto para imprimir e assinar.</p>
<p><a class="btn" href="https://projects-betanull.github.io/mei-em-dia/arquivos/Relatorio_Mensal_MEI_Gratis.xlsx">Baixar planilha grátis (.xlsx)</a></p>
<h2>O que tem na versão gratuita</h2>
<ul><li>Uma aba para cada mês com o modelo oficial do relatório (comércio, indústria e serviços, com e sem nota fiscal).</li>
<li>Totais calculados automaticamente.</li><li>Resumo anual com o total para a declaração DASN-SIMEI.</li></ul>
<h2>Como usar</h2>
<ol><li>Baixe o arquivo e abra no Excel ou importe no Google Planilhas (Arquivo → Importar).</li>
<li>Na aba do mês, preencha os valores que você recebeu em cada tipo de receita.</li>
<li>Imprima, assine e guarde junto com as notas fiscais do mês.</li></ol>
<h2>Quer que a planilha some tudo sozinha?</h2>
<p>Na versão gratuita você precisa somar suas vendas antes de digitar. Na versão completa você lança cada venda e despesa uma vez, e ela monta o relatório de qualquer mês, mostra o lucro, avisa quando você chega perto do limite de R$ 81 mil e controla o DAS.</p>
"""))

A.append(("como-fazer-orcamento-pessoal","Como fazer um orçamento pessoal que funciona (método 50-30-20)",
"Passo a passo para montar seu orçamento mensal, a regra 50-30-20 adaptada à realidade brasileira e como fazer sobrar dinheiro no fim do mês.",
"""<h1>Como fazer um orçamento pessoal que funciona (método 50-30-20)</h1>
<p>Orçamento não é cortar tudo o que dá prazer. É decidir antes para onde o dinheiro vai, em vez de descobrir depois para onde ele foi.</p>
<h2>1. Descubra quanto entra de verdade</h2>
<p>Use a renda <strong>líquida</strong>: o que cai na conta depois dos descontos. Se a renda varia (comissão, bicos, MEI), use a média dos últimos 3 meses, ou o menor valor deles para ficar mais seguro.</p>
<h2>2. Anote um mês inteiro de gastos</h2>
<p>Antes de planejar, registre tudo por 30 dias: do aluguel ao cafezinho. A maioria das pessoas se surpreende com delivery, assinaturas esquecidas e compras pequenas no cartão.</p>
<h2>3. Divida a renda com a regra 50-30-20</h2>
<table><tr><th>Parte</th><th>Para quê</th><th>Exemplo com R$ 4.000</th></tr>
<tr><td>50%</td><td>Necessidades: moradia, contas, mercado, transporte, saúde</td><td>R$ 2.000</td></tr>
<tr><td>30%</td><td>Desejos: lazer, restaurantes, compras, streaming</td><td>R$ 1.200</td></tr>
<tr><td>20%</td><td>Futuro: reserva de emergência, investimentos, quitar dívidas</td><td>R$ 800</td></tr></table>
<p>Na realidade brasileira, moradia e mercado costumam passar de 50%. Tudo bem ajustar para 60-30-10 no começo; o importante é ter uma parte fixa para o futuro e ir aumentando.</p>
<h2>4. Transforme em limites por categoria</h2>
<p>Quebre cada parte em categorias com um valor máximo: mercado R$ 900, delivery R$ 200, lazer R$ 250... É o limite por categoria que funciona no dia a dia, porque você sabe na hora se ainda pode gastar.</p>
<h2>5. Pague-se primeiro</h2>
<p>No dia em que o salário cair, transfira a parte do futuro para outra conta ou investimento. O que sobra é o que você pode gastar. Deixar para guardar "o que sobrar" quase sempre resulta em zero.</p>
<h2>6. Revise toda semana</h2>
<p>Uma olhada de 5 minutos por semana para ver quanto já foi gasto em cada categoria evita a surpresa no fim do mês. Se uma categoria estourou, compense em outra no mesmo mês.</p>
<h2>Erros comuns</h2>
<ul><li>Esquecer gastos anuais (IPVA, IPTU, material escolar): divida por 12 e reserve todo mês.</li>
<li>Tratar o limite do cartão como renda.</li><li>Fazer um orçamento apertado demais e desistir na segunda semana.</li></ul>
""","fin"))
A.append(("reserva-de-emergencia","Reserva de emergência: quanto guardar, onde deixar e como começar",
"Quanto deve ter na reserva de emergência, onde guardar com segurança e liquidez, e um plano simples para montar a sua mesmo ganhando pouco.",
"""<h1>Reserva de emergência: quanto guardar, onde deixar e como começar</h1>
<p>A reserva de emergência é o dinheiro que impede que um imprevisto, como desemprego, conserto do carro ou problema de saúde, vire dívida no cartão ou no cheque especial.</p>
<h2>Quanto guardar</h2>
<table><tr><th>Situação</th><th>Reserva recomendada</th></tr>
<tr><td>Carteira assinada, renda estável</td><td>3 a 6 meses de despesas</td></tr>
<tr><td>Autônomo, MEI ou renda variável</td><td>6 a 12 meses de despesas</td></tr></table>
<p>A conta é sobre suas <strong>despesas mensais</strong>, não sobre o salário. Se você gasta R$ 3.000 por mês e tem carteira assinada, a meta fica entre R$ 9.000 e R$ 18.000.</p>
<h2>Onde deixar</h2>
<p>A reserva precisa de três coisas: <strong>segurança</strong>, <strong>liquidez</strong> (resgate no mesmo dia) e render pelo menos perto da inflação. Opções comuns:</p>
<ul><li><strong>Tesouro Selic:</strong> título público, baixo risco, resgate rápido.</li>
<li><strong>CDB com liquidez diária</strong> que pague perto de 100% do CDI, de banco coberto pelo FGC.</li>
<li><strong>Contas remuneradas</strong> de bancos digitais com rendimento atrelado ao CDI.</li></ul>
<p>Evite ações, criptomoedas e qualquer aplicação com carência ou que possa cair de valor justo quando você precisar do dinheiro. A poupança é segura, mas costuma render menos que as opções acima.</p>
<h2>Como começar ganhando pouco</h2>
<ol><li>Defina uma primeira meta pequena: um mês de despesas.</li>
<li>Escolha um valor fixo para guardar todo mês, mesmo que seja R$ 50, e transfira assim que receber.</li>
<li>Direcione dinheiro extra (13º, restituição do IR, bicos) para a reserva até bater a meta.</li>
<li>Corte uma despesa recorrente (uma assinatura, delivery semanal) e mande esse valor direto para a reserva.</li></ol>
<h2>E se eu tiver dívidas?</h2>
<p>Se as dívidas têm juros altos (cartão rotativo, cheque especial), priorize quitá-las, mantendo uma reserva mínima para não voltar a usar o crédito no próximo imprevisto. Dívidas com juros baixos podem seguir no prazo enquanto a reserva cresce.</p>
<h2>Quando usar</h2>
<p>Só em emergências de verdade: perda de renda, saúde, consertos inadiáveis. Usou? A prioridade passa a ser repor a reserva.</p>
""","fin"))
A.append(("nfs-e-nacional-simples-nacional-novembro-2026-mei","NFS-e Nacional obrigatória a partir de 1º de novembro: o que muda para o MEI",
"Desde 1º de novembro de 2026, ME e EPP do Simples Nacional emitem nota de serviço pelo Emissor Nacional. Veja o que muda (e o que não muda) para o MEI.",
"""<h1>NFS-e Nacional obrigatória a partir de 1º de novembro: o que muda para o MEI</h1>
<p>A partir de <strong>1º de novembro de 2026</strong>, microempresas (ME) e empresas de pequeno porte (EPP) do Simples Nacional que prestam serviços passam a emitir a nota fiscal de serviço obrigatoriamente pelo <strong>Emissor Nacional da NFS-e</strong>, e não mais pelo sistema da prefeitura. A regra está na Resolução CGSN nº 191/2026, que adiou a data original de 1º de setembro.</p>
<h2>E o MEI? Resposta curta: para você, quase nada muda agora</h2>
<p>O MEI já é obrigado a emitir a NFS-e pelo Emissor Nacional desde <strong>setembro de 2023</strong>. Se você é MEI prestador de serviço e já emite pelo site nfse.gov.br ou pelo app NFS-e Mobile, continue do mesmo jeito.</p>
<p>A mudança de novembro vale para quem é ME ou EPP. Mas ela interessa ao MEI em duas situações:</p>
<ul><li><strong>Se você vai sair do MEI</strong> (por ter passado do limite de R$ 81 mil ou por contratar mais de um funcionário): como ME no Simples Nacional, você continua emitindo pelo mesmo Emissor Nacional. Não precisa aprender o sistema da prefeitura.</li>
<li><strong>Se seus clientes são empresas do Simples:</strong> as notas que eles emitem agora seguem o mesmo padrão nacional, o que facilita conferir e guardar documentos.</li></ul>
<h2>O imposto vai para Brasília?</h2>
<p>Não. O que muda é <strong>onde a nota é emitida e o formato dela</strong>, que passa a ser igual no país inteiro. O <strong>ISS continua sendo um imposto municipal</strong>: a prefeitura segue responsável por fiscalizar, cobrar e arrecadar, e recebe automaticamente os dados das notas emitidas no ambiente nacional. Para o MEI, o ISS continua embutido no DAS mensal (R$ 5), sem mudança.</p>
<p>O padrão nacional começou a ser construído em 2021 e 2022, por acordo entre a Receita Federal e entidades de municípios, e vem sendo adotado aos poucos pelas prefeituras. Ele também é a base técnica dos novos tributos da Reforma Tributária (IBS e CBS), que começam a aparecer nas notas a partir de 2027.</p>
<h2>O que vem em 2027</h2>
<table><tr><th>Quando</th><th>O que acontece</th></tr>
<tr><td>Desde set/2023</td><td>MEI emite NFS-e só pelo Emissor Nacional</td></tr>
<tr><td>1º/11/2026</td><td>ME e EPP do Simples também passam a emitir só pelo Emissor Nacional</td></tr>
<tr><td>1º/1/2027</td><td>Começam a valer as regras de IBS e CBS para o Simples Nacional nos documentos fiscais</td></tr></table>
<p>Para o MEI, o ponto de atenção em 2027 é a <strong>ampliação da exigência de nota fiscal</strong> prevista pela Reforma, inclusive em vendas para pessoa física. Veja os detalhes no <a href="https://projects-betanull.github.io/mei-em-dia/nota-fiscal-mei/">guia de nota fiscal do MEI</a> e acompanhe as regras finais no Portal do Empreendedor.</p>
<h2>Checklist rápido para o MEI</h2>
<ul><li>Sua conta gov.br está no nível prata ou ouro? É ela que dá acesso ao Emissor Nacional.</li>
<li>Seus clientes e serviços frequentes estão salvos como favoritos no emissor?</li>
<li>Você registra todas as receitas, com e sem nota, no seu controle mensal? É isso que monta o relatório mensal e mostra quanto falta para o limite anual.</li></ul>
"""))
A.append(("como-sair-das-dividas","Como sair das dívidas: plano em 7 passos para quitar e limpar o nome",
"Passo a passo para sair das dívidas: listar tudo, priorizar os juros mais caros, negociar com desconto, usar o Desenrola e não voltar a se endividar.",
"""<h1>Como sair das dívidas: plano em 7 passos para quitar e limpar o nome</h1>
<p>Dívida não se resolve com força de vontade nem pagando "um pouco de cada" sem critério. Resolve-se com um plano: saber exatamente quanto deve, atacar primeiro o que cobra mais juros e negociar no momento certo. Este guia mostra o caminho em sete passos.</p>
<h2>1. Liste todas as dívidas, sem exceção</h2>
<p>Pegue as faturas, os extratos e os carnês e monte uma lista com cada dívida. Para descobrir o que você não lembra, consulte de graça:</p>
<ul><li><strong>Registrato</strong>, do Banco Central (acesso com conta gov.br): mostra empréstimos, cartões e financiamentos em seu nome em todos os bancos.</li>
<li><strong>Serasa</strong> e outros birôs de crédito: mostram as dívidas negativadas, inclusive de lojas e contas de consumo.</li></ul>
<p>Para cada dívida, anote: credor, valor total, valor da parcela, <strong>taxa de juros ao mês</strong>, quantas parcelas faltam e se está em atraso.</p>
<table><tr><th>Credor</th><th>Saldo</th><th>Juros ao mês</th><th>Situação</th></tr>
<tr><td>Cartão (rotativo)</td><td>R$ 2.400</td><td>acima de 10%</td><td>Atrasado</td></tr>
<tr><td>Cheque especial</td><td>R$ 800</td><td>até 8%</td><td>Em uso</td></tr>
<tr><td>Empréstimo pessoal</td><td>R$ 3.000</td><td>cerca de 5%</td><td>Em dia</td></tr>
<tr><td>Consignado</td><td>R$ 6.000</td><td>cerca de 1,8%</td><td>Em dia</td></tr></table>
<p class="aviso">Exemplo ilustrativo. As taxas reais variam por banco e por cliente: confira no seu contrato ou na fatura.</p>
<h2>2. Pare de criar dívida nova</h2>
<p>Não adianta quitar de um lado e abrir de outro. Enquanto estiver no plano, tire o cartão da carteira e dos apps de compra, não use o cheque especial como se fosse saldo e não faça parcelamentos novos. Quem paga conta com cartão porque o dinheiro não fecha precisa primeiro ajustar o orçamento (passo 4).</p>
<h2>3. Ordene pela taxa de juros, não pelo valor</h2>
<p>A ordem que economiza mais dinheiro é quitar primeiro a dívida com <strong>maior juro</strong>, mantendo o pagamento mínimo das outras para não gerar multa. No Brasil, as mais caras quase sempre são, nesta ordem: <strong>rotativo do cartão, cheque especial e parcelamento de fatura</strong>. Consignado e financiamento de veículo costumam ficar por último.</p>
<p>Se você precisa de motivação, existe a alternativa de quitar primeiro a menor dívida (método "bola de neve"). Custa um pouco mais em juros, mas a sensação de riscar itens da lista ajuda muita gente a não desistir. Escolha um método e siga.</p>
<h2>4. Descubra quanto sobra por mês para as dívidas</h2>
<p>Faça um orçamento realista: renda líquida menos gastos essenciais (moradia, mercado, contas, transporte, saúde). O que sobra é o valor que você pode comprometer com acordos. <strong>Nunca feche uma parcela que não cabe nesse valor</strong>: acordo quebrado volta a acumular juros e piora a negociação seguinte. Veja como montar o seu no <a href="https://projects-betanull.github.io/mei-em-dia/como-fazer-orcamento-pessoal/">guia de orçamento pessoal</a>.</p>
<h2>5. Negocie com desconto</h2>
<p>Dívidas atrasadas há mais tempo costumam ter os maiores descontos, porque o credor já espera receber pouco. Caminhos gratuitos:</p>
<ul><li><strong>Direto com o banco ou a loja</strong>, pelo app ou central de atendimento. Peça o valor para quitação à vista e compare com o parcelado.</li>
<li><strong>Plataformas de negociação</strong> como Serasa Limpa Nome, que reúnem ofertas de vários credores, principalmente nos feirões de mutirão.</li>
<li><strong>Consumidor.gov.br</strong>, serviço público para registrar reclamação e buscar acordo com empresas participantes.</li></ul>
<p>Antes de aceitar, confira o <strong>custo total</strong> (parcela × número de parcelas) e peça tudo por escrito. Pague só por boleto ou Pix com o nome do credor ou da plataforma oficial: golpistas imitam ofertas de "limpa nome".</p>
<h2>6. Use os programas do governo quando se encaixar</h2>
<p>Em 2026, o <strong>Novo Desenrola</strong> abriu renegociação para pessoas com renda de até 5 salários mínimos (R$ 8.105), com descontos de 30% a 90% em dívidas de cartão, cheque especial e crédito pessoal, juros de até 1,99% ao mês e possibilidade de usar parte do FGTS. Em setembro, uma nova medida provisória criou o <strong>Desenrola 3.0</strong>, voltado a dívidas de até R$ 10 mil atrasadas há cerca de 2 a 4 anos e meio, com desconto mínimo de 90%. Pelo cronograma do governo, os descontos dessa fase começam a chegar aos devedores a partir de <strong>fevereiro de 2027</strong>. Prazos e regras podem mudar: confira sempre em gov.br antes de decidir.</p>
<h2>7. Troque dívida cara por barata (com cuidado)</h2>
<p>Pegar um empréstimo com juros menores para quitar o rotativo ou o cheque especial pode fazer sentido, desde que a parcela caiba no orçamento e você <strong>não volte a usar</strong> o crédito que quitou. Compare sempre o Custo Efetivo Total (CET), que inclui juros, tarifas e seguros.</p>
<h2>Seus direitos como endividado</h2>
<ul><li><strong>Limite de juros do cartão:</strong> desde janeiro de 2024, os juros e encargos do rotativo e do parcelamento da fatura não podem passar de <strong>100% do valor original</strong> da dívida (Lei 14.690/2023).</li>
<li><strong>Superendividamento:</strong> quem não consegue pagar as dívidas de consumo sem comprometer o mínimo para viver pode pedir a repactuação de todas elas em um único plano, pelo Procon ou pela Justiça (Lei 14.181/2021).</li>
<li><strong>Nome limpo após o pagamento:</strong> quitada a dívida, o credor deve pedir a retirada da negativação em até 5 dias úteis.</li></ul>
<h2>Depois de quitar</h2>
<p>Redirecione o valor que ia para as parcelas para uma <a href="https://projects-betanull.github.io/mei-em-dia/reserva-de-emergencia/">reserva de emergência</a>. É ela que evita que o próximo imprevisto vire uma nova dívida no cartão.</p>
""","fin"))
for art in A:
    slug,t,d,b=art[:4]; prod=art[4] if len(art)>4 else "mei"
    os.makedirs(f"{OUT}/{slug}",exist_ok=True)
    aviso='Conteúdo informativo, não é recomendação financeira individual.' if prod=='fin' else 'Conteúdo informativo. Regras podem mudar: confirme no Portal do Empreendedor ou com um contador.'
    body=b+cta(prod)+'<p class="aviso">'+aviso+'</p><p><a href="'+BASE+'/">← Todos os guias</a></p>'
    open(f"{OUT}/{slug}/index.html","w").write(page(slug+"/",t,d,body))
lista="".join(f'<a href="{BASE}/{s}/">{html.escape(t)}<span>{html.escape(d)}</span></a>' for s,t,d,*_ in A)
home=f"""<h1>Guias práticos para o MEI e para o seu dinheiro</h1><p>Limite de faturamento, DAS, relatório mensal, declaração anual e organização financeira explicados sem complicação.</p>{cta()}<div class="lista">{lista}</div>"""
open(f"{OUT}/index.html","w").write(page("","MEI em Dia: guias práticos para o Microempreendedor Individual","Limite do MEI, DAS, relatório mensal de receitas e DASN-SIMEI explicados de forma simples.",home,False))
sm="".join(f"<url><loc>{BASE}/{a[0]}/</loc><lastmod>{HOJE}</lastmod></url>" for a in A)
open(f"{OUT}/sitemap.xml","w").write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{BASE}/</loc></url>{sm}</urlset>')
open(f"{OUT}/robots.txt","w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
print("ok", len(A))
