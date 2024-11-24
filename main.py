def supermenu():
    while True:
        import mysql.connector
        mydb=mysql.connector.connect(host="localhost",database="KVNmotors", user="root", password="2006")
        mycursor=mydb.cursor()                             
        print("--------------------------------------")
        print("********KVN MOTORS********")
        print("")
        print("1. Customer")
        print("2. Adminstrator")
        print("3. Exit")
        print("--------------------------------------")
        choiceS = int(input("Enter your choice:"))
        if choiceS==1:
            print("")
            usermenu()

        elif choiceS==2:
              password=input("Enter The Login Password :")
              if (password!="KVNV"):
                 print("")
                 print("Wrong Admin Password!")
                 supermenu()   
              else:
                 adminmenu()
        
        elif choiceS==3:
            print("")
            print("######################################")
            print("")
            print("!!THANK YOU FOR VISITING KVNMOTORS!!")
            print("")
            print("######################################")
            break

        else:
            print("Invalid Choice !")
            print("")

def usermenu():
    while True:     
        import mysql.connector
        mydb=mysql.connector.connect(host="localhost",database="KVNmotors" ,user="root", password="2006")
        mycursor=mydb.cursor()
        print("--------------------------------------")
        print("             ##CUSTOMER##")
        print("--------------------------------------")
        print("")
        print("1. Show Available Cars")
        print("2. Get Information About A Specific Car")
        print("3. Buy A Car")
        print("4. Exit")
        print ("--------------------------------------")
        print("")
        choiceU=int(input("Enter Your Choice:"))
        if choiceU==1:  
            print("")
            print("___________________________________________________________________________________________________________________________________")
            print("|  ID  |   MODEL   | VARIANT | ENGINE IN CC |  FUEL  |  MILEAGE  |  EX-SHOWROOM PRICE  |    OTHERS    |   ONROAD PRICE  |   CSD   |")
            print("___________________________________________________________________________________________________________________________________")
            print("")
            mycursor.execute("Select * from TataCars")
            x = mycursor.fetchall()
            for i in range(0,len(x)):
              print("|",x[i][0]," | ",x[i][1],"|  ",x[i][2],"  |   ",x[i][3],"   |   ",x[i][4],"   |  ",x[i][5],"    |     ",x[i][6],"    |     ",x[i][7],"   |   ",x[i][8], 
                    "   |   ",x[i][9],"|")
              print("---------------------------------------------------------------------------------------------------------------------------------------")
            print("")

        elif choiceU==2:
            infofcar()
            print("")

        elif choiceU==3:
            conbycarname()

        elif choiceU==4:
            print("")
            print("######################################")
            break

        else:
            print("Invalid Choice !")
            print("")

def conbycarname():                #Done
       import mysql.connector
       mydb=mysql.connector.connect(host="localhost",database="KVNmotors" ,user="root", password="2006")
       mycursor=mydb.cursor()                                       
       print("")
       global model,variant,CSD,final
       model=input("Enter The Model Of Car:")
       variant=input("Enter Variant Of Car:")
       tup=(model,variant)
       CSD=input("Enter 'Y' IF DEFENCE RELATED PERSON or 'N' for NON DEFENCE RELATED PERSON : ")
       print("")

       if (CSD in "Yy"):
          query= "Select Ex_showroom,Others,Onroad_price,CSD,(Ex_showroom+Others+Onroad_price-CSD) as Final_Price from tatacars where Model=%s and Variants=%s"
          mycursor.execute(query,tup)
          records=mycursor.fetchall()       
          print("______________________________________________________________")
          print("|Ex-Showroom Price | Other | Onroad Price | CSD | Final Price|")
          print("--------------------------------------------------------------")
          for x in records:
             print(x[0],"             ",x[1],"  ","   ",x[2],"   ",x[3],"   ",x[4])
          final=x[4]
          print ("--------------------------------------------------------------") 
          bill()  
          print("")
          print("Congratulations For Buying The Car!")
          print("")
          print("")
            
       else:
          query= "Select Ex_showroom,Others,Onroad_price,(Ex_showroom+Others+Onroad_price) as Final_Price from tatacars where Model=%s and Variants=%s"
          mycursor.execute(query,tup)
          records=mycursor.fetchall()
          print("________________________________________________________")
          print("|Ex-Showroom Price | Other | Onroad Price | Final Price|")
          print("--------------------------------------------------------")
          for x in records:
             print(x[0],"            ",x[1],"  ","   ",x[2],"   ",x[3])
          final=x[3]
          print ("--------------------------------------------------------")   
          bill()
          print("")
          print("Congratulations For Buying The Car!")
          print("")
          print("")
          print("--------------------------------------")
                  
def infofcar():                            #Done
       import mysql.connector
       mydb=mysql.connector.connect(host="localhost",database="KVNmotors" ,user="root", password="2006")
       mycursor=mydb.cursor()          
       print("")                               
       model=input("Enter The Model Of Car:")
       print("")
       variant=input("Enter Variant Of Car:")
       print("")
       tup=(model,variant)
       query= "Select Model,Variants, Engine_cc,Fuel,Mileage_kmpl from tatacars where Model=%s and Variants=%s"
       mycursor.execute(query,tup)
       records=mycursor.fetchall()
       print("____________________________________________")
       print("| Model | Variant | Engine | Fuel | Mileage|")
       print("--------------------------------------------")
       for x in records:
          print("|",x[0],"  | ",x[1],"  |  ",x[2]," | ",x[3]," |",x[4],"|")
       print("--------------------------------------------")
       print("")

