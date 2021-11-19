import time
# def main fez funcionar, só nao sei pq
def main():
    time.sleep(2)

    print("========================================================")
    print("--Seja Bem-vindo(a) à 'A Maldição do Condomínio Saeli--'")
    print("========================================================")

    time.sleep(1)

    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("Este jogo é baseado em fatos reais (alguns deles exagerados) e em invenções da minha mente doentia.")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    time.sleep(1)
    print("\nEssa história se passa em um condomínio de alto padrão em uma cidade litorânea.")
    time.sleep(1)
    print("O luxo e a comodidade do condomínio escondem um segredo antigo e obscuro.\n")
    time.sleep(1)
    print("No século passado, o terreno do condomínio abrigava um antigo cafezal,")
    print("no qual o barão do café Daniel tratava seus escravos com mão de ferro.\n")
    time.sleep(1)
    print("Quando as noites chegavam, alguns deles conseguiam fugir, porém vários outros eram recapturados.\n")
    time.sleep(1)
    print("E ao procurar pelos 'fujões', ele se utilizava de um castiçal de sete velas,")
    print("ganhando, entre os escravos, a alcunha de 'O Homem das Sete Velas'.\n")
    time.sleep(1)
    print("A abolição em 1888 fez com que o homem caísse em desgraça ao ver seu cafezal ruir, morrendo anos depois.\n")
    time.sleep(1)
    print("Apesar de morto há anos, o fantasma dele ainda perambula pelo local,") 
    print("querendo para si o que já foi dele e matando sem piedade quem aparece pelo caminho.\n")
    time.sleep(2)

    print("========================================================")
    print("========================================================\n")
    time.sleep(2)

    print("Hoje é dia de Finados e algumas pessoas estão na orla da lagoa do condomínio, aproveitando o feriado.\n")
    time.sleep(1)
    print("O dia, que estava bonito, fecha de repente e muitas das pessoas que ali estavam desaparecem sem deixar rastro.\n")
    time.sleep(1)
    print("Só há três pessoas na orla da lagoa. Quando olham para trás,\nelas veem o espírito do Homem das Sete Velas pairando sobre a água\ne indo em direção a elas, sedento de sangue.\n")
    time.sleep(1)

    print("==========")
    print("INSTRUÇÕES")
    print("==========\n")
    time.sleep(2)
    print("Selecione um dos três personagens e decida o destino deles.\nLembre-se: o Homem das Sete Velas não é o único perigo que ronda o condomínio.\nTodos eles começam em pontos diferentes da Rua 14, que contorna a orla da lagoa.\n")
    seleciona_personagem()

def seleciona_personagem():
    selecao = int (input ("Digite o número correspondente ao personagem:\n1 - Leandro\n2 - Marcos\n3 - Renata\nDigite 1, 2 ou 3. Ou digite 4 para sair: "))
    if selecao == 1:
        print("Você selecionou o personagem Leandro.")
        game_1()
    elif selecao == 2:
        print("Você selecionou o personagem Marcos.")
        game_2()
    elif selecao == 3:
        print("Você selecionou o personagem Renata.")
        game_3()
    elif selecao == 4:
        print("Tá com medinho?")
        time.sleep(2)
        quit()
    else:
        print("Esta opção não é válida. Digite novamente.")
        seleciona_personagem()

def personagem_vive():
    print("Você conseguiu sair com vida!\n")
    print("Deseja jogar novamente? (sim/não)")
    resposta = input("").upper().lower().strip()
    if resposta == 'sim':
        seleciona_personagem()
    else:
        print("Tá com medinho?")
        time.sleep(2)
        quit()
    
def personagem_morre():
    print("Você foi incapaz de sair de lá com vida.\n")
    print("Tentar novamente? (sim/não)")
    resposta = input("").upper().lower().strip()
    if resposta == 'sim':
        seleciona_personagem()
    else:
        print("Tá com medinho?")
        time.sleep(2)
        quit()
    
