# Chapter 10: Heteroskedasticity

**Pages:** 326-359

---

Heteroskedasticity
10.1  Pure versus Impure Heteroskedasticity
10.2  The Consequences of Heteroskedasticity
10.3  Testing for Heteroskedasticity
10.4  Remedies for Heteroskedasticity
10.5  A More Complete Example
10.6  Summary and Exercises
10.7  Appendix: Econometric Lab #6
Chapter 10
Heteroskedasticity is the violation of Classical Assumption V, which states that 
the observations of the error term are drawn from a distribution that has a 
constant variance.1 The assumption of constant variances for different observa-
tions of the error term (homoskedasticity) is not always realistic. For example, 
in a model explaining heights, it’s likely that error term observations associated 
with the height of a basketball player would come from distributions with 
larger variances than those associated with the height of a mouse. Heteroske-
dasticity is important because OLS, when applied to heteroskedastic models, is 
no longer the minimum variance estimator (it still is unbiased, however).
In general, heteroskedasticity is more likely to take place in cross-sectional 
models than in time-series models. This focus on cross-sectional models is 
not to say that heteroskedasticity in time-series models is impossible, though. 
In fact, heteroskedasticity has turned out to be an important factor in time-
series studies of financial markets.
1. Various authors spell this “heteroscedasticity,” but Huston McCulloch appears to settle this 
controversy in favor of “heteroskedasticity” because of the word’s Greek origin. See J. Huston 
McCulloch, “On Heteros*edasticity,” Econometrica, Vol. 53, No. 2, p. 483. Although hetero-
skedasticity is a difficult word to spell, at least it’s an impressive comeback when parents ask, 
“What’d you learn for all that money?”
306


307
  Pure versus Impure Heteroskedasticity
The structure of this chapter will be quite familiar. We’ll attempt to answer 
the same four questions for heteroskedasticity that we answered for multicol-
linearity and serial correlation in the previous two chapters:
1.	 What is the nature of the problem?
2.	 What are the consequences of the problem?
3.	 How is the problem diagnosed?
4.	 What remedies for the problem are available?
10.1   Pure versus Impure Heteroskedasticity
Heteroskedasticity, like serial correlation, can be divided into pure and 
impure versions. Pure heteroskedasticity is caused by the error term of the 
correctly specified equation; impure heteroskedasticity is caused by a specifi-
cation error such as an omitted variable.
Pure Heteroskedasticity
Pure heteroskedasticity refers to heteroskedasticity that is a function of the 
error term of a correctly specified regression equation. As with serial correla-
tion, use of the word “heteroskedasticity” without any modifier (like pure or 
impure) implies pure heteroskedasticity.
Such pure heteroskedasticity occurs when Classical Assumption V, 
which assumes that the variance of the error term is constant, is violated in a 
correctly specified equation. Assumption V assumes that:
	
VAR1ei2 = σ2 = a constant  1i = 1, 2, . . . , N2	
(10.1)
If this assumption is met, all the observations of the error term can be 
thought of as being drawn from the same distribution: a distribution with 
a mean of zero and a variance of σ2. The property of having σ2 not change 
for different observations of the error term is called homoskedasticity. A 
homoskedastic error term distribution is pictured in the top half of Figure 
10.1; note that the variance of the distribution is constant (even though 
individual observations drawn from that sample will vary quite a bit).
With heteroskedasticity, this error term variance is not constant; instead, 
the variance of the distribution of the error term depends on exactly which 
observation is being discussed:
	
VAR1ei2 = σ2
i  1i = 1, 2, . . . , N2	
(10.2)


308
Chapter 10  Heteroskedasticity
Note that the only difference between Equations 10.1 and 10.2 is the sub-
script “i” attached to σ2, which implies that instead of being constant over all 
the observations, a heteroskedastic error term’s variance can change depend-
ing on the observation (hence the subscript).
Heteroskedasticity often occurs in data sets in which there is a wide dispar-
ity between the largest and smallest observed value of the dependent variable. 
0
Homoskedastic es
“Narrow” Distribution
“Wide” Distribution
0
Heteroskedastic es
Figure 10.1  Homoskedasticity versus Discrete Heteroskedasticity
In homoskedasticity, the distribution of the error term has a constant variance, so the obser-
vations are continually drawn from the same distribution (shown in the top panel). In the 
simplest heteroskedastic case, discrete heteroskedasticity, there would be two different error 
term variances and, therefore, two different distributions (one wider than the other, as in 
the bottom panel) from which the observations of the error term could be drawn.


309
  Pure versus Impure Heteroskedasticity
The larger the disparity between the size of observations of the dependent 
variable in a sample is, the larger the likelihood is that the error term obser-
vations associated with them will have different variances and therefore be 
heteroskedastic. That is, we’d expect that the error term distribution for very 
large observations might have a large variance, and that the error term distri-
bution for small observations might have a small variance.
In cross-sectional data sets, it’s easy to get such a large range between the 
highest and lowest values of the variables. The difference between California 
and Rhode Island in terms of the dollar value of the consumption of goods 
and services, for instance, is quite large (comparable in percentage terms to the 
difference between the heights of a basketball player and a mouse). Since cross-
sectional models often include observations of widely different sizes in the 
same sample (cross-state studies of the United States usually include California 
and Rhode Island as individual observations, for example), heteroskedasticity 
is hard to avoid if economic topics are going to be studied cross sectionally.
The simplest way to visualize pure heteroskedasticity is to picture a world in 
which the observations of the error term could be grouped into just two different 
distributions, “wide” and “narrow.” We’ll call this simple version of the problem 
discrete heteroskedasticity. Here, both distributions would be centered around zero, 
but one would have a larger variance than the other, as indicated in the bottom 
half of Figure 10.1. Note the difference between the two halves of the figure. With 
homoskedasticity, all the error term observations come from the same distribu-
tion; with heteroskedasticity, they come from different distributions.
For an example of discrete heteroskedasticity, we need go no further than 
our discussion of the heights of basketball players and mice. We’d certainly 
expect the variance of e to be larger for basketball players as a group than for 
mice, so the distribution of e for the heights of basketball players might look 
like the “wide” distribution in Figure 10.1, and the distribution of e for mice 
would be much narrower than the “narrow” distribution in Figure 10.1.
Heteroskedasticity takes on many more complex forms. In fact, the num-
ber of different models of heteroskedasticity is virtually limitless, and an 
analysis of even a small percentage of these alternatives would be a huge task. 
Instead, we’d like to address the general principles of heteroskedasticity by 
focusing on the most frequently specified model of pure heteroskedasticity, 
just as we focused on pure, positive, first-order serial correlation in the previ-
ous chapter. However, don’t let this focus mislead you into concluding that 
econometricians are concerned only with one kind of heteroskedasticity.
In this model of heteroskedasticity, the variance of the error term is related 
to an exogenous variable Zi. For a typical regression equation:
	
Yi = β0 + β1X1i + β2X2i + ei	
(10.3)


310
Chapter 10  Heteroskedasticity
the variance of the otherwise classical error term e might be equal to:
	
VAR1ei2 = σ2Zi	
(10.4)
where Z may or may not be one of the Xs in the equation. The variable Z is 
called a proportionality factor because the variance of the error term 
changes proportionally to Zi. The higher the value of Zi, the higher the 
variance of the distribution of the ith observation of the error term. There 
would be N different distributions, one for each observation, from which the 
observations of the error term could be drawn depending on the number of 
different values that Z takes. To see what homoskedastic and heteroskedastic 
distributions of the error term look like with respect to Z, compare Figures 
10.2 and 10.3. Note that the heteroskedastic distribution gets wider as Z 
increases but that the homoskedastic distribution maintains the same width 
no matter what value Z takes.
What is an example of a proportionality factor Z? How is it possible for 
an exogenous variable such as Z to change the whole distribution of an error 
term? Think about a function that relates the consumption expenditures in 
a state to its income. The expenditures of a small state like Rhode Island are 
not likely to be as variable in absolute value as the expenditures of a large 
state like California because a 10-percent change in spending for a large state 
involves a lot more money than a 10-percent change for a small one. In such 
a case, the dependent variable would be consumption expenditures and a 
likely proportionality factor, Z, would be population. As population rose, 
so too would the variance of the error term of an equation built to explain 
0
Zi
Probability
Distribution
of the eis
ei . 0
ei , 0
Figure 10.2  A Homoskedastic Error Term with Respect to Zi
If an error term is homoskedastic with respect to Zi, the variance of the distribution of 
the error term is the same (constant) no matter what the value of Zi is: VAR1ei2 = σ2.


