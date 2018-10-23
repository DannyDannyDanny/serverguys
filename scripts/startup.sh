# run at linux startup.
# updates and upgrades system
#sudo apt update; sudo apt upgrade -y


#OF=$(date +%Y%m%d)
# make logfile for this week
Min=$(date +%M)
Hour=$(date +%H)
Day=$(date +%a)
Week=$(date +%V)
Year=$(date +%Y)

Logfilename=$Hour$Min-$Day-$Week-$Year.log

echo making logfile $Logfilename
touch ../logs/$Logfilename
echo $(date +%H):$(date +%M):$(date +%S) log created >> ../logs/$Logfilename

#rm rf ../logs/*
