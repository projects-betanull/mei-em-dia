import os, datetime, html, json
OUT=".."; CHECKOUT="https://pay.kiwify.com.br/IJghjr7"; BASE="https://projects-betanull.github.io/mei-em-dia"
SITE="MEI em Dia"; HOJE=datetime.date.today().isoformat()
# Guia em destaque na página inicial (trocar quando houver um tema de prazo mais urgente)
DESTAQUE="mei-2027-o-que-muda"
CSS="""*{box-sizing:border-box}body{margin:0;font-family:system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif;color:#1f2937;line-height:1.7;background:#fafaf9;font-size:17px}
header{background:#1f6f5c;color:#fff;padding:12px 20px}header .in{max-width:760px;margin:0 auto;display:flex;flex-wrap:wrap;align-items:center;gap:6px 18px}
header .logo{color:#fff;text-decoration:none;font-weight:800;font-size:1.15rem;margin-right:auto}header nav a{color:#e3f1ec;text-decoration:none;font-size:.92rem}header nav a:hover{color:#fff;text-decoration:underline}header nav{display:flex;gap:14px;flex-wrap:wrap}
main{max-width:760px;margin:0 auto;padding:18px 20px 60px}h1{font-size:1.85rem;line-height:1.25;margin:.3em 0 .2em}h2{margin-top:1.8em;color:#1f6f5c;line-height:1.3}h3{font-size:1.05rem;margin:1.3em 0 .3em}
a{color:#1f6f5c}.crumbs{font-size:.85rem;color:#6b7280}.crumbs a{color:#6b7280}.data{font-size:.85rem;color:#6b7280;margin:0 0 1em}
.resumo{background:#fff;border-left:4px solid #1f6f5c;border-radius:8px;padding:14px 18px;margin:18px 0;box-shadow:0 1px 3px rgba(0,0,0,.06)}.resumo>strong{display:block;margin-bottom:4px}.resumo ul{margin:0;padding-left:20px}
.cta{background:#e3f1ec;border:1px solid #b7dccd;border-radius:12px;padding:20px;margin:32px 0}.cta strong{font-size:1.1rem}
.btn{display:inline-block;background:#1f6f5c;color:#fff!important;padding:12px 22px;border-radius:8px;text-decoration:none;font-weight:700;margin-top:10px}.btn2{background:#fff;color:#1f6f5c!important;border:2px solid #1f6f5c}
.mini{background:#f3f4f6;border-radius:8px;padding:12px 16px;margin:24px 0;font-size:.95rem}.gratis{background:#fff8e6;border:1px solid #f2d999;border-radius:12px;padding:16px 18px;margin:28px 0}
table{border-collapse:collapse;width:100%;margin:16px 0;display:block;overflow-x:auto}td,th{border:1px solid #d1d5db;padding:8px;text-align:left}th{background:#f3f4f6}
.lista a{display:block;padding:14px 0;border-bottom:1px solid #e5e7eb;font-weight:600;text-decoration:none}.lista span{display:block;font-weight:400;color:#6b7280;font-size:.95rem}
.rel{margin:36px 0 10px;padding-top:8px;border-top:2px solid #e5e7eb}.rel h2{margin-top:.6em}
.hero{padding:10px 0 4px}.hero p{font-size:1.1rem;color:#374151}.dest{background:#fff;border:2px solid #1f6f5c;border-radius:12px;padding:16px 18px;margin:22px 0}.dest small{color:#1f6f5c;font-weight:700;text-transform:uppercase;letter-spacing:.04em}.dest a{display:block;font-weight:700;font-size:1.1rem;text-decoration:none;margin:4px 0}
footer{text-align:center;color:#6b7280;font-size:.85rem;padding:30px 20px;border-top:1px solid #e5e7eb}footer a{color:#6b7280}.aviso{font-size:.85rem;color:#6b7280}"""
CHECKOUT2="https://pay.kiwify.com.br/YThmb2o"
GRATIS=f"{BASE}/planilha-relatorio-mensal-mei-gratis/"
MESES=["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
def data_br(iso):
    a,m,d=iso.split("-"); return f"{int(d)} de {MESES[int(m)-1]} de {a}"
def cta(prod="mei"):
    if prod=="fin": return f"""<div class="cta" id="oferta" style="background:#e8ebf7;border-color:#c5cbeb"><strong>Planilha Financeira Pessoal 2027: faça isso no automático</strong>
<p>Orçamento por categoria com alerta quando estoura, controle de dívidas, metas de economia e painel com gráficos. Funciona no Excel e no Google Planilhas.</p>
<a class="btn" style="background:#3b4a9c" href="{CHECKOUT2}" rel="nofollow">Quero a planilha por R$ 24,90</a></div>"""
    return f"""<div class="cta" id="oferta"><strong>Planilha MEI 2027: controle tudo isso automaticamente</strong>
<p>Relatório mensal pronto para imprimir, alerta do limite anual de faturamento, controle do DAS e valores da DASN-SIMEI calculados. Funciona no Excel e no Google Planilhas.</p>
<a class="btn" href="{CHECKOUT}" rel="nofollow">Quero a planilha por R$ 29,90</a></div>"""
def mini_cta(prod):
    if prod=="fin": return '<p class="mini">Prefere que as contas se façam sozinhas? A <a href="#oferta">Planilha Financeira Pessoal 2027</a> monta o orçamento por categoria e avisa quando um gasto estoura.</p>'
    return '<p class="mini">Quer que o relatório mensal, o lucro e o limite sejam calculados sozinhos? Veja a <a href="#oferta">Planilha MEI 2027</a>.</p>'
def gratis_box():
    return f'<div class="gratis"><strong>Grátis: planilha do Relatório Mensal de Receitas Brutas</strong><br>Os 12 meses prontos para preencher e imprimir, com o total anual para a DASN-SIMEI. <a href="{GRATIS}">Baixar a planilha grátis</a></div>'
ORG={"@type":"Organization","name":SITE,"url":f"{BASE}/","logo":f"{BASE}/apple-touch-icon.png"}
def page(slug,title,desc,body,schemas=(),og_img=None,tipo="article"):
    url=f"{BASE}/{slug}" if slug else f"{BASE}/"
    img=og_img or f"{BASE}/og/home.png"
    ld="".join(f'<script type="application/ld+json">{json.dumps(x,ensure_ascii=False)}</script>' for x in schemas)
    t=html.escape(title); d=html.escape(desc)
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="google-site-verification" content="w_NTN5a5cFI9a-yrtXuVR_EZzN4_bGfdlxHHK1rwZHU"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title><meta name="description" content="{d}"><link rel="canonical" href="{url}">
<link rel="icon" href="{BASE}/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="{BASE}/apple-touch-icon.png"><meta name="theme-color" content="#1f6f5c">
<meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:type" content="{tipo}"><meta property="og:url" content="{url}"><meta property="og:site_name" content="{SITE}"><meta property="og:locale" content="pt_BR">
<meta property="og:image" content="{img}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">
<style>{CSS}</style>{ld}</head><body><header><div class="in"><a class="logo" href="{BASE}/">{SITE}</a><nav><a href="{BASE}/#mei">Guias do MEI</a><a href="{BASE}/#financas">Finanças pessoais</a><a href="{GRATIS}">Planilha grátis</a></nav></div></header><main>{body}</main>
<footer>{SITE} — guias práticos para o Microempreendedor Individual.<br>Conteúdo informativo; confirme sempre no Portal do Empreendedor (gov.br/mei) ou com um contador.<br><a href="{BASE}/sobre/">Sobre o site e fontes</a> · <a href="{GRATIS}">Planilha grátis</a></footer></body></html>"""

def og_image(nome,titulo):
    """Gera a imagem de compartilhamento (1200x630) só se ainda não existir."""
    path=f"{OUT}/og/{nome}.png"
    if os.path.exists(path): return
    try:
        from PIL import Image, ImageDraw, ImageFont
        os.makedirs(f"{OUT}/og",exist_ok=True)
        im=Image.new("RGB",(1200,630),"#1f6f5c"); dr=ImageDraw.Draw(im)
        def fonte(peso,tam):
            for p in [f"/usr/share/fonts/opentype/inter/Inter-{peso}.otf",f"/usr/share/fonts/truetype/dejavu/DejaVuSans{'-Bold' if peso!='Regular' else ''}.ttf"]:
                if os.path.exists(p): return ImageFont.truetype(p,tam)
            return ImageFont.load_default()
        f1=fonte("Bold",64); f2=fonte("SemiBold",34); f3=fonte("Regular",28)
        dr.rounded_rectangle((70,70,150,150),18,fill="#ffffff"); dr.text((110,110),"M",font=fonte("Bold",56),fill="#1f6f5c",anchor="mm")
        dr.text((175,88),SITE,font=f2,fill="#ffffff")
        linhas=[]; atual=""
        for w in titulo.split():
            teste=(atual+" "+w).strip()
            if dr.textlength(teste,font=f1)>1060: linhas.append(atual); atual=w
            else: atual=teste
        linhas.append(atual); linhas=linhas[:4]
        y=210
        for l in linhas: dr.text((70,y),l,font=f1,fill="#ffffff"); y+=80
        dr.text((70,560),"Guia prático e gratuito para o seu negócio e o seu dinheiro",font=f3,fill="#b7dccd")
        im.save(path,optimize=True)
    except Exception as e:
        print("aviso: imagem og não gerada:",nome,e)

def icones():
    if not os.path.exists(f"{OUT}/favicon.svg"):
        open(f"{OUT}/favicon.svg","w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#1f6f5c"/><text x="32" y="45" font-family="Arial,Helvetica,sans-serif" font-size="38" font-weight="700" fill="#fff" text-anchor="middle">M</text></svg>')
    if not os.path.exists(f"{OUT}/apple-touch-icon.png"):
        try:
            from PIL import Image, ImageDraw, ImageFont
            im=Image.new("RGB",(180,180),"#1f6f5c"); dr=ImageDraw.Draw(im)
            p="/usr/share/fonts/opentype/inter/Inter-Bold.otf"
            f=ImageFont.truetype(p,110) if os.path.exists(p) else ImageFont.load_default()
            dr.text((90,92),"M",font=f,fill="#ffffff",anchor="mm"); im.save(f"{OUT}/apple-touch-icon.png",optimize=True)
        except Exception as e: print("aviso: ícone não gerado:",e)

A=[]
A.append(('limite-mei-2027','Limite do MEI em 2027 sobe para R$ 110 mil: o que muda e o que vale em 2026',
'A LC 238/2026 elevou o limite do MEI para R$ 110 mil em 2027 e R$ 140 mil em 2028. Veja o limite de 2026, o cálculo proporcional e o que acontece se passar.',
"""<h1>Limite do MEI em 2027 sobe para R$ 110 mil: o que muda e o que vale em 2026</h1>
<p>O limite de faturamento do MEI mudou pela primeira vez desde 2018. A <strong>Lei Complementar 238/2026</strong>, publicada em 21 de outubro de 2026, eleva o teto para <strong>R$ 110 mil em 2027</strong> e <strong>R$ 140 mil a partir de 2028</strong>. Mas atenção: em 2026 nada muda, e quem passar do limite neste ano continua sujeito às regras antigas.</p>
<h2>Limite do MEI ano a ano</h2>
<table><tr><th>Ano</th><th>Limite anual</th><th>Média por mês</th></tr>
<tr><td>2026</td><td>R$ 81.000</td><td>R$ 6.750</td></tr>
<tr><td>2027</td><td><strong>R$ 110.000</strong></td><td>R$ 9.166,67</td></tr>
<tr><td>A partir de 2028</td><td><strong>R$ 140.000</strong></td><td>R$ 11.666,67</td></tr></table>
<h2>Em 2026, o limite continua sendo R$ 81 mil</h2>
<p>Até 31 de dezembro de 2026 vale o teto de <strong>R$ 81.000</strong>. O novo valor não é retroativo: se você faturar R$ 95 mil em 2026, por exemplo, isso conta como excesso sobre os R$ 81 mil, mesmo que o valor caiba no limite de 2027. Por isso, quem está perto do teto deve planejar com cuidado as vendas de novembro e dezembro.</p>
<h2>Existe limite mensal?</h2>
<p>Não. O controle é anual. A média mensal (R$ 6.750 em 2026 e R$ 9.166,67 em 2027) é só uma referência: você pode faturar mais em dezembro e menos em fevereiro, desde que a soma do ano não passe do teto.</p>
<h2>Limite proporcional para quem abre o MEI no meio do ano</h2>
<p>Quem abre o MEI durante o ano tem limite proporcional aos meses de atividade, contando o mês de abertura. Em 2027, a conta é <strong>R$ 9.166,67 por mês</strong>:</p>
<table><tr><th>Abertura em 2027</th><th>Meses</th><th>Limite no ano (aprox.)</th></tr>
<tr><td>Janeiro</td><td>12</td><td>R$ 110.000</td></tr><tr><td>Abril</td><td>9</td><td>R$ 82.500</td></tr>
<tr><td>Julho</td><td>6</td><td>R$ 55.000</td></tr><tr><td>Outubro</td><td>3</td><td>R$ 27.500</td></tr></table>
<p>Em 2026, a conta continua sendo R$ 6.750 por mês de atividade.</p>
<h2>Passei do limite. E agora?</h2>
<p>A regra dos 20% da Lei Complementar 123/2006 continua valendo, agora sobre o novo teto:</p>
<table><tr><th>Situação</th><th>2026</th><th>2027</th><th>O que acontece</th></tr>
<tr><td>Excesso de até 20%</td><td>até R$ 97.200</td><td>até R$ 132.000</td><td>Continua MEI até dezembro, paga DAS complementar sobre o excesso e vira Microempresa (ME) em janeiro</td></tr>
<tr><td>Excesso acima de 20%</td><td>acima de R$ 97.200</td><td>acima de R$ 132.000</td><td>Desenquadramento retroativo a janeiro do mesmo ano, com impostos recalculados como ME, juros e multa</td></tr></table>
<h2>Faturei mais de R$ 81 mil em 2026. Posso voltar ao MEI em 2027?</h2>
<p>Contadores que analisaram a lei apontam que quem fechar 2026 com faturamento até R$ 110 mil poderá pedir para voltar ao MEI em janeiro de 2027, já que esse é o limite do novo ano. O excesso de 2026, porém, continua tendo as consequências da tabela acima para 2026. Ainda faltam as regras do Comitê Gestor do Simples Nacional sobre a transição: antes de decidir, confirme com um contador.</p>
<h2>Existe alguma condição para o novo limite valer?</h2>
<p>Sim. O art. 3º da lei condiciona a ampliação dos limites a que a perda de arrecadação seja considerada nas leis orçamentárias de 2027 a 2029. Na prática, o novo teto já está na lei, mas vale acompanhar as orientações do Portal do Empreendedor e da Receita Federal no começo de 2027.</p>
<h2>O que mais muda com a LC 238/2026</h2>
<ul><li><strong>Até 2 empregados</strong> a partir de 2027 (hoje é só 1). Veja as regras e o custo no guia <a href="https://projects-betanull.github.io/mei-em-dia/mei-pode-ter-funcionario/">MEI pode ter funcionário?</a>.</li>
<li><strong>Perdão das dívidas do INSS do DAS</strong> vencidas até 13/10/2026, de forma automática a partir de 1º de janeiro de 2027. Detalhes no guia do <a href="https://projects-betanull.github.io/mei-em-dia/das-mei-valor-vencimento/">DAS MEI</a>.</li>
<li><strong>Licitações exclusivas para MEI</strong>: órgãos públicos podem fazer compras reservadas a microempreendedores em contratações de menor valor.</li></ul>
<h2>O que entra no cálculo do limite</h2>
<p>Conta o <strong>faturamento bruto</strong>: tudo o que você recebeu com vendas e serviços, com ou sem nota fiscal, sem descontar despesas. Por isso o <a href="https://projects-betanull.github.io/mei-em-dia/controle-financeiro-mei/">controle financeiro</a> precisa somar todas as entradas, não só as notas emitidas.</p>
<h2>Como não ser pego de surpresa</h2>
<ul><li>Lance cada receita assim que ela entrar e preencha o <a href="https://projects-betanull.github.io/mei-em-dia/relatorio-mensal-de-receitas-brutas-mei/">relatório mensal</a> até o dia 20.</li><li>Confira todo mês quanto do limite do ano já foi usado.</li>
<li>Ao passar de 80% do limite, planeje os meses seguintes ou converse com um contador sobre virar ME.</li>
<li>Em 2027, atualize o teto da sua planilha ou aplicativo para R$ 110 mil, ou para o valor proporcional se abriu no meio do ano.</li></ul>
"""))
A.append(("relatorio-mensal-de-receitas-brutas-mei","Relatório Mensal de Receitas Brutas do MEI: o que é e como preencher",
"O que é o relatório mensal de receitas brutas, quem precisa fazer, prazo, como preencher cada campo e por quanto tempo guardar.",
"""<h1>Relatório Mensal de Receitas Brutas do MEI: o que é e como preencher</h1>
<p>O Relatório Mensal de Receitas Brutas é um resumo de tudo o que o MEI faturou no mês. É obrigatório para todo MEI, mas <strong>não é enviado ao governo</strong>: você preenche, assina e guarda, junto com as notas fiscais de compras e de vendas do mês.</p>
<h2>Prazo</h2>
<p>O relatório de cada mês deve ser preenchido até o <strong>dia 20 do mês seguinte</strong>. Guarde os relatórios e as notas por <strong>5 anos</strong>: em caso de fiscalização, eles são a prova do seu faturamento. O prazo é o mesmo do <a href="https://projects-betanull.github.io/mei-em-dia/das-mei-valor-vencimento/">DAS</a>, então dá para resolver os dois no mesmo dia.</p>
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
<ul><li>Lançar só o que teve nota e esquecer as vendas em dinheiro ou Pix.</li><li>Descontar despesas: o relatório é de receita <em>bruta</em>.</li><li>Deixar para preencher tudo em maio, na hora da <a href="https://projects-betanull.github.io/mei-em-dia/dasn-simei-declaracao-anual-mei/">declaração anual (DASN-SIMEI)</a>.</li></ul>
"""))
A.append(('das-mei-valor-vencimento','DAS MEI 2026 e 2027: valor, vencimento, atraso e perdão das dívidas',
'Valor do DAS MEI em 2026, previsão para 2027, vencimento no dia 20, multa por atraso, parcelamento e o perdão das dívidas do INSS do MEI pela LC 238/2026.',
"""<h1>DAS MEI 2026 e 2027: valor, vencimento, atraso e perdão das dívidas</h1>
<p>O DAS (Documento de Arrecadação do Simples Nacional) é o imposto mensal fixo do MEI. Ele junta, numa guia só, a contribuição para o INSS e os impostos da sua atividade, e é devido todo mês, mesmo nos meses sem faturamento. Este guia mostra quanto custa em 2026, a previsão para 2027, o que acontece se atrasar e como funciona o perdão de dívidas aprovado em outubro de 2026.</p>
<h2>Como o valor do DAS é calculado</h2>
<ul><li><strong>INSS:</strong> 5% do salário mínimo. É o que garante aposentadoria por idade, auxílio por incapacidade, salário-maternidade e pensão para a família.</li>
<li><strong>ICMS: R$ 1</strong>, para comércio e indústria.</li><li><strong>ISS: R$ 5</strong>, para serviços.</li></ul>
<p>ICMS e ISS são valores fixos. Toda mudança anual vem da parte do INSS, que acompanha o salário mínimo. O MEI caminhoneiro tem regra própria: a parte do INSS é de 12% do salário mínimo.</p>
<h2>Valor do DAS em 2026</h2>
<p>Com o salário mínimo de R$ 1.621, a parte do INSS é de R$ 81,05:</p>
<table><tr><th>Atividade</th><th>Composição</th><th>DAS 2026</th></tr>
<tr><td>Comércio ou indústria</td><td>R$ 81,05 + R$ 1</td><td><strong>R$ 82,05</strong></td></tr>
<tr><td>Serviços</td><td>R$ 81,05 + R$ 5</td><td><strong>R$ 86,05</strong></td></tr>
<tr><td>Comércio e serviços</td><td>R$ 81,05 + R$ 1 + R$ 5</td><td><strong>R$ 87,05</strong></td></tr></table>
<h2>Quanto vai ser o DAS em 2027?</h2>
<p>O valor depende do salário mínimo de 2027, que só é oficializado por decreto no fim de dezembro, depois da inflação de novembro. A proposta de Orçamento enviada ao Congresso projeta <strong>R$ 1.741</strong>. Se esse valor for confirmado, o DAS fica assim:</p>
<table><tr><th>Atividade</th><th>DAS 2027 (previsão)</th></tr>
<tr><td>Comércio ou indústria</td><td>R$ 88,05</td></tr><tr><td>Serviços</td><td>R$ 92,05</td></tr><tr><td>Comércio e serviços</td><td>R$ 93,05</td></tr></table>
<p>O valor novo vale a partir da guia de <strong>janeiro de 2027</strong>, paga em fevereiro. Como 20 de fevereiro de 2027 cai num sábado, essa primeira guia vence em 22 de fevereiro. Esta página será atualizada quando o decreto sair.</p>
<p>Há ainda um detalhe da Reforma Tributária: a Resolução CGSN 190/2026 prevê, a partir de 2027, uma parcela fixa de <strong>CBS e IBS de R$ 1,00 por mês</strong> (R$ 0,994 + R$ 0,006) no DAS do MEI, ao lado do ICMS e do ISS. Se ela entrar em todas as guias, cada valor da tabela acima sobe R$ 1. A composição exata por atividade será confirmada na guia gerada no Portal do Empreendedor. Veja o que mais muda no guia <a href="https://projects-betanull.github.io/mei-em-dia/mei-reforma-tributaria-2027-ibs-cbs-nota-fiscal/">MEI na Reforma Tributária em 2027</a>.</p>
<h2>Vencimento</h2>
<p>O DAS vence no <strong>dia 20 de cada mês</strong> e se refere ao mês anterior: o DAS de março vence em 20 de abril. Se o dia 20 cair em fim de semana ou feriado, o prazo passa para o dia útil seguinte. Aproveite a data para preencher também o <a href="https://projects-betanull.github.io/mei-em-dia/relatorio-mensal-de-receitas-brutas-mei/">relatório mensal de receitas</a> do mês anterior, que tem o mesmo prazo.</p>
<h2>Como pagar</h2>
<ol><li>Acesse o Portal do Empreendedor (gov.br/mei) ou o app MEI e entre em "Pagamento de contribuição mensal (DAS)".</li>
<li>Informe o CNPJ, escolha o ano e marque os meses que quer pagar.</li>
<li>Gere a guia e pague por Pix (QR Code na própria guia), boleto ou internet banking.</li></ol>
<p>Também dá para cadastrar o <strong>débito automático</strong> no portal, o que evita esquecimentos. E vale incluir o DAS no seu <a href="https://projects-betanull.github.io/mei-em-dia/controle-financeiro-mei/">controle financeiro mensal</a> como uma despesa fixa.</p>
<h2>E se atrasar?</h2>
<ul><li><strong>Multa de 0,33% por dia</strong> de atraso, limitada a 20% do valor da guia. Num DAS de R$ 86,05, a multa chega ao teto de R$ 17,21 com cerca de 61 dias.</li>
<li><strong>Juros pela taxa Selic</strong>, acumulada a partir do mês seguinte ao vencimento, mais 1% no mês do pagamento.</li>
<li>Os meses sem pagamento <strong>não contam</strong> para os benefícios do INSS.</li>
<li>Dívidas acumuladas vão para a Dívida Ativa (a parte federal, com a PGFN; ICMS e ISS, com o estado e o município) e o CNPJ pode ser cancelado.</li></ul>
<p>A guia gerada no portal depois do vencimento já vem com multa e juros calculados.</p>
<h2>Perdão das dívidas do DAS (LC 238/2026)</h2>
<p>A Lei Complementar 238/2026 perdoou as dívidas da <strong>parte do INSS do DAS vencidas até 13 de outubro de 2026</strong>, com juros e multas, estejam ou não na Dívida Ativa, inclusive as que estão em parcelamento ou em cobrança na Justiça. Pontos importantes:</p>
<ul><li><strong>É automático.</strong> Segundo a PGFN e a Receita Federal (Portaria nº 740/2026), não é preciso fazer pedido: o cancelamento será feito nos sistemas a partir de 1º de janeiro de 2027.</li>
<li><strong>ICMS e ISS não entram.</strong> Essas partes continuam sendo cobradas.</li>
<li><strong>Há uma condição:</strong> quem continuar MEI precisa pagar em dia o DAS de janeiro a junho de 2027. Atrasar nesse período pode cancelar o perdão.</li>
<li>Quem já pagou não recebe o dinheiro de volta.</li>
<li>Perdoar a dívida não é o mesmo que pagar a contribuição. Se esses meses fazem diferença para a sua aposentadoria ou para algum benefício, consulte o INSS antes de contar com eles.</li></ul>
<p>Você pode consultar suas pendências no Portal de Serviços da Receita Federal (dívidas ainda não inscritas) e no Regularize, da PGFN (dívidas em Dívida Ativa).</p>
<h2>Como parcelar o DAS atrasado</h2>
<p>Dívidas que não entram no perdão (ICMS, ISS e guias vencidas depois de 13/10/2026) podem ser parceladas no Portal do Simples Nacional, em "Parcelamento - Microempreendedor Individual". Se a dívida já estiver na Dívida Ativa, o parcelamento é feito pelo Regularize.</p>
<h2>Dicas para nunca mais atrasar</h2>
<ul><li>Ative o débito automático ou um lembrete fixo para o dia 15.</li>
<li>Separe o valor do DAS na conta da empresa assim que receber o primeiro pagamento do mês.</li>
<li>Pague mesmo nos meses fracos: o DAS é fixo e não depende do faturamento.</li></ul>
"""))
A.append(('dasn-simei-declaracao-anual-mei','DASN-SIMEI 2027: prazo, passo a passo e como fazer a declaração anual do MEI',
'A DASN-SIMEI referente a 2026 vai até 31 de maio de 2027. Veja quem precisa entregar, o que informar, o passo a passo, a multa por atraso e como corrigir erros.',
"""<h1>DASN-SIMEI 2027: prazo, passo a passo e como fazer a declaração anual do MEI</h1>
<p>A DASN-SIMEI é a declaração anual do MEI. Nela você informa quanto faturou no ano anterior, separando comércio e indústria de serviços, e se teve empregado. É rápida de fazer, mas quem perde o prazo paga multa e fica com o CNPJ irregular. Veja tudo o que precisa para entregar a declaração de 2027 sem erro.</p>
<h2>Prazo da DASN-SIMEI em 2027</h2>
<p>A declaração referente ao ano de 2026 deve ser entregue até <strong>31 de maio de 2027</strong> (segunda-feira). Ela já pode ser enviada a partir do começo de janeiro: não há vantagem em esperar o fim do prazo.</p>
<p>Quem dá baixa no MEI entrega a <strong>DASN-SIMEI de extinção</strong>, com prazo próprio:</p>
<table><tr><th>Baixa do MEI</th><th>Prazo da declaração de extinção</th></tr>
<tr><td>Entre janeiro e abril</td><td>Até o último dia de junho do mesmo ano</td></tr>
<tr><td>De maio em diante</td><td>Até o último dia do mês seguinte ao da baixa</td></tr></table>
<h2>Quem precisa entregar</h2>
<ul><li>Todo MEI que esteve ativo em 2026, mesmo que por poucos meses.</li>
<li>Quem <strong>não faturou nada</strong>: nesse caso, informa R$ 0,00.</li>
<li>Quem abriu o MEI durante 2026: declara o faturamento do período em que esteve ativo.</li></ul>
<h2>O que você vai informar</h2>
<table><tr><th>Campo</th><th>De onde vem</th></tr>
<tr><td>Receita bruta total do ano</td><td>Soma dos 12 <a href="https://projects-betanull.github.io/mei-em-dia/relatorio-mensal-de-receitas-brutas-mei/">relatórios mensais</a></td></tr>
<tr><td>Parte de comércio, indústria e transporte de cargas</td><td>Blocos de revenda e indústria dos relatórios</td></tr>
<tr><td>Parte de serviços</td><td>Bloco de prestação de serviços</td></tr>
<tr><td>Teve empregado?</td><td>Sim ou não</td></tr></table>
<p>A receita bruta é tudo o que entrou com vendas e serviços, <strong>com ou sem nota fiscal</strong>, sem descontar despesas. Quem preencheu os relatórios mensais em dia já tem tudo pronto: é só somar. Se não preencheu, junte extratos, notas emitidas e anotações de vendas em dinheiro e Pix antes de começar.</p>
<h2>Passo a passo para enviar</h2>
<ol><li>Acesse o Portal do Empreendedor (gov.br/mei) ou o app MEI e entre em "Declaração Anual de Faturamento (DASN-SIMEI)".</li>
<li>Informe o CNPJ e escolha o ano-calendário <strong>2026</strong>.</li>
<li>Digite a receita bruta total e, dentro dela, quanto veio de comércio e indústria. O restante corresponde aos serviços.</li>
<li>Responda se teve empregado em 2026.</li>
<li>Confira o resumo, transmita e salve o <strong>recibo de entrega</strong> em PDF.</li></ol>
<p>Se o faturamento passou do limite, o próprio sistema gera o DAS complementar sobre o excesso.</p>
<h2>Faturamento acima do limite</h2>
<p>Na declaração de 2027 (ano-base 2026) ainda vale o limite de <strong>R$ 81 mil</strong>. O teto de R$ 110 mil só vale para o faturamento de 2027, que será declarado em 2028.</p>
<table><tr><th>Faturamento em 2026</th><th>O que acontece</th></tr>
<tr><td>Até R$ 81.000</td><td>Declaração normal, sem imposto extra</td></tr>
<tr><td>De R$ 81.000,01 a R$ 97.200</td><td>DAS complementar sobre o excesso e passagem para Microempresa em janeiro de 2027</td></tr>
<tr><td>Acima de R$ 97.200</td><td>Desenquadramento retroativo a janeiro de 2026; procure um contador</td></tr></table>
<p>Veja as regras novas no guia do <a href="https://projects-betanull.github.io/mei-em-dia/limite-mei-2027/">limite do MEI em 2027</a>.</p>
<h2>Multa por atraso</h2>
<p>Entregar depois do prazo gera multa de <strong>2% ao mês</strong> (ou fração) sobre os impostos declarados, limitada a 20%, com <strong>valor mínimo de R$ 50</strong>. A guia da multa (DARF) sai junto com o recibo, na hora da transmissão. Há redução de 50% para quem entrega antes de qualquer intimação e paga no prazo da notificação, mas confira o valor que aparece na sua guia. Enquanto a declaração não é entregue, o MEI fica irregular e não consegue emitir as <a href="https://projects-betanull.github.io/mei-em-dia/das-mei-valor-vencimento/">guias DAS</a> dos períodos seguintes.</p>
<h2>Errei a declaração. Como corrigir?</h2>
<p>É só enviar uma <strong>declaração retificadora</strong> para o mesmo ano, pelo mesmo serviço. Ela substitui a anterior por completo, então preencha todos os campos de novo, não só o que mudou.</p>
<h2>DASN-SIMEI não é imposto de renda</h2>
<p>A DASN-SIMEI é a declaração da empresa. A declaração de imposto de renda da pessoa física é outra obrigação, com prazo próprio, e depende das suas rendas como pessoa (inclusive a parte do lucro do MEI que não é isenta). Veja como separar as duas coisas no guia <a href="https://projects-betanull.github.io/mei-em-dia/separar-dinheiro-pessoal-e-da-empresa-mei/">dinheiro pessoal e da empresa</a>.</p>
<h2>Erros que mais acontecem</h2>
<ul><li>Informar só o valor das notas emitidas e esquecer vendas em dinheiro e Pix.</li><li>Informar o lucro em vez do faturamento bruto.</li>
<li>Misturar receitas de comércio e de serviços.</li><li>Deixar para o último dia e enfrentar o portal lento.</li>
<li>Passar do limite e só perceber na hora da declaração.</li></ul>
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
<p>Mesmo quando a nota não é obrigatória, o valor recebido conta como faturamento e entra no <a href="https://projects-betanull.github.io/mei-em-dia/relatorio-mensal-de-receitas-brutas-mei/">relatório mensal</a> e no <a href="https://projects-betanull.github.io/mei-em-dia/limite-mei-2027/">limite anual de faturamento</a> (R$ 81 mil em 2026 e R$ 110 mil a partir de 2027).</p>
<h2>NFS-e ou NF-e?</h2>
<ul><li><strong>NFS-e (serviços):</strong> o MEI prestador de serviços emite pelo <strong>Emissor Nacional da NFS-e</strong> (site nfse.gov.br ou app NFS-e Mobile), com login gov.br. É gratuito. Desde 1º/11/2026, ME e EPP do Simples também usam esse emissor (veja <a href="https://projects-betanull.github.io/mei-em-dia/nfs-e-nacional-simples-nacional-novembro-2026-mei/">o que mudou em novembro</a>).</li>
<li><strong>NF-e (produtos):</strong> quem vende mercadorias emite a nota de produto, que depende de credenciamento na Secretaria da Fazenda do seu estado e de um sistema emissor autorizado.</li></ul>
<p>Quem vende produtos e serviços pode precisar dos dois tipos.</p>
<h2>Como emitir a NFS-e, passo a passo</h2>
<ol><li>Acesse o Emissor Nacional com sua conta gov.br (nível prata ou ouro).</li>
<li>No primeiro acesso, confira os dados do seu CNPJ.</li>
<li>Clique em emitir nota e informe os dados do cliente (CPF ou CNPJ).</li>
<li>Escolha o código do serviço que corresponde ao que você fez, descreva o serviço e informe o valor.</li>
<li>No campo "Valor aproximado dos tributos", marque "Não informar nenhum valor estimado para os Tributos (Decreto 8.264/2014)". Veja o motivo no guia do <a href="https://projects-betanull.github.io/mei-em-dia/valor-aproximado-dos-tributos-nfs-e-mei/">valor aproximado dos tributos na NFS-e do MEI</a>.</li>
<li>Confira tudo e emita. O PDF e o XML ficam salvos no sistema.</li></ol>
<p>Dica: cadastre como favoritos os clientes e serviços que se repetem. A emissão cai para menos de um minuto.</p>
<h2>O que muda em 2027</h2>
<p>Com a Reforma Tributária, a <strong>Resolução CGSN 190/2026</strong> retirou, a partir de 1º/1/2027, a dispensa de nota nas vendas a consumidor final: em regra, o MEI passa a emitir documento fiscal em toda venda (NFS-e nacional para serviços e, de preferência, a Nota Fiscal Fácil para mercadorias). Em outubro, porém, a <strong>Resolução CGSN 195/2026</strong> e o Decreto 13.140/2026 permitiram usar a <strong>DASN-SIMEI como documento fiscal</strong> nas vendas a pessoa física sem CNPJ. Para empresas e órgãos públicos, a nota continua obrigatória. Os detalhes de como isso vai funcionar ainda dependem de orientação do Comitê Gestor; veja tudo no guia <a href="https://projects-betanull.github.io/mei-em-dia/mei-reforma-tributaria-2027-ibs-cbs-nota-fiscal/">MEI na Reforma Tributária em 2027</a>. Na prática, quem registra toda venda no controle mensal, separando clientes pessoa física e empresa, vai sentir muito menos a mudança.</p>
<h2>Erros comuns</h2>
<ul><li>Não emitir para empresas por achar que é opcional.</li><li>Usar um código de serviço que não corresponde à atividade.</li>
<li>Lançar no controle só o que teve nota e esquecer vendas por Pix ou dinheiro.</li></ul>
"""))
A.append(('mei-pode-ter-funcionario','MEI pode ter funcionário? Em 2027 passam a ser 2: regras, custo e como contratar',
'Em 2026 o MEI pode ter 1 funcionário; a partir de 2027, até 2 (LC 238/2026). Veja o salário permitido, os encargos de 3% de INSS e 8% de FGTS e quanto custa contratar.',
"""<h1>MEI pode ter funcionário? Em 2027 passam a ser 2: regras, custo e como contratar</h1>
<p>Sim. Hoje o MEI pode ter <strong>um empregado</strong> com carteira assinada. Com a Lei Complementar 238/2026, a partir de <strong>1º de janeiro de 2027</strong> esse número sobe para <strong>dois</strong>. Mas há regras de salário e encargos que precisam caber no seu caixa.</p>
<h2>As regras</h2>
<table><tr><th>Período</th><th>Empregados permitidos</th></tr>
<tr><td>Até 31/12/2026</td><td>1</td></tr><tr><td>A partir de 1º/01/2027</td><td>Até 2</td></tr></table>
<ul><li><strong>Salário:</strong> cada empregado recebe o salário mínimo nacional ou o piso da categoria profissional.</li>
<li>Em 2026, contratar um segundo empregado ainda tira a empresa do MEI. Espere janeiro de 2027.</li>
<li>Se um empregado se afastar por motivo legal (licença-maternidade, auxílio por incapacidade), é possível contratar um substituto pelo período do afastamento.</li>
<li>O empregado tem todos os direitos da CLT: férias com 1/3, 13º, FGTS, vale-transporte, aviso prévio.</li>
<li>O registro é feito pelo <strong>eSocial</strong> (módulo simplificado), antes de a pessoa começar a trabalhar.</li></ul>
<h2>Quanto custa por mês</h2>
<p>Sobre o salário, o MEI paga <strong>3% de INSS patronal</strong> e <strong>8% de FGTS</strong>, numa guia única gerada pelo eSocial (DAE):</p>
<table><tr><th>Item</th><th>2026 (mínimo R$ 1.621)</th><th>2027 (previsão R$ 1.741)</th></tr>
<tr><td>Salário</td><td>R$ 1.621,00</td><td>R$ 1.741,00</td></tr><tr><td>INSS patronal (3%)</td><td>R$ 48,63</td><td>R$ 52,23</td></tr>
<tr><td>FGTS (8%)</td><td>R$ 129,68</td><td>R$ 139,28</td></tr><tr><td><strong>Total direto por empregado</strong></td><td><strong>R$ 1.799,31</strong></td><td><strong>R$ 1.932,51</strong></td></tr></table>
<p class="aviso">O salário mínimo de 2027 ainda não foi oficializado; R$ 1.741 é a projeção da proposta de Orçamento.</p>
<p>O INSS do próprio empregado (7,5% na faixa do salário mínimo) é descontado do salário dele, não é custo extra seu.</p>
<h2>O custo que muita gente esquece</h2>
<p>Além do mês a mês, separe todo mês uma reserva para 13º salário, férias com 1/3 e o FGTS sobre eles. Na prática, isso acrescenta cerca de <strong>20% a 25%</strong> ao custo. Considere também vale-transporte e uma provisão para a multa de 40% do FGTS em caso de demissão sem justa causa. Com dois empregados, todos esses valores dobram.</p>
<h2>Vale a pena contratar?</h2>
<p>Faça a conta com seus números: cada empregado precisa gerar mais lucro do que custa. Se seu lucro médio mensal for de R$ 3 mil, por exemplo, um custo total perto de R$ 2.200 consome quase tudo. Olhe o lucro dos últimos meses, não só o faturamento (o <a href="https://projects-betanull.github.io/mei-em-dia/controle-financeiro-mei/">guia de controle financeiro</a> mostra como calcular).</p>
<p>Lembre também do <a href="https://projects-betanull.github.io/mei-em-dia/limite-mei-2027/">limite de faturamento</a>, que sobe para R$ 110 mil em 2027. Crescer com funcionário costuma aproximar o MEI do teto. Se isso for acontecer, vale conversar com um contador sobre virar Microempresa.</p>
"""))
A.append(("controle-financeiro-mei","Controle financeiro para MEI: passo a passo com exemplo prático",
"Como fazer o controle financeiro do MEI: separar contas, registrar receitas e despesas, calcular o lucro, fechar o mês e acompanhar o limite, com exemplo real.",
"""<h1>Controle financeiro para MEI: passo a passo com exemplo prático</h1>
<p>Muitos MEIs faturam bem e mesmo assim sentem que o dinheiro some. Quase sempre o problema é falta de controle, não de vendas. Sem controle, você não sabe se o negócio dá lucro, quanto pode tirar para você, nem quanto falta para o limite anual (R$ 81 mil em 2026 e R$ 110 mil a partir de 2027).</p>
<p>A boa notícia: o controle financeiro do MEI não precisa de sistema caro nem de conhecimento de contabilidade. Um registro simples, feito com constância, resolve. Este guia mostra o passo a passo e um exemplo completo de um mês.</p>

<h2>Por que o MEI precisa de controle financeiro</h2>
<ul><li><strong>É obrigatório</strong> preencher o <a href="https://projects-betanull.github.io/mei-em-dia/relatorio-mensal-de-receitas-brutas-mei/">Relatório Mensal de Receitas Brutas</a> e guardá-lo por 5 anos. Sem anotar as vendas, não há como preenchê-lo.</li>
<li><strong>A declaração anual (DASN-SIMEI)</strong> pede o faturamento do ano separado em comércio/indústria e serviços. Com controle, é só somar.</li>
<li><strong>O limite de faturamento</strong> é anual. Quem passa dele em mais de 20% tem os impostos do ano inteiro recalculados, com multa.</li>
<li><strong>Saber o lucro real</strong> mostra se o preço está certo, quais gastos pesam mais e quanto você pode retirar sem quebrar o caixa.</li></ul>

<h2>Passo 1: separe a conta da empresa da conta pessoal</h2>
<p>Abra uma conta PJ (muitos bancos digitais oferecem conta gratuita para MEI) e use-a só para o negócio. Pagamentos de clientes, inclusive o Pix, entram nela; gastos do negócio saem dela. Misturar as duas contas é o erro número um, porque torna impossível saber o que é do negócio e o que é seu. Veja como fazer isso no guia <a href="https://projects-betanull.github.io/mei-em-dia/separar-dinheiro-pessoal-e-da-empresa-mei/">como separar o dinheiro pessoal do da empresa</a>.</p>

<h2>Passo 2: registre toda entrada e saída</h2>
<p>Cada venda e cada gasto vira uma linha, com cinco informações:</p>
<table><tr><th>Campo</th><th>Exemplo</th></tr>
<tr><td>Data</td><td>12/03</td></tr>
<tr><td>Tipo</td><td>Receita ou despesa</td></tr>
<tr><td>Categoria</td><td>Serviço, revenda, material, DAS...</td></tr>
<tr><td>Valor</td><td>R$ 150,00</td></tr>
<tr><td>Teve nota fiscal?</td><td>Sim ou não (só para receitas)</td></tr></table>
<p>Registre tudo, inclusive as vendas em dinheiro e por Pix sem nota. O limite e o relatório mensal consideram o <strong>faturamento bruto</strong>, com ou sem nota fiscal. O ideal é lançar no mesmo dia; se não der, separe 10 minutos por semana.</p>

<h2>Passo 3: use categorias de despesa</h2>
<p>Categorias mostram para onde o dinheiro vai. As mais comuns para MEI:</p>
<ul><li><strong>Mercadorias para revenda</strong> ou matéria-prima</li>
<li><strong>Materiais e insumos</strong> usados no serviço</li>
<li><strong>DAS</strong> (o imposto mensal)</li>
<li><strong>Aluguel</strong>, espaço ou coworking</li>
<li><strong>Internet e telefone</strong></li>
<li><strong>Transporte e combustível</strong></li>
<li><strong>Taxas</strong> de maquininha, de plataformas e bancárias</li>
<li><strong>Anúncios</strong> e divulgação</li>
<li><strong>Ferramentas e assinaturas</strong> (aplicativos, programas)</li></ul>
<p>Não crie categorias demais: oito a dez bastam. O que importa é usar sempre as mesmas, para comparar um mês com o outro.</p>

<h2>Passo 4: feche o mês</h2>
<p>Até o dia 20 do mês seguinte, faça três coisas: pague o <a href="https://projects-betanull.github.io/mei-em-dia/das-mei-valor-vencimento/">DAS</a>, preencha o relatório mensal e olhe os números do mês:</p>
<table><tr><th>Indicador</th><th>Como calcular</th><th>O que mostra</th></tr>
<tr><td>Faturamento</td><td>Soma das receitas</td><td>Quanto entrou</td></tr>
<tr><td>Lucro</td><td>Receitas − despesas</td><td>Quanto o negócio realmente ganhou</td></tr>
<tr><td>Margem</td><td>Lucro ÷ receitas</td><td>Quanto sobra de cada R$ 100 vendidos</td></tr>
<tr><td>Uso do limite</td><td>Faturamento acumulado no ano ÷ limite do ano (R$ 81 mil em 2026; R$ 110 mil em 2027)</td><td>Quanto do teto já foi usado</td></tr></table>

<h2>Exemplo prático: um mês de uma MEI</h2>
<p>A Ana é manicure e também revende esmaltes e produtos de cuidado. Em março, ela registrou:</p>
<table><tr><th>Receitas</th><th>Valor</th></tr>
<tr><td>Serviços de manicure e pedicure</td><td>R$ 4.300,00</td></tr>
<tr><td>Revenda de produtos</td><td>R$ 900,00</td></tr>
<tr><td><strong>Total de receitas</strong></td><td><strong>R$ 5.200,00</strong></td></tr></table>
<table><tr><th>Despesas</th><th>Valor</th></tr>
<tr><td>Produtos comprados para revenda</td><td>R$ 520,00</td></tr>
<tr><td>Materiais usados nos atendimentos</td><td>R$ 380,00</td></tr>
<tr><td>DAS (comércio e serviços, 2026)</td><td>R$ 87,05</td></tr>
<tr><td>Aluguel da cadeira no salão</td><td>R$ 600,00</td></tr>
<tr><td>Internet e celular</td><td>R$ 100,00</td></tr>
<tr><td>Transporte</td><td>R$ 180,00</td></tr>
<tr><td>Taxas da maquininha</td><td>R$ 70,00</td></tr>
<tr><td>Anúncios</td><td>R$ 100,00</td></tr>
<tr><td><strong>Total de despesas</strong></td><td><strong>R$ 2.037,05</strong></td></tr></table>
<p><strong>Resultado de março:</strong></p>
<ul><li>Lucro: R$ 5.200,00 − R$ 2.037,05 = <strong>R$ 3.162,95</strong></li>
<li>Margem: 3.162,95 ÷ 5.200 = <strong>cerca de 61%</strong></li>
<li>No relatório mensal: R$ 900 no bloco de revenda e R$ 4.300 no bloco de serviços.</li></ul>
<p>Com o lucro na mão, a Ana decide sua retirada. Se ela tirar 65% do lucro (cerca de R$ 2.050) e deixar o resto (cerca de R$ 1.100) na conta da empresa, forma uma reserva para meses fracos e para repor estoque.</p>
<p>E o limite? Se até agosto o faturamento acumulado dela for de R$ 41.300, ela usou 51% do limite e ainda pode faturar R$ 39.700 até dezembro. No ritmo de R$ 5.200 por mês, chegaria a cerca de R$ 62 mil no ano, dentro do teto.</p>

<h2>Passo 5: defina quanto você vai tirar para você</h2>
<p>Em vez de pegar dinheiro do caixa sempre que precisar, estabeleça uma <strong>retirada fixa por mês</strong>, como se fosse um salário, com base no lucro médio dos últimos meses. Faça uma única transferência para a sua conta pessoal e registre-a como "retirada do dono", não como despesa do negócio. Assim o lucro do mês continua aparecendo certo.</p>

<h2>Passo 6: acompanhe o limite anual todo mês</h2>
<p>O teto do MEI é de R$ 81 mil em 2026 e sobe para R$ 110 mil em 2027 (ou proporcional, se você abriu a empresa no meio do ano). Olhando o acumulado todo mês, você vê com meses de antecedência se vai passar. Ao chegar perto de 80% do limite, planeje os meses seguintes ou converse com um contador. Mais detalhes no guia do <a href="https://projects-betanull.github.io/mei-em-dia/limite-mei-2027/">limite do MEI em 2027</a>.</p>

<h2>Erros mais comuns no controle financeiro do MEI</h2>
<ul><li><strong>Anotar só o que teve nota fiscal.</strong> Vendas em dinheiro e Pix também são faturamento.</li>
<li><strong>Confundir faturamento com lucro.</strong> Faturar R$ 6 mil não significa ter R$ 6 mil para gastar.</li>
<li><strong>Esquecer as taxas.</strong> Maquininha, plataformas e tarifas bancárias somam bastante no fim do mês.</li>
<li><strong>Lançar a retirada do dono como despesa.</strong> Isso esconde o lucro real do negócio.</li>
<li><strong>Deixar tudo para maio,</strong> na hora da declaração anual, e tentar lembrar o ano inteiro de uma vez.</li>
<li><strong>Esquecer gastos anuais,</strong> como renovação de equipamentos ou de assinaturas: divida por 12 e reserve todo mês.</li></ul>

<h2>Caderno, aplicativo ou planilha?</h2>
<table><tr><th>Opção</th><th>Vantagem</th><th>Desvantagem</th></tr>
<tr><td>Caderno</td><td>Simples, sem custo</td><td>Não soma nada sozinho e é fácil perder</td></tr>
<tr><td>Aplicativo de gestão</td><td>Muitos recursos</td><td>Costuma cobrar mensalidade</td></tr>
<tr><td>Planilha</td><td>Faz as contas sozinha, sem mensalidade, funciona no celular e os dados ficam com você</td><td>Precisa estar bem montada</td></tr></table>
<p>Para começar sem gastar nada, use a <a href="https://projects-betanull.github.io/mei-em-dia/planilha-relatorio-mensal-mei-gratis/">planilha grátis do relatório mensal</a>. Se quiser que o lucro, o relatório e o limite sejam calculados automaticamente a partir de cada lançamento, a planilha completa está logo abaixo.</p>

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
<ol><li>Calcule o lucro médio dos últimos 3 meses (receitas − despesas). Se ainda não tem esses números, comece pelo <a href="https://projects-betanull.github.io/mei-em-dia/controle-financeiro-mei/">controle financeiro</a>.</li>
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
"Baixe grátis a planilha do Relatório Mensal de Receitas Brutas do MEI: digite os valores do mês e imprima o relatório no modelo oficial. Excel e Google Planilhas, sem cadastro.",
"""<h1>Planilha grátis: Relatório Mensal de Receitas Brutas do MEI</h1>
<p>Todo MEI precisa preencher e guardar o <a href="https://projects-betanull.github.io/mei-em-dia/relatorio-mensal-de-receitas-brutas-mei/">Relatório Mensal de Receitas Brutas</a>. Para facilitar, montamos uma planilha gratuita: você digita os valores de cada mês em uma tabela e ela monta o relatório no modelo oficial, com os 10 campos, pronto para imprimir e assinar. O download é direto, sem cadastro.</p>
<p><a class="btn" href="https://projects-betanull.github.io/mei-em-dia/arquivos/Relatorio_Mensal_MEI_Gratis.xlsx">Baixar planilha grátis (.xlsx)</a></p>
<h2>O que tem na planilha</h2>
<table><tr><th>Aba</th><th>Para que serve</th></tr>
<tr><td><strong>Valores do ano</strong></td><td>Uma linha por mês, de janeiro a dezembro. Você digita quanto recebeu em comércio, indústria e serviços, com e sem nota fiscal. A planilha soma o total do mês, o acumulado do ano e os valores que a DASN-SIMEI pede.</td></tr>
<tr><td><strong>Relatório para imprimir</strong></td><td>O relatório no modelo oficial. Você escolhe o mês (de 1 a 12) e os 10 campos são preenchidos sozinhos, com o nome da empresa e o CNPJ.</td></tr></table>
<h2>Como usar, passo a passo</h2>
<ol><li><strong>Baixe o arquivo</strong> e abra no Excel. No Google Planilhas, use Arquivo → Importar → Upload.</li>
<li>Na aba "Valores do ano", preencha o <strong>nome da empresa, o CNPJ e o ano</strong>.</li>
<li>Apague os valores de exemplo de janeiro e digite, nas células amarelas, <strong>o que você recebeu em cada mês</strong>, na coluna certa (veja a tabela abaixo).</li>
<li>Vá para a aba "Relatório para imprimir" e digite o <strong>número do mês</strong> (3 para março, por exemplo).</li>
<li><strong>Imprima</strong> (ou salve em PDF), preencha local e data e <strong>assine</strong>.</li>
<li>Guarde o relatório com as notas fiscais do mês por <strong>5 anos</strong>.</li></ol>
<p>O prazo para preencher o relatório de cada mês é o <strong>dia 20 do mês seguinte</strong>, o mesmo do <a href="https://projects-betanull.github.io/mei-em-dia/das-mei-valor-vencimento/">DAS</a>.</p>
<h2>Em qual coluna lançar cada receita</h2>
<table><tr><th>Você recebeu por...</th><th>Coluna</th></tr>
<tr><td>Revenda de produtos que comprou prontos, sem emitir nota</td><td>Comércio sem NF</td></tr>
<tr><td>Revenda de produtos, com nota fiscal emitida</td><td>Comércio com NF</td></tr>
<tr><td>Venda de produtos que você mesmo fabrica (bolos, artesanato, roupas), sem nota</td><td>Indústria sem NF</td></tr>
<tr><td>Venda de produtos que você fabrica, com nota</td><td>Indústria com NF</td></tr>
<tr><td>Serviços prestados sem emitir nota</td><td>Serviços sem NF</td></tr>
<tr><td>Serviços com NFS-e emitida</td><td>Serviços com NF</td></tr></table>
<p>Lance o valor <strong>bruto</strong> recebido, sem descontar despesas, taxas de maquininha ou custo de mercadoria. Vendas por Pix e em dinheiro entram do mesmo jeito.</p>
<h2>Exemplo preenchido</h2>
<p>Uma MEI que faz unhas e revende esmaltes recebeu em março: R$ 2.800 de serviços sem nota (clientes pessoa física), R$ 1.500 de serviços com nota (um salão parceiro, com CNPJ) e R$ 900 de revenda sem nota. Na linha de março ela digita:</p>
<table><tr><th>Comércio sem NF</th><th>Serviços sem NF</th><th>Serviços com NF</th><th>Total do mês</th></tr>
<tr><td>R$ 900,00</td><td>R$ 2.800,00</td><td>R$ 1.500,00</td><td><strong>R$ 5.200,00</strong></td></tr></table>
<p>No relatório impresso de março, a planilha preenche: campo 1 (revenda com dispensa de documento fiscal) R$ 900; campo 7 (serviços com dispensa) R$ 2.800; campo 8 (serviços com documento fiscal) R$ 1.500; e campo 10 (total geral) R$ 5.200. Os demais ficam zerados.</p>
<h2>Os 10 campos do relatório</h2>
<p>O modelo oficial tem três blocos (revenda de mercadorias, venda de produtos industrializados e prestação de serviços). Cada bloco tem três linhas: receita com dispensa de documento fiscal, receita com documento fiscal emitido e o total do bloco. O campo 10 é o total geral do mês. No fim, o relatório pede local, data e assinatura, e orienta a anexar as notas fiscais de compras e as notas emitidas no mês.</p>
<h2>Como a planilha ajuda na declaração anual</h2>
<p>Abaixo da tabela, a aba "Valores do ano" mostra três números: <strong>receita total</strong>, <strong>comércio + indústria</strong> e <strong>serviços</strong>. São os valores que a <a href="https://projects-betanull.github.io/mei-em-dia/dasn-simei-declaracao-anual-mei/">DASN-SIMEI</a> pede. A coluna "Acumulado" também mostra quanto você já faturou no ano, para comparar com o <a href="https://projects-betanull.github.io/mei-em-dia/limite-mei-2027/">limite do MEI</a> (R$ 81 mil em 2026 e R$ 110 mil em 2027).</p>
<h2>Quer que a planilha some tudo sozinha?</h2>
<p>Na versão gratuita você precisa somar suas vendas antes de digitar o total do mês. Na versão completa você lança cada venda e despesa uma vez, e ela monta o relatório de qualquer mês, mostra o lucro, avisa quando você chega perto do limite anual e controla o DAS.</p>
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
<tr><td>20%</td><td>Futuro: <a href="https://projects-betanull.github.io/mei-em-dia/reserva-de-emergencia/">reserva de emergência</a>, investimentos, <a href="https://projects-betanull.github.io/mei-em-dia/como-sair-das-dividas/">quitar dívidas</a></td><td>R$ 800</td></tr></table>
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
<li>Corte uma despesa recorrente (uma assinatura, delivery semanal) e mande esse valor direto para a reserva. Um <a href="https://projects-betanull.github.io/mei-em-dia/como-fazer-orcamento-pessoal/">orçamento por categoria</a> mostra onde cortar.</li></ol>
<h2>E se eu tiver dívidas?</h2>
<p>Se as dívidas têm juros altos (cartão rotativo, cheque especial), priorize quitá-las (veja o <a href="https://projects-betanull.github.io/mei-em-dia/como-sair-das-dividas/">plano para sair das dívidas</a>), mantendo uma reserva mínima para não voltar a usar o crédito no próximo imprevisto. Dívidas com juros baixos podem seguir no prazo enquanto a reserva cresce.</p>
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
<ul><li><strong>Se você vai sair do MEI</strong> (por ter passado do <a href="https://projects-betanull.github.io/mei-em-dia/limite-mei-2027/">limite de faturamento</a> ou por contratar mais empregados do que o permitido): como ME no Simples Nacional, você continua emitindo pelo mesmo Emissor Nacional. Não precisa aprender o sistema da prefeitura.</li>
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
<li>Você registra todas as receitas, com e sem nota, no seu <a href="https://projects-betanull.github.io/mei-em-dia/controle-financeiro-mei/">controle mensal</a>? É isso que monta o relatório mensal e mostra quanto falta para o limite anual.</li></ul>
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

A.append(("mei-reforma-tributaria-2027-ibs-cbs-nota-fiscal","MEI na Reforma Tributária em 2027: IBS, CBS, DAS e nota fiscal para pessoa física",
"O que muda para o MEI em 1º de janeiro de 2027: CBS e IBS no DAS, nota fiscal em toda venda, a DASN-SIMEI como documento fiscal para pessoa física e o nanoempreendedor.",
"""<h1>MEI na Reforma Tributária em 2027: IBS, CBS, DAS e nota fiscal para pessoa física</h1>
<p>Em <strong>1º de janeiro de 2027</strong> a Reforma Tributária do consumo começa a valer de verdade para as empresas do Simples Nacional, e o MEI está incluído. Entre agosto e outubro de 2026 saíram três normas que mudam o dia a dia do microempreendedor: a <strong>Resolução CGSN nº 190/2026</strong>, a <strong>Resolução CGSN nº 195/2026</strong> e o <strong>Decreto nº 13.140/2026</strong>. Muita notícia desencontrada circulou desde então. Este guia separa o que já está definido do que ainda depende de regulamentação.</p>
<h2>Resumo do que muda em 2027</h2>
<table><tr><th>Tema</th><th>Até 31/12/2026</th><th>A partir de 1º/1/2027</th></tr>
<tr><td>Impostos no DAS</td><td>INSS + ICMS (R$ 1) e/ou ISS (R$ 5)</td><td>Entra uma parcela fixa de CBS e IBS (R$ 1 no total, segundo a Resolução CGSN 190)</td></tr>
<tr><td>Nota para empresa (CNPJ)</td><td>Obrigatória</td><td>Continua obrigatória</td></tr>
<tr><td>Nota para pessoa física</td><td>Só se o cliente pedir</td><td>Regra geral passa a exigir documento fiscal, mas a DASN-SIMEI poderá cumprir esse papel (Resolução CGSN 195)</td></tr>
<tr><td>Destaque de IBS e CBS na nota</td><td>Não se aplica</td><td>O MEI continua dispensado de destacar os valores</td></tr></table>
<h2>CBS e IBS: o MEI vai pagar imposto novo?</h2>
<p>A CBS (federal) substitui o PIS e a Cofins, e o IBS (de estados e municípios) vai substituir aos poucos o ICMS e o ISS, até 2033. O MEI nunca pagou PIS e Cofins, e continua sem calcular imposto sobre cada venda: tudo segue dentro do <strong>valor fixo mensal do DAS</strong>.</p>
<p>O que muda é a composição da guia. O anexo da Resolução CGSN 190/2026 com os valores fixos do MEI prevê, a partir de 2027, <strong>R$ 0,994 de CBS e R$ 0,006 de IBS</strong>, ou seja, R$ 1,00 por mês, ao lado do R$ 1 de ICMS e dos R$ 5 de ISS, que continuam. Nos anos seguintes, os valores de ICMS e ISS diminuem e os de IBS aumentam, acompanhando a transição.</p>
<p>Na prática, a maior mudança no valor do DAS em 2027 continua vindo do <strong>salário mínimo</strong>, que define a parte do INSS (5%). Com a projeção de R$ 1.741 do Orçamento, só o INSS passa de R$ 81,05 para R$ 87,05. O valor exato da guia de janeiro de 2027 aparecerá no Portal do Empreendedor depois do decreto do salário mínimo. Veja as contas atualizadas no guia do <a href="https://projects-betanull.github.io/mei-em-dia/das-mei-valor-vencimento/">DAS MEI 2026 e 2027</a>.</p>
<h2>Nota fiscal em toda venda: o que a Resolução CGSN 190 mudou</h2>
<p>A Lei Complementar 214/2025, que regulamentou a Reforma, mudou a regra de documentos fiscais da Lei do Simples. Seguindo essa lei, a Resolução CGSN 190/2026, de agosto, retirou a antiga dispensa de nota nas vendas ao consumidor final, com efeitos a partir de 2027. Pela resolução, o MEI deve usar:</p>
<ul><li><strong>NFS-e de padrão nacional</strong> para serviços, emitida de graça no Emissor Nacional (nfse.gov.br ou app NFS-e Mobile), como o MEI já faz desde 2023. Veja o passo a passo no <a href="https://projects-betanull.github.io/mei-em-dia/nota-fiscal-mei/">guia de nota fiscal do MEI</a>.</li>
<li><strong>Nota Fiscal Fácil (NFF)</strong>, de preferência, para venda de mercadorias e alguns serviços de transporte. É o aplicativo gratuito de emissão de nota de produto; a disponibilidade depende do estado.</li></ul>
<p>A mesma resolução manteve o MEI <strong>dispensado de destacar IBS e CBS</strong> nos documentos que emite. Isso faz sentido: como o imposto é fixo no DAS, não existe valor por venda para mostrar. Se você emite nota por um sistema particular, e não pelo emissor oficial, confirme com o fornecedor que ele estará atualizado para os leiautes de 2027.</p>
<h2>DASN-SIMEI como documento fiscal: o alívio para quem vende a pessoa física</h2>
<p>Depois da Resolução 190, muitos MEIs que atendem o público (manicures, ambulantes, pequenos comércios, prestadores de serviço em domicílio) se assustaram com a ideia de emitir uma nota a cada venda de R$ 10. Em <strong>21 de outubro de 2026</strong>, o governo publicou o Decreto nº 13.140/2026 e o CGSN aprovou a Resolução nº 195/2026, que permitem usar a <strong>DASN-SIMEI como documento fiscal eletrônico</strong> nas vendas de mercadorias e serviços do MEI a <strong>consumidor final pessoa física sem CNPJ</strong>, com efeitos a partir de 1º de janeiro de 2027.</p>
<p>A Receita Federal apresentou a medida como uma simplificação das obrigações da Reforma para MEIs e nanoempreendedores. O que isso significa na prática:</p>
<ul><li><strong>Vendas a pessoa física:</strong> em vez de uma nota por venda, essas receitas poderão ser informadas na declaração anual. Se o cliente pedir a nota, você continua podendo (e devendo) emitir.</li>
<li><strong>Vendas a empresas e órgãos públicos:</strong> nada muda. A nota continua obrigatória.</li>
<li><strong>Pontos ainda em aberto:</strong> como as vendas a pessoa física serão detalhadas na DASN-SIMEI e se o formulário vai pedir informações novas ainda dependem das orientações do Comitê Gestor do Simples Nacional e do Portal do Empreendedor.</li></ul>
<p>Uma consequência é certa: se a declaração anual passa a servir de documento fiscal, ela precisa refletir exatamente o que você vendeu. Quem registra toda receita no <a href="https://projects-betanull.github.io/mei-em-dia/controle-financeiro-mei/">controle financeiro</a>, separando as vendas a pessoa física das vendas com nota, vai preencher a declaração sem dor de cabeça. Quem depende da memória vai ter mais trabalho e mais risco.</p>
<h2>Nanoempreendedor: quem fica sem CNPJ</h2>
<p>A Reforma criou a figura do <strong>nanoempreendedor</strong>: a pessoa física com receita bruta anual <strong>inferior à metade do limite do MEI</strong> e que não optou pelo MEI. O Decreto 13.140/2026 dispensou o nanoempreendedor de inscrição no CNPJ e de emissão de documentos fiscais eletrônicos ligados aos novos tributos. Para motoristas de aplicativo e entregadores, conta apenas 25% do valor bruto recebido por mês. As dispensas relativas ao IBS só produzem efeito a partir de 2029.</p>
<p>Isso não significa que vale a pena dar baixa no MEI para virar nanoempreendedor. O DAS é o que garante a contribuição para o INSS (aposentadoria por idade, auxílio por incapacidade, salário-maternidade), e o CNPJ permite vender para empresas e emitir nota. Antes de qualquer decisão, compare com um contador.</p>
<h2>Checklist para o MEI antes de janeiro de 2027</h2>
<ol><li><strong>Confira seu acesso gov.br</strong> (nível prata ou ouro) e entre no Emissor Nacional da NFS-e para ver se seus dados e serviços estão corretos.</li>
<li><strong>Se vende produtos</strong>, verifique se a Nota Fiscal Fácil está disponível no seu estado e faça o credenciamento na Secretaria da Fazenda, se ainda não tiver.</li>
<li><strong>Separe os clientes</strong>: quais são empresas (nota obrigatória) e quais são pessoas físicas.</li>
<li><strong>Organize o registro de vendas</strong> por tipo de cliente e por tipo de receita (comércio ou serviço), mês a mês.</li>
<li><strong>Pague o DAS em dia de janeiro a junho de 2027</strong>: é a condição para manter o perdão das dívidas do INSS previsto na LC 238/2026.</li>
<li><strong>Atualize o teto</strong> do seu controle para o novo <a href="https://projects-betanull.github.io/mei-em-dia/limite-mei-2027/">limite de R$ 110 mil em 2027</a>.</li></ol>
<h2>O que ainda pode mudar</h2>
<p>A Reforma está em plena fase de regulamentação, e as regras do Simples já foram ajustadas várias vezes em 2026. Os pontos que mais merecem atenção nas próximas semanas são o formato da DASN-SIMEI com as vendas a pessoa física, o valor final do DAS de 2027 e eventuais calendários estaduais da Nota Fiscal Fácil. Este guia será atualizado quando essas orientações forem publicadas.</p>
"""))


A.append(("valor-aproximado-dos-tributos-nfs-e-mei","Valor aproximado dos tributos na NFS-e do MEI: qual opção marcar",
"No Emissor Nacional, o MEI marca \"Não informar nenhum valor estimado para os Tributos (Decreto 8.264/2014)\". Veja por quê, onde fica o campo e como deixar salvo.",
"""<h1>Valor aproximado dos tributos na NFS-e do MEI: qual opção marcar</h1>
<p>Quem emite a nota de serviço pelo Emissor Nacional encontra um campo que confunde quase todo MEI: <strong>"Valor aproximado dos tributos"</strong>. Ele traz três opções, e uma delas cita um decreto. Para o MEI, a escolha é simples: marque <strong>"Não informar nenhum valor estimado para os Tributos (Decreto 8.264/2014)"</strong>. Este guia explica o motivo, mostra onde o campo aparece e como deixar a opção salva para as próximas notas.</p>
<h2>As três opções do campo</h2>
<table><tr><th>Opção</th><th>O que faz</th><th>Para o MEI</th></tr>
<tr><td>Preencher os valores monetários em cada NFS-e emitida</td><td>Você digita, em reais, a estimativa de tributos federais, estaduais e municipais de cada nota</td><td>Não é necessário</td></tr>
<tr><td>Configurar os valores percentuais correspondentes</td><td>Você cadastra percentuais e o sistema calcula a estimativa em cada nota</td><td>Não é necessário</td></tr>
<tr><td><strong>Não informar nenhum valor estimado para os Tributos (Decreto 8.264/2014)</strong></td><td>A nota sai sem a estimativa de tributos</td><td><strong>É a opção indicada</strong></td></tr></table>
<h2>Por que o MEI pode não informar</h2>
<p>O campo existe por causa da <strong>Lei 12.741/2012</strong>, conhecida como Lei da Transparência Fiscal, que manda mostrar ao consumidor quanto do preço corresponde, aproximadamente, a impostos. O <strong>Decreto 8.264/2014</strong> regulamentou essa lei e, no <strong>artigo 8º</strong>, tornou a regra <strong>facultativa para o MEI</strong>. Por isso o emissor oferece uma opção que cita justamente esse decreto.</p>
<p>Faz sentido: o MEI não calcula imposto sobre cada venda. Tudo o que ele paga está no valor fixo mensal do <a href="https://projects-betanull.github.io/mei-em-dia/das-mei-valor-vencimento/">DAS</a>, que é o mesmo emitindo uma nota ou cem. Não existe um percentual de imposto "embutido" em cada serviço para mostrar ao cliente.</p>
<h2>Onde o campo aparece no Emissor Nacional</h2>
<ul><li><strong>Na emissão completa da nota:</strong> na etapa de valores, depois do valor do serviço e da tributação municipal, no fim da tela.</li>
<li><strong>Nas configurações:</strong> no ícone de engrenagem, no canto superior da tela inicial, abaixo das informações de contato. Marcando a opção ali, ela já vem escolhida nas notas seguintes.</li></ul>
<p>Vale configurar uma vez, no primeiro acesso. A posição dos campos pode mudar quando o emissor é atualizado, mas o nome do campo e o texto da opção são esses.</p>
<h2>Passo a passo</h2>
<ol><li>Entre em nfse.gov.br com sua conta gov.br (nível prata ou ouro).</li>
<li>Abra as configurações (engrenagem) e localize "Valor aproximado dos tributos".</li>
<li>Marque "Não informar nenhum valor estimado para os Tributos (Decreto 8.264/2014)" e salve.</li>
<li>Ao emitir uma nota, confira na etapa de valores se a opção continua marcada.</li></ol>
<p>O restante da emissão está no guia <a href="https://projects-betanull.github.io/mei-em-dia/nota-fiscal-mei/">nota fiscal MEI: quando é obrigatória e como emitir</a>.</p>
<h2>Marquei outra opção. A nota está errada?</h2>
<p>Não. Informar a estimativa é opcional para o MEI, não proibido. Esse campo é apenas informativo para o cliente: ele <strong>não cria imposto a pagar</strong> nem muda o valor do seu DAS. Nas próximas notas, basta escolher a opção de não informar.</p>
<h2>E se o cliente pedir o valor dos tributos na nota?</h2>
<p>Algumas empresas pedem a nota "com os tributos" por hábito, porque recebem assim de fornecedores maiores. Você pode explicar que, como MEI, paga os impostos em valor fixo pelo DAS e que o Decreto 8.264/2014 torna essa informação facultativa. Se mesmo assim o cliente exigir, as duas primeiras opções do campo permitem informar uma estimativa; nesse caso, vale pedir a um contador o percentual adequado à sua atividade.</p>
<h2>Isso tem a ver com IBS e CBS em 2027?</h2>
<p>São regras diferentes. O "valor aproximado dos tributos" vem da Lei da Transparência Fiscal, de 2012. Já o IBS e a CBS são os tributos novos da Reforma Tributária, e para eles a Resolução CGSN 190/2026 mantém o MEI <strong>dispensado de destacar os valores</strong> na nota. Veja o que muda no guia <a href="https://projects-betanull.github.io/mei-em-dia/mei-reforma-tributaria-2027-ibs-cbs-nota-fiscal/">MEI na Reforma Tributária em 2027</a>.</p>
<h2>Outros cuidados ao emitir a NFS-e</h2>
<ul><li>Escolha o código de serviço que corresponde à atividade registrada no seu CNPJ.</li>
<li>Salve como favoritos os clientes e serviços que se repetem.</li>
<li>Lance o valor de cada nota no seu <a href="https://projects-betanull.github.io/mei-em-dia/controle-financeiro-mei/">controle financeiro</a>: ele entra no <a href="https://projects-betanull.github.io/mei-em-dia/relatorio-mensal-de-receitas-brutas-mei/">relatório mensal</a> e conta para o limite anual.</li></ul>
"""))
A.append(("mei-2027-o-que-muda","MEI 2027: o que muda no limite, no DAS, na nota fiscal e nos prazos",
"Limite de R$ 110 mil, até 2 empregados, DAS com novo salário mínimo, CBS e IBS, nota fiscal, perdão de dívidas e o calendário do MEI em 2027, em um só lugar.",
"""<h1>MEI 2027: o que muda no limite, no DAS, na nota fiscal e nos prazos</h1>
<p>2027 é o ano com mais mudanças para o MEI desde 2018. A Lei Complementar 238/2026 aumentou o limite de faturamento e o número de empregados, e a Reforma Tributária começa a valer para o Simples Nacional. Esta página resume tudo o que muda, com o link para o guia completo de cada assunto.</p>
<h2>Resumo: MEI em 2026 e em 2027</h2>
<table><tr><th>Tema</th><th>2026</th><th>2027</th></tr>
<tr><td>Limite de faturamento</td><td>R$ 81.000</td><td><strong>R$ 110.000</strong></td></tr>
<tr><td>Média por mês</td><td>R$ 6.750</td><td>R$ 9.166,67</td></tr>
<tr><td>Empregados</td><td>1</td><td><strong>Até 2</strong></td></tr>
<tr><td>DAS (comércio / serviços / os dois)</td><td>R$ 82,05 / 86,05 / 87,05</td><td>Previsão de R$ 88,05 / 92,05 / 93,05, mais R$ 1 de CBS e IBS</td></tr>
<tr><td>Nota para pessoa física</td><td>Só se o cliente pedir</td><td>Documento fiscal em toda venda, mas a DASN-SIMEI poderá cumprir esse papel</td></tr>
<tr><td>Dívidas antigas do DAS</td><td>Cobradas normalmente</td><td>Parte do INSS vencida até 13/10/2026 é perdoada</td></tr></table>
<h2>Limite de faturamento: R$ 110 mil</h2>
<p>O teto anual sobe de R$ 81 mil para <strong>R$ 110 mil em 2027</strong> e para R$ 140 mil a partir de 2028. A tolerância de 20% continua: quem faturar até R$ 132 mil em 2027 paga DAS complementar sobre o excesso e vira Microempresa em janeiro seguinte. O novo valor não vale para 2026. A lei condiciona a ampliação às leis orçamentárias, então vale acompanhar as orientações oficiais no começo do ano. Detalhes, limite proporcional e exemplos no guia do <a href="https://projects-betanull.github.io/mei-em-dia/limite-mei-2027/">limite do MEI em 2027</a>.</p>
<h2>Até 2 empregados</h2>
<p>A partir de 1º de janeiro de 2027, o MEI pode ter <strong>dois empregados</strong> com carteira assinada, cada um recebendo o salário mínimo ou o piso da categoria. Os encargos continuam sendo 3% de INSS patronal e 8% de FGTS. Veja quanto custa no guia <a href="https://projects-betanull.github.io/mei-em-dia/mei-pode-ter-funcionario/">MEI pode ter funcionário?</a>.</p>
<h2>DAS: valor novo a partir da guia de janeiro</h2>
<p>A parte do INSS é de 5% do salário mínimo. Com a projeção de R$ 1.741 da proposta de Orçamento, o DAS ficaria entre R$ 88,05 e R$ 93,05, conforme a atividade. O valor oficial depende do decreto do salário mínimo, que sai no fim de dezembro. A regulamentação da Reforma prevê ainda uma parcela fixa de R$ 1 de CBS e IBS. A primeira guia com o valor novo vence em <strong>22 de fevereiro de 2027</strong>. Contas completas no guia do <a href="https://projects-betanull.github.io/mei-em-dia/das-mei-valor-vencimento/">DAS MEI 2026 e 2027</a>.</p>
<h2>Perdão das dívidas do DAS</h2>
<p>A LC 238/2026 perdoou a <strong>parte do INSS do DAS vencida até 13 de outubro de 2026</strong>. O cancelamento é automático, a partir de 1º de janeiro de 2027, sem pedido. ICMS e ISS não entram. Para manter o perdão, quem continua MEI precisa pagar em dia o DAS de janeiro a junho de 2027. Veja as condições no <a href="https://projects-betanull.github.io/mei-em-dia/das-mei-valor-vencimento/">guia do DAS</a>.</p>
<h2>Nota fiscal e Reforma Tributária</h2>
<p>Pela Resolução CGSN 190/2026, a regra geral passa a exigir documento fiscal em toda venda a partir de 2027. Para aliviar quem vende a pessoa física, a Resolução CGSN 195/2026 e o Decreto 13.140/2026 permitem que a <strong>DASN-SIMEI sirva de documento fiscal</strong> nessas vendas. Para empresas e órgãos públicos, a nota continua obrigatória, e o MEI segue dispensado de destacar IBS e CBS. Entenda no guia <a href="https://projects-betanull.github.io/mei-em-dia/mei-reforma-tributaria-2027-ibs-cbs-nota-fiscal/">MEI na Reforma Tributária em 2027</a> e veja como emitir no guia de <a href="https://projects-betanull.github.io/mei-em-dia/nota-fiscal-mei/">nota fiscal do MEI</a>.</p>
<h2>Calendário do MEI em 2027</h2>
<table><tr><th>Data</th><th>O que acontece</th></tr>
<tr><td>Fim de dezembro de 2026</td><td>Decreto do salário mínimo define o valor do DAS de 2027</td></tr>
<tr><td>1º de janeiro</td><td>Passam a valer o limite de R$ 110 mil, os 2 empregados, o perdão de dívidas e as regras da Reforma</td></tr>
<tr><td>A partir de janeiro</td><td>Já é possível enviar a DASN-SIMEI referente a 2026</td></tr>
<tr><td>22 de fevereiro</td><td>Vence o primeiro DAS com o valor novo (competência de janeiro)</td></tr>
<tr><td>Todo dia 20</td><td>DAS do mês anterior e <a href="https://projects-betanull.github.io/mei-em-dia/relatorio-mensal-de-receitas-brutas-mei/">relatório mensal de receitas</a></td></tr>
<tr><td>31 de maio</td><td>Fim do prazo da <a href="https://projects-betanull.github.io/mei-em-dia/dasn-simei-declaracao-anual-mei/">DASN-SIMEI</a> referente a 2026</td></tr>
<tr><td>Julho</td><td>Vence o DAS de junho, último do período exigido para manter o perdão</td></tr></table>
<h2>O que fazer ainda em 2026</h2>
<ol><li><strong>Confira o faturamento do ano.</strong> Em 2026 o limite ainda é R$ 81 mil; planeje novembro e dezembro se estiver perto.</li>
<li><strong>Não contrate o segundo empregado antes de janeiro.</strong> Em 2026 isso ainda tira a empresa do MEI.</li>
<li><strong>Consulte suas pendências</strong> na Receita Federal e no Regularize para saber o que entra no perdão.</li>
<li><strong>Teste seu acesso</strong> ao Emissor Nacional da NFS-e com a conta gov.br prata ou ouro.</li>
<li><strong>Atualize seu <a href="https://projects-betanull.github.io/mei-em-dia/controle-financeiro-mei/">controle financeiro</a></strong> para o teto de R$ 110 mil em janeiro.</li></ol>
"""))

# ---------------------------------------------------------------------------
# META: dados extras de cada guia.
#   grupo: nf | obr | ctrl | fin  (seção na página inicial)
#   pub/mod: datas de publicação e da última mudança real de conteúdo.
#            Ao alterar o texto de um guia, atualize "mod" SÓ desse guia.
#   resumo: 2-3 itens do quadro "Resposta rápida" no topo.
#   faq: perguntas frequentes (aparecem na página e na marcação FAQPage).
#   rel: 3 guias para o bloco "Leia também".
#   gratis: True mostra o quadro da planilha gratuita.
#   tit: título curto (até 60 caracteres) para a tag <title>, que é o que aparece no Google.
#        O h1 da página continua sendo o título completo do guia.
# Guia novo sem META ainda funciona, mas sem esses blocos e com a data de hoje.
# ---------------------------------------------------------------------------
GRUPOS=[("nf","Nota fiscal","mei"),("obr","Impostos, prazos e obrigações do MEI","mei"),("ctrl","Organização financeira do MEI","mei"),("fin","Finanças pessoais","financas")]
META={
"valor-aproximado-dos-tributos-nfs-e-mei":dict(grupo="nf",pub="2026-11-12",mod="2026-11-12",tit="Valor aproximado dos tributos na NFS-e do MEI: o que marcar",
 resumo=["O MEI marca <strong>\"Não informar nenhum valor estimado para os Tributos (Decreto 8.264/2014)\"</strong>.",
  "O artigo 8º do Decreto 8.264/2014 torna essa informação <strong>facultativa para o MEI</strong>, que paga os impostos em valor fixo no DAS.",
  "A opção pode ficar salva nas configurações do Emissor Nacional (ícone de engrenagem)."],
 faq=[("O que o MEI coloca em valor aproximado dos tributos na nota fiscal?","A opção \"Não informar nenhum valor estimado para os Tributos (Decreto 8.264/2014)\". O artigo 8º desse decreto torna a informação facultativa para o MEI."),
  ("O MEI é obrigado a informar os tributos na NFS-e?","Não. A Lei 12.741/2012 exige a informação nas vendas ao consumidor, mas o Decreto 8.264/2014 tornou a regra facultativa para o MEI."),
  ("Informei um valor de tributos por engano. Vou pagar mais imposto?","Não. O campo é só informativo para o cliente. O imposto do MEI é o valor fixo mensal do DAS, que não muda com o que aparece nesse campo.")],
 rel=["nota-fiscal-mei","nfs-e-nacional-simples-nacional-novembro-2026-mei","mei-reforma-tributaria-2027-ibs-cbs-nota-fiscal"]),
"mei-2027-o-que-muda":dict(grupo="obr",pub="2026-11-12",mod="2026-11-12",gratis=True,tit="MEI 2027: o que muda no limite, DAS, nota fiscal e prazos",
 resumo=["Limite sobe para <strong>R$ 110 mil</strong> e o MEI pode ter <strong>até 2 empregados</strong> (LC 238/2026).",
  "O DAS muda com o novo salário mínimo e ganha uma parcela fixa de R$ 1 de CBS e IBS.",
  "Nas vendas a pessoa física, a DASN-SIMEI poderá servir de documento fiscal. Dívidas do INSS do DAS vencidas até 13/10/2026 são perdoadas."],
 faq=[("Qual é o limite do MEI em 2027?","R$ 110 mil no ano, pela LC 238/2026, com média de R$ 9.166,67 por mês. Em 2026 o limite continua sendo de R$ 81 mil."),
  ("Qual vai ser o valor do DAS MEI em 2027?","Depende do salário mínimo, definido por decreto no fim de dezembro. Com a projeção de R$ 1.741, ficaria entre R$ 88,05 e R$ 93,05, mais uma parcela fixa de R$ 1 de CBS e IBS prevista na regulamentação."),
  ("Quantos funcionários o MEI pode ter em 2027?","Até dois, a partir de 1º de janeiro de 2027. Em 2026 o limite ainda é de um empregado."),
  ("O MEI vai acabar com a Reforma Tributária?","Não. O MEI continua existindo e pagando os impostos em valor fixo no DAS, que passa a incluir uma parcela de CBS e IBS.")],
 rel=["limite-mei-2027","das-mei-valor-vencimento","mei-reforma-tributaria-2027-ibs-cbs-nota-fiscal"]),
"mei-reforma-tributaria-2027-ibs-cbs-nota-fiscal":dict(grupo="nf",pub="2026-11-10",mod="2026-11-10",tit="MEI na Reforma Tributária 2027: DAS, IBS, CBS e nota",gratis=True,
 resumo=["A partir de <strong>1º/1/2027</strong>, o DAS ganha uma parcela fixa de CBS e IBS (R$ 0,994 + R$ 0,006). O MEI não calcula imposto por venda.",
  "A Resolução CGSN 190/2026 passa a exigir documento fiscal em toda venda, mas a <strong>DASN-SIMEI poderá servir de documento fiscal</strong> nas vendas a pessoa física (Resolução CGSN 195/2026).",
  "Para empresas e órgãos públicos, a nota continua obrigatória. O MEI segue dispensado de destacar IBS e CBS na nota."],
 faq=[("O MEI vai ter que emitir nota fiscal para pessoa física em 2027?","A Resolução CGSN 190/2026 retirou a dispensa a partir de 2027, mas a Resolução CGSN 195/2026 e o Decreto 13.140/2026 permitem usar a DASN-SIMEI como documento fiscal nas vendas a consumidor final pessoa física sem CNPJ. Se o cliente pedir a nota, ela deve ser emitida."),
  ("O MEI precisa destacar IBS e CBS na nota fiscal?","Não. A Resolução CGSN 190/2026 mantém o MEI dispensado de destacar IBS e CBS nos documentos fiscais, porque esses tributos são pagos em valor fixo dentro do DAS."),
  ("O DAS do MEI vai aumentar em 2027?","Sim, principalmente por causa do novo salário mínimo, que define a parte do INSS. Além disso, a regulamentação prevê uma parcela fixa de R$ 1 de CBS e IBS. O valor exato aparece no Portal do Empreendedor depois do decreto do salário mínimo.")],
 rel=["nota-fiscal-mei","das-mei-valor-vencimento","nfs-e-nacional-simples-nacional-novembro-2026-mei"]),
"limite-mei-2027":dict(grupo="obr",pub="2026-10-30",mod="2026-11-08",tit="Limite do MEI 2027: R$ 110 mil (e R$ 81 mil em 2026)",gratis=True,
 resumo=["Em 2026 o limite continua em <strong>R$ 81 mil</strong>. Pela LC 238/2026, sobe para <strong>R$ 110 mil em 2027</strong> e <strong>R$ 140 mil em 2028</strong>.",
  "Não existe limite mensal. Quem abre o MEI em 2027 tem R$ 9.166,67 por mês de atividade.",
  "Passou até 20% (R$ 132 mil em 2027): DAS complementar e vira ME em janeiro. Acima disso, o desenquadramento volta a janeiro."],
 faq=[("O limite de R$ 110 mil já vale em 2026?","Não. Até 31 de dezembro de 2026 o limite é de R$ 81 mil. O novo teto vale para o faturamento a partir de 1º de janeiro de 2027."),
  ("Quanto o MEI pode faturar por mês em 2027?","Não existe limite mensal, só o anual de R$ 110 mil. A média é de R$ 9.166,67 por mês, mas você pode faturar mais em um mês e menos em outro."),
  ("Vendas sem nota fiscal contam para o limite?","Sim. O limite considera o faturamento bruto: tudo o que você recebeu com vendas e serviços, com ou sem nota fiscal.")],
 rel=["mei-2027-o-que-muda","mei-pode-ter-funcionario","das-mei-valor-vencimento"]),
"relatorio-mensal-de-receitas-brutas-mei":dict(grupo="obr",pub="2026-10-30",mod="2026-11-08",tit="Relatório mensal do MEI: o que é e como preencher",gratis=True,
 resumo=["É obrigatório para todo MEI, mas <strong>não é enviado ao governo</strong>: você preenche, assina e guarda.",
  "Prazo: até o <strong>dia 20 do mês seguinte</strong>.",
  "Guarde os relatórios e as notas fiscais por <strong>5 anos</strong>."],
 faq=[("Preciso enviar o relatório mensal para algum lugar?","Não. Ele fica com você, junto com as notas fiscais de compras e vendas do mês, e serve de prova do faturamento em caso de fiscalização."),
  ("E se eu não faturei nada no mês?","O mais seguro é preencher o relatório com os valores zerados e guardá-lo, para manter a sequência de meses documentada."),
  ("O relatório mensal ajuda na declaração anual?","Sim. A soma dos 12 relatórios dá o faturamento do ano, separado em comércio, indústria e serviços, que é exatamente o que a DASN-SIMEI pede.")],
 rel=["planilha-relatorio-mensal-mei-gratis","dasn-simei-declaracao-anual-mei","limite-mei-2027"]),
"das-mei-valor-vencimento":dict(grupo="obr",pub="2026-10-30",mod="2026-11-10",tit="DAS MEI 2026 e 2027: valor, vencimento e atraso",gratis=True,
 resumo=["Em 2026: <strong>R$ 82,05</strong> (comércio/indústria), <strong>R$ 86,05</strong> (serviços) ou <strong>R$ 87,05</strong> (os dois). Vence no <strong>dia 20</strong>.",
  "Em 2027 o valor sobe com o novo salário mínimo (previsão de R$ 88,05 a R$ 93,05), mais uma parcela fixa de R$ 1 de CBS e IBS prevista pela Reforma.",
  "A parte do INSS das dívidas vencidas até 13/10/2026 será perdoada automaticamente em 2027, se você pagar em dia de janeiro a junho."],
 faq=[("Preciso pagar o DAS se não faturei nada?","Sim. O DAS é um valor fixo mensal e é devido mesmo nos meses sem faturamento."),
  ("Preciso pedir o perdão das dívidas do DAS?","Não. Segundo a PGFN e a Receita Federal, o cancelamento da parte do INSS vencida até 13/10/2026 é automático a partir de 1º de janeiro de 2027. Para manter o perdão, pague em dia o DAS de janeiro a junho de 2027."),
  ("Quando sai o valor oficial do DAS 2027?","Depois que o governo publicar o decreto do salário mínimo de 2027, o que costuma acontecer no fim de dezembro. O valor novo vale a partir da guia de janeiro, paga em fevereiro.")],
 rel=["mei-reforma-tributaria-2027-ibs-cbs-nota-fiscal","relatorio-mensal-de-receitas-brutas-mei","dasn-simei-declaracao-anual-mei"]),
"dasn-simei-declaracao-anual-mei":dict(grupo="obr",pub="2026-10-30",mod="2026-11-08",tit="DASN-SIMEI 2027: prazo e passo a passo da declaração",gratis=True,
 resumo=["A declaração do ano de 2026 vai até <strong>31 de maio de 2027</strong> e já pode ser enviada em janeiro.",
  "Informa a receita bruta do ano, a parte de comércio/indústria e se teve empregado. É obrigatória mesmo sem faturamento.",
  "Atraso gera multa de 2% ao mês sobre os impostos, com mínimo de <strong>R$ 50</strong>."],
 faq=[("Quem não faturou nada precisa entregar a DASN-SIMEI?","Sim. A entrega é obrigatória para todo MEI que esteve ativo no ano, mesmo com faturamento zero."),
  ("Na declaração de 2027 já vale o limite de R$ 110 mil?","Não. A declaração de 2027 é sobre o faturamento de 2026, cujo limite é de R$ 81 mil. O teto de R$ 110 mil vale para o faturamento de 2027, declarado em 2028."),
  ("A DASN-SIMEI substitui o imposto de renda da pessoa física?","Não. São declarações diferentes: a DASN-SIMEI é da empresa, e a obrigação de declarar o IR como pessoa física depende das suas rendas."),
  ("Errei a declaração. Dá para corrigir?","Sim. Envie uma declaração retificadora para o mesmo ano pelo Portal do Empreendedor, preenchendo todos os campos de novo.")],
 rel=["relatorio-mensal-de-receitas-brutas-mei","planilha-relatorio-mensal-mei-gratis","limite-mei-2027"]),
"nota-fiscal-mei":dict(grupo="nf",pub="2026-10-30",mod="2026-11-12",tit="Como emitir nota fiscal MEI e quando ela é obrigatória",gratis=True,
 resumo=["Hoje a nota é obrigatória para vendas e serviços a <strong>empresas (CNPJ)</strong> e órgãos públicos.",
  "Para pessoa física, só se o cliente pedir. Em 2027, a regra geral passa a exigir documento fiscal, mas a DASN-SIMEI poderá cumprir esse papel nessas vendas.",
  "A NFS-e de serviços é emitida de graça no <strong>Emissor Nacional</strong> (nfse.gov.br)."],
 faq=[("O MEI precisa emitir nota para pessoa física?","Até 31/12/2026, só se o cliente pedir. A partir de 2027, a Resolução CGSN 190/2026 exige documento fiscal em toda venda, mas a Resolução CGSN 195/2026 permite que a DASN-SIMEI cumpra essa função nas vendas a pessoa física sem CNPJ. Se o cliente pedir a nota, ela deve ser emitida."),
  ("Emitir nota fiscal de serviço tem custo?","Não. O Emissor Nacional da NFS-e (site e app) é gratuito; basta a conta gov.br nível prata ou ouro."),
  ("Venda sem nota entra no faturamento?","Sim. Ela entra no relatório mensal e conta para o limite anual de faturamento.")],
 rel=["valor-aproximado-dos-tributos-nfs-e-mei","mei-reforma-tributaria-2027-ibs-cbs-nota-fiscal","nfs-e-nacional-simples-nacional-novembro-2026-mei"]),
"mei-pode-ter-funcionario":dict(grupo="obr",pub="2026-10-30",mod="2026-11-08",tit="MEI pode ter funcionário? Regras e custo em 2026 e 2027",
 resumo=["Em 2026 o MEI pode ter <strong>1 empregado</strong>. A partir de 1º/01/2027, pela LC 238/2026, até <strong>2</strong>.",
  "Cada um recebe salário mínimo ou piso da categoria. Encargos: <strong>3% de INSS + 8% de FGTS</strong>.",
  "Custo direto em 2026: cerca de R$ 1.799 por empregado, mais 20% a 25% de 13º, férias e reservas."],
 faq=[("Posso contratar o segundo funcionário ainda em 2026?","Não. Em 2026 o limite continua sendo de 1 empregado, e contratar o segundo tira a empresa do MEI. A regra de até 2 vale a partir de 1º de janeiro de 2027."),
  ("Onde registro o funcionário do MEI?","No eSocial, no módulo simplificado, antes de a pessoa começar a trabalhar. Os encargos são pagos em uma guia única (DAE).")],
 rel=["limite-mei-2027","controle-financeiro-mei","das-mei-valor-vencimento"]),
"controle-financeiro-mei":dict(grupo="ctrl",pub="2026-10-30",mod="2026-11-08",tit="Controle financeiro para MEI: passo a passo com exemplo",
 resumo=["Separe a conta da empresa da pessoal e registre <strong>toda</strong> entrada e saída, com ou sem nota.",
  "Feche o mês até o dia 20: pague o DAS, preencha o relatório mensal e veja lucro, margem e uso do limite.",
  "Defina uma retirada fixa para você, com base no lucro médio."],
 faq=[("O MEI é obrigado a ter controle financeiro?","O MEI não precisa ter contabilidade formal, mas é obrigado a preencher o relatório mensal de receitas brutas e a guardar as notas fiscais de compras e vendas. Na prática, isso exige registrar todas as receitas."),
  ("Preciso registrar as despesas também?","Para o governo, o essencial são as receitas. Mas sem as despesas você não sabe o seu lucro, que é o número que mostra se o negócio vale a pena e quanto você pode retirar."),
  ("Posso usar minha conta pessoal para o MEI?","Pode, mas não é recomendado. Com uma conta só, fica muito difícil separar o que é do negócio, e o controle perde a utilidade."),
  ("Quanto tempo leva por mês?","Lançando as vendas no dia a dia, o fechamento do mês leva de 15 a 30 minutos.")],
 rel=["separar-dinheiro-pessoal-e-da-empresa-mei","relatorio-mensal-de-receitas-brutas-mei","limite-mei-2027"]),
"separar-dinheiro-pessoal-e-da-empresa-mei":dict(grupo="ctrl",pub="2026-10-30",mod="2026-11-08",tit="MEI: como separar o dinheiro pessoal do da empresa",
 resumo=["Receba e pague tudo do negócio por uma <strong>conta PJ</strong> separada.",
  "Defina uma retirada mensal fixa de cerca de <strong>60% a 70% do lucro médio</strong>.",
  "Registre a retirada como \"retirada do dono\", não como despesa."],
 faq=[("O MEI é obrigado a ter conta PJ?","Não há obrigação legal, mas a conta separada é a forma mais simples de saber o que é do negócio e o que é seu."),
  ("Quanto o MEI pode retirar por mês?","Não existe valor fixo por lei. Um ponto de partida é retirar de 60% a 70% do lucro médio dos últimos 3 meses e deixar o resto como reserva do negócio.")],
 rel=["controle-financeiro-mei","reserva-de-emergencia","como-fazer-orcamento-pessoal"]),
"planilha-relatorio-mensal-mei-gratis":dict(grupo="obr",pub="2026-10-30",mod="2026-11-12",tit="Planilha Relatório Mensal MEI grátis (Excel e Google)",
 resumo=["Planilha <strong>gratuita</strong>: você digita os valores do mês e o relatório sai no modelo oficial, pronto para imprimir.",
  "Soma o total do mês, o acumulado do ano e os valores da DASN-SIMEI.","Funciona no Excel e no Google Planilhas. Download direto, sem cadastro."],
 faq=[("A planilha grátis funciona no celular?","Sim, pelo app do Google Planilhas ou do Excel. Para imprimir, é mais fácil pelo computador."),
  ("Preciso me cadastrar para baixar?","Não. O download é direto pelo botão da página."),
  ("Posso usar a planilha para 2026?","Sim. Basta mudar o ano na aba \"Valores do ano\". O modelo do relatório é o mesmo."),
  ("Preciso imprimir o relatório ou posso guardar em PDF?","O relatório precisa ser assinado e guardado por 5 anos com as notas do mês. O caminho mais seguro é imprimir e assinar; se preferir o PDF, guarde também as notas e confirme com um contador se o formato atende ao seu caso."),
  ("O que faço nos meses sem faturamento?","Deixe os valores zerados, imprima o relatório do mês e guarde, para manter a sequência documentada.")],
 rel=["relatorio-mensal-de-receitas-brutas-mei","dasn-simei-declaracao-anual-mei","controle-financeiro-mei"]),
"como-fazer-orcamento-pessoal":dict(grupo="fin",pub="2026-10-30",mod="2026-11-08",
 resumo=["Parta da renda <strong>líquida</strong> e anote um mês inteiro de gastos.",
  "Divida em 50% necessidades, 30% desejos e 20% futuro (60-30-10 no começo também vale).",
  "Transforme em limites por categoria e guarde a parte do futuro assim que o dinheiro cair."],
 faq=[("E se as necessidades passarem de 50% da renda?","É comum no Brasil. Comece com 60-30-10 e vá aumentando a parte do futuro aos poucos."),
  ("Como fazer orçamento com renda variável?","Use a média dos últimos 3 meses, ou o menor valor entre eles, para ficar mais seguro.")],
 rel=["reserva-de-emergencia","como-sair-das-dividas","separar-dinheiro-pessoal-e-da-empresa-mei"]),
"reserva-de-emergencia":dict(grupo="fin",pub="2026-10-30",mod="2026-11-08",tit="Reserva de emergência: quanto guardar e onde deixar",
 resumo=["Guarde de <strong>3 a 6 meses de despesas</strong> (renda estável) ou de <strong>6 a 12 meses</strong> (autônomo ou MEI).",
  "Deixe em aplicação segura e com resgate no mesmo dia, como Tesouro Selic ou CDB com liquidez diária.",
  "Comece com a meta de um mês de despesas e um valor fixo por mês."],
 faq=[("Posso deixar a reserva na poupança?","A poupança é segura e tem resgate imediato, mas costuma render menos que Tesouro Selic ou CDB com liquidez diária."),
  ("Monto a reserva ou quito as dívidas primeiro?","Dívidas de juros altos, como rotativo do cartão e cheque especial, vêm primeiro, mantendo uma reserva mínima para não voltar ao crédito no próximo imprevisto.")],
 rel=["como-fazer-orcamento-pessoal","como-sair-das-dividas","separar-dinheiro-pessoal-e-da-empresa-mei"]),
"nfs-e-nacional-simples-nacional-novembro-2026-mei":dict(grupo="nf",pub="2026-10-31",mod="2026-11-08",tit="NFS-e Nacional: o que muda para o MEI em novembro de 2026",
 resumo=["Desde <strong>1º/11/2026</strong>, ME e EPP do Simples emitem a nota de serviço só pelo Emissor Nacional.",
  "O MEI já usa o Emissor Nacional desde setembro de 2023: para você, <strong>nada muda agora</strong>.",
  "O ISS continua municipal e, no MEI, segue dentro do DAS."],
 faq=[("O MEI precisa fazer algo novo por causa da mudança de novembro?","Não. O MEI já emite a NFS-e pelo Emissor Nacional desde setembro de 2023. A mudança vale para ME e EPP."),
  ("Onde o MEI emite a nota de serviço?","No site nfse.gov.br ou no app NFS-e Mobile, com a conta gov.br nível prata ou ouro.")],
 rel=["nota-fiscal-mei","valor-aproximado-dos-tributos-nfs-e-mei","limite-mei-2027"]),
"como-sair-das-dividas":dict(grupo="fin",pub="2026-11-03",mod="2026-11-08",tit="Como sair das dívidas: plano em 7 passos",
 resumo=["Liste todas as dívidas (o Registrato e a Serasa ajudam a achar as esquecidas).",
  "Quite primeiro as de <strong>juros mais altos</strong>: rotativo do cartão e cheque especial.",
  "Negocie à vista com desconto e só feche parcelas que cabem no orçamento."],
 faq=[("Por quanto tempo uma dívida pode deixar o nome negativado?","Pelo Código de Defesa do Consumidor, a negativação pode durar no máximo 5 anos. Depois de pagar, o credor deve pedir a retirada em até 5 dias úteis."),
  ("Vale pegar um empréstimo para quitar o cartão?","Pode valer se o Custo Efetivo Total for bem menor, a parcela couber no orçamento e você não voltar a usar o crédito que quitou.")],
 rel=["como-fazer-orcamento-pessoal","reserva-de-emergencia","separar-dinheiro-pessoal-e-da-empresa-mei"]),
}
TITULOS={a[0]:a[1] for a in A}; DESCS={a[0]:a[2] for a in A}

def com_resumo(b,itens):
    box='<div class="resumo"><strong>Resposta rápida</strong><ul>'+"".join(f"<li>{i}</li>" for i in itens)+"</ul></div>"
    k=b.index("</p>",b.index("</p>",b.index('<p class="data">'))+4)+4  # depois do 1º parágrafo do texto
    return b[:k]+box+b[k:]
def com_mini_cta(b,prod):
    pos=[]; k=-1
    while True:
        k=b.find("<h2>",k+1)
        if k<0: break
        pos.append(k)
    if len(pos)<4: return b
    return b[:pos[2]]+mini_cta(prod)+b[pos[2]:]

icones(); og_image("home","Guias práticos para o MEI e para o seu dinheiro")
sm=[]
for art in A:
    slug,t,d,b=art[:4]; prod=art[4] if len(art)>4 else "mei"
    m=META.get(slug,{})
    if not m: print("aviso: guia sem META:",slug)
    pub=m.get("pub",HOJE); mod=m.get("mod",HOJE); url=f"{BASE}/{slug}/"
    os.makedirs(f"{OUT}/{slug}",exist_ok=True); og_image(slug,t)
    grupo=m.get("grupo","fin" if prod=="fin" else "obr"); gnome=dict((g,n) for g,n,_ in GRUPOS)[grupo]; ganc=dict((g,a) for g,_,a in GRUPOS)[grupo]
    # cabeçalho: migalhas + h1 + data
    h1_fim=b.index("</h1>")+5
    crumbs=f'<nav class="crumbs"><a href="{BASE}/">Início</a> › <a href="{BASE}/#{ganc}">{gnome}</a></nav>'
    dt=f'<p class="data">Atualizado em {data_br(mod)}</p>'
    corpo=crumbs+b[:h1_fim]+dt+b[h1_fim:]
    if m.get("resumo"): corpo=com_resumo(corpo,m["resumo"])
    corpo=com_mini_cta(corpo,prod)
    if m.get("faq"):
        corpo+="<h2>Perguntas frequentes</h2>"+"".join(f"<h3>{q}</h3><p>{r}</p>" for q,r in m["faq"])
    if m.get("gratis"): corpo+=gratis_box()
    aviso='Conteúdo informativo, não é recomendação financeira individual.' if prod=='fin' else 'Conteúdo informativo. Regras podem mudar: confirme no Portal do Empreendedor ou com um contador.'
    corpo+=cta(prod)+'<p class="aviso">'+aviso+'</p>'
    rel=[r for r in m.get("rel",[]) if r in TITULOS]
    if rel:
        corpo+='<div class="rel"><h2>Leia também</h2><div class="lista">'+"".join(f'<a href="{BASE}/{r}/">{html.escape(TITULOS[r])}<span>{html.escape(DESCS[r])}</span></a>' for r in rel)+'</div></div>'
    corpo+=f'<p><a href="{BASE}/">← Todos os guias</a></p>'
    img=f"{BASE}/og/{slug}.png"
    sch=[{"@context":"https://schema.org","@type":"Article","headline":t,"description":d,"image":img,"datePublished":pub,"dateModified":mod,"inLanguage":"pt-BR","mainEntityOfPage":url,"author":ORG,"publisher":ORG},
         {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Início","item":f"{BASE}/"},{"@type":"ListItem","position":2,"name":gnome,"item":f"{BASE}/#{ganc}"},{"@type":"ListItem","position":3,"name":t,"item":url}]}]
    if m.get("faq"):
        sch.append({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":r}} for q,r in m["faq"]]})
    open(f"{OUT}/{slug}/index.html","w").write(page(slug+"/",m.get("tit",t),d,corpo,sch,img))
    sm.append((url,mod))

# página inicial, organizada por seções
def item(s): return f'<a href="{BASE}/{s}/">{html.escape(TITULOS[s])}<span>{html.escape(DESCS[s])}</span></a>'
secoes=""; anc_feita=set()
for g,nome,anc in GRUPOS:
    slugs=[a[0] for a in A if META.get(a[0],{}).get("grupo","fin" if (len(a)>4 and a[4]=="fin") else "obr")==g]
    if not slugs: continue
    idattr=f' id="{anc}"' if anc not in anc_feita else ""; anc_feita.add(anc)
    secoes+=f'<h2{idattr}>{nome}</h2><div class="lista">'+"".join(item(s) for s in slugs)+"</div>"
    if g=="fin": secoes+=cta("fin").replace(' id="oferta"','')
dest=f'<div class="dest"><small>Em destaque</small><a href="{BASE}/{DESTAQUE}/">{html.escape(TITULOS[DESTAQUE])}</a>{html.escape(DESCS[DESTAQUE])}</div>' if DESTAQUE in TITULOS else ""
home=f"""<div class="hero"><h1>Guias práticos para o MEI e para o seu dinheiro</h1><p>Limite de faturamento, DAS, nota fiscal, relatório mensal, declaração anual e organização financeira, explicados sem complicação.</p>
<a class="btn" href="{GRATIS}">Baixar a planilha grátis do relatório mensal</a></div>{dest}{secoes.replace('</div><h2 id="financas">','</div>'+cta().replace(' id="oferta"','')+'<h2 id="financas">',1)}"""
hsch=[{"@context":"https://schema.org","@type":"WebSite","name":SITE,"url":f"{BASE}/","inLanguage":"pt-BR","publisher":ORG},dict(ORG,**{"@context":"https://schema.org"})]
open(f"{OUT}/index.html","w").write(page("","MEI em Dia: guias práticos para o Microempreendedor Individual","Limite do MEI, DAS, nota fiscal, relatório mensal e DASN-SIMEI explicados de forma simples, além de guias de finanças pessoais.",home,hsch,tipo="website"))

# página Sobre (confiança e fontes)
SOBRE_MOD="2026-11-08"
sobre=f"""<nav class="crumbs"><a href="{BASE}/">Início</a></nav><h1>Sobre o MEI em Dia</h1><p class="data">Atualizado em {data_br(SOBRE_MOD)}</p>
<p>O MEI em Dia publica guias gratuitos e diretos sobre as obrigações do Microempreendedor Individual e sobre organização do dinheiro: limite de faturamento, DAS, nota fiscal, relatório mensal, declaração anual, orçamento e dívidas.</p>
<h2>De onde vêm as informações</h2>
<ul><li><strong>Portal do Empreendedor</strong> (gov.br/mei) e <strong>Receita Federal</strong>: regras do MEI, DAS e DASN-SIMEI.</li>
<li><strong>Lei Complementar 123/2006</strong> e resoluções do <strong>Comitê Gestor do Simples Nacional (CGSN)</strong>.</li>
<li><strong>Portal da NFS-e Nacional</strong> (nfse.gov.br): emissão de nota fiscal de serviço.</li>
<li><strong>Banco Central</strong> e órgãos de defesa do consumidor: crédito, dívidas e direitos do consumidor.</li></ul>
<h2>Como os guias são atualizados</h2>
<p>Cada guia mostra a data da última atualização. Quando uma regra muda (novo salário mínimo, novo prazo, mudança da Reforma Tributária), o guia é revisado. Valores que dependem de regra ainda em discussão aparecem identificados como previsão.</p>
<h2>Como o site se mantém</h2>
<p>O site é gratuito e se mantém com a venda de duas planilhas: a Planilha MEI 2027 e a Planilha Financeira Pessoal 2027. As chamadas para essas planilhas aparecem identificadas nos guias.</p>
<h2>Limites deste conteúdo</h2>
<p>Os guias são informativos e não substituem a orientação de um contador ou de um profissional de finanças para o seu caso. Confirme sempre as regras no Portal do Empreendedor.</p>
<p><a href="{BASE}/">← Todos os guias</a></p>"""
os.makedirs(f"{OUT}/sobre",exist_ok=True)
open(f"{OUT}/sobre/index.html","w").write(page("sobre/","Sobre o MEI em Dia: fontes e como os guias são feitos","O que é o MEI em Dia, de onde vêm as informações dos guias do MEI em Dia, como são atualizados e como o site se mantém.",sobre,[{"@context":"https://schema.org","@type":"AboutPage","name":"Sobre o MEI em Dia","url":f"{BASE}/sobre/","dateModified":SOBRE_MOD,"publisher":ORG}],tipo="website"))

ult=max(m for _,m in sm)
sm_xml=f"<url><loc>{BASE}/</loc><lastmod>{ult}</lastmod></url><url><loc>{BASE}/sobre/</loc><lastmod>{SOBRE_MOD}</lastmod></url>"+"".join(f"<url><loc>{u}</loc><lastmod>{m}</lastmod></url>" for u,m in sm)
open(f"{OUT}/sitemap.xml","w").write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm_xml}</urlset>')
open(f"{OUT}/robots.txt","w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
print("ok", len(A))