311
  Pure versus Impure Heteroskedasticity
expenditures. The error term distributions would look something like those 
in Figure 10.3, where the Z in Figure 10.3 is population.
This example helps emphasize that heteroskedasticity is likely to occur in 
cross-sectional models because of the large variation in the size of the depen-
dent variable involved. An exogenous disturbance that might seem huge to a 
small state could seem miniscule to a large one, for instance.
Heteroskedasticity can occur in a time-series model with a significant 
amount of change in the dependent variable. If you were modeling sales of 
DVD players from 1994 to 2015, it’s quite possible that you would have a 
heteroskedastic error term. As the phenomenal growth of the industry took 
place, the variance of the error term probably increased as well. Such a pos-
sibility is unlikely in time series that have low rates of change, however.
Heteroskedasticity also can occur in any model, time series or cross sec-
tional, where the quality of data collection changes dramatically within the 
sample. As data collection techniques get better, the variance of the error term 
should fall because measurement errors are included in the error term. As 
measurement errors decrease in size, so should the variance of the error term. 
For more on this topic (called “errors in the variables”), see Section 14.6.
Impure Heteroskedasticity
Heteroskedasticity that is caused by an error in specification, such as an omit-
ted variable, is referred to as impure heteroskedasticity. Impure heteroske-
dasticity thus is similar to impure serial correlation.
0
Zi
Probability
Distribution
of the eis
ei . 0
ei , 0
Figure 10.3  A Heteroskedastic Error Term with Respect to Zi
If an error term is heteroskedastic with respect to Zi, the variance of the distribution of 
the error term changes systematically as a function of Zi. In this example, the variance is 
an increasing function of Zi, as in VAR1ei2 = σ2Zi.


312
Chapter 10  Heteroskedasticity
An omitted variable can cause a heteroskedastic error term because the 
portion of the omitted effect not represented by one of the included explana-
tory variables must be absorbed by the error term. If this effect has a hetero-
skedastic component, the error term of the misspecified equation might be 
heteroskedastic even if the error term of the true equation is not. This distinc-
tion is important because with impure heteroskedasticity the correct remedy 
is to find the omitted variable and include it in the regression. It’s therefore 
important to be sure that your specification is correct before trying to detect 
or remedy pure heteroskedasticity.
10.2   The Consequences of Heteroskedasticity
If the error term of your equation is known to be heteroskedastic, what does 
that mean for the estimation of your coefficients? If the error term of an 
equation is heteroskedastic, there are three major consequences:2
1.	 Pure heteroskedasticity does not cause bias in the coefficient estimates. Even 
if the error term of an equation is known to be purely heteroskedas-
tic, that heteroskedasticity will not cause bias in the OLS estimates of 
the coefficients. This is true because even though large positive errors 
are more likely, so too are large negative errors. The two tend to aver-
age each other out, leaving the OLS estimator still unbiased.
	As a result, we can say that an otherwise correctly specified equation 
that has pure heteroskedasticity still has the property that:
E1βn 2 = β  for all βs
	
Lack of bias does not guarantee “accurate” coefficient estimates, espe-
cially since heteroskedasticity increases the variance of the estimates, 
but the distribution of the estimates is still centered around the true β. 
Equations with impure heteroskedasticity caused by an omitted vari-
able, of course, will have possible specification bias.
2.	 Heteroskedasticity typically causes OLS to no longer be the minimum-
variance estimator (of all the linear unbiased estimators). Pure hetero-
skedasticity causes no bias in the estimates of the OLS ­coefficients, 
2. It turns out that the consequences of heteroskedasticity are almost identical in general frame-
work to those of serial correlation, though the two problems are quite different.


313
  The Consequences of Heteroskedasticity
but it does affect the minimum-variance property. If the error term of 
an equation is heteroskedastic with respect to a proportionality fac-
tor Z:
	
VAR1ei2 = σ2Zi	
(10.5)
	
then the minimum-variance portion of the Gauss–Markov Theorem 
cannot be proven because there are other linear unbiased estimators 
that have smaller variances. This is because the heteroskedastic error 
term causes the dependent variable to fluctuate, and the OLS estima-
tion procedure attributes this fluctuation to the independent variables. 
Thus, OLS is more likely to misestimate the true β in the face of hetero-
skedasticity. The βns still are unbiased because overestimates are just as 
likely as underestimates.
3.	 Heteroskedasticity causes the OLS estimates of the SE(bn)s to be biased, 
leading to unreliable hypothesis testing and confidence intervals. With 
heteroskedasticity, the OLS formula for the standard error produces 
biased estimates of the SE(βn)s. Because the SE(βn) is a prime compo-
nent in the t-statistic, these biased SE(βn)s cause biased t-scores and 
unreliable hypothesis testing in general. In essence, heteroskedastic-
ity causes OLS to produce incorrect SE(βn)s and t-scores! Not surpris-
ingly, most econometricians therefore are very hesitant to put much 
faith in hypothesis tests that were conducted in the face of pure het-
eroskedasticity.3
What sort of bias in the standard errors does heteroskedasticity tend to 
cause? Typically, heteroskedasticity causes OLS estimates of the standard 
errors to be biased downward, making them too small. Sometimes, however, 
they’re biased upward; it’s hard to predict in any given case. But either way, 
it’s a big problem for hypothesis testing and confidence intervals.
What’ll happen if OLS underestimates a standard error? Well, the “too 
low” SE1βn 2 will cause a “too high” t-score for a particular coefficient, and 
this will make it more likely that we will reject a null hypothesis (for exam-
ple, H0: β … 0) when it is in fact true. This increased chance of rejecting H0 
means that we’re more likely to make a Type I error and we’re more likely 
to make the mistake of keeping an irrelevant variable in an equation. Also, 
because the confidence interval depends directly on SE1βn 2 (see Equation 5.9), 
3. While our discussion here involves the t-test, the same conclusion of unreliability in the face 
of heteroskedasticity applies to all other test statistics, including confidence intervals.


314
Chapter 10  Heteroskedasticity
the underestimation of SE1βn 2 will fool us into thinking that our estimate is 
more precise than it really is.4
In other words, pure heteroskedasticity can make quite a mess of our 
results. Hypothesis testing will become unreliable, and confidence intervals 
will be misleading.
10.3   Testing for Heteroskedasticity
As we’ve seen, heteroskedasticity is a potentially nasty problem. The good news 
is that there are many tests for heteroskedasticity. The bad news is heteroske-
dasticity can take many different forms and no single test can find them all.
In this section, we’ll describe two of the most popular and powerful tests 
for heteroskedasticity, the Breusch–Pagan test and the White test.5 While nei-
ther test can “prove” that heteroskedasticity exists, these tests often can give 
us a pretty good idea of whether or not it’s a problem.
Before using any test for heteroskedasticity, it’s a good idea to start with the 
following preliminary questions:
1.	 Are there any obvious specification errors? Are there any likely omitted 
variables? Have you specified a linear model when a double-log model 
is more appropriate? Don’t test for heteroskedasticity until the specifica-
tion is as good as possible. After all, if you find heteroskedasticity in an 
incorrectly specified model, there’s a chance it will be impure.
2.	 Are there any early warning signs of heteroskedasticity? Just as certain 
kinds of clouds can warn of potential storms, certain kinds of data can 
signal possible heteroskedasticity. In particular, if the dependent vari-
able’s maximum value is many, many times larger than its minimum, 
beware of heteroskedasticity.
3.	 Does a graph of the residuals show any evidence of heteroskedasticity? It 
sometimes saves time to plot the residuals against a potential Z propor-
tionality factor or against the dependent variable. If you see a pattern in 
the residuals, you’ve got a problem. See Figure 10.4 for a few examples 
of heteroskedastic patterns in the residuals.
4. If OLS overestimates the standard error, then we’ll have the same problems but in reverse. 
The “too high” SE1βn 2 will lead to a “too low” t-score. If the t-score is lowered enough, we might 
be fooled into failing to reject a false null hypothesis, thus increasing the risk that we’ll drop a 
relevant variable from the model. In addition, the confidence intervals will be too wide, leading 
to similar potential mistakes.
5. Both tests belong to a general group of tests based on the Lagrange Multiplier (LM), which 
you first met in Chapter 9.


