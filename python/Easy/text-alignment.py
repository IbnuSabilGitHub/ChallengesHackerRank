#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1,' ')+c+(c*i).ljust(thickness-1,' '))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).rjust(thickness+(thickness//2),' ')+(c*thickness).rjust(thickness*4,' '))

#Middle Belt
for i in range((thickness//2)+1):
    print((c*thickness*5).center((thickness*5)+((thickness//2)*2),' '))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).rjust(thickness+(thickness//2),' ')+(c*thickness).rjust(thickness*4,' '))   

#Bottom Cone
for i in range(thickness-1,-1,-1):
    print(((c*i).rjust(thickness-1,' ')+c+(c*i).ljust(thickness-1,' ')).rjust((thickness*5)+((thickness//2)*2),' '))