from abc import ABC,abstractmethod 


class Notifier(ABC):
    @abstractmethod
    def send(self,message):
        pass


class EmailNotifer(Notifier):
    def send(self,message):
        print("email sent")

class SMSNotifier(Notifier):
    def send(self,message):
        print("message sent")

class PushNotifier(Notifier):
    def send(self,message):
        print("push sent")

class NotiferFactory:
    @classmethod
    def create_notifer(cls,notifier):
        if notifier == "email" :
            return EmailNotifer()
        elif notifier == "sms":
            return SMSNotifier()
        elif notifier == "push":
            return PushNotifier()
        else:
            raise Exception("fuck you!")


def main():
    sms = NotiferFactory.create_notifer("sms")
    push = NotiferFactory.create_notifer("push")
    
    sms.send("hello")
    push.send("hello")
    
main()

