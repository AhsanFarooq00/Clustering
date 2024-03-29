
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.optimize import curve_fit
from scipy import stats



# Your provided data
years = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
Australia_CO2 = [263437.5,264709.7,268366.5,273016.9,280096.3,290141.5,300180.4,307778.5,327536.9,333677.7,339422.8,345609.4,353315.8,352893.5,366141.6,368801.9,374104.4,384368.3,387570.3,393859.7,395993.2,394436.7,395690,388427.4,379267.2,385782.4,394803.6,397149.4,396059.9,395199.1,378996.8]
China_CO2 = [2173364.2, 2302185.2, 2418175.3, 2645411.7, 2767666.4, 3088620.2, 3070505.1, 3134112.6, 3236278.6, 3153661.1, 3346525.8, 3529081.3, 3796157.1, 4424412.6, 5113216.6, 5824625.1, 6437470.3, 6993182.8, 7199604.7, 7719071.4, 8474922.7, 9282553.7, 9540539.7, 9979128, 10021043.4, 9859281.2, 9860914, 10089273.2, 10567262, 10762824, 10944686.2]
Pakistan_CO2 = [59026,60305.8,66977.8,73749.6,76253.6,82737.2,85821.1,89362.5,90190.3,98773.3,98374.1,99837.2,102325.6,105663.5,118313.6,121608.7,132304.2,145813.3,140734.2,145337.9,140378.6,141690,143819.1,145993.7,154235.2,164152.3,181113.3,198738.8,186865.6,184096.3,184111.2]
Russia_CO2 = [2163533.1, 2136444.3, 2030810.7, 1880244.5, 1685046.3, 1635484.8, 1601176.5, 1489506.5, 1487965, 1523721.3, 1563845.6, 1567172, 1565334.4, 1609996.7, 1600978.5, 1611982.1, 1654851, 1658148.6, 1655191.1, 1546666.4, 1617827.5, 1699083.2, 1675755.9, 1632679.7, 1611960.7, 1592559.4, 1571517.3, 1594550.3, 1661000, 1703588.7, 1618271]

Australia_GDP_Per_Capita = [18248.94071,18859.40796,18623.79174,17699.55774,18129.40219,20448.12197,22021.78391,23646.62305,21479.1142,20712.66978,21870.41597,19695.72974,20301.84317,23718.13385,30836.73068,34479.76793,36595.70715,41051.61207,49701.28178,42816.5674,52147.02419,62609.66072,68078.04423,68198.41934,62558.24388,56758.8692,49918.79393,53954.55349,57273.52048,55049.57192,51868.24756]
China_GDP_Per_Capita = [347.5783659, 359.2132687, 423.3044301, 525.3656924, 473.4899164, 609.6043379, 709.4158882, 781.7425612, 828.594691, 873.297611, 959.3604313, 1053.112314, 1148.514257, 1288.637491, 1508.667916, 1753.414192, 2099.21943, 2693.958732, 3468.327063, 3832.227457, 4550.473944, 5614.386022, 6300.58218, 7020.386074, 7636.07434, 8016.445595, 8094.390167, 8817.045608, 9905.406383, 10143.86022, 10408.71955]
Pakistan_GDP_Per_Capita = [346.6685155,382.7514315,399.4655807,412.6753983,404.6068674,455.5079732,461.4002095,441.7549177,427.5063275,420.6826106,644.457157,610.1432316,599.7894108,673.382966,774.7853357,832.7511375,909.0324033,1012.182794,1087.514777,985.3493008,1011.59718,1161.044321,1236.892763,1259.668368,1303.18537,1421.835278,1468.822082,1567.640612,1620.742591,1437.165833,1322.314785]
Russia_GDP_Per_Capita = [3494.062988, 3490.452393, 3098.802734, 2930.670166, 2662.104004, 2665.779785, 2643.929199, 2737.572021, 1834.861816, 1330.757202, 1771.594116, 2100.352539, 2377.529541, 2975.123047, 4102.364746, 5323.455078, 6920.199707, 9101.239258, 11635.28418, 8562.824219, 10674.99023, 14311.06445, 15420.85938, 15974.62207, 14095.64648, 9313.021484, 8704.894531, 10720.33203, 11287.35449, 11536.25879, 10194.44141]

# Create a DataFrame
data = pd.DataFrame({
    'Year': years,
    'Australia_CO2': Australia_CO2,
    'China_CO2': China_CO2,
    'Pakistan_CO2': Pakistan_CO2,
    'Russia_CO2': Russia_CO2,
    'Australia_GDP_Per_Capita': Australia_GDP_Per_Capita,
    'China_GDP_Per_Capita': China_GDP_Per_Capita,
    'Pakistan_GDP_Per_Capita': Pakistan_GDP_Per_Capita,
    'Russia_GDP_Per_Capita': Russia_GDP_Per_Capita
})

# Normalize data for clustering
normalized_data = (data - data.mean()) / data.std()

# Apply k-means clustering on GDP per capita and CO2 per capita
kmeans = KMeans(n_clusters=3, random_state=42)
cluster_features = ['Australia_GDP_Per_Capita', 'China_GDP_Per_Capita', 'Pakistan_GDP_Per_Capita', 'Russia_GDP_Per_Capita',
                     'Australia_CO2', 'China_CO2', 'Pakistan_CO2', 'Russia_CO2']
data['Cluster'] = kmeans.fit_predict(normalized_data[cluster_features])

# Plotting
plt.figure(figsize=(12, 6))
for cluster in data['Cluster'].unique():
    cluster_data = data[data['Cluster'] == cluster]
    plt.scatter(cluster_data['Year'], cluster_data['Australia_CO2'], label=f'Cluster {cluster + 1}')

plt.xlabel('Year')
plt.ylabel('Australia CO2 Emissions')
plt.title('Clustering of Australia CO2 Emissions over Time')
plt.legend()
plt.show()

# Plotting
plt.figure(figsize=(12, 6))
for cluster in data['Cluster'].unique():
    cluster_data = data[data['Cluster'] == cluster]
    plt.scatter(cluster_data['Year'], cluster_data['China_GDP_Per_Capita'], label=f'Cluster {cluster + 1}')

plt.xlabel('Year')
plt.ylabel('China_GDP_Per_Capita')
plt.title('Clustering of China_GDP_Per_Capita over Time')
plt.legend()
plt.show()

# Curve fitting example using Australia GDP per capita
def linear_func(x, a, b):
    return a * x + b

ing the curve fit
plt.figure(figsize=(12, 6))
plt.scatter(data['Year'], data['Australia_GDP_Per_Capita'], label='Actual Data')
plt.plot(future_years, predicted_values, label='Best Fitting Function', color='orange')
plt.fill_between(future_years, lower_bound, upper_bound, color='orange', alpha=0.2, label='Confidence Range')
plt.xlabel('Year')
plt.ylabel('Australia GDP Per Capita')
plt.title('Curve Fit of Australia GDP Per Capita over Time')
plt.legend()
plt.show()
