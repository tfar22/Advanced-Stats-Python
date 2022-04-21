# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 16:26:10 2020

@author: thoma
"""
print('')
print('z-score calculation:')
import numpy as np

#below is the average mph of a curveball for 10 pitchers
data = [81.3, 84.6, 78.9, 78.0, 82.5, 86.5, 83.3, 82.4, 85.8, 65.6]

#I am looking at the last raw score in our set.
z = (data[9] - np.mean(data))/np.std(data)
print('The z-score is {:4.2f}'.format(z))
print('Looking at the confidence interval for 95%, the absolute value of the obtained value for z is greater than the critical value which is 1.96, which means the raw score we are looking at happened by chance and is significant.')
print('')
print('One-sample z-test calculation:')

#ERA stands for earned run average. It is the average number of earned runs pitcher's allow in 9 innings.
ERAdata = [5.59,5.56,4.33,4.51,4.91,5.04,4.84,4.44,5.22,4.43,4.14,4.22,4.77,4.32,4.66,5.13,5.54,5.2,5.2,5.29,5.26,6.01,4.99,5.25,5.59,4.97,5.15,5.41]
#Here is the average ERA for each year the Rockies have been in Existence
careerERA = np.mean(ERAdata)

#Here is the team ERA in 2020
ERA2020 = 5.59

#The sample size for the Rockies in 2020 (number of pitchers used)
n = 24

ztest = (ERA2020 - careerERA)/(np.std(ERAdata)/np.sqrt(n))
print('The z-test statistic is ', ztest)
print('Looking at the confidence interval for 95%, the obtained value for z is greater than the critical value which is 1.96, which means the raw score we are looking at happened to chance and is significant.')
print('')
print('Independent t-test calculation:')

#Our independent variable for this calculation will be team name.
#Our dependent variable will be H9, or hits that a pitcher gives up per nine innings.

#Here are the various H9 scores for the Colorado Rockies in 2020
COLH9 = [4.9,7.7,8,8.1,8.6,8.7,9.8,10.1,10.4,12.4,13.5,14]

#Here are the various H9 scores for the Chicago Cubs
CHIH9 = [8.1,7,7.7,9.4,5.1,10.6,3.9,7.4,5.4,9.3,9.2,10.9,5.9,9.6,5.9,9,7.7,3.6,5.4,6,16.9,21.6,9,9,0,27]

#sample sizes of each sample
n1 = len(COLH9)
n2 = len(CHIH9)

#standard deviations of each sample
s1 = np.std(COLH9)
s2 = np.std(CHIH9)

#means of each sample
X1 = np.mean(COLH9)
X2 = np.mean(CHIH9)

#finally, time to calculate t
t = (X1 - X2)/(np.sqrt((((n1 -1)*s1**2 + (n2 - 1)*s2**2)/(n1 + n2 - 2))*((n1 + n2)/(n1*n2))))
print('The t-test statistic is', t)
print('Our t-obtained is less than t-critical according to the t-distribution table. Therefore, p > alpha, meaning we cannot reject the null hypothesis and the difference between our two samples is insignificant.')
print('')

print('Repeated measures t-test calculation:')

#Our independent variable will be home/away games
#Our dependent variable will be batting average

#Here are the two samples of data for the same participants
AVGhome = [0.383,0.37,0.359,0.349,0.333,0.314,0.306,0.281,0.271,0.26,0.244,0.217,0.214,0.214,0.161,0.136,0.125]

AVGroad = [0.3,0.296,0.277,0.269,0.25,0.246,0.244,0.235,0.227,0.226,0.211,0.186,0.186,0.176,0.157,0.077,0.071]

#defining difference
D = []
diff = zip(AVGhome, AVGroad)
for AVGhome, AVGroad in diff:
    D.append(AVGhome - AVGroad)
#sample size
n = len(D)

#mean of the differences of raw scores
Dbar = np.mean(D)

#difference of squares
Ddiff = (D - Dbar)**2

#sum of difference of squares
Dss = sum(Ddiff)

#standard deviation
s = Dss/(n - 1)

t_repeated = Dbar/(s/np.sqrt(n))
print('The t-test statistic (repeated measure) is', t_repeated)
print('The t-test statistic is rather high and it is greater than the critical value for t. Therefore, the difference between our two conditions is signicant (which makes sense if you know that the Rockies" home is Coors Field).')
print('')

print('One way ANOVA calculation:')
#independent variable is club name (I am comparing the pitching staffs once again)
#dependent variable is the HR's allowed per nine innings in 2020
#Chicago Cubs numbers
chihr9 = [1.1,0.6,1.9,1.6,0.4,1,0.4,0.9,1.5,0.5,2.9,2.2,1.2,1.9,1.3,0.9,1.9,1.8,5.4,3,0,0,9,0,0,0]

#Colorado Rockies numbers
colhr9 = [0.7,1.1,1.1,2.5,1.4,1.4,0.7,0.7,2.3,0.8,1.8,1.3,3.9,3.2,1.5,3,5.1,4.2,6.2,0,0,3.4,0,0]

#Los Angeles Dodgers numbers
ladhr9 = [1.2,1.4,0.8,0.4,1.7,3.2,0.7,0.4,0.4,0.4,0.9,0,0.5,1.9,1.1,2.1,1.4,1.5,0,2.1,0]

#Calculating the grand mean
G = (np.mean(ladhr9) + np.mean(chihr9) + np.mean(colhr9))/3

#calculating total sample size
N = len(ladhr9) + len(chihr9) + len(colhr9)

#number of levels (k)
k = 3

#the means for each team (group)
xlad = np.mean(ladhr9)
xchi = np.mean(chihr9)
xcol = np.mean(colhr9)

#here are the sample sizes for each team
nlad = len(ladhr9)
nchi = len(chihr9)
ncol = len(colhr9)

#some of squared deviations for between groups
SSbt = nlad*(xlad - G)**2 + nchi*(xchi - G)**2 + ncol*(xcol - G)**2
print('SS b/w =', SSbt)

#some of sqaured deviations within
chi_sum = sum((chihr9 - xchi)**2)
lad_sum = sum((ladhr9 - xlad)**2)
col_sum = sum((colhr9 - xcol)**2)

SSwi = chi_sum + lad_sum + col_sum
print('SS w/i =', SSwi)

#some of squares total
print('Total SS =', SSbt + SSwi)

#between groups degrees of freedom
DFbt = k - 1
DFwi = N - k
print('DF b/w =', DFbt)
print('DF w/i =', DFwi)
print('Total DF =', DFbt + DFwi)

#calculating means squared for both between and within groups
MSbt = SSbt/DFbt
MSwi = SSwi/DFwi
print('MS b/w =', MSbt)
print('MS w/i =', MSwi)

#calculating F
F = MSbt/MSwi
print('F =', F)
print('Our critical value for F is 3.132, according to the F-distribution table. Our obtained value for F is less than our critical, meaning there is no significant difference among the groups. This means we cannot reject our null hypothesis and that pitching staffs all around the league give up the same number of HRs each game.')
print('')
print('One-way repeated measures ANOVA:')
#One-way repeated measures ANOVA
#here are the raw scores (AB/HR) for 5 different players from AA, AAA, and MLB
AA = [11, 12.4, 9, 13.4, 10.9]
AAA = [13.8, 15.3, 17.3, 12.2, 16]
MLB = [14, 11, 15, 16.3, 20.4]

#here are the means for each level for the 5 players
xAA = np.mean(AA)
xAAA = np.mean(AAA)
xMLB = np.mean(MLB)

#here is the grand mean and the total sample size
G = (xAA + xAAA + xMLB)/3
N = (len(AA) + len(AAA) + len(MLB))
k = 3   #number of levels

#sample size of the group
n = len(MLB)

#SS between calculation
SSbt = n*(xAA - G)**2 + n*(xAAA - G)**2 + n*(xMLB - G)**2
print('SS b/w =', SSbt)

#some of sqaured deviations within
AA_sum = sum((AA - xAA)**2)
AAA_sum = sum((AAA - xAAA)**2)
MLB_sum = sum((MLB - xMLB)**2)

SSwi = AA_sum + AAA_sum + MLB_sum
print('SS w/i =', SSwi)

#some of squares total
print('Total SS =', SSbt + SSwi)

#between groups degrees of freedom
DFbt = k - 1
DFwi = N - k
print('DF b/w =', DFbt)
print('DF w/i =', DFwi)
print('Total DF =', DFbt + DFwi)

#calculating means squared for both between and within groups
MSbt = SSbt/DFbt
MSwi = SSwi/DFwi
print('MS b/w =', MSbt)
print('MS w/i =', MSwi)

#calculating F
F = MSbt/MSwi
print('F =', F)
print('Our critical value is 3.885 according to our F-distribution table. Our obtained value is greater than than critical for an alpha = 0.05, meaning there is a significant difference among the different levels of one group of the same participants.')
print('')

print('Pearson Correlation Calculation:')
#The independent variable will be spin rate on a curveball
#The dependent variable will be average Whiff%

sr = [2325, 2425, 2578, 2619, 2739, 2856, 2951, 3018, 3109, 3219]
whiff = [0.34, 0.38, 0.41, 0.46, 0.49, 0.52, 0.54, 0.58, 0.59, 0.59]

#sample size
N = len(sr)

#degrees of freedom
df = N - 1

#means
srx = np.mean(sr)
whiffy = np.mean(whiff)

#covariance
cov = sum((sr - srx)*(whiff - whiffy))/df

#standard deviations
sr_sd = np.sqrt(sum(((sr - srx)**2)/df))
whiff_sd = np.sqrt(sum(((whiff - whiffy)**2)/df))

#Pearson coefficient
r = cov/(sr_sd * whiff_sd)
print('r =', r)
print('r^2 =', r**2)
print('1 - r^2 =', 1 - r**2)
print('Since r is in between 0.7 and 1.0, then there is a strong correlation between spin rate and whiff %. The coefficient of determination (r^2) tells us more directly that there is a strong correlation. The coefficient of nondetermination (1 - r^2) tells us the percentage of variance in whiff% not explained by spin rate.')
print('')

print('Chi-squared Goodness of Fit Calculation:')
#Chi-squared goodness of fit
#our contingency will be handedness of pitchers
#observed frequencies
rhp = 124   #right handed pitchers
lhp = 50    #left handed pitchers
ap = 1      #ambidexterous pitchers

#calculating expected frequencies
N = rhp + lhp + ap   #sample size
E = N/3     #expected frequencies for 3 different nominal variables

#calculation of chi-squared
X2 = ((rhp - E)**2 + (lhp - E)**2 + (ap - E)**2)/E
print('X2 =', X2)
print('Since X2 is pretty high, the frequencies are very different from each other and differ from the hypothetical population.')
print('')

print('Chi-squared Test of Independence Calculation:')

#the contingencies will be preference of pitcher to face (Jacob DeGrom or Max Scherzer)
#the independent variables will be batter handedness (L or R)
#frequency of those who like to face Degrom:
L_deg = 15
R_deg = 15

#frequency of those who like to face Scherzer:
L_shrz = 35
R_shrz = 35

#column 1 will be degrom, column 2 will be scherzer
#row 1 will be left handers, row 2 will be left handers
#totals
row1 = L_deg + L_shrz
row2 = R_deg + R_shrz
col1 = L_deg + R_deg
col2 = L_shrz + R_shrz

#grand total
G = L_deg + R_deg + L_shrz + R_shrz

#calculating expected frequencies (first number is row #, second number is col #)
E11 = row1*col1/G
E12 = row1*col2/G
E21 = row2*col1/G
E22 = row2*col2/G

#R is number of rows, C is number of columns
R = 2
C = 2

#calculating degrees of freedom
df = (R - 1)*(C - 1)

#calculating chi-squared
X2 = ((L_deg - E11)**2)/E11 + ((L_shrz - E12)**2)/E12 + ((R_deg - E21)**2)/E21 + ((R_shrz - E22)**2)/E22
print('X2 =', X2)
print('X2 = 0, meaning there is no difference in the preference of facing Jacob Degrom and Max Scherzer. 0 is less than our critical value at 1 degree of freedom, meaning p > alpha, meaning we cannot reject our null hypothesis.')
print('')
print('Hope you enjoyed my stats packet!')




