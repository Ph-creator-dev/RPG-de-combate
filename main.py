from RPG import *

def main():
    p1 = Mago('Teste', 1000, 1)
    p2 = Guerreiro('Exemplo', 1500, 2)

    p1.atacar(p2)

if __name__ == '__main__':
    main()