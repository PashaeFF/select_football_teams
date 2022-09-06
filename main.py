import selected_options

class FootballTeam(selected_options.SelectedFunctions):
    
    def main(self):
        while True:
            
            print(self.main_text)
            select_main = input("Reqem daxil et: ")
            print(f"\n{self.star}\n")

            if select_main == "1":
                self.list_footballer()

            elif select_main == "2":
                return self.add_human()
            elif select_main == "3":
                return self.delete_human()
            elif select_main == "4":
                return self.select_teams()
            elif select_main == "5":
                return self.last_selected_teams()
            elif select_main == "q" or select_main == "Q":
                return exit()
            else:
                print(self.wrong_input)
                self.main()


        

call = FootballTeam()
call.main()
# call.list_fo
# otballer()
# call.add_human()
# call.delete_human()
# call.select_teams()
# call.count_difference()
# call.last_selected_teams()