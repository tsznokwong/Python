class PID:
    Cp = 0.3
    Ci = 0.5
    Cd = 0.1

    target = 80
    current = 10
    flow = 0.2
    
    cycleTime = 0.1
    currentTime = 0

    def error(self):
        return self.target - self.current

    integral = 0
    previousCycleError = 0
    def differential(self):
        return (self.error() - self.previousCycleError) / self.cycleTime

    epsilon = 0.0001

    def adjust(self):
        self.currentTime += self.cycleTime
        self.previousCycleError = self.error()
        self.integral += self.error() * self.cycleTime
        self.current += self.flow
        self.flow += self.Cp * self.error() + self.Ci * self.integral + self.Cd * self.differential()
        print(self.target, self.current, self.error())
        if abs(self.error()) > self.epsilon:
            self.adjust()
        
    def __init__(self):
        self.adjust()

    def set_flow(self, x):
        self.flow = x
        self.adjust()

    def set_target(self, x):
        self.target = x
        self.adjust()

    def set_current(self, x):
        self.current = x
        self.adjust()


