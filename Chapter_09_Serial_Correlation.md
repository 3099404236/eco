# Chapter 9: Serial Correlation

**Pages:** 293-325

---

273
9.1  Time Series
9.2  Pure versus Impure Serial Correlation
9.3  The Consequences of Serial Correlation
9.4  The Detection of Serial Correlation
9.5  Remedies for Serial Correlation
9.6  Summary and Exercises
9.7 Appendix: Econometric Lab #5
Serial Correlation
In the next two chapters we’ll investigate the final component of the specifi-
cation of a regression equation—choosing the correct form of the stochastic 
error term. Our first topic, serial correlation, is the violation of Classical 
Assumption IV that different observations of the error term are uncorrelated 
with each other. Serial correlation, also called autocorrelation, can exist in 
any research study in which the order of the observations has some meaning 
and occurs most frequently in time-series data sets. In essence, serial correla-
tion implies that the value of the error term from one time period depends 
in some systematic way on the value of the error term in other time periods. 
Since time-series data are used in many applications of econometrics, it’s 
important to understand serial correlation and its consequences for OLS 
estimators.
The approach of this chapter to the problem of serial correlation will be 
similar to that used in the previous chapter. We’ll attempt to answer the same 
four questions:
1.	 What is the nature of the problem?
2.	 What are the consequences of the problem?
3.	 How is the problem diagnosed?
4.	 What remedies for the problem are available?
Chapter 9


274
Chapter 9  Serial Correlation
9.1   Time Series
Virtually every equation in the text so far has been cross-sectional in nature, 
but that’s going to change dramatically in this chapter. As a result, it’s probably 
worthwhile to talk about some of the characteristics of time-series equations.
Time-series data involve a single entity (like a person, corporation, or state) 
over multiple points in time. Such a time-series approach allows researchers 
to investigate analytical issues that can’t be examined very easily with a cross-
sectional regression. For example, macroeconomic models and supply-and-
demand models are best studied using time-series, not cross-sectional, data.
The notation for a time-series study is different from that for a cross-
sectional one. Our familiar cross-sectional notation (for one time period and 
N different entities) is:
Yi = β0 + β1X1i + β2X2i + β3X3i + ei
	
where  i  goes from 1 to N.
A time-series regression has one entity and T different time periods, however, 
so we’ll switch to this notation:
Yt = β0 + β1X1t + β2X2t + β3X3t + et
where  t  goes from 1 to T.
Thus:
Y1 = β0 + β1X11 + β2X21 + β3X31 + e1  refers to observations from the first 
time period
Y2 = β0 + β1X12 + β2X22 + β3X32 + e2  refers to observations from the ­second 
time period
	
g
YT = β0 + β1X1T + β2X2T + β3X3T + eT  refers to observations from the Tth 
time period
What’s so tough about that, you say? All we’ve done is change from i to t 
and change from N to T. Well, it turns out that time-series studies have some 
characteristics that make them more difficult to deal with than cross-sections:
1.	 The order of observations in a time series is fixed. With a cross-sectional data 
set, you can enter the observations in any order you want, but with time-
series data, you must keep the observations in chronological order.
2.	 Time-series samples tend to be much smaller than cross-sectional ones. Most 
time-series populations have many fewer potential observations than 
do cross-sectional ones, and these smaller data sets make statistical 
inference more difficult. In addition, it’s much harder to generate a 


275
  Pure versus Impure Serial Correlation
time-series observation than a cross-sectional one. After all, it takes a 
year to get one more observation in an annual time series!
3.	 The theory underlying time-series analysis can be quite complex. In part 
because of the problems mentioned above, time-series econometrics 
includes a number of complex topics that require advanced estimation 
techniques. We’ll tackle these topics in Chapters 12, 14, and 15.
4.	 The stochastic error term in a time-series equation is often affected by events 
that took place in a previous time period. This is serial correlation, the 
topic of our chapter, so let’s get started!
9.2   Pure versus Impure Serial Correlation
Pure Serial Correlation
Pure serial correlation occurs when Classical Assumption IV, which 
assumes uncorrelated observations of the error term, is violated in a correctly 
specified equation. If there is correlation between observations of the error 
term, then the error term is said to be serially correlated. When econometri-
cians use the term serial correlation without any modifier, they are referring 
to pure serial correlation.
The most commonly assumed kind of serial correlation is first-order 
serial correlation, in which the current value of the error term is a function 
of the previous value of the error term:
	
et = ρet-1 + ut	
(9.1)
where:  e = the error term of the equation in question
	
ρ = the first-order autocorrelation coefficient
	
u = a classical (not serially correlated) error term
The functional form in Equation 9.1 is called a first-order Markov scheme. 
The new symbol, ρ (rho, pronounced “row”), called the first-order autocor-
relation coefficient, measures the functional relationship between the value 
of an observation of the error term and the value of the previous observation 
of the error term.
The magnitude of ρ indicates the strength of the serial correlation in an 
equation. If ρ is zero, then there is no serial correlation (because e would 
equal u, a classical error term). As ρ approaches 1 in absolute value, the 
value of the previous observation of the error term becomes more important 
in determining the current value of et, and a high degree of serial correlation 
exists. For ρ to be greater than 1 in absolute value is unreasonable because 


276
Chapter 9  Serial Correlation
it implies that the error term has a tendency to continually increase in abso-
lute value over time (“explode”). As a result of this, we can state that:
	
-1 6 ρ 6 +1	
(9.2)
The sign of ρ indicates the nature of the serial correlation in an equation. 
A positive value for ρ implies that the error term tends to have the same sign 
from one time period to the next; this is called positive serial correlation. 
Such a tendency means that if et happens by chance to take on a large value 
in one time period, subsequent observations would tend to retain a portion 
of this original large value and would have the same sign as the original. 
For example, in time-series models, the effects of a large external shock to 
an economy (like an earthquake) in one period may linger for several time 
periods. The error term will tend to be positive for a number of observations, 
then negative for several more, and then back positive again.
Figure 9.1 shows two different examples of positive serial correlation. 
The error term observations plotted in Figure 9.1 are arranged in chrono-
logical order, with the first observation being the first period for which data 
are available, the second being the second, and so on. To see the difference 
between error terms with and without positive serial correlation, compare 
the patterns in Figure 9.1 with the depiction of no serial correlation 1ρ = 02 
in Figure 9.2.
A negative value of ρ implies that the error term has a tendency to switch 
signs from negative to positive and back again in consecutive observations; 
this is called negative serial correlation. It implies that there is some sort 
of cycle (like a pendulum) behind the drawing of stochastic disturbances. 
Figure 9.3 shows two different examples of negative serial correlation. For 
instance, negative serial correlation might exist in the error term of an 
equation that is in first differences because changes in a variable often fol-
low a cyclical pattern. In most time-series applications, however, negative 
pure serial correlation is much less likely than positive pure serial correla-
tion. As a result, most econometricians analyzing pure serial correlation 
concern themselves primarily with positive serial correlation.
Serial correlation can take on many forms other than first-order serial cor-
relation. For example, in a quarterly model, the current quarter’s error term 
observation may be functionally related to the observation of the error term 
from the same quarter in the previous year. This is called seasonally based serial 
correlation:
	
et = ρet-4 + ut


277
  Pure versus Impure Serial Correlation
Similarly, it is possible that the error term in an equation might be a function 
of more than one previous observation of the error term:
	
et = ρ1et-1 + ρ2et-2 + ut
Such a formulation is called second-order serial correlation.
2
1
0
Time
e
2
1
0
Time
e
Figure 9.1  Positive Serial Correlation
With positive first-order serial correlation, the current observation of the error term 
tends to have the same sign as the previous observation of the error term. An example  
of positive serial correlation would be external shocks to an economy that take more 
than one time period to completely work through the system.


