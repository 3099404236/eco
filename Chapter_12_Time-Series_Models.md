# Chapter 12: Time-Series Models

**Pages:** 384-409

---

Time-Series Models
12.1  Distributed Lag Models
12.2  Dynamic Models
12.3  Serial Correlation and Dynamic Models
12.4  Granger Causality
12.5  Spurious Correlation and Nonstationarity
12.6  Summary and Exercises
Chapter 12
The purpose of this chapter is to provide an introduction to a number of 
interesting models that have been designed to cope with and take advantage 
of the special properties of time-series data. Working with time-series data 
often causes complications that simply can’t happen with cross-sectional 
data. Most of these complications involve the order of the observations 
because order matters quite a bit in time-series data but doesn’t matter much 
(if at all) in cross-sectional data.
The most important of the topics concerns a class of dynamic models in 
which a lagged value of the dependent variable appears on the right-hand 
side of the equation. As you will see, the presence of a lagged dependent vari-
able on the right-hand side of the equation implies that the impact of the 
independent variables can be spread out over a number of time periods.
Why would you want to distribute the impact of an independent variable 
over a number of time periods? To see why, consider the impact of advertis-
ing on sales. Most analysts believe that people remember advertising for 
more than one time period, so advertising affects sales in the future as well as 
in the current time period. As a result, models of sales should include current 
and lagged values of advertising, thus distributing the impact of advertising 
over a number of different lags.
While this chapter focuses on such dynamic models, you’ll also learn 
about models in which different numbers of lags appear and we’ll investigate 
364


365
  Distributed Lag Models
how the presence of these lags affects our estimators. The chapter concludes 
with a brief introduction to a topic called nonstationarity. If variables have 
significant changes in basic properties (like their mean or variance) over 
time, they are said to be nonstationary, and it turns out that nonstationary 
variables have the potential to inflate t-scores and measures of overall fit in 
an equation.
12.1   Distributed Lag Models
As described in Section 7.3, lagged independent variables can be used when-
ever you expect X to affect Y after a period of time. For example, if the under-
lying theory suggests that X1 affects Y with a one-time-period lag (but X2 has 
an instantaneous impact on Y), we use equations like:
	
Yt = β0 + β1X1t-1 + β2X2t + et	
(7.14)
Such lags are called simple lags, and the estimation of β1 with OLS is no 
more difficult than the estimation of the coefficients of nonlagged equa-
tions, except for possible impure serial correlation if the lag is misspeci-
fied. Remember, however, that the coefficients of such equations should be 
interpreted carefully. For example, β2 in Equation 7.14 measures the effect 
of a one-unit increase in this time’s X2 on this time’s Y holding last time’s X1 
constant.
A case that’s more complicated than this one-period lag occurs when the 
impact of an independent variable is expected to be spread out over a number 
of time periods. Suppose, for example, that we’re interested in studying the 
impact of a change in the money supply on GDP. Theoretical and empirical 
studies have provided evidence that, because of rigidities in the marketplace, 
it takes time for the economy to react completely to a change in the money 
supply. If it takes two years, some of the effect will take place immediately, 
some will take place with a lag of one year, and the rest will occur with a lag 
of two years. In such a case, the appropriate econometric model would be:
	
Yt = β0 + β1Xt + β2Xt-1 + β3Xt-2 + et	
(12.1)
where Y would be GDP and X would be the money supply. The right-hand 
side of Equation 12.1 is unusual, because X appears three times, each with a 
different lag, distributing the impact of X over a number of time periods. This 
is a distributed lag model; it explains the current value of Y as a function of 
current and past values of X.
Can you think of another example of a dependent variable that might be 
appropriately explained with a distributed lag? For instance, is your grade on 


366
Chapter 12  Time-Series Models
an econometrics exam a function only of how much you studied the night 
before the test, or is it impacted by your work during the previous days and 
weeks? Most people would agree that with a few notable exceptions, a distrib-
uted lag model would indeed be a good way to measure the impact of study-
ing on an exam grade.
The estimation of Equation 12.1 with OLS typically is straightforward. 
There will be some unavoidable multicollinearity between the Xs, but oth-
erwise a distributed lag model like Equation 12.1 will be quite useful in a 
variety of applications.
However, the impact of X on Y often can be expected to continue over a 
large number of time periods, so in many cases we’ll need more lagged values 
of X than are shown in Equation 12.1. If we were building a quarterly model 
of the impact of a change in the money supply on GDP, for example, then 
we’d need quite a few lagged independent variables, and a more general dis-
tributed lag equation would be appropriate:
	
Yt = α0 + β0Xt + β1Xt-1 + β2Xt-2 + g + βpXt-p + et	
(12.2)
where p is the maximum number of periods by which X is lagged. In our 
quarterly GDP model, p might be as high as 10 or 11. (Note that in order to 
have the subscript of β equal the lag in X, we’ve defined the constant term as 
α0 and β0 now is a slope coefficient.)
Take a careful look at Equation 12.2. The slope coefficients β0 through 
βp measure the effects of the various lagged values of X on the current 
value of Y (holding constant the other independent variables in the equa-
tion). In most economic applications, including our GDP example, we’d 
expect the impact of X on Y to decrease as the length of the lag (indicated 
by the subscript of the β) increases. As a result, we’d always expect β0 and 
β1 to be larger in absolute value than β9 or β10.
Unfortunately, the estimation of Equation 12.2 with OLS causes a number 
of problems:
1.	 The various lagged values of X are likely to be severely multicollinear, 
making coefficient estimates imprecise.
2.	 In large part because of this multicollinearity, there is no guarantee that 
the estimated βs will follow the smoothly declining pattern that economic 
theory would suggest. Instead, it’s quite typical for the estimated coeffi-
cients of Equation 12.2 to follow a fairly irregular pattern, for example:
	
βn 0 = 0.26  βn 1 = 0.07  βn 2 = 0.17  βn 3 = -  0.03  βn 4 = 0.08
3.	 The degrees of freedom tend to decrease, sometimes substantially, for 
two reasons. First, we have to estimate a coefficient for each lagged X, 
thus increasing K and lowering the degrees of freedom (N 2 K 2 1). 


367
  Dynamic Models
Second, unless data for lagged Xs outside the sample are available, we 
have to decrease the sample size by 1 for each lagged X we calculate, 
thus lowering the number of observations, N, and therefore the degrees 
of freedom.
As a result of these problems with OLS estimation of distributed lag equa-
tions like Equation 12.2, it’s standard practice to consider a simplifying 
assumption in such situations. The most commonly used simplification is to 
replace all the lagged independent variables with a lagged value of the depen-
dent variable, and we’ll call that kind of equation a dynamic model.
12.2   Dynamic Models
The simplest dynamic model is:
	
