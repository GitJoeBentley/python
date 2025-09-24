from datetime import datetime, date
from random import randint

class HighScores:
    def __init__(self):
        self.filename = "resources/highscores.txt"
        self.scores = []
        self.read_from_file()

    def write_to_file(self):
        self.sort()
        counter = 0
        with open(self.filename,"w") as file:
            for item in self.scores:
                if counter >= 10:
                    break
                record = item[0] + ',' + str(item[1]) + ',' + str(item[2])
                file.write(record + '\n')
                counter += 1
        file.close()

    def read_from_file(self):
        try:
            with open(self.filename,"r") as file:
                for line in file:
                    if len(line) > 10:
                        line = line.rstrip()
                        temp = line.split(',')
                        dt = date.fromisoformat(temp[2])
                        s = (temp[0],int(temp[1]),dt)
                        self.scores.append(s)
        except FileNotFoundError:
            print("Cannot open",self.filename)
            return
            
        file.close()

    def sort(self):        self.scores.sort(key=lambda x: x[1], reverse = True)
    
    def print(self):
        for rec in self.scores:
            print(rec[0].ljust(16) + str(rec[1]).rjust(3) + rec[2].strftime("%m/%d/%y").rjust(10))

    def __str__(self) -> str:
        counter = 1
        if len(self.scores) == 0:
            s = "No high scores recorded"
        else:
            s = "  *********** High Scores ***********\n\n     Name           Score      Date\n"
            for rec in self.scores:
                s = s + str(counter).rjust(3) + "  " + rec[0].ljust(16) + str(rec[1]).rjust(3) + rec[2].strftime("%m/%d/%y").rjust(13) + '\n'
                counter += 1
        return s
        
        

"""
if __name__ == '__main__':
    h = HighScores()
    h.read_from_file()
    h.print()
    
    h.scores.append(("gail",randint(70,75),date.fromisoformat('2019-01-15')))
    print("")
    # sort
    h.sort()
    h.print()

    h.write_to_file()
"""