__author__ = 'SuSh'
import re
class IllegalArgumentException(Exception):
    """Base class for exceptions in this module."""
    def __int__(self,message):
        Exception.__init__(self,message)

class user_info(object):
    def __init__(self, userName, msisdn, initialBalance, circle,plan="GENERAL_PLAN"):
        self.userName = userName
        self.circle = circle
        self.msisdn = msisdn
        self.initialbalance = initialBalance
        self.plan=plan

class Plan(object):
    def __init__(self, name, std_cost_sms, std_cost_call, local_cost_sms,local_cost_call):
        self.name = name
        self.std_cost_sms = std_cost_sms
        self.std_cost_call = std_cost_call
        self.local_cost_sms = local_cost_sms
        self.local_cost_call = local_cost_call

    def call_cost(self):
        pass

class TelecomServiceProvider:
    def __init__(self):
        self.user_dict={}


    def validation(self,uname,msisdn,circle):
        circles_list=["NCR", "Maharashtra", "Kolkata", "Tamilnadu"]
        if re.match("^[a-zA-Z]*$", uname):
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
            ud=user_info(userName, msisdn, initialBalance, circle)
            self.user_dict[msisdn]=ud


    #throw IllegalArgumentException if circle(whole country is divided into various circles) is not from the list of circles              {"NCR", "Maharashtra", "Kolkata", "Tamilnadu"}
	#msisdn- phone number with country code- e.g "919980032533"

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
            for i in self.user_dict:
                if msisdn == i[msisdn]:
                    i[plan]=planName
                else:
                    return "msisdn don't exist"

    def getcallrates(self,planName):
        if(planName=="GENERAL_PLAN"):
            return 1,1
        elif(planName=="STD_PLAN"):
            return 1.25,0.75
        elif(planName=="LOCAL_PLAN"):
            return 0.75,1.25
    def getsmsrates(self,planName):
        if(planName=="GENERAL_PLAN"):
            return 1,1
        elif(planName=="STD_PLAN"):
            return 1.2,0.5
        elif(planName=="LOCAL_PLAN"):
            return 0.5,1.2
    def makeCall(self, msisdn, callDurationInSecs, destinationCircle="DEFAULT"):
    #return user's updated balance based on his plan, call duration and destination circle
    #throw IllegalArgumentException if destinationCircle is not from the list of circles provided
        callDurationInSecs=int(callDurationInSecs)
        for i in self.list_of_users:
            if msisdn == i.msisdn:
                local,std=self.getcallrates(i.plan)
                min=(callDurationInSecs-1)/60+1
                i.balance=i.balance-min*local
        else:
            return "msisdn don't exist"

    def sendSMS(self, msisdn, destinationCircle="DEFAULT"):
    #return user's updated balance based on his plan and destination circle
    #throw IllegalArgumentException if destinationCircle is not from the list of circles provided
        for i in self.list_of_users:
            if msisdn == i.msisdn:
                local,std=self.getsmsrates(i.plan)
                i.balance=i.balance-local
        else:
            return "msisdn don't exist"

    def recharge(self, msisdn, rechargeAmount):
        try:
            if rechargeAmount>0:
                if self.user_dict[msisdn]:
                    self.user_dict[msisdn].initialbalance += rechargeAmount
                else:
                    raise Exception("No user with such MSISDN")
            else:
                raise Exception("Enter Positive Amount!")
        except Exception as e:
            print e
    #update the balance amount based on rechargeAmount

    def getBalanceAmount(self, msisdn):
        try:
            if self.user_dict[msisdn]:
                return self.user_dict[msisdn].initialbalance
            else:
                raise Exception("No user with such MSISDN")
        except Exception as e:
            print e
    #returns the current balance for given msisdn

    def getUsername(self, msisdn):
        try:
            if self.user_dict[msisdn]:
                print "User name with msisdn",self.user_dict[msisdn].msisdn,"is:",self.user_dict[msisdn].userName
            else:
                raise Exception("No user with such MSISDN")
        except Exception as e:
            print e
            pass
    #returns the name of user for given msisdn


if __name__ == "__main__":
    tsp=TelecomServiceProvider()
    try:
        tsp.registerUser("ShravanRachiraju","919701806599",0,"NCR")
        tsp.registerUser("Shravan Rachiraju","919701806599",0,"NCR")
        tsp.registerUser("ShravanRachiraju","9701806599",0,"NCR")
        tsp.registerUser("ShravanRachiraju","919701806599",0,"AP")
        tsp.getUsername("919701806599")
    except IllegalArgumentException as msg:
        print msg.message
