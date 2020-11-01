from random import shuffle


class Card:
    """
    カードクラス

    Attributs:
        suit (list of str): マーク
        value (list of str): 番号
    """

    suits = ["spades", "hearts", "diamonds", "clubs"]

    values = [None, None,
              "2", "3", "4", "5", "6", "7", "8", "9", "10",
              "Jack", "Queen", "King", "Ace"]

    def __init__(self, v, s):
        """
        初期化関数

        Args:
            v (int): 何番目のマークか
            s (int): 何番のカードか
        """
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        """
        大小比較用の特殊メソッド
        """
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            return self.suit < c2.suit
        return False

    def __gt__(self, c2):
        """
        大小比較用の特殊メソッド
        """
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            return self.suit > c2.suit
        return False

    def __repr__(self):
        """
        print() のフォーマット用関数
        """
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v


class Deck:
    """
    デッキクラス

    Attributs:
        cards (list of Card): デッキ内のカードの配列
    """

    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def draw(self):
        """
        デッキから1枚カードを引き、デッキ内からそのカードを削除する
        """
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Player:
    """
    プレイヤークラス

    Attributs:
        wins (int): 勝ち数
        card (Card): 所持カード
        name (str): プレイヤー名
    """

    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    """
    ゲームクラス

    Attributs:
        deck (Deck): ゲームで使用するデッキ
        p1 (Player): プレイヤー1
        p2 (Player): プレイヤー2
    """

    def __init__(self):
        name1 = input("Name of Player1: ")
        name2 = input("Name of Player2: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def print_winner(self, winner):
        w = "{} win this round!"
        print(w.format(winner.name))

    def print_draw(self, p1, p2):
        d = "{} draw {}, {} draw {}"
        print(d.format(p1.name, p1.card, p2.name, p2.card))

    def play_game(self):
        cards = self.deck.cards
        print("GAME START!")
        while len(cards) >= 2:
            m = "finish with q, play with other keys: "
            response = input(m)
            if response == 'q':
                break
            self.p1.card = self.deck.draw()
            self.p2.card = self.deck.draw()
            self.print_draw(self.p1, self.p2)
            if self.p1.card > self.p2.card:
                self.p1.wins += 1
                self.print_winner(self.p1)
            else:
                self.p2.wins += 1
                self.print_winner(self.p2)

        win = self.winner(self.p1, self.p2)
        print("GAME FINISH! {} WIN!".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "Draw!"


game = Game()
game.play_game()
