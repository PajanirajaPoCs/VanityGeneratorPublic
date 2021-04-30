import json
import boto3
import time
from datetime import datetime
from english_words import english_words_set

def lambda_handler(event, context):
    print(event)
    #Load list of 7 letter words
    a= list(english_words_set)
    b=[]
    for i in a:
        if len(i)==7 or len(i)==6:
            b.append(i.upper())
    b.sort()
    
    ListOfVanity="There is one vanity found for your number."
    #custPhone= event["Details"]["Parameters"]["CustomerEndpoint"]["Address"]
    
    custPhone= event["Details"]["Parameters"]["Cust_phone"]
    
    arrayvanity=[]
    
    custPhone = custPhone[1::]
  
    phoneNumber=[]
    for i in custPhone:
        j= int(i)
        phoneNumber.append(j)
    pNLen=len(phoneNumber)
    
    #print(phoneNumber)
    array2=["A","B","C"]
    array3=["D","E","F"]
    array4=["G","H","I"]
    array5=["J","K","L"]
    array6=["M","N","O"]
    array7=["P","Q","R","S"]
    array8=["T","U","V"]
    array9=["W","X","Y","Z"]
    
    loop1,loop2,loop3,loop4,loop5,loop6,loop7=[],[],[],[],[],[],[]
    loopArray=[loop1,loop2,loop3,loop4,loop5,loop6,loop7]
    arrArray=[array2,array3,array4,array5,array6,array7,array8,array9]
    
    if phoneNumber[-1]==9:
        loop7=array9
    elif phoneNumber[-1]==8:
        loop7=array8
    elif phoneNumber[-1]==7:
        loop7=array7
    elif phoneNumber[-1]==6:
        loop7=array6
    elif phoneNumber[-1]==5:
        loop7=array5
    elif phoneNumber[-1]==4:
        loop7=array4
    elif phoneNumber[-1]==3:
        loop7=array3
    elif phoneNumber[-1]==2:
        loop7=array2  
    
    
    if phoneNumber[-2]==9:
        loop6=array9
    elif phoneNumber[-2]==8:
        loop6=array8
    elif phoneNumber[-2]==7:
        loop6=array7
    elif phoneNumber[-2]==6:
        loop6=array6
    elif phoneNumber[-2]==5:
        loop6=array5
    elif phoneNumber[-2]==4:
        loop6=array4
    elif phoneNumber[-2]==3:
        loop6=array3
    elif phoneNumber[-2]==2:
        loop6=array2 
    
    if phoneNumber[-3]==9:
        loop5=array9
    elif phoneNumber[-3]==8:
        loop5=array8
    elif phoneNumber[-3]==7:
        loop5=array7
    elif phoneNumber[-3]==6:
        loop5=array6
    elif phoneNumber[-3]==5:
        loop5=array5
    elif phoneNumber[-3]==4:
        loop5=array4
    elif phoneNumber[-3]==3:
        loop5=array3
    elif phoneNumber[-3]==2:
        loop5=array2 
        
    if phoneNumber[-4]==9:
        loop4=array9
    elif phoneNumber[-4]==8:
        loop4=array8
    elif phoneNumber[-4]==7:
        loop4=array7
    elif phoneNumber[-4]==6:
        loop4=array6
    elif phoneNumber[-4]==5:
        loop4=array5
    elif phoneNumber[-4]==4:
        loop4=array4
    elif phoneNumber[-4]==3:
        loop4=array3
    elif phoneNumber[-4]==2:
        loop4=array2 
        
    if phoneNumber[-5]==9:
        loop3=array9
    elif phoneNumber[-5]==8:
        loop3=array8
    elif phoneNumber[-5]==7:
        loop3=array7
    elif phoneNumber[-5]==6:
        loop3=array6
    elif phoneNumber[-5]==5:
        loop3=array5
    elif phoneNumber[-5]==4:
        loop3=array4
    elif phoneNumber[-5]==3:
        loop3=array3
    elif phoneNumber[-5]==2:
        loop3=array2 
        
    if phoneNumber[-6]==9:
        loop2=array9
    elif phoneNumber[-6]==8:
        loop2=array8
    elif phoneNumber[-6]==7:
        loop2=array7
    elif phoneNumber[-6]==6:
        loop2=array6
    elif phoneNumber[-6]==5:
        loop2=array5
    elif phoneNumber[-6]==4:
        loop2=array4
    elif phoneNumber[-6]==3:
        loop2=array3
    elif phoneNumber[-6]==2:
        loop2=array2 
        
    if phoneNumber[-7]==9:
        loop1=array9
    elif phoneNumber[-7]==8:
        loop1=array8
    elif phoneNumber[-7]==7:
        loop1=array7
    elif phoneNumber[-7]==6:
        loop1=array6
    elif phoneNumber[-7]==5:
        loop1=array5
    elif phoneNumber[-7]==4:
        loop1=array4
    elif phoneNumber[-7]==3:
        loop1=array3
    elif phoneNumber[-7]==2:
        loop1=array2 
    #print(loop1)
    for i in range(len(loop1)):
        
        v1=""
        v1+=loop1[i]
        for j in range(len(loop2)):
            v2=v1
            v2+=loop2[j]
            for k in range(len(loop3)):
                v3=v2
                v3+=loop3[k]
                for l in range(len(loop4)):
                    v4=v3
                    v4+=loop4[l]
                    for m in range(len(loop5)):
                        v5=v4
                        v5+=loop5[m]
                        for n in range(len(loop6)):
                            v6=v5
                            v6+=loop6[n]
                            arrayvanity.append(v6)
                            for o in range(len(loop7)):
                                v7=v6
                                v7+=loop7[o]
                                arrayvanity.append(v7)
        
    
    listVanity=[]
    
    for i in arrayvanity:
        for j in b:
            if i==j:
                listVanity.append(i)
    
     #DB Insertion
    client = boto3.resource('dynamodb')
    table = client.Table("callerVanity")
     
    ct = datetime.now()
    cTime = ct.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    #print(cTime)
    print(listVanity)
    finalList=""
    #listVanity=["RAINBOW","WELCOME"]
    if len(listVanity) > 0 :
        table.put_item(Item={'callerID':int(custPhone),'VanityNumberList':listVanity, 'timestamp':cTime})
        
        for i in range(len(listVanity)):
            finalList = finalList + listVanity[i] + " , "
           # finalList = finalList.pop(-1)
            
        ListOfVanity =  "You have " +str(len(listVanity)) +" vanity. They are  " + finalList
    else:
        ListOfVanity =  "Sorry, There is no vanity for your number"
        
    print(ListOfVanity)
    return{ "varFromLambda":ListOfVanity}
    