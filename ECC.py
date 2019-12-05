class ECC():

    def __init__(self, a, b, p, k):
        self.a = a
        self.b = b
        self.p = p
        self.k = k
        self.r_x = None
        self.r_y = None

    def setGPoint(self, g):
        self.g_x = g[0]
        self.g_y = g[1]
    
    def setPAPoint(self, pa):
        self.pa_x = pa[0]
        self.pa_y = pa[1]
    
    def setPMPoint(self, pm):
        self.pm_x = pm[0]
        self.pm_y = pm[1]

    def add(self, x_0, y_0, x_1, y_1):
        if x_0 is None:
          self.r_x = x_1
          self.r_y = y_1
          return self.r_x, self.r_y
        if x_1 is None:
          self.r_x = x_0
          self.r_y = y_0
          return self.r_x, self.r_y
        if (x_0 == x_1) and ((y_1 + y_0) == self.p):
          self.r_x = None
          self.r_y = None
          return self.r_x, self.r_y
        if x_0 is not x_1:
          lambduh = (((y_1 - y_0) / (x_1 - x_0)) % self.p)
          lambduh %= self.p
          self.r_x = int((lambduh*lambduh - x_0 - x_1) % self.p)
          self.r_y = int((lambduh*(x_0 - self.r_x) - y_0) % self.p)
          return self.r_x, self.r_y
        lambduh = ((3*x_1*x_1 + self.a) / (y_0*2)) % self.p
        # return int((lambduh*lambduh - x_0 - x_1) % self.p), int(((x_0 - self.r_x)*lambduh - y_0) % self.p)
        self.r_x = int((lambduh*lambduh - x_0 - x_1) % self.p)
        self.r_y = int(((x_0 - self.r_x)*lambduh - y_0) % self.p)
        return self.r_x, self.r_y
    
    def decrypt(self):
        kg_x, kg_y, kpa_x, kpa_y, pm_x, pm_y = self.g_x, self.g_y, self.pa_x, self.pa_y, 0, 0
        # kg, kpa, pm = (0, 0), (0, 0), (0, 0)
        for i in range(self.k):
            kg_x, kg_y = self.add(kg_x, kg_y, self.g_x, self.g_y)
        
        for j in range(self.k):
            kpa_x, kpa_y = self.add(kpa_x, kpa_y, self.pa_x, self.pa_y)
        pm_x, pm_y = self.add(self.pm_x, self.pm_y, kpa_x, kpa_y)
        return {(kg_x, kg_y), (pm_x, pm_y)}


if __name__ == '__main__':
    curve = ECC(-1, 188, 751, 386)
    curve.setGPoint((0,376))
    curve.setPAPoint((201,5))
    curve.setPMPoint((562,201))
    ciphertext = curve.decrypt()
    print(ciphertext)