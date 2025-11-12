# Chapter 7: Specification: Choosing a Functional Form

**Pages:** 209-240

---

189
Chapter 7
Specification: Choosing  
a Functional Form
7.1  The Use and Interpretation of the Constant Term
7.2  Alternative Functional Forms
7.3  Lagged Independent Variables
7.4  Slope Dummy Variables
7.5  Problems with Incorrect Functional Forms
7.6  Summary and Exercises
7.7  Appendix: Econometric Lab #4
Even after you’ve chosen your independent variables, the job of specifying 
the equation is not over. The next step is to choose the functional form of the 
relationship between each independent variable and the dependent variable. 
Should the equation go through the origin? Do you expect a curve instead 
of a straight line? Does the effect of a variable peak at some point and then 
start to decline? An affirmative answer to any of these questions suggests that 
an equation other than the standard linear model of the previous chapters 
might be appropriate. Such alternative specifications are important for two 
reasons: a correct explanatory variable may well appear to be insignificant or 
to have an unexpected sign if an inappropriate functional form is used, and 
the consequences of an incorrect functional form for interpretation and fore-
casting can be severe.
Theoretical considerations usually dictate the form of a regression model. 
The basic technique involved in deciding on a functional form is to choose 
the shape that best exemplifies the expected underlying economic or business 
principles and then to use the mathematical form that produces that shape. 
To help with that choice, this chapter contains plots of the most commonly 
used functional forms along with the mathematical equations that corre-
spond to each.


190
Chapter 7  Specification: Choosing a Functional Form 
The chapter begins with a brief discussion of the constant term. In particu-
lar, we suggest that the constant term should be retained in equations and 
that estimates of the constant term should not be relied on for inference or 
analysis. The chapter concludes with a discussion of slope dummy variables.
7.1   The Use and Interpretation of the Constant Term
In the linear regression model, β0 is the intercept or constant term. It is the 
expected value of Y when all the explanatory variables (and the error term) 
equal zero. An estimate of β0 has at least three components:
1.	 the true β0,
2.	 the constant impact of any specification errors (an omitted variable, 
for example), and
3.	 the mean of e for the correctly specified equation (if not equal to zero).
Unfortunately, these components can’t be distinguished from one another 
because we can observe only βN 0, the sum of the three components. The result 
is that we have to analyze βN 0 differently from the way we analyze the other 
coefficients in the equation.1
At times, β0 is of theoretical importance. Consider, for example, the 
following cost equation:
	
Ci = β0 + β1Qi + ei
where Ci is the total cost of producing output Qi. The term β1Qi represents 
the total variable cost associated with output level Qi, and β0 represents the 
total fixed cost, defined as the cost when output Qi = 0. Thus, a regression 
equation might seem useful to a researcher who wanted to determine the 
relative magnitudes of fixed and variable costs. This would be an example of 
relying on the constant term for inference.
On the other hand, the product involved might be one for which it is 
known that there are few—if any—fixed costs. In such a case, a researcher 
might want to eliminate the constant term; to do so would conform to the 
notion of zero fixed costs and would conserve a degree of freedom (which 
would presumably make the estimate of β1 more precise). This would be an 
example of suppressing the constant term.
1. If the second and third components of β0 are small compared to the first component, then 
this difference diminishes. See R. C. Allen and J. H. Stone, “Textbook Neglect of the Constant 
Coefficient,” The Journal of Economic Education, Fall 2005, pp. 379–384.


191
  The Use and Interpretation of the Constant Term
Neither suppressing the constant term nor relying on it for inference is 
advisable, however, and the reasons for these conclusions are explained in 
the following sections.
Do Not Suppress the Constant Term
In most cases, suppressing the constant term leads to a violation of the Classi-
cal Assumptions, because it’s very rare that economic theory implies that the 
true intercept, β0, equals zero. If you omit the constant term, then the impact 
of the constant is forced into the estimates of the other coefficients, causing 
potential bias. This is demonstrated in Figure 7.1. Given the pattern of the 
X and Y observations, estimating a regression equation with a constant term 
would likely produce an estimated regression line very similar to the true 
regression line, which has a constant term (β0) quite different from zero. 
The slope of this estimated line is very low, and the t-score of the estimated 
slope coefficient may be very close to zero.
However, if the researcher were to suppress the constant term, which 
implies that the estimated regression line must pass through the origin, then 
the estimated regression line shown in Figure 7.1 would result. The slope 
Figure 7.1  The Harmful Effect of Suppressing the Constant Term
If the constant (or intercept) term is suppressed, the estimated regression will go through 
the origin. Such an effect potentially biases the βNs and inflates their t-scores. In this par-
ticular example, the true slope is close to zero in the range of the sample, but forcing the 
regression through the origin makes the slope appear to be significantly positive.
Y
0
X
Estimated Relationship
Suppressing the Intercept
True Relation
Observations
b0


192
Chapter 7  Specification: Choosing a Functional Form 
coefficient is biased upward compared with the true slope coefficient. The 
t-score is biased upward as well, and it may very well be large enough to indi-
cate that the estimated slope coefficient is statistically significantly positive. 
Such a conclusion would be incorrect.
Thus, even though some regression packages allow the constant term to be 
suppressed (set to zero), the general rule is: Don’t!
Do Not Rely on Estimates of the Constant Term
It would seem logical that if it’s a bad idea to suppress the constant term, 
then the constant term must be an important analytical tool to use in evalu-
ating the results of the regression. Unfortunately, there are at least two rea-
sons that suggest that the intercept should not be relied on for purposes of 
analysis or inference.
First, the error term is generated, in part, by the omission of a number 
of marginal independent variables, the mean effect of which is placed in 
the constant term. The constant term acts as a garbage collector, with an 
unknown amount of this mean effect being dumped into it. The constant 
term’s estimated coefficient may be different from what it would have been 
without performing this task, which is done for the sake of the equation as a 
whole. As a result, it’s meaningless to run a t-test on βN 0.
Second, the constant term is the value of the dependent variable when 
all the independent variables and the error term are zero, but the variables 
used for economic analysis are usually positive. Thus, the origin often lies 
outside the range of sample observations (as can be seen in Figure 7.1). Since 
the constant term is an estimate of Y when the Xs are outside the range of the 
sample observations, estimates of it are tenuous.
7.2   Alternative Functional Forms
The choice of a functional form for an equation is a vital part of the specifica-
tion of that equation. Before we can talk about those functional forms, how-
ever, we need to make a distinction between an equation that is linear in the 
coefficients and one that is linear in the variables.
An equation is linear in the variables if plotting the function in terms of 
X and Y generates a straight line. For example, Equation 7.1:
	
Y = β0 + β1X + e	
(7.1)
is linear in the variables, but Equation 7.2:
	
Y = β0 + β1X2 + e	
(7.2)


193
  Alternative Functional Forms
is not linear in the variables, because if you were to plot Equation 7.2 it 
would be a quadratic, not a straight line.
An equation is linear in the coefficients only if the coefficients (the βs) 
appear in their simplest form—they are not raised to any powers (other than 
one), are not multiplied or divided by other coefficients, and do not them-
selves include some sort of function (like logs or exponents). For example, 
Equation 7.1 is linear in the coefficients, but Equation 7.3:
	
Y = β0 + Xβ1	
(7.3)
is not linear in the coefficients β0 and β1. Equation 7.3 is not linear because 
there is no rearrangement of the equation that will make it linear in the βs 
of original interest, β0 and β1. In fact, of all possible equations for a single 
explanatory variable, only functions of the general form:
	