278
Chapter 9  Serial Correlation
Impure Serial Correlation
By impure serial correlation we mean serial correlation that is caused by 
a specification error such as an omitted variable or an incorrect functional 
form. While pure serial correlation is caused by the underlying distribution 
of the error term of the true specification of an equation (which cannot be 
changed by the researcher), impure serial correlation is caused by a specifica-
tion error that often can be corrected.
How is it possible for a specification error to cause serial correlation? 
Recall that the error term can be thought of as the effect of omitted variables, 
nonlinearities, measurement errors, and pure stochastic disturbances on the 
dependent variable. This means, for example, that if we omit a relevant vari-
able or use the wrong functional form, then the portion of that omitted effect 
that cannot be represented by the included explanatory variables must be 
absorbed by the error term. The error term for an incorrectly specified equa-
tion thus includes a portion of the effect of any omitted variables and/or a 
portion of the effect of the difference between the proper functional form 
and the one chosen by the researcher. This new error term might be serially 
correlated even if the true one is not. If this is the case, the serial correlation 
has been caused by the researcher’s choice of a specification and not by the 
pure error term associated with the correct specification.
As you’ll see in Section 9.5, the proper remedy for serial correlation 
depends on whether the serial correlation is likely to be pure or impure. Not 
2
1
0
Time
e
Figure 9.2  No Serial Correlation
With no serial correlation, different observations of the error term are completely 
­uncorrelated with each other. Such error terms would conform to Classical Assumption IV.


279
  Pure versus Impure Serial Correlation
surprisingly, the best remedy for impure serial correlation is to attempt to 
find the omitted variable (or at least a good proxy) or the correct functional 
form for the equation. Both the bias and the impure serial correlation will 
disappear if the specification error is corrected. As a result, most econometri-
cians try to make sure they have the best specification possible before they 
spend too much time worrying about pure serial correlation.
2
1
0
Time
e
2
1
0
Time
e
Figure 9.3  Negative Serial Correlation
With negative first-order serial correlation, the current observation of the error term 
tends to have the opposite sign from the previous observation of the error term. In most 
time-series applications, negative serial correlation is much less likely than positive 
­serial correlation.


280
Chapter 9  Serial Correlation
To see how an omitted variable can cause the error term to be serially 
­correlated, suppose that the true equation is:
	
Yt = β0 + β1X1t + β2X2t + et	
(9.3)
where et is a classical error term. As shown in Section 6.1, if X2 is accidentally 
omitted from the equation (or if data for X2 are unavailable), then:
	
Yt = β0 + β1X1t + e*t  where  e*t = β2X2t + et	
(9.4)
Thus, the error term in the omitted variable case is not the classical error 
term e. Instead, it’s also a function of one of the independent variables, X2. As 
a result, the new error term, e*, can be serially correlated even if the true error 
term e is not. In particular, the new error term e* will tend to exhibit detect-
able serial correlation when:
1.	 X2 itself is serially correlated (this is quite likely in a time series) and
2.	 the size of e is small1 compared to the size of β2X2.
These tendencies hold even if there are a number of included and/or omitted 
variables. Therefore:
	
e*t = ρe*t-1 + ut	
(9.5)
Another common kind of impure serial correlation is caused by an incor-
rect functional form. Here, the choice of the wrong functional form can cause 
the error term to be serially correlated. Let’s suppose that the true equation is 
polynomial in nature:
	
Yt = β0 + β1X1t + β2X2
1t + et	
(9.6)
but that instead a linear regression is run:
	
Yt = α0 + α1X1t + e*t 	
(9.7)
The new error term e* is now a function of the true error term e and of the 
differences between the linear and the polynomial functional forms. As can 
be seen in Figure 9.4, these differences often follow fairly autoregressive pat-
terns. That is, positive differences tend to be followed by positive differences, 
and negative differences tend to be followed by negative differences. As a 
1. If typical values of e are significantly larger in absolute size than β2X2, then even a serially 
correlated omitted variable (X2) will not change e* very much. In addition, recall that the omit-
ted variable, X2, will cause bias in the estimate of β1, depending on the correlation between the 
two Xs. If βn 1 is biased because of the omission of X2, then a portion of the β2X2 effect must have 
been absorbed by βn 1 and will not end up in the residuals. As a result, tests for serial correlation 
based on those residuals may give incorrect readings. Such residuals may leave misleading clues 
as to possible specification errors.


281
  The Consequences of Serial Correlation
result, using a linear functional form when a nonlinear one is appropriate 
will usually result in positive impure serial correlation.
9.3   The Consequences of Serial Correlation
The consequences of serial correlation are quite different in nature from the 
consequences of the problems discussed so far in this text. Omitted variables, 
irrelevant variables, and multicollinearity all have fairly recognizable external 
0
Y
X1
Y 5 b0 1 b1X1
0
e
1
2
X1
Figure 9.4  Incorrect Functional Form as a Source of Impure Serial Correlation
The use of an incorrect functional form tends to group positive and negative residuals 
together, causing positive impure serial correlation.


282
Chapter 9  Serial Correlation
symptoms. Each problem changes the estimated coefficients and standard 
errors in a particular way, and an examination of these changes (and the 
underlying theory) often provides enough information for the problem to 
be detected. As we shall see, serial correlation is more likely to have internal 
symptoms; it affects the estimated equation in a way that is not easily observ-
able from an examination of just the results themselves.
The existence of serial correlation in the error term of an equation violates 
Classical Assumption IV, and the estimation of the equation with OLS has at 
least three consequences:2
2. If the regression includes a lagged dependent variable as an independent variable, then the 
problems worsen significantly. For more on this topic (called a dynamic model), see Chapter 12.
	1.	 Pure serial correlation does not cause bias in the coefficient 
­estimates.
	2.	 Serial correlation causes OLS to no longer be the minimum variance 
estimator (of all the linear unbiased estimators).
	3.	 Serial correlation causes the OLS estimates of the SE1βn 2s to be 
­biased, leading to unreliable hypothesis testing.
1.	 Pure serial correlation does not cause bias in the coefficient estimates. If the 
error term is serially correlated, one of the assumptions of the Gauss–
Markov Theorem is violated, but this violation does not cause the coef-
ficient estimates to be biased. If the serial correlation is impure, however, 
bias may be introduced by the use of an incorrect specification.
This lack of bias does not necessarily mean that the OLS estimates 
of the coefficients of a serially correlated equation will be close to the 
true coefficient values. A single estimate observed in practice can come 
from a wide range of possible values. In addition, the standard errors of 
these estimates will typically be increased by the serial correlation. This 
increase will raise the probability that a βn will differ significantly from 
the true β value. What unbiased means in this case is that the distribu-
tion of the βns is still centered around the true β.
2.	 Serial correlation causes OLS to no longer be the minimum variance estimator 
(of all the linear unbiased estimators). Although the violation of Classical 
Assumption IV causes no bias, it does affect the other main conclusion 
of the Gauss–Markov Theorem, that of minimum variance. In particular, 


283
  The Consequences of Serial Correlation
