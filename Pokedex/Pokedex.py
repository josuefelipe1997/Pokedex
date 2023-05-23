import Dados_Pokemon
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

#################### CRIA A TELA DA POKEDEX FECHADA ####################
def open_pokedex():
    janela = tk.Tk()
    janela.title('POKEDEX')
    janela.geometry('425x600')
    image = tk.PhotoImage(file='imagens\\imagens_pokedex\\PokedexClosed.png')
    image = image.subsample(1,1)
    label_imagem = tk.Label(image=image)
    label_imagem.place(x=0, y=0, relwidth=1.0, relheight=1.0)

    botao_abrir = PhotoImage(file='imagens\\imagens_pokedex\\AbrirPokedex.png')
    botao_abrir = botao_abrir.subsample(1,1)        

    abrir_pokedex = Button(janela, command=janela.destroy,image=botao_abrir,bd=0.5, cursor="hand2", highlightthickness=0, bg="#C70017")
    abrir_pokedex.place(x=30, y=290)

    janela.mainloop()

#################### REALIZA A ABERTURA DA POKEDEX ####################
open_pokedex()

#################### CORES ####################
co0 = "#000000"  # Preta
co1 = "#30FB05"  # Verde
co3 = "#FFFFFF"  # Branco
co4 = "#FB0505"  # Vermelho

#################### CRIA A TELA DA POKEDEX ABERTA ####################
janela = tk.Tk()
janela.title('POKEDEX')
janela.geometry('800x600')
janela.configure(bg='gray')

image = tk.PhotoImage(file='imagens\\imagens_pokedex\\PokedexOpen.png')
image = image.subsample(1,1)
label_imagem = tk.Label(image=image)
label_imagem.place(x=0, y=0, relwidth=1.0, relheight=1.0)

#################### FUNÇÃO QUE JÁ INICIA A POKEDEX COM O BULBASAUR ####################
def pokemon_inicial():
    global nome_do_pokemon
    nome_do_pokemon = 'bulbasaur'
    pokemon = Dados_Pokemon.main(nome_do_pokemon)
    trocar_pokemon(pokemon)
    return pokemon

#################### FUNCÃO QUE REALIZA A BUSCA DO POKEMON ####################
def busca_pokemon():
    global nome_do_pokemon
    nome_do_pokemon = str(nome_pokemon_busca.get())
    nome_do_pokemon = nome_do_pokemon.lower()
    pokemon = Dados_Pokemon.main(nome_do_pokemon)
    trocar_pokemon(pokemon)
    return pokemon

#################### FUNÇÃO QUE TROCA AS INFORMAÇÔES DOS POKEMONS NA TELA ####################
def trocar_pokemon(pokemon):
    global imagem_pokemon

    #################### TIPO POKEMON ####################
    nome_poke = list(pokemon.keys())[0]
    pok_nome['text'] = nome_poke.capitalize()

    pok_tipo_1['text'] = ''
    pok_tipo_2['text'] = ''

    if len(pokemon[nome_do_pokemon]['tipo']) == 3:
        poke_tip_1 = pokemon[nome_do_pokemon]['tipo'][1]
        pok_tipo_1['text'] = poke_tip_1.capitalize()
        poke_tip_2 = pokemon[nome_do_pokemon]['tipo'][2]
        pok_tipo_2['text'] = poke_tip_2.capitalize()

    else:
        pok_tipo_1['text'] = pokemon[nome_do_pokemon]['tipo'][1]
    pok_id['text'] = f"#{pokemon[nome_do_pokemon]['tipo'][0]}"

    #################### IMAGEM DO POKEMON ####################
    imagem_pokemon = f'imagens\\imagens_pokemon\\{nome_do_pokemon}.png'
    imagem_pokemon = Image.open(imagem_pokemon)
    imagem_pokemon = imagem_pokemon.resize((325,325))
    imagem_pokemon = ImageTk.PhotoImage(imagem_pokemon)

    pok_imagem = Label(janela, image=imagem_pokemon, relief='flat', anchor=CENTER, fg=co1)
    pok_imagem.place(x=30, y=155)

    #################### STATUS DO POKEMON ####################
    pok_status['text'] = 'Status'
    pok_hp['text'] = f"HP: {pokemon[nome_do_pokemon]['status']['hp']}"
    pok_ataque['text'] = f"Ataque: {pokemon[nome_do_pokemon]['status']['attack']}"
    pok_defesa['text'] = f"Defesa: {pokemon[nome_do_pokemon]['status']['defense']}"
    pok_spec_ataque['text'] = f"Special Ataque: {pokemon[nome_do_pokemon]['status']['special-attack']}"
    pok_spec_defesa['text'] = f"Special Defesa: {pokemon[nome_do_pokemon]['status']['special-defense']}"
    pok_velocidade['text'] = f"Velocidade: {pokemon[nome_do_pokemon]['status']['speed']}"

    ##### HABILIDADES DO POKEMON #####
    pok_habilidades['text'] = 'Habilidades'

    try:
        poke_hab_1 = pokemon[nome_do_pokemon]['habilidades'][0]
        pok_habilidade_1['text'] = poke_hab_1.capitalize()
    except:
        pok_habilidade_1['text'] = ''
    try:
        poke_hab_2 = pokemon[nome_do_pokemon]['habilidades'][1]
        pok_habilidade_2['text'] = poke_hab_2.capitalize()
    except:
        pok_habilidade_2['text'] = ''
    try:
        poke_hab_3 = pokemon[nome_do_pokemon]['habilidades'][2]
        pok_habilidade_3['text'] = poke_hab_3.capitalize()
    except:
        pok_habilidade_3['text'] = ''
    try:
        poke_hab_4 = pokemon[nome_do_pokemon]['habilidades'][3]
        pok_habilidade_4['text'] = poke_hab_4.capitalize()
    except:
        pok_habilidade_4['text'] = ''

