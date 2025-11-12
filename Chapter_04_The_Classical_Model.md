# Chapter 4: The Classical Model

**Pages:** 112-134

---

4.1  The Classical Assumptions
4.2  The Sampling Distribution of 훃n
4.3  The Gauss–Markov Theorem and the Properties  
of OLS Estimators
4.4  Standard Econometric Notation
4.5 Summary and Exercises
The Classical Model
Chapter 4
The classical model of econometrics has nothing to do with ancient Greece 
or even the classical economic thinking of Adam Smith. Instead, the term 
classical refers to a set of fairly basic assumptions required to hold in order 
for OLS to be considered the “best” estimator available for regression models. 
When one or more of these assumptions do not hold, other estimation tech-
niques (such as Generalized Least Squares, to be explained in Chapter 9) may 
be better than OLS.
As a result, one of the most important jobs in regression analysis is to decide 
whether the classical assumptions hold for a particular equation. If so, the OLS 
estimation technique is the best available. Otherwise, the pros and cons of 
alternative estimation techniques must be weighed. These alternatives usually 
are adjustments to OLS that take account of the particular assumption that 
has been violated. In a sense, most of the rest of this book deals in one way or 
another with the question of what to do when one of the classical assumptions 
is not met. Since econometricians spend so much time analyzing violations 
of them, it is crucial that they know and understand these assumptions.
4.1   The Classical Assumptions
The Classical Assumptions must be met in order for OLS estimators to 
be the best available. Because of their importance in regression analysis, 
the assumptions are presented here in tabular form as well as in words. 
92


93
  The Classical Assumptions
Subsequent chapters will investigate major violations of the assumptions 
and introduce estimation techniques that may provide better estimates in 
such cases.
An error term satisfying Assumptions I through V is called a classical error 
term, and if Assumption VII is added, the error term is called a classical normal 
error term.
I. The regression model is linear, is correctly specified, and has an additive 
error term. The regression model is assumed to be linear:
	
Yi = β0 + β1X1i + β2X2i + g+ βKXKi + ei	
(4.1)
The assumption that the regression model is linear1 does not require the 
underlying theory to be linear. For example, an exponential function:
	
Yi = eβ0Xi
β1eei	
(4.2)
where e is the base of the natural log, can be transformed by taking the natu-
ral log of both sides of the equation:
	
ln1Yi2 = β0 + β1 ln1Xi2 + ei	
(4.3)
1. The Classical Assumption that the regression model is “linear” technically requires the model 
to be “linear in the coefficients.” You’ll learn what it means for a model to be linear in the 
coefficients, particularly in contrast to being linear in the variables, in Section 7.2. We’ll cover 
the application of regression analysis to equations that are nonlinear in the variables in that 
same section, but the application of regression analysis to equations that are nonlinear in the 
coefficients is beyond the scope of this textbook.
The Classical Assumptions
	 I.	 The regression model is linear, is correctly specified, and has an  
additive error term.
	 II.	 The error term has a zero population mean.
	III.	 All explanatory variables are uncorrelated with the error term.
	IV.	 Observations of the error term are uncorrelated with each other  
(no serial correlation).
	 V.	 The error term has a constant variance (no heteroskedasticity).
	VI.	 No explanatory variable is a perfect linear function of any other 
­explanatory variable(s) (no perfect multicollinearity).
	VII.	 The error term is normally distributed (this assumption is optional 
but usually is invoked).


94
Chapter 4  The Classical Model
If the variables are relabeled as Yi* = ln1Yi2 and Xi* = ln1Xi2, then the form 
of the equation becomes linear:
	
Yi* = β0 + β1Xi* + ei	
(4.4)
In Equation 4.4, the properties of the OLS estimator of the βs still hold 
because the equation is linear.
Two additional properties also must hold. First, we assume that the equa-
tion is correctly specified. If an equation has an omitted variable or an 
incorrect functional form, the odds are against that equation working well. 
Second, we assume that a stochastic error term has been added to the equa-
tion. This error term must be an additive one and cannot be multiplied by or 
divided into any of the variables in the equation.
II. The error term has a zero population mean. As was pointed out in 
Section 1.2, econometricians add a stochastic (random) error term to regres-
sion equations to account for variation in the dependent variable that is not 
explained by the model. The specific value of the error term for each obser-
vation is determined purely by chance. Probably the best way to picture this 
concept is to think of each observation of the error term as being drawn from 
a random variable distribution such as the one illustrated in Figure 4.1.
Classical Assumption II says that the mean of this distribution is zero. 
That is, when the entire population of possible values for the stochastic error 
Figure 4.1  An Error Term Distribution with a Mean of Zero
Observations of stochastic error terms are assumed to be drawn from a random variable 
distribution with a mean of zero. If Classical Assumption II is met, the expected value 
(the mean) of the error term is zero.
0
Probability
-
+
g


95
  The Classical Assumptions
term is considered, the average value of that population is zero. For a small 
sample, it is not likely that the mean is exactly zero, but as the size of the 
sample approaches infinity, the mean of the sample approaches zero.
What happens if the mean doesn’t equal zero in a sample? As long as you 
have a constant term in the equation, the estimate of β0 will absorb the non-
zero mean. In essence, the constant term equals the fixed portion of Y that 
cannot be explained by the independent variables, and the error term equals 
the stochastic portion of the unexplained value of Y.
Although it’s true that the error term never can be observed, it’s instructive to 
pretend that we can do so to see how the constant term absorbs the non-zero 
mean of the error term in a sample. Consider a typical regression equation:
	
