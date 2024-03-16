class Friend:
    def __init__(self, name, given_gifts, received_gifts):
        self.name: str = name
        self.given: [Gift] = given_gifts
        self.given_cnt: int = self.calc_given_cnt()
        self.received: [Gift] = received_gifts
        self.received_cnt: int = self.calc_received_cnt()
        self.gift_efficient: int = self.calc_gift_efficient()
        self.recv_expected: int = 0

    def calc_given_cnt(self):
        cnt = 0
        for gift in self.given:
            cnt += gift.amount
        return cnt

    def calc_received_cnt(self):
        cnt = 0
        for gift in self.received:
            cnt += gift.amount
        return cnt

    def calc_gift_efficient(self):
        return self.given_cnt - self.received_cnt


class Gift:
    def __init__(self, sender, receiver, amount):
        self.sender: str = sender
        self.receiver: str = receiver
        self.amount: int = amount


class Logic:
    def __init__(self):
        self.friends = []
        self.gifts = []

    def setup_friends(self, raw_friends: [str]):
        for friend in raw_friends:
            given = self.findall_gift_sent(friend)
            received = self.findall_gift_recv(friend)
            self.friends.append(Friend(friend, given, received))

    def setup_gifts(self, raw_gifts: [str]):
        for gift in raw_gifts:
            sender, receiver = gift.split(" ")
            self.conditional_gift_create(sender, receiver)

    def conditional_gift_create(self, sender: str, receiver: str):
        exist_gift_info = self.is_gift_sent(sender, receiver)
        if exist_gift_info is None:
            self.gifts.append(Gift(sender, receiver, 1))
        else:
            exist_gift_info.amount += 1

    def is_gift_sent(self, sender, receiver) -> bool:
        for gift in self.gifts:
            if gift.sender == sender and gift.receiver == receiver:
                return gift
        return None

    def is_gift_exchanged(self, sender, receiver) -> bool:
        is_sent = False
        is_recv = False
        gift_sent_amount = 0
        gift_recv_amount = 0
        for gift in self.gifts:
            if gift.sender == sender and gift.receiver == receiver:
                is_sent = True
                gift_sent_amount = gift.amount
        for gift in self.gifts:
            if gift.sender == receiver and gift.receiver == sender:
                is_recv = True
                gift_recv_amount = gift.amount
        return is_sent or is_recv, gift_sent_amount, gift_recv_amount

    def findall_gift_sent(self, sender: str) -> [Gift]:
        results = []
        for gift in self.gifts:
            if gift.sender == sender:
                results.append(gift)
        return results

    def findall_gift_recv(self, receiver: str) -> [Gift]:
        results = []
        for gift in self.gifts:
            if gift.receiver == receiver:
                results.append(gift)
        return results

    def find_friend(self, name: str) -> Friend:
        for friend in self.friends:
            if friend.name == name:
                return friend

    def calc_recv_expected(self):
        for i in range(len(self.friends)):
            current = self.friends[i]
            for j in range(i + 1, len(self.friends), 1):
                partner = self.friends[j]
                is_exchanged, gift_sent_amount, gift_recv_amount = self.is_gift_exchanged(current.name, partner.name)

                # 선물주고받은 이력있고, 주고받은 개수가 같이 않은 경우
                if is_exchanged and gift_sent_amount > gift_recv_amount:
                    current.recv_expected += 1
                elif is_exchanged and gift_sent_amount < gift_recv_amount:
                    partner.recv_expected += 1
                # 주고받은 개수가 같거나, 이력이 없는 경우
                elif current.gift_efficient > partner.gift_efficient:
                    current.recv_expected += 1
                elif current.gift_efficient < partner.gift_efficient:
                    partner.recv_expected += 1
                print("{} -> {} = {} / {} / {}".format(current.name, partner.name, is_exchanged, current.recv_expected,
                                                       partner.recv_expected))

    def find_max_recv_expected(self):
        max_recv_expected = -10000000
        for friend in self.friends:
            if friend.recv_expected > max_recv_expected:
                max_recv_expected = friend.recv_expected
        return max_recv_expected


global_logic = Logic()


def solution(friends, gifts):
    global global_logic

    global_logic.setup_gifts(gifts)
    global_logic.setup_friends(friends)
    global_logic.calc_recv_expected()

    answer = global_logic.find_max_recv_expected()
    for gift in global_logic.gifts:
        print("{} -> {}, {}개".format(gift.sender, gift.receiver, gift.amount))

    for friend in global_logic.friends:
        print("{} - 준거: {}개 / 받은거: {}개 / 선물 지수: {} / 예상: {}개".format(friend.name, friend.given_cnt, friend.received_cnt,
                                                                     friend.gift_efficient, friend.recv_expected))

    print(answer)
    return answer
