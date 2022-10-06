class Enemy:
 life = 3
 def attack(self):
  print("outch me dolio")
  self.life -= 1
 def checklife(self):
  if self.life <= 0:
   print("I am dead!")
  else:
   print(str(self.life) + "life left")
enemy1 = Enemy()
enemy1.attack()
enemy2 = Enemy()
print(callable(Enemy))
print(callable(enemy1))
print(callable(enemy2))
print(enemy2.life)
