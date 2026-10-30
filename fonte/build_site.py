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
def cta(): return f"""<div class="cta"><strong>Planilha MEI 2027: controle tudo isso automaticamente</strong>
<p>Relatório mensal pronto para imprimir, alerta do limite de R$ 81 mil, controle do DAS e valores da DASN-SIMEI calculados. Funciona no Excel e no Google Planilhas.</p>
<a class="btn" href="{CHECKOUT}" rel="nofollow">Quero a planilha por R$ 29,90</a></div>"""
def page(slug,title,desc,body,article=True):
    url=f"{BASE}/{slug}" if slug else f"{BASE}/"
    ld=f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"{html.escape(title)}","dateModified":"{HOJE}","publisher":{{"@type":"Organization","name":"{SITE}"}}}}</script>' if article else ""
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
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
<p>O MEI não precisa emitir nota fiscal quando vende para pessoa física (consumidor final), a não ser que o cliente peça. Para empresas (CNPJ), a nota é obrigatória. Na prestação de serviços, a nota é a NFS-e no padrão nacional. Mesmo sem nota, a receita entra no relatório e conta para o limite anual.</p>
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
<p>Como depende do salário mínimo, o DAS muda todo janeiro. Confira o valor exato da sua guia no Portal do Empreendedor ou no app MEI.</p>
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
for slug,t,d,b in A:
    os.makedirs(f"{OUT}/{slug}",exist_ok=True)
    body=b+cta()+'<p class="aviso">Conteúdo informativo. Regras podem mudar: confirme no Portal do Empreendedor ou com um contador.</p><p><a href="'+BASE+'/">← Todos os guias</a></p>'
    open(f"{OUT}/{slug}/index.html","w").write(page(slug+"/",t,d,body))
lista="".join(f'<a href="{BASE}/{s}/">{html.escape(t)}<span>{html.escape(d)}</span></a>' for s,t,d,_ in A)
home=f"""<h1>Guias práticos para o MEI</h1><p>Limite de faturamento, DAS, relatório mensal e declaração anual explicados sem complicação.</p>{cta()}<div class="lista">{lista}</div>"""
open(f"{OUT}/index.html","w").write(page("","MEI em Dia: guias práticos para o Microempreendedor Individual","Limite do MEI, DAS, relatório mensal de receitas e DASN-SIMEI explicados de forma simples.",home,False))
sm="".join(f"<url><loc>{BASE}/{s}/</loc><lastmod>{HOJE}</lastmod></url>" for s,_,_,_ in A)
open(f"{OUT}/sitemap.xml","w").write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{BASE}/</loc></url>{sm}</urlset>')
open(f"{OUT}/robots.txt","w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
print("ok", len(A))
