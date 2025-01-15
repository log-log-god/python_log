def totalScore(s1,s2,s3):
    hap = s1+s2+s3
    return hap

def averageScore(s1,s2,s3):
    return (s1,s2,s3)/3

def passfail(s1,s2,s3):
    avg = (s1+s2+s3)/3
    if avg >=60 and s1 >=40 and s2>=40 and s3>=40:
        return 'Pass'
    else:
        return 'Fail'
    
if __name__ =='__main__':
    print(f'{totalScore(40, 60, 44)}')
    print(f'{averageScore(40, 33, 98)}')
    print(f'{passfail(90, 56, 90)}')