f(Y) = β0 + β1f(X)	
(7.4)
are linear in the coefficients β0 and β1. Linear regression analysis can be 
applied to an equation that is nonlinear in the variables as long as the equa-
tion is linear in the coefficients. Indeed, when econometricians use the 
phrase “linear regression” (for example, in the Classical Assumptions), they 
usually mean “regression that is linear in the coefficients.”
The use of OLS requires that the equation be linear in the coefficients, but 
there is a wide variety of functional forms that are linear in the coefficients 
while being nonlinear in the variables. Indeed, in previous chapters we’ve 
already used several equations that are linear in the coefficients and nonlin-
ear in the variables, but we’ve said little about when to use such nonlinear 
equations. The purpose of the current section is to present the details of the 
most frequently used functional forms to help the reader develop the ability 
to choose the correct one when specifying an equation.
The choice of a functional form almost always should be based on 
the underlying theory and only rarely on which form provides the best 
fit. The logical form of the relationship between the dependent variable 
and the independent variable in question should be compared with the 
properties of various functional forms, and the one that comes closest to 
that underlying theory should be chosen. To allow such a comparison, 
the paragraphs that follow characterize the most frequently used forms in 
terms of graphs, equations, and examples. In some cases, more than one 
functional form will be applicable, but usually a choice between alterna-
tive functional forms can be made on the basis of the information we’ll 
present.


194
Chapter 7  Specification: Choosing a Functional Form 
Linear Form
The linear regression model, used almost exclusively in this text thus far, is 
based on the assumption that the slope of the relationship between the inde-
pendent variable and the dependent variable is constant:2
	
∆Y
∆Xk
= βk  k = 1, 2, . . . , K
If the hypothesized relationship between Y and X is such that the slope of the 
relationship can be expected to be constant, then the linear functional form 
should be used.
Since the slope is constant, the elasticity of Y with respect to X (the per-
centage change in the dependent variable caused by a 1-percent increase in 
the independent variable, holding the other variables in the equation con-
stant) can be calculated fairly easily:
	
ElasticityY, Xk =
∆Y/Y
∆Xk/Xk
= ∆Y
∆Xk # Xk
Y = βk Xk
Y
Unless theory, common sense, or experience justifies using some other 
functional form, you should use the linear model. Because, in effect, it’s 
being used by default, the linear model is sometimes referred to as the default 
functional form.
Double-Log Form
The double-log form is the most common functional form that is nonlinear in 
the variables while still being linear in the coefficients. Indeed, the double-log 
form is so popular that some researchers use it as their default functional form 
instead of the linear form. In a double-log functional form, the natural log of 
Y is the dependent variable and the natural log of X is the independent variable:
	
lnY = β0 + β1 lnX1 + β2 lnX2 + e	
(7.5)
where lnY refers to the natural log of Y, and so on. For a brief review of the 
meaning of a natural log, see the boxed feature on pages 196 and 197.
2. Throughout this section, the “delta” notation (∆) will be used instead of the calculus notation 
to make for easier reading. The specific definition of ∆ is “change,” and it implies a small change 
in the variable it is attached to. For example, the term ∆X should be read as “change in X.” Since 
a regression coefficient represents the change in the expected value of Y brought about by a one-
unit increase in Xk (holding constant all other variables in the equation), then βk = ∆Y/∆Xk. 
Those comfortable with calculus should substitute partial derivative signs for ∆s.


195
  Alternative Functional Forms
The double-log form, sometimes called the log-log form, often is used 
because a researcher has specified that the elasticities of the model are con-
stant and the slopes are not. This is in contrast to the linear model, in which 
the slopes are constant but the elasticities are not.
In a double-log equation, an individual regression coefficient can be inter-
preted as an elasticity because:
	
βk = ∆(lnY)
∆(lnXk) =
∆Y/Y
∆Xk/Xk
= ElasticityY, Xk	
(7.6)
Since regression coefficients are constant, the condition that the model have 
a constant elasticity is met by the double-log equation.
The way to interpret βk in a double-log equation is that if Xk increases by 
1 percent while the other Xs are held constant, then Y will change by βk per-
cent. Since elasticities are constant, the slopes are now no longer constant.
Figure 7.2 is a graph of the double-log function (ignoring the error term). 
The panel on the left shows the economic concept of an isoquant or an indif-
ference curve. Isoquants from production functions show the different com-
binations of factors X1 and X2, probably capital and labor, that can be used to 
produce a given level of output Y. The panel on the right of Figure 7.2 shows 
Figure 7.2  Double-Log Functions
Depending on the values of the regression coefficients, the double-log functional form 
can take on a number of shapes. The left panel shows the use of a double-log function 
to depict a shape useful in describing the economic concept of an isoquant or an indif-
ference curve. The right panel shows various shapes that can be achieved with a double-
log function if X2 is held constant or is not included in the equation.
X2
0
X1
Y1
Y2
 lnY 5 b0 1 b1lnX1 1 b2lnX2
Y
0
X1
b1 . 1
b1 , 0
0 , b1 , 1


196
Chapter 7  Specification: Choosing a Functional Form 
the relationship between Y and X1 that would exist if X2 were held constant 
or were not included in the model. Note that the shape of the curve depends 
on the sign and magnitude of coefficient β1. If β1 is negative, a double-log 
functional form can be used to model a typical demand curve.
Double-log models should be run only when the logged variables take 
on positive values. Dummy variables, which can take on the value of zero, 
should not be logged.
Semilog Form
The semilog functional form is a variant of the double-log equation in 
which some but not all of the variables (dependent and independent) are 
expressed in terms of their natural logs. For example, you might choose to 
use the logarithm of one of the original independent variables, as in:
	
Yi = β0 + β1 ln X1i + β2X2i + ei	
(7.7)
In this case, the economic meanings of the two slope coefficients are differ-
ent, since X2 is linearly related to Y while X1 is nonlinearly related to Y.
What Is a Log?
What the heck is a log? If e (a constant equal to 2.71828) to the “bth power” 
produces x, then b is the log of x:
b is the log of x to the base e if: eb = x
Thus, a log (or logarithm) is the exponent to which a given base must be taken 
in order to produce a specific number. While logs come in more than one variety, 
we’ll use only natural logs (logs to the base e) in this text. The symbol for a natu-
ral log is “ln,” so ln1x2 = b means that 12.718282b = x or, more simply,
ln1x2 = b  means that  eb = x
For example, since e2 = 12.7182822 = 7.389, we can state that:
ln17.3892 = 2
Thus, the natural log of 7.389 is 2! Two is the power of e that produces 7.389. 
Let’s look at some other natural log calculations:
ln11002
 =
4.605
ln110002
 =
6.908


197
  Alternative Functional Forms
The right-hand side of Figure 7.3 shows the relationship between Y and X1 in 
this kind of semilog equation when X2 is held constant. Note that if β1 is greater 
than zero, the impact of changes in X1 on Y decreases as X1 gets bigger. Thus, the 
semilog functional form should be used when the relationship between X1 and 
Y is hypothesized to have this “increasing at a decreasing rate” form.4
Applications of the semilog form are quite frequent. For example, 
most consumption functions tend to increase at a decreasing rate past 
ln1100002
 =