Yi = β0 + β1Xi + ei	
(4.5)
Suppose that the mean of ei is 3 instead of 0, then2 E1ei - 32 = 0. If we add 
3 to the constant term and subtract it from the error term, we obtain:
	
Yi = 1β0 + 32 + β1Xi + 1ei - 32	
(4.6)
Since Equations 4.5 and 4.6 are equivalent (do you see why?), and since 
E1ei - 32 = 0, then Equation 4.6 can be written in a form that has a zero 
mean for the error term ei*:
	
Yi = β0* + β1Xi + ei*	
(4.7)
where β0* = β0 + 3 and ei* = ei - 3. As can be seen, Equation 4.7 conforms 
to Assumption II. In essence, if Classical Assumption II is violated in an equa-
tion that includes a constant term, then the estimate of β0 absorbs the non-
zero mean of the error term, and the estimates of the other coefficients are 
unaffected.
III. All explanatory variables are uncorrelated with the error term. It is 
assumed that the observed values of the explanatory variables are indepen-
dent of the values of the error term.
If an explanatory variable and the error term were instead correlated with 
each other, the OLS estimates would be likely to attribute to the X some of 
the variation in Y that actually came from the error term. If the error term 
and X were positively correlated, for example, then the estimated coeffi-
cient would probably be higher than it would otherwise have been (biased 
upward), because the OLS program would mistakenly attribute the variation 
2. Here, as in Chapter 1, the “E” refers to the expected value (mean) of the item in parentheses 
after it. Thus E1ei - 32 equals the expected value of the stochastic error term epsilon minus 3. 
In this specific example, since we’ve defined E1ei2 = 3, we know that E1ei - 32 = 0. One way 
to think about expected value is as our best guess of the long-run average value a specific ran-
dom variable will have.


96
Chapter 4  The Classical Model
in Y caused by e to X instead. As a result, it’s important to ensure that the 
explanatory variables are uncorrelated with the error term.
Classical Assumption III is violated most frequently when a researcher 
omits an important independent variable from an equation.3 As you learned 
in Chapter 1, one of the major components of the stochastic error term is 
omitted variables, so if a variable has been omitted, then the error term will 
change when the omitted variable changes. If this omitted variable is corre-
lated with an included independent variable (as often happens in economics), 
then the error term is correlated with that independent variable as well. We 
have violated Assumption III! Because of this violation, OLS will attribute 
the impact of the omitted variable to the included variable, to the extent that 
the two variables are correlated.
IV. Observations of the error term are uncorrelated with each other. The 
observations of the error term are drawn independently from each other. If a 
systematic correlation exists between one observation of the error term and 
another, then OLS estimates will be less precise than estimates that account 
for the correlation. For example, if the fact that the e from one observation is 
positive increases the probability that the e from another observation also is 
positive, then the two observations of the error term are positively correlated. 
Such a correlation would violate Classical Assumption IV.
In economic applications, this assumption is most important in time-series 
models. In such a context, Assumption IV says that an increase in the error 
term in one time period (a random shock, for example) does not show up 
in or affect in any way the error term in another time period. In some cases, 
though, this assumption is unrealistic, since the effects of a random shock 
sometimes last for a number of time periods. For example, a natural disaster 
like the 2015 earthquake in Nepal will have a negative impact on a region 
long after the time period in which it was truly a random event. If, over all 
the observations of the sample, et+1 is correlated with et, then the error term is 
said to be serially correlated (or autocorrelated), and Assumption IV is violated. 
Violations of this assumption are considered in more detail in Chapter 9.
V. The error term has a constant variance. The variance (or dispersion) of 
the distribution from which the observations of the error term are drawn 
is constant.4 That is, the observations of the error term are assumed to be 
drawn continually from identical distributions (for example, the one pictured 
3. Another important economic application that violates this assumption is any model that is 
simultaneous in nature. This will be considered in Chapter 14.
4. This is a simplification. The actual assumption (that error terms have positive finite second 
moments) is equivalent to this simplification in all but a few extremely rare cases.


97
  The Classical Assumptions
in Figure 4.1). The alternative would be for the variance of the distribution 
of the error term to change for each observation or range of observations. In 
Figure 4.2, for example, the variance of the error term is shown to increase 
as the variable Z increases; such a pattern violates Classical Assumption V. 
The actual values of the error term are not directly observable, but the lack 
of a constant variance for the distribution of the error term causes OLS to 
generate inaccurate estimates of the standard error of the coefficients.5
For example, suppose that you’re studying the amount of money that the 
50 states spend on education. New York and California are more heavily 
­populated than New Hampshire and Nevada, so it’s probable that the vari-
ance of the error term for big states is larger than it is for small states. The 
amount of unexplained variation in educational expenditures seems likely to 
5. Because some observations have errors with a large variance, those observations are not as 
reliable and so should be given less weight when minimizing the sum of squares. OLS, how-
ever, gives equal weight to each observation, so it will be less precise than estimators that weigh 
the observations more appropriately.
Figure 4.2  An Error Term Whose Variance Increases as Z Increases
One example of Classical Assumption V not being met is when the variance of the error 
term increases as Z increases. In such a situation (called heteroskedasticity), the observa-
tions are on average farther from the true regression line for large values of Z than they 
are for small values of Z.
Y
0
Z
Small gs
Associated with
Small Zs
Large gs Associated
with Large Zs
E(Y|X) = d0 + d1Z