def bill():  
    from datetime import datetime        
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",database="KVNmotors" ,user="root", password="")
    mycursor=mydb.cursor() 
    print("")                                   
    Custmr_Name=input("Enter Your Name:")
    print("")
    Custmr_Phone=(input("Enter Your Phone Number:"))
    print("") 
    Custmr_Dlicense=input("Enter Your LicenseID:")
    print("")
    Custmr_Address=input("Enter Your Home Address:")
    print("")
    date = datetime.now().strftime("%d/%m/%y")
    time = datetime.now().strftime("%H:%M:%S")
    tup2=(Custmr_Name, Custmr_Phone, Custmr_Dlicense, Custmr_Address, model, variant, CSD, final, date, time)
    query="Insert Into DataOfBuyers values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(query,tup2)
    mydb.commit()
    print("")

def adminmenu():
   while True:
        import mysql.connector
        mydb=mysql.connector.connect(host="localhost",database="KVNmotors", user="root", password="2006")
        mycursor=mydb.cursor()
        print("--------------------------------------")
        print("             ##ADMIN##")
        print("--------------------------------------")
        print("")
        print("1. Show Data in Maintable")
        print("2. To Add New Car/Car Variant in Maintable")
        print("3. To Updata A Price in Maintable")
        print("4. Delete A Record From Maintable")
        print("5. Check Cars Sold By Company:")
        print("6. Exit")
        print("")
        print("--------------------------------------")
        choiceA = int(input("Enter your choice:"))
        if choiceA==1:
            print("")
            print("___________________________________________________________________________________________________________________________________")
            print("|  ID  |   MODEL   | VARIANT | ENGINE IN CC |  FUEL  |  MILEAGE  |  EX-SHOWROOM PRICE  |    OTHERS    |   ONROAD PRICE  |   CSD   |")
            print("___________________________________________________________________________________________________________________________________")
            print("")
            mycursor.execute("Select * from TataCars")
            x = mycursor.fetchall()
            for i in range(0,len(x)):
              print("|",x[i][0]," | ",x[i][1],"|  ",x[i][2],"  |   ",x[i][3],"   |   ",x[i][4],"   |  ",x[i][5],"    |     ",x[i][6],"    |     ",x[i][7],"   |   ",x[i][8],"   |   ",x[i][9],"|")
              print("---------------------------------------------------------------------------------------------------------------------------------------")
            print("")

        elif choiceA==2:
            print("")
            identity=int(input("Enter The ID Of Car:"))
            print("")
            model=input("Enter The Model Of Car:")
            print("")
            variant=input("Enter The Variant Of Car:")
            print("")
            engine=int(input("Enter The Engine in CC:"))
            print("")
            fuel=input("Enter The Fuel:")
            print("")
            mileage=float(input("Enter The Mileage Of Car:"))
            print("")
            exshowroom=int(input("Enter The Ex-showroom Price:"))
            print("")
            other=int(input("Enter The Other Price(Incl. RC,Insurance,etc):"))
            onroad=exshowroom+other
            print("")
            csd=int(input("Enter CSD Ammount:"))
            print("")
            tup=(identity,model,variant,engine,fuel,mileage,exshowroom,other,onroad,csd)
            query="Insert Into TataCars values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            mycursor.execute(query,tup)
            mydb.commit()    # to make changes in table
        
            print("Record Added Successfully!")
            print("")
   
        elif choiceA==3:
            print("")
            identity=int(input("Enter ID Of Car You Want To Edit:"))
            exshowroom=int(input("Enter The New Ex-showroom Price:"))
            other=int(input("Enter The New Others Price:"))
            csd=int(input("Enter The CSD Ammount:"))
            tup1=(exshowroom,identity)
            tup2=(other,identity)
            tup3=(csd,identity)
            tup4=(exshowroom+other,identity)
            query1="Update TataCars Set Ex_showroom=%s Where ID=%s"
            query2="Update TataCars Set Others=%s Where ID=%s"
            query3="Update TataCars Set CSD=%s Where ID=%s"
            query4="Update TataCars Set Onroad_Price=%s Where ID=%s"
            mycursor.execute(query1,tup1)
            mydb.commit()    # to make changes in table
            mycursor.execute(query2,tup2)
            mydb.commit()
            mycursor.execute(query3,tup3)
            mydb.commit()
            mycursor.execute(query4,tup4)
            mydb.commit()
            print("")
            print("Record Updated Successfully!")
            print("")

        elif choiceA==4:
            print("")
            identity=int(input("Enter Record ID You Want To Delete:"))
            print("")
            tup=(identity,)
            query=("DELETE From TataCars where ID=%s")
            mycursor.execute(query,tup)
            mydb.commit()    # to make changes in table
            print("")
            print("Record Deleted Successfully!")
            print("")

        elif choiceA==5:                                                    #doing
            print("")
            query= "Select * from DataOfBuyers"
            mycursor.execute(query)
            records=mycursor.fetchall()
            print("__________________________________________________________________________________________________________________________________")
            print("|  Custr.Name  |  Custmr.Phone |  Custmr.Dlicense  |  Custmr.Address  | Model | Variant | Cust In Def | Sold Price | Date | Time |")
            print("----------------------------------------------------------------------------------------------------------------------------------")
            for x in records:
              print("| ",x[0],"  | ",x[1]," | ",x[2],"   |   ",x[3]," |   ",x[4],"  | ",x[5]," | ",x[6]," | ",x[7]," | ",x[8]," | ",x[9],"|")
              print ("----------------------------------------------------------------------------------------------------------------------------------")
            print("")

        elif choiceA==6:
            print("")
            
            print("######################################")
            break

        
        else:
            print("Invalid Choice !")
            print("")

supermenu()








    







    













