__author__ = 'SuSh'
import re
class IllegalArgumentException(Exception):
    def __init__(self,message):
        Exception.__init__(self,message)

class User_details:
    def __init__(self,userName, msisdn, initialBalance,circle,plan="GENERAL_PLAN"):
        self.userName=userName
        self.msisdn=msisdn
        self.balance=initialBalance
        self.circle=circle
        self.plan=plan
        self.vas=[]
class VAS:
    def __init__(self,vasName, validfrom, validTill, subsciptionCharges):
        self.vasName=vasName
        self.validfrom=validfrom
        self.validtill=validTill
        self.subsciptionCharges=subsciptionCharges

class TelecomServiceProvider:

    def __init__(self):
        self.list_of_users=[]
        self.list_of_vas=[]

    def validation(self,uname,msisdn,circle):
        circles_list=["NCR", "Maharashtra", "Kolkata", "Tamilnadu"]
        if re.match("^[a-zA-Z]*$", uname) :
            if re.match("^([91]{2})([0-9]{10})*$",msisdn):
                if circle in circles_list:
                    return True
                else:
                    raise IllegalArgumentException("Circle Not in List")
            else:
                return -1
        else:
            return -2

    def registerUser(self, userName, msisdn, initialBalance, circle):
    #throw IllegalArgumentException if circle(whole country is divided into various circles) is not from the list of circles {"NCR", "Maharashtra", "Kolkata", "Tamilnadu"}
    #msisdn- phone number with country code- e.g "919980032533"
        result = self.validation(userName, msisdn, circle)
        if result == -1:
            print "Error In MSISDN"
        elif result == -2:
            print "Error In UserName"
        else:
            print "Valid Details"
            user=User_details(userName, msisdn, initialBalance, circle)
            self.list_of_users.append(user)

    def setPlan(self, msisdn, planName):
    #There are 3 plans as of now:
    #GENERAL_PLAN
    #STD Call Rs1/min Local Call Rs1/min
    #STD SMS Rs1 Local SMS Rs1
    #
    #STD_PLAN
    #STD Call Rs0.5/min Local CallRs1.2/min
    #STD SMS Rs0.75 Local SMS Rs1.25
    #
    #LOCAL_PLAN
    #Local Rs0.5/min, STD Rs1.2/min
    #STD SMS Rs1.25 Local SMS Rs.75
        for i in range(len(self.list_of_users)):
            if msisdn == self.list_of_users[i].msisdn:
                 self.list_of_users[i].plan=planName
        else:
            return "msisdn don't exist"
    def getsmsrates(self,planName):
        if(planName=="GENERAL_PLAN"):
            return 1,1
        elif(planName=="STD_PLAN"):
            return 1.25,0.75
        elif(planName=="LOCAL_PLAN"):
            return 0.75,1.25
    def getcallrates(self,planName):
        if(planName=="GENERAL_PLAN"):
            return 1,1
        elif(planName=="STD_PLAN"):
            return 1.2,0.5
        elif(planName=="LOCAL_PLAN"):
            return 0.5,1.2
    def makeCall(self, msisdn, callDurationInSecs, destinationCircle="DEFAULT"):
    #return user's updated balance based on his plan, call duration and destination circle
    #throw IllegalArgumentException if destinationCircle is not from the list of circles provided
        for i in range(len(self.list_of_users)):
            if msisdn == self.list_of_users[i].msisdn:
                local,std=self.getcallrates(self.list_of_users[i].plan)
                min=(int(callDurationInSecs)-1)/60+1;
                self.list_of_users[i].balance=self.list_of_users[i].balance-min*local
                return "call sucessful"
        else:
            return "msisdn don't exist"

    def sendSMS(self, msisdn, destinationCircle="DEFAULT"):
    #return user's updated balance based on his plan and destination circle
    #throw IllegalArgumentException if destinationCircle is not from the list of circles provided
        for i in range(len(self.list_of_users)):
            if msisdn == self.list_of_users[i].msisdn:
                local,std=self.getsmsrates(self.list_of_users[i].plan)
                self.list_of_users[i].balance=self.list_of_users[i].balance-local
                return "sms sucessful"
        else:
            return "msisdn don't exist"

    def recharge(self, msisdn, rechargeAmount):
    #update the balance amount based on rechargeAmount
        for i in range(len(self.list_of_users)):
            if msisdn == self.list_of_users[i].msisdn:
                self.list_of_users[i].balance=self.list_of_users[i].balance+int(rechargeAmount);
                return "recharged sucessfully"
        else:
            return "msisdn don't exist"

    def getBalanceAmount(self, msisdn):
    #returns the current balance for given msisdn
        for i in range(len(self.list_of_users)):
            if msisdn == self.list_of_users[i].msisdn:
                return self.list_of_users[i].balance
        else:
            return "msisdn don't exist"

    def getUsername(self, msisdn):
    #returns the name of user for given msisdn
        for i in range(len(self.list_of_users)):
            if msisdn == self.list_of_users[i].msisdn:
                return self.list_of_users[i].userName
        else:
            return "msisdn don't exist"
    def addVAS(self,vasName, validfrom, validTill, subsciptionCharges):
        vas=VAS(vasName, validfrom, validTill, subsciptionCharges)
        self.list_of_vas.append(vas)

    def subscribeVAS(self,msisdn, vasName):
    #return false if not enough balance or VAS validity period has expired
        for i in range(len(self.list_of_users)):
            if msisdn == self.list_of_users[i].msisdn:
                self.list_of_users[i].vas.append(vasName)
                return "successfully subsrcibed"
        else:
            return "msisdn don't exist"

    def getSubscribedUserCount(self,vasName):
    #return count of users subscribed for given VAS
        c=0
        for i in range(len(self.list_of_users)):
            for j in self.list_of_users[i].vas:
                if(j==vasName):
                    c=c+1
        return c

    def userSubscribed(self,msisdn, vasName):
    #return true if the user is subscribed to mentioned VAS
        for i in range(len(self.list_of_users)):
            if msisdn == self.list_of_users[i].msisdn:
                for j in self.list_of_users[i].vas:
                    if(j==vasName):
                        return "Subscribed"
                else:
                    return "not subscribed"

        return "msisdn not found"

    def getVASListForUser(self,msisdn):
    #return a String[] containing names of various VASs subscribed by the user
        for i in range(len(self.list_of_users)):
            if msisdn == self.list_of_users[i].msisdn:
                return self.list_of_users[i].vas
        return "msisdn don't exsits"


    def downloadData(self,msisdn, kiloBytes):
    #update the balance based on downloaded data
        for i in range(len(self.list_of_users)):
            if msisdn == self.list_of_users[i].msisdn:
                self.list_of_users[i].balance=self.list_of_users[i].balance-((int(kiloBytes)-1)/10+1)*0.1
                return "sucessfull"
        return "msisdn not found"