98
Chapter 4  The Classical Model
be larger in big states like New York than in small states like New Hampshire. 
The violation of Assumption V is referred to as heteroskedasticity and will be 
discussed in more detail in Chapter 10.
VI. No explanatory variable is a perfect linear function of any other explan-
atory variable(s). Perfect collinearity between two independent variables 
implies that they are really the same variable, or that one is a multiple of the 
other, and/or that a constant has been added to one of the variables. That is, 
the relative movements of one explanatory variable will be matched exactly 
by the relative movements of the other even though the absolute size of the 
movements might differ. Because every movement of one of the variables is 
matched exactly by a relative movement in the other, the OLS estimation 
procedure will be incapable of distinguishing one variable from the other.
Many instances of perfect collinearity (or multicollinearity if more than 
two independent variables are involved) are the result of the researcher not 
accounting for identities (definitional equivalences) among the independent 
variables. This problem can be corrected easily by dropping one of the per-
fectly collinear variables from the equation.
What’s an example of perfect multicollinearity? Suppose that you decide 
to build a model of the profits of tire stores in your city and you include 
annual sales of tires (in dollars) at each store and the annual sales tax paid by 
each store as independent variables. Since the tire stores are all in the same 
city, they all pay the same percentage sales tax, so the sales tax paid will be 
a constant percentage of their total sales (in dollars). If the sales tax rate is 
7%, then the total taxes paid will be 7% of sales for each and every tire store. 
Thus sales tax will be a perfect linear function of sales, and you’ll have perfect 
multicollinearity!
Perfect multicollinearity also can occur when two independent variables 
always sum to a third or when one of the explanatory variables doesn’t 
change within the sample. With perfect multicollinearity, OLS (or any other 
estimation technique) will be unable to estimate the coefficients of the col-
linear variables (unless there is a rounding error). While it’s quite unusual 
for an experienced researcher to encounter perfect multicollinearity, even 
imperfect multicollinearity can cause problems for estimation, as you will see 
in Chapter 8.
VII. The error term is normally distributed. Although we have already 
assumed that observations of the error term are drawn independently 
(Assumption IV) from a distribution that has a zero mean (Assumption II) 
and that has a constant variance (Assumption V), we have said little about the 
shape of that distribution. Assumption VII states that the observations of the 
error term are drawn from a distribution that is normal (that is, bell-shaped, 
and generally following the symmetrical pattern portrayed in Figure 4.3).


99
  The Classical Assumptions
This assumption of normality is not required for OLS estimation. Its major 
application is in hypothesis testing and confidence intervals, which use the esti-
mated regression coefficient to investigate hypotheses about economic behav-
ior. Hypothesis testing is the subject of Chapter 5, and without the normality 
assumption, most of the small sample tests of that chapter would be invalid.
Even though Assumption VII is optional, it’s usually advisable to add the 
assumption of normality to the other six assumptions for two reasons:
1.	 The error term ei can be thought of as the sum of a number of minor 
influences or errors. As the number of these minor influences gets 
larger, the distribution of the error term tends to approach the normal 
distribution.
2.	 The t-statistic and the F-statistic, which will be developed in Chapter 5, 
are not truly applicable unless the error term is normally distributed.
A quick look at Figure 4.3 shows how normal distributions differ when 
the means and variances are different. In normal distribution A (a Standard 
Normal Distribution), the mean is 0 and the variance is 1; in normal distri-
bution B, the mean is 2, and the variance is 0.5. When the mean is different, 
the entire distribution shifts. When the variance is different, the distribution 
becomes fatter or skinnier.
Figure 4.3  Normal Distributions
Although all normal distributions are symmetrical and bell-shaped, they do not neces-
sarily have the same mean and variance. Distribution A has a mean of 0 and a variance 
of 1, whereas distribution B has a mean of 2 and a variance of 0.5. As can be seen, the 
whole distribution shifts when the mean changes, and the distribution gets fatter as the 
variance increases.
0
2.0
4.0
-2.0
Probability
Distribution A      
o = 0
u2 = 1
Distribution B      
o = 2   
u2 = 0.5


100
Chapter 4  The Classical Model
4.2   The Sampling Distribution of 훃N
“It cannot be stressed too strongly how important it is for students  
to understand the concept of a sampling distribution.”6
Just as the error term follows a probability distribution, so too do the 
estimates of β. In fact, each different sample of data typically produces a 
different estimate of β. The probability distribution of these βN  values across 
different samples is called the sampling distribution of 훃N .
Recall that an estimator is a formula, such as the OLS formula in Equa-
tion 2.4 that tells you how to compute βN , while an estimate is the value of βN  
computed by the formula for a given sample. Since researchers usually have 
only one sample, beginning econometricians often assume that regression 
analysis can produce only one estimate of β for a given population. In real-
ity, however, each different sample from the same population will produce a 
different estimate of β. The collection of all the possible samples has a distri-
bution, with a mean and a variance, and we need to discuss the properties of 
this sampling distribution of βN , even though in most real applications we will 
encounter only a single draw from it. Be sure to remember that a sampling 
distribution refers to the distribution of different values of βN  across differ-
ent samples, not within one. These βN s usually are assumed to be normally 
distributed because the normality of the error term implies that the OLS esti-
mates of β are normally distributed as well.
Let’s look at an example of a sampling distribution of βN  by going back 
to the height and weight example of Chapter 1 (with weight measured in 
pounds and height measured in inches above five feet).
	