def game_1():
    print("De onde você está há dois caminhos possíveis para fugir, as Ruas 3 e 4.")
    print("Digite 1 para Rua 3 ou 2 para Rua 4.\n")
    resposta = int (input("Escolha: "))
    if resposta == 1:
        print("Você escolheu a Rua 3.\n")
        rua_3()
    elif resposta == 2:
        print("Você escolheu a Rua 4.\n")
        rua_4()
    else:
        print("Esta opção não é válida. Digite novamente.\n")
        game_1()

def rua_3():
    print("Na sua fuga, você se depara com uma casa de madeira.\nApesar de velha e acabada, ela pode ser um bom esconderijo.\n")
    print("Digite 1 para entrar na casa ou 2 para continuar sua fuga.")
    resposta = int (input("Escolha: "))
    if resposta == 1:
        print("Você escolheu se esconder na casa.\n")
        jogador_esconde()
    elif resposta == 2:
        print("Você continuou sua fuga.\n")
        jogador_continua_fuga()
    else:
        print("Esta opção não é válida. Digite novamente.\n")
        rua_3()

def jogador_esconde():
    print("Ao adentrar a casa antiga, você encontra uma velha lanterna,\nque por incrível que pareça, dá sinais de que funciona.")
    print("Digite 1 para pegar a lanterna ou 2 para deixá-la de lado.")
    resposta = int (input("Escolha: "))
    if resposta == 1:
        print("Você pegou a lanterna.\n")
        jogador_pega_lanterna()
    elif resposta == 2:
        print("Você deixou a lanterna de lado.\n")
        jogador_deixa_lanterna()
    else:
        print("Esta opção não é válida. Digite novamente.\n")
        jogador_esconde()
    
def jogador_continua_fuga():
    print("A princípio nada neste caminho apresenta perigo e, embora o Sete Velas continua a te caçar,\nmais algumas outras rotas se tornam disponíveis para você.")
    print("Digite 1 para entrar na Rua 12 ou 2 para entrar na Rua 13.")
    resposta = int (input("Escolha: "))
    if resposta == 1:
        print("Um morador do condomínio sai com seu carro da garagem.\nPorém ele está alcoolizado, não nota sua presença na rua e te atropela.\n")
        personagem_morre()
    elif resposta == 2:
        print("Você se depara com uma espécie de salão de festas.\nNele há um funcionário do condomínio que, ao ver seu desespero, resolve te ajudar a sair dali.\n")
        personagem_vive()
    else:
        print("Esta opção não é válida. Digite novamente.\n")
        jogador_continua_fuga()
    
def jogador_pega_lanterna():
    print("A velha lanterna lhe parece útil e você decide levá-la consigo.")
    print("Mas antes que consiga sair da velha casa, o mal tempo e os ventos fortes acabam por derrubá-la; você morre preso aos escombros.\n")
    personagem_morre()
    
def jogador_deixa_lanterna():
    print("Ao sair, você tropeça em alguns destroços e a noite impede você de ver um longo pedaço de madeira com pregos.")
    print("Um último tropeço projeta seu corpo em direção a ele, provocando um ferimento fatal na cabeça.\n")
    personagem_morre()
    
def rua_4():
    print("Na sua fuga, você se depara com uma velha casa.")
    print("Uma senhora está no quintal da casa e te oferece ajuda, enquanto cuida de alguns gatos.\n")
    print("Digite 1 para entrar ou 2 para seguir seu caminho.")
    resposta = int (input("Escolha: "))
    if resposta == 1:
        print("Você aceitou ajuda.\n")
        jogador_entra_mercedes()
    elif resposta == 2:
        print("Você seguiu em frente.\n")
        jogador_segue_pela_4() 
    else:
        print("Esta opção não é válida. Digite novamente.\n")
        rua_4()

