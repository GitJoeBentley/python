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
                record = item[0] + ',' + str(item[1]) + ',' + str(item[2]) + ',' + str(item[3])
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
                        dt = date.fromisoformat(temp[3])
                        s = (temp[0],int(temp[1]),int(temp[2]),dt)
                        self.scores.append(s)
            file.close()

        except FileNotFoundError:
            print("Cannot open",self.filename)
            #return
            

    def sort(self):        self.scores.sort(key=lambda x: x[1], reverse = True)
    
    def print(self):
        for rec in self.scores:
            print(rec[0].ljust(16) + str(rec[1]).rjust(10)+ str(rec[2]).rjust(10) + rec[3].strftime("%m/%d/%y").rjust(12))

    def __str__(self) -> str:
        counter = 1
        if len(self.scores) == 0:
            s = "No high scores recorded"
        else:
            s = "  ******************* High Scores *******************\n\n     Name           Score      Apples       Date\n"
            for rec in self.scores:
                s = s + str(counter).rjust(3) + "  " + rec[0].ljust(16) + str(rec[1]).rjust(3) + \
                    str(rec[2]).rjust(13) + rec[3].strftime("%m/%d/%y").rjust(13) + '\n'
                counter += 1
        return s
        
        
"""
if __name__ == '__main__':
    h = HighScores()
    #h.read_from_file()
    #h.print()
    h.scores.append(("Pete",randint(10,15),randint(1,10),date.fromisoformat('2019-01-15')))
    h.scores.append(("Harry",randint(90,95),randint(1,10),date.fromisoformat('2025-05-15')))
    h.scores.append(("Joe",randint(80,95),randint(1,10),date.fromisoformat('2025-05-15')))
    h.print()
    print("")
    # sort
    h.sort()
    h.print()
    h.write_to_file()
    """
