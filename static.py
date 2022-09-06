
class Static():
    def __init__(self):
        #List humans
        self.humans = [{'name': 'Rafiq', 'rating':60},{'name': 'Hasan','rating':70},{'name': 'Karim','rating':80},{'name': 'Sabuhi','rating':60},
                        {'name': 'Tural','rating':70},{'name': 'Nicat','rating':80},{'name': 'Ahmad','rating':90},{'name': 'Huseyn','rating':80},
                        {'name': 'Iqbal','rating':70},{'name': 'Tacir','rating':70},{'name': 'Azad','rating':90},{'name': 'Shukran','rating':90}]

        #Humans levels for rating
        self.level_1 = []
        self.level_2 = []
        self.level_3 = []

        #teams
        self.team_1 = []
        self.team_2 = []
        self.teams = ["Team 1","Team 2"]

        self.selected_team_1 = []
        self.selected_team_2 = []

        #last_yellow_dresseds_team
        self.yellow = []
    

        #Main page text
        self.main_text = """\nOyunchulari goruntulemek uchun = > 1 \nOyunchu elave etmek uchun => 2\nOyunchu silmek uchun => 3\nOyunchulari komandalara bolmek uchun => 4\nSon sechilen oyunchulari goruntulemek uchun => 5\n"""
        self.wrong_input  = "Zehmet olmasa orada yazilanlardan birini qeyd et..."
        
        #all page text and characters
        self.star = 30*"*"
        self.back_text = f"\n{self.star}\nEsas sehifeye qayitmaq uchun => \"B\"\n{self.star}\n"
        self.select_number_text = f"\n{self.star}\nZehmet olmasa Reqem qeyd edin...\n{self.star}\n"
        
        #text footballers list
        self.footballers_list_text = f"\n{self.star}\nFutbolchularin listi\n{self.star}\n"

        #text addhuman
        self.add_human_text = f"\n{self.star}\nOyunchu elave et\n{self.star}\n"
        self.add_name = ""
        self.add_rating_number = ""

        

        #text delete human
        self.delete_human_text = f"\n{self.star}\nOyunchu sil\n{self.star}\n"
    
    def human_read(self):
       self.human_adding_text = f"\n{self.star}\nElave etdiyin oyunchu\n Adi: {self.add_name}\n Reytinqi: {self.add_rating_number}\n\n{self.star}\n"
       return self.human_adding_text