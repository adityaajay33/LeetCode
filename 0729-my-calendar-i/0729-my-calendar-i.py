class MyCalendar:

    def __init__(self):
        #bisect insort
        self.schedule = []
        

    def book(self, start: int, end: int) -> bool:
        if not self.schedule or self.schedule[0]>=end:
            self.schedule.insert(0, end)
            self.schedule.insert(0, start)
            return True
        elif self.schedule[-1]<=start:
            self.schedule.append(start)
            self.schedule.append(end)
            return True

        ind = bisect_right(self.schedule, start)
        ind1 = bisect_left(self.schedule, end)

        if ind1==ind and ind%2==0:
            self.schedule.insert(ind, start)
            self.schedule.insert(ind+1, end)
            return True
        else:
            return False

#[20,29],[13,22],[44,50],[1,7],[2,10],[14,20]
                


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)