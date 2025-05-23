import random


class SequenceGame:
    def __init__(self):
        print(
            """
                ********************************
                    WELCOME TO SEQUENCE GAME    
                ********************************\n
        """
        )
        self.display_menu()

    def display_menu(self):
        print(
            """
                            menu
                ********************************
                Options: 
                    1. Jugar
                    2. Instrucciones - WIP
                    3. Salir
        """
        )
        menu_option = input(
            """
        ******************** > """
        )
        if menu_option == "1":
            self.start_game()
        elif menu_option == "2":
            self.instructions()
        else:
            print(
                """
                ********************************
                    THANKS FOR PLAYING, SEE YOU!    
                ********************************\n"""
            )

    def start_game(self):
        _sequence_to_guess = str(random.randint(100, 999))
        # print(_sequence_to_guess)
        print(
            """ 
                ***** GUESS THE SEQUENCE ******* 
                ********************************
                      You have 5 tries
                ********************************\n
            """
        )
        for tries in range(0, 4):
            enter_seq = input("Enter your secuence > ")
            second_line = ""
            if _sequence_to_guess == enter_seq:
                print(
                    f"""     
                            ***** YOU GOT IT ******* 
                        ********************************
                        You found in your {tries + 1} round
                        ********************************\n\n\n
                    """
                )
                break
            else:
                for pos in range(len(_sequence_to_guess)):
                    if _sequence_to_guess[pos] == enter_seq[pos]:
                        second_line += "^"
                    elif enter_seq[pos] in _sequence_to_guess:
                        second_line += "_"
                    else:
                        second_line += " "
                print(
                    f"""
                    {" ".join(second_line)}
                    {" ".join(enter_seq)}
                """
                )
        self.display_menu()

    def instructions(self):
        print("WIP")

    def main(self):
        self.display_menu()


seq_inst = SequenceGame()
seq_inst.display_menu()
