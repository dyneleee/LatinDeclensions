import random

def f(choice):
    dec = random.randint(1, 5)
    gen = random.randint(1, 3)
    num = random.randint(1, 2)
    case = random.randint(1, 5) #nom, acc, gen, dat, abl
    if choice==1:
        if dec==1:
            print('1st declension ',end='')
        elif dec==2:
            print('2nd declension ',end='')
        elif dec==3:
            print('3rd declension ', end='')
        else:
            print('%dth declension '%dec, end='')
    else:
        if gen==1:
            print('masculine ', end='')
        elif gen==2:
            print('feminine ', end='')
        elif gen==3:
            print('neuter ', end='')
        
    if case==1:
        print('nominative ', end='')
    elif case==2:
        print('accusative ', end='')
    elif case==3:
        print('genitive ', end='')
    elif case==4:
        print('dative ', end='')
    else:
        print('ablative ', end='')
    if num==1:
        print('singular')
    else:
        print('plural')
    #print(str(dec)+" declension, "+str(num)+" number, "+str(case)+" case")
    ans=input()
    if choice==1:
        return check1(dec, num, case, ans)
    if choice==2:
        return check2(gen, num, case, ans)


def check1(dec, num, case, ans):
    dict = {
    111:'a', 112:'am', 113:'ae', 114:'ae', 115:'ā',
    121:'ae', 122: 'ās', 123: 'ārum', 124:'īs', 125:'īs',
    211:'us', 212:'um', 213:'ī', 214:'ō', 215:'ō',
    221:'ī', 222: 'ōs', 223: 'ōrum', 224:'īs', 225:'īs',
    311:'is', 312:'em', 313:'is', 314:'ī', 315:'e',
    321:'ēs', 322: 'ēs', 323: 'ium', 324:'ibus', 325:'ibus',
    411:'us', 412:'um', 413:'ūs', 414:'uī', 415:'ū',
    421:'ūs', 422: 'ūs', 423: 'uum', 424:'ibus', 425:'ibus',
    511:'ēs', 512:'em', 513:'ēī', 514:'ēī', 515:'ē',
    521:'ēs', 522: 'ēs', 523: 'ērum', 524:'ēbus', 525:'ēbus'
    }
    alt_dict = {
        111:'a', 112:'am', 113:'ae', 114:'ae', 115:'ā',
    121:'ae', 122: 'ās', 123: 'ārum', 124:'īs', 125:'īs',
    211:'us', 212:'um', 213:'ī', 214:'ō', 215:'ō',
    221:'ī', 222: 'ōs', 223: 'ōrum', 224:'īs', 225:'īs',
    311:'is', 312:'em', 313:'is', 314:'ī', 315:'e',
    321:'ēs', 322: 'ēs', 323: 'ium', 324:'ibus', 325:'ibus',
    411:'us', 412:'um', 413:'ūs', 414:'uī', 415:'ū',
    421:'ūs', 422: 'ūs', 423: 'uum', 424:'ibus', 425:'ibus',
    511:'ēs', 512:'em', 513:'eī', 514:'eī', 515:'ē',
    521:'ēs', 522: 'ēs', 523: 'ērum', 524:'ēbus', 525:'ēbus'
    }
    x=100*dec+10*num+case
    if ans==dict[x] or ans==alt_dict[x]:
        print('Correct!')
        return True
    print('Incorrect! Correct answer: '+dict[x])
    return False

def check2(gen, num, case, ans):
    dict = {
    111:'hic', 112:'hunc', 113:'huius', 114:'huic', 115:'hōc',
    121:'hī', 122: 'hōs', 123: 'hōrum', 124:'hīs', 125:'hīs',
    211:'haec', 212:'hanc', 213:'huius', 214:'huic', 215:'hāc',
    221:'hae', 222: 'hās', 223: 'hārum', 224:'hīs', 225:'hīs',
    311:'hoc', 312:'hoc', 313:'huius', 314:'huic', 315:'hōc',
    321:'haec', 322: 'haec', 323: 'hōrum', 324:'hīs', 325:'hīs',
    }
    x=100*gen+10*num+case
    if ans==dict[x]:
        print('Correct!')
        return True
    print('Incorrect! Correct answer: '+dict[x])
    return False


print('declensions: 1\nhic: 2\n')
choice = int(input())
print('\n')
points=0
while True:
    if f(choice) == False:
        break
    points+=1

print('Points: %d'%points)
