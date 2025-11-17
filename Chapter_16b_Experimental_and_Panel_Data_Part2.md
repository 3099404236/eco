ercise is that they run far too many different specifications “just to 
see” what the results look like. In our opinion, all but one or two of 
the specification decisions involved in this exercise should be made 
before the first regression is estimated, so one measure of the qual-
ity of your work is the number of different equations you estimated. 
Typically, the fewer the better.
	
  As to which specification to run, most of the decisions involved 
are matters of personal choice and experience. Our favorite model 
on theoretical grounds is:
	
+	
-	
-	
+	
+	
+
Pi =  β0 +  β1Si +  β2Ni +  β3Ai +  β4A2
i  +  β5Yi +  β6CAi +  ei
	
We think that BE and BA are redundant with S. In addition, we can 
justify both positive and negative coefficients for SP, giving it an 
ambiguous expected sign, so we’d avoid including it. We would not 
quibble with someone who preferred a linear functional form for 
A to our quadratic. In addition, we recognize that CA is quite insig-
nificant for this sample, but we’d retain it, at least in part because it 
gets quite hot in Monrovia in the summer.


511
ANSWERS
	
  As to interactive variables, the only one we can justify is between 
S and N. Note, however, that the proper variable is not S # N but 
instead is S # (5 - N), or something similar, to account for the differ-
ent expected signs. This variable turns out to improve the fit while 
being quite collinear (redundant) with N and S.
	
  In none of our specifications did we find evidence of serial cor-
relation or heteroskedasticity, although the latter is certainly a pos-
sibility in such cross-sectional data.
Chapter 12
12–2.	
a.	The double-log functional form doesn’t change the fact that this 
is a dynamic model. As a result, Y and M almost surely are related 
by a distributed lag.
	
b.	In their relationship to M, both Y and R have the same distrib-
uted lag pattern over time, since the λn  of 0.60 applies to both. 
(The equation is in double-log form, so technically the relation-
ships are between the logs of those variables.)
	
c.	 Serial correlation is always a concern in a dynamic model. Many 
students will look at the Durbin–Watson statistic of 1.80 and 
conclude that there is no evidence of positive serial correlation 
in this equation, but that statistic is biased toward 2 in the pres-
ence of a lagged dependent variable. Ideally, we would use the 
Lagrange Multiplier Serial Correlation Test, but we don’t have 
the data to do so. Durbin’s h test, which is beyond the scope of 
this text, provides evidence that there is indeed serial correlation 
in the equation. For more, see Robert Raynor, “Testing for Serial 
Correlation in the Presence of Lagged Dependent Variables,” The 
Review of Economics and Statistics, Vol. 75, No. 4, pp. 716–721.
12–4.	
LM = NR2 = 24*0.0056 = 0.134 6 3.84 = 5-percent critical chi-
square value with one degree of freedom, so we cannot reject the 
null hypothesis of no serial correlation.
Chapter 13
13–2.	
a.	WN: The log of the odds that a woman has used a recognized form 
of birth control is 2.03 higher if she doesn’t want any more chil-
dren than it is if she wants more children, holding ME constant.


512
aPPENDIX A
	
	
ME: A one-unit increase in the number of methods of birth con-
trol known to a woman increases the log of the odds that she has 
used a form of birth control by 1.45, holding WN constant.
	
	
LPM: If the model were a linear probability model, then each 
individual slope coefficient would represent the impact of a one-
unit increase in the independent variable on the probability that 
the ith woman had ever used a recognized form of birth control, 
holding the other independent variable constant.
	
b.	Yes, but we didn’t expect βn ME to be more significant than βn WN.
	
c.	 As we’ve said before, β0 has virtually no theoretical significance. 
See Section 7.1.
	
d.	We’d add one of a number of potentially relevant variables; for 
instance, the educational level of the ith woman, whether the ith 
woman lives in a rural area, and so on.
13–4.	
a.	There are only two women in the sample who are over 65, and 
both of them are out of the workforce. Because this causes a near 
singular matrix, most Logit programs, including Stata’s, will not 
be able to estimate this equation.
	
b.	In both models, the coefficient of A is insignificantly different 
from zero, R  2
P falls when A is added, and the other coefficients 
don’t change by a standard error when A is added. As a result, 
you’d include A in the equation only if you believe it clearly 
belongs there on the basis of theory.
	
a.	 Dn i = - 0.22 - 0.38Mi - 0.001Ai + 0.09Si
	
	
	
10.162	
10.0072	 10.042
	
	
	
t = -2.43	
-0.14	
2.42
	
	
	
R  2 = .29	
N = 30	
R  2
p = .806
	
b.	ln3Di/11 - Di24 = -5.27 - 2.61Mi - 0.01Ai + 0.67Si
	
	
	
11.202	
10.042	 10.322
	
	
	
-2.17	
-0.25	
2.10
	
	
	
R  2
p = .76
Chapter 14
14–2.	
a.	If e2 decreases, Y2 decreases and then Y1 decreases.
	
b.	If eD increases, QD increases, and then QS increases (equilibrium 
condition) and Pt increases. (Remember that the variables are 
simultaneously determined, so it doesn’t matter which one is on 
the left-hand side.)
∏


513
Answers
	
c.	 If e1 increases, CO increases, and then Y increases and YD 
increases.
14–4.	
a.	There are three predetermined variables in the system, and both 
equations have three slope coefficients, so both equations are 
exactly identified. (If the model specified that the price of beef 
was determined jointly with the price and quantity of chicken, 
then it would not be predetermined, and the equations would be 
­underidentified.)
	
b.	There are two predetermined variables in the system, and both 
equations have two slope coefficients, so both equations are 
exactly identified.
	
c.	 There are seven predetermined variables in the system, and there 
are three slope coefficients in both equations, so the first two 
equations are overidentified. Note that we don’t worry about the 
identification properties of the third equation because it isn’t 
part of the simultaneous system.
	
d.	There are five predetermined variables in the system, and there 
are three, two, and four slope coefficients in the first, second, 
and third equations, respectively, so all three equations are 
overidentified.
14–6.	
a.	OLS estimation will still encounter simultaneity bias because 
price and quantity are simultaneously determined. Not all en-
dogenous variables will appear on the left-hand side of a struc-
tural equation.
	
b.	The direction of the bias depends on the correlation between the 
error term and the right-hand-side endogenous variable. If the 
correlation between the error term and price is positive, as it most 
likely is, then the simultaneity bias will also be positive.
	
c.	 Three: stage one: P as a function of YD and W
	
	
stage two: QD as a function of Pn and YD: QS as a function of Pn and W
	
d.	OLS:  Qn D = 57.3 - 0.86P + 1.03YD
	
	
	
 Qn S = 167.5 + 3.95P - 1.42W
	
	
2SLS: Qn D = 95.1 - 6.11Pn + 2.71YD
	
	
	
Qn S = 480.2 + 13.5Pn - 5.50W
Chapter 15
15–2.	
a.	$310,120.00
	
b.	117,276; 132,863; 107,287; Nowheresville


514
APPENDIX A
15–4.	
a.	P isn’t a dummy variable. Instead, it’s a variable whose main function 
is to be multiplied by other variables so that the sign of the resulting 
interaction variable changes depending on the incumbent’s party.
	
b.	The interaction variables were required because the dependent 
variable measures the percentage of votes won by the Democrats, 
but the independent variables measure items that support (or 
damage) public support for the incumbent party. For example, if a 
Democrat is in office in a time of high growth, that growth should 
increase the share of votes won by Democrats, so a positive sign 
makes sense. However, if a Republican is in office in a time of high 
growth, the growth should decrease the share of votes won by the 
Democrats, so a negative sign makes sense. Multiplying GROWTH 
by +1 if the incumbent is a Democrat and -1 if the incumbent is 
a Republican (by using P) is a way of accomplishing this goal.
	
c.	
VOTE = 48.70 + 8.183P - 1.845DUR*P + 0.087DOW*P + 0.535GROWTH*P
	
	
	
12.3962	 10.8432	
10.0702	
10.1972
	
t = 	 	
3.42	
-2.19	
1.25	
2.71
	
-0.762INFLATION*P + 0.040ARMY*P - 0.078SPEND*P
	
10.3632	
10.0342	
10.0362
	
-2.10	
1.15	
-2.18
	
N = 21  R  2 = .77  DW = 2.20
	
d.	The coefficient of DUR*P is negative, while the coefficient of 
ARMY*P is positive, both opposite of their expected signs. The 
coefficients of the other interactive terms have the expected signs. 
We can reject the null hypotheses for P (assuming a positive 
expected sign), GROWTH*P, INFLATION*P, and SPEND*P. We 
cannot reject for DUR*P, DOW*P, and ARMY*P.
	
e.	 Plugging the actual values for 2000 into the equation, we get a 
forecast of 52.740, which is 2.475 percentage points higher than 
the actual 50.265. For 2004, we get a forecast of 44.280, which is 
4.306 percentage points below the actual 48.586.
	
f.	 To do this, we should estimate Equation 15.20 with data through 
2004, producing:
VOTE = 48.76 + 7.340P - 1.659DUR*P + 0.116DOW*P + 0.496GROWTH*P
	
12.2082	
10.8122	
10.0642	
10.1892
	
t = 	 3.32	
-2.04	
1.80	
2.63
	
-0.727INFLATION*P + 0.039ARMY*P - 0.081SPEND*P
	
10.3422	
10.0342	
10.0342
	
-2.13	
1.14	
-2.36
	
	
	 N = 23	
R  2 = .75	
DW = 2.23
h
h


515
Answers
	
	
Plugging the actual values for 2008 into this equation, we get 
a forecast of 42.892, surprisingly below the share that Barack 
Obama actually earned.
Chapter 16
16–2.	
a.	 ∆OUTCOMEEaston = 28,500 - 25,000 = 3,500
	
	
∆OUTCOMEAllentown = 23,750 - 22,500 = 1,250
	
b.	We must assume that the changes in the outcome would have 
been the same in both the treatment and control group (had 
there been no treatment) in order for this estimation to be valid. 
However, there was a $2,500 disparity between the average 
incomes prior to the treatment, so there most likely are several 
differences between the two groups.
	
c.	 Even if the underlying assumption in part b is met, we should be 
cautious when interpreting our conclusions. A data set with only 
two observations is absurdly small and is unlikely to provide 
accurate results except by chance.
16–4.	
a.	This is a natural experiment dataset that also happens to be a 
panel dataset because it contains observations on the same vari-
able from the same cross-sectional sample from two different 
time periods.
	
b.	The appropriate technique is the difference-in-differences estima-
tor, resulting in:
	
	
∆SMOKE = -2.43 - 0.73TAX
	
	
	
10.572
	
	
	
t = 	
-1.29
	
	
	
N = 45	
R  2 = .015
	
c.	 The estimated coefficient is almost significant in the expected 
direction, but the fit is terrible. Most experienced researchers 
won’t be surprised by this result, because of the design of the 
research. In particular, it seems extremely optimistic to expect 
to explain cigarette consumption by state using a dummy for 
whether the cigarette tax rate increased as the only independent 
variable. Variables other than tax rates certainly play a role, as 
does the fact that some states increased cigarette taxes by substan-
tially more than did others, and yet that information is lost if you 
limit yourself to a dummy variable, since it tells you only whether 
taxes increased, not the amount by which they increased.
®


516
aPPENDIX A
16–6.	
a.	 ∆Q = 0.039 - 0.025∆P
	
	
	
(0.002)
	
	
	
t = 	
-12.33
	
	
	 N = 4	
R 2 = .98
	
b.	Fixed effects and differencing produce identical results for the 
coefficient and standard error on the price variable. The fixed 
effect approach, however, produces estimates for coefficients 
on time and entity dummy variables. The adjusted R-squared 
will also differ. But since the variables of interest should be the 
same in the differencing and fixed effect approaches, the identi-
cal results for the price variable produced by the two methods is 
reassuring. They produce identical answers.
	
c.	 The error term in the differencing model certainly appears to be 
defined in such a way as to be serially correlated.
8


517
Statistical Tables
Appendix B
The following tables present the critical values of various statistics used pri-
marily for hypothesis testing. The primary applications of each statistic are 
explained and illustrated. The tables are:
B-1	
Critical Values of the t-Distribution
B-2	
Critical Values of the F-Statistic: 5-Percent Level of Significance
B-3	
Critical Values of the F-Statistic: 1-Percent Level of Significance
B-4	
Critical Values of the Durbin–Watson Test Statistics dL and dU
B-5	
The Normal Distribution
B-6	
The Chi-Square Distribution


