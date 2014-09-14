class User(object):
    def __init__(self,userName = "", msisdn = "", initialBalance = 0, circle = ""):
        self.userName = userName
        self.msisdn = msisdn
        self.initialbalance = initialBalance
        self.circle = circle
        self.plan = Plan

class Plan(object):
    def __init__(self, name, std_cost_sms, std_cost_call, local_cost_sms,local_cost_call):
        self.name = name
        self.std_cost_sms = std_cost_sms
        self.std_cost_call = std_cost_call
        self.local_cost_sms = local_cost_sms
        self.local_cost_call = local_cost_call

    def call_cost(self):
        pass

class Plans(object):
    GeneralPlan = Plan("GENERAL_PLAN",1.0,1.0,1.0,1.0)
    StdPlan = Plan("STD_PLAN",0.75,0.5,1.25,1.2)
    LocalPlan = Plan("LOCAL_PLAN",1.25,1.2,0.75,0.5)


class TelecomServiceProvider:

    list_of_circles_without_service = {"NCR", "Maharashtra", "Kolkata", "Tamilnadu"}
    def __init__(self):
        self.all_users = {}

    def registerUser(self, userName, msisdn, initialBalance, circle):
        try:
            if circle not in self.list_of_circles_without_service:
                raise Exception("IllegalArgumentException")
            else:
                newUser = User(userName, msisdn, initialBalance, circle)
                self.all_users[msisdn]=newUser
        except Exception as e:
            print e


    def setPlan(self, msisdn, planName):
        try:
            if self.all_users[msisdn]:
                if planName == "GENERAL_PLAN":
                    self.all_users[msisdn].plan = Plans.GeneralPlan
                elif planName == "STD_PLAN":
                    self.all_users[msisdn].plan = Plans.StdPlan
                elif planName == "LOCAL_PLAN":
                    self.all_users[msisdn].plan = Plans.LocalPlan
            else:
                raise Exception("No such registered User")
        except Exception as e:
            print e
            pass

    def makeCall(self, msisdn, callDurationInSecs, destinationCircle):
        try:
            if destinationCircle not in self.list_of_circles_without_service:
                raise Exception("IllegalArgumentException")
            else:
                if self.all_users[msisdn]:
                    if self.all_users[msisdn].circle == destinationCircle:
                        self.all_users[msisdn].initialbalance -= callDurationInSecs*(self.all_users[msisdn].plan.local_cost_call/60)
                    else:
                        self.all_users[msisdn].initialbalance -= callDurationInSecs*(self.all_users[msisdn].plan.std_cost_sms/60)
                    return self.all_users[msisdn].initialbalance
                else:
                    print "ERROR:No Such User.Not allowed to make a call"
        except Exception as e:
            print e

	        #return user's updated balance based on his plan, call duration and destination circle
	        #throw IllegalArgumentException if destinationCircle is not from the list of circles provided
            pass
    def sendSMS(self, msisdn, destinationCircle):
        try:
            if destinationCircle not in self.list_of_circles_without_service:
                raise Exception("IllegalArgumentException")
            else:
                if self.all_users[msisdn]:
                    if self.all_users[msisdn].circle == destinationCircle:
                        self.all_users[msisdn].initialbalance -= self.all_users[msisdn].plan.local_cost_sms
                    else:
                        self.all_users[msisdn].initialbalance -= self.all_users[msisdn].plan.std_cost_sms
                    return self.all_users[msisdn].initialbalance
                else:
                    print "ERROR:No Such User.Not allowed to make a call"
        except Exception as e:
            print e


    def recharge(self, msisdn, rechargeAmount):
        try:
            if rechargeAmount>0:
                if self.all_users[msisdn]:
                    self.all_users[msisdn].initialbalance += rechargeAmount
                else:
                    raise Exception("No Such User")
            else:
                raise Exception("Negative recharge Amount")
        except Exception as e:
            print e
        #update the balance amount based on rechargeAmount
    def getBalanceAmount(self, msisdn):
        try:
            if self.all_users[msisdn]:
                return self.all_users[msisdn].initialbalance
            else:
                raise Exception("No Such User")
        except Exception as e:
            print e
        #returns the current balance for given msisdn
        pass

    def getUsername(self, msisdn):
        try:
            if self.all_users[msisdn]:
                return self.all_users[msisdn].userName
            else:
                raise Exception("No Such User")
        except Exception as e:
            print e
            pass


if __name__=="__main__":
    Airtel = TelecomServiceProvider()
    Airtel.registerUser("Shravan","919703489059",99,"Maharashtra")
    Airtel.setPlan("919703489059","GENERAL_PLAN")
    #UserOne = User("Shravan","919703489059","99","Hyderabad")
    Airtel.registerUser("sairam","919441226037",99,"Maharashtra")
    #UserTwo = User("sairam","919441226037","99","Hyderabad")
    print Airtel.getBalanceAmount("919703489059")
    print Airtel.getBalanceAmount("919441226037")
    print Airtel.makeCall("919703489059",99,"Maharashtra")
    Airtel.registerUser('test','91919191123',3,'Maharashtra')
    Airtel.setPlan("91919191123","GENERAL_PLAN")
    print Airtel.makeCall('91919191123',100,"Maharashtra")