9.210
ln11000002  = 11.513
ln110000002 = 13.816
Note that as a number goes from 100 to 1,000,000, its natural log goes from 
4.605 to only 13.816! Since logs are exponents, even a small change in a log 
can mean a big change in impact. As a result, logs can be used in economet-
rics if a researcher wants to reduce the absolute size of the numbers associ-
ated with the same actual meaning.
One useful property of natural logs in econometrics is that they make 
it easier to figure out impacts in percentage terms. If you run a double-log 
regression, the meaning of a slope coefficient is the percentage change in the 
dependent variable caused by a one percentage point increase in the inde-
pendent variable, holding the other independent variables in the equation 
constant.3 It’s because of this percentage change property that the slope coef-
ficients in a double-log equation are elasticities.
3. This is because the derivative of a natural log of X equals dX/X (or ∆X/X), which is the same 
as percentage change.
4. Another functional form that can be used when you anticipate that the relationship between 
X and Y has an “increasing at a decreasing rate” shape is the inverse functional form. This form 
expresses Y as a function of the reciprocal (or inverse) of one or more of the independent vari-
ables (in this case X1):
Yi = β0 + β1(1/X1i) + β2X2i + ei
The inverse functional form should be used when the impact of a particular independent vari-
able is expected to approach zero as that independent variable approaches infinity. To see this, 
note that as X1 gets larger, its impact on Y decreases.
Be careful, however, because X1 cannot equal zero, since if X1 equaled zero, dividing it into 
anything would result in infinite or undefined values.


198
Chapter 7  Specification: Choosing a Functional Form 
some level of income. These Engel curves tend to flatten out because as 
incomes get higher, a smaller percentage of income goes to consumption 
and a greater percentage goes to saving. Consumption thus increases at a 
decreasing rate. If Y is the consumption of an item and X1 is disposable 
income (with X2 standing for all the other independent variables), then 
the use of the semilog functional form is justified whenever the item’s 
consumption can be expected to increase at a decreasing rate as income 
increases.
For example, recall the beef demand equation, Equation 2.7, from Chapter 2:
	
 CBt = 37.54 -  0.88Pt +  11.9Ydt	
(2.7)
	
 
 (0.16)
 (1.76)
	
t = 	
-5.36	
 6.75
	
R  2 = 0.631	 N = 28 (annual)
where:	
CB = per capita consumption of beef 
	
P  = the price of beef in cents per pound
	
Yd = U.S. disposable income in thousands of dollars
8
Figure 7.3  Semilog Functions
The semilog functional form on the right (lnX) can be used to depict a situation in 
which the impact of X1 on Y is expected to increase at a decreasing rate as X1 gets bigger 
as long as β1 is greater than zero (holding X2 constant). The semilog functional form 
on the left (lnY) can be used to depict a situation in which an increase in X1 causes Y to 
increase at an increasing rate.
Y 5 (b0 1 b2X2)
1 b1lnX1
Y
0
X1
(Holding X2 constant)
b1 . 0
b1 , 0
b1 . 0
Y
0
X1
(Holding X2 constant)
b1 , 0
lnY 5 b0 1 b1X1 1 b2X2


199
  Alternative Functional Forms
If we substitute the log of disposable income (lnYdt) for disposable income 
in Equation 2.7, we get:
	
CBt = -71.75 - 0.87Pt + 98.87lnYdt	
(7.8)
	
10.132	 111.112
	
t = 	
-6.93	
8.90
	
R  2 = .750	 N = 28 1annual2
In Equation 7.8, the independent variables include the price of beef and the log 
of disposable income. Equation 7.8 would be appropriate if we hypothesize 
that as income rises, consumption will increase at a decreasing rate. For other 
products, perhaps like yachts or summer homes, no such decreasing rate could 
be hypothesized, and the semilog function would not be appropriate.
Not all semilog functions have the log on the right-hand side of the equa-
tion, as in Equation 7.7. The alternative semilog form is to have the log on 
the left-hand side of the equation. This would mean that the natural log of Y 
would be a function of unlogged values of the Xs, as in:
	
lnY = β0 + β1X1 + β2X2 + e	
(7.9)
This model has neither a constant slope nor a constant elasticity, but the coef-
ficients do have a very useful interpretation. If X1 increases by one unit, then 
Y will change in percentage terms. Specifically, Y will change by β1 # 100 per-
cent for every unit that X1 increases, holding X2 constant. The left-hand side 
of Figure 7.3 shows such a semilog function.
This fact means that the lnY semilog function of Equation 7.9 is perfect 
for any model in which the dependent variable adjusts in percentage terms 
to a unit change in an independent variable. The most common economic 
and business application of Equation 7.9 is in a model of the earnings of 
individuals, where firms often give annual raises in percentage terms. In such 
a model, Y would be the salary or wage of the ith employee, and X1 would be 
the experience of the ith worker. Each year X1 would increase by one, and β1 
would measure the percentage raises given by the firm.
Note that we now have two different kinds of semilog functional forms, 
creating possible confusion. As a result, many econometricians use phrases like 
“right-side semilog” or “lin-log functional form” to refer to Equation 7.7 while 
using “left-side semilog” or “log-lin functional form” to refer to Equation 7.9.
Polynomial Form
In most average cost functions, the slope of the cost curve changes sign as output 
changes. If the slopes of a relationship are expected to depend on the level of 
the variable itself, then a polynomial model should be considered. Polynomial 
8


200
Chapter 7  Specification: Choosing a Functional Form 
functional forms express Y as a function of independent variables, some of which 
are raised to powers other than 1. For example, in a second-degree polynomial 
(also called a quadratic) equation, at least one independent variable is squared:
	
Yi = β0 + β1X1i + β2(X1i)2 + β3X2i + ei	
(7.10)
Such a model can indeed produce slopes that change sign as the independent 
variables change. The slope of Y with respect to X1 in Equation 7.10 is:
	
∆Y
∆X1
= β1 + 2β2X1	
(7.11)
Note that the slope depends on the level of X1. For small values of X1, β1 might 
dominate, but for large values of X1, β2 will always dominate. If this were a cost 
function, with Y being the average cost of production and X1 being the level of 
output of the firm, then we would expect β1 to be negative and β2 to be positive if 
the firm has the typical U-shaped cost curve depicted in the left half of Figure 7.4.
For another example, consider a model of annual employee earnings as 
a function of the age of each employee and a number of other measures of 
productivity such as education. What is the expected impact of age on earn-
ings? As a young worker gets older, his or her earnings will typically increase. 
Figure 7.4  Polynomial Functions
Quadratic functional forms (polynomials with squared terms) take on U or inverted U 
shapes, depending on the values of the coefficients (holding X2 constant). The left panel 
shows the shape of a quadratic function that could be used to show a typical cost curve; 
the right panel allows the description of an impact that rises and then falls (like the 
impact of age on earnings).
Y 5 (b0 1 b3X2) 1 (b1X1 1 b2X1)
2
Y
0
X1
(Holding X2 constant)
b2 . 0
b1 , 0
Y
0
X1
(Holding X2 constant)
b2 , 0
b1 . 0


201
  Alternative Functional Forms
Beyond some point, however, an increase in age will not increase earnings by 
very much at all, and around retirement we’d expect earnings to start to fall 
abruptly with age. As a result, a logical relationship between earnings and age 
might look something like the right half of Figure 7.4; earnings would rise, 
level off, and then fall as age increased. Such a theoretical relationship could 
be modeled with a quadratic equation:
	