+
	
WEIGHTi = β0 + β1HEIGHTi + ei	
(4.8)
Suppose you take a sample of six students and apply OLS to Equation 4.8 to 
get an estimate of β1. So far, so good.
But what will happen if you select a second sample of six students and do 
the same thing? Will you get the exact same βN 1? Nope! Your second βN 1 will 
depend on the second sample, which almost surely will be different from 
your first sample. If your random sample includes a couple of football line-
men, you’re likely to get a really large coefficient. If you randomly choose 
some cross country runners, you’ll get a low estimate. Even if there’s nothing 
6. Peter Kennedy, A Guide to Econometrics (Malden, MA: Blackwell, © 2008), p. 403.


101
  The Sampling Distribution of 훃N
unusual about your second sample, you’ll almost certainly get a different βN 1. 
Why? Different data yield different estimates, so if you collect 100 samples, 
you’re likely to get 100 different βN 1s.
All these βN 1 estimates come from a distribution with its own mean and 
variance, called a sampling distribution. To help you understand this, we took 
100 different samples of six students and estimated Equation 4.8 100 times. 
Take a look at Figure 4.4. With the help of a histogram, we’ve graphed all 100 
βN 1s so that we can get an idea of what the sampling distribution looks like.
While the histogram in Figure 4.4 isn’t perfectly normally distributed (rep-
resented by the thin line), it’s close. Notice how the estimates are clustered 
in the middle (near the mean of 7.75), with fewer and fewer estimates in 
the tails. With many more estimates of β1, we’d expect the histogram to look 
even more like a normal curve.
For an estimation technique to be “good,” the mean of the sampling 
distribution of the βN s it produces should equal the true population β. This 
property has a special name in econometrics: unbiasedness. There’s much 
more to come on this idea.
Figure 4.4  A Height and Weight Sampling Distribution of βN
We estimated Equation 4.8 (the height weight equation) with 100 samples of six students  
each and plotted the 100 βNs in Figure 4.4. The result is a sampling distribution of βN  
with a mean of 7.75 and a pattern that is reasonably close to being normally distributed 
(the thin line).
30
20
10
Beta Estimates
Frequency
0
0
10
20
30
40
-10
-5.41
(min)
(mean)
(max)
7.75
23.03


102
Chapter 4  The Classical Model
Although we don’t know the true β in this case, it’s likely that if we took 
enough samples—thousands perhaps—the mean of the βN 1s would approach 
the true β. For example, when we took 1,000 samples of six, the mean of the 
βN 1s was 6.88. The chances are that 6.88 is closer to the true β than is 7.75, the 
mean of the 100 estimates shown in Figure 4.4.
The moral of the story is that while a single sample provides a single estimate 
of β1, that estimate comes from a sampling distribution with a mean and a 
variance. Other estimates from that sampling distribution will most likely be 
different. When we discuss the properties of estimators in the next section, 
it will be important to remember that we are discussing the properties of a 
sampling distribution, not the properties of one sample.
Properties of the Mean
A desirable property of a distribution of estimates is that its mean equals the 
true mean of the variable being estimated. An estimator that yields such esti-
mates is called an unbiased estimator.
Only one value of βN  is obtained in practice, but the property of unbiasedness 
is useful because a single estimate drawn from an unbiased distribution is 
more likely to be near the true value (assuming identical variances) than one 
taken from a distribution not centered around the true value. If an estimator 
produces βN s that are not centered around the true β, the estimator is referred 
to as a biased estimator.
We cannot ensure that every estimate from an unbiased estimator is better 
than every estimate from a biased one, because a particular unbiased esti-
mate7 could, by chance, be farther from the true value than a biased estimate 
might be. This could happen by chance or because the biased estimator had 
An estimator βN  is an unbiased estimator if its sampling distribution has 
as its expected value the true value of β.
	
E1βN 2 = β	
(4.9)
7. Technically, since an estimate has just one value, an estimate cannot be unbiased (or biased). 
On the other hand, the phrase “estimate produced by an unbiased estimator” is cumbersome, 
especially if repeated 10 times on a page. As a result, many econometricians use “unbiased 
estimate” as shorthand for “a single estimate produced by an unbiased estimator.”


103
  The Sampling Distribution of 훃N
a smaller variance. For example, a broken clock is a biased estimator of the 
time of day, but it has a zero variance and happens to be exactly right twice 
a day. Without any other information about the distribution of the esti-
mates, however, we would always rather have an unbiased estimate than a 
biased one.
Properties of the Variance
Just as we would like the distribution of the βN s to be centered around the 
true population β, we would also like that distribution to be as narrow (or 
precise) as possible. A distribution centered around the truth but with an 
extremely large variance might be of very little use because any given esti-
mate would quite likely be far from the true β value. For a βN  distribution 
with a small variance, the estimates are likely to be close to the mean of 
the sampling distribution. To see this more clearly, compare distributions 
A and B (both of which are unbiased) in Figure 4.5. Distribution A, which 
has a larger variance than distribution B, is less precise than distribution B. 
Figure 4.5  Distributions of βN
Different distributions of βN  can have different means and variances. Distributions  
A and B, for example, are both unbiased, but distribution A has a larger variance than 
does distribution B. Distribution C has a smaller variance than distribution A, but  
it is biased.
True
d
Distribution B
(unbiased, small variance)
Distribution A
(unbiased, large variance)
Distribution C
(biased, medium variance)


