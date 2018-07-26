__author__ = 'similarities'

import math



class Intensity_calculation:

    def __init__(self, A, EL, tau, lambdaL, name, reprate, IL=float, a0=float, E_flux=float):
        self.A = A
        self.EL = EL
        self.tau = tau
        self.lambdaL = lambdaL
        self.name = name
        self.reprate = reprate
        self.IL = IL
        self.a0 = a0
        self.E_flux = E_flux



    def calc_I(self):
        self.IL = self.EL/(self.A * self.tau)

        print(self.name, format(self.IL, ".3E"), "Intensity [W/cm^2]", "reprate:", self.reprate)

    def calc_Eflux(self):
        self.E_flux = self.EL / self.A
        print(self.name, format(self.E_flux, "0.3E"), "EnergyFlux [J/cm^2]", "reprate:", self.reprate)

    def calc_a0(self):
        # 0.15 gives the ratio of energy content in focal region
        self.a0 = math.sqrt((self.IL* 0.23* self.lambdaL**2)/(1.38*10E18))
        print(self.name, format(self.a0, "0.3E"), "a0 with 15% energy content in FHWM", "reprate:", self.reprate)


# insert (Area, laser energy, pulse duration, "name", repetition rate)
DamageThreshold1 = Intensity_calculation(1, 3, 25*10E-15, 0.8, "Tien PRL 1999", 1)
DamageThreshold1.calc_I()
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
            #print(self.name, math.degrees(self.theta), "half angle [degree]")
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
        print(self.focalLength-self.length, "test delta length")
        self.radius = (self.focalLength-self.length) * math.tan(self.theta)
        area = math.pi * self.radius ** 2
        print(format(self.radius, "0.3E"), 'radius [cm]', self.name)
        print(format(area, "0.3E"), "Area in [cm`2]", self.name)
        return area

    def areaCalc_by_radius(self):
        area = math.pi * self.radius ** 2
        print(format(self.radius, "0.3E"), 'radius [cm]', self.name)
        print(format(area, "0.3E"), "Area in [cm`2]", self.name)
        return area

# insert laser parameter (half angle focusing, distance from focusing optic, D [cm], f[cm], radius[cm],"name")



class Main:



    area2 = Beam_Area_calculation(-12, 170, 0, 0, 0, "Area2")
    area3 = Beam_Area_calculation(0, 170, 0, 0, (0.00006), "Area3")


    area2.angle()
    area2.areaCalc_by_angle()

    iL3 = Intensity_calculation(area3.areaCalc_by_radius(), 3.5, 25*10E-15, 0.8, "no 3:", 1)
    iL3.calc_I()
    iL3.calc_a0()

    iL2 = Intensity_calculation(area2.areaCalc_by_angle(), 3.5, 25*10E-15, 0.8, "no 2:", 1)
    iL2.calc_I()

    # calculation for prepulse 10-5
    area1 = Beam_Area_calculation(0, 149.95, 13, 150, 0, "Area1")
    area4 = Beam_Area_calculation(0, 149.8+1.3, 13, 150, 0, "Area1 =1cm")
    area1.angle()
    area4.angle()
    iL1 = Intensity_calculation(area1.areaCalc_by_angle(), 3.5*10E-5, 25*10E-15, 0.8, "no 1:", 1)
    iL1.calc_I()
    iL4 = Intensity_calculation(area4.areaCalc_by_angle(), 3.5, 25*10E-15, 0.8, "no 1 +1 cm:", 1)
    iL4.calc_I()


Main()