we cannot prove that the distribution of the OLS βns is minimum vari-
ance (among the linear unbiased estimators) when Assumption IV is 
violated.
The serially correlated error term causes the dependent variable to 
fluctuate in a way that the OLS estimation procedure sometimes at-
tributes to the independent variables. Thus, OLS is more likely to mis-
estimate the true β in the face of serial correlation. On balance, the βns 
are still unbiased because overestimates are just as likely as underesti-
mates, but these errors increase the variance of the distribution of the 
estimates, increasing the amount that any given estimate is likely to dif-
fer from the true β.
3.	 Serial correlation causes the OLS estimates of the SE(bn)s to be biased, leading 
to unreliable hypothesis testing. With serial correlation, the OLS formula 
for the standard error produces biased estimates of the SE(βn)s. Because 
the SE(βn) is a prime component in the t-statistic, these biased SE(βn)s 
cause biased t-scores and unreliable hypothesis testing in general. In 
essence, serial correlation causes OLS to produce incorrect SE(βn)s and 
t-scores! Not surprisingly, most econometricians therefore are very hesi-
tant to put much faith in hypothesis tests that were conducted in the 
face of pure serial correlation.3
What sort of bias does serial correlation tend to cause? Typically, the 
bias in the estimate of SE(βn) is negative, meaning that OLS underes-
timates the size of the standard errors of the coefficients. This comes 
about because serial correlation usually results in a pattern of observa-
tions that allows a better fit than the actual (not serially correlated) 
observations would otherwise justify. This tendency of OLS to underes-
timate the SE(βn) means that OLS typically overestimates the t-scores of 
the estimated coefficients, since:
	
t =
1βn - βH02
SE1βn 2
	
(9.8)
Thus the t-scores printed out by a typical software regression package in 
the face of serial correlation are likely to be too high. Similarly, confi-
dence intervals for the coefficients will tend to be too narrow.
What will happen to hypothesis testing if OLS underestimates the SE(βn)s 
and therefore overestimates the t-scores? Well, the “too low” SE(βn) will cause 
3. While our discussion here involves the t-test, the same conclusion of unreliability in the face 
of serial correlation applies to all other test statistics.


284
Chapter 9  Serial Correlation
a “too high” t-score for a particular coefficient, and this will make it more 
likely that we will reject a null hypothesis (for example H0: β … 0) when it 
is in fact true. This increased chance of rejecting H0 means that we’re more 
likely to reject a true null hypothesis, so we’re more likely to make the mis-
take of keeping an irrelevant variable in an equation because its coefficient’s 
t-score has been overestimated. In other words, hypothesis testing becomes 
unreliable when we have pure serial correlation.
9.4   The Detection of Serial Correlation
How can we detect serial correlation? While the first indication of serial cor-
relation often occurs when we observe a pattern in the residuals similar to 
Figure 9.1, most econometricians rely on more formal tests like the Durbin–
Watson test and the Lagrange Multiplier test.
The Durbin–Watson Test
The Durbin–Watson test is used to determine if there is first-order serial 
correlation in the error term of an equation by examining the residuals of a 
particular estimation of that equation.4 It’s important to use the Durbin–
Watson test only when the assumptions that underlie its derivation are met:
1.	 The regression model includes an intercept term.
2.	 The serial correlation is first-order in nature:
	
et = ρet-1 + ut	
(9.9)
	
where ρ is the autocorrelation coefficient and u is a classical (normally 
distributed) error term.
3.	 The regression model does not include a lagged dependent variable 
(discussed in Chapter 12) as an independent variable.5
The equation for the Durbin–Watson statistic for T observations is:
	
d = a
T
2
1et - et-122n a
T
1
e2
t 	
(9.10)
4. J. Durbin and G. S. Watson, “Testing for Serial Correlation in Least-Squared Regression,” 
Biometrika, 1951, pp. 159–177.
5. In such a circumstance, the Durbin–Watson test is biased toward 2.


285
  The Detection of Serial Correlation
where the ets are the OLS residuals. Note that the numerator has one fewer 
observation than the denominator because an observation must be used 
to calculate et-1. The Durbin–Watson statistic equals 0 if there is extreme 
positive serial correlation, 2 if there is no serial correlation, and 4 if there is 
extreme negative serial correlation. To see this, let’s put appropriate residual 
values into Equation 9.10 for these three cases:
1.	 Extreme Positive Serial Correlation: d = 0
	
In this case, et = et-1, so 1et - et-12 = 0 and d = 0.
2.	 Extreme Negative Serial Correlation: d ≈4
	
In this case, et = -et-1, and 1et - et-12 = 12et2. Substituting into 
Equation 9.10, we obtain d = g 12et22/g 1et22 and d ≈4.
3.	 No Serial Correlation: d ≈2
	
When there is no serial correlation, the mean of the distribution of d 
is equal to 2.6 That is, if there is no serial correlation, d ≈2.
Using the Durbin–Watson Test
The Durbin–Watson test is unusual in two respects. First, econometricians 
almost never test the one-sided null hypothesis that there is negative serial 
correlation in the residuals because negative serial correlation, as mentioned 
previously, is quite difficult to explain theoretically in economic or business 
analysis. Its existence usually means that impure serial correlation has been 
caused by some specification error.
Second, the Durbin–Watson test is sometimes inconclusive. Whereas pre-
viously explained decision rules always have had only “acceptance” regions 
and rejection regions, the Durbin–Watson test has a third possibility, called 
the inconclusive region. For reasons outlined in Section 9.5, we do not rec-
ommend the application of a remedy for serial correlation if the Durbin–
Watson test is inconclusive.7
6. To see this, multiply out the numerator of Equation 9.10, obtaining
	
d = c a
T
2
e2
t - 2 a
T
2
1etet-12 + a
T
2
e2
t-1d n a
T
1
e2
t ≈c a
T
2
e2
t + a
T
2
e2
t-1d n a
T
1
e2
t ≈2	
(9.11)
If there is no serial correlation, then et and et-1 are not related, and, on average, g1etet-12 = 0.
7. This inconclusive region is troubling, but the development of exact Durbin–Watson tests may 
eliminate this problem in the future. Some computer programs allow the user the option of cal-
culating an exact Durbin–Watson probability (of first-order serial correlation). Alternatively, it’s 
worth noting that there is a growing trend toward the use of dU as a sole critical value. This trend 
runs counter to our view that if the Durbin–Watson test is inconclusive, then no remedial action 
should be taken except to search for a possible cause of impure serial correlation.


286
Chapter 9  Serial Correlation
With these exceptions, the use of the Durbin–Watson test is quite similar 
to the use of the t-test. To test for positive serial correlation, the following 
steps are required:
1.	 Obtain the OLS residuals from the equation to be tested and calculate 
the d statistic by using Equation 9.10.
2.	 Determine the sample size and the number of explanatory variables 
and then consult Statistical Table B-4 in Appendix B to find the upper 
critical d value, dU, and the lower critical d value, dL, respectively. In-
structions for the use of this table are also in that appendix.
3.	 Given the null hypothesis of no positive serial correlation and a one-
sided alternative hypothesis:
	
 H0: ρ … 0    (no positive serial correlation)
	
 HA: ρ 7 0    (positive serial correlation)	
(9.12)
	
the appropriate decision rule is:
 If d 6 dL  Reject H0
 If d 7 dU  Do not reject H0
 If dL … d … dU  Inconclusive
	
In rare circumstances, perhaps first differenced equations, a two-sided 
Durbin–Watson test might be appropriate. In such a case, steps 1 and 
2 are still used, but step 3 is now:
	
Given the null hypothesis of no serial correlation and a two-sided 
­alternative hypothesis:
	
 H0: ρ = 0    1no serial correlation2
	
 HA: ρ ≠0  
 1serial correlation2
	
(9.13)
	
the appropriate decision rule is:
 if d 6 dL   Reject H0
 if d 7 4 - dL   Reject H0
 if 4 - dU 7 d 7 dU   Do not reject H0
	
 otherwise  Inconclusive