def jogador_entra_mercedes():
    print("Ao entrar, você nota o cheiro característico de uma casa que possui dezenas de gatos.")
    print("Dona Mercedes, a senhora que ofereceu abrigo, também oferece um pouco de comida. O aspecto mal cuidado da casa provoca certo nojo.\n")
    print("Digite 1 para aceitar a comida ou 2 para recusar.")
    resposta = int (input("Escolha: "))
    if resposta == 1:
        print("Você aceitou comer.\n")
        jogador_come()
    elif resposta == 2:
        print("Você se recusou a comer.\n")
        jogador_recusa_comida()
    else:
        print("Esta opção não é válida. Digite novamente.\n")
        jogador_entra_mercedes()

def jogador_segue_pela_4():
    print("Uma placa suja escrito 'Saída' chama a atenção, mas fica a impressão de que nela há algo a mais escrito.")
    print("Digite 1 para seguir pela suposta saída ou 2 para limpar melhor a placa.")
    resposta = int (input("Escolha: "))
    if resposta == 1:
        print("Você seguiu para a saída.\n")
        jogador_paralelepipedo()
    elif resposta == 2:
        print("Você decidiu limpar a placa.\n")
        jogador_limpa_placa() 
    else:
        print("Esta opção não é válida. Digite novamente.\n")
        jogador_segue_pela_4()

def jogador_come():
    print("Você se surpreende com a comida oferecida; ela é muito saborosa!")
    print("Ao mesmo tempo que ela se satisfaz em ver você comendo bem, ela fica curiosa sobre sua fuga.")
    print("Você termina de comer e, por conta da sua gentileza com a idosa, ela se prontifica a conduzir você à saída.")
    print("Apesar da dificuldade de locomoção da Dona Mercedes, você consegue escapar. O Homem das Sete Velas desaparece.\n")
    personagem_vive()
    
def jogador_recusa_comida():
    print("O asco toma conta. De maneira educada, você recusa o prato.")
    print("Dona Mercedes, entretanto, não se sente contente. Você conta da sua fuga e ela ajuda, ainda que relutante.")
    print("Há um tom de mentira na voz dela...\n")
    print("Digite 1 para seguir o suposto conselho ou 2 para seguir sua intuição.")
    resposta = int (input("Escolha: "))
    if resposta == 1:
        print("Você seguiu a suposta orientação.\n")
        jogador_mentira_mercedes()
    elif resposta == 2:
        print("Você seguiu sua intuição.\n")
        jogador_segue_intuição()
    else:
        print("Esta opção não é válida. Digite novamente.\n")
        jogador_recusa_comida()

def jogador_paralelepipedo():
    print("Fugir do Sete Velas se tornou algo desesperador, mas sem fôlego e fraco você continua.")
    print("Um paralelepípedo solto na rua faz com que você tropece e caia.")
    print("Na queda, o Sete Velas chega rapidamente atrás de você, a fim de ceifar sua vida.\n")
    personagem_morre()

def jogador_limpa_placa():
    print("A placa na verdade diz: 'A única saída aqui é a morte'.")
    print("Sem que se dê conta, o Sete Velas está atrás de você ateando fogo em seu corpo.\n")
    personagem_morre()
    
def jogador_mentira_mercedes():
    print("Você adentra uma rua escura, sem identificação.")
    print("Nesse interim, a energia acaba em toda a área do condomínio.")
    print("Mas há uma luz, porém não era bem essa a luz que você tanto queria. O Sete Velas te capturou.\n")
    personagem_morre()

def jogador_segue_intuição():
    print("Você continua a empreender fuga desesperadamente, e sem se dar conta cai em um barranco criado pelas fortes chuvas dos dias anteriores.")
    print("Você fica preso ali e vai definhando dia após dia, sem que ninguém se dê conta.\n")
    personagem_morre()

