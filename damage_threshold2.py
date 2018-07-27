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
        self.content = 0.4
        self.transmission = 0.56*0.66*self.content



    def calc_I(self):
        self.IL = self.EL * self.transmission/(self.A * self.tau)
        print(self.name, format(self.IL, ".3E"), "Intensity [W/cm^2]", "with", self.content,"fraction of EL in focus")
        print("xxxxxxxxxxx")

    def calc_Eflux(self):
        self.E_flux = self.EL / self.A
        print(self.name, format(self.E_flux, "0.3E"), "EnergyFlux [J/cm^2]", "reprate:", self.reprate)

    def calc_a0(self):
        # 0.15 gives the ratio of energy content in focal region
        self.a0 = math.sqrt((self.IL* self.lambdaL**2)/(1.38*1E18))
        print(self.name, format(self.a0, "0.3E"), "a0 with:", self.content," energy content in FHWM", "reprate:", self.reprate)



class Beam_Area_calculation:
    def __init__(self, theta, length, diameter, focalLength, radius, lambdaL, name, waist0 = float, waist = float):
        self.theta = theta
        self.length = length
        self.diameter = diameter
        self.focalLength = focalLength
        self.name = name
        self.radius = radius
        self.lambdaL = lambdaL
        self.waist0 = waist0
        self.waist = waist

    def angle(self):
        if self.theta == 0 & self.radius == 0:
            self.theta = math.atan(self.diameter * 0.5 /self.focalLength)
            #print(self.name, math.degrees(self.theta), "half angle [degree]")
            print(self.name, format(self.theta, "0.3E"), "half angle [rad]")
            #print("NA:", self.diameter/(2*self.focalLength))
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
        self.radius = (self.length-self.focalLength) * math.tan(self.theta)
        area = math.pi * self.radius ** 2
        print(format(self.radius, "0.3E"), 'radius [cm]', self.name)
        print(format(area, "0.3E"), "Area in [cm`2]", self.name)
        return area

    def areaCalc_by_radius(self):
        print(self.radius)
        area = math.pi * self.radius ** 2
        print(format(self.radius, "0.3E"), 'radius [cm]', self.name)
        print(format(area, "0.3E"), "Area in [cm`2]", self.name)
        return area

    def areaCalc_Gaussian(self):
        self.waist0 = 0.5*(4 * (self.lambdaL) / math.pi) * self.focalLength / self.diameter
        print(self.name)
        #print("diffraction limit (linear) in mum", self.lambdaL/(self.diameter/self.focalLength))

        print("minimum beamwaist w0/2 in mum", format(self.waist0, "0.3E"), "f:", self.focalLength)
        self.waist = self.waist0 *1E-4 * math.sqrt(1+(self.lambdaL*1E-4 * (self.length-self.focalLength)/(math.pi* self.waist0*1E-4)))
        print("for f:", self.focalLength, "at length of:", self.length)
        print('half beamwaist in cm:', format(self.waist, "0.2E"))
        area = math.pi * (self.waist)**2
        print("Gaussian calculation", format(area, "0.3E"), "Area in [cm^2]")

        return area
# insert laser parameter (half angle focusing, distance from focusing optic, D [cm], f[cm], radius[cm],"name")



class Main:


    # (theta[degree],distance[cm],beam diameter [cm], focal lenght[cm], radius of focused beam [cm], lambda L [in mum], name]

   # area3 = Beam_Area_calculation(0, 150, 0, 0, 5*10**-4, 0.8, "Area3")



    #iL3 = Intensity_calculation(area3.areaCalc_by_radius(), 7.5, 25*1E-15, 0.8, "no 3:", 1)
    #iL3.calc_I()
    #iL3.calc_a0()

    # calculation for prepulse 10-5
    area1 = Beam_Area_calculation(0, 150, 13, 150, 0, 0.8, "no1 case 1.5m focal length")
    area1.angle()

    iL1 = Intensity_calculation(area1.areaCalc_Gaussian(), 7.5, 25*1E-15, 0.8, "no 1:", 1)
    iL1.calc_I()
    iL1.calc_a0()
    area4 = Beam_Area_calculation(0, 150+1, 13, 150, 0, 0.8, "no1 +1 cm :case1 with 1cm defocusing")
    area4.angle()
    iL4 = Intensity_calculation(area4.areaCalc_Gaussian(), 7.5, 25*1E-15, 0.8, "no 1 +1 cm:", 1)
    iL4.calc_I()


Main()




