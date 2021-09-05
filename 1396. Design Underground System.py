#1396. Design Underground System
class UndergroundSystem:

    def __init__(self):
        self.id = {}
        self.pair = Counter()
        self.freq = Counter()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.id[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        name, t_in = self.id.pop(id)
        self.pair[(name,stationName)] += t - t_in
        self.freq[(name,stationName)] += 1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.pair[(startStation,endStation)]/self.freq[(startStation, endStation)]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
