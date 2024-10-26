

yn = print('welcome to kings banking systems, our banking procedure here are: \n1 for withdrawl \n2 for deposit \n3 for transfer\n') 
ram = dict()
ram2 = dict()
rew = []
ke = input('do you want to open a new account\n')
def accno():
   import random
         
   for i in range(1):
     e = random.random()
   re = print('this is your acc no\n')
   hq = print(e)
   rew.append(e)
def open_acc():
   ty = input('please enter your name and amount\n')
   her = open('jah.txt','w')
   till = her.write(ty)
   kill = her.close()
   accno()
   
   king = ty.split(':')
   ram[king[0]] = king[1]
   ram2[rew[0]] = king[0]
   hb = print('you will have to open another account')
   hx = input('please enter another name and amount\n')
   accno()
   ling = hx.split(':')
   ram[ling[0]] = ling[1]
   ram2[rew[1]] = ling[0]

def withdraw():
          ring = input('enter accno\n')
          me = ram2.get(rew[0])
          print(me)
          we = input('enter the amount you will like to withdrawl\n')
          no = ram.get(me)
          qz = int(we)
          kl = int(no)
          if qz < kl:
             hj = kl - qz
             sq = ram[me] = hj
             fd = print('this is your balance',sq)
          if qz > kl:
             print('please this amount is greater than that in your acc')
          
def deposit():
          hjk = input('enter accno\n')
          ke = ram2.get(rew[0])
          print(ke)
          ha = input('enter the amount you will like to deposit to your acc\n')
          ui = ram.get(ke)
          js = int(ui)
          ds = int(ha)
          ut = js + ds
          rq = ram[ke] = ut
          print('this is your balance',rq)
          
def transfer():
          us = input('enter your accno\n')
          vc = ram2.get(rew[0])
          tq = input('please enter the accno you will like to transfer cash to\n')
          rc = ram2.get(rew[1])
          rs = input('enter the amount you will like to transfer\n')
          aq = ram.get(vc)
          jc = int(aq)
          ab = int(rs)
          if ab < jc:  
            wx = jc - ab
            kx = ram[vc] = wx
            cz = print('this is your balance',kx)
            bn = ram.get(rc)
            sa = int(bn)
            op = sa + ab
            cw = ram[rc] = op
            od = print(rc,'this is your current balance',cw)
          if ab > jc:
             print('please this amount is grater than that in your acc')
def main():
   open_acc()
   asd = input('please enter any of our procedures\n')
   if asd == '1':
        withdraw()
   if asd == '2':
        deposit()
   if asd == '3':
        transfer()