518
aPPENDIX B
Table B-1: The t-Distribution
The t-distribution is used in regression analysis to test whether an estimated 
slope coefficient (say, βn k) is significantly different from a hypothesized value 
(such as βH0). The t-statistic is computed as:
tk = 1βn k - βH02/SE1βn k2
where βn k is the estimated slope coefficient and SE1βn k2 is the estimated stan-
dard error of βn k. To test the one-sided hypothesis:
 H0: βk … βH0
 HA: βk 7 βH0
the computed t-value is compared with a critical t-value tc, found in the t-table 
on the opposite page in the column with the desired level of significance 
for a one-sided test (usually 5 percent) and the row with N - K - 1 degrees 
of freedom, where N is the number of observations and K is the number of 
explanatory variables. If 0 tk0 7 tc and if tk has the sign implied by the alterna-
tive hypothesis, then reject H0; otherwise, do not reject H0. In most econo-
metric applications, βH0 is zero and most computer regression programs will 
calculate tk for βH0 = 0. For example, for a 5-percent one-sided test with 15 
degrees of freedom, tc = 1.753, so any positive tk larger than 1.753 would 
lead us to reject H0 and declare that βn k is statistically significant in the hy-
pothesized direction at the 5-percent level.
For a two-sided test, H0: βk = βH0 and HA: βk ≠βH0, the procedure is 
identical except that the column corresponding to the two-sided level of sig-
nificance is used. For example, for a 5-percent two-sided test with 15 degrees 
of freedom, tc = 2.131, so any tk larger in absolute value than 2.131 would 
lead us to reject H0 and declare that βn k is significantly different from βH0 at 
the 5-percent level of significance. For more on the t-test, see Chapter 5.


519
Statistical Tables
Table B-1  Critical Values of the t-Distribution
Level of Significance
Degrees of 
Freedom
One-Sided: 10% 
Two-Sided: 20%
5% 
10%
2.5% 
5%
1% 
2%
0.5% 
1%
  1
3.078
6.314
12.706
31.821
63.657
  2
1.886
2.920
4.303
6.965
9.925
  3
1.638
2.353
3.182
4.541
5.841
  4
1.533
2.132
2.776
3.747
4.604
  5
1.476
2.015
2.571
3.365
4.032
  6
1.440
1.943
2.447
3.143
3.707
  7
1.415
1.895
2.365
2.998
3.499
  8
1.397
1.860
2.306
2.896
3.355
  9
1.383
1.833
2.262
2.821
3.250
10
1.372
1.812
2.228
2.764
3.169
11
1.363
1.796
2.201
2.718
3.106
12
1.356
1.782
2.179
2.681
3.055
13
1.350
1.771
2.160
2.650
3.012
14
1.345
1.761
2.145
2.624
2.977
15
1.341
1.753
2.131
2.602
2.947
16
1.337
1.746
2.120
2.583
2.921
17
1.333
1.740
2.110
2.567
2.898
18
1.330
1.734
2.101
2.552
2.878
19
1.328
1.729
2.093
2.539
2.861
20
1.325
1.725
2.086
2.528
2.845
21
1.323
1.721
2.080
2.518
2.831
22
1.321
1.717
2.074
2.508
2.819
23
1.319
1.714
2.069
2.500
2.807
24
1.318
1.711
2.064
2.492
2.797
25
1.316
1.708
2.060
2.485
2.787
26
1.315
1.706
2.056
2.479
2.779
27
1.314
1.703
2.052
2.473
2.771
28
1.313
1.701
2.048
2.467
2.763
29
1.311
1.699
2.045
2.462
2.756
30
1.310
1.697
2.042
2.457
2.750
40
1.303
1.684
2.021
2.423
2.704
60
1.296
1.671
2.000
2.390
2.660
120
1.289
1.658
1.980
2.358
2.617
(Normal)
∞
1.282
1.645
1.960
2.326
2.576
Source: Reprinted from Table IV in Sir Ronald A. Fisher, Statistical Methods for Research 
Workers, 14th ed. (copyright © 1970, University of Adelaide) with permission of Hafner, a  
division of the Macmillan Publishing Company, Inc.


520
aPPENDIX B
Table B-2: The F-Distribution
The F-distribution is used in regression analysis to deal with a null hypoth-
esis that contains multiple hypotheses or a single hypothesis about a group 
of coefficients. To test the most typical joint hypothesis (a test of the overall 
significance of the regression):
 H0: β1 = β2 = g
  = βK = 0
 HA: H0 is not true
the computed F-value is compared with a critical F-value, found in one of 
the two tables that follow. The F-statistic has two types of degrees of free-
dom, one for the numerator (columns) and one for the denominator (rows). 
For the null and alternative hypotheses above, there are K numerator (the 
number of restrictions implied by the null hypothesis) and N - K - 1 de-
nominator degrees of freedom, where N is the number of observations and 
K is the number of explanatory variables in the equation. This particular F-
statistic is printed out by most computer regression programs. For example, 
if K = 5 and N = 30, there are 5 numerator and 24 denominator degrees 
of freedom, and the critical F-value for a 5-percent level of significance 
(Table B-2) is 2.62. A computed F-value greater than 2.62 would lead us to 
reject the null hypothesis and declare that the equation is statistically signifi-
cant at the 5-percent level. For more on the F-test, see Section 5.6.


521
Statistical Tables
Table B-2  Critical Values of the F-Statistic: 5-Percent Level of Significance
v1 = Degrees of Freedom for Numerator
1
2
3
4
5
6
7
8
10
12
20
H
  1
161
200
216
225
230
234
237
239
242
244
248
254
  2
18.5 19.0 19.2 19.2 19.3 19.3 19.4 19.4 19.4 19.4 19.4 19.5
  3
10.1 9.55 9.28 9.12 9.01 8.94 8.89 8.85 8.79 8.74 8.66 8.53
  4
7.71 6.94 6.59 6.39 6.26 6.16 6.09 6.04 5.96 5.91 5.80 5.63
  5
6.61 5.79 5.41 5.19 5.05 4.95 4.88 4.82 4.74 4.68 4.56 4.36
  6
5.99 5.14 4.76 4.53 4.39 4.28 4.21 4.15 4.06 4.00 3.87 3.67
  7
5.59 4.74 4.35 4.12 3.97 3.87 3.79 3.73 3.64 3.57 3.44 3.23
  8
5.32 4.46 4.07 3.84 3.69 3.58 3.50 3.44 3.35 3.28 3.15 2.93
  9
5.12 4.26 3.86 3.63 3.48 3.37 3.29 3.23 3.14 3.07 2.94 2.71
10
4.96 4.10 3.71 3.48 3.33 3.22 3.14 3.07 2.98 2.91 2.77 2.54
11
4.84 3.98 3.59 3.36 3.20 3.09 3.01 2.95 2.85 2.79 2.65 2.40
12
4.75 3.89 3.49 3.26 3.11 3.00 2.91 2.85 2.75 2.69 2.54 2.30
13
4.67 3.81 3.41 3.18 3.03 2.92 2.83 2.77 2.67 2.60 2.46 2.21
14
4.60 3.74 3.34 3.11 2.96 2.85 2.76 2.70 2.60 2.53 2.39 2.13
15
4.54 3.68 3.29 3.06 2.90 2.79 2.71 2.64 2.54 2.48 2.33 2.07
16
4.49 3.63 3.24 3.01 2.85 2.74 2.66 2.59 2.49 2.42 2.28 2.01
17
4.45 3.59 3.20 2.96 2.81 2.70 2.61 2.55 2.45 2.38 2.23 1.96
18
4.41 3.55 3.16 2.93 2.77 2.66 2.58 2.51 2.41 2.34 2.19 1.92
19
4.38 3.52 3.13 2.90 2.74 2.63 2.54 2.48 2.38 2.31 2.16 1.88
20
4.35 3.49 3.10 2.87 2.71 2.60 2.51 2.45 2.35 2.28 2.12 1.84
21
4.32 3.47 3.07 2.84 2.68 2.57 2.49 2.42 2.32 2.25 2.10 1.81
22
4.30 3.44 3.05 2.82 2.66 2.55 2.46 2.40 2.30 2.23 2.07 1.78
23
4.28 3.42 3.03 2.80 2.64 2.53 2.44 2.37 2.27 2.20 2.05 1.76
24
4.26 3.40 3.01 2.78 2.62 2.51 2.42 2.36 2.25 2.18 2.03 1.73
25
4.24 3.39 2.99 2.76 2.60 2.49 2.40 2.34 2.24 2.16 2.01 1.71
30
4.17 3.32 2.92 2.69 2.53 2.42 2.33 2.27 2.16 2.09 1.93 1.62
40
4.08 3.23 2.84 2.61 2.45 2.34 2.25 2.18 2.08 2.00 1.84 1.51
60
4.00 3.15 2.76 2.53 2.37 2.25 2.17 2.10 1.99 1.92 1.75 1.39
120
3.92 3.07 2.68 2.45 2.29 2.18 2.09 2.02 1.91 1.83 1.66 1.25
∞
3.84 3.00 2.60 2.37 2.21 2.10 2.01 1.94 1.83 1.75 1.57 1.00
Source: Abridged from M. Merrington and C. M. Thompson, “Tables of percentage points 
of the inverted beta (F) distribution,” Biometrika, Vol. 33, 1943, p. 73, by permission of the 
Biometrika trustees.
v2 =  Degrees of Freedom for Denominator


522
aPPENDIX B
Table B-3: The F-Distribution
The F-distribution is used in regression analysis to deal with a null hypoth-
esis that contains multiple hypotheses or a single hypothesis about a group 
of coefficients. To test the most typical joint hypothesis (a test of the overall 
significance of the regression):
 H0: β1 = β2 = g
   = βK = 0
 HA: H0 is not true
the computed F-value is compared with a critical F-value, found in Tables B-2 
and B-3. The F-statistic has two types of degrees of freedom, one for the 
­numerator (columns) and one for the denominator (rows). For the null and 
alternative hypotheses above, there are K numerator (the number of restric-
tions implied by the null hypothesis) and N - K - 1 denominator degrees 
of freedom, where N is the number of observations and K is the number of 
explanatory variables in the equation. This particular F-statistic is printed out 
by most computer regression programs. For example, if K = 5 and N = 30, 
there are 5 numerator and 24 denominator degrees of freedom, and the criti-
cal F-value for a 1-percent level of significance (Table B-3) is 3.90. A com-
puted F-value greater than 3.90 would lead us to reject the null hypothesis 
and declare that the equation is statistically significant at the 1-percent level. 
For more on the F-test, see Section 5.6.


523
Statistical Tables
Table B-3  Critical Values of the F-Statistic: 1-Percent Level of Significance
v1 = Degrees of Freedom for Numerator
1
2
3
4
5
6
7
8
10
12
20
H
1 4052 5000 5403 5625 5764 5859 5928 5982 6056 6106 6209 6366
2
98.5 99.0 99.2 99.2 99.3 99.3 99.4 99.4 99.4 99.4 99.4 99.5
3
34.1 30.8 29.5 28.7 28.2 27.9 27.7 27.5 27.2 27.1 26.7 26.1
4
21.2 18.0 16.7 16.0 15.5 15.2 15.0 14.8 14.5 14.4 14.0 13.5
5
16.3 13.3 12.1 11.4 11.0 10.7 10.5 10.3 10.1 9.89 9.55 9.02
6
13.7 10.9 9.78 9.15 8.75 8.47 8.26 8.10 7.87 7.72 7.40 6.88
7
12.2 9.55 8.45 7.85 7.46 7.19 6.99 6.84 6.62 6.47 6.16 5.65
8
11.3 8.65 7.59 7.01 6.63 6.37 6.18 6.03 5.81 5.67 5.36 4.86
9
10.6 8.02 6.99 6.42 6.06 5.80 5.61 5.47 5.26 5.11 4.81 4.31
10
10.0 7.56 6.55 5.99 5.64 5.39 5.20 5.06 4.85 4.71 4.41 3.91
11
9.65 7.21 6.22 5.67 5.32 5.07 4.89 4.74 4.54 4.40 4.10 3.60
12
9.33 6.93 5.95 5.41 5.06 4.82 4.64 4.50 4.30 4.16 3.86 3.36
13
9.07 6.70 5.74 5.21 4.86 4.62 4.44 4.30 4.10 3.96 3.66 3.17
14
8.86 6.51 5.56 5.04 4.70 4.46 4.28 4.14 3.94 3.80 3.51 3.00
15
8.68 6.36 5.42 4.89 4.56 4.32 4.14 4.00 3.80 3.67 3.37 2.87
16
8.53 6.23 5.29 4.77 4.44 4.20 4.03 3.89 3.69 3.55 3.26 2.75
17
8.40 6.11 5.19 4.67 4.34 4.10 3.93 3.79 3.59 3.46 3.16 2.65
18
8.29 6.01 5.09 4.58 4.25 4.01 3.84 3.71 3.51 3.37 3.08 2.57
19
8.19 5.93 5.01 4.50 4.17 3.94 3.77 3.63 3.43 3.30 3.00 2.49
20
8.10 5.85 4.94 4.43 4.10 3.87 3.70 3.56 3.37 3.23 2.94 2.42
21
8.02 5.78 4.87 4.37 4.04 3.81 3.64 3.51 3.31 3.17 2.88 2.36
22
7.95 5.72 4.82 4.31 3.99 3.76 3.59 3.45 3.26 3.12 2.83 2.31
23
7.88 5.66 4.76 4.26 3.94 3.71 3.54 3.41 3.21 3.07 2.78 2.26
24
7.82 5.61 4.72 4.22 3.90 3.67 3.50 3.36 3.17 3.03 2.74 2.21
25
7.77 5.57 4.68 4.18 3.86 3.63 3.46 3.32 3.13 2.99 2.70 2.17
30
7.56 5.39 4.51 4.02 3.70 3.47 3.30 3.17 2.98 2.84 2.55 2.01
40
7.31 5.18 4.31 3.83 3.51 3.29 3.12 2.99 2.80 2.66 2.37 1.80
60
7.08 4.98 4.13 3.65 3.34 3.12 2.95 2.82 2.63 2.50 2.20 1.60
120
6.85 4.79 3.95 3.48 3.17 2.96 2.79 2.66 2.47 2.34 2.03 1.38
∞
6.63 4.61 3.78 3.32 3.02 2.80 2.64 2.51 2.32 2.18 1.88 1.00
Source: Abridged from M. Merrington and C. M. Thompson, “Tables of percentage points 
of the inverted beta (F ) distribution,” Biometrika, Vol. 3, 1943, p. 73, by permission of the 
Biometrika trustees.
v2 = Degrees of Freedom for Denominator


