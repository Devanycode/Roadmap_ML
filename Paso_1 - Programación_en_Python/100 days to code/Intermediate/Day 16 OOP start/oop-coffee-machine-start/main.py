from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()   # Es el Diccionario que contiene la información del Menú
money_machine = MoneyMachine()  # Tiene las funciones para imprimir el reporte de dinero y verificar si el pago es suficiente
coffe_maker = CoffeeMaker() 
"""Tiene los métodos para imprimir reporte de materiales,
verificar si hay materiales suficientes para la bebida pedida,
Deducir los ingredientes que necesite un objeto de MenuItem """


def report():
    coffe_maker.report()
    money_machine.report()
    start_machine()

def not_in_menu(input):
    while True:
        if input == "off":
            return False
        elif input == "report":
            report()
            return
        else:
            start_machine()
            return   

def start_machine():
    while True:
        items = menu.get_items()    # Devuelve las bebidas ofrecidas
        drink = input(f"What would you like? {items}: ").lower()    # Se pide al usuario que pida una bebida entre las opciones disponibles
        if drink in ["off", "report"]:  # Si tiene estos nombres clave se apagará la máquina o mostrará en pantalla los recursos actuales
            not_in_menu(drink)
            return
        drink_select = menu.find_drink(drink)  # Verifica que la bebida escrita está en MenuItem
        print(drink_select.cost)
        if drink_select != None:   # Si no devuelve None es que está en el Menú 
            if coffe_maker.is_resource_sufficient(drink_select) == True:    # Comprueba que hayan recursos suficientes para la bebida solicitada
                cost_drink = drink_select.cost  # Precio de la bebida seleccionada
                if money_machine.make_payment(cost_drink) == True:  # Se pide al usuario ingresar sus monedas
                    coffe_maker.make_coffee(drink_select)   # Si el valor ingresado es suficiente se prepara el café
                    return

 
start_machine()