def game_2():
    print("De onde você está há dois caminhos possíveis para fugir, as Ruas 7 e 8.")
    time.sleep(1)
    print("Digite 1 para Rua 7 ou 2 para Rua 8.\n")
    resposta = int (input("Escolha: "))
    if resposta == 1:
        print("Você escolheu a Rua 7.\n")
        rua_7()
    elif resposta == 2:
        print("Você escolheu a Rua 8.\n")
        rua_8()
    else:
        print("Esta opção não é válida. Digite novamente.\n")
        game_2()

def rua_7():
    print("Na sua fuga, você nota que esta é uma rua sem saída, mas no fim dela há um muro.")
    print("É possível pular este muro.\n")
    print("Digite 1 para pular o muro ou 2 para não pular e se desvenchilar do espírito maligno.")
    resposta = int (input("Escolha: "))
    if resposta == 1:
        print("Você pula o muro.\n")
        jogador_pulou_muro()
    elif resposta == 2:
        print("Você decide tentar se desvencilhar.\n")
        jogador_desvencilha()
    else:
        print("Esta opção não é válida. Digite novamente.\n")
        rua_7()

def jogador_desvencilha():
    print("Certamente uma atitude bastante corajosa, porém igualmente burra.")
    print("Ao vê-lo sem saída, o Homem das Sete Velas se torna cada vez mais sedendo de sangue.")
    print("Nenhuma oração, reza ou qualquer coisa foi capaz de afastá-lo de você.\n")
    personagem_morre()

def jogador_pulou_muro():
    print("O muro dá para os fundos de uma casa de número 464.")
    print("A casa é de uma família simpática com duas lindas crianças,")
    print("porém um Husky Siberiano branco, de grande porte e muito feroz começa a latir.\n")
    print("Digite 1 para acalmar o cão ou 2 para gritar por socorro.")
    resposta = int (input("Escolha: "))
    if resposta == 1:
        print("Você tentou acalmar o cachorro.\n")
        jogador_acalma_harry()
    elif resposta == 2:
        print("Você decide tentar se desvencilhar.\n")
        jogador_grita()
    else:
        print("Esta opção não é válida. Digite novamente.\n")
        jogador_pulou_muro()

def jogador_acalma_harry():
    print("O cão para de latir, passa a rosnar e se aproximar cada vez mais de você, como se fosse um lobo faminto.")
    print("Em um momento de distração, o cão vai direto no seu pescoço.\n")
    personagem_morre()
    
def jogador_grita():
    print("O seu grito de socorro é alto, mas não o suficiente para acordar a família do 464 do sono pesado.")
    print("Ao mesmo tempo, seu grito deixa o cachorro extremamente perturbado, e seguindo o seu instinto,")
    print("ele vai em sua direção arrancando partes dos seus membros. A perda de sangue te leva à morte minutos depois.")
    personagem_morre()
    
def rua_8():
    print("Uma bonita casa rosa chama a atenção durante sua fuga. Há relatos de que, no passado,")
    print("uma ex-moradora participou de um assassinato de grande repercussão no país.")
    print("Tal fato causa apreensão em todas as pessoas que passam em frente da casa.\n")
    print("Digite 1 para tocar a campainha ou 2 para pular o muro.")
    resposta = int (input("Escolha: "))
    if resposta == 1:
        print("Você tocou a campainha.\n")
        jogador_toca_campainha()
    elif resposta == 2:
        print("Você pulou o muro.\n")
        jogador_muro_casa_rosa()
    else:
        print("Esta opção não é válida. Digite novamente.\n")
        rua_8()

def jogador_toca_campainha():
    print("Depois de várias tentativas, ninguém vem ao seu encontro.")
    print("Você volta a correr e se depara com mais um cruzamento de ruas.\n")
    print("Digite 1 para entrar na Rua 5 ou 2 para entrar na Rua 6.")
    resposta = int (input("Escolha: "))
    if resposta == 1:
        print("Você entrou na Rua 5.\n")
        rua_5()
    elif resposta == 2:
        print("Você entrou na Rua 6.\n")
        rua_6()
    else:
        print("Esta opção não é válida. Digite novamente.\n")
        jogador_toca_campainha()

