def iscars_number(card_number):
    card_number=card_number.replace('-','')

    if len(card_number)== 16 and card_number[0] in "456":
        if card_number.isdigit():
            for i in range(len(card_number)-3):
                if card_number[i]==card_number[i+1]==card_number[i+2]==card_number[i+3]:
                    return False
            
            return True
    
    return False

card_number=input() 

if iscars_number(card_number):
    print("Valid")

else:
    print("Invalid")