Yt = α0 + β0Xt + λYt-1 + ut	
(12.3)
Note that Y is on both sides of the equation! Luckily, the subscripts are differ-
ent in that the Y on the left-hand side is Yt, and the Y on the right-hand side 
is Yt−1. It’s this difference in time period that makes the equation dynamic. 
Thus, the simplest dynamic model is an equation in which the current 
value of the dependent variable Y is a function of the current value of X and 
a lagged value of Y itself. Such a model with a lagged dependent variable is 
often called an autoregressive equation.
Let’s look at Equation 12.3 to try to see why it can be used to represent 
a distributed lag model or any model in which the impact of X on Y is dis-
tributed over a number of lags. Suppose that we lag Equation 12.3 one time 
period:
	
Yt-1 = α0 + β0Xt-1 + λYt-2 + ut-1	
(12.4)
If we now substitute Equation 12.4 for Yt-1 in Equation 12.3, we get:
	
Yt = α0 + β0Xt + λ1α0 + β0Xt-1 + λYt-2 + ut-12 + ut	
(12.5)
or
	
Yt = 1α0 + λα02 + β0Xt + λβ0Xt-1 + λ2Yt-2 + 1λut-1 + ut2	 (12.6)
If we do this one more time (that is, if we lag Equation 12.3 two time peri-
ods, substitute it into Equation 12.5, and rearrange), we get:
	
Yt = α0* + β0Xt + λβ0Xt-1 + λ2β0Xt-2 + λ3Yt-3 + ut*	
(12.7)


368
Chapter 12  Time-Series Models
where α0* is the new (combined) intercept and ut* is the new (combined) 
error term. We’ve shown that a dynamic model can indeed be used to repre-
sent a distributed lag model!
In addition, note that the coefficients of the lagged Xs follow a clear pat-
tern. To see this, let’s go back to Equation 12.2:
	
Yt = α0 + β0Xt + β1Xt-1 + β2Xt-2 + g + βpXt-p + et	
(12.2)
and compare the coefficients in Equation 12.2 to those in Equation 12.7. We get:
	
 β1 = λβ0
	
 β2 = λ2β0
	
 β3 = λ3β0
	
.
	
.
	
.
	
 βp = λpβ0	
(12.8)
As long as λ is between 0 and 1, these coefficients will indeed smoothly 
decline,1 as shown in Figure 12.1.
Dynamic models like Equation 12.3 avoid the three major problems 
with distributed lag equations that we outlined in the previous section. The 
degrees of freedom have increased dramatically, and the multicollinearity 
problem has disappeared. If ut is well behaved, OLS estimation of Equation 
12.3 can be shown to have desirable properties for large samples. How large 
is “large enough”? Our recommendation, based more on experience than 
proof, is to aim for a sample of at least 50 observations. The smaller the sam-
ple, the more likely you are to encounter bias. In particular, estimates of λ 
will be biased downward, and the bias will be especially severe for larger val-
ues of λ and in the presence of additional independent variables, even irrel-
evant ones. As a result, samples below 30 should be avoided, in part because 
of this bias and in part because hypothesis testing can become unreliable.2
In addition to this sample size issue, dynamic models face another seri-
ous problem. It turns out that serial correlation almost surely will cause bias 
in the OLS estimates of dynamic models. This problem will be discussed in 
Section 12.3.
1. This model is sometimes referred to as a Koyck distributed lag model because it was origi-
nally developed by L. M. Koyck in Distributed Lags and Investment Analysis (Amsterdam: North-
Holland Publishing, 1954).
2. David Grubb and James Symons, “Bias in Regressions with a Lagged Dependent Variable,” 
Econometric Theory, Vol. 3, No. 3, pp. 371–386.


369
  Dynamic Models
An Example of a Dynamic Model
As an example of a dynamic model, let’s look at an aggregate consumption 
function from a macroeconomic equilibrium GDP model. Many econo-
mists argue that in such a model, consumption (COt) is not just an instan-
taneous function of disposable income (YDt). Instead, they believe that 
­current consumption is also influenced by past levels of disposable income 
(YDt-1, YDt-2, etc.):
	
COt = α0 + β0YDt + β1YDt-1 + β2YDt-2 + g + βpYDt-p + et	
(12.9)
Such an equation fits well with simple models of consumption, but it makes 
sense only if the coefficients of past levels of income decrease as the length of 
the lag increases. That is, the impact of lagged income on current consump-
tion should decrease as the lag gets bigger. Thus we’d expect the coefficient of 
YDt-2 to be less than the coefficient of YDt-1, and so on.
As a result, most econometricians would model Equation 12.9 with a 
dynamic model:
	
COt = α0 + β0YDt + λCOt-1 + ut	
(12.10)
0
1
2
3
4
l 5 0.75
l 5 0.50
l 5 0.02
5
6
7
1.0
0.5
Relative Weight of Lagged Variable
Time Period of Lag
Figure 12.1  Geometric Weighting Schemes for Various Dynamic Models
As long as λ is between 0 and 1, a dynamic model has the impact of the independent 
variable declining as the length of the lag increases.


370
Chapter 12  Time-Series Models
To estimate Equation 12.10, we use data from Section 14.3, where we will 
build a small macromodel of the U.S. economy from 1976 through 2007. 
The OLS estimates of Equation 12.10 for this data set are (standard errors in 
parentheses):
	
COt = - 266.6 + 0.46YDt + 0.56COt-1	
(12.11)
	
10.102     10.102
	
t = 4.70       5.66	
	
R  2 = .999  N = 32  (annual 1976–2007)	
If we substitute βn 0 = 0.46 and λn = 0.56 into Equation 12.3 for i = 1, we 
obtain βn 1 = βn 0λn 1 = 10.46210.5621 = 0.26. If we continue this process, it 
turns out that Equation 12.11 is equivalent to:
	
COt = -  605.91 + 0.46YDt + 0.26YDt-1 + 0.14YDt-2
	
 + 0.08YDt-3 + g	
(12.12)
As can be seen, the coefficients of YD in Equation 12.12 do indeed decline as 
we’d expect in a dynamic model.
To compare this estimate with an OLS estimate of the same equation with-
out the dynamic model format, we’d need to estimate a distributed lag equa-
tion with at least three lagged variables.
	
COt = α0 + β0YDt + β1YDt-1 + β2YDt-2 + β3YDt-3 + et	
(12.13)
If we estimate Equation 12.13 using the same data set, we get:
COt = - 695.89 + 0.73YDt + 0.39YDt-1 + 0.006YDt-2 - 0.08YDt-3
(12.14)
How do the coefficients of Equation 12.14 look? As the lag increases, the coef-
ficients of YD decrease sharply, actually going negative for t−3. Neither eco-
nomic theory nor common sense leads us to expect this pattern. Such a poor 
result is due to the severe multicollinearity between the lagged Xs. Most econo-
metricians therefore estimate consumption functions with a lagged dependent 
variable simplification scheme like the dynamic model in Equation 12.10.
An interesting interpretation of the results in Equation 12.11 concerns the 
long-run multiplier implied by the model. The long-run multiplier measures 
the total impact of a change in income on consumption after all the lagged 
effects have been felt. One way to get this estimate would be to add up all the 
βns, but an easier alternative is to calculate βn 031>11 - λn24, which in this case 
equals 0.4631>11 - 0.5624 or 1.05. A sample of this size is likely to encoun-
ter small sample bias, however, so we shouldn’t overanalyze the results. For 
more on this data set and the other equations in the model, see Section 14.3. 
For more on testing and adjusting dynamic equations like Equation 12.11 for 
serial correlation, let’s move on to the next section.
9
9
9