def rua_5():
    print("Ao correr por esta rua, você vê duas irmãs gêmeas de mãos dadas que te encaram com um olhar vazio.")
    print("Elas criam uma espécie de barreira que não permite você de continuar sua fuga. Por fim, o Sete Velas te alcança.\n")
    personagem_morre()
    
def rua_6():
    print("O movimento de alguns funcionários ao longe e das cancelas te enchem de esperança.")
    print("Parece que você encontrou a saída por conta própria.\n")
    personagem_vive()
    
def jogador_muro_casa_rosa():
    print("A casa vazia parece realmente bem cuidada, mas um barulho chama a atenção.")
    print("Você se aproxima e percebe que uma bela piscina está coberta por uma lona.")
    print("A lona se mexe, dando a entender que algo ou alguém está preso por baixo.\n")
    print("Digite 1 para remover a lona ou 2 voltar por onde veio.")
    resposta = int (input("Escolha: "))
    if resposta == 1:
        print("Você removeu a lona da piscina.\n")
        jogador_remove_lona()
    elif resposta == 2:
        print("Você resolveu voltar.\n")
        jogador_volta_mesmo_caminho()
    else:
        print("Esta opção não é válida. Digite novamente.\n")
        jogador_muro_casa_rosa()

def jogador_remove_lona():
    print("Você remove a lona da piscina. O espírito do Sete Velas te puxa pelas penas e te afoga.\n")
    personagem_morre()
    
def jogador_volta_mesmo_caminho():
    print("Por conta do medo, um movimento descuidado faz com que o sistema de alarme seja disparado.")
    print("Câmeras, luzes e cercas elétricas ocultas são ativadas.")
    print("Você é atingido por uma das cercas, recebendo uma forte descarga que carboniza seu corpo.")
    personagem_morre()
    
def game_3():
    print("De onde você está há dois caminhos possíveis para fugir, as Ruas 9 e 10.")
    print("Digite 1 para Rua 9 ou 2 para Rua 10.\n")
    resposta = int (input("Escolha: "))
    if resposta == 1:
        print("Você escolheu a Rua 9.\n")
        rua_9()
    elif resposta == 2:
        print("Você escolheu a Rua 10.\n")
        rua_10()
    else:
        print("Esta opção não é válida. Digite novamente.\n")
        game_3()

def rua_9():
    print("Na sua fuga, você se depara com uma casa na qual uma grande festa está ocorrendo.")
    print("Há vários carros de luxo e outros com placas indicando ser pertencentes a políticos.")
    print("Você decide buscar ajuda aqui, mas o segurança não parece estar muito dispostoa isso.\n")
    print("Digite 1 para apelar para o lado emocional do segurança ou 2 para agir grosseiramente.")
    resposta = int (input("Escolha: "))
    if resposta == 1:
        print("Você apelou para o emocional.\n")
        jogador_apela_emocional()
    elif resposta == 2:
        print("Você usou decidiu se valer da grosseria.\n")
        jogador_grosseiro()
    else:
        print("Esta opção não é válida. Digite novamente.\n")
        rua_9()

def jogador_apela_emocional():
    print("O segurança acompanha você até o dono da festa,")
    print("um atual candidato à prefeitura que parece disposto a te ajudar,")
    print("ainda que para 'fazer média' com alguns opositores presentes.\n")
    print("Ele sai de um quarto escuro que leva para um subsolo.")
    print("De lá, é possível ouvir gritos abafados e orações entoadas ao contrário.")
    print("Ao sair, ele te oferece uma bebida para acalmar os ânimos, mas o quarto ainda te atrai de alguma forma...\n")
    print("Digite 1 para verificar o quarto ou 2 para esperar o anfitrião voltar.")
    resposta = int (input("Escolha: "))
    if resposta == 1:
        print("Você verifica o quarto.\n")
        jogador_verifica_quarto()
    elif resposta == 2:
        print("Você decidiu esperar o anfitrião.\n")
        jogador_espera_anfitrião()
    else:
        print("Esta opção não é válida. Digite novamente.\n")
        jogador_apela_emocional()