Examples of the Use of the Durbin–Watson Statistic
Let’s work through some applications of the Durbin–Watson test. First, turn 
to Statistical Table B-4. Note that the upper and lower critical d values (dU 
and dL) depend on the number of explanatory variables (do not count the 
constant term), the sample size, and the level of significance of the test.


287
  The Detection of Serial Correlation
Now let’s set up a one-sided 5-percent test for a regression with three 
explanatory variables and 25 observations. As can be seen from 5-percent 
table B-4, the critical values are dL = 1.12 and dU = 1.66. As a result, if the 
hypotheses are:
 H0: ρ … 0   1no positive serial correlation2
 HA: ρ 7 0   1positive serial correlation2
the appropriate decision rule is:
	
 if d 6 1.12    Reject H0
	
 if d 7 1.66    Do not reject H0
	
 if 1.12 … d … 1.66    Inconclusive
A computed Durbin–Watson statistic of 1.78, for example, would indicate 
that there is no evidence of positive serial correlation, a value of 1.28 would 
be inconclusive, and a value of 0.60 would imply positive serial correlation. 
Figure 9.5 provides a graph of the “acceptance,” rejection, and inconclusive 
regions for this example.
For a real-world example, let’s look at a simple time-series model of the 
annual consumption of chicken in the United States. There are a variety of 
0
2
0.60
dU 5 1.66
dL 5 1.12
1.28
1.78
4
Inconclusive Region
dL , d , dU
Rejection Region
d , dL
“Acceptance” Region
dU , d
Positive Serial
Correlation
No Positive Serial
Correlation
Figure 9.5  An Example of a One-Sided Durbin–Watson Test
In a one-sided Durbin–Watson test for positive serial correlation, only values of d signif-
icantly below 2 cause the null hypothesis of no positive serial correlation to be rejected. 
In this example, a d of 1.78 would indicate no positive serial correlation, a d of 0.60 
would indicate positive serial correlation, and a d of 1.28 would be inconclusive.


288
Chapter 9  Serial Correlation
variables that might make sense in such an equation, and at least three vari-
ables seem obvious. We’d expect the demand for chicken to be a negative 
function of the price of chicken and a positive function of income and the 
price of a substitute (in this case, beef):
	
-	
+ 	
+
Yt = β0 + β1PCt + β2PBt + β3YDt + et
where:    Yt
 = per capita chicken consumption (in pounds) in year t
	
PCt = the price of chicken (in cents per pound) in year t
	
PBt  = the price of beef (in cents per pound) in year t
	
YDt = U.S. per capita disposable income (in hundreds of dollars) 
in year t
If we collect data for these variables for the years 1974 through 2002, we 
can estimate8 the following equation:
	
 Ynt = 27.7 - 0.11PCt + 0.03PBt + 0.23YDt	
	
10.032	
10.022	
10.012
	
t = 	
-3.38	
+1.86	
+15.7
	
R 2 = .9904 N = 29 1annual 1974–20022	
(9.14)
How does our estimated equation look? The overall fit of Equation 9.14 is 
excellent, and each of the individual regression coefficients is significantly dif-
ferent from zero in the expected direction. The price of chicken does indeed 
have a significant negative effect (holding the price of beef and disposable 
income constant), and the price of beef and disposable income do indeed 
have positive effects (holding the other independent variables constant).
However, this is a time-series equation, so if there’s serial correlation, 
hypothesis testing will be unreliable, and one or more of these t-scores could 
be artificially high. We’d better run a Durbin–Watson test!
When we calculate a Durbin–Watson statistic for Equation 9.14,9 we get 
0.99. Is that cause to be concerned about serial correlation? What would be 
the result of a one-sided 5-percent test of the null hypothesis of no positive 
serial correlation? Well, once we’ve got the Durbin–Watson statistic, the next 
8. The data for this equation are in dataset CHICK9. As we’ll see in Chapter 14, estimating 
an equation for the demand for chicken without taking into account the simultaneously 
­determined supply of chicken runs the risk of bias, particularly in the coefficient of the price of 
chicken.
9. Luckily, you don’t actually need to calculate the Durbin–Watson statistic yourself. Some 
econometric software programs, including EViews, calculate the Durbin–Watson statistic auto-
matically, while others, including Stata, allow you to do so quite simply. In Stata, for example, 
the command is estat dwatson.


289
  The Detection of Serial Correlation
step is to consult Statistical Table B-4. In that table, with K (the number of 
explanatory variables10) equal to 3 and N (the number of observations) equal 
to 29, we find that the critical d values are dL = 1.20 and dU = 1.65. (It’s 
probably a good idea to check these d values yourself to make sure that you 
know how to look them up.)
The decision rule would thus be:
	
 if d 6 1.20	
Reject H0
	
 if d 7 1.65	
Do not reject H0
	
 if 1.20 … d … 1.65	
Inconclusive
Since 0.99 is less than the critical lower limit of the d statistic, we would reject 
the null hypothesis of no positive serial correlation, and we would have to 
decide how to cope with that serial correlation.
The Lagrange Multiplier (LM) test
Unfortunately, the Durbin–Watson test has a number of limitations. As men-
tioned, it can be used only when the serial correlation is first-order, when a 
constant is included in the equation, and when the equation doesn’t include 
a lagged dependent variable. The Durbin–Watson test’s inconclusive region 
also is a drawback, particularly since the size of the inconclusive region 
increases as the number of independent variables increases.
A popular alternative to the Durbin–Watson test is the Lagrange Multi-
plier (LM) test, which checks for serial correlation by analyzing how well 
the lagged residuals explain the residual of the original equation in an equa-
tion that also includes all the explanatory variables of the original model. 
If the lagged residuals are significant in explaining this time’s residuals (as 
shown by the chi-square test), then we can reject the null hypothesis of no 
serial correlation.11 The LM serial correlation test is just one application of a 
10. Be careful! While we define K as the number of explanatory variables, some other sources, 
including Stata and the Stanford University Durbin–Watson tables, define K as the number of 
coefficients (which is equivalent to K + 1 in our notation). As long as you’re aware of this dif-
ference, it won’t cause you any problems. Incidentally, the Stanford tables, which are online at 
http://web.stanford.edu/~clint/bench/dwcrit.htm, have many more observations than can be 
printed in a textbook, so they’re quite useful if you have a large sample.
11. The Lagrange Multiplier test for serial correlation is sometimes referred to as the Breusch–
Godfrey test, which is why the Stata command for this test is estat bgodfrey, lag (1). Note that if 
we’re testing for first-order serial correlation, we need to specify that the lag equals 1. If we are 
concerned with second-order serial correlation, then the lag would equal 2, etc.


290
Chapter 9  Serial Correlation
general Lagrange Multiplier testing approach that can be applied to a variety 
of econometric problems.12
Using the Lagrange Multiplier (LM) test to investigate the possibility of 
serial correlation involves three steps:
1.	 Obtain the residuals from the estimated equation. For an equation 
with two independent variables, this would equal:
	
et = Yt - Ynt = Yt - βn 0 - βn 1X1t - βn 2X2t	
(9.15)
2.	 Use these residuals as the dependent variable in an auxiliary equation 
that includes as independent variables all those on the right-hand side 
of the original equation as well as the lagged residuals:
	
et = α0 + α1X1t + α2X2t + α3et-1 + ut	
(9.16)
3.	 Estimate Equation 9.16 using OLS and then test the null hypothesis 
that α3 = 0 with the following test statistic:
	
LM = NR2	
	