ei
0
Small es Associated
with Small Zs
Zi
Zi
Zi
Large es Associated
with Large Zs
Small es Associated
with Large Zs
Large es Associated
with Small Zs
e Rises and then
Falls as Z Increases
1
2
ei
0
1
2
ei
0
1
2
Figure 10.4  Eyeballing Residuals for Possible Heteroskedasticity
If you plot the residuals of an equation with respect to a potential Z proportionality 
­factor, a pattern in the residuals is an indication of possible heteroskedasticity.
315


316
Chapter 10  Heteroskedasticity
Note that Figure 10.4 shows “textbook” examples of heteroskedasticity. 
The real world is nearly always a lot messier than textbook graphs. It’s not 
unusual to look at a real-world residual plot and be unsure whether there’s a 
pattern or not. As a result, even if there are no obvious specification errors, no 
early warning signs, and no visible residual patterns, it’s a good idea to do a 
formal statistical test for heteroskedasticity, so we’d better get started.
The Breusch–Pagan Test
The Breusch–Pagan test is a method of testing for heteroskedasticity in the 
error term by investigating whether the squared residuals can be explained by 
possible proportionality factors.6
Here’s how it works.
1.	 Obtain the residuals from the estimated regression equation. For an equation 
with two independent variables, this would be:
	
ei = Yi - Yni = Yi - βn 0 - βn 1X1i - βn 2X2i	
(10.6)
2.	 Use the squared residuals as the dependent variable in an auxiliary equation. 
As the explanatory variables in the auxiliary regression, use right-hand 
variables from the original regression that you suspect might be pro-
portionality factors. For many researchers, the default option is to 
include all of them. For instance, if the original equation has two ex-
planatory variables, then the auxiliary regression would be:
	
ei
2 = α0 + α1X1i + α2X2i + ui	
(10.7)
3.	 Test the overall significance of Equation 10.7 with a chi-square test. The null 
and alternative hypotheses are:
H0: α1 = α2 = 0
HA: H0 is false
	
The null hypothesis is homoskedasticity, because if α1 = α2 = 0, then 
the variance equals α0, which is a constant. The test statistic here is NR2, 
or the sample size (N) times the unadjusted R2 from Equation 10.7. 
This test statistic has a chi-square distribution7 with degrees of freedom 
6. T. S. Breusch and A. R. Pagan, “A Simple Test for Heteroscedasticity and Random Coefficient 
Variation,” Econometrica, Vol. 47, pp. 1287–1294.
7. You might wonder why the test statistic is not the overall F-statistic of the auxiliary regres-
sion. It turns out that the F-statistic is valid only if the errors are normally distributed, and in 
this case, with squared residuals as the dependent variable, it’s not safe to assume the errors are 
normally distributed. With non-normal errors, the proper test is a chi-square test.


317
  Testing for Heteroskedasticity
equal to the number of slope coefficients in the auxiliary regression 
(Equation 10.7). If NR2 is greater than or equal to the critical chi-square 
value, then we reject the null hypothesis of homoskedasticity.
If you strongly suspect that only certain variables are plausible Z factors, 
then you should run the Breusch–Pagan test using only an intercept and the 
suspect variables. The degrees of freedom for the chi-square statistic of course 
would change in such a situation, because they’re equal to the number of 
right-hand-side variables in the auxiliary equation. If you’re certain you know 
the one and only proportionality factor Z and that there are no other forms 
of heteroskedasticity present, you don’t even need to fool with the chi-square 
statistic. You can just do a two-sided t-test8 on the αn for Z.
The strengths of the Breusch–Pagan test are that it’s easy to use and it’s 
powerful if heteroskedasticity is related to one or more linear proportionality 
factors. Its weakness is that if it fails to find heteroskedasticity, it only means 
there is no evidence of heteroskedasticity related to the Zs you’ve chosen. If 
you’re pretty certain that the Xs in the auxiliary regression are the only plau-
sible proportionality factors, you can rest easy. But if you’re not certain, you 
might want to use the White test, which we’ll discuss shortly.
As an example of the use of the Breusch–Pagan test, let’s return to the 
Woody’s restaurants example of Section 3.2 and use the residuals of Equa-
tion 3.4 to test for heteroskedasticity. Recall that the regression explained 
the number of customers, as measured by the check volume (Y) for a cross 
section of 33 different Woody’s restaurants as a function of the number of 
nearby competitors (N), the nearby population (P), and the average house-
hold income of the local area (I):
	
Yni = 102,192 - 9075Ni + 0.355Pi + 1.288Ii	
(3.4)
	
120532   10.0732   10.5432
	
t = -4.42    4.88      2.37
	
N = 33        R  2 = .579
The first step in the Breusch–Pagan test is to obtain the residuals from 
Equation 3.4. You can find these residuals in Table 3.2 on page 77. The 
8. A Breusch–Pagan test with a single Z is a linear version of the Park test, which uses a double-
log equation to test whether the squared residuals can be explained by a single potential Z pro-
portionality factor. See R. E. Park, “Estimation with Heteroskedastic Error Terms,” Econometrica, 
Vol. 54, p. 888. A major disadvantage of the Park test, of course, is that the researcher must 
choose a single Z proportionality factor.


318
Chapter 10  Heteroskedasticity
second step is to square the residuals and use them as the dependent vari-
able in an auxiliary regression. If we include all the independent variables in 
Equation 3.4 in our auxiliary equation, we get:
	
ei
2 = α0 + α1Ni + α2Pi + α3Ii + ui	
(10.8)
If we estimate Equation 10.8, we find that the unadjusted R2 = .0441. 
We know that N = 33, so we can calculate that the chi-square statistic
= NR2 = 331.04412 = 1.455. Since the 5-percent critical value of chi-
square with 3 degrees of freedom is 7.81, we can’t reject the null hypothesis 
that α1 = α2 = α3 = 0. As a result, the Breusch–Pagan test doesn’t provide 
any evidence that Equation 3.4 suffers from heteroskedasticity. This makes 
sense. Even though the Woody’s sample is cross-sectional, the largest value 
of the dependent variable isn’t even twice the size of the smallest one, so we 
have no reason to suspect pure heteroskedasticity.
The White Test
Probably the most popular of all the heteroskedasticity tests is the White 
test9 because it can find more types of heteroskedasticity than any other test. 
That’s a distinct advantage in a world where just about any variable or combi-
nation of variables, linear or nonlinear, could trip us up with a heteroskedas-
tic stumbling block. Let’s see how it works.
The White test investigates the possibility of heteroskedasticity in an 
equation by seeing if the squared residuals can be explained by the equa-
tion’s independent variables, their squares, and their cross–products. To run 
the White test:
1.	 Obtain the residuals of the estimated regression equation.
2.	 Estimate an auxiliary regression, using the squared residuals as the dependent 
variable, with each X from the original equation, the square of each X, and 
the product of each X times every other X as the explanatory variables. For ex-
ample, if the original equation’s independent variables are X1 and X2, 
the White test equation is:
	
ei
2 = α0 + α1X1i + α2X2i + α3X1i
2 + α4X2i
2 + α5X1i X2i + ui	
(10.9)
9. Halbert White, “A Heteroskedasticity-Consistent Covariance Matrix Estimator and a Direct 
Test for Heteroskedasticity, Econometrica, Vol. 48, pp. 817–838.


319
  Testing for Heteroskedasticity