524
aPPENDIX B
Table B-4: The Durbin–Watson Statistic
The Durbin–Watson statistic is used to test for first-order serial correla-
tion in the residuals. First-order serial correlation is characterized by 
et = ρet-1 + ut, where et is the error term found in the regression equation 
and ut is a classical (not serially correlated) error term. Since ρ = 0 im-
plies no serial ­correlation, and since most economic and business models 
imply positive serial correlation if any pure serial correlation exists, the 
typical hypotheses are:
 H0: ρ … 0
 HA: ρ 7 0
To test the null hypothesis of no positive serial correlation, the Durbin–­
Watson statistic must be compared to two different critical d-values, dL and 
dU found in Table B-4, depending on the level of significance, the number of 
explanatory variables (K) and the number of observations (N). For example, 
with 2 explanatory variables and 30 observations, the 5-percent one-tailed crit-
ical values are dL = 1.28 and dU = 1.57, so any computed Durbin–­Watson 
statistic less than 1.28 would lead to the rejection of the null hypothesis. 
For computed DW d-values between 1.28 and 1.57, the test is inconclusive, 
and for values greater than 1.57, we can say that there is no evidence of posi-
tive serial correlation at the 5-percent level. These ranges are illustrated in the 
following diagram:
0
2
4
dL
1.28  
dU
  1.57
Reject H0
Test
Inconclusive
1-Percent One-Sided Test of H0 :  t … 0 vs. HA : t 7 0
Do Not Reject H0
Two-sided tests are done similarly, with 4 - dU and 4 - dL being the 
­critical DW d-values between 2 and 4.


525
Statistical Tables
Table B-4  Critical Values of the Durbin–Watson Test Statistics dL and dU: 
5-Percent One-Sided Level of Significance  
(10-Percent Two-Sided Level of Significance)
N
K = 1
K = 2
K = 3
K = 4
K = 5
K = 6
K = 7
dL
dU
dL
dU
dL
dU
dL
dU
dL
dU
dL
dU
dL
dU
15 1.08 1.36 0.95 1.54 0.81 1.75 0.69 1.97 0.56 2.21 0.45 2.47 0.34 2.73
16 1.11 1.37 0.98 1.54 0.86 1.73 0.73 1.93 0.62 2.15 0.50 2.39 0.40 2.62
17 1.13 1.38 1.02 1.54 0.90 1.71 0.78 1.90 0.66 2.10 0.55 2.32 0.45 2.54
18 1.16 1.39 1.05 1.53 0.93 1.69 0.82 1.87 0.71 2.06 0.60 2.26 0.50 2.46
19 1.18 1.40 1.07 1.53 0.97 1.68 0.86 1.85 0.75 2.02 0.65 2.21 0.55 2.40
20 1.20 1.41 1.10 1.54 1.00 1.68 0.89 1.83 0.79 1.99 0.69 2.16 0.60 2.34
21 1.22 1.42 1.13 1.54 1.03 1.67 0.93 1.81 0.83 1.96 0.73 2.12 0.64 2.29
22 1.24 1.43 1.15 1.54 1.05 1.66 0.96 1.80 0.86 1.94 0.77 2.09 0.68 2.25
23 1.26 1.44 1.17 1.54 1.08 1.66 0.99 1.79 0.90 1.92 0.80 2.06 0.72 2.21
24 1.27 1.45 1.19 1.55 1.10 1.66 1.01 1.78 0.93 1.90 0.84 2.04 0.75 2.17
25 1.29 1.45 1.21 1.55 1.12 1.66 1.04 1.77 0.95 1.89 0.87 2.01 0.78 2.14
26 1.30 1.46 1.22 1.55 1.14 1.65 1.06 1.76 0.98 1.88 0.90 1.99 0.82 2.12
27 1.32 1.47 1.24 1.56 1.16 1.65 1.08 1.76 1.00 1.86 0.93 1.97 0.85 2.09
28 1.33 1.48 1.26 1.56 1.18 1.65 1.10 1.75 1.03 1.85 0.95 1.96 0.87 2.07
29 1.34 1.48 1.27 1.56 1.20 1.65 1.12 1.74 1.05 1.84 0.98 1.94 0.90 2.05
30 1.35 1.49 1.28 1.57 1.21 1.65 1.14 1.74 1.07 1.83 1.00 1.93 0.93 2.03
31 1.36 1.50 1.30 1.57 1.23 1.65 1.16 1.74 1.09 1.83 1.02 1.92 0.95 2.02
32 1.37 1.50 1.31 1.57 1.24 1.65 1.18 1.73 1.11 1.82 1.04 1.91 0.97 2.00
33 1.38 1.51 1.32 1.58 1.26 1.65 1.19 1.73 1.13 1.81 1.06 1.90 0.99 1.99
34 1.39 1.51 1.33 1.58 1.27 1.65 1.21 1.73 1.14 1.81 1.08 1.89 1.02 1.98
35 1.40 1.52 1.34 1.58 1.28 1.65 1.22 1.73 1.16 1.80 1.10 1.88 1.03 1.97
36 1.41 1.52 1.35 1.59 1.30 1.65 1.24 1.73 1.18 1.80 1.11 1.88 1.05 1.96
37 1.42 1.53 1.36 1.59 1.31 1.66 1.25 1.72 1.19 1.80 1.13 1.87 1.07 1.95
38 1.43 1.54 1.37 1.59 1.32 1.66 1.26 1.72 1.20 1.79 1.15 1.86 1.09 1.94
39 1.43 1.54 1.38 1.60 1.33 1.66 1.27 1.72 1.22 1.79 1.16 1.86 1.10 1.93
40 1.44 1.54 1.39 1.60 1.34 1.66 1.29 1.72 1.23 1.79 1.18 1.85 1.12 1.93
45 1.48 1.57 1.43 1.62 1.38 1.67 1.34 1.72 1.29 1.78 1.24 1.84 1.19 1.90
50 1.50 1.59 1.46 1.63 1.42 1.67 1.38 1.72 1.34 1.77 1.29 1.82 1.25 1.88
55 1.53 1.60 1.49 1.64 1.45 1.68 1.41 1.72 1.37 1.77 1.33 1.81 1.29 1.86
60 1.55 1.62 1.51 1.65 1.48 1.69 1.44 1.73 1.41 1.77 1.37 1.81 1.34 1.85
65 1.57 1.63 1.54 1.66 1.50 1.70 1.47 1.73 1.44 1.77 1.40 1.81 1.37 1.84
70 1.58 1.64 1.55 1.67 1.53 1.70 1.49 1.74 1.46 1.77 1.43 1.80 1.40 1.84
75 1.60 1.65 1.57 1.68 1.54 1.71 1.52 1.74 1.49 1.77 1.46 1.80 1.43 1.83
80 1.61 1.66 1.59 1.69 1.56 1.72 1.53 1.74 1.51 1.77 1.48 1.80 1.45 1.83
85 1.62 1.67 1.60 1.70 1.58 1.72 1.55 1.75 1.53 1.77 1.50 1.80 1.47 1.83
90 1.63 1.68 1.61 1.70 1.59 1.73 1.57 1.75 1.54 1.78 1.52 1.80 1.49 1.83
95 1.64 1.69 1.62 1.71 1.60 1.73 1.58 1.75 1.56 1.78 1.54 1.80 1.51 1.83
100 1.65 1.69 1.63 1.72 1.61 1.74 1.59 1.76 1.57 1.78 1.55 1.80 1.53 1.83
Source: N. E. Savin and Kenneth J. White, “The Durbin–Watson Test for Serial Correlation 
with Extreme Sample Sizes or Many Regressors,” Econometrica, November 1977, p. 1994. 
­Reprinted with permission.
Note: N = number of observations, K = number of explanatory variables excluding the constant 
term. We assume that the equation contains a constant term and no lagged dependent variables.


526
aPPENDIX B
Table B-5: The Normal Distribution
The normal distribution is usually assumed for the error term in a regression 
equation. Table B-5 indicates the probability that a randomly drawn number 
from the standardized normal distribution (mean = 0 and variance = 1) 
will be greater than or equal to the number identified in the side tabs, 
called Z. For a normally distributed variable e with mean μ and variance σ2, 
Z = 1e - μ2/σ. The row tab gives Z to the first decimal place, and the 
­column tab adds the second decimal place of Z.


527
Statistical Tables
Table B-5  The Normal Distribution
z
.00
.01
.02
.03
.04
.05
.06
.07
.08
.09
0.0
.5000
.4960
.4920
.4880
.4840
.4801
.4761
.4721
.4681
.4641
0.1
.4602
.4562
.4522
.4483
.4443
.4404
.4364
.4325
.4286
.4247
0.2
.4207
.4168
.4129
.4090
.4052
.4013
.3974
.3936
.3897
.3859
0.3
.3821
.3783
.3745
.3707
.3669
.3632
.3594
.3557
.3520
.3483
0.4
.3446
.3409
.3372
.3336
.3300
.3264
.3228
.3192
.3156
.3121
0.5
.3085
.3050
.3015
.2981
.2946
.2912
.2877
.2843
.2810
.2776
0.6
.2743
.2709
.2676
.2643
.2611
.2578
.2546
.2514
.2483
.2451
0.7
.2420
.2389
.2358
.2327
.2296
.2266
.2236
.2206
.2177
.2148
0.8
.2119
.2090
.2061
.2033
.2005
.1977
.1949
.1922
.1894
.1867
0.9
.1841
.1814
.1788
.1762
.1736
.1711
.1685
.1660
.1635
.1611
1.0
.1587
.1562
.1539
.1515
.1492
.1469
.1446
.1423
.1401
.1379
1.1
.1357
.1335
.1314
.1292
.1271
.1251
.1230
.1210
.1190
.1170
1.2
.1151
.1131
.1112
.1093
.1075
.1056
.1038
.1020
.1003
.0985
1.3
.0968
.0951
.0934
.0918
.0901
.0885
.0869
.0853
.0838
.0823
1.4
.0808
.0793
.0778
.0764
.0749
.0735
.0721
.0708
.0694
.0681
1.5
.0668
.0655
.0643
.0630
.0618
.0606
.0594
.0582
.0571
.0559
1.6
.0548
.0537
.0526
.0516
.0505
.0495
.0485
.0475
.0465
.0455
1.7
.0446
.0436
.0427
.0418
.0409
.0401
.0392
.0384
.0375
.0367
1.8
.0359
.0351
.0344
.0336
.0329
.0322
.0314
.0307
.0301
.0294
1.9
.0287
.0281
.0274
.0268
.0262
.0256
.0250
.0244
.0239
.0233
2.0
.0228
.0222
.0217
.0212
.0207
.0202
.0197
.0192
.0188
.0183
2.1
.0179
.0174
.0170
.0166
.0162
.0158
.0154
.0150
.0146
.0143
2.2
.0139
.0136
.0132
.0129
.0125
.0122
.0119
.0116
.0113
.0110
2.3
.0107
.0104
.0102
.0099
.0096
.0094
.0091
.0089
.0087
.0084
2.4
.0082
.0080
.0078
.0075
.0073
.0071
.0069
.0068
.0066
.0064
2.5
.0062
.0060
.0059
.0057
.0055
.0054
.0052
.0051
.0049
.0048
2.6
.0047
.0045
.0044
.0043
.0041
.0040
.0039
.0038
.0037
.0036
2.7
.0035
.0034
.0033
.0032
.0031
.0030
.0029
.0028
.0027
.0026
2.8
.0026
.0025
.0024
.0023
.0023
.0022
.0021
.0020
.0020
.0019
2.9
.0019
.0018
.0018
.0017
.0016
.0016
.0015
.0015
.0014
.0014
3.0
.0013
.0013
.0013
.0012
.0012
.0011
.0011
.0011
.0011
.0010
Source: Based on Biometrika Tables for Statisticians, Vol. 1, 3rd ed., 1966, with the permission 
of the Biometrika trustees.
Note: The table plots the cumulative probability Z 7 z.