where N is the sample size and R2 is the unadjusted coefficient of de-
termination, both of the auxiliary equation, Equation 9.16. 
For large samples, LM has a chi-square distribution with degrees of freedom 
equal to one (the number of restrictions in the null hypothesis). If LM is 
greater than the critical chi-square value from Statistical Table B-6, then we 
reject the null hypothesis that α3 = 0 and conclude that there is serial corre-
lation in the original equation. Note that even though α3 tends to be positive 
in economic examples, this is a two-sided test.
An Example of the Lagrange Multiplier Test
As an example of the Lagrange Multiplier test, let’s run a 5-percent test for 
serial correlation on our chicken demand model, Equation 9.14. The appro-
priate LM equation to run is:
	
et = α0 + α1PCt + α2PBt + α3YDt + α4et-1 + ut	
(9.17)
where et is the residual from Equation 9.14, the equation that we’re testing 
for serial correlation.
12. For example, the White test for heteroskedasticity (to be explained in Section 10.3) also is 
an application of the Lagrange Multiplier approach. For a survey of the various uses to which 
Lagrange Multiplier tests can be put, see Rob Engle, “Wald, Likelihood Ratio, and Lagrange 
Multiplier Tests in Econometrics,” in Z. Griliches and M. D. Intrilligator (eds.), Handbook of 
Econometrics, Vol. II (Amsterdam, Elsevier Science Publishers, 1984).


291
  Remedies for Serial Correlation
Since there are three independent variables, the null hypothesis becomes 
H0: α4 = 0. If we estimate Equation 9.17, we get an R2 of .291. Since the 
sample size is 29, this means that:
	
LM = NR2 = 8.439
The decision rule is to reject the null hypothesis if NR2 is greater than the crit-
ical chi-square value with 1 degree of freedom, so the next step is to consult 
Table B-6 and look up the critical value. As you can see if you take a look at 
Table B-6, the 5-percent chi-square critical value with 1 degree of freedom is 
3.84. Since 8.439 7 3.84, we can reject the null hypothesis and conclude that 
we have serial correlation in the chicken demand model. This is a two-sided 
test, but it confirms the result of our one-sided Durbin–Watson test. It seems 
clear that the chicken demand equation has serial correlation!
9.5   Remedies for Serial Correlation
Suppose that the Durbin–Watson or LM test detects serial correlation in the 
residuals of your equation. Is there a remedy? Some students suggest reorder-
ing the observations of Y and the Xs to avoid serial correlation. They think 
that if this time’s error term appears to be affected by last time’s error term, 
why not reorder the data randomly to get rid of the problem? The answer is 
that the reordering of the data does not get rid of the serial correlation; it just 
makes the problem harder to detect. If e2 = f1e12 and we reorder the data, 
then the error term observations are still related to each other, but they now 
no longer follow each other, and it becomes almost impossible to discover 
the serial correlation. Interestingly, reordering the data changes the Durbin–
Watson statistic but does not change the estimates of the coefficients or their 
standard errors at all.13
13. This can be proven mathematically, but it is usually more instructive to estimate a regres-
sion yourself, change the order of the observations, and then reestimate the regression. See 
Exercise 3 at the end of the chapter.
The place to start in correcting a serial correlation problem is to look 
carefully at the specification of the equation for possible errors that 
might be causing impure serial correlation. Is the functional form cor-
rect? Are you sure that there are no omitted variables? Only after the 
specification of the equation has been reviewed carefully should the pos-
sibility of an adjustment for pure serial correlation be considered.


292
Chapter 9  Serial Correlation
It’s worth noting that if an omitted variable increases or decreases over time, 
as is often the case, or if the data set is logically reordered (say, according to the 
magnitude of one of the variables), then the Durbin–Watson or LM test can 
help detect impure serial correlation. A significant Durbin–Watson or LM test 
result can easily be caused by an omitted variable or an incorrect functional 
form. In such circumstances, the Durbin–Watson or LM tests do not distin-
guish between pure and impure serial correlation, but the detection of negative 
serial correlation is often a strong hint that the serial correlation is impure.
If you conclude that you have pure serial correlation, then the appropri-
ate response is to consider the application of Generalized Least Squares or 
Newey–West standard errors, as described in the following sections.
Generalized Least Squares
Generalized least squares (GLS) is a method of ridding an equation of 
pure first-order serial correlation and in the process restoring the minimum 
variance property to its estimation. GLS starts with an equation that does not 
meet the Classical Assumptions (due in this case to the pure serial correlation 
in the error term) and transforms it into one (Equation 9.22) that does meet 
those assumptions.
At this point, you could skip directly to Equation 9.22, but it’s easier to 
understand the GLS estimator if you examine the transformation from which 
it comes. Start with an equation that has first-order serial correlation:
	
Yt = β0 + β1X1t + et	
(9.18)
which, if et = ρet-1 + ut (due to pure serial correlation), also equals:
	
Yt = β0 + β1X1t + ρet-1 + ut	
(9.19)
where e is the serially correlated error term, ρ is the autocorrelation coeffi-
cient, and u is a classical (not serially correlated) error term.
If we could get the ρet-1 term out of Equation 9.19, the serial correlation 
would be gone, because the remaining portion of the error term (ut) has no 
serial correlation in it. To rid ρet-1 from Equation 9.19, multiply Equation 9.18 
by ρ and then lag the new equation by one time period, obtaining
	
ρYt-1 = ρβ0 + ρβ1X1t-1 + ρet-1	
(9.20)
Notice that we now have an equation with a ρet-1 term in it. If we now sub-
tract Equation 9.20 from Equation 9.19, the equivalent equation that remains 
no longer contains the serially correlated component of the error term:
	
Yt - ρYt-1 = β011 - ρ2 + β11X1t - ρX1t-12 + ut	
(9.21)


293
  Remedies for Serial Correlation
Equation 9.21 can be rewritten as:
	
Y t* = β0* + β1X1t* + ut	
(9.22)
where:	
 Y*t = Yt - ρYt-1
	
(9.23)
	
 X*1t = X1t - ρX1t-1
	
 β*0 = β0 - ρβ0
	
Equation 9.22 is called a Generalized Least Squares (or “quasi-differenced”) 
version of Equation 9.19. Notice that:
1.	 The error term is not serially correlated. As a result, OLS estimation of 
Equation 9.22 will be minimum variance. (This is true if we know ρ or 
if we accurately estimate ρ.)
2.	 The slope coefficient β1 is the same as the slope coefficient of the origi-
nal serially correlated equation, Equation 9.19. Thus coefficients esti-
mated with GLS have the same meaning as those estimated with OLS.
3.	 The dependent variable has changed compared to that in Equation 9.19. 
This means that the GLS R  2 is not necessarily comparable to the OLS R  2.
Unfortunately we can’t use OLS to estimate a Generalized Least Squares 
model because GLS equations are inherently nonlinear in the coefficients. To 
see why, take a look at Equation 9.21. We need to estimate values not only for 
β0 and β1 but also for ρ, and ρ is multiplied by β0 and β1 (which you can see 
if you multiply out the right-hand side of the equation). Since OLS requires 
that the equation be linear in the coefficients, we need a different estimation 
procedure.
Luckily, there are a number of techniques that can be used to estimate 
GLS equations. While the best-known of these is the Cochrane–Orcutt 
method,14 our recommendation is to use a slightly different approach, the 
Prais–Winsten method. The Prais–Winsten method15 is a two–step itera-
tive technique that rids an equation of serial correlation by first producing 
14. D. Cochrane and G. H. Orcutt, “Application of Least Squares Regression to Relationships Con-
taining Autocorrelated Error Terms,” Journal of the American Statistical Association, 1949, pp. 32–61.
15. S. J. Prais and C. B. Winsten, “Trend Estimators and Serial Correlation,” Cowles Commis-
sion Discussion Paper No. 383 (1954) Chicago. The Prais–Winsten method (sometimes called 
Yule–Walker) is very similar to Cochrane–Orcutt, but the Prais–Winsten estimate of ρ is more 
accurate because it uses the first observation in Step 1 while Cochrane–Orcutt does not. For 
more, see Masahito Kobayashi, “Comparison of Efficiencies of Several Estimators for Linear 
Regressions with Autocorrelated Errors,” Journal of the American Statistical Association, 1985, 
pp. 951–953.


