__author__ = 'similarities'

import math
import matplotlib.pyplot as plt



# insert laser parameter (Area [cm^2], EL [J], LambdaL [mum],"name", reprate [Hz])


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
        self.transmission = 0.65*self.content




    def calc_I(self):
        self.IL = self.EL * self.transmission/(self.A * self.tau)
        print(self.name, format(self.IL, ".3E"), "Intensity [W/cm^2]", "with", self.content,"fraction of EL in focus")
        print("xxxxxxxxxxx")
        return self.IL

    def calc_Eflux(self):
        self.E_flux = self.EL / self.A
        print(self.name, format(self.E_flux, "0.3E"), "EnergyFlux [J/cm^2]", "reprate:", self.reprate)

    def calc_a0(self):
        # 0.15 gives the ratio of energy content in focal region
        self.a0 = math.sqrt((self.IL* self.lambdaL**2)/(1.38*1E18))
        print(self.name, format(self.a0, "0.3E"), "a0 with:", self.content," energy content in FHWM")
        return self.a0



# insert beam parameter (anlge [rad], distance from focusing optic [cm], beam diameter [cm],
# focal length [cm], radius of area [cm], LambdaL [mum], "name")
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
        self.rayleigh = float


    def angle(self):
        if self.theta == 0 & self.radius == 0:

            self.theta = math.atan(self.diameter * 0.5 / self.focalLength)
            #print(self.name, math.degrees(self.theta), "half angle [degree]")

            print(self.name, format(self.theta, "0.3E"), "half angle [rad]")
            #print("NA:", self.diameter/(2*self.focalLength))
            return self.theta

        elif self.theta < 0 & self.radius == 0:

            print(self.name, 'negative angle!')
            self.theta = self.theta*(-1)
            self.theta = math.radians(self.theta)


        elif self.radius != 0:
            print(self.name,"radius is already given [w0 e.g.]")


        elif self.radius == 0 & self.theta >0:

            #self.theta = math.radians(self.theta)
            #print(self.name, 'half angle [rad]', self.theta)
            self.theta = self.theta

        else:
            Exception




    def areaCalc_by_angle(self):

        self.radius = (self.focalLength - self.length) * math.tan(self.theta)

        area = math.pi * self.radius ** 2

        print(format(self.radius, "0.3E"), 'radius [cm]', self.name)
        print(format(area, "0.3E"), "Area in [cm`2]", self.name)

        return area



    def areaCalc_by_radius(self):

        area = math.pi * self.radius ** 2

        print(format(self.radius, "0.3E"), 'radius [cm]', self.name)
        print(format(area, "0.3E"), "Area in [cm`2]", self.name)

        return area



    def beamwaist_Gaussian(self):

        self.waist0 = 0.5*(4 * self.lambdaL / math.pi) * self.focalLength / self.diameter
        self.rayleigh = math.pi * (self.waist0**2)/self.lambdaL
        #print (self.rayleigh, "Rayleigh length in mum")
        #print("diffraction limit (linear) in mum", self.lambdaL/(self.diameter/self.focalLength))
        #print("minimum beamwaist w0/2 in mum", format(self.waist0, "0.3E"), "f:", self.focalLength)
        self.waist = self.waist0 * 1E-4 * math.sqrt(1 + (self.length / (self.rayleigh * 1E-4)) ** 2)

        print("for f:", self.focalLength, "at length of:", self.length)
        print('half beam waist in cm:', format(self.waist, "0.2E"))

        return self.waist



    def areaCalc_Gaussian(self):

        area = math.pi * (self.waist)**2

        print("Gaussian calculation", format(area, "0.3E"), "Area in [cm^2]")

        return area


# plot parameter (array_y, array_x, "color", "name of plot", "axis label y", "axis label x")
def plot_xy(array_y,array_x, colour, name, name_y, name_x):

    #plot=plt.scatter(array_y, array_x, color=colour,label=name)
    plt.semilogy(array_y, array_x, color=colour,label=name)
    plt.legend() #handles=[plot]
    plt.grid(True)
    plt.ylabel(name_y)
    plt.xlabel(name_x)
    plt.show()


# call Class main(stepsize) for functionalized/ plotted output of either beamwaist, area, I, a0 as a function
# of defocusing length [cm], calculates in 100 mum step

class Main:

    def __init__(self, defocusingLength):

        self.defocusingLength = defocusingLength
        self.array_x = list(range(1, self.defocusingLength))
        self.array_y = list(range(1, self.defocusingLength))
        self.array_I = list(range(1, self.defocusingLength))
        self.array_z = list(range(1, self.defocusingLength))
        self.array_xx = list(range(1, self.defocusingLength))

    # single calls for testing
    # (theta[degree],distance[cm],beam diameter [cm], focal lenght[cm], radius of focused beam [cm], lambda L [in mum], name]

   # area3 = Beam_Area_calculation(0, 150, 0, 0, 5*10**-4, 0.8, "Area3")



    #iL3 = Intensity_calculation(area3.areaCalc_by_radius(), 7.5, 25*1E-15, 0.8, "no 3:", 1)
    #iL3.calc_I()
    #iL3.calc_a0()

    # calculation for prepulse 10-5
    #area1 = Beam_Area_calculation(0, 0, 13, 150, 0, 0.8, "no1 case 1.5m focal length")
    #area1.angle()
    #area1.beamwaist_Gaussian()

    #iL1 = Intensity_calculation(area1.areaCalc_Gaussian(), 7.5, 25*1E-15, 0.8, "no 1:", 1)
    #iL1.calc_I()
    #iL1.calc_a0()
    #area4 = Beam_Area_calculation(0, 1, 13, 150, 0, 0.8, "no1 +1 cm :case1 with 1cm defocusing")
    #area4.angle()
    #area4.beamwaist_Gaussian()
    #iL4 = Intensity_calculation(area4.areaCalc_Gaussian(), 7.5, 25*1E-15, 0.8, "no 1 +1 cm:", 1)
    #iL4.calc_I()


    def defocusin_w0(self):

        for i in range(0, self.defocusingLength-1):
            # i/100 = 100 mu m
            area5 = Beam_Area_calculation(0, i/100, 13, 150, 0, 0.8, "no1 +i * 100 x um defocusing")
            area5.angle()

            self.array_x[i] = i/100
            self.array_y[i] = area5.beamwaist_Gaussian()
            self.array_z[i] = area5.areaCalc_Gaussian()
            #print(self.array_z[i], self.array_x[i], "area per cm")

            i = i + 1

        return self.array_y, self.array_x, self.array_z



    def defocusing_I(self):


        for i in range(0, self.defocusingLength-1):

            iL5 = Intensity_calculation(self.array_z[i], 7.5, 25*1E-15, 0.8, "no 1 +i", 1)
            self.array_I[i] = iL5.calc_I()
            self.array_xx[i] = iL5.calc_a0()

            i = i + 1

        return self.array_I, self.array_x, self.array_xx

# 1 step is 100 mu-m
aha = Main(100)
array_y, array_x, array_z = aha.defocusin_w0()
plot_xy(array_x, array_z, "r",  "area vs defocusing length","A in cm^2", "defocusing in cm")
plot_xy(array_x, array_y, "r",  "half beamwaist vs defocusing","w0 in cm", "defocusing in cm")

array_y, array_x, array_z = aha.defocusing_I()
plot_xy(array_x, array_y, "b",  "intensity vs defocusing","I [W/cm^2]", "defocusing in cm")
plot_xy(array_x, array_z, "g",  "a0 vs defocusing","a0", "defocusing in cm")