528
aPPENDIX B
Table B-6: The Chi-Square Distribution
The chi-square distribution describes the distribution of the estimate of the 
variance of the error term. It is useful in a number of tests, including the 
White test of Section 10.3 and the Lagrange Multiplier Serial Correlation 
Test of Section 9.4. The rows represent degrees of freedom, and the columns 
denote the probability that a number drawn randomly from the chi-square 
distribution will be greater than or equal to the number shown in the body 
of the table. For example, the probability is 10 percent that a number drawn 
randomly from any chi-square distribution will be greater than or equal to 
22.3 for 15 degrees of freedom.
To run a White test for heteroskedasticity, calculate NR2, where N is the 
sample size and R2 is the coefficient of determination (unadjusted R2) from 
Equation 10.9. (This equation has as its dependent variable the squared 
residual of the equation to be tested and has as its independent variables 
the independent variables of the equation to be tested plus the squares and 
cross-products of these independent variables.)
The test statistic NR2 has a chi-square distribution with degrees of freedom 
equal to the number of slope coefficients in Equation 10.9. If NR2 is larger 
than the critical chi-square value found in Statistical Table B-6, then we reject 
the null hypothesis and conclude that it’s likely that we have heteroskedastic-
ity. If NR2 is less than the critical chi-square value, then we cannot reject the 
null hypothesis of homoskedasticity.


529
Statistical Tables
Table B-6  The Chi-Square Distribution
Degrees  
of  
Freedom
Level of Significance 
(Probability of a Value at Least as Large as the Table Entry)
10%
5%
2.5%
1%
1
2.71
3.84
5.02
6.63
2
4.61
5.99
7.38
9.21
3
6.25
7.81
9.35
11.34
4
7.78
9.49
11.14
13.28
5
9.24
11.07
12.83
15.09
6
10.64
12.59
14.45
16.81
7
12.02
14.07
16.01
18.48
8
13.36
15.51
17.53
20.1
9
14.68
16.92
19.02
21.7
10
15.99
18.31
20.5
23.2
11
17.28
19.68
21.9
24.7
12
18.55
21.0
23.3
26.2
13
19.81
22.4
24.7
27.7
14
21.1
23.7
26.1
29.1
15
22.3
25.0
27.5
30.6
16
23.5
26.3
28.8
32.0
17
24.8
27.6
30.2
33.4
18
26.0
28.9
31.5
34.8
19
27.2
30.1
32.9
36.2
20
28.4
31.4
34.2
37.6
Source: Based on Biometrika Tables for Statisticians, Vol. 1, 3rd ed., 1966, with the permission 
of the Biometrika trustees.
Note: The table plots the cumulative probability Z 7 z.


This page intentionally left blank


Applied regression analysis, steps in
data collection, inspection, and  
cleaning, 69–71, 75, 76–77, 
90–91
defined, 66
documenting results, 72–73, 78–79, 91
dummy variables and, 79–83, 80
equation estimating and evaluating, 
72, 78, 91
exercise (econometric lab), 89–91
hypothesize expected signs of coeffi-
cients, 68–69, 75, 90
independent variables and functional 
form selection, 67–68, 74–75, 90
literature review and theoretical 
­modeling, 66–67, 74, 89–90
overview, 66–73
practical tips, 351–352
restaurant location decisions, 73–79. 
See also Woody’s restaurant 
­locations example
ARIMA forecasting technique
defined, 456
models, 457–459
Assumptions, in Classical model.  
See Classical Assumptions
Atukeren, Erdal, 375n8
Autocorrelation. See Serial correlation
Autoregressive equations, 367, 378
Autoregressive process, defined, 457
Average observations, 401
Barkley, Andrew, 176n10
Batte, Marvin T., 217, 217n9
Baum, Christopher F., 320n11
Acceptance regions, 119, 120, 133, 135, 
287, 287
Additive error term, 93–94
Adjusted R2, 52–54
dummy dependent variable models 
and, 402
incorrect functional form and,  
206–207
misuse example, 55–56
specification criteria for potential 
variable, 166
misuse example, 168
selection example, 177
specification search bias and,  
171–172
AIC (Akaike’s Information Criterion), 
187–188
Akaike, Hirotogu, 187n19
Akaike’s Information Criterion (AIC), 
187–188
Allen, R. C., 190n1
Alternative functional forms,  
192–201
Alternative hypotheses, 116–118
defined, 117
Amatya, Ramesh, 408n10
Amemiya, T., 404n8
American Economic Review, 73n5
Analysis
regression, 5–14. See also Regression 
analysis
residual, 164
sensitivity, 72, 174, 177
single-equation linear regression, 5
Ando, Albert, 332n17
INDEX
NOTE: Page numbers in italics refer to figures and tables; footnotes are indicated by 
“n” following the page number.
531


Bayaner, Ahmet, 217n9
Bayesian Information Criterion (BIC), 
187–188
Bayesian statistics, 116, 116n1
Becketti, Sean, 373n4
Belsley, D. A., 233n5
Bertrand, M., 470n4
Best Linear Unbiased Estimator (BLUE), 
106
Best practices, for specification searches, 
170
βn
sampling distribution of, 100–105, 
103, 104
SE(βn), 105
β0 (constant or intercept term), 7, 8, 
190–192
Classical Assumptions, 191
components, 190–191, 190n1
dummy variable and, 80n8
estimates, 192
regression equation and, 71
suppression, 191, 191–192
use and interpretation, 190–192
β1 (slope coefficient), 7–8
cross-sectional model, 22
Bias
Best Linear Unbiased Estimator, 106
in distributions of βn, 103
Durbin–Watson test, 284n5
in dynamic models, 368
expected, 161, 162–163, 162n4, 164
Generalized Least Squares, 295
heteroskedasticity, 312–313
measurement errors, 442
multicollinearity, 226–227, 236
Newey–West standard errors, 296
omitted variable. See Omitted 
­variable bias
Ordinary Least Squares, 418–421
serial correlation, 280n1
specification, 158
specification criteria, 166
independent variable selection 
­example, 177
misuse example, 168
specification searches, 171–172
t-tests, 171–172
Two-Stage Least Squares, 424n5
Bias equations, omitted variables, 161, 
162–163, 162n4
Biased estimator, 102, 102n7
BIC (Bayesian Information Criterion), 
187–188
Binomial logit, defined, 397
Binomial logit model, 397–404
example, 403–404
Binomial probit
defined, 404
model, 404–405
BLUE (Best Linear Unbiased Estimator), 
106
Borders
null hypothesis, 122
values, 130n8
Brada, Josef C., 300n18, 301
Brazilian black market for dollars  
(data set), 336–337
Breusch, T. S., 316n6
Breusch–Godfrey test, 289n11
Breusch–Pagan test, 316–318, 317n8, 320
defined, 316
British Household Panel Data Survey, 
474
Brown, Eleanor, 86
Bruggink, Thomas H., 150n15
Buckles, Stephen, 181n11
Bucklin, R. E., 334, 334n19
Bureau of Labor Statistics, 473
Cahill, Preston, 218n10
Campbell, J., 378n12
Campbell, John Y., 380n15
Canadian National Public Health 
­Survey, 474
Card, David, 469, 469n3
Carnot, N., 444n3
Cassel, Eric, 360n8
Causality
dual, 412
Granger, 374–376
regression analysis and, 5–6
532
INDEX


Caves, R. E., 334, 334n19
Census Catalog and Guide, 345
Checklist, regression projects,  
354–355
Chi-square test
heteroskedasticity, 317, 319, 327
serial correlation, 373
Chicken consumption example
Durbin–Watson statistic, 288n8, 452
forecasting and, 445–447, 447, 452
Generalized Least Squares,  
294–295
Cigarette consumption (data set), 487
City expenditures functions
aggregate, 323
per capita, 324
Classical Assumptions, 92
constant variance for error term (V), 
96–98, 97
explanatory variables uncorrelated 
with error term (III), 95–96
independence of observations of error 
term (IV), 96
linear regression model (I), 93–94, 
93n1
multicollinearity of explanatory 
­variables (VI), 98
normal distribution for error term 
(VII), 98–99, 99
violations
constant term, 191
heteroskedasticity, 306, 307
instrumental variables, 421–422
multicollinearity, 221–222
omitted variables and, 
­consequences of, 159–160
serial correlation, 273, 275, 282, 
371–372
simultaneous equations, 411,  
415, 416
zero population mean, error terms 
with (II), 94, 94–95
Classical error term, 93
Classical model, 92–108
Classical Assumptions, 92–99, 93n1
Gauss–Markov Theorem, 106–107
sampling distribution of βn, 100–105
standard econometric notation,  
107–108, 108
Classical normal error term, 93
Classical null hypothesis, 116–118
Cleaning data, 71, 75, 90–91
Cochrane, D., 293n14
Cochrane–Orcutt method, 293, 293n15
Coefficient errors, applied regression 
analysis, 72, 73n4, 78, 78n7
Coefficient estimators, properties, 107
Coefficients, 7
double-log functions, 195, 195
dummy variable, 81–82
estimated/estimating, 78, 78n7
t-values and, 78, 78n7
estimated logit, interpreting, 400–403
expected signs, 68–69, 75, 90
F-tests, 142
heteroskedasticity, 312–313
linear in the, 93n1, 193
multicollinearity, 226–228
multivariate regression, 12, 41–42
omitted variable, 158
Ordinary Least Squares and, 38, 
38n3, 392
partial regression, 41–42
random, estimation of, 105
reduced-form, 417
regression, notation for, 108
seasonal dummy, 147
serial correlation, 275
simple correlation, 232–233, 232n3, 
233n4
slope. See Slope coefficient (β1)
structural, 413
true, 15n9
unexpected sign, handling of,  
348–350
Cohen, Kalman, 335n21
Cohen, Malcolm, 409n11
Cointegration, 382–384
defined, 383
Cola supply and demand model,  
414, 416
Collection, of data, 69–71, 75
533
INDEX


534
INDEX
Critical values
defined, 119
F-value, 145, 145n14
t-values, 119, 123–125, 132, 133, 135
selecting, 130
Cross-sectional data sets/models
defined, 21
heteroskedasticity in, 309
housing prices, 20–23, 22
pooled cross sections across time, 
473n7
time series studies vs., 274–275
Data
cleaning, 71, 75, 90–91
collecting, 69–71, 75, 90–91
inspecting, 71, 75, 90–91
missing, 346
panel. See Panel data
research projects, 342–346
Data collection
advanced sources for, 346–348
missing data, 346
panel data, 347–348
for regression projects, 342–346
surveys, 347
Data entry errors, finding, 71, 91
Data mining, 172–173
Data sets
Brazilian black market for dollars, 
336–337
cigarette consumption, 487
college application, 61–62
cross-sectional. See Cross-sectional 
data sets/models
financial aid example, 46–47
Four Musketeers, 388
heteroskedasticity in, 308–309
homeowners’ (non-self-employed) 
income and consumption, 333
housing prices, 361–362
labor force participation of women, 396
murder rate example, 479–481
MVP 1998, 243
petroleum consumption, 326–327
pharmaceutical price discrimination, 
154
College application (data set), 61–62
Collinearity, 98, 222n1. See also 
­Multicollinearity
Common Application, 60, 60n9
data set example, 61–62
Compound null hypotheses, 142, 147
Condition number, 233n5
Conditional forecast/forecasting, 
450–451
defined, 450
Conditions
omitted, dummy variables and, 80, 
82–83
order, 433–434
rank, 433n11
Confidence intervals, 139–142
defined, 139
forecasting, 449, 452–454, 455
Confidence level, 127
Consequences
heteroskedasticity, 312–314
irrelevant variables, 165
multicollinearity, 226–231
omitted variables, 159–160
serial correlation, 281–284
Constant term, defined, 7. See also β0 
(constant or intercept term)
Constant variance, 96–98, 97, 306
Constants, 7
Control groups, 465–472, 472
defined, 465
Corrections
Error Correction Model, 384n20
heteroskedasticity, 320–324,  
337–339
multicollinearity, 235–240
omitted variables, 163–164
serial correlation, 291–296
in dynamic models, 373–374
Correlation
serial. See Serial correlation
simple correlation coefficients,  
232–233, 232n3, 233n4
spurious, 376–385
Covariance stationarity, 377n11
Criteria specification, 166–167
misuse example, 167–169