294
Chapter 9  Serial Correlation
an estimate of ρ and then estimating the GLS equation using that ρn. The two 
steps are:
1.	 Estimate ρ by running a regression based on the residuals of the equa-
tion suspected of having serial correlation:
	
et = ρet-1 + ut	
(9.24)
	
where the ets are the OLS residuals from the equation suspected of hav-
ing pure serial correlation and ut is a classical (non-serially-correlated) 
error term.
2.	 Use this ρn to estimate the GLS equation by substituting ρn into Equa-
tion 9.21 and using OLS to estimate Equation 9.21 with the adjusted 
data.
These two steps are repeated (iterated) until further improvement results in 
little change in ρn. Once ρn has converged (usually in just a few iterations), the 
last estimate of step 2 is used as the final estimate of Equation 9.21.
Unfortunately, all methods of estimating GLS equations use iterative non-
linear regression techniques that are well beyond the scope of this text. As a 
result, most researchers rely on their econometric software packages to estimate 
their GLS equations for them. In Stata, for example, the Prais–Winsten method 
can be run using the command prais followed by a listing of the dependent 
and independent variables.16
Let’s apply Generalized Least Squares, using the Prais–Winsten method, to 
the chicken demand example that was found to have serial correlation in the 
previous section. Recall that we estimated the per capita demand for chicken 
as a function of the price of chicken, the price of beef, and disposable income:
	
 Ynt = 27.7 - 0.11PCt + 0.03PBt + 0.23YDt
	
10.032	
10.022	
10.012
	
t = -3.38	
+ 1.86	
+15.7
	
 R  2 =  .9904 N =  29 DW =  0.99	
(9.14)
Note that we have added the Durbin–Watson statistic to the documenta-
tion with the notation DW. All future time-series results will include the DW 
statistic, but cross-sectional documentation of the DW is not required unless 
the observations are ordered in some meaningful manner (like smallest to 
largest or youngest to oldest).
16. In Stata, the command to apply GLS (using Prais–Winsten) to Equation 9.14 thus would be 
prais Y PC PB YD. In EViews, the easiest way to estimate a GLS equation is to add AR(1) to the 
equation as an independent variable, as in: LS Y C PC PB YD AR(1). The result is a GLS estimate 
where ρn will appear as the estimated coefficient of the variable AR(1).


295
  Remedies for Serial Correlation
If we reestimate Equation 9.14 with the Prais–Winsten approach to GLS, 
we obtain:
	
 Yt = 28.5 - 0.08PCt + 0.016PBt + 0.24YDt
	
10.042	
10.0212	
10.022
	
t = - 2.13	
+ 0.74	
+13.12
	
 R  2 = .963 N = 29 ρn = 0.56	
(9.25)
Let’s compare Equations 9.14 and 9.25. Note that the ρn used in Equation 9.25 
is 0.56. This means that Y was actually run as Y* = Yt - 0.56Yt-1, PC as 
PC* = PCt - 0.56PCt-1, etc. Second, ρn replaces DW in the documentation of 
GLS estimates in part because the DW of Equation 9.25 isn’t strictly compa-
rable to non-GLS DWs (it is biased toward 2).
Generalized Least Squares estimates, no matter how they are produced, 
have at least two problems. First, even though serial correlation causes no 
bias in the estimates of the βns, the GLS estimates usually are different from 
the OLS ones. For example, note that all three slope coefficients change as 
we move from OLS in Equation 9.14 to GLS in Equation 9.25. This isn’t 
surprising, since different estimates can have different values even though 
their expected values are the same. The second problem is more impor-
tant, however. It turns out that GLS works well if ρn is close to the actual ρ, 
but the GLS ρn is biased in small samples. If ρn is biased, then the biased ρn 
introduces bias into the GLS estimates of the βns. Luckily, there is a remedy 
for serial correlation that helps avoid both of these problems: Newey–West 
standard errors.
Newey–West Standard Errors
Not all corrections for pure serial correlation involve Generalized Least Squares. 
Newey–West standard errors are SE(βn)s that take account of serial cor-
relation without changing the βns themselves in any way.17 The logic behind 
Newey–West standard errors is powerful. If serial correlation does not cause 
bias in the βns but does impact the standard errors, then it makes sense to adjust 
the estimated equation in a way that changes the SE(βn)s but not the βns.
17. W. K. Newey and K. D. West, “A Simple, Positive Semi-Definite Heteroskedasticity and 
­Autocorrelation Consistent Covariance Matrix,” Econometrica, 1987, pp. 703–708. Newey–West 
standard errors are similar to HC standard errors (or White standard errors), to be discussed in 
Section 10.4.


296
Chapter 9  Serial Correlation
Thus Newey–West standard errors have been calculated specifically to 
avoid the consequences of pure first-order serial correlation. The Newey–
West procedure yields an estimator of the standard errors that, while they 
are biased, is generally more accurate than uncorrected standard errors for 
large samples (greater than 100) in the face of serial correlation. As a result, 
Newey–West standard errors can be used for t-tests and other hypothesis tests 
in most samples without the errors of inference potentially caused by serial 
correlation. Typically, Newey–West SE(βn)s are larger than OLS SE(βn)s, thus 
producing lower t-scores and decreasing the probability that a given esti-
mated coefficient will be significantly different from zero.
To see how Newey–West standard errors work, let’s apply them to the 
same serially correlated chicken demand equation to which we applied GLS 
in Equation 9.14. If we use Newey–West standard errors in the estimation of 
Equation 9.14, we get:
	
 Ynt = 27.7 - 0.11PCt + 0.03PBt + 0.23YDt	
(9.26)
	
10.032	
10.022	
10.012
	
t = -3.30	
+ 2.12	
+19.2
	
 R  2 =  .9904  N = 29	
Let’s compare Equations 9.14 and 9.26. First of all, the βns are identical in 
Equations 9.14 and 9.26. This is because Newey–West standard errors do 
not change the OLS βns. Second, while we can’t observe the change because 
of rounding, the Newey–West standard errors must be different from the 
OLS standard errors because the t-scores have changed even though the esti-
mated coefficients are identical. However, two of the Newey–West SE(βn)s are 
slightly lower than the OLS SE(βn)s, which is a surprise even in a small sample 
like this one. Such a result indicates that there may well be an omitted vari-
able or nonstationarity (to be discussed in Chapter 12) in this equation.
9.6   Summary
1.	
Serial correlation, or autocorrelation, is the violation of Classical As-
sumption IV that the observations of the error term are uncorrelated 
with each other. Usually, econometricians focus on first-order serial 
correlation, in which the current observation of the error term is as-
sumed to be a function of the previous observation of the error term 
and a not-serially-correlated error term (u):
	
et = ρet-1 + ut  - 1 6 ρ 6 1
	
where ρ is “rho,” the autocorrelation coefficient.