104
Chapter 4  The Classical Model
For comparison purposes, a biased distribution (distribution C) is also pictured; 
note that bias implies that the expected value of the distribution is to the 
right or left of the true β.
The variance of the distribution of the βN s can be decreased by increasing 
the size of the sample. This also increases the degrees of freedom, since the 
number of degrees of freedom equals the sample size minus the number 
of coefficients or parameters estimated. As the number of observations 
increases, other things held constant, the variance of the sampling distribu-
tion tends to decrease. Although it is not true that a sample of 60 will always 
produce estimates closer to the true β than a sample of 6, it is quite likely to 
do so; such larger samples should be sought. Figure 4.6 presents illustrative 
sampling distributions of βN s for 6, 60, and 600 observations for OLS estima-
tors of β when the true β equals 1. The larger samples do indeed produce 
sampling distributions that are more closely centered around β.
1
2
3
d
4
N = 60
N = 600
N = 6
0
-1
-2
N
Figure 4.6  Sampling Distribution of βN  for Various Observations (N)
As the size of the sample increases, the variance of the distribution of βN s calculated from 
that sample tends to decrease. In the extreme case (not shown), a sample equal to the 
population would yield only an estimate equal to the mean of that distribution, which 
(for unbiased estimators) would equal the true β, and the variance of the estimates 
would be zero.


105
  The Sampling Distribution of 훃N
The powerful lesson illustrated by Figure 4.6 is that if you want to maxi-
mize your chances of getting an estimate close to the true value, apply OLS to 
a large sample. There’s no guarantee that you’ll get a more accurate estimate 
from a large sample, but your chances are better. Larger samples, all else 
equal, tend to result in more precise estimates. And if the estimator is unbi-
ased, more precise estimates are more accurate estimates.
Think of it this way. Having a couple of cross country runners might lead 
to a pretty wacky estimate from a sample of 6, but their influence on βN 1 is 
going to be much smaller in a sample of 60. You could imagine getting 2 
cross country runners in a random sample of 6 students, but it would be vir-
tually impossible to get 20 cross country runners in a sample of 60. So try to 
get larger samples.
In econometrics, we must rely on general tendencies. The element of 
chance, a random occurrence, is always present in estimating regression coef-
ficients, and some estimates may be far from the true value no matter how 
good the estimating technique. However, if the distribution is centered on 
the true value and has as small a variance as possible, the element of chance 
is less likely to induce a poor estimate. If the sampling distribution is cen-
tered around a value other than the true β (that is, if βN  is biased) then a lower 
variance implies that most of the sampling distribution of βN  is concentrated 
on the wrong value. However, if this value is not very different from the true 
value, which is usually not known in practice, then the greater precision will 
still be valuable.
One method of deciding whether this decreased variance in the distribu-
tion of the βN s is valuable enough to offset the bias is to compare different 
estimation techniques by using a measure called the Mean Square Error (MSE). 
The Mean Square Error is equal to the variance plus the square of the bias. The 
lower the MSE, the better.
A final item of importance is that as the variance of the error term 
increases, so too does the variance of the distribution of βN . The reason for the 
increased variance of βN  is that with the larger variance of ei, the more extreme 
values of ei are observed with more frequency, and the error term becomes 
more important in determining the values of Yi.
The Standard Error of 훃N
Since the standard error of the estimated coefficient, SE1훃N 2, is the square 
root of the estimated variance of the βN s, it is similarly affected by the size of 
the sample and the other factors we’ve mentioned. For example, an increase 
in sample size will cause SE1βN 2 to fall; the larger the sample, the more pre-
cise our coefficient estimates will be.


106
Chapter 4  The Classical Model
Given Classical Assumptions I through VI (Assumption VII, normality, 
is not needed for this theorem), the Ordinary Least Squares estimator of 
βk is the minimum variance estimator from among the set of all linear 
unbiased estimators of βk, for k = 0, 1, 2, c, K.
4.3   The Gauss–Markov Theorem and the Properties  
of OLS Estimators
The Gauss–Markov Theorem proves two important properties of OLS estima-
tors. This theorem is proven in all advanced econometrics textbooks, but for 
a regression user, it’s more important to know what the theorem implies than 
to be able to prove it. The Gauss–Markov Theorem states that:
The Gauss–Markov Theorem is perhaps most easily remembered by stat-
ing that “OLS is BLUE” where BLUE stands for “Best (meaning minimum 
variance) Linear Unbiased Estimator.” Students who might forget that “best” 
stands for minimum variance might be better served by remembering “OLS 
is MvLUE,” but such a phrase is hardly catchy or easy to remember.
If an equation’s coefficient estimation is unbiased (that is, if each of the 
estimated coefficients is produced by an unbiased estimator of the true popu-
lation coefficient), then:
	E1βN k2 = βk  1k = 0, 1, 2, c, K2