535
INDEX
measurement errors, 440–441
other techniques, 404–406
variations in. See under Y variable
Derivatives, partial, 401
Description, 2–3
Deseasonalizing data, 146
Detection
heteroskedasticity, 314–320
econometric lab exercise, 337–338
multicollinearity, 232–235
nonstationarity, 386
serial correlation, 284–291
Deterministic component, regression 
equation, 9
Deviations, standard, 107
Dewald, W. G., 73n5
Diamond, A., 470n4
Diaz, Jaime, 25n11
DiCioccio, E., 484n14
Dickey, D. A., 380n14
Dickey–Fuller test, 379–382
defined, 380
Diekmann, Florian, 217, 217n9
Difference-in-differences estimator, 
­defined, 470
Differences
estimator, 467
observed, systematic reasons for, 466
Differencing models, 475n10, 
 488–489
Discrete heteroskedasticity, 308, 309
Dispersion. See Variance
Distributed lag models, 365–367
defined, 365
Distributions
biases, 103
discrete heteroskedasticity, 309
homoskedasticity vs., 307, 308
impure serial correlation, 278
intercept, 484
multicollinearity, 226–227, 227
normal, 420n4
error terms and, 98–99, 99
sampling distribution of βn, 100–105, 
103, 104
simultaneity bias, 421
Standard Normal, 99
pooled cross sections across time, 
473n7
Presidential election, 463
from RateMyProfessor.com, 29
salon haircut, 488
SAT interactive learning exercise, 
248–249
small macromodel, 426
Soviet defense spending, 301
stock price, 212–213
student consumption, 229
Woody’s restaurant locations 
­example, 76–77
Decision rules
acceptance and rejection regions,  
285, 287
defined, 119
F-test, 143
hypothesis testing, 119, 120, 121
t-test, 123–125, 131
Decomposition, variance, 47, 48
Degree of confidence, 127
Degrees of freedom
critical t-value and, 123
defined, 53
dynamic models, 366–368
F-tests, 143–145
heteroskedasticity and, 319, 320n11, 
327n15
number of observations and, 69–70
regression equation and
adjustment, 54
calculating, 70, 70n3
sequential specification criteria and, 
186, 187
t-tests, 123, 124
variance of distribution and, 104
Δ notation, 194n2
Demeaned model, 475n10
Denny’s restaurants, 73n6. See also 
Woody’s restaurant locations 
­example
Dent, W., 375n9
Dependent variables, 5–6, 390
binomial logit model, 397–404
estimated vs. actual value, 15–16
linear probability model, 390–397


536
INDEX
Durbin–Watson tables (Stanford 
­University), 289n10
Durbin–Watson test
defined, 284
for serial correlation detection,  
284–286, 285n7
dynamic models, 372, 372n3
examples, 286–289, 287
one-sided, 287
Dynamic models, 364, 367–371
basic form, 367–371
bias, 368
defined, 367
distributed lag models, 365–367
example, 369–370
geometric weighting schemes, 369
Granger causality and, 374–376
serial correlation, 371–374
corrections, 373–374
testing for, 372–373
serial correlation and, 374–376
ECM (Error Correction Model),  
384n20
EconLit, 67, 67n1, 345
Econometric Labs
applied regression analysis, 89–91
heteroskedasticity, detection and 
­correction exercise, 337–339
hypothesis testing, 155–156
regression analysis, 63–64
serial correlation, 303–305
specification, 217–220
Econometrics
alternative approaches, 4–5
Classical model, 92–108
definitions, 1–2
ethical behavior and, 351–352
notation conventions, 107–108, 108
software. See individually named 
­applications; Software
uses, 2–4
Economic activity, relationships 
­describing, 2–3
Economic data, sources, 345. See also 
Data collection
Disturbance (error) terms. See Stochas-
tic error terms
Documentation, results, 72–73,  
78–79, 91
Dominant variable, defined, 224
Dorfman, J. J., 393n2
Dornbusch, Rudiger, 334, 334n20
Double-log functional forms, 194–196, 
195, 201
defined, 194
Driver’s license test, binomial logit 
­example, 403–404
Dropping variables, 162n4, 164,  
170, 171
redundant variables, 236–238
Dual causality, 412
Dummy variable trap, 81
Dummy variables, 14, 146–147, 
319n10
applied regression analysis and, 
79–83, 80
defined, 79
dependent, 390
binomial logit mode, 397–404
binomial probit model, 404–405
linear probability model, 391–392
multinomial models, 405–406
Ordinary Least Squares and, 392
other techniques, 404–406
examples, 175
independent
functional forms, 196, 203–206
in housing price exercise, 359, 361
log of, 196
omitted condition and, 82–83
one-time, 83
seasonal, 146–147
slope, 203–206, 205
Durbin, J., 284n4
Durbin–Watson statistic
heteroskedasticity, 325
serial correlation
equation, 284–286
software calculation, 289n9
tables, 289n11
use examples, 286–289


537
INDEX
estimated regression equation, 16
homoskedastic vs. heteroskedastic, 
310–311, 310–311
notation, 108
observations, 96
standard deviation, notation for, 108
stochastic, 8–11, 94, 94–95, 95n2, 96
with zero population mean, 94, 
94–95
Errors
coefficients, 73n4
data entry, finding, 71, 91
explanatory variables, 95–96
heteroskedasticity, 307, 321
homoskedasticity vs., 310–311, 
310–311
impure serial correlation, 307
irrelevant variables, 165–166
Mean Square Error, 105
measurement, 441–442
Y variation and, 9
nonlinear relationships, 10
normal distribution, 98–99, 99
Ramsey Regression Specification Error 
Test, 185–186
rounding, 39
serial correlation, 275
specification, 68, 157–158
standard. See Standard errors
term distribution with a mean of 
zero, 94, 94–95
Type I Errors, 118–119
Type II Errors, 118–119
variables, 440–442
ESS (explained sum of squares), 48–49, 
48n6, 145, 145n13
defined, 48
estat bgodfrey lag, 289n11
Estimated coefficients, 78, 78n7
logit, interpreting, 400–403
random, 105
regression, weight/height example, 40
Estimated regression equation, 14–17
defined, 14
Ordinary Least Squares technique 
and, 50–54
Economics, experimental, 465n1
methods, 466–472
Efficiency, of estimators, 106
Elasticity, defined, 194
Elder, John, 381n16
Elliott, G., 444n3
Endogenous variables, 412–413, 428n9
defined, 412
Engel curves, 198
Engle, Rob, 290n12, 382n17, 384n19
Equations
autoregressive, 367, 378
Best Linear Unbiased Estimator, 106
bias, omitted variables and, 161, 
162–163, 162n4
distributed lag models, 366
Durbin–Watson test, 284
Generalized Least Squares, 292–295
identification problem, 430–434
independent variables, 161n3
investment, 427n9
linear
in the coefficients, 193
defined, 8, 8n5
in the variables, 192–193
multiple regression, 121
Ordinary Least Squares, 392
Ramsey Regression Specification Error 
Test, 186, 186n16
reduced-form, 416–417
OLS and, 423
regression. See Regression equation
second-degree polynomial, 200, 200, 
201
serial correlation, 282
simultaneous. See Simultaneous 
equations
single-equation linear models, 6–8
stochastic error terms, 8–11
supply and demand simultaneous, 416
weight-guessing, 17–19, 20
Error Correction Model (ECM), 384n20
Error term
additive, 93–94
classical, 93
constant variance, 96–98, 97


538
INDEX
Exogenous variables, 412–413
defined, 412
Expectations
signs of coefficients, 68–69, 75, 90
values, 9
estimated coefficients, notation  
for, 108
Expected bias, 161, 162–163, 162n4, 164
Expected value, defined, 9
Experimental economics, 465n1
methods, 466–472
Experiments
impossible, 468
natural, 469–472
random assignment, 466–468
Explained sum of squares (ESS), 48–49, 
48n6, 145, 145n13
defined, 48
Explanatory variables. See Independent 
variables
F-statistic, 143
Breusch–Pagan test, 316n7
F-test, 142–147, 376, 376n10
defined, 142
other uses, 146–147
overview, 142–144
significance, 144–146
F-values, 143–144
Fair, Ray C., 211, 211n6, 444n2, 
461n13
Fallows, James, 246n7
FDA (Food and Drug Administration), 
116
Feedback effects, 412
Financial aid (multivariate regression 
model example), 43–47
as ability to pay, 45
data set, 46–47
as function of high school rank, 45
First-order autocorrelation coefficient, 
defined, 275
First-order serial correlation, 275
Durbin–Watson test, 284–289, 285n6
Generalized Least Squares, 292
Lagrange Multiplier test, 289
Estimates
constant terms, 192
defined, 36
heteroskedasticity, 312–313
multicollinearity and, 226
Ordinary Least Squares, 384
regression, 288
serial correlation, 282–283
Two-Stage Least Squares, 424n5
validity, 49–50
Estimation
binomial logit, 397–400
coefficients, 78, 78n7
distributed lag models, 365–367
dynamic models, 368, 370
fixed effects models, 472n6, 477–483
linear probability model, 392
Ordinary Least Squares, 37
estimator properties, 106–107
example, 39–40
multivariate regression model, 
40–49
properties, 37, 37n2
regression equations, 50–54, 72, 78
single-independent-variable 
­models, 35–40
random coefficients, 105
sample size and, 69
standard errors, 78, 78n7, 314n4
Two-Stage Least Squares, 428n10
Estimators, 100
Best Linear Unbiased Estimator, 106
biased, 102, 102n7
defined, 37
differences, 467
difference-in-differences, 470
efficiency, 106
Ordinary Least Squares coefficients, 
properties of, 106–107
Two-Stage Least Squares, 424–425, 
424n5
unbiased, 101, 102n7, 106, 107
Ethics, 351–352
EViews, 72
Durbin–Watson statistic, 288n9
Generalized Least Squares, 294n16


539
INDEX
inverse, 197, 197n4
lagged independent variables and, 
202–203
linear, 194, 201
polynomial, 199–201, 200, 201
pure serial correlation and, 275
quadratic, 200, 201, 200
selecting, 201, 201
semilog, 196–199, 198, 201
stochastic error and, 9–10
Functions
double-log, 194–196, 195
investment, 427n8
linear, 98
polynomial, 199–201, 200
semilog, 196–199, 198
Gauss–Markov Theorem, 106–107
heteroskedasticity, 313
GDP (Gross Domestic Product),  
3–4, 344
Generalized Least Squares (GLS), 
292–295
defined, 292
Gensemer, Bruce, 438n12
Geometric weighting schemes, 369
Geweke, John, 375n9
GLS (Generalized Least Squares), 
292–295
defined, 292
Gneezy, Uri, 465n1
Goldman, Dana, 409n12
Goodman, Allen C., 360n9
Goodness-of-fit measures, 50–52, 51
spurious regression and, 56
Granger, C. W. J., 375n7, 379n13, 
382n17, 384n19, 444n3
Granger, Clive, 4n4
Granger causality, 374–376, 389n22
defined, 375
Graves, Ronald L., 300n18, 301
Greene, William H., 406n9, 442n14
Grether, G. M., 359n6
Griffiths, W. E., 187n20
Griliches, Zvi, 290n12, 442n15
Gross Domestic Product (GDP), 3–4, 344
Fit
goodness of. See Goodness of fit 
­measures
mathematical vs. statistical, in X,Y 
­coordinate system, 69–70, 70, 71
measuring, linear probability model 
and, 392
Fixed effects model, 475–477
defined, 475
estimation, 472n6, 477–483
panel data and, 481–482, 482n11
random effects model vs., 484
Fluctuations, random, 466
Food and Drug Administration (FDA), 
116
Forecasting, 3–4, 21, 443–444
ARIMA models, 456–459
complex problems, 449–456
defined, 444
examples, 447
uses, 444–449
Forms. See Functional forms
Forst, Jerry, 176n10
Four Musketeers (data set), 388
Four specification criteria, 166. See also 
Specification criteria
Fowles, Richard, 216, 216n8
FRED (Federal Reserve Economic 
­Database), 345
Freeman, Vera, 181n11
Friedman, Milton, 116
Friend, I., 332n17
Fuller, W. A., 380n14
Functional form test, RESET as, 186n18
Functional forms
alternatives, 192–201, 201
applied regression analysis, 67–68, 
74–75, 90
constant term, use and interpretation 
of, 190–192
double-log, 194–196, 195, 201
dummy variables and, 196, 203–206, 
205
impure serial correlation and,  
278–279, 280, 281
incorrect, problems with, 206–209, 208