Earningsi = β0 + β1Agei + β2Age  2
i + g + ei	
(7.12)
What would the expected signs of βN 1 and βN 2 be? Since you expect the impact 
of age to rise and fall, you’d thus expect βN 1 to be positive and βN 2 to be nega-
tive (all else being equal). In fact, this is exactly what many researchers in 
labor economics have observed.
With polynomial regressions, the interpretation of the individual regres-
sion coefficients becomes difficult, and the equation may produce unwanted 
results for particular ranges of X. Great care must be taken when using a poly-
nomial regression equation to ensure that the functional form will achieve 
what is intended by the researcher and no more.
Choosing a Functional Form
The best way to choose a functional form for a regression model is to select 
the specification that best matches the underlying theory of the equation. 
In a majority of cases, the linear form will be adequate, and for most of the 
rest, common sense will point out a fairly easy choice from the alternatives 
outlined above. Table 7.1 contains a summary of the properties of the various 
alternative functional forms.
Table 7.1  Summary of Alternative Functional Forms
Functional Form
Equation (one X only)
The Change in Y when X Changes
Linear
Yi = β0 + β1Xi + ei
If X increases by one unit, Y will 
change by β1 units.
Double-log
lnYi = β0 + β1 lnXi + ei
If X increases by one percent, Y will 
change by β1 percent. (Thus  β1 is 
the elasticity of Y with respect to X.)
Semilog (lnX)
Yi = β0 + β1 lnXi + ei
If X increases by one percent, Y will 
change by β1>100 units.
Semilog (lnY)
lnYi = β0 + β1Xi + ei
If X increases by one unit, Y will 
change by roughly 100β1 percent.
Polynomial
Yi = β0 + β1Xi + β2X  2
i + ei
If X increases by one unit, Y will 
change by 1β1 + 2β2X2 units.


202
Chapter 7  Specification: Choosing a Functional Form 
7.3   Lagged Independent Variables
Virtually all the regressions we’ve studied so far have been “instantaneous” in 
nature. In other words, they have included independent and dependent vari-
ables from the same time period, as in:
	
Yt = β0 + β1X1t + β2X2t + et	
(7.13)
where the subscript t is used to refer to a particular point in time. If all vari-
ables have the same subscript, then the equation is instantaneous.
However, not all economic or business situations imply such instanta-
neous relationships between the dependent and independent variables. In 
many cases time elapses between a change in the independent variable and 
the resulting change in the dependent variable. The period of time between 
the cause (the change in X) and the effect (the change in Y) is called a lag. 
Time periods can be measured in days, months, years, etc. Many econo-
metric equations include one or more lagged independent variables like 
X1t-1, where the subscript t - 1 indicates that the observation of X1 is from 
the time period previous to time period t, as in the following equation:
	
Yt = β0 + β1X1t-1 + β2X2t + et	
(7.14)
In this equation, X1 has been lagged by one time period, but the relationship 
between Y and X2 is still instantaneous. While this one-time-period lag is 
the most frequent lag in economics, lags of two or more time periods can be 
used when justified by the underlying theory.
For an example of a lagged independent variable, think about the process 
by which the supply of an agricultural product is determined. Since agri-
cultural goods take time to grow, decisions on how many acres to plant or 
how many eggs to let hatch into egg-producing hens (instead of selling them 
immediately) must be made months, if not years, before the product is actu-
ally supplied to the consumer. Any change in an agricultural market, such as 
an increase in the price that the farmer can earn for providing cotton, has a 
lagged effect on the supply of that product:
	
+ 	
-
	
Ct = β0 + β1PCt-1 + β2PFt + et	
(7.15)
where:	
Ct
 = the quantity of cotton supplied in year t
	
PCt-1 = the price of cotton in year t - 1
	
PFt
 = the price of farm labor in year t
Note that this equation hypothesizes a lag between the price of cotton and 
the production of cotton, but not between the price of farm labor and the 


203
  Slope Dummy Variables
production of cotton. It’s reasonable to think that if cotton prices change, 
farmers won’t be able to react immediately because it takes a while for cotton 
to be planted and to grow.
The meaning of the regression coefficient of a lagged variable is not the 
same as the meaning of the coefficient of an unlagged variable. The estimated 
coefficient of a lagged X measures the change in this year’s Y attributed to a 
one-unit increase in last year’s X (holding constant the other Xs in the equa-
tion). Thus β1 in Equation 7.15 measures the extra number of units of cot-
ton that would be produced this year as a result of a one-unit increase in last 
year’s price of cotton, holding this year’s price of farm labor constant.
If the lag structure is hypothesized to take place over more than one time 
period, or if a lagged dependent variable is included on the right-hand side 
of an equation, the question becomes significantly more complex. Such 
cases, called distributed lags, will be dealt with in Chapter 12.
7.4   Slope Dummy Variables
In Section 3.3 we introduced the concept of a dummy variable, which we 
defined as one that takes on the values of 0 or 1, depending on a qualita-
tive attribute such as gender. In that section our sole focus was on the use of 
a dummy variable as an intercept dummy, which changes the constant or 
intercept term, depending on whether the qualitative condition is met. These 
take the general form:
	
Yi = β0 + β1Xi + β2Di + ei	
(7.16)
	
where Di = e 1 if the ith observation meets a particular condition
0 otherwise
Until now, every independent variable in this text has been multiplied by 
exactly one other item: the slope coefficient. To see this, take another look at 
Equation 7.16. As you can see, X is multiplied only by β1, and D is multiplied 
only by β2, and there are no other factors involved.
This restriction does not apply to a new kind of variable called an interac-
tion term. An interaction term is an independent variable in a regression 
equation that is the multiple of two or more other independent variables. 
Each interaction term has its own regression coefficient, so the end result is 
that the interaction term has three or more components, as in β3XiDi. Such 
interaction terms are used when the change in Y with respect to one indepen-
dent variable (in this case X) depends on the level of another independent 
variable (in this case D). For an example of the use of interaction terms, see 
Exercise 8.


204
Chapter 7  Specification: Choosing a Functional Form 
Interaction terms can involve two quantitative variables (β3X1X2) or two 
dummy variables (β3D1D2), but the most frequent application of interaction 
terms involves one quantitative variable and one dummy variable (β3X1D1), 
a combination that is typically called a slope dummy. Slope dummy variables 
allow the slope of the relationship between the dependent variable and an 
independent variable to be different depending on whether the condition 
specified by a dummy variable is met. This is in contrast to an intercept 
dummy variable, which changes the intercept, but does not change the slope, 
when a particular condition is met.
In general, a slope dummy is introduced by adding to the equation a vari-
able that is the multiple of the independent variable that has a slope you 
want to change and the dummy variable that you want to cause the changed 
slope. The general form of a slope dummy equation is:
	
Yi = β0 + β1Xi + β2Di + β3XiDi + ei	
(7.17)
Note that Equation 7.17 is the same as Equation 7.16, except that we have 
added an interaction term in which the dummy variable is multiplied by an 
independent variable (β3XiDi). Let’s check to make sure that the slope of Y 
with respect to X does indeed change if D changes:
	
When D = 0, ∆Y/∆X = β1
	
When D = 1, ∆Y/∆X = (β1 + β3)
In essence, the coefficient of X changes when the condition specified by 
D is met. To see this, substitute D = 0 and D = 1, respectively, into 
Equation 7.17 and factor out X.
Note that Equation 7.17 includes both a slope dummy and an intercept 
dummy. It turns out that whenever a slope dummy is used, it’s vital to also 
have β1Xi and β2D in the equation to avoid bias in the estimate of the coef-
ficient of the slope dummy term. If there are other Xs in an equation, they 
should not be multiplied by D unless you hypothesize that their slopes 
change with respect to D as well.
Take a look at Figure 7.5, which has both a slope dummy and an intercept 
dummy. In Figure 7.5 the intercept will be β0 when D = 0 and β0 + β2 when 
D = 1. In addition, the slope of Y with respect to X will be β1 when D = 0 
and β1 + β3 when D = 1. As a result, there really are two equations:
	
Yi =
 β0
 + β1Xi + ei  [when D = 0]
	
 Yi =  (β0 + β2) + (β1 + β3)Xi + ei  [when D = 1]
In practice, slope dummies have many realistic uses. For example, consider 
the question of earnings differentials between men and women. Although 
there is little argument that these differentials exist, there is quite a bit of 


205
  Slope Dummy Variables