if __name__=="__main__":

    tsp=TelecomServiceProvider()
    try:
        tsp.registerUser("ShravanRachiraju","919701806599",0,"NCR")


    #     while(True):
    #         print("1.register")
    #         print("2.getbalance")
    #         print("3.getusername")
    #         print("4.makecall")
    #         print("5.sendsms")
    #         print("6.setplan")
    #         print("7.add balance")
    #         print("8.exit")
    #         i=raw_input("enter your choice")
    #         if(i=="1"):
    #             name=raw_input("enter your name")
    #             msisdn=raw_input("enter mobile number")
    #             circle=raw_input("enter your circle name")
    #             T.registerUser(name,msisdn,0,circle)
    #         elif(i=="2"):
    #             msisdn=raw_input("enter mobile number")
    #             print T.getBalanceAmount(msisdn)
    #         elif(i=="3"):
    #             msisdn=raw_input("enter mobile number")
    #             print T.getUsername(msisdn)
    #         elif(i=="4"):
    #             msisdn=raw_input("enter mobile number")
    #             duration=raw_input("enter the duration")
    #             print T.makeCall(msisdn,duration)
    #         elif(i=="5"):
    #             msisdn=raw_input("enter mobile number")
    #             print T.sendSMS(msisdn)
    #         elif(i=="6"):
    #             msisdn=raw_input("enter mobile number")
    #             print("""#There are 3 plans as of now:
    # #1.GENERAL_PLAN
    # #STD Call Rs1/min Local Call Rs1/min
    # #STD SMS Rs1 Local SMS Rs1
    # #
    # #2.STD_PLAN
    # #STD Call Rs0.5/min Local CallRs1.2/min
    # #STD SMS Rs0.75 Local SMS Rs1.25
    # #
    # #3.LOCAL_PLAN
    # #Local Rs0.5/min, STD Rs1.2/min
    # #STD SMS Rs1.25 Local SMS Rs.75""")
    #             i=raw_input("enter your choice")
    #             if(i=="1"):
    #                 T.setPlan(msisdn,"GENERAL_PLAN")
    #             elif(i=="2"):
    #                 T.setPlan(msisdn,"STD_PLAN")
    #             elif(i=="3"):
    #                 T.setPlan(msisdn,"LOCAL_PLAN")
    #         elif(i=="7"):
    #             msisdn=raw_input("enter mobile number")
    #             balance=raw_input("enter the recharge balance")
    #             T.recharge(msisdn,balance)
    #         elif(i=="8"):
    #             break;

    except IllegalArgumentException as ilae:
        print ilae.message