371
  Serial Correlation and Dynamic Models
12.3   Serial Correlation and Dynamic Models
The consequences of serial correlation depend crucially on the type of model 
we’re talking about. For a distributed lag model such as Equation 12.2, serial 
correlation has the effects outlined in Section 9.3: Serial correlation causes: 
(1) OLS to no longer be the minimum variance unbiased estimator, (2) the 
SE(βn)s to be biased, and (3) no bias in the OLS βns themselves.
For dynamic models such as Equation 12.3, however, all this changes, and 
serial correlation does indeed cause bias in the βns produced by OLS. Com-
pounding this is the fact that the detection of and remedies for serial correla-
tion that we discussed in Chapter 9 need to be modified in the presence of a 
lagged dependent variable.
Serial Correlation Causes Bias in Dynamic Models
If an equation with a lagged dependent variable as an independent variable 
has a serially correlated error term, then OLS estimates of the coefficients will 
be biased, even in large samples.
To see where this bias comes from, let’s start with a dynamic model: 
	
Yt = α0 + β0Xt + λYt-1 + ut	
(12.3)
and lag it one time period:
	
c	
c	
	
Yt-1 = α0 + β0Xt-1 + λYt-2 + ut-1	
(12.15)
As you can see from the upward-pointing arrows above Equation 12.15, if 
ut-1 is positive, then Yt-1 will be higher than it would have been otherwise.
In addition, if ut is serially correlated, then we know that:
	
c	
c
	
ut = ρut-1 + et	
(12.16)
where et is a classical error term with an expected value of zero. As you can 
see from the arrows above Equation 12.16, if ut-1 is positive, then ut will be 
higher than it would have been otherwise as long as ρ is positive, as it typi-
cally is in economic applications.
If we add the arrows from Equations 12.15 and 12.16 to Equation 12.3, 
we get:
	
c	
c
	
Yt = α0 + β0Xt + λYt-1 + ut	
(12.3)
Take a look at the arrows in Equation 12.3. Yt-1 and ut are correlated! Such 
a correlation violates Classical Assumption III, which assumes that the error 


372
Chapter 12  Time-Series Models
term is not correlated with any of the explanatory variables. (If ut-1 is nega-
tive, then both ut and Yt-1 will be lower than they would have been other-
wise, which again violates Classical Assumption III.)
The consequences of this correlation include biased estimates, in particu-
lar of the coefficient λ, because OLS attributes to Yt-1 some of the change in 
Yt actually caused by ut. In essence, the uncorrected serial correlation acts like 
an omitted variable (ut-1). Since an omitted variable causes bias whenever it 
is correlated with one of the included independent variables, and since ut-1 
is correlated with Yt-1, the combination of a lagged dependent variable and 
serial correlation causes bias in the coefficient estimates. This bias is in addi-
tion to the bias mentioned on page 368.
Testing for Serial Correlation in Dynamic Models
If serial correlation causes bias in a dynamic model, then tests for serial corre-
lation are obviously important. Unfortunately, however, the Durbin–Watson 
test is potentially invalid for an equation that contains a lagged dependent 
variable as an independent variable because the Durbin–Watson statistic is 
biased toward 2 in a dynamic equation. This bias toward 2 means that serial 
correlation in a dynamic model is more likely to evade detection by the 
Durbin–Watson test.3
Luckily, the Lagrange Multiplier (LM) serial correlation test of Section 9.4 
still is valid even in the face of a lagged dependent variable. Using the Lagrange 
Multiplier to test for serial correlation in a typical dynamic model involves 
three steps that should seem familiar:
1.	 Obtain the residuals from the estimated equation:
	
et = Yt - Ynt = Yt - αn 0 - βn 0X1t - λn Yt-1	
(12.17)
2.	 Use these residuals as the dependent variable in an auxiliary equation 
that includes as independent variables all those on the right-hand side 
of the original equation as well as the lagged residuals:
	
et = a0 + a1Xt + a2Yt-1 + a3et-1 + ut	
(12.18)
3. The opposite is not a problem. A Durbin−Watson test that indicates serial correlation in the 
presence of a lagged dependent variable, despite the bias toward 2, is an even stronger affirma-
tion of serial correlation.


373
  Serial Correlation and Dynamic Models
3.	 Estimate Equation 12.18 using OLS and then test the null hypothesis 
that a3 = 0 with the following test statistic:
	
LM = NR2	
(12.19)
	
where N is the sample size and R2 is the unadjusted coefficient of de-
termination, both of the auxiliary equation, Equation 12.18. For large 
samples, NR2 has a chi-square distribution with degrees of freedom 
equal to the number of restrictions in the null hypothesis (in this case, 
one). If NR2 is greater than the critical chi-square value from Statistical 
Table B-6, then we reject the null hypothesis that a3 = 0 and conclude 
that there is indeed serial correlation in the original equation.
As an example of testing for serial correlation in a dynamic model, let’s 
run a Lagrange Multiplier (LM) serial correlation test on Equation 12.11, the 
consumption function we estimated in the previous section. If we estimate 
the auxiliary equation for that model, we get an R2 of .4025 which, when 
multiplied by the sample size of 31 (do you see why it’s 31 and not 32?), 
produces an NR2 of 12.48. 12.48 is greater than 3.84, the 5-percent critical 
chi-square value with one degree of freedom, so we have strong evidence of 
serial correlation in Equation 12.11. What should we do?
Correcting for Serial Correlation in Dynamic Models
If the Lagrange Multiplier test indicates serial correlation in a dynamic 
model, the first step is to consider the possibility that the serial correlation is 
impure, perhaps caused by omission of a relevant variable and/or by failure 
to capture the actual distributed lag pattern accurately.
If the serial correlation appears to be pure, then the theoretically preferred 
solution is to transform the equation so as to eliminate the serial correlation 
and re-estimate the model. The required transformation is quite similar to 
the Generalized Least Squares approach to serial correlation described in Sec-
tion 9.5. Unfortunately, the iterative nonlinear estimation of the transformed 
equation is well beyond the scope of this text, so it’s not a realistic alternative 
for most readers.4 Instead, our suggestion is to use one of two alternatives, 
depending on the underlying theory of the model and the size of the sample.
If theory indicates that only a few lagged values of X are meaningful in 
explaining Y, then a potential way to avoid the bias due to serial correlation 
4. Readers interested in this approach should see Sean Becketti, “Introduction to Time Series 
Using Stata” (College Station: Stata Press, 2013), pp. 192–195.