controversy over the extent to which these differentials are caused by sexual 
discrimination (as opposed to other factors). Suppose you decide to build a 
model of earnings to get a better view of this controversy. If you hypothesized 
that men earn more than women on average, then you would want to use an 
intercept dummy variable for gender in an earnings equation that included 
measures of experience, special skills, education, and so on, as independent 
variables:
	
ln(Earningsi) = β0 + β1Di + β2EXPi + g + ei	
(7.18)
where:	
Di
 = 1 if the ith worker is male and 0 otherwise
	
EXPi = the years experience of the ith worker
	
ei
 = a classical error term
In Equation 7.18, βN 1 would be an estimate of the average difference in earnings 
between males and females, holding constant their experience and the other 
factors in the equation. Equation 7.18 also forces the impact of increases in 
experience (and the other factors in the equation) to have the same effect for 
females as for males because the slopes are the same for both genders.
Figure 7.5  Slope and Intercept Dummies
If slope dummy (β3XiDi) and intercept dummy (β2Di) terms are added to an equation, 
a graph of the equation will have different intercepts and different slopes depending on 
the value of the qualitative condition specified by the dummy variable. The difference 
between the two intercepts is β2, whereas the difference between the two slopes is β3.
Y
0
X
Di 5 0
b2
b0
b0 1 b2
(b2 . 0)
Di 5 1
Slope 5 b1
Slope 5 b1 1 b3
(b3 . 0)
Yi 5 b0 1 b1Xi 1 b2Di 1 b3XiDi


206
Chapter 7  Specification: Choosing a Functional Form 
If you hypothesized that men also increase their earnings more per year of 
experience than women, then you would include a slope dummy as well as 
an intercept dummy in such a model:
	
ln(Earningsi) = β0 + β1Di + β2EXPi + β3DiEXPi + g + ei	 (7.19)
In Equation 7.19, βN 3 would be an estimate of the differential impact of an 
extra year of experience on earnings between men and women. We could test 
the possibility of a positive true β3 by running a one-tailed t-test on βN 3. If βN 3 
were significantly different from zero in a positive direction, then we could 
reject the null hypothesis of no difference due to gender in the impact of 
experience on earnings, holding constant the other variables in the equation.
7.5   Problems with Incorrect Functional Forms
Once in a while a circumstance will arise in which the model is logically non-
linear in the variables, but the exact form of this nonlinearity is hard to spec-
ify. In such a case, the linear form is not correct, and yet a choice between the 
various nonlinear forms cannot be made on the basis of economic theory. 
Even in these cases, however, it still pays (in terms of understanding the true 
relationships) to avoid choosing a functional form on the basis of fit alone.
If functional forms are similar, and if theory does not specify exactly which 
form to use, why should we try to avoid using goodness of fit over the sample 
to determine which equation to use? This section will highlight two answers 
to this question:
1.	 R  2s are difficult to compare if the dependent variable is transformed.
2.	 An incorrect functional form may provide a reasonable fit within the 
sample but have the potential to make large forecast errors when used 
outside the range of the sample.
r2s Are Difficult to Compare When Y Is Transformed
When the dependent variable is transformed from its linear version, the over-
all measure of fit, the R2, cannot be used for comparing the fit of the non-
linear equation with the original linear one.5 This problem is not especially 
important in most cases because the emphasis in applied regression analysis 
5. This warning also applies to other measures of overall fit, for example Akaike’s Information 
Criterion (AIC) and the Bayesian Information Criterion (BIC) of Section 6.7, the appendix on 
additional specification criteria.


207
  Problems with Incorrect Functional Forms
is usually on the coefficient estimates. However, if R  2s are ever used to com-
pare the fit of two different functional forms, then it becomes crucial that this 
lack of comparability be remembered. For example, suppose you were trying 
to compare a linear equation:
	
Y = β0 + β1X1 + β2X2 + e	
(7.20)
with a semilog version of the same equation (using the version of a semilog 
function that takes the log of the dependent variable):
	
lnY = β0 + β1X1 + β2X2 + e	
(7.21)
Notice that the only difference between Equations 7.20 and 7.21 is the 
functional form of the dependent variable. The reason that the R  2s of the 
respective equations cannot be used to compare overall fits of the two equa-
tions is that the total sum of squares (TSS) of the dependent variable around 
its mean is different in the two formulations. That is, the R  2s are not com-
parable because the dependent variables are different. There is no reason to 
expect that different dependent variables will have the identical (or easily 
comparable) degrees of dispersion around their means.
Incorrect Functional Forms Outside the Range of the Sample
If an incorrect functional form is used, then the probability of mistaken 
inferences about the true population parameters will increase. Using an 
incorrect functional form is a kind of specification error that is similar to the 
omitted variable bias discussed in Section 6.1. Even if an incorrect functional 
form provides good statistics within a sample, large residuals almost surely 
will arise when the misspecified equation is used on data that were not part 
of the sample used to estimate the coefficients.
In general, the extrapolation of a regression equation to data that are out-
side the range over which the equation was estimated runs increased risks of 
large forecasting errors and incorrect conclusions about population values. 
This risk is heightened if the regression uses a functional form that is inap-
propriate for the particular variables being studied.
Two functional forms that behave similarly over the range of the sample 
may behave quite differently outside that range. If the functional form is cho-
sen on the basis of theory, then the researcher can take into account how the 
equation would act over any range of values, even if some of those values are 
outside the range of the sample. If functional forms are chosen on the basis 
of fit, then extrapolating outside the sample becomes tenuous.
Figure 7.6 contains a number of hypothetical examples. As can be seen, 
some functional forms have the potential to fit quite poorly outside the 


208
Chapter 7  Specification: Choosing a Functional Form 
sample range. Such graphs are meant as examples of what could happen, 
not as statements of what necessarily will happen, when incorrect func-
tional forms are pushed outside the range of the sample over which they 
were estimated. Do not conclude from these diagrams that nonlinear func-
tions should be avoided. If the true relationship is nonlinear, then the 
Figure 7.6  Incorrect Functional Forms Outside the Sample Range
If an incorrect form is applied to data outside the range of the sample on which it was 
estimated, the probability of large mistakes increases. In particular, note how the poly-
nomial functional form can change slope rapidly outside the sample range (panel b) 
and that even a linear form can cause mistakes if the true functional form is nonlinear 
(panel d).
Y
0
X
(a) Double-Log (b , 0)
Sample
Y
0
X
Out of Sample
(b) Polynomial
Sample
Y
0
X
Out of Sample
Out of Sample
(c) Semilog Right
Sample
Out of Sample
Y
0
X
(d) Linear
Sample


209
  Summary
linear functional form will make large forecasting errors outside the sample. 
Instead, the researcher must take the time to think through how the equation 
will act for values both inside and outside the sample before choosing a func-
tional form to use to estimate the equation. If the theoretically appropriate 
nonlinear equation appears to work well over the relevant range of possible 
values, then it should be used without concern over this issue.
7.6   Summary
	 1.	 Do not suppress the constant term. On the other hand, don’t rely on 
estimates of the constant term for inference even if it appears to be 
statistically significant.
	 2.	 The choice of a functional form should be based on the underlying 
economic theory to the extent that theory suggests a shape similar to 
that provided by a particular functional form. A form that is linear 
in the variables should be used unless a specific hypothesis suggests 
otherwise.
	 3.	 Functional forms that are nonlinear in the variables include the 
double-log form, the semilog form, and the polynomial form. 
The double-log form is especially useful if the elasticities involved are 
expected to be constant. The semilog form has the advantage of al-
lowing the effect of an independent variable to tail off as that variable 
increases. The polynomial form is useful if the slopes are expected to 
change sign, depending on the level of an independent variable.
	 4.	 A slope dummy is a dummy variable that is multiplied by an in-
