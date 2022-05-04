import PySimpleGUI as sg

# Configurar o layout
sg.theme('Black')
layout = [
    [sg.Text('Qual personagem mostrar:'), sg.Input(key='personagem')],
    [sg.Button('Click')],
    [sg.Output(size=(105,47))]
]

# Configuração da janela
janela = sg.Window('Menu Genshin Impact',layout)

# Ler os eventoss

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Click':
        if valores['personagem'] =='xiao': 
            print('''                                                             Xiao

Set de Artefatos: 4 peças do Set novo, seguindo os status de ATK - AnemoDMG - Crit Rate/Damage 
        
EnergyRecharge recomendado: 120%
        
Arma Recomendada: Jade Spear
       
Talentos: Prosperidade(Seg/Quinta)
        
Boss para matar: Dragato Primordial
        
Material necessário: Flor de Qinqxin
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=''')
       
       
        elif valores['personagem'] == 'zhongli':
            print('''                                                            Zhongli

Set de Artefatos: 4 peças do Milelith Firmes, seguindo os status de Vida - Vida - Vida.') 

Arma Recomendada: Borla Preta           

Talentos: Ouro(Quarta/Sabádo)  

Boss pra matar: Cubo Geo

Material necessário: Cor Lapis 
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=''')


        elif valores['personagem'] == 'jean':

            print('''                                                             Jean

Set de Artefatos: 2pc Glad 2pc VV, seguindo os status de ATK - AnemoDMG - Crit Rate/Damage ou Bônus de cura
        
EnergyRecharge recomendado: 180%
        
Arma Recomendada: Espada do sacrifício
       
Talentos: Resistência(Terça/Sexta)
        
Boss para matar: Cubo Anemo
        
Material necessário: Flor de Dandelion
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=''')
        
        
        elif valores['personagem'] == 'bennet':
            print('''                                                           Bennet

Set de Artefatos: 4 peças do Antigo Ritual Real, seguindo os status de Vida - Vida - Bônus de cura
        
EnergyRecharge recomendado: 220%
        
Arma Recomendada: Espada celestial
       
Talentos: Resistência(Terça/Sexta)
        
Boss para matar: Flor Pyro
        
Material necessário: Margaridas
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=''')


        elif valores['personagem'] == 'xingqiu':
            print('''                                                             Xingqiu

Set de Artefatos: 4pc Selo, seguindo os status de EnergyRecharge - HydroDMG - Crit Rate/Damage 
        
EnergyRecharge recomendado: 240%
        
Arma Recomendada: Espada do Sacrifício
       
Talentos: Ouro(Quarta/Sábado)
        
Boss para matar: Oceanid
        
Material necessário: Flor de Seda
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=''')


        elif valores['personagem'] == 'sucrose':
            print('''                                                            Sucrose

Set de Artefatos: 4 peças do Set novo, seguindo os status de Proficiência - Proficiência - Proficiência
        
EnergyRecharge recomendado: 120%
        
Arma Recomendada: Memórias de sacrifício
       
Talentos: Prosperidade(Seg/Quinta)
        
Boss para matar: Cubo Anemo
        
Material necessário: Margaridas
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=''')


        elif valores['personagem'] == 'diluc':
            print('''
Set de Artefatos: 4 peças do Set Bruxa Carmesim, seguindo os status de ATK - PyroDMG - Crit Rate/Damage 
        
EnergyRecharge recomendado: 100%
        
Arma Recomendada: Wolfsgrave
       
Talentos: Prosperidade(Terça/Sexta)
        
Boss para matar: Flor Pyro
        
Material necessário: Flor de Dandelion''')
        
        
        elif valores['personagem'] == 'xiangling':
            print('''                                                         Xiangling

Set de Artefatos: 4 peças do Set Selo da Insulação, seguindo os status de EnergyRecharge - PyroDMG - Crit Rate/Damage 
        
EnergyRecharge recomendado: 150%
        
Arma Recomendada: The Catch
       
Talentos: Prosperidade(Seg/Quinta)
        
Boss para matar: Flor Pyro
        
Material necessário: Pimenta de Jueyun
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=''')


        elif valores['personagem'] == 'keqing':
            print('''                                                           Keqing

Set de Artefatos: 2pc Glad 2pc Thundering Fury, seguindo os status de ATK - ElectroDMG - Crit Damage/Ratio.') 

Arma Recomendada: Flute
            
Talentos: Prosperidade(Segunda/Quinta/Domingo)

Boss pra matar: Cubo Electro  

Material necessário: Cor Lapis
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=''')


        elif valores['personagem'] == 'ningguang':
            print('''                                                          Ningguang

Set de Artefatos: 4 peças do Set novo, seguindo os status de ATK - GeoDMG - Crit Rate/Damage 
        
EnergyRecharge recomendado: 120%
        
Arma Recomendada: Lost Winds
       
Talentos: Prosperidade(Seg/Quinta)
        
Boss para matar: Cubo Geo
        
Material necessário: Lírio de Vidro
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=''')