540
INDEX
Heteroskedasticity-consistent covari-
ance matrix (HCCM), 321n12
Heteroskedasticity-corrected standard 
errors (HCSEs), 321, 323n11, 
330
detected, 321
Hill, R. Carter, 187n20
Hirschfield, Mary, 86
Homeowners’ (non-self-employed) 
­income and consumption  
(data set), 333
Homoskedasticity, 306, 307, 308
errors, 310–311, 311
heteroskedasticity vs., 307, 308
error terms, 310–311, 310–311
in linear probability model, 392
Hoover, Kevin, 375n8
Housing prices
cross-sectional model, 21–23, 22
data set, 361–362
interactive exercise, 360–363
regression analysis explaining, 20–23
Hypothesis
alternative, 116–118
classical null, 116–118
expected signs of coefficients, 68–69, 
75, 90
priors and, 68
Hypothesis testing, 3, 5, 99, 115–116, 
155–156
confidence level, 127
data mining and, 172–173
decision rules, 119, 120, 121
error types, 118–119
exercise (econometric lab), 155–156
overview, 116–121
serial correlation, 283–284
t-tests, 121–139
“i” subscript, in regression equation, 
13–14
order, 14n8
Identification
defined, 430
problem, 430–434
Ihlanfeldt, Keith, 360, 360n8
Groups
control, 465–472, 472
treatment, 465–472, 472
Grubb, David, 368n2
Guides, regression projects, 356, 357
Hainmueller, J., 470n4
Hamermesh, Daniel S., 73n5
Hastings, Justine, 471n5, 471n6
Hausman test, 484
Hawthorne Effect, 468
Haynes, Stephen, 461n14, 462n15, 463
HCCM (heteroskedasticity-consistent 
covariance matrix), 321n12
HCSEs (heteroskedasticity-corrected 
standard errors), 321, 323n11, 
330
detected, 321
Hedonic models, 21n10, 87–89, 87n11
housing prices, 358–360
Hendry, David F., 137n10
Heo, Uk, 389, 389n21
Heterogeneity, unobservable, 468
Heteroskedasticity
bias, 312–313
Classical Assumptions, 97, 98, 306, 
307
coefficients, 312–313
consequences, 312–314
data sets, 308–309
defined, 307
detection and correction exercise 
(econometric lab), 337–339
discrete, 308, 309
errors, 310–311, 311
estimates, 312–313
example, 324–330
Gauss–Markov Theorem, 313
homoskedasticity vs., 307, 308
error terms, 310–311, 310–311
impure, 311–312
pure, 307–311
remedies for, 320–324
statistics, 313n3
testing for, 314–320
time-series models, 311


541
INDEX
Indifference curves, 195, 195–196
Inflation, high variance inflation factors 
and, 233–235, 233n5, 235n6
Inspection, of data, 71, 75, 90–91
Instrumental variables, 421–422, 
428n9, 442
defined, 421
Interaction terms, 203–204
defined, 203
Intercept dummy, 205
defined, 203
Intercept term. See also β0 (constant or 
intercept term)
defined, 7
distribution, 484
Internet resources, for project data, 345
Interpreting estimated logit coefficients, 
400–403
defined, 400
Intervals, confidence, 139–142
Intriligator, M. D., 290n12
Inverse functional form, 197, 197n4
Investment functions, 427n8
Irrelevant variables, 165–167
defined, 165
Isoquant, 195, 195
Jacobs, Rodney, 375n9
Jevons, Stanley, 6
Johnson, Bruce, 55n7, 63n11
Joint null hypotheses, 142, 147
Jones, R., 332n17
Journal of Economic Literature, 67
Journal of Money, Credit, and Banking, 
73n5
Judge, George C., 187n20
Kain, J., 359n6
Keele, Luke, 374n6
Keeler, James, 438n12
Kelly, Nathan, 374n6
Kenkel, Donald S., 113n10
Kennedy, Peter, 100n6, 116n1, 350n5, 
381n16, 383n18, 384n20, 
446n5, 474n9, 484n13
Keynes, John Maynard, 89, 116
Impact multipliers, defined, 417
Imperfect multicollinearity, 224–225, 
225
defined, 224
“Importance,” testing of, 138–139
Impossible experiments, 488
Impure heteroskedasticity, 311–312
defined, 311
Impure serial correlation, 278–281, 
279, 281
defined, 278
Lagrange Multiplier test, 365
simple lags, 365
Inconclusive region, serial correlation 
detection, 285n7, 287
Incorrect functional forms, problems 
with, 206–209, 208
Independent variables, 5–6, 12
data mining, 172–173
equations, 161n3
error term relationship and, 96
examples, 174–177
interaction terms as, 203–204
lagged, 202–203
measurement errors, 441–442
multicollinearity, 222n1
multivariate regression coefficients 
and, 41
notation in regression analysis, 11–12
omitted. See Omitted variables
omitted variables, 158–164
in regression equation, examples, 
13–14
selecting
in applied regression analysis,  
67–68, 74–75, 90
example, 174–177
sensitivity analysis, 174, 177
single-independent-variable models, 
OLS and, 35–40
specification, 170–174. See also 
­Specification
errors, 68, 157–158
stochastic error and, 8, 8n6
Index of Leading Indicators, 450
Indicator, leading, 450–451


542
INDEX
defined, 126
marginal, 127
t-test value, 123, 130
selecting, 126–127
Likelihood ratio test, 185n14
Linear equations, 8n5
defined, 8
Linear functional forms, 98, 198, 201, 
281
nonlinear forms vs, 208, 208–209
Linear in the coefficients, 93n1
defined, 193
Linear in the variables, 192–193
defined, 192
Linear probability model, 390–397
defined, 390
example of, 394–396
Ordinary Least Squares and, 392, 399
problems with, 392–394, 393
Linear regression model, 93–94, 93n1, 
194, 280
Linneman, Peter, 359, 359n7
List, John, 465n1
Literature review, in applied regression 
analysis, 66–67, 74, 89–90
Lo, A. W., 334, 334n19
Loeb, Peter D., 216, 216n8
Log-log (double-log) functional forms, 
194–196, 195, 201
Log (logarithm)
defined, 196
natural, 196–197
zero value and, 196, 197n4
Longitudinal data. See Panel data
Lott, William F., 334n20, 337
Lutkepohl, Helmut, 187n20
MacKinnon, J. G., 382n17, 384n19
Macromodel, small (data set), 426
Maddala, G. S., 186n18, 399n5, 404n8
Maeshiro, Asatoshi, 374n5
Malkiel, Burton, 449n6
Mankiw, N. G., 378n12
MAPE (mean absolute percentage 
error), defined, 446
Marginal significance level, 127
Keynesian macroeconomic model, 
naive linear, 425–429, 427n7
Kmenta, Jan, 118, 118n2
Kobayashi, Masahito, 293n15
Koen, V., 444n3
Koopmans, T. C., 1n1
Koyck, L. M., 368n1
Koyck distributed lag models, 368n1
Krueger, Alan, 469, 469n3
Labor force participation of women 
(data set), 396
Lagged independent variables,  
202–203, 413, 416, 423
Lagrange Multiplier (LM) test
defined, 289
heteroskedasticity and, 314n5
for serial correlation, 289–291, 
289n11
dynamic models and, 372–373
Lags
defined, 202
distributed lag models, 365–367
estat bgodfrey, 289n11
Koyck distributed lag models, 368n1
lagged values, 364
lagged variables, 202–203, 413, 416, 
423
dependent as independent, 364–372
time, 412n1
Lancaster, Tony, 116n1
Leading indicator, 450–451
defined, 450
Leamer, Ed, 1n1, 118n4, 375n9
Least squares. See Generalized Least 
Squares (GLS); Ordinary Least 
Squares (OLS); Two-Stage Least 
Squares (2SLS); Weighted Least 
Squares (WLS)
Lee, Tsoung-Chao, 187n20
Left-out variables. See Omitted variables
Left-side semilog, 199, 208
Lerman, Robert I., 409n11
Level of confidence, 127
Level of significance
choosing, 130


543
INDEX
demeaned, 475n10
differencing, 475n10, 488–489
distributed lag, 365–367
dynamic. See Dynamic models
Error Correction, 384n20
fixed effects, 475–477
estimation, 477–483
random effects model vs., 484
forecasting. See Forecasting
functional forms. See Functional 
forms
hedonic, 21n10, 87–89, 87n11, 
358–360
Keynesian, 427n7
Koyck distributed lag, 368n1
linear probability, 390–397
multinomial, 405–406
multivariate regression, estimating 
with OLS, 40–49
Ordinary Least Squares, 392, 399
panel data, 482
random effects, 483–484
simultaneous equation, forecasting 
and, 449
single-equation linear, 6–8
single-independent-variable, 
­estimating with OLS, 35–40
specifying, in applied regression 
­analysis, 67–68, 74–75, 90
supply and demand, 414, 416
theoretical, in applied regression 
analysis, 66–67, 74, 89–90
time-series. See Time-series models
Modigliani, Franco, 332n17
Monte Carlo studies, 187n20, 419n3
Moore, Robert L., 86
Mosteller, Frederick, 160n2
Moving-average process, defined, 457
MSE (Mean Square Error), 105
Multicollinearity, 98
bias, 236
consequences, 226–231
correction, 235–240
defined, 222n1
detection of, 232–235
distribution, 226–227, 227
Markov scheme, 275
Martinez-Vasquez, Jorge, 360, 360n8
Maximum likelihood (ML), 399, 399n4
Mayer, Thomas, 173n9
McCulloch, J. Huston, 306n1
McCullough, B. D., 290n12
McGillvray, R. G., 392n1
McIntosh, C. S., 393n2
Mean
forecasting methods and, 446
properties, 102–103
zero population, 94, 94–95
Mean absolute percentage error 
(MAPE), defined, 446
Mean Square Error (MSE), 105
Measurement error
simultaneous equations, 441–442, 
442n15
Y variation and, 9
Measurement unit, of variables, 70–71
Measurements. See also Equations
economic, 1–2. See also Econometrics
forecasting accuracy, 445–447, 447
overall fit, linear probability model, 
392
Meese, R., 375n9
Mendelsohn, Robert, 360n8
Methods
Cochrane–Orcutt, 293, 293n15
experimental economics, 466–472
mean absolute percentage error, 446
Prais–Winsten, 293, 293n15
Root mean square error, 446
Michener, Ron, 329
Mieszkowski, Peter, 359n6
Miller, Roger Leroy, 167n6
Missing data, 346
Misuse of adjusted R2, 55–56
ML (maximum likelihood), 399, 399n4
Models
ARIMA, 456–459
binomial logit, 397–404
binomial probit, 404–405
classical. See Classical model
cross-sectional. See Cross-sectional 
data sets/models


544
INDEX
Newey–West standard errors, 295–296
defined, 295
heteroskedasticity, 321n12
Nixon, Clair J., 217n9
NLSY (National Longitudinal Survey of 
Youth), 473
No serial correlation, 278
Non-random samples, 467–468
Nonexperimental quantitative research, 
steps in, 4–5
Nonstationarity, 376–385
cointegration, 382–384
detecting, 386
Dickey–Fuller test, 382–384
macroeconomic model, 429
sequences for dealing with, 384–385
spurious correlation and, 376–385
spurious regression, 379
testing for, 379–382
Nonstationary
defined, 377
time series, 377–378
Normal distributions, 420n4
error terms, 98–99, 99
Notation
delta, as used in text, 194n2
independent variables, 11–12
regression, extending, 11–14
standard econometric, 107–108, 108
time series studies, 274
Null hypothesis, 116–118
acceptance, 119, 120, 121
border for, 121–122, 130n6
defined, 117
F-test, 142–147
heteroskedasticity, 320, 320n11, 327, 
327n15, 328
homoskedasticity, 316–317
rejection, 117–119, 120, 123–125
stating, 130n8
testing, 155–156
Oat market supply and demand model, 
437–438
Observations
average, 401
Multicollinearity (continued)
imperfect, 224–225, 225
perfect, 98, 221, 222–224, 224
remedies for, 235–238
severe, 227, 366, 370
t-scores, 227–228
unadjusted, 238–240
unavoidable, 366
unexpected sign and, 349
variances, 226–227, 227
Multinomial logit, 406n9
Multinomial models, 405–406
Multiple regression equations, t-statistic 
and, 121
Multipliers
impact, 417
Lagrange. See Lagrange Multiplier 
(LM) test
Multivariate regression coefficients, 12, 
41–42
defined, 41
Multivariate regression model
defined, 12
equation, 12, 42–43, 43n4
estimating with OLS, 40–49
example, 43–47
Murder rate (data set), 479–481
Murti, V. N., 216, 216n7
MVP 1998 (data set), 243
Narrow distribution, 308, 309
National Health Interview Survey 
(1990), 113n11
National Longitudinal Survey of Youth 
(NLSY), 473
Natural experiments, 469–471
defined, 469
example, 471–472
Natural logs, 196–197
defined, 196
Negative critical values, 382n17
Negative serial correlation,  
276, 279
Nelson, C. R., 378n12, 457n10
Newbold, P., 379n13
Newey, W. K., 295n17