3.	 Test the overall significance of Equation 10.9 with a chi-square test. Once 
again, the test statistic is NR2, the sample size (N) times the unadjusted 
R2 of Equation 10.9. This test statistic has a chi-square distribution with 
degrees of freedom equal to the number of slope coefficients in the 
auxiliary regression. The null hypothesis is that all the slope coefficients 
in Equation 10.9 equal zero, and if NR2 is greater than the chi-square 
critical value, then we can reject the null hypothesis and conclude that 
there’s evidence of heteroskedasticity.
Check out the explanatory variables in Equation 10.9. They include 
every variable in the original model, their squares, and their cross products. 
Including all the variables from the original model allows the White test to 
check to see if any or all of them are Z proportionality factors. Including 
all the squared terms and cross products allows us to test for more exotic 
and complex types of heteroskedasticity. This is the White test’s greatest 
strength.
However, the White test contains more right-hand-side variables than the 
original regression, sometimes a lot more. This can be its greatest weakness. 
To see why, note that as the number of explanatory variables in an original 
regression rises, the number of right-hand variables in the White test auxil-
iary regression goes up much faster. For example, there are five right-hand 
variables in Equation 10.9 even though the original model had only two, 
X1 and X2. With three variables in the original model, the White regression 
could have nine. With 12 explanatory variables in the original model, there 
could10 be 90 in the White regression with all the squares and interactive 
terms included!
And this is where the weakness becomes a real problem. If the number 
of right-hand variables in the auxiliary regression exceeds the number of 
observations, you can’t run the White test regression because you would have 
negative degrees of freedom in the auxiliary equation! Even if the degrees of 
freedom in the auxiliary equation are positive but small, the White test might 
do a poor job of detecting heteroskedasticity because the fewer the degrees of 
10. There could be fewer explanatory variables if one or more of the original independent 
variables is a dummy, since the square of a dummy is the same as a dummy and the cross 
product of a variable times a dummy equals the original variable itself or zero. Because of the 
large number of variables and this possible duplication, it’s tedious to create and check all the 
variables for the White test. Luckily, Stata and most other econometric software packages have 
simple commands to do the work for you.


320
Chapter 10  Heteroskedasticity
freedom there are, the less powerful the statistical test is. In such a situation, 
you’d be limited to the Breusch–Pagan test or an alternative.11
As an example of the White test, let’s again return to the Woody’s restau-
rants model of Section 3.2. As with the Breusch–Pagan test, the first step is to 
obtain the residuals of the original Woody’s equation. The second step in the 
White test is to square the residuals and use them as the dependent variable 
in an auxiliary regression that includes N, P, I, their squares, and their cross 
products as independent variables:
ei
2 = α0 + α1Ni + α2Pi + α3Ii + α4Ni
2 + α5Pi
2 + α6Ii
2
	
+ α7NiPi + α8NiIi + α9PiIi + ui
If we estimate this equation with the Woody’s data, we find that the unad-
justed R2 = .1218. Since N = 33, the chi-square NR2 = 331.12182 = 4.02. 
That’s less than 16.92, the 5-percent critical chi-square value with nine degrees 
of freedom (do you see why it’s nine?), so we once again can’t reject the null 
hypothesis of homoskedasticity.
10.4   Remedies for Heteroskedasticity
The first thing to do if the Breusch–Pagan test or the White test indicates the 
possibility of heteroskedasticity is to examine the equation carefully for speci-
fication errors. Although you should never include an explanatory variable 
simply because a test indicates the possibility of heteroskedasticity, you ought 
to rigorously think through the specification of the equation. If this rethinking 
allows you to discover a variable that should have been in the regression from 
the beginning, then that variable should be added to the equation. Similarly, if 
you had the wrong functional form to begin with, the discovery of heteroske-
dasticity might be the hint you need to rethink the specification and switch to 
the functional form that best represents the underlying theory. However, if there 
are no obvious specification errors, the heteroskedasticity is probably pure in 
nature, and one of the remedies described in this section should be considered.
11. For instance, there is an alternative form of the White test that has many fewer degrees of 
freedom in the auxiliary equation. You perform this alternative White test by replacing all the 
right-hand variables in Equation 10.9 with the fitted Y values and the squares of the fitted Y 
values from the original model. That is, run: e2
i = α0 + α1Yni + α2Yn 2
i + ui with the null hypoth-
esis being α1 = α2 = 0 and the rest of the test being the same. This isn’t as good as the full 
White test, but if the full White test is impossible to run, this may be an excellent alternative. 
For more, see Christopher F. Baum, An Introduction to Modern Econometrics Using Stata (College 
Station, TX: Stata Press, 2006), p. 146.


321
  Remedies for Heteroskedasticity
Heteroskedasticity-Corrected Standard Errors
The most popular remedy for heteroskedasticity is heteroskedasticity-
corrected standard errors, which adjust the estimation of the SE1βn 2s for het-
eroskedasticity while still using the OLS estimates of the slope coefficients. 
The logic behind this approach is powerful. Since heteroskedasticity causes 
problems with the SE1βn 2s but not with the βns, it makes sense to improve 
the estimation of the SE1βn 2s in a way that doesn’t alter the estimates of the 
slope coefficients. This approach is virtually identical to the use of Newey–
West standard errors as a remedy for serial correlation.
Thus, heteroskedasticity-corrected (HC) standard errors are SE1βn 2s 
that have been calculated specifically to avoid the consequences of heteroske-
dasticity. The HC procedure yields an estimator of the standard errors that, 
while they are biased, are generally more accurate than uncorrected standard 
errors for large samples in the face of heteroskedasticity. As a result, the HC 
SE1βn 2s can be used in t-tests and other hypothesis tests in most samples with-
out the errors of inference potentially caused by heteroskedasticity. Typically, 
the HC SE1βn 2s are larger than the OLS SE1βn 2s, thus producing lower t-scores 
and decreasing the probability that a given estimated coefficient will be signifi-
cantly different from zero. The technique was suggested by Halbert White in 
the same article in which he proposed the White test for heteroskedasticity.12
There are a few problems with using heteroskedasticity-corrected standard 
errors. First, the technique works best in large samples, so it’s best to avoid 
HC SE1βn 2s in small samples. Second, details of the calculation of the HC 
SE1βn 2s are beyond the scope of this text and imply a model that is substan-
tially more general than the basic theoretical construct, VAR1ei2 = σ2Zi, of 
this chapter. In addition, not all computer regression software packages cal-
culate heteroskedasticity-corrected standard errors.
Redefining the Variables
Another approach to ridding an equation of heteroskedasticity is to go back 
to the basic underlying theory of the equation and redefine the variables in 
a way that avoids heteroskedasticity. A redefinition of the variables often is 
useful in allowing the estimated equation to focus more on the behavioral 
12. Note that Newey–West standard errors, introduced in Section 9.4, also can be used as HC 
standard errors. Indeed, some econometric software packages provide a choice between the 
White and Newey–West procedures. Unless otherwise noted, however, HC standard errors 
should be assumed to be of the White variety. Most authors refer to this method as HCCM, for 
heteroskedasticity-consistent covariance matrix.


322
Chapter 10  Heteroskedasticity
aspects of the relationship. Such a rethinking is a difficult and discouraging 
process because it appears to dismiss all the work already done. However, 
once the theoretical work has been reviewed, the alternative approaches that 
are discovered are often exciting in that they offer possible ways to avoid 
problems that had previously seemed insurmountable. Be careful, however. 
Redefining your variables is a functional form specification change that can 
dramatically change your equation.
In some cases, the only redefinition that’s needed to rid an equation of 
heteroskedasticity is to switch from a linear functional form to a double-log 
functional form. The double-log form has inherently less variation than the 
linear form, so it’s less likely to encounter heteroskedasticity. In addition, 
there are many research topics for which the double-log form is just as theo-
retically logical as the linear form. This is especially true if the linear form was 
chosen by default, as is often the case.
In other situations, it might be necessary to completely rethink the 
research project in terms of its underlying theory. For example, consider a 
cross-sectional model of the total expenditures by the governments of dif-
ferent cities. Logical explanatory variables to consider in such an analysis are 
the aggregate income, the population, and the average wage in each city. The 
larger the total income of a city’s residents and businesses, for example, the 
larger the city government’s expenditures (see Figure 10.5). In this case, it’s 
not very enlightening to know that the larger cities have larger incomes and 
larger expenditures (in absolute magnitude) than the smaller ones.
Fitting a regression line to such data (see the line in Figure 10.5) also gives 
undue weight to the larger cities because they would otherwise give rise to 
large squared residuals. That is, since OLS minimizes the summed squared 
residuals, and since the residuals from the large cities are likely to be large 
due simply to the size of the city, the regression estimation will be especially 
sensitive to the residuals from the larger cities. This is often called “spurious 
correlation” due to size.
In addition, the residuals may indicate heteroskedasticity. It makes 
sense to consider reformulating the model in a way that will discount 
the scale factor (the size of the cities) and emphasize the underlying 
behavior. In this case, per capita expenditures would be a logical depen-
dent variable. Such a transformation is shown in Figure 10.6. This form 
of the equation places New York and Los Angeles on the same scale as, 
say, Pasadena or New Brunswick, and thus gives them the same weight 
in estimation. If an explanatory variable happened not to be a function 
of the size of the city, however, it would not need to be adjusted to per 
capita terms. If the equation included the average wage of city workers, for 
example, that wage would not be divided through by population in the 
transformed equation.