297
Exercises 
2.	
Pure serial correlation is serial correlation that is a function of the 
error term of the correctly specified regression equation. Impure serial 
correlation is caused by specification errors such as an omitted vari-
able or an incorrect functional form. While impure serial correlation 
can be positive 10 6 ρ 6 +12 or negative 1 -1 6 ρ 6 02 pure serial 
correlation in economics or business situations is almost always posi-
tive (unless first differences are involved).
3.	
The major consequence of serial correlation is bias in the OLS SE (βn)s, 
causing unreliable hypothesis testing. Pure serial correlation does not 
cause bias in the estimates of the βs.
4.	
A commonly used method of detecting first-order serial correlation 
is the Durbin–Watson test, which uses the residuals of an estimated 
regression to test the possibility of serial correlation in the error term. 
An often-preferred alternative is the Lagrange Multiplier (LM) test, 
which is far more general than the Durbin–Watson test.
5.	
The first step in ridding an equation of serial correlation is to check 
for possible specification errors. Only once the possibility of impure 
serial correlation has been reduced to a minimum should remedies 
for pure serial correlation be considered.
6.	
Generalized Least Squares (GLS) is a method of transforming an 
equation to rid it of pure first-order serial correlation. The use of GLS 
requires the estimation of ρ.
7.	
Newey–West standard errors are an alternative remedy for serial cor-
relation that adjusts the OLS estimates of the SE(βn)s to take account 
of the serial correlation without changing the βns.
Exercises 
(The answers to the even-numbered exercises are in Appendix A.)
	 1.	 Write the meaning of each of the following terms without referring to 
the book (or your notes), and compare your definition with the ver-
sion in the text for each.
a.	Durbin–Watson test (p. 284)
b.	first-order auto correlation coefficient (p. 275)
c.	 first-order serial correlation (p. 275)
d.	Generalized Least Squares (GLS) (p. 292)
e.	 impure serial correlation (p. 278)


298
Chapter 9  Serial Correlation
f.	 Lagrange Multiplier (LM) test (p. 289)
g.	negative serial correlation (p. 276)
h.	Newey–West standard errors (p. 295)
i.	 positive serial correlation (p. 276)
j.	 Prais–Winsten method (p. 293)
k.	pure serial correlation (p. 275)
	 2.	 Consider the following equation for U.S. per capita consumption of 
beef:
CBt = - 330.3 + 49.1lnYt - 0.34PBt + 0.33PRPt - 15.4Dt
	
17.42	
10.132	
10.122	
14.12
	
t = 6.6	
- 2.6	
2.7	
- 3.7
	
R  2 = .700    N = 28       DW = 0.94	
(9.27)
where: CBt  = the annual per capita pounds of beef consumed in the 
United States in year t
	
	 ln Yt  = the log of per capita disposable real income in the U.S. in 
year t
	
	 PBt  = average annualized real wholesale price of beef in year t (in 
cents per pound)
	
	 PRPt = average annualized real wholesale price of pork in year t 
(in cents per pound)
	
	 Dt
 =  a dummy variable equal to 1 for years in which there was a 
“health scare” about the dangers of red meat, 0 otherwise
a.	Develop and test your own hypotheses with respect to the indi-
vidual estimated slope coefficients.
b.	Test for serial correlation in Equation 9.27 using the Durbin–Watson 
test at the 5-percent level.
c.	 What econometric problem(s) (if any) does Equation 9.27 appear 
to have? What remedy would you suggest?
d.	You take your own advice and apply GLS to Equation 9.27, obtaining:
CBt = -193.3 + 35.2ln Yt - 0.38PBt + 0.10PRPt - 5.7Dt
	
114.12 
  10.102 
  10.092        13.92
	
t = 2.5   
-3.7 
 
 
1.1         -1.5
	
R  2 = .857  N = 28  ρn = 0.82	
(9.28)
	
Compare Equations 9.27 and 9.28. Which do you prefer? Why?
	 3.	 Recall from Section 9.5 that switching the order of a data set will 
not change its coefficient estimates. A revised order will change the 
Durbin–Watson statistic, however. To see both these points, run 
9
9


299
Exercises 
regressions 1HS = β0 + β1P + e2 and compare the coefficient esti-
mates and DW statistics for this data set:
Year
Housing Starts
Population
   1
  9090
2200
   2
  8942
2222
   3
  9755
2244
   4
10327
2289
   5
10513
2290
	
	 in the following three orders (in terms of year):
a.	1, 2, 3, 4, 5
b.	5, 4, 3, 2, 1
c.	 2, 4, 3, 5, 1
	 4.	 Suppose that the data in a time-series study were entered in reverse 
chronological order. Would this change in any way the testing or 
adjusting for serial correlation? How? In particular:
a.	What happens to the Durbin–Watson statistic’s ability to detect 
­serial correlation if the order is reversed?
b.	What happens to the GLS method’s ability to adjust for serial cor-
relation if the order is reversed?
c.	 What is the intuitive economic explanation of reverse serial cor-
relation?
	 5.	 Your friend is just finishing a study of attendance at Los Angeles Laker 
regular-season home basketball games when she hears that you’ve 
read a chapter on serial correlation and asks your advice. Before run-
ning the equation on last season’s data, she “reviewed the literature” 
by interviewing a number of basketball fans. She found out that fans 
like to watch winning teams. In addition, she learned that while some 
fans like to watch games throughout the season, others are most 
interested in games played late in the season. Her estimated equation 
(standard errors in parentheses) was:
	
An  t = 14123 + 20L t +  2600Pt +  900Wt
	
 15002
 110002
 13002
	
DW = 0.85  N = 40  R 2 = .46
where:  At = the attendance at game t
        Lt = the winning percentage (games won divided by games 
played) of the Lakers before game t


300
Chapter 9  Serial Correlation
	
	
Pt  = the winning percentage before game t of the Lakers’ opponent 
in that game
	
	
Wt = a dummy variable equal to 1 if game t was on Friday, Satur-
day, or Sunday, 0 otherwise
a.	Test for serial correlation using the Durbin–Watson test at the 
5-percent level.
b.	Make and test appropriate hypotheses about the slope coefficients 
at the 1-percent level.
c.	 Compare the size and significance of the estimated coefficient of L 
with that for P. Is this difference surprising? Is L an irrelevant vari-
able? Explain your answer.
d.	If serial correlation exists, would you expect it to be pure or impure 
serial correlation? Why?
e.	 Your friend omitted the first game of the year from the sample be-
cause the first game is always a sellout and because neither team 
had a winning percentage yet. Was this a good decision?
	 6.	 In a 1988 article, Josef Brada and Ronald Graves built an interest-
ing model of defense spending in the Soviet Union just before the 
breakup of that nation.18 The authors felt sure that Soviet defense 
spending was a function of U.S. defense spending and Soviet GNP but 
were less sure about whether defense spending also was a function of 
the ratio of Soviet nuclear warheads to U.S. nuclear warheads. Using a 
double-log functional form, the authors estimated a number of alter-
native specifications, including (standard errors in parentheses):
 lnSDHt = -  1.99 + 0.056lnUSDt +  0.969lnSYt +  0.057lnSPt
	
10.0742	
10.0652	
10.0322
	
t = 0.76	
14.98	
1.80
	
N = 25 1annual 1960–19842 R  2 = .979 DW = 0.49	
(9.29)
 lnSDHt = -  2.88 + 0.105lnUSDt +  1.066lnSYt
 10.0732
 10.0382
 t = 1.44
 28.09
	
N = 25 1annual 1960–19842 R  2 = .977 DW = 0.43	
(9.30)
®
®
18. Josef C. Brada and Ronald L. Graves, “The Slowdown in Soviet Defense Expenditures,” 
Southern Economic Journal, Vol. 54, No. 4, pp. 969–984. In addition to the variables used in this 
exercise, Brada and Graves also provide data for SFPt, the rate of Soviet factor productivity in 
year t, which we include in Table 9.1.


