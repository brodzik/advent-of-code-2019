import numpy as np


class DeckOfCards:
    def __init__(self, n_cards):
        self.n_cards = n_cards
        self.cards = np.arange(n_cards)

    def find(self, value):
        return np.where(self.cards == value)

    def deal_into_new_stack(self):
        self.cards = np.flip(self.cards)

    def cut(self, n):
        self.cards = np.concatenate((self.cards[n:], self.cards[:n]))

    def deal_with_increment(self, n):
        temp = np.zeros(self.n_cards, dtype=int)
        i = 0

        for c in self.cards:
            temp[i] = c
            i = (i + n) % self.n_cards

        self.cards = temp


def main():
    deck = DeckOfCards(10007)

    with open("input.txt") as input_file:
        for line in input_file:
            line = line.strip().split(" ")
            if line[0] == "deal":
                if line[1] == "into":
                    deck.deal_into_new_stack()
                elif line[1] == "with":
                    deck.deal_with_increment(int(line[3]))
            elif line[0] == "cut":
                deck.cut(int(line[1]))

    print(deck.cards)
    print(deck.find(2019))


if __name__ == "__main__":
    main()