374
Chapter 12  Time-Series Models
is to estimate a distributed lag model (Equation 12.2 with p = 1 or 2) 
instead of a dynamic model. The distributed lag model will have potential 
multicollinearity but will not likely face the other problems typically associ-
ated with distributed lag models because p is so low. Most econometricians 
would prefer to deal with the consequences of multicollinearity than to face 
bias, so this is an improvement. There’s a second advantage to distributed 
lags. The Xt-p terms, in essence, are acting as proxies for Yt-1. As we’ll learn 
in Chapter 14, such proxies are similar to instrumental variables, and they are 
especially useful because they will eliminate bias if they’re uncorrelated with 
the error term.
In a small sample, the best approach may well be to continue to use OLS 
even in the face of serial correlation in a dynamic model. For a nontrivial 
subset of real-world examples, OLS actually outperforms more sophisticated 
techniques. One reason is that in a small sample, the estimation bias in λ men-
tioned in Section 12.2 and the bias introduced by serial correlation often are 
of opposite signs, so they offset each other. As a result, OLS can do better than 
a technique that eliminates only the bias caused by serial correlation.5 The 
second reason is that there’s evidence from Monte Carlo studies that the size of 
the bias introduced by serial correlation in small samples often is fairly low.6
To sum, unless you’re comfortable with iterative nonlinear least squares, 
our suggestion for dealing with serial correlation in dynamic models depends 
on theory and the sample size. If theory calls for very few lagged Xs, we sug-
gest the distributed lag approach. If the sample is small, we think continuing 
to use OLS, even in the face of serial correlation, presents the best alternative. 
If both the sample and the meaningful number of lagged Xs are large, we’d 
recommend using distributed lags because of the benefits of the instrumental 
variable approach.
12.4   Granger Causality
One application of distributed lag models is to provide evidence about the 
direction of causality in economic relationships. Such a test is useful when we 
know that two variables are related but we don’t know which variable causes 
the other to move. For example, most economists believe that increases in the 
5. Asatoshi Maeshiro, “Teaching Regressions with a Lagged Dependent Variable and Autocor-
related Disturbances,” Journal of Economic Education, Vol. 27, No. 1, pp. 72–84.
6. Luke Keele and Nathan Kelly, “Dynamic Models for Dynamic Theories: The Ins and Outs of 
Lagged Dependent Variables,” Political Analysis, Vol. 14, No. 2, pp. 186–205.


375
  Granger Causality
money supply stimulate GDP, but others feel that increases in GDP eventu-
ally lead the monetary authorities to increase the money supply. Who’s right?
One approach to such a question of indeterminate causality is to theorize 
that the two variables are determined simultaneously. We’ll address the esti-
mation of simultaneous equation models in Chapter 14. A second approach 
to the problem is to test for what is called “Granger causality.”
How can we claim to be able to test for causality? After all, didn’t we say in 
Chapter 1 that even though most economic relationships are causal in nature, 
regression analysis can’t prove such causality? The answer is that we don’t 
actually test for theoretical causality; instead, we test for Granger causality.
Granger causality, or precedence, is a circumstance in which one time-
series variable consistently and predictably changes before another variable.7 
Granger causality is important because it allows us to analyze which variable 
precedes or “leads” the other, and, as we shall see, such leading variables are 
extremely useful for forecasting purposes.
Despite the value of Granger causality, however, we shouldn’t let ourselves 
be lured into thinking that it allows us to prove economic causality in any 
rigorous way. If one variable precedes (“Granger causes”) another, we can’t 
be sure that the first variable “causes” the other to change.8 As a result, even 
if we’re able to show that event A always happens before event B, we have not 
shown that event A “causes” event B.
There are a number of different tests for Granger causality, and all the vari-
ous methods involve lagged dependent variables in one way or another.9 Our 
preference is to use an expanded version of a test originally developed by 
Granger. Granger suggested that to see if A Granger-caused Y, we should run:
	 Yt = β0 + β1Yt-1 + g + βpYt-p + α1At-1 + g + αpAt-p + et	
(12.20)
7. See C. W. J. Granger, “Investigating Causal Relations by Econometric Models and Cross-
Spectral Methods,” Econometrica, Vol. 37, No. 3, pp. 424−438.
8. In a previous edition, we ended this paragraph by saying, “For example, Christmas cards 
typically arrive before Christmas, but it’s clear that Christmas wasn’t caused by the arrival of the 
cards.” However, this isn’t a true example of Granger causality, because the date of Christmas 
is fixed and therefore isn’t a “time-series variable.” See Erdal Atukeren, “Christmas cards, Easter 
bunnies, and Granger-causality,” Quality & Quantity, Vol. 42, No. 6, Dec. 2008, pp. 835–844. For 
an in-depth discussion of causality, see Kevin Hoover, Causality in Macroeconomics (Cambridge: 
Cambridge University Press, 2001).
9. See John Geweke, R. Meese, and W. Dent, “Comparing Alternative Tests of Causality in 
Temporal Systems,” Journal of Econometrics, Vol. 21, pp. 161−194, and Rodney Jacobs, Edward 
Leamer, and Michael Ward, “Difficulties with Testing for Causation,” Economic Inquiry, Vol. 17, 
No. 3, pp. 401−413.


376
Chapter 12  Time-Series Models
and test the null hypothesis that the coefficients of the lagged As (the αs) 
jointly equal zero.10 If we can reject this null hypothesis using the F-test, then 
we have evidence that A Granger-causes Y. Note that if p = 0, Equation 12.20 
is similar to the dynamic model, Equation 12.3.
Applications of this test involve running two Granger tests, one in each 
direction. That is, run Equation 12.20 and also run:
	  At = β0 + β1At-1 + g + βpAt-p + α1Yt-1 + g + αpYt-p + et	
(12.21)
testing for Granger causality in both directions by testing the null hypothesis 
that the coefficients of the lagged Ys (again, the αs) jointly equal zero. If the 
F-test is significant for Equation 12.20 but not for Equation 12.21, then we 
can conclude that A Granger-causes Y.
12.5   Spurious Correlation and Nonstationarity
One problem with time-series data is that independent variables can appear 
to be more significant than they actually are if they have the same underly-
ing trend as the dependent variable. In a country with rampant inflation, for 
example, almost any nominal variable will appear to be highly correlated 
with all other nominal variables. Why? Nominal variables are unadjusted 
for inflation, so every nominal variable will have a powerful inflationary 
component. This inflationary component will usually outweigh any real 
causal relationship, making nominal variables appear to be correlated even 
if they aren’t.
Such a problem is an example of spurious correlation, a strong relation-
ship between two or more variables that is not caused by a real underlying 
causal relationship. If you run a regression in which the dependent variable 
and one or more independent variables are spuriously correlated, the result 
is a spurious regression, and the t-scores and overall fit of such spurious regres-
sions are likely to be overstated and untrustworthy.
There are many causes of spurious correlation. In a cross-sectional data 
set, for example, spurious correlation can be caused by dividing both the 
dependent variable and at least one independent variable by a third variable 
that varies considerably more than do the others. The focus of this section, 
however, will be on time-series data and in particular on spurious correlation 
caused by nonstationary time series.
10. Such a joint test requires the use of the F-test of Section 5.6.


