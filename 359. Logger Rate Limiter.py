#359. Logger Rate Limiter
class Logger:

    def __init__(self):
        self.message = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.message:
            if abs(self.message[message] - timestamp) >= 10:
                self.message[message] = timestamp
                return True
            else: return False
        elif message not in self.message:
            self.message[message] = timestamp
            return True
        else:
            return []
            


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