545
INDEX
distributed lag models, 365–367
estimation using
estimator properties, 106–107
example, 39–40
multivariate regression model, 
40–49
regression equations, 50–54, 72, 78
single-independent-variable 
­models, 35–40
F-test, 143
heteroskedasticity and, 313–314
linear equations and, 195
linear probability models, 392, 399
mechanics, 38
misuse of adjusted R2, 55–56
multicollinearity and, 223, 228
reduced-form equations and, 423
regression equations, evaluating 
­quality of, 49–50
serial correlation, 282–283
simultaneous equations and, 411
using, reasons for, 36–37
Otto, James, 28n13
Outlier, 71
Overall fit, measuring, 392
p-values, 127–128
defined, 127
limitations, 137n9
Pagan, A. R., 316n6
Panel data, 473–475, 482
defined, 473
fixed effects model applied to,  
481–482, 482n11
formation, 465
regression project and, 347–348
Parameters, Ordinary Least Squares 
­estimate, 37
Park, R. E., 317n8
Park test, 317n8
Partial derivatives, 401
Partial regression coefficients, 41–42
Pechman, Clarice, 334, 334n20
Perfect multicollinearity, 98, 221, 
 222–224, 224
defined, 222
differences in, systematic reasons for, 
466
error term, 96
error variance and, 97n5
estimated regression equation, 16
number, 69
order, 273, 274, 291n13, 294
outlier, 71
sampling distribution, 104
serial correlation, 273
OLS. See Ordinary Least Squares (OLS)
Omitted condition
defined, 80
dummy variables and, 82–83
Omitted variable bias
avoiding, 159n1
defined, 158
example, 162–163
expected, 161, 162–163, 162n4, 164
multicollinearity, 230–231
Omitted variables, 158–164
bias. See Omitted variable bias
consequences, 159–161
correcting for, 163–164
defined, 158
evidence, 158
heteroskedasticity, 312, 328
serial correlation, 280n1
One-sided critical values, 382
One-sided test
defined, 117
Durbin–Watson test, 287
t-test, 125, 129–133, 133
One-time dummy variable, 83
Online computer databases, 345
Orcutt, G. H., 293n14
Order, observation, 273, 274, 291n13, 
294
Order condition, 433–434
defined, 433
Ordered logit model, 406n9
Ordinary Least Squares (OLS), 35–57
bias, 418–421
Classical Assumptions, 92–99, 93n1
coefficients, 38, 38n3
defined, 36


546
index
Proportionality factor, defined, 310
Proxy variables, 346
PSID (U.S. Panel Survey of Income 
­Dynamics), 474
Publications, as data sources, 345
Pure heteroskedasticity, 307–311
defined, 307
Pure serial correlation, 275–278, 282, 
373
defined, 275
Quadratic functional form, 200, 201, 
200
Qualitative conditions, dummy 
­variables and, 203, 205
Quantitative research, nonexperimental, 
steps in, 4–5
Quasi-experiments. See Natural 
­experiments
Quigley, J., 359n6
R2, 50–52, 51
adjusted. See Adjusted R2
R 2, 54. See also Adjusted R2
R 2p, defined, 394
Ragan, James F., Jr., 439n13
Ramanathan, Ramu, 185n14
Ramsey, J. B., 185n15
Ramsey Regression Specification Error 
Test (RESET), 185–186
equations, 186, 186n16
Random assignment experiments, 
466–468
defined, 466
Random coefficient estimation, 105
Random component, regression 
­equation, 9
Random effects model, 483–484
defined, 483
fixed effects model vs., 484
Random error term. See Stochastic error 
term
Random fluctuations, 466
Random occurrences, 105
Random variation, stochastic error 
term, 9
Peron, Pierre, 380n15
Perry, Gregory, 217n9
Perry, John, 30n15
Petroleum consumption (data set), 
326–327
Pharmaceutical price discrimination 
(data set), 154
Philips, David, 468n2
Phillips, P. C. B., 186n18
Pindyck, Robert S., 399n4, 456n8, 
457n10
Plosser, C. I., 378n12
Polynomial functional form, 199–201, 
200, 201
defined, 199
Polynomials, 185
regression, 201
serial correlation, 280
Pooled cross sections across time, 
473n7
Populations. See also Sampling
testing limits on, 139
zero population means, 94, 94–95
Positive serial correlation, 278
defined, 276
Prais, S. J., 293n15
Prais–Winsten method, 293n15, 294, 
295
defined, 293
Precedence, 374–376
Predetermined variables, 428n9
defined, 413
Presidential election (data set), 463
Priors, regression equation and, 68
Probability, 96
Durbin–Watson test, 285n7
linear probability model, 390–397
Processes
autoregressive, 457–458
moving-average, 457–458
Properties
estimators, 106–107
mean, 102–103
OLS coefficient estimators, 107
Two-Stage Least Squares, 424–425
variances, 103–105


547
INDEX
research projects in. See Regression 
projects
sensitivity analysis, 352
single-equation linear, 5
models, 6–8
variations, 8, 8n6
Regression coefficients, 12
double-log functions, 195, 195
estimated, weight/height example, 40
notation, 108
Regression equation
adjusted for degrees of freedom, 54
calculating degrees of freedom in, 70, 
70n3
estimated/estimating, 14–17, 72,  
78, 91
evaluating, 49–50, 72, 78, 91
“i” subscripts in, 13
order of, 14n8
Ordinary Least Squares estimate 
­validity and, 50–54
priors and, 68
quality of, 49–50
stochastic error term in, 9
“t” subscripts in, 14
order of, 14n8
weight guessing, 17–20
Regression lines
goodness-of-fit measures and,  
51, 52
slope, 22, 22
true and estimated, 16, 16–17
Regression projects
advanced data sources, 346–348
checklist, 353, 354–355, 355
data collection, 342–346
practical advice for, 348–352
running, 340–341
topic selection, 341–342
User’s Guide, 356, 357
writing, 352–353
Rejection, of null hypotheses, 117–119, 
120, 123–125
Rejection regions, 119, 120, 133, 135, 
287, 287
Research topics. See Topics
Random walk, defined, 378
Range of sample, functional forms and, 
207–209, 208
Rank condition, 433n11
Rao, Potluri, 167n6
RateMyProfessor.com, 28
ratings data set, 29
Ratio tests, 185n14
Rau, B. Bhaskara, 383n18
Ray, Subhash C., 334n20, 337
Rea, Samuel A., Jr., 409n11
Redefining variables, 321–324,  
323–324
Reduced-form coefficients, 417
Reduced-form equations, 416–417
defined, 416
Redundant variables, 236–238
defined, 237
Regression. See also Regression analysis
autoregressive equations, 367, 378
estimation, 288
Ordinary Least Squares technique 
for, 36
multivariate linear models, 12
polynomial, 201
SAT interactive regression learning 
exercise, 244–272
data set, 248–249
serial correlation and, 282n2
software packages, 319n10, 321, 
321n12
spurious, 56, 379
stepwise, 173n8
Regression analysis, 5–14
applied. See Applied regression 
­analysis
checklist, 354–355
Classical Assumptions, 92–99
defined, 5
example, 17–20
exercise (econometric lab), 63–64
housing prices, 20–23, 22
linear, 193, 194
multivariate coefficients, 12
notation extension, 11–14
practical tips, 350–351


548
INDEX
Sampling distribution
βn, 100–105, 103, 104
simultaneity bias and, 421
Samuelson, Paul A., 1n1
Sanford, Douglas, 28n13
Sastri, V. K., 216, 216n7
SAT interactive regression learning 
­exercise, 244–272
data set for, 248–249
Saunders, Edward M., Jr., 110n9
SC (Schwarz Criterion), 187n19
Schut, Frederick T., 152, 152n16, 153, 
154, 183n13
Schwarz, G., 187n19
Schwarz Criterion (SC), 187n19
Searches. See Specification searches
Seasonal dummies, 146–147
defined, 146
Seasonally-based serial correlation, 276
SE(βn), 105
Second-degree (quadratic) polynomial 
equations, 200, 200, 201
Second-order serial correlation, 277, 
289n10
Sego, Bob, 246n7
Selection
critical values, 130
functional form, 201, 201
independent variables, 157–158.  
See also Independent variables
applied regression analysis, 67–68, 
74–75, 90
level of significance, t-test, 126–127
Semilog
left, 199, 208
right, 199, 208
Semilog functional form, 196–199, 
198, 201
defined, 196
Sensitivity analysis, 72, 177
defined, 174
Sequences, time-series models, 384–385
Sequential binary logit, defined, 406
Sequential specification searches, 
170–171
defined, 170
RESET (Ramsey Regression ­Specification 
Error Test), 185–186
equations, 186, 186n16
Residual analysis, 164
Residual sum of squares (RSS), 48–49, 
48n6, 143, 145, 145n13
defined, 48
Residuals
defined, 15
estimated regression equation, 16
heteroskedasticity, 314, 315,  
316–318, 322
Ordinary Least Squares estimate and, 
36–37
serial correlation, 280n1
Restaurant locations. See Woody’s 
­restaurant locations example
Results, documenting, 72–73, 78–79, 
91
Rezende, Leonardo, 88, 88n12,  
182n12
Rho (ρ), 275–277
Right-hand-side variables, 3n3
Right-side semilog, 199, 208
RMSE (root mean square error 
­criterion), defined, 446
Roe, Brian E., 217, 217n9
Romley, John, 409n12
Root mean square error criterion 
(RMSE), defined, 446
Ross, Douglas, 28n13
Rounding errors, 39
RSS (residual sum of squares), 48–49, 
48n6, 143, 145, 145n13
defined, 48
Rubinfeld, Daniel I., 399n4, 456n8, 
457n10
Rules. See Decision rules
Rush, Racelle, 150n15
Salon haircuts (data set), 488
Sample range, incorrect functional 
forms and, 207–209, 208
Samples
increasing size of, 238
non-random, 467–468


549
INDEX
Simons, James, 368n2
Simple correlation coefficients,  
232–233, 232n3, 233n4
defined, 232
Simple lags, 365
Simulation, forecasting in, 456
Simultaneity bias, 418–419
defined, 418
example, 419–420, 421
sampling distribution, 421
Simultaneous equation models, 449, 
454–456
Simultaneous equations, 3n3, 411–412
bias of Ordinary Least Squares, 
418–421
Classical Assumptions and, 415, 416
identification problem, 430–434
reduced-form, 416–417
structural, 413
systems, nature of, 412–417
Two-Stage Least Squares, 421–429
Single-equation linear regression 
­analysis, 5
models, 6–8
Single-independent-variable models, 
estimating with OLS, 35–40
Six steps in applied regression analysis,  
defined, 66. See also Applied 
­regression analysis, steps in
Slope coefficient (β1), 7–8, 69–70, 71
defined, 7
hypothesizing expected signs of, 
68–69, 69n2, 75, 90
Slope dummy
defined, 204
variables, 203–206, 205
Slopes
regression line, 22, 22
slope and intercept dummies, 205
Small macromodel (data set), 426
Software. See also EViews; Stata
Durbin–Watson statistic, 288
heteroskedasticity and, 319n10, 321, 
321n12
for OLS estimation of multivariate 
regression models, 43
Serial correlation
bias in dynamic models, 371–374
chi-square tests in, 373
Classical Assumptions, 273, 275, 282, 
371–372
consequences, 281–284
corrections, 373–374
detection of, 284–291
Durbin–Watson test, 284–289
dynamic models and, 371–374
equations, 371
error terms, 371–372
observation of, 96
exercise (econometric lab), 303–305
first-order. See First-order serial 
­correlation
forecasting, 449, 451–452
Generalized Least Squares, 292–295
hypothesis testing, 283–284
impure, 278–281, 279, 281, 365, 373
Lagrange Multiplier test, 372–373
negative, 276, 279
Newey–West standard errors, 295–296
no (absent), 278
Ordinary Least Squares, 292–295
positive, 276, 278, 287
pure, 275–278, 282, 373
remedies for, 291–296
seasonally-based, 276
second-order, 277, 289n10
statistics, 283n3
t-scores, 283–284, 296
testing for, 284–291
in dynamic models, 372–373
unreliability, 283n3
values, 280n1
Severe multicollinearity, 227, 366, 370
remedies for, 235–238
Shifting demand curve, 432
Shifting supply curve, 431, 432
Shiller, Robert J., 444n2
Sign, unexpected vs. expected, 348–349
Significance
F-test, 144–146, 144n12
level. See Level of significance, t-test
Silva, Fabio, 26n12