377
  Spurious Correlation and Nonstationarity
Stationary and Nonstationary Time Series
A stationary series is one whose basic properties, for example, its mean and 
its variance, do not change over time. In contrast, a nonstationary series has 
one or more basic properties that do change over time. For instance, the real 
per capita output of an economy typically increases over time, so it’s nonsta-
tionary. By contrast, the growth rate of real per capita output often does not 
increase over time, so this variable is stationary even though the variable it’s 
based on, real per capita output, is nonstationary. A time series can be non-
stationary even with a constant mean if another property, such as the vari-
ance, changes over time.
More formally, a time-series variable, Xt, is stationary if:
1.	 the mean of Xt is constant over time,
2.	 the variance of Xt is constant over time, and
3.	 the simple correlation coefficient between Xt and Xt-k depends on the 
length of the lag (k) but on no other variable (for all k).11
If one or more of these properties is not met, then Xt is nonstationary. 
And if a series is nonstationary, that problem is referred to as nonstationarity.
Although our definition of a stationary series focuses on stationary and 
nonstationary variables, it’s important to note that error terms (and, therefore, 
residuals) also can be nonstationary. In fact, we’ve already had experience 
with a nonstationary error term. Many cases of heteroskedasticity in time-
series data involve an error term with a variance that tends to increase with 
time. That kind of heteroskedastic error term is also nonstationary!
The major consequence of nonstationarity for regression analysis is spuri-
ous correlation that inflates R2 and the t-scores of the nonstationary inde-
pendent variables, which in turn leads to incorrect model specification. This 
occurs because the regression estimation procedure attributes to the nonsta-
tionary Xt changes in Yt that were actually caused by some factor (trend, for 
example) that also affects Xt. Thus, the variables move together because of 
the nonstationarity, increasing R2 and the relevant t-scores. This is especially 
11. There are two different definitions of stationarity. The particular definition we use here is a 
simplification of the most frequently cited definition, referred to by various authors as weak, 
wide-sense, or covariance stationarity. In addition, there are many models of nonstationarity, 
for example ARCH and GARCH, that are significantly more sophisticated than the model of 
nonstationarity introduced in this section.


378
Chapter 12  Time-Series Models
important in macroeconometrics, and the macroeconomic literature includes 
many articles that examine various series for signs of nonstationarity.12
Some variables are nonstationary mainly because they increase rapidly 
over time. Spurious regression results involving these kinds of variables often 
can be avoided by the addition of a simple time trend 1t = 1, 2, 3, c , T2 
to the equation as an independent variable.
Unfortunately, many economic time-series variables are nonstationary 
even after the removal of a time trend. This nonstationarity often takes the 
form of the variable behaving as though it were a “random walk.” A random 
walk is a time-series variable in which the next period’s value equals this 
period’s value plus a stochastic error term. A random-walk variable is nonsta-
tionary because it can wander up and down without an inherent equilibrium 
and without approaching a long-term mean of any sort.
To get a better understanding of how a random walk gives rise to nonsta-
tionarity, let’s suppose that Yt is generated by an equation that includes only 
past values of itself (an autoregressive equation):
	
Yt = γYt-1 + vt	
(12.22)
where vt is a classical error term.
Take a look at Equation 12.22. Can you see that if 0 γ0 6 1, then the 
expected value of Yt will eventually approach 0 (and therefore be stationary) 
as the sample size gets bigger and bigger? (Remember, since vt is a classical 
error term, its expected value = 0.) Similarly, can you see that if 0 γ0 7 1, 
then the expected absolute value of Yt will continuously increase, making Yt 
nonstationary? This is nonstationarity due to a trend, but it still can cause 
spurious regression results.
Most importantly, what about if 0 γ0 = 1? In this case,
	
Yt = Yt-1 + vt	
(12.23)
It’s a random walk! The expected value of Yt does not converge on any value, 
meaning that it is nonstationary. This circumstance, where γ = 1 in Equation 
12.23 (or similar equations), is called a unit root. If a variable has a unit 
root, then Equation 12.23 holds, and the variable follows a random walk and 
is nonstationary. The relationship between unit roots and nonstationarity is so 
strong that some econometricians use the words interchangeably, even though 
they recognize that many factors other than unit roots can cause nonstationarity.
12. See, for example, C. R. Nelson and C. I. Plosser, “Trends and Random Walks in Macroeco-
nomics Time Series: Some Evidence and Implication,” Journal of Monetary Economics, Vol. 10, 
pp. 169−182, and J. Campbell and N. G. Mankiw, “Permanent and Transitory Components in 
Macroeconomic Fluctuations,” American Economic Review, Vol. 77, No. 2, pp. 111−117.


379
  Spurious Correlation and Nonstationarity
Spurious Regression
As noted at the beginning of this section, if the dependent variable and at 
least one independent variable in an equation are trending, as they will if 
they contain unit roots, it’s possible for the results of an OLS regression to be 
spurious.13
Consider the linear regression model
	
Yt = α0 + β0Xt + ut	
(12.24)
If both X and Y are nonstationary, then they can be highly correlated for non-
causal reasons, and our standard regression inference measures will be very 
misleading in that they’ll overstate R  2 and the t-score for βn 0.
For example, take a look at the following estimated equation:
	
PRICEt = -27.8 + 0.070TUITIONt
	
10.0062
	
t = 11.4
	
R  2 = .94  T = 101annual2	
(12.25)
The R  2 of this equation and the t-score for the coefficient of TUITION are 
clearly significant, but what are the definitions of the variables? Well, PRICE 
is the price of a gallon of gasoline in Portland, Oregon, and TUITION is the 
tuition for a semester of study at Occidental College (Oxy) in Los Angeles (both 
measured in nominal dollars). Is it possible that an increase in the tuition at 
Oxy caused gas prices in Portland to go up? Not unless every Oxy student was 
the child of a Portland gas station owner! What’s going on? Well, this regression 
is from the 1970s, a decade of inflation, so any nominally measured variables 
are likely to result in an equation that fits as well as Equation 12.25. Both vari-
ables are nonstationary, and this particular regression result clearly is spurious.
To avoid spurious regression results, it’s crucial to be sure that time-series 
variables are stationary before running regressions.
The Dickey–Fuller Test
To ensure that the equations we estimate are not spurious, it’s important to 
test for nonstationarity. If we can be reasonably sure that all the variables are 
stationary, then we need not worry about spurious regressions. How can you 
tell if a time series is nonstationary? The first step is to visually examine the 
h
13. See C. W. J. Granger and P. Newbold, “Spurious Regression in Econometrics,” Journal of 
Econometrics, Volume 2, pp. 111–120.