323
  Remedies for Heteroskedasticity
Suppose your original equation is:
	
EXPi = β0 + β1POPi + β2INCi + β3WAGEi + ei	
(10.10)
where EXPi refers to expenditures, INCi refers to income, WAGEi refers to the 
average wage, and POPi refers to the population of the ith city.
The transformed equation would be13
	
EXPi/POPi = α0 + α1INCi/POPi + α2WAGEi + ui	
(10.12)
0
Income
Small Cities
Large Cities
Expenditures
Slope with
Large Cities
Included
Slope without
Large Cities
Figure 10.5  An Aggregate City Expenditures Function
If city expenditures are explained in an aggregate model, the larger cities play a major 
role in the determination of the coefficient values. Note how the slope would be some-
what lower without the heavy influence of the larger cities. In addition, heteroskedastic-
ity is a potential problem in an aggregate model because the wide range of sizes of the 
dependent variable makes different error term variances more likely.
13. This transformed equation is very similar to the equation for Weighted Least Squares 
(WLS). Weighted Least Squares is a remedy for heteroskedasticity that consists of dividing the 
­entire equation (including the constant and the heteroskedastic error term) by the proportion-
ality factor Z and then re-estimating the equation with OLS. For the example in this section, the 
WLS equation would be:
	
EXPi/POPi = β0/POPi + β1 + β2INCi/POPi + β3WAGEi/POPi + ui	
(10.11)
where the variables and βs in Equation 10.11 are identical to those in Equation 10.10. Divid-
ing through by Z means that u is a homoskedastic error term as long as Z is the correct propor-
tionality factor. This is not a trivial problem, however, and other transformations and HCSEs 
are much easier to use than WLS is, so we no longer recommend the use of WLS.


324
Chapter 10  Heteroskedasticity
where ui is a classical homoskedastic error term. While the directly trans-
formed Equation 10.12 probably avoids heteroskedasticity, such a solution 
should be considered incidental to the benefits of rethinking the equation in 
a way that focuses on the basic behavior being examined.
Note that it’s possible that the reformulated Equation 10.12 could have 
­heteroskedasticity; the error variances might be larger for the observations 
having the larger per capita values for expenditures than they are for smaller 
per capita values. Thus, it is legitimate to suspect and test for heteroske-
dasticity even in this transformed model. Such heteroskedasticity in the 
transformed equation is unlikely, however, because there will be little of the 
variation in size normally associated with heteroskedasticity.
10.5   A More Complete Example
Let’s work through a more complete example involving heteroskedasticity, a 
cross-sectional model of petroleum consumption by state.
0
Income Per Capita
Large and Small Cities
Given Equal Weight
Expenditures Per Capita
Figure 10.6  A Per Capita City Expenditures Function
If city expenditures are explained in a per capita model, then large and small cities have 
equal weights. In addition, heteroskedasticity is less likely, because the dependent variable 
does not vary over a wide range of sizes.


325
  A More Complete Example
Possible explanatory variables include functions of the size of the state 
(such as the number of miles of roadway, the number of motor vehicle reg-
istrations, or the population) and variables that are not functions of the size 
of the state (such as the price of gasoline or the speed limit). Since there is 
little to be gained by including more than one variable that measures the size 
of the state (because such an addition would be theoretically redundant and 
likely to cause needless multicollinearity), and since the speed limit was the 
same for all states (it would be a useful variable in a time-series model, how-
ever) a reasonable model to consider might be:
	
+ 	
-
	
PCONi = β0 + β1REGi + β2PRICEi + ei	
(10.13)
where: PCONi = petroleum consumption in the ith state (trillions of BTUs)
	
 REGi
 = motor vehicle registrations in the ith state (thousands)
	
PRICEi = the price of gasoline in the ith state (cents per gallon)
	
ei
 = a classical error term
The more cars there are registered in a state, we would think, the more 
petroleum would be consumed, while a high gasoline price would decrease 
aggregate gasoline purchases in that state.14 If we now collect data from 2005 
for this example (see Table 10.1) we can estimate:
	
PCONi = 4101 + 0.16REGi - 1885PRICEi	
	
(0.01)	
(750)	
	
t = 	
12.4	
-2.51	
	
N = 50	
R  2 = .76	
(10.14)
This equation seems to have no problems; the coefficients are significant 
in the hypothesized directions, and the overall equation is statistically sig-
nificant. No Durbin–Watson statistic is shown because there is no “natural” 
order of the observations to test for serial correlation (if you’re curious, the 
DW for the order in Table 10.1 is 2.15).
Given the discussion in the previous sections, let’s investigate the possibility 
of heteroskedasticity caused by variation in the size of the states. To test this 
possibility, we obtain the residuals from Equation 10.14, and run Breusch–
Pagan and White tests on them.
h
14. An alternative to using PRICE as an independent variable in this equation is to use 
PRICE*REG or PRICE*POP (where POPi is the population of the ith state). These are more 
sophisticated examples of the interaction terms we introduced in Section 7.4 in our discussion 
of slope dummy variables.


326
Chapter 10  Heteroskedasticity
Table 10.1  Data for the Petroleum Consumption Example
PCON
PRICE
REG
POP
STATE
580
2.11
4545
4548
Alabama
284
2.13
673
663
Alaska
537
2.23
3972
5953
Arizona
377
2.10
1940
2776
Arkansas
3837
2.47
32487
36154
California
463
2.19
1808
4663
Colorado
463
2.17
3059
3501
Connecticut
148
2.07
737
842
Delaware
1940
2.21
15691
17768
Florida
1058
2.09
8063
9133
Georgia
270
2.47
948
1273
Hawaii
139
2.14
1374
1429
Idaho
1313
2.22
9458
12765
Illinois
901
2.19
4955
6266
Indiana
393
2.13
3398
2966
Iowa
434
2.17
2368
2748
Kansas
664
2.14
3428
4173
Kentucky
1610
2.10
3819
4507
Louisiana
262
2.16
1075
1318
Maine
561
2.15
4322
5590
Maryland
734
2.08
5420
6433
Massachusetts
1010
2.24
8247
10101
Michigan
694
2.11
4647
5127
Minnesota
484
2.11
1978
2908
Mississippi
737
2.09
4589
5798
Missouri
161
2.17
1009
935
Montana
231
2.21
1703
1758
Nebraska
242
2.38
1349
2412
Nevada
198
2.08
1174
1307
New Hampshire
1233
1.99
6262
8703
New Jersey
250
2.19
1548
1926
New Mexico
1776
2.23
11863
19316
New York
947
2.14
6148
8672
North Carolina
121
2.19
695
635
North Dakota
1340
2.19
10634
11471
Ohio
545
2.08
3725
3543
Oklahoma
370
2.28
2897
3639
Oregon
1466
2.14
9864
12405
Pennsylvania
102
2.12
812
1074
Rhode Island
517
2.06
3339
4247
South Carolina


327
  A More Complete Example
Before we can run a Breusch–Pagan test, we must decide which variables to 
include on the right-hand side of the auxiliary equation. REG (motor vehicle 
registrations) is a measure of market size, so it’s an obvious proportionality 
factor. On the other hand, PRICE (gasoline prices) seems unlikely to vary 
significantly with the size of the state, so it’s less likely to be a Z. However, 
many researchers automatically include all the independent variables from 
the original equation in the Breusch–Pagan auxiliary equation, so let’s use 
that approach and estimate the auxiliary equation (Equation 10.7) with both 
REG and PRICE:
	
