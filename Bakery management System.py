import pymysql as py
# import mysql.connector

con = py.connect(host='blg1ldsow80t8uyzb66c-mysql.services.clever-cloud.com', user='uruct9bnwbk9yctr',
                    password='HPJlSDy4ikLP5P3QVVbz', database='blg1ldsow80t8uyzb66c')
curs = con.cursor()

# we created a database and table (cs) on clever cloud

# curs.execute("Create table if not exits cs(sno int,product varchar(20),cost int)")
# curs.execute("select * from cs")
# res = curs.fetchall()
# if res==[]:
#     curs.execute("insert into cs values(1,'cake',50)")
#     curs.execute("insert into cs values(2,'pastry',20)")
#     curs.execute("insert into cs values(3,'milk',60)")
#     curs.execute("insert into cs values(4,'butter',20)")
#     curs.execute("insert into cs values(5,'cheese',30)")
#     con.commit()



# curs.execute("Create table if not exits vip(sno int,varieties varchar(20))")
# curs.execute("select * from vip")
# res=curs.fetchall()
# if res==[]:
#     curs.execute("insert into vip values(1,'Vaniella')")
#     curs.execute("insert into vip values(2,'chocalate')")
#     curs.execute("insert into vip values(3,'strawberry')")
#     curs.execute("insert into vip values(4,'butter_scotch')")
#     con.commit()



# curs.execute("Create table if not exits worker(sno int, name varchar(20), salary int)")
# curs.execute("select * from worker")
# res = curs.fetchall()
# if res==[]:
#     curs.execute("insert into worker values(1,'mukesh',12500)")
#     curs.execute("insert into worker values(2,'Ram',10500)")
#     curs.execute("insert into worker values(3,'Suresh',15000)")
#     curs.execute("insert into worker values(4,'Raju',12500)")
#     curs.execute("insert into worker values(5,'Shyam',10000)")
#     con.commit()

from datetime import datetime

# print('_'*40)
print("\n")
print('_'*40 + "WELCOME To BACKERY MANAGEMENT SYSYTEM" + '_'*40)
print("\n")
print("Made By : _Chilled_Sweet_" + '_'*5)
print("\n")
print('_'*100 )
print("\n")


print('_'*5  + "\tPlease Choose :" +'_'*5 +"\n\n\t1. For Admin \n\n\t2. For Customers \n\n\t3. For Exits \n" )

choice = int(input("\nEnter Your choice : "))