380
Chapter 12  Time-Series Models
data. For many time series, a quick glance at the data (or a diagram of the 
data) will tell you that the mean of a variable is increasing dramatically over 
time and that the series is nonstationary.
After this trend has been removed, the standard method of testing for non-
stationarity is the Dickey–Fuller test,14 which examines the hypothesis that 
the variable in question has a unit root15 and, as a result, is likely to benefit 
from being expressed in first-difference form.
To best understand how the Dickey–Fuller test works, let’s return to the 
discussion of the role that unit roots play in the distinction between station-
arity and nonstationarity. Recall that we looked at the value of γ in Equation 
12.22 to help us determine if Y was stationary or nonstationary:
	
Yt = γYt-1 + vt	
(12.22)
We decided that if 0 γ0 6 1, then Y is stationary, and that if 0 γ0 7 1, then Yt 
is nonstationary. However, if 0 γ0 = 1, then Yt is nonstationary due to a unit 
root. Thus we concluded that the autoregressive model is stationary if 0 γ0 6 1 
and nonstationary otherwise.
From this discussion of stationarity and unit roots, it makes sense to esti-
mate Equation 12.22 and determine if 0 γ0 6 1 to see if Y is stationary, and 
that’s almost exactly how the Dickey–Fuller test works. First, we subtract Yt−1 
from both sides of Equation 12.22, yielding:
	
1Yt - Yt-12 = 1γ - 12Yt-1 + vt	
(12.26)
If we define ∆Yt = Yt - Yt-1 then we have the simplest form of the Dickey–
Fuller test:
	
∆Yt = β1Yt-1 + vt	
(12.27)
where β1 = γ - 1. The null hypothesis is that Yt contains a unit root and is 
therefore nonstationary, and the alternative hypothesis is that Yt is stationary. 
If Yt contains a unit root, γ = 1 and β1 = 0. If Yt is stationary, 0 γ0 6 1 and 
β1 6 0. Hence we construct a one-sided t-test on the hypothesis that β1 = 0:
	
H0: β1 = 0
	
HA: β1 6 0
14. D. A. Dickey and W. A. Fuller, “Distribution of the Estimators for Autoregressive Time-Series 
with a Unit Root,” Journal of the American Statistical Association, Vol. 74, pp. 427–431.
15. For more on unit roots, see John Y. Campbell and Pierre Peron, “Pitfalls and Opportuni-
ties: What Macroeconomists Should Know About Unit Roots,” NBER Macroeconomics Annual 
­(Cambridge, MA: MIT Press, 1991), pp. 141–219.


381
  Spurious Correlation and Nonstationarity
The Dickey–Fuller test actually comes in three versions:
1.	 Equation 12.27,
2.	 Equation 12.27 with a constant term added (Equation 12.28), and
3.	 Equation 12.27 with a constant term and a trend term added 
­(Equation 12.29).
The form of the Dickey–Fuller test in Equation 12.27 is correct if Yt follows 
Equation 12.22, but most econometricians add a constant term to the equa-
tion, for reasons similar to those mentioned in Section 7.1, so the basic 
Dickey–Fuller test equation becomes:
	
∆Yt = β0 + β1Yt-1 + vt	
(12.28)
Alternatively, if we believe Yt contains a trend “t” 1t = 1, 2, 3, c , T2, then 
we’d add “t” to the equation as a variable with a coefficient, and the appropri-
ate Dickey–Fuller test equation is:
	
∆Yt = β0 + β1Yt-1 + β2t + vt	
(12.29)
How do we decide whether to use Equation 12.28 or Equation 12.29? If 
you compare the two equations, you can see that the only difference between 
them is a trend term (β2t) that’s in Equation 12.29 but not in Equation 12.28. 
Thus Equation 12.29 is appropriate if Y is growing and Equation 12.28 is 
appropriate if Y is not growing. Perhaps the best way to make this decision is 
to plot Y over time and then judge whether or not it appears to be growing.16 
GDP and consumption are good examples of variables that usually are grow-
ing over time, while most rates (like interest rates and unemployment rates) 
are good examples of variables that are not growing.
No matter which form of the Dickey–Fuller test we use, the decision rule 
is the same. If βn 1 is significantly less than 0 as measured by a t-test, then we 
can reject the null hypothesis of a unit root; this implies that the variable is 
stationary. If βn 1 is not significantly less than 0, then we cannot reject the 
null hypothesis of a unit root; this implies that the variable is nonstationary. 
(Recall from Chapter 5 that if we’re not able to reject the null hypothesis, we 
still have not “proven” that Y is nonstationary.)
16. John Elder and Peter Kennedy, “Testing for Unit Roots: What Should Students Be Taught?” 
Journal of Economic Education, Vol. 32, No. 2, pp. 137–146. Elder and Kennedy also investigate 
what to do in the unlikely case that the growth status of Y is unknown.


382
Chapter 12  Time-Series Models
Be careful, however. The standard t-table does not apply to Dickey–Fuller 
tests. Instead the critical values are somewhat higher than those in Statistical 
Table B-1, and they also depend on the version of the Dickey–Fuller test you 
use. In Table 12.1,17 we list critical values for the two versions of the Dickey–
Fuller test we have discussed the most, Equations 12.28 and 12.29. For exam-
ple, a 5-percent one-sided test of β1 in Equation 12.28 with a sample size of 
25 has a critical t-value of 3.00 compared to 1.717 for a standard t-test (with 
22 degrees of freedom since K = 2).
The Dickey–Fuller specifications in Equations 12.28 and 12.29 and the 
critical values for those specifications are derived under the assumption that 
the error term is serially uncorrelated. If the error term is serially correlated, 
then the test must be modified to take this serial correlation into account. This 
adjustment, called the Augmented Dickey–Fuller test (ADF), adds a series of 
lagged values of ∆Y to the Dickey–Fuller test. While the ADF is the most-used 
version of the Dickey–Fuller test, it is beyond the scope of this textbook, at 
least in part because choosing how many lagged ∆Y values to include can be 
quite complicated.
Cointegration
If the Dickey–Fuller test reveals nonstationarity, what should we do?
The traditional approach is to take the first differences (∆Y = Yt - Yt-1 
and ∆X = Xt - Xt-1) and use them in place of Yt and Xt in the equation. 
17. Most sources list negative critical values for the Dickey–Fuller test, because the unit root test 
is one-sided with a negative expected value. However, the t-test decision rule of this text is based 
on the absolute value of the t-score, so negative critical values would cause every null hypoth-
esis to be rejected. As a result, the critical values in Table 12.1 are positive. For adjusted critical 
t-values for the Dickey–Fuller test, including those in Table 12.1, see J. G. MacKinnon, “Criti-
cal Values of Cointegration Tests,” in Rob Engle and C. W. J. Granger, eds., Long-Run Economic 
Relationships: Readings in Cointegration (New York: Oxford University Press, 1991), Chapter 13. 
Most software packages provide these critical values with the output from a Dickey–Fuller test.
Table 12.1  5-Percent One-Sided Critical Values for the Dickey–Fuller test
Sample Size  
(T)
For Equation 12.28  
(Y not growing)
For Equation 12.29  
(Y growing)
  25
