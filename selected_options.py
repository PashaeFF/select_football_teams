import check
import random
from  data import last_yellow_dresseds_team, last_teams
if hasattr(last_yellow_dresseds_team,"last_yellow_dresseds_team"):
    last_yellow_dresseds_team =  last_yellow_dresseds_team.last_yellow_dresseds_team
else:
    last_yellow_dresseds_team = []
if hasattr(last_teams,"last_team_1"):
    last_team_1 =  last_teams.last_team_1
else:
    last_team_1 =  []

if hasattr(last_teams,"last_team_2"):
    last_team_2 =  last_teams.last_team_2
else:
    last_team_2 =  []

class SelectedFunctions(check.CheckAndSolv):
############ return main page  ###########
    def return_main(self):
        back = input(self.back_text)
        back = back.capitalize()
        print(f"\n{self.star}\n")
        if back == "B":
            self.main()

    # 1 ########### Futbolchularin listi ###########
    def list_footballer(self):
        print(self.footballers_list_text)
        for number, human in enumerate(self.humans, 1):
            print(f"{number}) {human['name']} ({human['rating']})")
        self.return_main()
        
    # 2 ########### Futbolchu elave et ###########
    def add_human(self):
        print(self.add_human_text)
        print(self.back_text)
        self.add_name += input("Oyunchunun adi: ")

        self.add_name = self.add_name.capitalize()
        if self.add_name == "B":
            self.main()
        self.add_rating_number = (input("Oyunchunun reytinqi (40-100 arasi): "))
        if self.add_rating_number.isdigit():
            self.add_rating_number = int(self.add_rating_number)
            if self.add_rating_number < 40 or self.add_rating_number > 100:
                print("Max.100, min. 10 verile biler")
                self.add_human()
            else:
                self.humans.append({'name': self.add_name, 'rating': self.add_rating_number})
                print(self.human_read())
                self.return_main()
        else:
            print(self.select_number_text)
        

    # 3 ######## Oyunchu sil ###########
    def delete_human(self):
        print(self.delete_human_text)
        print(self.back_text)
        for number, human in enumerate(self.humans, 1):
            print(f"{number}) {human['name']} ({human['rating']})")
        select_for_delete = input("Silmek istediyin oyunchunun qarshisindaki reqemi qeyd et: ")

        if select_for_delete.isdigit():
            select_for_delete = int(select_for_delete)
            for number, human in enumerate(self.humans, 1):
                if number == select_for_delete:
                    print(f"id {number} olan {human['name']} oyunchunu sildiniz...")
                    self.humans.pop(number-1)

        elif select_for_delete == "b":
            self.main()

        elif select_for_delete == "B":
            self.main()
        else:
            print(self.select_number_text)

        self.return_main()

    # 4 ######## Oyunchulari Komandalara bol ###########
    def select_teams(self):
        self.rating_optimization()
        self.team_1.clear()
        self.team_1 = random.sample(self.level_1, k=len(self.level_1)//2) + random.sample(self.level_2, k=len(self.level_2)//2) + random.sample(self.level_3, k=len(self.level_3)//2)
        self.team_2.clear()
        for i in self.humans:
            if i in self.team_1:
                continue
            else:  
                self.team_2.append(i)
        
                
        self.count_difference()


    # 5 ######## Son sechilen oyunchular ve nakidka geyinenler ###########
    def last_selected_teams(self):
        last = last_teams
        yellow_d = last_yellow_dresseds_team
        yellow_s = ""
        power_1 = 0
        for num, human in enumerate(last.lats_team_1,1):
            print(f"{num}) {human['name']} => {human['rating']}")
            power_1 += human['rating']
        print(f"\nTeam Power: {power_1}\n")
        power_2 = 0
        for num, human in enumerate(last.lats_team_2,1):
            print(f"{num}) {human['name']} => {human['rating']}")
            power_2 += human['rating']
        print(f"\nTeam Power: {power_2}")
        for i in yellow_d:
            yellow_s += i['name']+", "
            
        print("Son nakidka geyinenler: ", yellow_s[0:-2])
        
        self.return_main()