Best means that each βN k has the smallest variance possible (in this case, out 
of all the linear unbiased estimators of βk). An unbiased estimator with the 
smallest variance is called efficient, and that estimator is said to have the prop-
erty of efficiency. Since the variance typically falls as the sample size increases, 
larger samples almost always produce more accurate coefficient estimates than 
do smaller ones.
The Gauss–Markov Theorem requires that just the first six of the seven 
classical assumptions be met. What happens if we add in the seventh assump-
tion, that the error term is normally distributed? In this case, the result of 
the Gauss–Markov Theorem is strengthened because the OLS estimator can 
be shown to be the best (minimum variance) unbiased estimator out of all 
the possible estimators, not just out of the linear estimators. In other words, 
if all seven assumptions are met, OLS is “BUE.”


107
  Standard Econometric Notation
Given all seven classical assumptions, the OLS coefficient estimators can 
be shown to have the following properties:
1.	 They are unbiased. That is, E1βN 2 is β. This means that the OLS estimates 
of the coefficients are centered around the true population values of 
the parameters being estimated.
2.	 They are minimum variance. The distribution of the coefficient estimates 
around the true parameter values is as tightly or narrowly distributed 
as is possible for an unbiased distribution. No other unbiased estima-
tor has a lower variance for each estimated coefficient than OLS.
3.	 They are consistent. As the sample size approaches infinity, the estimates 
converge to the true population parameters. Put differently, as the 
sample size gets larger, the variance gets smaller, and each estimate  
approaches the true value of the coefficient being estimated.8
4.	 They are normally distributed. The βN s are N1β, VAR3βN 42. Thus various 
statistical tests based on the normal distribution may indeed be  
applied to these estimates, as will be done in Chapter 5.
4.4   Standard Econometric Notation
This section presents the standard notation used throughout the economet-
rics literature. Table 4.1 presents various alternative notational devices used 
to represent the different population (true) parameters and their correspond-
ing estimates (based on samples).
The measure of the central tendency of the sampling distribution of βN , 
which can be thought of as the mean of the βN s, is denoted as E1βN 2, read as 
“the expected value of beta-hat.” The variance of βN  is the typical measure of 
dispersion of the sampling distribution of βN . The variance (or, alternatively, 
the square root of the variance, called the standard deviation) has several alter-
native notational representations, including VAR1βN 2 and σ21βN 2, read as the 
“variance of beta-hat.”
The variance of the estimates is a population parameter that is never actu-
ally observed in practice; instead, it is estimated with σN 21βN k2, also written as 
s21βN k2. Note, by the way, that the variance of the true β, σ21β2, is zero, since 
there is only one true βk with no distribution around it. Thus, the estimated 
8. Technically, OLS estimates are consistent only if the independent variables continue to 
fluctuate as the sample size increases. See Halbert White, Asymptotic Theory for Econometricians 
(Orlando: Academic Press, 1984), p. 20.


108
Chapter 4  The Classical Model
variance of the estimated coefficient is defined and observed, the true vari-
ance of the estimated coefficient is unobservable, and the true variance of the 
true coefficient is zero. The square root of the estimated variance of the coef-
ficient estimate is the standard error of βN , SE1βN k2, which we will use exten-
sively in hypothesis testing.
4.5   Summary
	 1.	 The seven Classical Assumptions state that the regression model is 
linear with an additive error term that has a mean of zero, is uncorre-
lated with the explanatory variables and other observations of the error 
term, has a constant variance, and is normally distributed (optional). 
In addition, explanatory variables must not be perfect linear functions 
of each other.
Table 4.1  Notation Conventions
Population Parameter  
(True Values, but Unobserved)
Estimate  
(Observed from Sample)
Name
Symbol(s)
Name
Symbol(s)
Regression  
  coefficient
βk
Estimated regression  
  coefficient
βn k
Expected value of 
  the estimated  
coefficient
e1βn k2
Variance of the  
  error term
σ2 or VaR1ei2
Estimated variance  
  of the error term
s2 or σn 2
Standard deviation  
  of the error term
σ
An estimate of the  
  standard deviation 
of the error term
s or SE
Variance of the  
  estimated  
  coefficient
σ21βn k2 or VaR1βn k2
Estimated variance  
  of the estimated 
coefficient
s21βn k2 or VaR1βn k2
Standard deviation 
  of the estimated 
coefficient
σβk or σ1βn k2
Standard error of  
  the estimated  
coefficient
σn 1βn k2 or se1βn k2
Error or  
  disturbance  
term
ei
Residual (estimate  
  of error in a loose 
sense)
ei
h
 n


109
Exercises
	 2.	 The two most important properties of an estimator are unbiasedness 
and minimum variance. An estimator is unbiased when the expected 
value of the estimated coefficient is equal to the true value. Minimum 
variance holds when the estimating distribution has the smallest vari-
ance of all the estimators in a given class of estimators (for example, 
unbiased estimators).
	 3.	 Given the Classical Assumptions, OLS can be shown to be the mini-
mum variance, linear, unbiased estimator (or BLUE, for best linear 
unbiased estimator) of the regression coefficients. This is the Gauss–
Markov Theorem. When one or more of the classical properties do 
not hold (excluding normality), OLS is no longer BLUE, although it 
still may provide better estimates in some cases than the alternative 
estimation techniques discussed in subsequent chapters.
	 4.	 Because the sampling distribution of the OLS estimator of βN k is BLUE, 
it has desirable properties. Moreover, the variance, or the measure of 
dispersion of the sampling distribution of βN k
 , decreases as the num-
ber of observations increases.
	 5.	 There is a standard notation used in the econometric literature. 