301
Exercises 
where:  SDHt = the CIA’s “high” estimate of Soviet defense expenditures 
in year t (billions of 1970 rubles)
	
	
USDt = U.S. defense expenditures in year t (billions of 1980 dollars)
	
	
SYt
 = Soviet GNP in year t (billions of 1970 rubles)
	
	
SPt
 = the ratio of the number of USSR nuclear warheads (NRt) 
to the number of U.S. nuclear warheads (NUt) in year t
Table 9.1  Data on Soviet Defense Spending
Year
SDH
SDL
USD
SY
SFP
NR
NU
1960
31
23
200.54
232.3
7.03
415
1734
1961
34
26
204.12
245.3
6.07
445
1846
1962
38
29
207.72
254.5
3.90
485
1942
1963
39
31
206.98
251.7
2.97
531
2070
1964
42
34
207.41
279.4
1.40
580
2910
1965
43
35
185.42
296.8
1.87
598
4110
1966
44
36
203.19
311.9
4.10
674
4198
1967
47
39
241.27
326.3
4.90
1058
4338
1968
50
42
260.91
346.0
4.07
1270
4134
1969
52
43
254.62
355.9
2.87
1662
4026
1970
53
44
228.19
383.3
4.43
2047
5074
1971
54
45
203.80
398.2
3.77
3199
6282
1972
56
46
189.41
405.7
2.87
2298
7100
1973
58
48
169.27
435.2
3.87
2430
8164
1974
62
51
156.81
452.2
4.30
2534
8522
1975
65
53
155.59
459.8
6.33
2614
9170
1976
69
56
169.91
481.8
0.63
3219
9518
1977
70
56
170.94
497.4
2.23
4345
9806
1978
72
57
154.12
514.2
1.03
5097
9950
1979
75
59
156.80
516.1
0.17
6336
9945
1980
79
62
160.67
524.7
0.27
7451
9668
1981
83
63
169.55
536.1
0.47
7793
9628
1982
84
64
185.31
547.0
0.07
8031
10124
1983
88
66
201.83
567.5
1.50
8730
10201
1984
90
67
211.35
578.9
1.63
9146
10630
Source: Josef C. Brada and Ronald L. Graves, “The Slowdown in Soviet Defense Expen-
ditures,” Southern Economic Journal, Vol. 54, No. 4, p. 974.
Datafile 5 DEFEND9


302
Chapter 9  Serial Correlation
a.	The authors expected positive signs for all the slope coefficients of 
both equations. Test these hypotheses at the 5-percent level.
b.	Use our four specification criteria to determine whether SP is an ir-
relevant variable. Explain your reasoning.
c.	 Test both equations for positive first-order serial correlation. Does 
the high probability of serial correlation cause you to reconsider 
your answer to part b? Explain.
d.	Someone might argue that because the DW statistic improved when 
lnSP was added, the serial correlation was impure and that GLS was 
not called for. Do you agree with this conclusion? Why or why not?
e.	 If we run a GLS version of Equation 9.29, we get Equation 9.31. Does 
this result cause you to reconsider your answer to part b? Explain
 lnSDHt = -2.65 + 0.104lnUSDt +  1.034 lnSYt -  0.032 lnSPt
 10.0872
 10.0782
 10.0342
 t = 1.20
 13.30
 0.93
	
N = 24 1annual 1960–19842 R  2 = .986 ρn = 0.75	
(9.31)
	 7.	 As an example of impure serial correlation caused by an incorrect 
functional form, let’s return to the equation for the percentage of 
putts made (Pi) as a function of the length of the putt in feet (Li) 
that we discussed originally in Exercise 3 in Chapter 1. The complete 
documentation of that equation is
 Pni = 83.6 - 4.1Li
 10.42
 t = - 10.6
	
N = 19  R  2 = .861  DW = 0.48	
(9.32)
a.	Test Equation 9.32 for serial correlation using the Durbin–Watson 
test at the 5-percent level.
b.	Why might the linear functional form be inappropriate for this 
study? Explain your answer.
c.	 If we now reestimate Equation 9.32 using a double-log functional 
form, we obtain:
 lnPi = 5.50 - 0.92 lnLi
 10.072
 t = - 13.0
	
N = 19  R  2 = .903  DW = 1.22	
(9.33)
®
h


303
Appendix: Econometric Lab #5
	
Test Equation 9.33 for serial correlation using the Durbin–Watson 
test at the 5-percent level.
d.	Compare Equations 9.32 and 9.33. Which equation do you prefer? 
Why?
9.7   Appendix: Econometric Lab #5
In this lab, you’ll expand on Econometric Lab #2 by estimating an aggregate 
consumption function for the U.S. economy for the period 1945–2006, test-
ing your equation for serial correlation, and, if appropriate, taking corrective 
action.19
Step 1: State the Variables and the Expected Signs of the 
Coefficients
As in Econometric Lab #2, our goal is to model U.S. aggregate consumption 
as a function of disposable personal income and the real interest rate. Once 
again, the data are from the St. Louis Federal Reserve FRED database and the 
Economic Report of the President. Descriptions of the variables are in Table 9.2, 
along with the hypothesized signs for the coefficients, and the dataset itself is 
on the text’s website as CONS9.
Table 9.2  Variable Definitions
Variable
Description
Expected sign
cont
Real personal consumption expenditures in 
year t, in billions of 2009 dollars
NA
dpit
Real disposable personal income in year t, 
in billions of 2009 dollars
1
aaat
The real interest rate on Aaa corporate 
bonds in year t
2
yeart
Year t
NA
19. Econometric Lab #2 used a sample for the period 1945–2014, but we end Lab #5’s sample 
in 2006 to avoid the (admittedly interesting) complications introduced by the Great Recession.


304
Chapter 9  Serial Correlation
Step 2: Estimate the Aggregate Consumption Function
Now estimate the consumption function, using disposable personal income 
and the real interest rate as the independent variables.20
Step 3: Examine the Residuals
Generate the residuals from the regression in Step 2 (naming them “e”) and 
plot them as a line graph against yeart (with yeart on the x-axis). Does the 
plot look entirely random? Explain.
Step 4: Run the Durbin–Watson Test
Conduct a Durbin–Watson test for positive serial correlation.
a.	 Carefully write down the null and alternative hypotheses.
b.	 Run a Durbin–Watson test for positive serial correlation at the 5-percent 
level. What are the upper and lower critical values in this case? What 
can you conclude? Explain.
Step 5: Run the Lagrange Multiplier Serial Correlation Test
Let’s see if our Durbin–Watson results can be confirmed with the Lagrange 
Multiplier test.
a.	 Are the null and alternative hypotheses for the Lagrange Multiplier test 
the same as for the Durbin–Watson test? Why or why not?
b.	 Conduct a Lagrange Multiplier test for serial correlation at the 5-percent 
level. What can you conclude? Explain.
Step 6: Estimate the Model with Generalized Least Squares
a.	 If you encountered serial correlation in either of the previous steps, 
re-estimate our aggregate consumption model using Generalized Least 
Squares.
20. If you’re using Stata, be sure to tell Stata that this is a time series and that yeart is the time 
variable.


305
Appendix: Econometric Lab #5
b.	 Are the GLS coefficients and t-statistics the same as the OLS coeffi-
cients and t-statistics? Explain.
c.	 After the GLS transformation, does serial correlation still appear to 
­exist? Support your answer.
Step 7: Calculate Newey-West Standard Errors
a.	 If you ran a GLS model in Step 6, now estimate the aggregate con-
sumption model using the Newey–West method with a lag of 1.
b.	 After the Newey–West calculation, are the coefficients the same as the 
OLS coefficients? Explain.
c.	 Why are the Newey–West t-statistics different from the OLS t-statistics? 
Which do you prefer? Why?
