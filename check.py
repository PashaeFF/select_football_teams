import static
import random
from  data import last_yellow_dresseds_team
if hasattr(last_yellow_dresseds_team,"last_yellow_dresseds_team"):
    last_yellow_dresseds_team =  last_yellow_dresseds_team.last_yellow_dresseds_team
else:
    last_yellow_dresseds_team = []

class CheckAndSolv(static.Static):
    ############ rating optimization  ###########
      ######## select team ########
    def rating_optimization(self):
        for i in self.humans:
            if i['rating'] < 61 and i not in self.level_3:
                self.level_3.append(i)
            elif 60 < i['rating'] < 81  and i not in self.level_2:
                self.level_2.append(i)
            elif 80 < i['rating']  and i not in self.level_1:
                self.level_1.append(i)

    
    
    ############ Selected teams ################
    def selected_teams(self): 
        f = open("data/last_teams.py", "w")
        
        f.write(f"""lats_team_1 = {self.team_1}
lats_team_2 = {self.team_2}""")
        f.close()
        n = open("data/last_yellow_dresseds_team.py", "w")
        
        d = []
        if isinstance(self.yellow, list):
            for i in self.yellow:
                for e in i:
                    d.append(e)
        n.write(f"last_yellow_dresseds_team = {d}")
        n.close()


        
    

        
    ######### Selected teams result OK or... #############
    def ok(self):
        ok = input("Netice ile razisiniz? H/Y: ")
        ok = ok.capitalize()
        if ok == "H":
            self.selected_teams()
            self.return_main()
        elif ok == "Y":
            self.select_teams()


    #print teams, power and dress
    def team_print(self):
        yellow_d = last_yellow_dresseds_team
        
        self.form_1 = 0
        self.form_2 = 0
        for i in yellow_d:
            for e in self.team_1:
                if i['name'] == e['name']:
                    self.form_1 += 1
        for i in yellow_d:
            for e in self.team_2:
                if i['name'] == e['name']:
                    self.form_2 += 1
        print("Kechen oyun Team 1 uzre forma geyinenlerin sayi: ", self.form_1)
        print("Kechen oyun Team 2 uzre forma geyinenlerin sayi: ", self.form_2)
        
        self.form = random.choice(self.teams)
        #Team 1
        print("\nTeam 1: ")
        power_1 = 0
        for number, human in enumerate(self.team_1, 1):
            print(f"{number}) {human['name']} => {human['rating']}")
            power_1 += human['rating']

        print(f"\nTeam Power: {power_1}")
        if self.form_1 < self.form_2:
            print(f'> Team 1 < nakidka geyinmelidir...')
            self.yellow.append(self.team_1)
        
        #Team 2
        print("\nTeam 2: ")
        power_2 = 0
        for number, human in enumerate(self.team_2, 1):
            print(f"{number}) {human['name']} => {human['rating']}")
            power_2 += human['rating']

        print(f"\nTeam Power: {power_2}")
        if self.form_1 > self.form_2:
            print(f'> Team 2 < nakidka geyinmelidir...')
            self.yellow.append(self.team_2)

        if self.form_1 == self.form_2:
            print(f'{self.form} nakidka geyinmelidir...')
            self.yellow.append(self.team_1)

        
        
        self.ok()
            
                
          
    #Difference check and solv:
    def count_difference(self):
        len_1 = len(self.team_1)
        len_2 = len(self.team_2)
        h_list = []

        
        if len_1 > len_2:
            for i in self.team_1:
                if i not in self.team_2:
                    if 100 >= i['rating'] >= 70:
                        h_list.append(i)
            len_3 = len_1 - len_2
            
            for i in h_list[-len_3//2:]:
                self.team_2.append(i)
                self.team_1.remove(i)
            self.team_print()
            
        elif len_1 < len_2:
            for i in self.team_2:
                if i not in self.team_1:
                    if 100 >= i['rating'] >= 70:
                        h_list.append(i)
            len_3 = len_2 - len_1
            
            for i in h_list[-len_3//2:]:
                self.team_1.append(i)
                self.team_2.remove(i)
            self.team_print()
        else:
            self.team_print()

