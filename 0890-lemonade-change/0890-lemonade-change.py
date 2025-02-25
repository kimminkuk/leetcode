class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # input / output
        # stk 으로 생각해보면 되겠다.
        # 어 왜 틀림?? 틀리는 경우가 있나???
        # 아 모든 수표가 5달라가 아니지..
        output = []
        my_wallet_only_5 = []
        my_wallet_only_10 = []
        lemonade_bill = 5
        for bill in bills:
            if bill == lemonade_bill:
                my_wallet_only_5.append(bill)
            else:
                r = (bill - lemonade_bill)
                # r을 어떻게 조합하지?
                # r의 경우가, 5 or 15뿐임.
                # my_wallet에서 5, 10로 나눠야 할듯
                if r == 5:
                    if my_wallet_only_5:
                        my_wallet_only_5.pop()
                    else:
                        return False
                elif r == 15:
                    # 10, 5 1개 이상 있는 경우,
                    if my_wallet_only_10 and my_wallet_only_5:
                        my_wallet_only_5.pop()
                        my_wallet_only_10.pop()
                    # 5만 3개 있는 경우,
                    elif len(my_wallet_only_5) >= 3:
                        for _ in range(3): my_wallet_only_5.pop()
                    else:
                        return False


                # 20달라의 경우는, 돌려줄 수 있는 개념이 아님
                if bill == 10:
                    my_wallet_only_10.append(bill)
        return True



        