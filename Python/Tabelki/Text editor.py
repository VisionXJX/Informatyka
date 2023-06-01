Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print ("1 po Ang: %s \n po Ang: %s" % ('one', 'two')0
       
SyntaxError: incomplete input
print ("1 po Ang: %s \n po Ang: %s" % ('one', 'two')0
       
SyntaxError: incomplete input
print ("1 po Ang: %s \n po Ang: %s" % ('one', 'two'))
       
1 po Ang: one 
 po Ang: two
print ("1 po Ang: %s \n2 po Ang: %s" % ('one', 'two'))
       
1 po Ang: one 
2 po Ang: two
print ("1 po Ang: %s \n2 po Ang: %s \n3 po Ang: %s \n4 po Ang: %s \n5 po Ang: %s \n6 po Ang: %s \n7 po Ang: %s \n8 po Ang: %s \n9 po Ang: %s \n10 po Ang: %s" % ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'))
       
1 po Ang: one 
2 po Ang: two 
3 po Ang: three 
4 po Ang: four 
5 po Ang: five 
6 po Ang: six 
7 po Ang: seven 
8 po Ang: eight 
9 po Ang: nine 
10 po Ang: ten
print ("1 po Ang: {} \n2 po Ang: {}".format('one', 'two'))
       
1 po Ang: one 
2 po Ang: two
>>> Z
...        
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    Z
NameError: name 'Z' is not defined
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> print ("Cyfra %d poprzedza %d" % (7,8))
...        
Cyfra 7 poprzedza 8
>>> print ("Cyfra {} poprzedza {}".format (7,8))
...        
Cyfra 7 poprzedza 8
]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> print ("Rekord Świata na 100m to %f ustanowił go %f" % (9.58, "Usain Bolt"))
...        
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print ("Rekord Świata na 100m to %f ustanowił go %f" % (9.58, "Usain Bolt"))
TypeError: must be real number, not str
>>> print ("Rekord Świata na 100m to %f ustanowił go %f" % str(9.58, "Usain Bolt"))
...        
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print ("Rekord Świata na 100m to %f ustanowił go %f" % str(9.58, "Usain Bolt"))
TypeError: decoding to str: need a bytes-like object, float found
>>> print float("Rekord Świata na 100m to %f ustanowił go %f" % str(9.58, "Usain Bolt"))
...        
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> print int(("Rekord Świata na 100m to %f ustanowił go %f" % ('9.58', 'Usain Bolt')))
...        
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> print ("Rekord Świata na 100m to {} ustanowił go {}".format (9.58, "Usain Bolt"))
...        
Rekord Świata na 100m to 9.58 ustanowił go Usain Bolt