Table 4.1 presents this fairly complex set of notational conventions 
for use in regression analysis. This table should be reviewed periodi-
cally as a refresher.
Exercises
(The answers to the even-numbered exercises are in Appendix A.)
	 1.	 Write the meaning of each of the following terms without referring 
to the book (or to your notes), and compare your definition with the 
version in the text for each:
a.	biased estimator (p. 102)
b.	BLUE (p. 106)
c.	 classical error term (p. 93)
d.	efficiency (p. 106)
e.	 Gauss–Markov Theorem (p. 106)
f.	 sampling distribution of βn (p. 100)
g.	 SE1βN 2 (p. 105)
h.	standard normal distribution (p. 99)
i.	 the Classical Assumptions (p. 92)
j.	 unbiased estimator (p. 102)


110
Chapter 4  The Classical Model
	 2.	 Consider the following estimated regression equation (standard errors 
in parentheses):
Ynt = -120 + 0.10Ft + 5.33Rt  R  2 = .50
10.052   11.002
where:	
 Yt = the corn yield (bushels/acre) in year t
	
	 	
 Ft = fertilizer intensity (pounds/acre) in year t
	
	 	
Rt = rainfall (inches) in year t
a.	Carefully state the meaning of the coefficients 0.10 and 5.33 in this 
equation in terms of the impact of F and R on Y.
b.	Does the constant term of -120 really mean that negative amounts 
of corn are possible? If not, what is the meaning of that estimate?
c.	 Suppose you were told that the true value of βF is known to be 0.20. 
Does this show that the estimate is biased? Why or why not?
d.	Suppose you were told that the equation does not meet all the clas-
sical assumptions and therefore is not BLUE. Does this mean that 
the true βR is definitely not equal to 5.33? Why or why not?
	 3.	 Which of the following pairs of independent variables would violate 
Assumption VI? (That is, which pairs of variables are perfect linear 
functions of each other?)
a.	right shoe size and left shoe size (of students in your class)
b.	consumption and disposable income (in the United States over the 
last 30 years)
c.	 Xi and 2Xi
d.	Xi and 1Xi22
	 4.	 Edward Saunders published an article that tested the possibility that 
the stock market is affected by the weather on Wall Street. Using daily 
data from 28 years, he estimated an equation with the following vari-
ables (standard errors in parentheses):9
DJt = βN 0 + 0.10Rt-1 + 0.0010Jt - 0.017Mt + 0.0005Ct
10.012       10.00062   10.0042     10.00022
N = 6,911 (daily) R  2 = .02
8
9. Edward M. Saunders, Jr., “Stock Prices and Wall Street Weather,” American Economic Review, 
Vol. 76, No. 1, pp. 1337–1346. (Published by the American Economic Association, © 1993.) 
Saunders also estimated equations for the New York and American Stock Exchange indices, 
both of which had much higher R2s than did this equation. Rt-1 was included in the equation 
“to account for nonsynchronous trading effects” (p. 1341).


111
Exercises
where:	
DJt = the percentage change in the Dow Jones industrial 
average on day t
	
	
Rt  = the daily index capital gain or loss for day t
	
	
Jt  = a dummy variable equal to 1 if the ith day was in 
January, 0 otherwise
	
	
Mt  = a dummy variable equal to 1 if the ith day was a 
Monday, 0 otherwise
	
	
Ct  = a variable equal to 1 if the cloud cover was 20 per-
cent or less, equal to -1 if the cloud cover was 100 
percent, 0 otherwise
a.	Saunders did not include an estimate of the constant term in his 
published regression results. Which of the Classical Assumptions 
supports the conclusion that you shouldn’t spend much time 
analyzing estimates of the constant term? Explain.
b.	Which of the Classical Assumptions would be violated if you 
decided to add a dummy variable to the equation that was equal 
to 1 if the ith day was a Tuesday, Wednesday, Thursday, or Friday, 
and equal to 0 otherwise? (Hint: The stock market is not open on 
weekends.)
c.	 Carefully state the meaning of the coefficients of R and M, being 
sure to take into account the fact that R is lagged (one time period 
behind) in this equation for valid theoretical reasons.
d.	The variable C is a measure of the percentage of cloud cover from 
sunrise to sunset on the ith day and reflects the fact that approxi-
mately 85 percent of all New York’s rain falls on days with 100 
percent cloud cover. Is C a dummy variable? What assumptions 
(or conclusions) did the author have to make to use this variable? 
What constraints does it place on the equation?
e.	 Saunders concludes that these findings cast doubt on the hypoth-
esis that security markets are entirely rational. Based just on the 
small portion of the author’s work that we include in this question, 
would you agree or disagree? Why?
	 5.	 In Hollywood, most nightclubs hire “promoters,” or people who walk 
around near the nightclub and try to convince passersby to enter the 
club. One of the nightclub owners asked a marketing consultant to 
estimate the effectiveness of such promoters in terms of their ability 
to attract patrons to the club. The consultant did some research and 
found that the main entertainment at the nightclubs was attractive 
dancers and that the most popular nightclubs were on Hollywood 


112
Chapter 4  The Classical Model
Boulevard or attached to hotels, so he hypothesized the following 
model of nightclub attendance:
+	
+	
+	
+
PEOPLEi = β0 + β1HOLLYi + β2PROMOi + β3HOTELi + β4GOGOi + ei
where:	
PEOPLEi  = attendance at the ith nightclub at midnight 
on Saturday 11/24/07
	
