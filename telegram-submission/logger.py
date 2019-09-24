def newlog():
    # try to append to the file
    fa = open("log.log","w")
    fa.write("-------- LOG FILE --------")
    fa.close()
    #break

def log(text):
    try:
        # try to append to the file
        fa = open("log.log","a")
        fa.write("\n"+text)
        fa.close()
        #break
    except:
        # otherwise replace the file
        fw = open("log.log","a")
        fw.write("dsgfh")
        fw.write("\n"+text)
        fw.close()