if choice == 1:
    admin = input("\nUsername : ")
    password = input("\nEnter Password : ")

    if admin.lower() == "kartik" or  password == 1234:
        print('\n'+'*'*20 + "\tHello Sir, You Log in as Admin successfully..!\t" + '*'*20)
        
    else:
        ("\nIncorrect username or password.")
        exit()
        
    ch = 0
    while ch!= 8:
        print('_'*100 )
        print("\n\tPress 1 :- To Add Item in Shop  ")
        print("\n\tPress 2 :- To See Item in Shop  ")
        print("\n\tPress 3 :- To Update Cost Of any Item in Shop  ")
        print("\n\tPress 4 :- To Add Varieties of Cake in Shop  ")
        print("\n\tPress 5 :- To Add Worker in the Shop  ")
        print("\n\tPress 6 :- To See Workers in Shop  ")
        print("\n\tPress 7 :- To Update Salary of any Worker  ")
        print("\n\tPress 8 :- To EXIT  ")
        print('_'*100 )

  
        c = int(input("\nEnter Your Choice : "))
        print('_'*50 )

        if c ==1:
            def add():
                sno = int(input("\nEnter sr. No.        : "))
                product = input("\nEnter product Name   : ")
                cost = int(input("\nEnter The Cost(Rs.) : "))

                curs.execute("insert into cs values(%d,'%s',%d)" %(sno,product,cost))
                con.commit()
                print("\nNew Item Added Succesfully..!")
                print('_'*100 )
            add()

        elif c == 2:
            def items():
                print("\n\t\tItem In The Shop ")
                print('_'*50)
                curs.execute("select * from cs")
                res = curs.fetchall()

                print("Sno", "\tProduct", "\tCost")
                print('_'*50)
                print("")
                for row in res:
                    print(row[0],'\t',row[1],'','',":",'\t',row[2])
                print('_'*100 )

            items()

        elif c == 3:
            def money():
                print("\n\t\tItem In The Shop ")
                print('_'*50)
                curs.execute("select * from cs")
                res = curs.fetchall()

                print("Sno", "\tProduct", "\tCost")
                print('_'*50)
                print("")
                for row in res:
                    print(row[0],'\t',row[1],'','',":",'\t',row[2])
                print('_'*100 )

                pr_nm = input("\nEnter The Name of Product that you want to upadte the cost : ")
                curs.execute("select * from cs where products = '%s'" % pr_nm.lower())
                res = curs.fetchone()
                print('_' * 50)

                if res:
                    print("\n\t\tSearch Item")
                    print("")
                    print("Sno", "\tProduct", "\tCost")
                    print('_' * 50)
                    print("")

                    print(res[0], '\t', res[1], '', '', ":", '\t', res[2])

                    print("")
                    new_cost = input(f"\nEnter the New Cost(Rs.) of {res[1]} : ")
                    curs.execute("update cs set cost = '%s' where products = '%s'" (new_cost, pr_nm))
                    con.commit()
                    print(f"\nCost Of {res[1]} will be Change Successfully..!")
                    print('_'*100 )

                    print("\n\t\tItem's In A Shop (After Updation)")
                    print('_'*50)
                    curs.execute("select * from cs")
                    res = curs.fetchall()

                    print("Sno", "\tProduct", "\tCost")
                    print('_'*50)
                    print("")
                    for row in res:
                        print(row[0],'\t',row[1],'','',":",'\t',row[2])
                    print('_'*100 )
                    
                else:
                    print("\nYou Enter Invalid Sr. No. , Please Enter Valid Sr. No. ")

            money()
        elif c == 4:
            def variety():
                sno = int(input("\nEnter sr. No.        : "))
                Varieties = input("\nEnter Variety      :")
                print('_'*50)

                curs.execute("insert into vip values('%s','%s')" %(sno,Varieties))
                con.commit()
                print("New Variety added Successfully..!")
                print('_'*100 )
            variety()

        elif c == 5:
            def ad():
                sno = int(input("\nEnter Batch No. of Worker          : "))
                emp = input("\nEnter Name                          : ")
                salary = float(input("\nEnter The Salary of An Worker    : "))
                

                curs.execute("insert into worker values('%s','%s','%s')" %(sno,emp,salary))
                con.commit()
                print('_'*100 )
                print("\nNew Worker Added Successfully..!")

            ad()

        elif c ==6:
            def worker():
                    print("\n\t\tList Of Worker's In Shop")
                    print('_' * 50)

                    curs.execute("select * from worker")
                    res = curs.fetchall()

                    print("\tBatch No.", "\tName", "\t\tSalary")
                    print('_'*50)
                    print("")
                    for row in res:
                        print('\t',row[0],'\t\t',row[1],'', '', '','\t',row[2])
                    print('_'*100 )
            worker()

        elif c == 7:
            def up():
                # worker()
                
                print("\n\t\tList Of Worker's In Shop")
                print('_' * 50)

                curs.execute("select * from worker")
                res = curs.fetchall()

                print("\tBatch No.", "\tName", "\t\tSalary")
                print('_'*50)
                print("")
                for row in res:
                    print('\t',row[0],'\t\t',row[1],'', '', '','\t',row[2])
                print('_'*50 )
                
                print("\nPress 1 :- To Increase The Salary Of worker")
                print("\nPress 1 :- To Decrease The Salary Of worker")

                sig = int(input("\nEnter Your choice(1/2) : "))

                name = input("\nEnter The Name of Worker : ")
                curs.execute("select * from worker where name = '%s'" % name.lower())
                res = curs.fetchone()
                print('_' * 50)
                if res:
                    print("\tBatch No.", "\tName", "\t\tSalary")
                    print('_'*50)
                    print("")
                    
                    print('\t',res[0],'\t\t',res[1],'', '', '','\t',res[2])
                    print('_'*50 )

                else:
                    print("\nWorker Not Found..!")

                if sig == 1:
                    n_salary = float(input("\nEnter How Much Salary You want To Increase  : "))

                    curs.execute("update worker set salary = salary + %.2f where name = '%s'" %(n_salary,name))
                    
                    con.commit()
                    print("\n\nSalary Increases Successfully..!")
                    print('_'*100 )

                    print("\n\tSalary Of worker's (After Increament)")
                    print('_'*50)
                    curs.execute("select * from worker")
                    res = curs.fetchall()

                    print("\tBatch No.", "\tName", "\t\tSalary")
                    print('_'*50)
                    print("")
                    for row in res:
                        print('\t',row[0],'\t\t',row[1],'', '', '','\t',row[2])
                    print('_'*50 )

                elif sig == 2:
                    n_salary = float(input("\nEnter How Much Salary You want To Decrease  : "))

                    curs.execute("update worker set salary = salary - %.2f where name = '%s'" %(n_salary,name))
                    con.commit()
                    print("\n\nSalary Decrease's Successfully..!")
                    print('_'*100 )
                    
                    print("\n\t\tList Of Worker's In Shop (After Decrement)")
                    print('_'*50)
                    curs.execute("select * from worker")
                    res = curs.fetchall()

                    print("\tBatch No.", "\tName", "\t\tSalary")
                    print('_'*50)
                    print("")
                    for row in res:
                        print('\t',row[0],'\t\t',row[1],'', '', '','\t',row[2])
                    print('_'*100 )
                else:
                    print("\nYou Enter Invalid Batch No. , Please Enter Valid Batch No. ")

            up()

        elif c == 8:
            break

        else:
            print("\nSorry You Have Entered The Wrong Input From 1 To 7, Please Enter Valid Option..!")

elif choice == 2:
    print("\n")
    print('='*40 + ""+"WELCOME To Our Bakery"+"" + '='*40)
    print("\n")
    name = input("\nEnter Your Name : ")
    while True:
        number = input("\nEnter Mobile No. : ")

        try:
            if len(number) != 10:
                print("\nPlease Enter a valid Mobile No. \n")
                continue
            else: 
                break

        except ValueError:
            print("\nEnter only numbers\n")
            continue
    print("\nPress 1 :- To See The Menu",sep='.....')
    print("\nPress 2 :- To Order an Item : ")

    c = int(input("\nEnter Your Choice : "))
    
    if c == 1:
        def items():
                print("\n\t\tItem In The Shop ")
                print('_'*50)
                curs.execute("select * from cs")
                res = curs.fetchall()
                print("Sno", "\tProduct", "\tCost")
                print('_'*50)
                print("")
                for row in res:
                    print(row[0],'\t',row[1],'','',":",'\t',row[2])
                print('_'*100 )

        items()
