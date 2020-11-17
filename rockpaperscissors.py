import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

computer= random.randint(1,3)

man = int(input(f"Enter the number from 1.2 and 3 in which \n 1 is for 'rock'{rock},\n 2 is for 'paper'{paper}\n 3 is for 'scissors'{scissors}\nPlease give your choice = "))
manchoose=print(f"Player has choice the number  {man}")

print(f"Computer has choose {computer}")

if man==1:
  if computer==1:
    print(f"The mach is draw beacuse both having same choice rock {rock}")
  elif computer==2:
    print(f"Computer win by paper{paper}")
  else:
    print(f"Player win by rock{rock}")
elif man==2:
  if computer==1:
    print(f"Player win the match by paper{paper}")
  elif computer==2:
    print(f"The mach is draw beacuse both having same choice paper{paper}")
  else:
    print(f"Computer win by scissors{scissors}")
elif man==3:
  if computer==1:
    print(f"Computer win the match by rock{rock}")
  elif computer==2:
    print(f"Computer win by scissors {scissors}")
  else:
    print(f"The mach is draw beacuse both having same choice scissors{scissors}")
else:
  print(f"Player,please choose the number from 1,2 and 3\nYou have choosen the wrong input = {man}")