3.00
3.60
  50
2.93
3.50
100
2.89
3.45
∞
2.86
3.41


383
  Spurious Correlation and Nonstationarity
With economic data, taking a first difference usually is enough to convert a 
nonstationary series into a stationary one. Unfortunately, using first differ-
ences to correct for nonstationarity throws away information that economic 
theory can provide in the form of equilibrium relationships between the vari-
ables when they are expressed in their original units (Xt and Yt). As a result, 
first differences should not be used without carefully weighing the costs and 
benefits of that shift, and in particular first differences should not be used 
until the residuals have been tested for cointegration.
Cointegration consists of matching the degree of nonstationarity of the 
variables in an equation in a way that makes the error term (and residuals) 
of the equation stationary and rids the equation of any spurious regression 
results. Even though individual variables might be nonstationary, it’s possible 
for linear combinations of nonstationary variables to be stationary, or cointe-
grated. If a long-run equilbrium relationship exists between a set of variables, 
those variables are said to be cointegrated. If the variables are cointegrated, 
then you can avoid spurious regressions even though the dependent variable 
and at least one independent variable are nonstationary.
To see how this works, let’s return to Equation 12.24:
	
Yt = α0 + β0Xt + ut	
(12.24)
As we saw in the previous section, if Xt and Yt are nonstationary, it’s likely 
that we’ll get spurious regression results. To understand how it’s possible to 
get sensible results from Equation 12.24 if the nonstationary variables are 
cointegrated, let’s focus on the case in which both Xt and Yt contain one unit 
root. The key to cointegration is the behavior of ut.  
If we solve Equation 12.24 for ut, we get:
	
ut = Yt - α0 - β0Xt	
(12.30)
In Equation 12.30, ut is a function of two nonstationary variables, so you’d 
certainly expect ut also to be nonstationary, but that’s not necessarily the 
case. In particular, suppose that Xt and Yt are related? More specifically, if 
economic theory supports Equation 12.24 as an equilibrium, then departures 
from that equilibrium should not be arbitrarily large.
Hence, if Yt and Xt are related, then the error term ut may well be stationary 
even though Xt and Yt are nonstationary. If ut is stationary, then the unit roots 
in Yt and Xt have “cancelled out” and Yt and Xt are said to be cointegrated.18
18. For more on cointegration, see Peter Kennedy, A Guide to Econometrics (Malden, MA: Black-
well, 2008), pp. 309–313 and 327–330, and B. Bhaskara Rau, ed., Cointegration for the Applied 
Economist (New York: St. Martin’s Press, 1994).


384
Chapter 12  Time-Series Models
We thus see that if Xt and Yt are cointegrated, then OLS estimation of the 
coefficients in Equation 12.24 can avoid spurious results. To determine if Xt 
and Yt are cointegrated, we begin with OLS estimation of Equation 12.24 and 
calculate the OLS residuals:
	
et = Yt - αn 0 - βn 0Xt	
(12.31)
We then perform a Dickey–Fuller test on the residuals. Once again, the 
standard critical t-values do not apply to this application, so adjusted critical 
t-values should be used.19 If we are able to reject the null hypothesis of a unit 
root in the residuals, we can conclude that Yt and Xt are cointegrated and our 
OLS estimates are not spurious.
To sum, if the Dickey–Fuller test reveals that our variables have unit roots, 
the first step is to test for cointegration in the residuals. If the nonstationary 
variables are not cointegrated, then the equation should be estimated using 
first differences (∆Y and ∆X). However, if the nonstationary variables are 
cointegrated, then the equation can be estimated in its original units.20
A Standard Sequence of Steps for Dealing with Nonstationary 
Time Series
This material is fairly complex, at least compared to previous chapters, so 
let’s pause for a moment to summarize the various steps suggested in Sec-
tion 12.5. To deal with the possibility that nonstationary time series might be 
19. See J. G. MacKinnon, “Critical Values of Cointegration Tests,” in Rob Engle and C. W. J. 
Granger, eds., Long-Run Economic Relationships: Readings in Cointegration (New York: Oxford Uni-
versity Press, 1991), Chapter 13, and Rob Engle and C. W. J. Granger, “Co-integration and Error 
Correction: Representation, Estimation and Testing,” Econometrica, Vol. 55, No. 2.
20. In this case, it’s common practice to use a version of the original equation called the Error 
Correction Model (ECM). While the equation for the ECM is fairly complex, the model itself 
is a logical extension of the cointegration concept. If two variables are cointegrated, then there 
is an equilibrium relationship connecting them. A regression on these variables therefore is 
an estimate of this equilibrium relationship along with a residual, which is a measure of the 
extent to which these variables are out of equilibrium. When formulating a dynamic relation-
ship between the variables, economic theory suggests that the current change in the dependent 
variable should be affected not only by the current change in the independent variable but also 
by the extent to which these variables were out of equilibrium in the preceding period (the 
residual from the cointegrating process). The resulting equation is the ECM. For more on the 
ECM, see Peter Kennedy, A Guide to Econometrics (Malden, MA: Blackwell, 2008), pp. 299–301 
and 322–323.


385
  Summary
causing regression results to be spurious, most empirical work in time series 
follows a standard sequence of steps:
	 1.	Specify the model. This model might be a time-series equation with 
no lagged variables, a distributed lag model or a dynamic model.
	 2.	Test all variables for unit roots using the appropriate version of the 
Dickey–Fuller test.
	 3.	If the variables don’t have unit roots, estimate the equation in its 
original units (Y and X).
	 4.	If the variables have unit roots, test the residuals of the equation for 
cointegration using the Dickey–Fuller test.
	 5.	If the variables have unit roots but are not cointegrated, then change 
the functional form of the model to first differences (∆Y and ∆X) 
and estimate the equation.
	 6.	If the variables have unit roots and also are cointegrated, then 
­estimate the equation in its original units.
12.6   Summary
1.	
A distributed lag explains the current value of Y as a function of cur-
rent and past values of X, thus “distributing” the impact of X over 
a number of lagged time periods. OLS estimation of distributed lag 
equations without any constraints encounters problems with mul-
ticollinearity, degrees of freedom, and a noncontinuous pattern of 
estimated coefficients over time.
2.	
A dynamic model avoids these problems by assuming that the coef-
ficients of the lagged independent variables decrease in a geometric 
fashion the longer the lag. Given this, the dynamic model is:
	