dependent variable to allow the slope of the relationship between 
the dependent variable and the particular independent variable to 
change, depending on whether a particular condition is met.
	 5.	 The use of nonlinear functional forms has a number of potential 
problems. In particular, the R  2s are difficult to compare if Y has 
been transformed, and the residuals are potentially large if an incor-
rect functional form is used for forecasting outside the range of the 
sample.


210
Chapter 7  Specification: Choosing a Functional Form 
Exercises
(The answers to the even-numbered exercises are in Appendix A.)
	 1.	 Write the meaning of each of the following terms without referring to 
the book (or your notes), and compare your definition with the ver-
sion in the text for each.
a.	 double-log functional form (p. 194)
b.	 elasticity (p. 194)
c.	 interaction term (p. 203)
d.	 intercept dummy (p. 203)
e.	 lag (p. 202)
f.	 linear in the coefficients (p. 193)
g.	 linear in the variables (p. 192)
h.	 log (p. 196)
i.	 natural log (p. 196)
j.	 polynomial functional form (p. 199)
k.	 semilog functional form (p. 196)
l.	 slope dummy (p. 204)
	 2.	 For each of the following pairs of dependent (Y) and independent 
(X) variables, pick the functional form that you think is likely to be 
appropriate, and then explain your reasoning (assume that all other 
relevant independent variables are included in the equation):
a.	 Y =  sales of shoes
	
X =  disposable income
b.	Y =  the attendance at the Hollywood Bowl outdoor symphony 
concerts on a given night
	
X =  whether the orchestra’s most famous conductor was sched-
uled to conduct that night
c.	 Y =  aggregate consumption of goods and services in the United 
States
	
X =  aggregate disposable income in the United States
d.	Y =  the money supply in the United States
	
X =  the interest rate on Treasury Bills (in a demand function)
e.	 Y =  the average production cost of a box of pasta
	
X =  the number of boxes of pasta produced
	 3.	 Look over the following equations and decide whether they are linear 
in the variables, linear in the coefficients, both, or neither:


211
Exercises
a.	 Yi = β0 + β1X  3
i + ei
b.	Yi = β0 + β1ln Xi + ei
c.	 ln Yi = β0 + β1ln Xi + ei
d.	Yi = β0 + β1X  β2
i + ei
e.	 Y  β0
i
= β1 + β2X  2
i + ei
	 4.	 In 2003, Ray Fair6 analyzed the relationship between stock prices and 
risk aversion by looking at the 1996–2000 performance of the 65 
companies that had been a part of Standard and Poor’s famous index 
(the S&P 500) since its inception in 1957. Fair focused on the P/E 
ratio (the ratio of a company’s stock price to its earnings per share) 
and its relationship to the beta coefficient (a measure of a company’s 
riskiness—a high beta implies high risk). Hypothesizing that the 
stock price would be a positive function of earnings growth and divi-
dend growth, he estimated the following equation:
LNPEi = 2.74 - 0.22BETAi + 0.83EARNi + 2.81DIVi
	
10.112	
10.572	
10.842
	
t = 	
-1.99	
1.44	
3.33
	
N = 65	 R2 = .232	
R  2 = .194
where:	
LNPEi = the log of the median P/E ratio of the ith com-
pany from 1996 to 2000
	
	 	
BETAi  = the mean beta coefficient of the ith company 
from 1958 to 1994
	
	 	
EARNi = the median percentage earnings growth rate for 
the ith company from 1996 to 2000
	
	 	
DIVi
 = the median percentage dividend growth rate for 
the ith company from 1996 to 2000
a.	Create and test appropriate hypotheses about the slope coefficients 
of this equation at the 5-percent level.
b.	One of these variables is lagged and yet this is a cross-sectional equa-
tion. Explain which variable is lagged and why you think Fair lagged it.
c.	 Is one of Fair’s variables potentially irrelevant? Which one? Use 
Stata, EViews, or your own regression program on the data in 
Table 7.2 to estimate Fair’s equation without your potentially 
h
6. Ray C. Fair, “Risk Aversion and Stock Prices,” Cowles Foundation Discussion Papers 1382, 
Cowles Foundation: Yale University, revised February 2003 © 2003. Most of the article is well 
beyond the scope of this text, but Fair generously included the data (including proprietary data 
that he generated) necessary to replicate his regression results. Note that the beta coefficient is 
not the same as the β regression coefficient used in econometrics.


212
Chapter 7  Specification: Choosing a Functional Form 
Table 7.2  Data for the Stock Price Example
COMPANY
PE
BETA
EARN
DIV
  1
Alcan
12.64
0.466
0.169
-0.013
  2
TXU Corp.
10.80
0.545
0.016
0.014
  3
Procter & Gamble
19.90
0.597
0.066
0.050
  4
PG&E
11.30
0.651
0.021
0.014
  5
Phillips Petroleum
13.27
0.678
0.071
0.006
  6
AT&T
13.71
0.697
-0.004
-0.008
  7
Minnesota Mining & Mfg.
17.61
0.781
0.054
0.051
  8
Alcoa
15.97
0.795
0.120
-0.015
  9
American Electric Power
10.68
0.836
-0.001
-0.021
10
Public Service Entrp
9.63
0.845
-0.018
-0.011
11
Hercules
16.07
0.851
0.077
-0.008
12
Air Products & Chemicals
16.20
0.865
0.051
0.074
13
Bristol Myers Squibb
17.01
0.866
0.068
0.110
14
Kimberly-Clark
13.42
0.869
0.063
0.018
15
Aetna
8.98
0.894
-0.137
0.007
16
Wrigley
14.49
0.898
0.062
0.044
17
Halliburton
17.84
0.906
0.120
-0.011
18
Deere & Co.
12.15
0.916
-0.010
0.004
19
Kroger
11.82
0.931
0.010
0.000
20
Intl Business Machines
16.08
0.944
0.081
0.045
21
Caterpillar
16.95
0.952
-0.043
-0.005
22
Goodrich
12.06
0.958
0.028
-0.015
23
General Mills
17.16
0.965
0.060
0.048
24
Winn-Dixie Stores
16.10
0.973
0.045
0.047
25
Heinz (H J)
13.49
0.979
0.079
0.079
26
Eastman Kodak
28.28
0.983
0.023
0.009
27
Campbell Soup
16.33
0.986
0.028
0.025
28
Philip Morris
12.25
0.993
0.129
0.130
29
Southern Co.
11.26
0.995
0.034
0.000
30
Du Pont
14.16
0.996
0.099
0.001
31
Phelps Dodge
11.47
1.008
0.186
-0.011
32
Pfizer Inc.
17.63
1.019
0.052
0.062
33
Hershey Foods
14.66
1.022
0.025
0.058
34
Ingersoll-Rand
14.24
1.024
0.045
-0.018
(continued )