def jogador_grosseiro():
    print("O segurança definitivamente não gostou dessa abordagem e decide não acolher você.")
    print("Você permanece nas ruas do condomínio, tentando encontrar a saída sem sucesso.")
    print("Você para de correr e decide caminhar, como se estivesse aceitando o seu destinho: seu encontro com o Sete Velas.\n")
    personagem_morre()
    
def jogador_verifica_quarto():
    print("Você desce as escadas para o subsolo. A umidade e o cheiro de vísceras tomam conta do ambiente.")
    print("Lá, algumas pessoas mascaradas e com vestes pretas observam você adentrar o recinto.")
    print("O cheiro ruim e os gritos eram de animais sendo sacrificados em um estranho ritual.")
    print("É até possível sair de lá, desde que você diga a senha correta.\n")
    print("Digite 1 para dizer que se enganou ou 2 para dizer a senha.")
    resposta = int (input("Escolha: "))
    if resposta == 1:
        print("Você afirma que se enganou e pede desculpas.\n")
        jogador_se_desculpa()
    elif resposta == 2:
        print("Você disse a senha.\n")
        jogador_diz_senha
    else:
        print("Esta opção não é válida. Digite novamente.\n")
        jogador_verifica_quarto()

def jogador_espera_anfitrião():
    print("O candidato tenta te acalmar e garante que irá ajudar você a sair.")
    print("Ele pede para que um dos seguranças te conduza até a saída.")
    print("Ao longo do caminho, percebe-se que o segurança não estava acompanhando você conforme o combinado,")
    print("mas sim o espírito do Sete Velas. Sabe como é promessa de político, né?\n")
    personagem_morre()

def jogador_se_desculpa():
    print("O líder do ritual se mostra piedoso a princípio,")
    print("mas afirma que a sua presença lá tem um motivo, embora você não sabe qual é.")
    print("Você é pego por trás e anestesiado por um pano embebido em éter.")
    print("Depois de algum tempo você ouve as mesmas orações estranhas de antes e, quando finalmente abre os olhos,")
    print("perecebe que está em uma maca, vendo seus membros sendo arrancados um a um.")
    print("A anestesia foi tão forte que nem forças para gritar você teve.")
    personagem_morre()
    
def jogador_diz_senha():
    print("Você diz 'edflio'. Sua tentativa de sair do quarto se mostrou infrutífera, o que desagrada o líder do ritual.")
    print("Todos ao redor se tornam hostis diante da sua presença, impedindo que você saia do cômodo às pressas.")
    print("Você é pego à força, é despido de suas roupas e é violentamente torturado com diversos instrumentos antigos.")
    print("Seus gritos são abafados pela festa que ocorre nos andares superiores, e o tal candidato sequer lembra que você esteve na festa.\n")
    personagem_morre()

def rua_10():
    print("Durante sua fuga, uma luxuosa casa acesa com uma bandeira do Brasil chama sua atenção, e você pede ajuda.")
    print("Um homem carrancudo, de quase 50 anos, resolve te convidar a entrar.")
    print("Enquanto o dono da casa busca um copo d'água, é possível ver uma coleção de diversas armas em uma parede.\n")
    print("Digite 1 para olhar as armas mais de perto ou 2 para permanecer no mesmo lugar, esperando o homem.")
    resposta = int (input("Escolha: "))
    if resposta == 1:
        print("Você foi verificar mais de perto as armas expostas.\n")
        jogador_verifica_armas()
    elif resposta == 2:
        print("Você decide esperar.\n")
        jogador_espera_sentado()
    else:
        print("Esta opção não é válida. Digite novamente.\n")
        rua_10()