Yt = α0 + β0Xt + λYt-1 + ut
	
where Yt−1 is a lagged dependent variable and 0 6 λ 6 1.
3.	
In small samples, OLS estimates of a dynamic model are biased and 
have unreliable hypothesis testing properties. Even in large samples, 
OLS will produce biased estimates of the coefficients of a dynamic 
model if the error term is serially correlated.


386
Chapter 12  Time-Series Models
4.	
In a dynamic model, the Durbin–Watson test is biased toward 2, so it 
should not be used. The most-used alternative is the Lagrange Multi-
plier test.
5.	
Granger causality, or precedence, is a circumstance in which one time-
series variable consistently and predictably changes before another 
variable does. If one variable precedes (Granger-causes) another, we 
still can’t be sure that the first variable “causes” the other to change.
6.	
A nonstationary series is one that exhibits significant changes (for ex-
ample, in its mean and variance) over time. If the dependent variable 
and at least one independent variable are nonstationary or trending, 
a regression may encounter spurious correlation that inflates R  2 and 
t-scores.
7.	
Nonstationarity can be detected using the Dickey–Fuller test. If 
the variables have unit roots and therefore are nonstationary, then the 
residuals of the equation should be tested for cointegration using the 
Dickey–Fuller test. If the variables are nonstationary but are not coin-
tegrated, then the equation should be estimated with first differences. 
If the variables are nonstationary and also are cointegrated, then the 
equation can be estimated in its original units.
Exercises
(Answers to the even-numbered exercises are in Appendix A.)
	 1.	 Write the meaning of each of the following terms without referring to 
the book (or your notes), and then compare your definition with the 
version in the text for each:
a.	cointegration (p. 383)
b.	Dickey–Fuller test (p. 380)
c.	 distributed lag model (p. 365)
d.	dynamic model (p. 367)
e.	 Granger causality (p. 375)
f.	 nonstationary (p. 377)
g.	random walk (p. 378)
h.	spurious correlation (p. 376)
i.	 stationary (p. 377)
j.	 unit root (p. 378)


387
Exercises
	 2.	 Consider the following equation aimed at estimating the demand for 
real cash balances in Mexico (standard errors in parentheses):
	
 lnMt = 2.00 - 0.10lnRt +  0.70lnYt +  0.60lnMt-1
	
 10.102
 10.352
 10.102
	
R  2 = .90  DW = 1.80  N = 26
where:  Mt = the money stock in year t (millions of pesos)
	
Rt = the long-term interest rate in year t (percent)
	
Yt = the real GNP in year t (millions of pesos)
a.	What economic relationship between Y and M is implied by the 
equation?
b.	How are Y and R similar in terms of their relationship to M?
c.	 Does this equation seem likely to have serial correlation? Explain.
	 3.	 You’ve been hired to determine the impact of advertising on gross sales 
revenue for “Four Musketeers” candy bars. Four Musketeers has the same 
price and more or less the same ingredients as competing candy bars, so 
it seems likely that only advertising affects sales. You decide to build a 
model of sales as a function of advertising, but you’re not sure whether a 
distributed lag or a dynamic model is appropriate.
	
	 	
Using data on Four Musketeers candy bars from Table 12.2, esti-
mate both of the following equations from 1985–2009 and compare 
the lag structures implied by the estimated coefficients. (Hint: Be care-
ful to use the correct sample.)
a.	distributed lag model (4 lags)
b.	a dynamic model
	 4.	 Test for serial correlation in the estimated dynamic model you got as 
your answer to Exercise 3b.
	 5.	 Some farmers were interested in predicting inches of growth of corn as 
a function of rainfall on a monthly basis, so they collected data from 
the growing season and estimated an equation of the following form:
	
Gt = β0 + β1Rt + β2Gt-1 + et
where:  Gt = inches of growth of corn in month t
	
Rt = inches of rain in month t
	
et  = a normally distributed classical error term
	
	 The farmers expected a negative sign for β2 (they felt that since corn 
can only grow so much, if it grows a lot in one month, it won’t grow 
much in the next month), but they got a positive estimate instead. 
What suggestions would you have for this problem?
h


388
Chapter 12  Time-Series Models
	 6.	 Run 5-percent Dickey–Fuller tests for the following variables from the 
chicken demand equation, using dataset CHICK9 on the text’s website, 
and determine which variables, if any, you think are nonstationary.
a.	 Yt
b.	PCt
c.	 PBt
d.	YDt
Table 12.2  Data for the Four Musketeers Exercise
Year
Sales
Advertising
1981
*
30
1982
*
35
1983
*
36
1984
320
39
1985
360
40
1986
390
45
1987
400
50
1988
410
50
1989
400
50
1990
450
53
1991
470
55
1992
500
60
1993
500
60
1994
490
60
1995
580
65
1996
600
70
1997
700
70
1998
790
60
1999
730
60
2000
720
60
2001
800
70
2002
820
80
2003
830
80
2004
890
80
2005
900
80
2006
850
75
2007
840
75
2008
850
75
2009
850
75
Datafile 5 MOUSE12


389
Exercises
	 7.	 In 2001, Heo and Tan published an article21 in which they used 
the Granger causality model to test the relationship between eco-
nomic growth and democracy. For years, political scientists have 
noted a strong positive relationship between economic growth and 
democracy, but the authors of previous studies (which included 
Granger causality studies) disagreed about the causality involved. Heo 
and Tan studied 32 developing countries and found that economic 
growth “Granger-caused” democracy in 11 countries, while democracy 
“Granger-caused” economic growth in 10 others.
a.	How is it possible to get significant Granger causality results in 
two different directions in the same study? Is this evidence that the 
study was done incorrectly? Is this evidence that Granger causality 
tests cannot be applied to this topic?
b.	Based on the evidence presented, what’s your conclusion about the 
relationship between economic growth and democracy? Explain.
c.	 If this were your research project, what would your next step be? 
(Hint: In particular, is there anything to be gained by learning more 
about the countries in the two different Granger causality groups?22)
21. Uk Heo and Alexander Tan, “Democracy and Economic Growth: a Causal Analysis,” Com-
parative Politics, Vol. 33, No. 4 (July 2001), pp. 463–473.
22. For the record, the 11 countries in which growth Granger-caused democracy were Costa 
Rica, Egypt, Guatemala, India, Israel, South Korea, Mexico, Nicaragua, Thailand, Uruguay, and 
Venezuela, and the 10 countries in which democracy Granger-caused growth were Bolivia, 
Burma, Colombia, Ecuador, El Salvador, Indonesia, Iran, Paraguay, the Philippines, and South 
Africa.