213
Exercises
COMPANY
PE
BETA
EARN
DIV
35
FPL Group
11.86
1.048
0.038
0.019
36
Pitney Bowes
16.11
1.064
0.049
0.086
37
Archer-Daniels-Midland
14.43
1.073
0.073
-0.011
38
Rockwell
9.42
1.075
0.062
0.020
39
Dow Chemical
15.25
1.081
0.042
0.026
40
General Electric
15.16
1.091
0.051
0.015
41
Abbott Laboratories
17.58
1.097
0.114
0.098
42
Merck & Co.
23.29
1.122
0.066
0.072
43
J C Penney
13.14
1.133
0.094
-0.003
44
Union Pacific Corp.
12.99
1.136
0.010
0.021
45
Schering-Plough
18.18
1.137
0.112
0.060
46
Pepsico
18.94
1.147
0.082
0.046
47
McGraw-Hill
16.93
1.150
0.051
0.052
48
Household International
8.36
1.184
0.019
0.008
49
Emerson Electric
17.52
1.196
0.047
0.044
50
General Motors
11.21
1.206
0.052
-0.023
51
Colgate-Palmolive
16.60
1.213
0.067
0.025
52
Eaton Corp.
10.64
1.216
0.137
0.001
53
Dana Corp.
10.26
1.222
0.069
-0.011
54
Sears Roebuck
12.41
1.256
0.030
-0.014
55
Corning Inc.
19.33
1.258
0.052
-0.013
56
General Dynamics
9.06
1.285
0.056
-0.023
57
Coca-Cola
21.68
1.290
0.085
0.055
58
Boeing
11.93
1.306
0.169
0.017
59
Ford
8.62
1.308
0.016
0.026
60
Peoples Energy
9.58
1.454
0.000
0.005
61
Goodyear
12.02
1.464
0.022
0.012
62
May Co.
11.32
1.525
0.050
0.006
63
ITT Industries
9.92
1.630
0.038
0.018
64
Raytheon
11.75
1.821
0.112
0.050
65
Cooper Industries
12.41
1.857
0.108
0.037
Source: Ray C. Fair, “Risk Aversion and Stock Prices,” Cowles Foundation Discussion Papers 
1382, Cowles Foundation: Yale University, revised February 2003 © 2003.
Datafile = STOCK7
Table 7.2  (continued)


214
Chapter 7  Specification: Choosing a Functional Form 
irrelevant variable and then use our four specification criteria to 
determine whether the variable is indeed irrelevant.
d.	What functional form does Fair use? Does this form seem appro-
priate on the basis of theory? (Hint: A review of the literature would 
certainly help you answer this question, but before you start that 
review, think through the meaning of the slope coefficients in this 
functional form.)
e.	 (optional) Suppose that your review of the literature makes you 
concerned that Fair should have used a double-log functional form 
for his equation. Use the data in Table 7.2 to estimate that func-
tional form on Fair’s data. What is your estimated result? Does it 
support your concern? Explain.
	 5.	 In an effort to explain regional wage differentials, you collect wage 
data from 7,338 unskilled workers, divide the country into four 
regions (Northeast, South, Midwest, and West), and estimate the fol-
lowing equation (standard errors in parentheses):
	
 YNi = 4.78 - 0.038Ei -  0.041Si -  0.048Wi
	
 (0.019)
 (0.010)
 (0.012)
	
R  2 = .49  N = 7,338
where:	
Yi  = the hourly wage (in dollars) of the ith unskilled 
worker
	
	 	
Ei  = a dummy variable equal to 1 if the ith worker lives in 
the Northeast, 0 otherwise
	
	 	
Si  = a dummy variable equal to 1 if the ith worker lives in 
the South, 0 otherwise
	
	 	
Wi = a dummy variable equal to 1 if the ith worker lives in 
the West, 0 otherwise
a.	What is the omitted condition in this equation?
b.	If you add a dummy variable for the omitted condition to the 
equation without dropping Ei, Si, or Wi, what will happen?
c.	 If you add a dummy variable for the omitted condition to the 
equation and drop Ei, what will the sign of the new variable’s esti-
mated coefficient be?
d.	Which of the following three statements is most correct? Least cor-
rect? Explain your answers.
	
	
i.	
The equation explains 49 percent of the variation of Y 
around its mean with regional variables alone, so there must 
be quite a bit of wage variation by region.


215
Exercises
	
	
ii.	
The coefficients of the regional variables are virtually identi-
cal, so there must not be much wage variation by region.
	
	
iii.	
The coefficients of the regional variables are quite small 
compared with the average wage, so there must not be much 
wage variation by region.
	 6.	 Suggest the appropriate functional forms for the relationships 
between the following variables. Be sure to explain your reasoning:
a.	The age of the ith house in a cross-sectional equation for the sales 
price of houses in Cooperstown, New York. (Hint: Cooperstown is 
known as a lovely town with a number of elegant historic homes.)
b.	The price of natural gas in year t in a demand-side time-series equa-
tion for the consumption of natural gas in the United States.
c.	 The income of the ith individual in a cross-sectional equation for 
the number of suits owned by individuals.
d.	A dummy variable for being a student (1 = yes) in the equation 
specified in part c.
	 7.	 V. N. Murti and V. K. Sastri7 investigated the production character-
istics of various Indian industries, including cotton and sugar. They 
specified Cobb–Douglas production functions for output (Q) as a 
double-log function of labor (L) and capital (K):
	
lnQi = β0 + β1lnLi + β2lnKi + ei
	
	 and obtained the following estimates (standard errors in parentheses):
Industry
  훃N 0
   훃N 1
   훃N 2
 R2
Cotton
0.97
  0.92
  0.12
.98
 
(0.03)
(0.04)
Sugar
2.70
  0.59
  0.33
.80
(0.14)
(0.17)
a.	What are the elasticities of output with respect to labor and capital 
for each industry?
b.	What economic significance does the sum (βN 1 + βN 2) have?
c.	 Murti and Sastri expected positive slope coefficients. Test their hy-
potheses at the 5-percent level of significance. (Hint: This is much 
harder than it looks!)
7. V. N. Murti and V. K. Sastri, “Production Functions for Indian Industry,” Econometrica, Vol. 
25, No. 2, pp. 205–221.


216
Chapter 7  Specification: Choosing a Functional Form 
	 8.	 Richard Fowles and Peter Loeb studied the interactive effect of drink-
ing and altitude on traffic deaths.8 The authors hypothesized that 
drunk driving fatalities are more likely at high altitude than at low 
altitude because higher elevations diminish the oxygen intake of the 
brain, increasing the impact of a given amount of alcohol. To test 
this hypothesis, they used an interaction variable between altitude 
and beer consumption. They estimated the following cross-sectional 
model (by state for the continental United States) of the motor vehi-
cle fatality rate (Note: t-scores in parentheses):
	
 FNi = -  3.36 - 0.002Bi +  0.17Si -  0.31Di +  0.011Bi Ai	
(7.22)
	
 1 - 0.082
 11.852 1 - 1.292
 14.052
	
N = 48  R  2 = .499
where:	
Fi  = traffic fatalities per motor vehicle mile driven in the 
ith state
	
	 	
Bi  = per capita consumption of beer (malt beverages) in 
state i
	
	 	
Si  = average highway driving speed in state i
	
	 	
Di = a dummy variable equal to 1 if the ith state had a 
vehicle safety inspection program, 0 otherwise
	
	 	
Ai = the average altitude of metropolitan areas in state i (in 
thousands)
a.	Carefully state and test appropriate hypotheses about the coeffi-
cients of B, S, and D at the 5-percent level. Do these results give any 
indication of econometric problems in the equation? Explain.
b.	Think through the interaction variable. What is it measuring? Care-
fully state the meaning of the coefficient of B*A.
c.	 Create and test appropriate hypotheses about the coefficient of the 
interaction variable at the 5-percent level.
d.	Note that Ai is included in the equation in the interaction vari-
able but not as an independent variable on its own. If an equation 
includes an interaction variable, should both components of the 
8. Richard Fowles and Peter D. Loeb, “The Interactive Effect of Alcohol and Altitude on Traffic 
Fatalities,” Southern Economic Journal, Vol. 59, pp. 108–111. To focus the analysis, we have omit-
ted the coefficients of three other variables (the minimum legal drinking age, the percent of the 
population between 18 and 24, and the variability of highway driving speeds) that were insig-
nificant in Equations 7.22 and 7.23.


217
  Appendix: Econometric Lab #4
