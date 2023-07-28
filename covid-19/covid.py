import pandas as pd
import matplotlib.pyplot as plt

IR = pd.read_csv("iran.csv")
CA = pd.read_csv("canada.csv")
US = pd.read_csv("australia.csv")
IT = pd.read_csv("italy.csv")
TU = pd.read_csv("turkey.csv")
USA = pd.read_csv("usa.csv")


plt.plot(IR["cases"], color="green", label="Iran")
plt.plot(CA["cases"], color="limegreen", label="Canada")
plt.plot(US["cases"], color="palegreen", label="Australia")
plt.plot(IT["cases"], color="paleturquoise", label="Italy")
plt.plot(TU["cases"], color="deepskyblue", label="Turkey")
plt.plot(USA["nr_cases"], color="dodgerblue", label="USA")

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
labels = ['January','February','March','April','May','June','July','August','September','October','November','December']
plt.xticks(x, labels, rotation=45)
plt.yticks(ticks=[100, 500,1000,1500,2000,2500,3000,3500,4000,4500,5000])

plt.xlabel("Month",fontsize = 17, color= 'cornflowerblue')
plt.ylabel("Number",fontsize = 17, color= 'cornflowerblue')

plt.title("The number of covid 19 cases in 2022 ",fontsize = 25, y= 1.03)

plt.legend()
plt.show()


#people_vaccinated