e2
i = 5164290 + 83.33REGi - 2475027PRICEi	
	
(25.1)	
(1476765)	
	
t = 	
3.32	
-1.68	
	
N = 50	
R2 = .197	
(10.15)
The Breusch–Pagan test specifies that we should reject the null hypothesis 
of homoskedasticity 1α1 = α2 = 02 if NR2 7  the appropriate critical chi-
square value. Since N = 50 and R2 = .197, NR2 = 501.1972 = 9.85. If you 
take a look at Table B-6, you’ll see that the 5-percent critical chi-square value 
equals 5.99, so since 9.85 7 5.99, we can reject the null hypothesis of homo-
skedasticity.15 We have heteroskedasticity!
PCON
PRICE
REG
POP
STATE
113
2.20
854
775
South Dakota
782
2.11
4980
5956
Tennessee
5628
2.07
17470
22929
Texas
276
2.12
2210
2490
Utah
86
2.13
508
622
Vermont
965
2.10
6591
7564
Virginia
793
2.28
5598
6292
Washington
255
2.20
1352
1814
West Virginia
597
2.26
4725
5528
Wisconsin
162
2.08
646
509
Wyoming
Source: 2008 Statistical Abstract (U.S. Department of Commerce). 
Datafile = GAS10
15. If we run the Breusch–Pagan test with REG as the only proportionality factor, we also can reject 
the null hypothesis of homoskedasticity at the 5-percent level because the t-score of 2.90 is greater 
than 2.01, the 5-percent two-sided critical t-score with 48 degrees of freedom. (Table B-1 doesn’t 
include a value for 48 degrees of freedom, but we can interpolate to get a critical value of 2.01.)


328
Chapter 10  Heteroskedasticity
To see whether the White test also will detect this heteroskedasticity, we’ll 
need to modify Equation 10.9 to fit our example. The dependent variable will 
be the square of the residuals in Equation 10.14, and the independent vari-
ables will be REG, PRICE, their squares, and their cross-product:
	
ei
2 = α0 + α1REGi + α2PRICEi + α3REGi
2	
	
+ α4PRICEi
2 + α5REGi*PRICEi + ui	
(10.16)
If we estimate Equation 10.16 with the residuals from Equation 10.14 and 
the data from Table 10.1, we obtain an R2 of .85.
Since N = 50, NR2 = 50*.85 = 42.5. As you can confirm by looking at 
Table B-6, the critical chi-square value at the 5-percent level for 5 degrees of 
freedom is 11.07. This means that our decision rule is:
Do not reject the null hypothesis of homoskedasticity if NR2 6 11.07
Reject the null hypothesis of homoskedasticity if NR2 Ú 11.07
NR2 = 42.5 7 11.07, so we can reject the null hypothesis of homoskedasticity.
Since there appears to be heteroskedasticity in the residuals of Equation 
10.14, what should we do? First, we should think through the specification 
of the equation in search of an omitted variable. While there are a number 
of possible omitted variables, it turns out that the heteroskedasticity in the 
equation is pure heteroskedasticity for the most part.
Let’s apply the most popular of our remedies, heteroskedasticity-corrected 
standard errors, to this example. If we start with Equation 10.14 and use 
White’s suggested method for estimating SE1βn 2s that are minimum variance 
(for large samples) in the face of heteroskedasticity, we obtain:
	
PCONi = 4101 + 0.16REGi - 1885PRICEi	
	
10.032         113602	
	
t =   4.85          -1.39	
(10.17)
Compare Equation 10.14 with Equation 10.17. Note that the slope coef-
ficients are identical, as you’d expect, since the HC approach uses OLS to esti-
mate the coefficients. Also note that the HC SE1βn 2s are higher than the OLS 
SE1βn 2s, as is usually but not necessarily the case. While the resulting t-scores 
are lower, they are still reasonably large in the direction we expected, making 
Equation 10.17 very appealing indeed.
A second possible remedy for heteroskedasticity is to change to a double-
log functional form. If we use the data in Table 10.1 to estimate a double-log 
equation, we get:
®


329
  A More Complete Example
	
lnPCONi = -0.32 + 0.90lnREGi - 0.89lnPRICEi	
	
10.042     
11.032	
	
t =         20.3        -0.87	
	
N = 50      R  2 = .89	
(10.18)
As can be seen, switching to logs improves R  2 and the significance of the 
coefficient of lnREG, but the t-score for the coefficient of lnPRICE is below 1. 
We’d normally be concerned about such a low t-score, but the estimated coef-
ficient is in the expected direction, and PRICE unambiguously belongs in the 
equation for theoretical reasons, so there’s no reason to consider the possibil-
ity that PRICE might be irrelevant. As we’d hope, the White test indicates that 
the residuals of Equation 10.18 are indeed homoskedastic.
Finally, an alternative is to rethink the purpose of the regression and refor-
mulate the variables of the equation to try to avoid heteroskedasticity result-
ing from spurious correlation due to size. If we were to rethink Equation 
10.14, we might decide to attempt to explain per capita petroleum consump-
tion, coming up with:
	
PCONi/POPi = β0 + β1REGi/POPi + β2PRICEi + ei	
(10.19)
where POPi is the population of the ith state in thousands of people.
If we estimate Equation 10.19, we obtain:
	
PCONi/POPi = 0.23 + 0.15REGi/POPi - 0.10PRICEi	
(10.20)
	
10.062         
10.102	
	
t =        2.52           -1.00	
	
N = 50    R  2 = .12	
If we compare Equation 10.20 with Equations 10.17 and 10.18, we see that 
this approach is quite different and not necessarily better. The statistical 
properties of Equation 10.20, though not directly comparable to the other 
equations, do not appear as strong as they might16 be, but this is not neces-
sarily the deciding factor. One positive note is that the residuals of Equation 
10.20 do indeed appear to be homoskedastic.
®
16. Petroleum-producing states like Texas, Louisiana, and Alaska consume petroleum products 
for many reasons other than their use in motor vehicles, so it might be tempting to add a vari-
able measuring petroleum production to the equation. A better approach, however, would be 
to limit the dependent variable to the consumption of petroleum for use in motor vehicles. In 
addition, there is evidence that the Statistical Abstract of the United States data for REG may well 
have been incorrect for Colorado. Adjusting for this possible error improves the fit of the per-
capita model dramatically. We are grateful to Ron Michener for both of these insights.


330
Chapter 10  Heteroskedasticity
Which remedy is best: HC standard errors, the double-log functional 
form, or reformulating the equation? Most econometricians would prefer HC 
standard errors, though the sample size of 50 makes it unlikely that the large 
sample properties of HC estimators hold in this case. However, this answer 
could change depending on the underlying theory of your equation. If theory 
strongly supports either the double-log or the reformulated functional form, 
then that model clearly is best. In such a situation, however, it’s worth ask-
ing why the theoretically superior functional form wasn’t chosen in the 
first place. Finally, in the fairly unusual case that t-scores aren’t used to test 
hypotheses or retain variables, then it’s not at all clear that any sort of remedy 
for heteroskedasticity is required at all.
10.6   Summary
1.	
Heteroskedasticity is the violation of Classical Assumption V that 
the observations of the error term are drawn from a distribution 
with a constant variance. Homoskedastic error term observations 
are drawn from a distribution that has a constant variance for all 
observations, and heteroskedastic error term observations are drawn 
from distributions whose variances differ from observation to obser-
vation. Heteroskedasticity occurs most frequently in cross-sectional 
data sets.
2.	
The variance of a heteroskedastic error term is not equal to σ2, a con-
stant. Instead, it equals σ2
i , where the subscript i indicates that the 
variance can change from observation to observation. Many different 
kinds of heteroskedasticity are possible, but a common model is one 
in which the variance changes systematically as a function of some 
other variable, a proportionality factor Z:
VAR1ei2 = σ2Zi
	