interaction be independent variables in the equation as a matter of 
course? Why or why not? (Hint: Recall that with slope dummies, 
we emphasized that both the intercept dummy term and the slope 
dummy variable term should be in the equation.)
e.	 When the authors included Ai in their model, the results were as 
in Equation 7.23 (with t-scores once again in parenthesis). Which 
equation do you prefer? Explain.
	
 FNi = -2.33 - 0.024Bi +  0.14Si -  0.24Di -  0.35Ai +  0.023Bi Ai	
(7.23)
	
 (- 0.80)
 (1.53) (- 0.96)  (- 1.07)
 (1.97)
	
N = 48 R  2 = .501
7.7   Appendix: Econometric Lab #4
This lab is an exercise in specification: choosing the variables and the func-
tional form. It also will give you experience in transforming variables and 
conducting joint hypothesis tests in Stata or your computer’s econometric 
software program. The dependent variable that we’re going to study is the 
price of a used farm tractor that was sold at auction in the United States.
Step 1: Review the Literature
Since you’re probably not an expert on the prices of used tractors, let’s start with 
a quick review of the literature. This is a model of the price of a used tractor 
as a function of the attributes of that tractor and the time of the sale, so this is 
another example of a hedonic model. For more on hedonic models, see page 358.
Believe it or not, there have been a number of econometric studies of trac-
tor prices. Most significantly, in 2008 Diekmann et al.9 studied used tractor 
prices utilizing a semilog left functional form and found that key indepen-
dent variables included make, horsepower, age, hours of use, sale date, drive 
(four-wheel drive or two-wheel drive), automatic transmission, and fuel 
(diesel or gas). This provides a useful starting point.
9. Florian Diekmann, Brian E. Roe, and Marvin T. Batte, “Tractors on eBay: Differences between 
Internet and In-Person Auctions.” American Journal of Agricultural Economics, Vol. 90, No. 2, pp. 
306–320. Also see Gregory Perry, Ahmet Bayaner, and Clair J. Nixon, “The Effect of Usage and Size 
on Tractor Depreciation,” American Journal of Agricultural Economics, Vol. 72, No. 2, pp. 317–325.


218
Chapter 7  Specification: Choosing a Functional Form 
Step 2: Estimate the Basic Model
As our basic model, let’s estimate a variation of Diekmann’s model using a 
more current dataset. Table 7.3 contains the definitions of the variables we’ll 
need to attempt to replicate Diekmann’s regression. The dependent variable 
is the price of a used farm tractor that was sold at auction in the United States 
between June 1, 2011 and May 31, 2012. The data10 are available on this text’s 
website as dataset TRACTOR7. Table 7.3 also has the hypothesized expected 
sign of the coefficient of each variable, given the underlying theory. Now:
10. The data were collected by Preston Cahill of Centre College.
Table 7.3  Variable Definitions for the Used Tractor Price Model
Variable
Description
Hypoth. Sign of Coef.
Yi = salepricei
The price paid for tractor i in dollars
n/a
Tractor Specifications:
horsepoweri
The horsepower of tractor i
+
agei
The number of years since tractor i was 
manufactured
-
enghoursi
The number of hours of use recorded 
on tractor i
-
dieseli
A dummy variable = 1 if tractor i runs 
on diesel fuel, 0 otherwise
+
fwdi
A dummy variable = 1 if tractor i has 
four-wheel drive, 0 otherwise
+
manuali
A dummy variable = 1 if tractor i trans-
mission is manual, 0 otherwise
-
johndeerei
A dummy variable = 1 if tractor i is man-
ufactured by John Deere, 0 otherwise
+
cabi
A dummy variable = 1 if tractor i has an 
enclosed cab, 0 otherwise
+
Time of year:
springi
A dummy variable = 1 if tractor i was 
sold in April or May, 0 otherwise
?
summeri
A dummy variable = 1 if tractor i was 
sold June–September, 0 otherwise
?
winteri
A dummy variable = 1 if tractor i was 
sold December–March, 0 otherwise
?


219
  Appendix: Econometric Lab #4
a.	 Estimate an equation with the natural log of the sale price (salepricei) 
as the dependent variable and all the other variables in Table 7.3 as 
the independent variables. (Hints: Don’t forget to generate lnsaleprice 
before you run your regression, and make sure not to include any vari-
ables that are not listed in Table 7.3.)
b.	 Take a look at your regression results. What is R2? Does this seem rea-
sonable? Explain your thinking.
c.	 Do any of your estimated coefficients have unexpected signs? If so, 
which ones?
d.	 Run one-sided 5-percent t-tests on the coefficients of all your indepen-
dent variables except for the seasonal dummies. For which coefficients 
can you reject the null hypothesis?
e.	 Carefully interpret the coefficient of johndeere. What does it mean in 
real-world terms?
f.	 What econometric problems (if any) appear to exist in the basic model?
Step 3: Consider a Polynomial Functional Form for Horsepower
Suppose you show the results of your basic model to a used tractor dealer 
who happened to take econometrics in college. He says that your results are 
promising, but he’s found it very difficult to sell overpowered used tractors 
because these tractors waste fuel and provide no extra benefit to the buyer. He 
thinks that new tractor buyers often overestimate how much power they’ll need 
and that used tractor buyers don’t make this mistake as often. He therefore 
suggests that it could be that as horsepower increases, the price increases, at 
least up to a point, but beyond that point, further increases in horsepower start 
to have a negative effect on price. You decide to take his advice and consider 
changing the functional form of horsepower to a polynomial.
a.	 Generate the new variable and run the new regression. (Hint: Did you 
remember to hypothesize the signs of the coefficients of horsepower 
and its square before you ran the regression?)
b.	 Run 5-percent one-sided t-tests on your hypotheses for the coefficients 
of horsepower and its square.
c.	 At what horsepower (to the nearest round number) does the value of 
a tractor reach an extreme (other things being equal)? Is the extreme a 
minimum or a maximum?
d.	 Which equation do you prefer between the basic equation and the poly-
nomial equation? Why? (Be sure to cite evidence to support your choice.)


220
Chapter 7  Specification: Choosing a Functional Form 
Step 4: Add a Potential Omitted Variable to Your Step 3 Model
As you’re leaving the used tractor lot, you happen to notice that quite a few of 
the tractors have enclosed cabs. Since such a cab would come in handy in bad 
weather, you have a sudden sinking feeling that you might have an omitted 
variable! To test this, you find the data for cab (luckily also in TRACTOR7).
Now:
a.	 Add cab to the model you preferred in Step 3, part d, and re-estimate 
the equation.
b.	 Use our four specification criteria to decide whether cab belongs in the 
equation. (Hint: Write out specific answers for all four criteria and then 
justify your conclusion.)
Step 5: Joint Hypothesis Testing
Go back to the basic model of Step 2, and test at the 5-percent level the 
joint hypothesis that the time of year of the sale has no effect on the price of 
tractors:
a.	 What is the omitted condition in this seasonal model? What’s unusual 
about this?
b.	 Carefully write out your null and alternative hypotheses.
c.	 Estimate your constrained equation.
d.	 Run the appropriate F-test at the 5-percent level. Calculate F and look 
up the appropriate critical F-value.
e.	 What’s your conclusion? Do used tractor prices have a seasonal 
pattern?
(Optional) Step 6: Consider a Slope Dummy That Interacts Diesel 
with Use
It is well known that diesel engines tend to be more durable than gasoline 
engines. That fact raises the question of whether an additional hour of use 
affects the value of a diesel tractor differently than for a gasoline tractor. 
Generate the variable you need to test this hypothesis, add this variable to 
the basic model of Step 2, estimate the revised slope dummy model, and test 
the appropriate slope dummy hypothesis at the 5-percent level. What is your 
t-value? Can you reject the null hypothesis?
