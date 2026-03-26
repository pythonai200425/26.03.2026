

class Auction:

    def __init__(self, max_offers):
        self.__max_offers = max_offers
        self.__offers = []
        # max 3: 80 90 110 -- 115 --> 90 110 115

    def offer_bidding(self, price) -> bool:
        if price <= 0:
            return False
        if not self.__offers or price > self.__offers[-1]:
            if len(self.__offers) == self.__max_offers:
                self.remove_lowest()
            self.__offers.append(price)
            return True
        return False

    def get_winner(self) -> int:
        return self.__offers[-1]

    def remove_lowest(self) -> int:
        # 80 90 100 110 -> 90 100 110
        lowest = self.__offers.pop(0)
        return lowest

    def get_offers(self) -> list[int]:
        return self.__offers.copy()

    def get_max_offers(self):
        return self.__max_offers