The proportionality factor Z is usually a variable related in some way 
to the size or accuracy of the dependent variable.
3.	
Pure heteroskedasticity is a function of the error term of the correctly 
specified regression equation. Impure heteroskedasticity is caused by 
a specification error such as an omitted variable.
4.	
The major consequence of heteroskedasticity is bias in the OLS SE(βn)s, 
causing unreliable hypothesis testing. Pure heteroskedasticity does 
not cause bias in the estimates of the βs themselves.


331
Exercises
5.	
Two popular tests for heteroskedasticity are the Breusch–Pagan test 
and the White test. Both test for heteroskedasticity by analyzing the 
extent to which the squared residuals of the original equation can be 
explained by an auxiliary equation.
6.	
The first step in correcting heteroskedasticity is to check for a speci-
fication error that might be causing impure heteroskedasticity. If the 
specification is as good as possible, then solutions such as HC stan-
dard errors or redefining the variables should be considered.
Exercises
(The answers to the even-numbered exercises are in Appendix A.)
	 1.	 Write the meaning of each of the follow terms without referring to the 
book (or your notes), and compare your definition with the version 
in the text for each.
a.	the Breusch–Pagan test (p. 316)
b.	heteroskedasticity (p. 307)
c.	 heteroskedasticity-corrected standard errors (p. 321)
d.	impure heteroskedasticity (p. 311)
e.	 proportionality factor (p. 310)
f.	 pure heteroskedasticity (p. 307)
g.	the White test (p. 318)
	 2.	 Let’s return to the analysis of the international pharmaceutical indus-
try that we started in Exercise 9 of Chapter 5. That study was cross 
sectional and included countries as large as the United States and as 
small as Luxembourg, so you’d certainly expect heteroskedasticity to 
be a potential problem. Luckily, the dependent variable in the origi-
nal research was Pi, the pharmaceutical price level in the ith country 
divided by that of the United States, so the researchers didn’t encoun-
ter the wide variations in size typically associated with heteroskedas-
ticity. (Do you see why?)
	
	    Suppose, however, that we use the same data set to build a model 
of pharmaceutical consumption:
	
CVi = -15.9 + 0.18Ni + 0.22Pi + 14.3PCi	
	
10.052   10.092    16.42	
	
t =      3.32      2.53        2.24	
	
N = 32    R  2 = .31	
(10.21)
9


332
Chapter 10  Heteroskedasticity
where:  CVi = the volume of consumption of pharmaceuticals in 
the ith country divided by that of the United States
	
Ni   = the population of the ith country divided by that of 
the United States
	
PCi = a dummy variable equal to 1 if the ith country encour-
aged price competition, 0 otherwise
a.	Does heteroskedasticity seem more likely when CV is the depen-
dent variable than when P is the dependent variable? Explain your 
reasoning.
b.	Use the data in Table 5.2 (datafile = DRUGS5) to test for heteroske-
dasticity in Equation 10.21 with both the Breusch–Pagan and the 
White test at the 5-percent level.
c.	 If your answer to part b is heteroskedasticity, estimate HC standard 
errors for Equation 10.21.
d.	Similarly, if you encountered heteroskedasticity, re-estimate Equa-
tion 10.21 using a double-log functional form.
e.	 Similarly, if you encountered heteroskedasticity, reformulate the 
variables in Equation 10.21 to avoid heteroskedasticity and esti-
mate your reformulated equation.
f.	 Which of our three remedies for heteroskedasticity do you think is 
best in this case? Why?
g.	In Chapter 5, we estimated an equation with P as a function of 
CVN (CV per capita), and now we’ve estimated an equation with 
CV as a function of PC. Which Classical Assumption are you worried 
that we might have violated? Explain.
	 3.	 Of all the econometric problems we’ve encountered, heteroskedastic-
ity is the one that seems the most difficult to understand. Close your 
book and attempt to write an explanation of heteroskedasticity in 
your own words. Be sure to include a diagram in your description.
	 4.	 A. Ando and F. Modigliani collected the following data on the income 
and consumption of non-self-employed homeowners:17
17. Albert Ando and Franco Modigliani, “The ’Permanent Income’ and ’Life Cycle’ Hypotheses 
of Saving Behavior: Comparisons and Tests,” in I. Friend and R. Jones, eds. Consumption and 
Saving, Vol. II, 1960, p. 154.


333
Exercises
Income Bracket ($)
Average Income ($)
Average Consumption ($)
      0–999
    556
  2760
1000–1999
  1622
  1930
2000–2999
  2664
  2740
3000–3999
  3587
  3515
4000–4999
  4535
  4350
5000–5999
  5538
  5320
6000–7499
  6585
  6250
7500–9999
  8582
  7460
10000–above
14033
11500
a.	Run a regression to explain average consumption as a function of 
average income.
b.	Use the Breusch–Pagan test to test the residuals from the equation 
you ran in part a for heteroskedasticity at the 5-percent level.
c.	 Run a 5-percent White test on the same residuals.
d.	If the tests run in parts b or c show evidence of heteroskedasticity, 
then what, if anything, should be done about it?
	 5.	 James Stock and Mark Watson suggest a quite different approach to 
heteroskedasticity. They state that “economic theory rarely gives any 
reason to believe that the errors are homoskedastic. It therefore is 
prudent to assume that the errors might be heteroskedastic unless you 
have compelling reasons to believe otherwise.”18 As a result, Stock 
and Watson automatically use HC standard errors without testing 
for heteroskedasticity. In fact, since they adjust every equation for 
heteroskedasticity, they don’t even list homoskedasticity as a Classical 
Assumption.
a.	What do you think? Do you agree with Stock and Watson? Explain 
your reasoning.
b.	If Stock and Watson are right, does this mean that we don’t need to 
learn about heteroskedasticity in the first place? Did you waste your 
time reading this chapter?
18. James Stock and Mark Watson, Introduction to Econometrics (Boston: Pearson, 2015), 
p. 163.


334
Chapter 10  Heteroskedasticity
	 6.	 R. Bucklin, R. Caves, and A. Lo estimated the following double-log 
model to explain the yearly circulation of metropolitan newspapers 
(standard errors in parentheses):19
	
 Cn i = -  8.2 - 0.56Pi + 0.90Ii + 0.76Qi + 0.27Ai + 0.08Si - 0.77 Ti
	
 10.582
 10.142  10.212
 10.142
 10.052
 10.272
N = 50
where:  Ci = yearly circulation of the ith newspaper
	
Pi = the weighted average single copy price of the ith 
newspaper
	
Ii  = the total disposable income of the metropolitan area 
of the ith newspaper
	
Qi = the number of personnel in editorial positions at the 
ith newspaper
	
Ai = the volume of retail advertising in the ith newspaper
	
Si  = amount of competition from suburban dailies in the 
ith newspaper’s region
	
Ti = the number of television stations in the ith news­
paper’s region
	
(All variables are in logarithmic form.)
a.	Hypothesize signs and run t-tests on each of the individual slope 
coefficients.
b.	Does heteroskedasticity seem theoretically likely? Explain.
c.	 Given your responses to parts a and b, what econometric problems 
(out of omitted variables, irrelevant variables, incorrect functional 
form, multicollinearity, serial correlation, and heteroskedasticity) 
appear to exist in this equation?
d.	If you could suggest just one change in the specification of this equa-
tion, what would that change be? Carefully explain your answer.
	 7.	 Let’s investigate the possibility of heteroskedasticity in time-series 
data by looking at a model of the black market for U.S. dollars 
in ­Brazil that was studied by R. Dornbusch and C. Pechman.20 In 
19. R. E. Bucklin, R. E. Caves, and A. W. Lo, “Games of Survival in the U.S. Newspaper Industry,” 
Applied Economics, Vol. 21, pp. 631–650.
20. Rudiger Dornbusch and Clarice Pechman, “The Bid-Ask Spread in the Black Market for 
Dollars in Brazil,” Journal of Money, Credit and Banking, Vol. 17, pp. 517–520. The data for this 
study were not published with the original article but are on the data diskette that accompanies 
William F. Lott and Subhash C. Ray, Applied Econometrics: Problems with Data Sets (Fort Worth: 
Dryden/Harcourt Brace, 1992). The analytical approach of this question also comes from Lott 
and Ray, pp. 169–173.


