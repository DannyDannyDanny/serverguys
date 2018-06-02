def newlog():
    # try to append to the file
    print("clearing log")
    fa = open("weatherguy/weather.log","w")
    fa.write("-------- LOG FILE --------")
    fa.close()
    #break

def log(text):
    print(text)
    try:
        # try to append to the file
        fa = open("weatherguy/weather.log","a")
        fa.write("\n"+text)
        fa.close()
        #break
    except:
        # otherwise replace the file
        fw = open("weatherguy/weather.log","a")
        fw.write("Failures")
        fw.write("\n"+text)
        fw.close()
