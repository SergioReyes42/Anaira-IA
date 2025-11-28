# main.py
from src.chatbot import ChatBot
from src.tax_calculator import TaxCalculator
from src.accounting import Accounting
from src.nlp_module import NLPModule

def main():
    print("Bienvenido a Anaira IA - Asistente Contable y Fiscal para Guatemala")
    bot = ChatBot()
    nlp = NLPModule()

    while True:
        pregunta = input("¿En qué puedo ayudarte hoy? (Escribe 'salir' para terminar): ")
        if pregunta.lower() == "salir":
            break
        # Primero intentamos NLP
        respuesta_nlp = nlp.responder(pregunta)
        if respuesta_nlp:
            print("IA (NLP):", respuesta_nlp)
        else:
            print("IA:", bot.responder(pregunta))

if __name__ == "__main__":
    main()