335
Exercises
particular, the authors wanted to know if the Demsetz-Bagehot bid-
ask theory, previously tested on cross-sectional data from the United 
States, could be extended to time-series data outside the United 
States.21 They estimated the following model on monthly data from 
Brazil for March 1979 through December 1983:
	
+	
+
	
St = β0 + β1It + β2ln11 + Vt2 + et	
(10.22)
where:  St = the average daily spread between the bid and asking prices 
for the U.S. dollar on the Brazilian black market in month t
	
It = the average interest rate in month t
	
Vt = the variance of the daily premium between the black market 
rate and the official exchange rate for the dollar in month t
a.	Use the authors’ data in Table 10.2 (datafile = BID10) to estimate 
Equation 10.22 and test the residuals for positive first-order serial 
correlation.
b.	If serial correlation appears to exist, reestimate Equation 10.22 
using GLS. Do the coefficient estimates change? Which equation 
do you prefer? Why?
c.	 The authors noted that S nearly doubled in size during their sam-
ple period. Does this make you concerned about the possibility of 
heteroskedasticity? Why or why not?
d.	Test the residuals of Equation 10.22 for heteroskedasticity using 
the Breusch–Pagan test. (Hint: A possible proportionality factor is a 
time-trend variable that equals 1 for March 1979 and that increases 
by 1 for each following month.)
e.	 Test the residuals of your GLS version of Equation 10.22 for 
heteroskedasticity. Did running GLS change the possibility of 
heteroskedasticity?
f.	 What remedy would you suggest for any heteroskedasticity that 
might exist in such a time-series model? Be specific.
21. For a review of this literature at the time of Dornbusch and Pechman’s research, see Kalman 
Cohen et al., “Market Makers and the Market Spread: A Review of Recent Literature,” Journal of 
Financial and Quantitative Studies, Vol. 14, No. 4, pp. 813–835.


336
Chapter 10  Heteroskedasticity
Table 10.2   Data on the Brazilian Black Market for Dollars
Month
S
I
V
1979:03
2.248
4.15
20.580
1979:04
2.849
4.04
12.450
1979:05
2.938
2.68
21.230
1979:06
2.418
2.81
26.300
1979:07
2.921
1.92
22.600
1979:08
2.587
2.37
18.750
1979:09
2.312
3.59
20.040
1979:10
2.658
2.03
31.110
1979:11
2.262
2.41
29.040
1979:12
4.056
4.09
20.590
1980:01
3.131
3.28
11.770
1980:02
3.404
2.89
7.900
1980:03
2.835
3.44
6.150
1980:04
3.309
2.43
6.780
1980:05
3.042
2.13
8.550
1980:06
3.417
2.94
13.380
1980:07
2.929
3.19
11.870
1980:08
3.821
3.26
15.560
1980:09
2.753
3.98
24.560
1980:10
2.633
3.69
21.110
1980:11
2.608
4.43
15.000
1980:12
2.168
5.86
7.480
1981:01
2.273
4.36
2.820
1981:02
1.892
5.66
1.540
1981:03
2.283
4.60
1.520
1981:04
2.597
4.42
4.930
1981:05
2.522
5.41
10.790
1981:06
2.865
4.63
17.160
1981:07
4.206
5.46
30.590
1981:08
2.708
5.88
23.900
1981:09
2.324
5.52
20.620
1981:10
2.736
6.07
18.900
1981:11
3.277
5.48
26.790
1981:12
3.194
6.79
29.640
1982:01
3.473
5.46
32.870
1982:02
2.798
6.20
30.660
1982:03
3.703
6.19
40.740
1982:04
3.574
6.06
48.040
1982:05
3.484
6.26
33.510
1982:06
2.726
6.27
23.650


337
Appendix: Econometric Lab #6
10.7   Appendix: Econometric Lab #6
This laboratory assignment is an exercise in the detection and correction of 
heteroskedasticity.
Several years ago, an airplane pilot took econometrics, and for his project 
he estimated a hedonic model of the determinants of used, single-engine air-
plane prices in the year 2000. This lab uses data from his project as the basis 
for an exercise in the detection and correction of heteroskedasticity. The data-
set, PLANES10, consists of the variables in Table 10.3.
Step 1: Use the Data to Estimate the Model with OLS
Use lnpricei as the dependent variable and use all the other variables in 
Table 10.3 as independent variables in your regression. Which variables 
have coefficients that are significant in the expected direction at the 5-percent 
level?
Month
S
I
V
1982:07
4.430
6.89
37.080
1982:08
4.158
7.55
51.260
1982:09
5.633
6.93
60.450
1982:10
5.103
8.14
83.980
1982:11
3.691
7.80
69.490
1982:12
3.952
9.61
68.030
1983:01
3.583
7.01
85.630
1983:02
4.459
7.94
77.060
1983:03
6.893
10.06
71.490
1983:04
5.129
11.82
51.520
1983:05
4.171
11.18
43.660
1983:06
5.047
10.92
59.500
1983:07
8.434
11.72
61.070
1983:08
5.143
9.54
75.380
1983:09
3.980
9.78
72.205
1983:10
4.340
9.91
59.258
1983:11
4.330
9.61
38.860
1983:12
4.350
10.09
33.380
Source: William F. Lott and Subhash C. Ray, Applied Econometrics: Problems with Data Sets 
(Fort Worth: Dryden/Harcourt Brace, 1992). (data diskette) 
Datafile = BID10


338
Chapter 10  Heteroskedasticity
Step 2: Multicollinearity Concerns
Could severe imperfect multicollinearity account for any of the coefficients 
being insignificant at the 5-percent level? If so, which ones? Use simple cor-
relation coefficients and VIFs to support your answer.
Step 3: Heteroskedasticity Concerns
Plot the residuals from your OLS regression against the passenger capacity. 
Do the residuals look heteroskedastic? Explain.
Step 4: Conduct a Breusch–Pagan Test for Heteroskedasticity
Use all the right-hand variables in the original model to run the Breusch–
Pagan auxiliary regression.
Table 10.3   Variable Listing
 
 
Variable
 
 
Description
Hypoth.  
Sign of  
Coef.
lnpricei
Natural log of the price in dollars for used, basic 
single-engine aircraft i
n/a
lnceilingi
Natural log of the service ceiling, or the highest  
possible altitude plane i can fly, in feet
1
lncruisei
Natural log of the cruising speed in miles per hour 
of airplane i
1
lnhorsei
Natural log of horsepower of the engine of airplane i
1
fixgeari
Equal to 1 if aircraft i’s landing gear is fixed (not  
retractable), 0 otherwise
2
lnfueli
Natural log of the volume of the fuel tank of aircraft 
i, in gallons
1
passi
The number of passengers aircraft i can accommo-
date during flight
1
tdragi
Equal to 1 if aircraft i is a tail dragger, 0 otherwise 
(A tail dragger is an aircraft that has a wheel  
connected to its tail—hence, a tail dragger.)
2
wtopi
Equal to 1 if aircraft i has wings above the fuselage, 
0 otherwise
2
lnagei
Natural log of the age in years of aircraft i
2


339
Appendix: Econometric Lab #6
Write the null and alternative hypotheses, compute the test statistic, and 
conduct the test at the 5-percent level. Does heteroskedasticity appear to be 
present?
Step 5: Conduct a White Test for Heteroskedasticity
Test the regression in Step 1 at the 5-percent level for heteroskedasticity using 
the White test. Use the White test command in your regression package to 
run the auxiliary regression and to calculate the test statistic. How many 
variables are on the right-hand side of the auxiliary regression? What is the 
chi-square critical value? According to the White test, does there appear to be 
heteroskedasticity in the model?
Step 6: Estimate the Equation with Heteroskedasticity-Corrected 
Standard Errors
Re-estimate the model in Step 1 with heteroskedasticity-corrected standard 
errors, also known as White standard errors. Are the coefficients and R  2 the 
same?
Step 7: Compare the Results
Compare the OLS results from Step 1 with the heteroskedasticity-corrected 
results in Step 6. For how many of the coefficients are the heteroskedasticity-
corrected standard errors larger than the OLS standard errors? Doesn’t this 
make the equation worse? If so, why bother to estimate the heteroskedasticity-
corrected errors?
