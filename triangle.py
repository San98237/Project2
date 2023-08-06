angle1 = int(input("Please enter the degree of the first angle"))
angle2 = int(input("Please enter the degree of the second angle"))
angle3 = int(input("Please enter the degree of the third angle"))
add = angle1 + angle2 + angle3
if add == 180:
    if angle1 == 90 and angle2 < 90 and angle3<90:
        print("It is a right angled triangle")
    elif angle1 > 90 and angle2 < 90 and angle3<90:
        print("It is an obtuse angled triangle")
        if angle1<90 and angle2 == 90 and angle3<90:
            print("It is an right angled triangle")
        elif angle1<90 and angle2>90 and angle3<90:
            print("It is an obtuse angled triangle")
        elif angle1<90 and angle2<90 and angle3<90:
            print("It is an acute angled triangle")
            if angle1<90 and angle2<90 and angle3==90:
                print("It is an acute angled triangle")
            elif angle1<90 and angle2<90 and angle3>90:
                print("It is an obtuse angled triangle")
else:
    print("This is not a possible triangle")