HOLLYi
 = equal to 1 if the ith nightclub is on Hollywood 
Boulevard, 0 otherwise
	
PROMOi = number of promoters working at the ith 
nightclub that night
	
HOTELi  = equal to 1 if the ith nightclub is part of a 
hotel, 0 otherwise
	
GOGOi
 = number of dancers working at the ith night-
club that night
	
	 He then collected data from 25 similarly sized nightclubs on or near 
Hollywood Boulevard and came up with the following estimates 
(standard errors in parentheses):
PEOPLEi = 162.8 + 47.4HOLLYi + 22.3PROMOi + 214.5HOTELi + 26.9GOGOi
121.72        111.82            146.02         17.22
N = 25 R  2 = .57
	
	 Let’s work through the classical assumptions to see which assump-
tions might or might not be met by this model. As we analyze each 
assumption, make sure that you can state the assumption from 
memory and that you understand how the following questions help 
us understand whether the assumption has been met.
a.	Assumption I: Is the equation linear with an additive error term? Is 
there a chance that there’s an omitted variable or an incorrect func-
tional form?
b.	Assumption II: Is there a constant term in the equation?
c.	 Assumption III: Is there a chance that there’s an omitted variable or 
that this equation is part of a simultaneous system?
d.	Assumption IV: Is the model estimated with time-series data with 
the chance that a random event in one time period could affect the 
regression in subsequent time periods?
e.	 Assumption V: Is the model estimated with cross-sectional data 
with dramatic variations in the size of the dependent variable?
f.	 Assumption VI: Is any independent variable a perfect linear func-
tion of any other independent variable?
®


113
Exercises
g.	Assume that dancers earn about as much per hour as promoters. If 
the equation is accurate, should the nightclub owner hire one more 
promoter or one more dancer if they want to increase attendance? 
Explain your answer.
	 6.	 In 2001, Donald Kenkel and Joseph Terza published an article in 
which they investigated the impact on an individual’s alcohol con-
sumption of a physician’s advice to reduce drinking.10 In that article, 
Kenkel and Terza used econometric techniques well beyond the scope 
of this text to conclude that such physician advice can play a signifi-
cant role in reducing alcohol consumption.
	
	   We took a fifth (no pun intended) of the authors’ dataset11 and esti-
mated the following equation (standard errors in parentheses):
DRINKSi = 13.00 + 11.36ADVICEi - 0.20EDUCi + 2.85DIVSEPi + 14.20UNEMPi
12.122         10.312        12.552          15.162
t = 5.37          -0.65            1.11             2.75
N = 500 R  2 = .07
where:	
DRINKSi = drinks consumed by the ith individual in the last 
two weeks
	
	 	
ADVICEi = 1 if a physician had advised the ith individual to 
cut back on drinking alcohol, 0 otherwise
	
	 	
EDUCi
 = years of schooling of the ith individual
	
	 	
DIVSEPi  = 1 if the ith individual was divorced or separated, 0 
otherwise
	
	 	
UNEMPi  = 1 if the ith individual was unemployed, 0 
otherwise
a.	Carefully state the meaning of the estimated coefficients of DIVSEP 
and UNEMP. Do the signs of the coefficients make sense to you? 
Do the relative sizes of the coefficients make sense to you? Explain.
®
10. Donald S. Kenkel and Joseph V. Terza, “The Effect of Physician Advice on Alcohol Con-
sumption: Count Regression with an Endogenous Treatment Effect,” Journal of Applied Econo-
metrics, 2001, pp. 165–184.
11. The dataset, which is available on the JAE website, consists of more than 20 variables for 
2467 males who participated in the 1990 National Health Interview Survey and who were 
current drinkers with high blood pressure. Because roughly 30 percent of the sample had zero 
drinks, many econometricians wouldn’t use OLS to estimate this equation. Instead, they’d use 
techniques that, while similar to those covered in Chapter 13, are beyond the scope of this text.


114
Chapter 4  The Classical Model
b.	Carefully state the meaning of the estimated coefficient of ADVICE. 
Does the sign of the coefficient make sense to you? If so, explain. 
If not, this unexpected sign might be related to a violation of one 
of the Classical Assumptions. What Classical Assumption (other 
than Assumption I) is this equation almost surely violating? (Hint: 
Think about what might cause a physician to advise a patient to cut 
back on alcohol drinking and then review the Classical Assump-
tions one more time.)
c.	 We broke up our sample of 500 observations into five different 
samples of 100 observations each and calculated βns for four of the 
five samples. The results (for βN ADVICE) were:
1st sample:	
βN ADVICE = 10.43
2nd sample:	 βN ADVICE = 13.52
3rd sample:	
βN ADVICE = 14.39
4th sample:	
βN ADVICE = 8.01
The βN s are different! Explain in your own words how it’s possible 
to get different βN s when you’re estimating identical specifications 
on data that are drawn from the same source. What term would 
you use to describe this group of βN s?
d.	The data for the fifth sample of 100 observations are in data-
set DRINKS4 on the text’s website. Use these data to estimate 
DRINKS = f(ADVICE, EDUC, DIVSEP, and UNEMP) with Stata, 
EViews, or another regression program. What value do you get for 
βN ADVICE? How do your estimated coefficients compare to those of 
the entire sample of 500?