#################### NOME ####################
pok_nome = Label(janela, text='', relief='flat', anchor=CENTER, font=('Fixedsys 30 bold'),bg=co1, fg=co0)
pok_nome.place(x=470, y=160)

#################### CATEGORIA ####################
pok_tipo_1 = Label(janela, text='', relief='flat', anchor=CENTER, font=('Ivy 12 italic'), bg=co1, fg=co0)
pok_tipo_1.place(x=470, y=210)

pok_tipo_2 = Label(janela, text='', relief='flat', anchor=CENTER, font=('Ivy 12 italic'), bg=co1, fg=co0)
pok_tipo_2.place(x=535, y=210)

#################### ID ####################
pok_id = Label(janela, text='', relief='flat', anchor=CENTER, font=('Ivy 15 bold'), bg=co1, fg=co0)
pok_id.place(x=700, y=160)

#################### STATUS ####################
pok_status = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 15'), bg=co1, fg=co0)
pok_status.place(x=470, y=325)

# HP
pok_hp = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
pok_hp.place(x=470, y=375)

# ATAQUE
pok_ataque = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
pok_ataque.place(x=470, y=400)

# DEFESA
pok_defesa = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
pok_defesa.place(x=470, y=425)

# SPECIAL ATAQUE
pok_spec_ataque = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
pok_spec_ataque.place(x=470, y=450)

# SPECIAL DEFESA
pok_spec_defesa = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
pok_spec_defesa.place(x=470, y=475)

# VELOCIDADE
pok_velocidade = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
pok_velocidade.place(x=470, y=500)

#################### HABILIDADE ####################
pok_habilidades = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 15'), bg=co1, fg=co0)
pok_habilidades.place(x=640, y=325)

# HABILIDADE 1
pok_habilidade_1 = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
pok_habilidade_1.place(x=640, y=375)

# HABILIDADE 2
pok_habilidade_2 = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
pok_habilidade_2.place(x=640, y=400)

# HABILIDADE 3
pok_habilidade_3 = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
pok_habilidade_3.place(x=640, y=425)

# HABILIDADE 4
pok_habilidade_4 = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
pok_habilidade_4.place(x=640, y=450)


#################### ABRINDO POKEDEX COM O PRIMEIRO POKEMON ####################
pokemon_inicial()

#################### CRIANDO CAMPO E BOTÃO PESQUISA POKEMON ####################
# CAMPO NOME POKEMON
nome_pokemon_busca = Entry(janela, textvariable='Pokemon', relief='sunken', bg=co4, fg=co0)
nome_pokemon_busca.place(x=235, y=60, width=140, height=25)

#nome_pokemon_busca.place(x=625, y=10, width=170, height=25)

# BOTÃO PESQUISAR
pesquisar = PhotoImage(file='imagens\\imagens_pokedex\\Pokeball.png')
pesquisar = pesquisar.subsample(3,3)

botao_pesquisar = Button(janela, command=busca_pokemon,image=pesquisar,bd=0.5, highlightthickness=0, bg=co4)
botao_pesquisar.place(x=342, y=90)

janela.mainloop()