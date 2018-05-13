def cashRemove():
    import pymysql as sql, tkinter as kin

    gui = kin.Tk()

    def withdrawl():
        db = sql.connect("localhost", "root", "", "newbank")
        curs = db.cursor()

        curs.execute("Select Balance from bank1 where Name = '{}'".format("Will"))
        data = curs.fetchall()

        money = float(takeAmount.get())
        print(data[0][0])
        val = data[0][0]
        val2 = val-money
        #val2_string=str(val2)

        print("£" , val)
        print("You have withdrawn £" , val2)

        curs.execute("update bank1 set Balance = '{}' where Name = '{}'".format(val2,"Will"))
        db.commit()
        db.close



    gui.geometry("500x700")
    takeAmount=kin.IntVar()




    label1 = kin.Label(gui, text="ATM", fg = "Blue").grid(row = 0, column = 2)
    label2 = kin.Label(gui, text="Withdrawl amount", fg = "red").grid(row = 1, column = 0)

    take = kin.Entry(gui,textvariable = takeAmount).grid (row = 3, column = 2)


    button = kin.Button(gui, text = "Withdraw", command = withdrawl).grid(row = 4, column = 2)
    gui.mainloop()

cashRemove()
