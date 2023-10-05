import random
import tkinter as tk
from tkinter import messagebox, Text

# Función para mezclar la baraja inglesa
def shuffle_deck():
    suits = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jota', 'Reina', 'Rey', 'As']
    deck = [{'palo': palo, 'valor': valor} for palo in suits for valor in values]
    random.shuffle(deck)
    return deck

# Función para repartir cartas a los jugadores
def deal_cards(num_players):
    deck = shuffle_deck()
    hands = [[] for _ in range(num_players)]
    
    if num_players < 2 or num_players > 4:
        messagebox.showerror("Error", "El número de jugadores debe estar entre 2 y 4.")
        return
    
    for _ in range(7):
        for player in hands:
            card = deck.pop()
            player.append(card)
    
    remaining_cards = deck
    
    # Mostrar las cartas restantes en una ventana
    result_window = tk.Toplevel()
    result_window.title("Cartas Restantes")
    result_text = Text(result_window)
    result_text.pack()
    
    result_text.insert(tk.END, "Cartas Restantes:\n")
    for i, card in enumerate(remaining_cards, start=1):
        result_text.insert(tk.END, f"Carta {i}: {card['valor']} de {card['palo']}\n")
    
    # Mostrar las manos de los jugadores en una ventana separada
    for i, hand in enumerate(hands, start=1):
        hand_window = tk.Toplevel()
        hand_window.title(f"Mano del Jugador {i}")
        hand_text = Text(hand_window)
        hand_text.pack()
        
        hand_text.insert(tk.END, f"Mano del Jugador {i}:\n")
        for card in hand:
            hand_text.insert(tk.END, f"{card['valor']} de {card['palo']}\n")

# Función para manejar el botón "Mezclar y repartir"
def shuffle_and_deal():
    num_players = int(num_players_entry.get())
    deal_cards(num_players)

# Crear la ventana principal
window = tk.Tk()
window.title("Mezclador de Cartas")

# Crear etiqueta y campo de entrada para el número de jugadores
num_players_label = tk.Label(window, text="Número de jugadores (entre 2 y 4):")
num_players_label.pack()

num_players_entry = tk.Entry(window)
num_players_entry.pack()

# Crear botón "Mezclar y repartir"
shuffle_button = tk.Button(window, text="Mezclar y Repartir", command=shuffle_and_deal)
shuffle_button.pack()

# Ejecutar la ventana principal
window.mainloop()