550
INDEX
Standard deviations, 107
error terms, notation for, 108
estimated coefficient terms, notation 
for, 108
Standard econometric notation,  
107–108, 108
Standard errors
border values and, 130n8
coefficients, 72, 73n4, 78, 78n7, 97, 
97n5
estimated, 78, 78n7
confidence level and, 126
data mining and, 173
heteroskedasticity and, 313–314, 
314n4
heteroskedasticity-corrected, 321, 
323n11
Newey–West. See Newey–West 
­standard errors
SE(βn), 105
White, 321n12
Standard Normal Distribution, 99
Stanford University Durbin–Watson 
tables, 289n10
Stata, 72
Durbin–Watson test, 288, 289n10
Lagrange Multiplier test, 289n11
p-value, 127n5
Prais–Winsten method, 294, 294n16
Ramsey Regression Specification Error 
Test, 185, 185n17
specification exercise, 217
terminology used by, 145n13
using, 30–34
Woody’s restaurant data set from, 
76–77
Stationarity, definitions of, 377n11
Stationary
defined, 377
time series, 377, 458
Statistical Abstract of the United States, 
345n2
Statistics
Durbin–Watson test. See  
­Durbin–Watson statistic
heteroskedasticity, 313n3
Sonstelle, Jon, 26n12
Sources, for project data, 345
advanced sources, 346–348
Soviet defense spending (data set), 301
Specification
bias, 158
criteria. See Specification criteria
defined, 67
errors, 157–158
exercise (econometric lab), 217–220
heteroskedasticity, 307
models, 67–68, 74–75, 90
multicollinearity, 228
omitted variable bias and, 158
searches. See Specification searches
Specification criteria, 166–167,  
185–188
Akaike’s Information Criterion, 
187–188
Bayesian Information Criterion, 
187–188
definitions, 166
misuse, 167–169
Ramsey’s Regression Specification 
Error Test, 185–186
Schwarz Criterion, 187–188
use cautions, 184
Specification errors, 157–158
definitions, 68, 157
Specification searches, 169–174
best practices, 170
bias, causes of, 171–172
data mining, 172–173
sensitivity analysis, 174
sequential, 170–171
Spurious correlation, 376–385
cointegration, 382–384
defined, 376
Dickey–Fuller test, 382–384
nonstationarity and, 376–385
spurious regression and, 379
time series, 377–378
sequence of steps for dealing with, 
384–385
Spurious regression, 56, 379
Srinivasan, T. N., 186n18


551
INDEX
t-scores, 126, 167, 168
multicollinearity, 227–228, 235–236
serial correlation, 283–284, 296
t-statistic, 121–123
defined, 121
“t” subscript, in regression equation, 14
order of, 14n8
t-test, 121–139
bias, 171–172
confidence intervals, 139–142
confidence level, 126–127
decision rules, 123–125
estimated logit coefficients, 400n6
examples, 129–136
“importance” and, 138–139
level of significance, choosing,  
126–127
limitations, 137–139
null hypothesis border, 122
one-sided, 125
examples, 129–133, 133
p-values and, 127–128
population, limits on, 139
specification criteria, 166
independent variable selection 
­example, 177
misuse example, 168
specification search bias and, 171–172
t-statistic, 121–123
theoretical validity, 137–138
two-sided, 125
examples, 134–136, 135
t-value, 78, 78n7
critical, t-test and, 119, 123–125, 130, 
132, 133, 135
estimating, 130–131
Tan, Alexander, 389, 389n21
Terza, Joseph V., 113n10
Tests/testing
Breusch–Godfrey, 289n11
Breusch–Pagan, 316–318, 320
chi-square. See Chi-square test
Dickey–Fuller, 382–384
Durbin–Watson. See Durbin–Watson 
test
errors, 118–119
serial correlation, 283n3
t-tests, 121–123
Steigerwald, Doug, 482n12
Stepwise regression, 173n8
Stochastic component, regression 
­equation, 9
Stochastic error terms, 94, 94–95,  
95n2, 96
components, 8–11
defined, 8
notation, 108
omitted variables, 159
Stock, J., 424n6
Stock, James, 333, 333n18, 428n9
Stock prices
data set, 212–213
forecasting and, 447, 447–449
Stone, J. H., 190n1
Stone, J. R., 1n1
Stone, Joe, 461n14, 462n15, 463
Structural coefficients, 413
Structural equations, defined, 413
Student consumption (data set), 229
Subscripts, order of, 14n8
Sum of squares
explained, 48–49
residual, 48–49, 48n6
total, 47, 49
Summation symbol (Σ), 36n1
Durbin–Watson test, 284–285,  
285n6
Ordinary Least Squares and, 36, 38
Summed squared residuals, 37, 38, 
42–43
Summers, Lawrence H., 172n7
Supply and demand models, 414, 416, 
437–438
Surveys
administration, 473n7
best practices, 347n4
regression project, 347
Symbols, used for stochastic error term, 
8–9
t-distribution, estimated logit 
­coefficients, 400n6


552
INDEX
Timmerman, A. G., 444n3
Tissot, B., 444n3
Tolerance, 235
Topics
data types for, 343–345. See also Data 
collection
selecting for regression projects, 
341–342
potential sources, 342
Total sum of squares (TSS), 49, 207
defined, 47
Transformations, Y, 206–207
Treatment groups, 465–472, 472
defined, 466
Trends, Durbin–Watson test, 285n7
True, defined, 15n9
True relationships, between variables, 16
TSS (total sum of squares), 49, 207
defined, 47
Tukey, John, 160n2
Two-sided test
defined, 117
t-test, 125
examples of, 134–136, 135
Two-Stage Least Squares (2SLS),  
421–429
defined, 422
example, 425–429
explained, 422–424
identification problem, 430–434
instrumental variables, 421–422
naive linear Keynesian macroeco-
nomic model, 425–429, 427n7
order condition, 433–434
properties of, 424–425
simultaneity bias and, 422
simultaneous equations and, 411
Two-tailed test, 117
2SLS. See Two-Stage Least Squares 
(2SLS)
Type I Errors, 118–119
border values and, 130n8
critical t-values, 123
data mining and, 173
defined, 118
level of significance and, 126
Tests/testing (continued)
F-test, 142–147, 376, 376n10
Granger causality, 374–376
Hausman, 484
for heteroskedasticity, 314–320
hypothesis. See Hypothesis testing
“importance” and, 138–139
Lagrange Multiplier. See Lagrange 
Multiplier (LM) test
likelihood ratio, 185n14
null hypotheses and, 155–156
one-sided, 117
Park, 317n8
population, limits on, 139
Ramsey Regression Specification Error 
Test, 185–186
ratios, 185n14
for serial correlation in dynamic 
models, 372–373
t-test, 121–139. See also t-test
unreliability, serial correlation and, 
283n3
White. See White test
Theoretical models, in applied regres-
sion analysis, developing, 66–67, 
74, 89–90
Theoretical validity, 137–138
Theory, specification criteria, 166
independent variable selection 
­example, 177
misuse example, 168
Time lags, 412n1
variables, 202–203, 413, 416, 423
Time series, 14
nonstationary, 377–378
stationary, 377–378
studies, 274–275
Time-series models, 364–365
dynamic models, 367–371
Granger causality, 374–376
heteroskedasticity in, 311
sequences, 384–385
serial correlation and dynamic 
­models, 371–374
spurious correlation, 376–385
stationary, 458


553
INDEX
Variables
bias, 171–172
dependent. See Dependent variables
dominant, 224
dropping, 162n4, 164, 170, 171
dummy. See Dummy variables
endogenous, 412–413
errors in the, 440–442
exogenous, 412–413
explanatory. See Independent variables
functional (mathematical) form of, 
67–68, 74–75, 90
independent. See Independent variables
instrumental, 421–422, 442
irrelevant, 165–167
linear in the, 192–193
movement of, 6
multicollinearity, 222n1
omitted. See Omitted variables
predetermined, 413
proxy, 346
random walk, 378
redefining, 321–324, 323–324
redundant, 236–238
relationship between, 412–413
right-hand-side, 3n3
single-independent-variable models, 
OLS and, 35–40
slope dummy, 203–206, 205
true relationships between, 16
units of measurement of, 70
Variance
coefficient estimators
notation for, 108
properties, 107
constant, 96–98, 97, 306
decomposition of, 47, 48
error terms, notation for, 108
heteroskedasticity, 307, 309–310
multicollinearity, 226–227, 227
properties, 103–105
Variance inflation factor (VIF),  
233–235, 233n5, 235n6
defined, 234
Variation. See Errors
Veal, M. R., 393n2
Type II Errors, 118–119
defined, 118
level of significance and, 126
Unbiased estimators, 101, 102n7,  
106, 107
defined, 102
Unboundedness, 397–400
Unconditional forecast, defined, 450
Unexpected sign, in regression analysis, 
handling, 348–350
Unit root, defined, 378
Units of measurement, of the variables, 
70–71
Unknown Xs, 449, 450–451
Unobservable heterogeneity, 468
U.S. economy (1945–2014),  
applied regression analysis  
(econometric lab), 89–91
U.S. News and World Report, 60n10
U.S. Panel Survey of Income Dynamics 
(PSID), 474
User’s Guides, regression projects,  
356, 357
Validity
estimates, 49–50
theoretical, 137–138
Values
borders, 130n8
critical, 119
for chi-square test, 327
for Dickey–Fuller test, 382,  
382n17
selecting, 130
t-value. See under Critical values
current, 364
double-log functions, 195, 195
expected, 9
F-value, 143, 145, 145n14
lagged, 364
p-values, 127–128
serial correlation, 280n1
t-values, 130. See also Critical t-values
VanBergeijk, Peter A. G., 152, 152n16, 
153, 154, 183n13


554
INDEX
Woody’s restaurant locations example, 
73–79
critical t-test values, 124, 125
data set from Stata, 76–77
data source for, 73n6
heteroskedasticity, 317–318, 320
irrelevant variables and, 165–166
omitted variable bias, 162
p-value, 128
two-sided t-test, 135
Wooldridge, Jeffrey M., 186n18, 401n7, 
473n7
Writing, regression projects, 352–353
Wunnava, P., 484n14
X variables
simultaneous equations and,  
412–413
unknown, 449, 450–451
X,Y coordinate system, 69, 70
mathematical vs. statistical fit in, 
69–70, 70, 71
Y variables
simultaneous equations and,  
412–413, 423
transformations, 206–207
variations
additional, 8, 8n6
sources, 8, 9
Yogo, M., 424n6
Zimmerman, K. F., 393n2
VIF (variance inflation factor),  
233–235, 233n5, 235n6
defined, 234
Vigen, Tyler, 55n7
Vinod, H. D., 290n12
Visco, Ignazio, 164n5
Ward, Michael, 375n9
Watson, G. S., 284n4
Watson, Mark, 333, 333n18, 428n9
Weak stationarity, 377n11
Weight-guessing equation, 20
forecasting and, 444–445
using height data, 17–18, 19
Weight/height data
estimated regression coefficients, 40
regression analysis (econometric lab), 
63–64
weight-guessing equation using, 
17–18, 19
Weighted Least Squares (WLS), 323n11, 
323n13
Weighting schemes, geometric, 369
West, K. D., 295n17
White, Halbert, 107n8, 318n9, 321
White standard errors, 321n12
White test, 290n12, 318–320, 321
alternative form, 320n11
defined, 318
Wide distribution, 308, 309
Wide-sense stationarity, 377n11
Winsten, C. B., 293n15
WLS (Weighted Least Squares), 323n11, 
323n13
Women’s participation in labor force 
(data set), 396


This page intentionally left blank


This page intentionally left blank


This page intentionally left blank


This page intentionally left blank
