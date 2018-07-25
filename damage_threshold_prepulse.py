__author__ = 'similarities'

import math



class Intensity_calculation:

    def __init__(self, A, EL, tau, name, reprate, IL=float, E_Flux = float, LambdaL = float, a0 = float):
        self.A = A
        self.EL = EL
        self.tau = tau
        self.name = name
        self.reprate = reprate
        self.IL = IL
        self.LambdaL = LambdaL # in micro-meter
        self.a0 = a0
        self.E_Flux = E_Flux




    def calcI(self):
        self.IL = self.EL/(self.A * self.tau)

        print(format(self.IL, ".3E"), "Intensity [W/cm^2], single")

    def calc_Eflux(self):
        self.E_flux = self.EL / self.A
        print(format(self.E_Flux, "0.3E"), "EnergyFlux [J/cm^2],single")

    def calc_a0(self):
        self.a0 = math.sqrt((self.IL * self.lambdaL**2)/(1.3*10**18))

# insert (Area, laser energy, pulse duration, "name", repetition rate)
DamageThreshold1 = Intensity_calculation(1, 3, 25*10E-15, "Tien PRL 1999", 1)
print(DamageThreshold1.name)
DamageThreshold1.calcI()
DamageThreshold1.calc_Eflux()


class Beam_Area_calculation:
    def __init__(self, theta, length, diameter, focalLength, radius, name):
        self.theta = theta
        self.length = length
        self.diameter = diameter
        self.focalLength = focalLength
        self.name = name
        self.radius = radius

    def angle(self):
        if self.theta == 0 & self.radius == 0:
            self.theta = math.atan(self.diameter * 0.5 /self.focalLength)
            print(self.name, math.degrees(self.theta), "half angle [degree]")
            print(self.name, format(self.theta, "0.3E"), "half angle [rad]")
            #print(self.theta, ' new theta from outside')

        elif self.theta < 0 & self.radius == 0:
            print(self.name, 'negative angle!')
            self.theta = self.theta*(-1)
            self.theta = math.radians(self.theta)


        elif self.radius != 0:
            print(self.name,"radius is already given [w0 e.g.]")

        elif self.radius == 0 & self.theta >0:
            self.theta = math.radians(self.theta)
            print(self.name, 'half angle [rad]', self.theta)




    def areaCalc_by_angle(self):

        self.radius = self.length * math.tan(self.theta) * math.cos(self.theta)
        area = math.pi * self.radius ** 2
        print(format(self.radius, "0.3E"), 'radius [cm]', self.name)
        print(format(area, "0.3E"), "Area in [cm`2]", self.name)

    def areaCalc_by_radius(self):
        area = math.pi * self.radius ** 2
        print(format(self.radius, "0.3E"), 'radius [cm]', self.name)
        print(format(area, "0.3E"), "Area in [cm`2]", self.name)

# insert laser parameter (half angle focusing, distance from focusing optic, D [cm], f[cm], radius[cm],"name")
area1 = Beam_Area_calculation(0, 56, 13, 150, 0, "Area1")
area2 = Beam_Area_calculation(-12, 170, 0, 0, 0, "Area2")
area3 = Beam_Area_calculation(0, 170, 0, 0, (0.00006), "Area3")
area1.angle()
area1.areaCalc_by_angle()


area2.angle()
area2.areaCalc_by_angle()

area3.areaCalc_by_radius()

