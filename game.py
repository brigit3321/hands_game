import utils
import random

print("じゃんけんを始めます")

player_name = input("名前を入力してください:")

print("何を出しますか? (0: グー, 1: チョキ, 2: パー")

player_hand = int(input("数値で入力してください:"))

if utils.validate(player_hand):

    computer_hand = random.randint(0, 2)

    if player_name == "":
        utils.print_hand(player_hand)

    else:
        utils.print_hand(player_hand, player_name)

    utils.print_hand(computer_hand, "コンピューター")

    result = utils.judge(player_hand, computer_hand)

    print("結果は" + result + "でした")

else:
    print("正しい数値を入力してください")