def jogador_verifica_armas():
    print("Além das armas, há fotos com várias pessoas e políticos ligados a diversos crimes chocantes.")
    print("Medo e curiosidade tomam conta de você.\n")
    print("Digite 1 para fugir da casa ou 2 para questionar o homem.")
    resposta = int (input("Escolha: "))
    if resposta == 1:
        print("Você, com medo, decidiu fugir.\n")
        jogador_foge_medo()
    elif resposta == 2:
        print("Você resolve questionar aquilo tudo.\n")
        jogador_questiona()
    else:
        print("Esta opção não é válida. Digite novamente.\n")
        jogador_verifica_armas()

def jogador_espera_sentado():
    print("Quando ele volta, você conta toda a história da sua fuga.")
    print("Sendo uma pessoa corrupta, ele exige um pagamento de R$ 150 para ajudar você a sair do condomínio.\n")
    print("Digite 1 para pagar a propina ou 2 para se recusar.")
    resposta = int (input("Escolha: "))
    if resposta == 1:
        print("Você resolve pagar.\n")
        jogador_paga_propina()
    elif resposta == 2:
        print("Você se recusa a dar propina.\n")
        jogador_não_paga()
    else:
        print("Esta opção não é válida. Digite novamente.\n")
        jogador_espera_sentado()

def jogador_foge_medo():
    print("Com receio de ser desmascarado, o homem passa a te perseguir, mas por conta da idade, se cansa e resolve realizar um disparo em sua direção.")
    print("O tiro, que poderia ser fatal, acaba atingindo sua coxa direita.\n")
    print("Digite 1 para tentar estancar o sangramento ou 2 para continuar correndo mesmo assim.")
    resposta = int (input("Escolha: "))
    if resposta == 1:
        print("Você resolveu tratar o ferimento.\n")
        jogador_trata_ferida()
    elif resposta == 2:
        print("Você decidiu continuar correndo.\n")
        jogador_corre_sangrando()
    else:
        print("Esta opção não é válida. Digite novamente.\n")
        jogador_foge_medo()

def jogador_questiona():
    print("O homem se torna muito agressivo com sua atitude e te soca a cabeça com muita força.")
    print("Você apaga e ao acordar, se vê em um quarto totalmente branco, pequeno,\na prova de som, sem que ninguém a sua volta saiba da sua existência.\n")
    personagem_morre()

def jogador_paga_propina():
    print("Você paga, recolhendo todas as notas na sua carteira. A partir daí, ele passa a ter uma atitude um pouco mais amigável.")
    print("E durante o caminho até a saída, curiosamente, nenhum sinal da presença do Sete Velas...\n")
    personagem_vive()


def jogador_não_paga():
    print("Ele te conduz à saída de maneira relutante e um mal pressentimento paira no ar.")
    print("Logo ao sair, um dos seguranças externos recebe uma ordem para te matar, a fim de sanar a suposta dívida.")
    print("E antes mesmo de você ter qualquer noção do ocorrido, seu corpo inerte cai no chão com o impacto da bala na nuca.\n")
    personagem_morre()


def jogador_trata_ferida():
    print("A única coisa a disposição é o cinto da sua calça que você usa para estancar o sangramento.")
    print("O tempo perdido para se tratar foi suficiente para o espírito te alcançar.\n")
    personagem_morre()


def jogador_corre_sangrando():
    print("Quando mais você corre, mais sangue você perde. Começa a ficar tonto, fraco, sem fôlego e apaga.")
    print("Em um primeiro momento, você vê o espírito do Sete Velas bem distante.")
    print(" Só posteriormente é possível sentir a parafina derretida queimando sua pele...\n")
    personagem_morre()

main()