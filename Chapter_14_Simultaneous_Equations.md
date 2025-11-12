# Chapter 14: Simultaneous Equations

**Pages:** 431-462

---

411
Chapter 14
Simultaneous Equations
14.1  Structural and Reduced-Form Equations
14.2  The Bias of Ordinary Least Squares
14.3  Two-Stage Least Squares (2SLS)
14.4  The Identification Problem
14.5  Summary and Exercises
14.6  Appendix: Errors in the Variables
The most important models in economics and business are simultaneous 
in nature. Supply and demand, for example, is obviously simultaneous. To 
study the demand for chicken without also looking at the supply of chicken 
is to take a chance on missing important linkages and thus making signifi-
cant mistakes. Virtually all the major approaches to macroeconomics, from 
Keynesian aggregate demand models to rational expectations schemes, are 
inherently simultaneous. Even models that appear to be inherently single-
equation in nature often turn out to be much more simultaneous than you 
might think. The price of housing, for instance, is dramatically affected by the 
level of economic activity, the prevailing rate of interest in alternative assets, 
and a number of other simultaneously determined variables.
All this wouldn’t mean much to econometricians if it weren’t for the fact 
that the estimation of simultaneous equations systems with OLS causes a 
number of difficulties that aren’t encountered with single equations. Most 
important, Classical Assumption III, which states that all explanatory vari-
ables should be uncorrelated with the error term, is violated in simultane-
ous models. Mainly because of this, OLS coefficient estimates are biased in 
simultaneous models. As a result, an alternative estimation procedure called 
Two-Stage Least Squares usually is employed in such models instead of OLS.
You’re probably wondering why we’ve waited until now to discuss simulta-
neous equations if they’re so important in economics and if OLS encounters 
bias when estimating them. The answer is that the simultaneous estimation 


412
Chapter 14  Simultaneous Equations
of an equation changes every time the specification of any equation in the 
entire system is changed, so a researcher must be well equipped to deal with 
specification problems like those of previous chapters. As a result, it does not 
make sense to learn how to estimate a simultaneous system until you are 
fairly adept at estimating a single equation.
14.1   Structural and Reduced-Form Equations
Before we can study the problems encountered in the estimation of simulta-
neous equations, we need to introduce a few concepts.
The Nature of Simultaneous Equations Systems
Which came first, the chicken or the egg? This question is impossible to 
answer satisfactorily because chickens and eggs are jointly determined; there 
is a two-way causal relationship between the variables. The more eggs you 
have, the more chickens you’ll get, but the more chickens you have, the more 
eggs you’ll get.1 More realistically, the economic world is full of the kind of 
feedback effects and dual causality that require the application of simultane-
ous equations. Besides the supply and demand and simple macroeconomic 
model examples mentioned previously, we could talk about the dual causality 
of population size and food supply, the joint determination of wages and 
prices, or the interaction between foreign exchange rates and international 
trade and capital flows. In a typical econometric equation:
	
Yt = β0 + β1X1t + β2X2t + et	
(14.1)
a simultaneous system is one in which Y clearly has an effect on at least one 
of the Xs in addition to the effect that the Xs have on Y.
Such topics are usually modeled by distinguishing between variables that 
are simultaneously determined (the Ys, called endogenous variables) and 
those that are not (the Xs, called exogenous variables):
	
Y1t = α0 + α1Y2t + α2X1t + α3X2t + e1t	
(14.2)
	
Y2t = β0 + β1Y1t + β2X3t + β3X2t + e2t	
(14.3)
1. This also depends on how hungry you are, which is a function of how hard you’re working, 
which depends on how many chickens you have to take care of. (Although this chicken/egg 
example is simultaneous in an annual model, it would not be truly simultaneous in a quarterly 
or monthly model because of the time lags involved.)


413
  Structural and Reduced-Form Equations
For example, Y1 and Y2 might be the quantity and price of chicken (respec-
tively), X1 the income of the consumers, X2 the price of beef (beef is a substi-
tute for chicken in both consumption and production), and X3 the price of 
chicken feed. With these definitions, Equation 14.2 would characterize the 
behavior of consumers of chickens and Equation 14.3 the behavior of suppli-
ers of chickens. These behavioral equations are also called structural equations. 
Structural equations characterize the underlying economic theory behind 
each endogenous variable by expressing it in terms of both endogenous and 
exogenous variables. Researchers must view them as an entire system in order 
to see all the feedback loops involved. For example, the Ys are jointly deter-
mined, so a change in Y1 will cause a change in Y2, which will in turn cause 
Y1 to change again. Contrast this feedback with a change in X1, which will 
not eventually loop back and cause X1 to change again. The αs and the βs in 
the equation are structural coefficients, and hypotheses should be made about 
their signs just as we did with the regression coefficients of single equations.
Note that a variable is endogenous because it is jointly determined, not 
just because it appears in both equations. That is, X2, which is the price of 
beef but could be another factor beyond our control, is in both equations 
but is still exogenous in nature because it is not simultaneously determined 
within the chicken market. In a large general equilibrium model of the entire 
economy, however, such a price variable would also likely be endogenous. 
How do you decide whether a particular variable should be endogenous or 
exogenous? Some variables are almost always exogenous (the weather, for 
example), but most others can be considered either endogenous or exogenous, 
depending on the number and characteristics of the other equations in the 
system. Thus, the distinction between endogenous and exogenous variables 
usually depends on how the researcher defines the scope of the research 
project.
Sometimes, lagged endogenous variables appear in simultaneous systems, 
usually when the equations involved are dynamic models (described in 
Chapter 12). Be careful! Such lagged endogenous variables are not simulta-
neously determined in the current time period. They thus have more in com-
mon with exogenous variables than with nonlagged endogenous variables. 
To avoid problems, we’ll define the term predetermined variable to include 
all exogenous variables and lagged endogenous variables. “Predetermined” 
implies that exogenous and lagged endogenous variables are determined out-
side the system of specified equations or prior to the current period. Endog-
enous variables that are not lagged are not predetermined, because they 
are jointly determined by the system in the current time period. Therefore, 
econometricians tend to speak in terms of endogenous and predetermined 
variables when discussing simultaneous equations systems.


414
Chapter 14  Simultaneous Equations
Let’s look at the specification of a simple supply and demand model, say 
for the “cola” soft-drink industry:
	
QDt = α0 + α1Pt + α2X1t + α3X2t + eDt	
(14.4)
	
QSt  = β0 + β1Pt + β2X3t + eSt
	
(14.5)
	
QSt  = QDt (equilibrium condition)	
where:	
QDt = the quantity of cola demanded in time period t
	
QSt  = the quantity of cola supplied in time period t
	
Pt
 = the price of cola in time period t
	
X1t  = dollars of advertising for cola in time period t
	
X2t  = another “demand-side” exogenous variable (e.g., income 
or the prices or advertising of other drinks)
	
X3t  = a “supply-side” exogenous variable (e.g., the price of artifi-
cial flavors or other factors of production)
	
et
 = classical error terms (each equation has its own error term, 
subscripted “D” and “S” for demand and supply)
In this case, price and quantity are simultaneously determined, but price, 
one of the endogenous variables, is not on the left side of any of the equa-
tions. It’s incorrect to assume automatically that the endogenous variables 
are those that appear on the left side of at least one equation; in this case, 
we could have just as easily written Equation 14.5 with price on the left side 
and quantity supplied on the right side, as we did in the chicken example in 
Equations 14.2 and 14.3. Although the estimated coefficients would be dif-
ferent, the underlying relations would not. Note also that there must be as 
many equations as there are endogenous variables. In this case, the three 
endogenous variables are QD, QS, and P.
What would be the expected signs for the coefficients of the price variables 
in Equations 14.4 and 14.5? We’d expect price to enter negatively in the 
demand equation but to enter positively in the supply equation. The higher 
the price, after all, the less quantity will be demanded, but the more quantity 
will be supplied. These signs would result in the typical supply and demand 
diagram that we’re all used to. Look at Equations 14.4 and 14.5 again, and 
note that they would be identical except for the different predetermined 
variables. What would happen if we accidentally put a supply-side prede-
termined variable in the demand equation or vice versa? We’d have a very 
difficult time identifying which equation was which, and the expected signs 
for the coefficients of the endogenous variable P would become ambiguous. 
As a result, we must take care when specifying the structural equations in a 
system.


415
  Structural and Reduced-Form Equations
Simultaneous Systems Violate Classical Assumption III
Recall from Chapter 4 that Classical Assumption III states that the error term 
and each explanatory variable must be uncorrelated with each other. If there 
is such a correlation, then the OLS regression estimation program is likely to 
attribute to the explanatory variable variations in the dependent variable that 
are actually being caused by variations in the error term. The result will be 
biased estimates.
To see why simultaneous equations violate the assumption of independence 
between the error term and the explanatory variables, look again at a simul-
taneous system, Equations 14.2 and 14.3 (repeated with directional errors):
	
c	
c	
c
	
Y1t = α0 + α1Y2t + α2X1t + α3X2t + e1t	
(14.2)
	
c	
c
	
Y2t = β0 + β1Y1t + β2X3t + β3X2t + e2t	
(14.3)
Let’s work through the system and see what happens when one of the error 
terms increases, holding everything else in the equations constant:
1.	 If e1 increases in a particular time period, Y1 will also increase due to 
Equation 14.2.
2.	 If Y1 increases, Y2 will also rise2 due to Equation 14.3.
3.	 But if Y2 increases in Equation 14.3, it also increases in Equation 14.2 
where it is an explanatory variable.
Thus, an increase in the error term of an equation causes an increase in an 
explanatory variable in the same equation: If e1 increases, Y1 increases, and 
then Y2 increases, violating the assumption of independence between the 
error term and the explanatory variables.
For a visual understanding of this, take a look at Figure 14.1 on page 416. 
If the error term in the demand equation increases, then the demand curve 
will shift from D to D′, and both price and quantity will increase. Thus an 
increase in the error term will be correlated with an increase in an indepen-
dent variable. We’ve violated Classical Assumption III!
2. This assumes that β1 is positive. If β1 is negative, Y2 will decrease and there will be a negative 
correlation between e1 and Y2, but this negative correlation will still violate Classical Assump-
tion III. Also note that both Equations 14.2 and 14.3 could have Y1t on the left side; if two 
variables are jointly determined, it doesn’t matter which variable is considered dependent and 
which explanatory, because they are actually mutually dependent. We used this kind of simulta-
neous system in the cola model portrayed in Equations 14.4 and 14.5.


416
Chapter 14  Simultaneous Equations
This is not an isolated result that depends on the particular equations 
involved. Instead, this result works for other error terms, equations, and 
simultaneous systems. All that is required for the violation of Classical 
Assumption III is that there be endogenous variables that are jointly deter-
mined in a system of simultaneous equations.
Reduced-Form Equations
An alternative way of expressing a simultaneous equations system is through 
the use of reduced-form equations, equations that express a particular 
endogenous variable solely in terms of an error term and all the predetermined 
(exogenous plus lagged endogenous) variables in the simultaneous system.
The reduced-form equations for the structural Equations 14.2 and 14.3 
would thus be:
	
Y1t = π0 + π1X1t + π2X2t + π3X3t + v1t	
(14.6)
	
Y2t = π4 + π5X1t + π6X2t + π7X3t + v2t	
(14.7)
0
Q
QD 5 QS
S 5 Equation 14.5
b1 . 0
D 5 Equation 14.4
a1 , 0
P
Pe
P9
D9
Q9
Figure 14.1  Supply and Demand Simultaneous Equations
An example of simultaneous equations that jointly determine two endogenous variables 
is the supply and demand for a product. In this case, Equation 14.4, the downward-
sloping demand function, and Equation 14.5, the upward-sloping supply function, 
intersect at the equilibrium price and quantity for this market.


417
  Structural and Reduced-Form Equations
where the vs are stochastic error terms and the πs are called reduced-form 
coefficients because they are the coefficients of the predetermined variables in 
the reduced-form equations. Where do these reduced-form equations come 
from? If you substitute Equation 14.3 into Equation 14.2, solve for Y1, and 
then regroup terms, you’ll get Equation 14.6.
Note that each reduced-form equation includes only one endogenous 
variable (the dependent variable) and that each equation has exactly the 
same set of predetermined variables. The reduced-form coefficients, such 
as π1 and π5, are known as impact multipliers because they measure the 
impact on the endogenous variable of a one-unit increase in the value of 
the predetermined variable, after allowing for the feedback effects from the 
entire simultaneous system.
There are at least three reasons for using reduced-form equations:
1.	 Since the reduced-form equations have no inherent simultaneity, they 
do not violate Classical Assumption III. Therefore, they can be esti-
mated with OLS without encountering the problems discussed in this 
chapter.
2.	 The interpretation of the reduced-form coefficients as impact multipli-
ers means that they have economic meaning and useful applications of 
their own. For example, if you wanted to compare a government spend-
ing increase with a tax cut in terms of the per-dollar impact in the first 
year, estimates of the impact multipliers (reduced-form coefficients or 
πs) would allow such a comparison.
3.	 Perhaps most importantly, reduced-form equations play a crucial role 
in the estimation technique most frequently used for simultaneous 
equations. This technique, Two-Stage Least Squares, will be explained 
in Section 14.3.
To conclude, let’s return to the cola supply and demand model and specify 
the reduced-form equations for that model. (To test yourself, flip back to 
Equations 14.4 and 14.5 and see if you can get the right answer before going 
on.) Since the equilibrium condition forces QD to be equal to QS, we need 
only two reduced-form equations:
	
Qt = π0 + π1X1t + π2X2t + π3X3t + v1t	
(14.8)
	
Pt = π4 + π5X1t + π6X2t + π7X3t + v2t	
(14.9)
Even though P never appears on the left side of a structural equation, it’s an 
endogenous variable and should be treated as such.


418
Chapter 14  Simultaneous Equations
14.2   The Bias of Ordinary Least Squares
The first six Classical Assumptions must be met for OLS estimates to be BLUE; 
when an assumption is violated, we must determine which of the proper-
ties no longer holds. It turns out that applying OLS directly to the structural 
equations of a simultaneous system produces biased and inconsistent esti-
mates of the coefficients. Such bias is called simultaneous equations bias or 
simultaneity bias.
Understanding Simultaneity Bias
Simultaneity bias refers to the fact that in a simultaneous system, the 
expected values of the OLS-estimated structural coefficients 1βN s2 are not 
equal to the true βs. We are therefore faced with the problem that in a simul-
taneous system:
	
E1βN 2 ≠β	
(14.10)
Why does this simultaneity bias exist? Recall from Section 14.1 that in simul-
taneous equations systems, the error terms (the es) tend to be correlated with 
the endogenous variables (the Ys) whenever the Ys appear as explanatory 
variables. Let’s follow through what this correlation means (assuming 
positive coefficients for simplicity) in typical structural equations like 14.11 
and 14.12:
	
Y1t = β0 + β1Y2t + β2Xt + e1t	
(14.11)
	
Y2t = α0 + α1Y1t + α2Zt + e2t	
(14.12)
Since we cannot observe the error term 1e12 and don’t know when e1t is 
above average, it will appear as if every time Y1 is above average, Y2 is also 
above average (as long as α1 is positive). As a result, the OLS estimation pro-
gram will tend to attribute increases in Y1 caused by the error term e1 to Y2, 
thus typically overestimating β1. This overestimation is simultaneity bias. If 
the error term is abnormally negative, Y1t will be less than it would have been 
otherwise, causing Y2t to be less than it would have been otherwise, and the 
computer program will attribute the decrease in Y1 to Y2, once again causing 
us to overestimate β1 (that is, induce upward bias).
Recall that the causation between Y1 and Y2 runs in both directions 
because the two variables are interdependent. As a result, β1, when estimated 
by OLS, can no longer be interpreted as the impact of Y2 on Y1, holding X 
constant. Instead, βN 1 now measures some mix of the effects of the two endog-
enous variables on each other! In addition, consider β2. It’s supposed to be 


419
  The Bias of Ordinary Least Squares
the effect of X on Y1 holding Y2 constant, but how can we expect Y2 to be held 
constant when a change in Y1 takes place? As a result, there is potential bias 
in all the estimated coefficients in a simultaneous system.
What does this bias look like? It’s possible to derive an equation for the 
expected value of the regression coefficients in a simultaneous system that 
is estimated by OLS. This equation shows that as long as the error term and 
any of the explanatory variables in the equation are correlated, then the coef-
ficient estimates will be biased and inconsistent. In addition, it also shows 
that the bias will have the same sign as the correlation between the error term 
and the endogenous variable that appears as an explanatory variable in that 
error term’s equation. Since that correlation is often positive in economic 
and business examples, the bias often will be positive, although the direction 
of the bias in any given situation will depend on the specific details of the 
structural equations and the model’s underlying theory.
This does not mean that every coefficient from a simultaneous system 
estimated with OLS will be a bad approximation of the true population 
coefficient. However, it’s vital to consider an alternative to OLS whenever 
simultaneous equations systems are being estimated. Before we investigate 
the alternative estimation technique most frequently used (Two-Stage Least 
Squares), let’s look at an example of simultaneity bias.
An Example of Simultaneity Bias
To show how the application of OLS to simultaneous equations estimation 
causes bias, we used a Monte Carlo experiment3 to generate an example of 
such biased estimates. Since it’s impossible to know whether any bias exists 
unless you also know the true βs, we arbitrarily picked a set of coefficients 
to be considered “true.” We then stochastically generated data sets based on 
these “true” coefficients, and obtained repeated OLS estimates of these coef-
ficients from the generated data sets. The expected value of these estimates 
turned out to be quite different from the true coefficient values, thus exem-
plifying the bias in OLS estimates of coefficients in simultaneous systems.
3. Monte Carlo experiments are computer-generated simulations that typically follow seven 
steps: 1. Assume a “true” model with specific coefficient values and an error term distribution. 
2. Select values for the independent variables. 3. Select an estimating technique (usually OLS). 
4. Create various samples of the dependent variable, using the assumed model, by randomly 
generating error terms from the assumed distribution; often, the number of samples created 
runs into the thousands. 5. Compute the estimates of the βs from the various samples using the 
estimating technique. 6. Summarize and evaluate the results. 7. Consider sensitivity analyses 
using different values, distributions, or estimating techniques.


420
Chapter 14  Simultaneous Equations
We used a supply and demand model as the basis for our example:
	
Qt = β0 + β1Pt + β2Xt + eDt	
(14.13)
	
Qt = α0 + α1Pt + α2Zt + eSt	
(14.14)
where:	
Qt = the quantity demanded and supplied in time period t
	
Pt  = the price in time period t
	
Xt = a “demand-side” exogenous variable, such as income
	
Zt  = a “supply-side” exogenous variable, such as weather
	
et  = classical error terms (different for each equation)
The first step was to choose a set of true coefficient values that corre-
sponded to our expectations for this model:
β1 = -1    β2 = +1    α1 = +1    α2 = +1
In other words, we have a negative relationship between price and quantity 
demanded, a positive relationship between price and quantity supplied, and 
positive relationships between the exogenous variables and their respective 
dependent variables.
The next step was to randomly generate a number of data sets based on the 
true values. This also meant specifying some other characteristics of the data4 
before generating the different data sets (5,000 in this case).
The final step was to apply OLS to the generated data sets and to calculate 
the estimated coefficients of the demand equation (14.13). (Similar results 
were obtained for the supply equation.) The arithmetic means of the results 
for the 5,000 regressions were:
	
QN Dt = βN 0 - 0.37Pt + 1.84Xt	
(14.15)
In other words, the expected value of βN 1 should have been -1.00, but instead 
it was roughly -0.37; the expected value of βN 2 should have been +1.00, but 
instead it was around 1.84:
E1βN 12 ≈-0.37 ≠-1.00
E1βN 22 ≈1.84 ≠1.00
This is simultaneity bias! As the diagram of the sampling distributions of the βN s 
in Figure 14.2 shows, the OLS estimates of β1 were almost never very close to 
-1.00, and the OLS estimates of β2 were distributed over a wide range of values.
4. Other assumptions included a normal distribution for the error term, β0 = 0, α0 = 0, 
σ2
S = 3, σ2
D = 2, r2
xz = 0.4, and N = 20. In addition, we assumed that the error terms of the 
two equations were not correlated.


421
  Two-Stage Least Squares (2SLS)
23
22
21
True
b1
True
b2
E(b2) < 1.84
E(b1) < 2 0.37
Sampling Distribution
of b2
0
1
2
3
Sampling Distribution
of b1
N
N
N
N
14.3   Two-Stage Least Squares (2SLS)
How can we get rid of (or at least reduce) simultaneity bias? There are a num-
ber of estimation techniques that help mitigate simultaneity bias, but the most 
frequently used alternative to OLS is called Two-Stage Least Squares (2SLS).
Since OLS encounters bias in the estimation of simultaneous equations 
mainly because such equations violate Classical Assumption III, one solution 
to the problem is to try to avoid violating that assumption. The first step in 
doing this is to find a variable that is:
1.	 highly correlated with the endogenous variable, and
2.	 uncorrelated with the error term.
Such a variable is called an instrumental variable; it is highly correlated 
with the endogenous variable, but is uncorrelated with the error term. More 
generally, instrumental variables (IV) regression is a method of avoiding the 
Figure 14.2  Sampling Distributions Showing Simultaneity Bias  
of OLS Estimates
In the experiment in Section 14.2, simultaneity bias is evident in the distribution of the 
estimates of β1, which had a mean value of -0.37 compared with a true value of -1.00,  
and in the estimates of β2, which had a mean value of 1.84 compared with a true value 
of 1.00.


422
Chapter 14  Simultaneous Equations
violation of Classical Assumption III by producing predicted values of endog-
enous variables that can be substituted for the endogenous variables where 
they appear on the right-hand side of structural equations. These predicted 
values typically are produced by running an OLS equation to explain the 
endogenous variable as a function of one or more instrumental variables.
To see how this works, take a look at Equation 14.16 in the following 
system:
	
Y1t = β0 + β1Y2t + β2X1t + e1t	
(14.16)
	
Y2t = α0 + α1Y1t + α2X2t + e2t	
(14.17)
If we could find a variable (or variables) highly correlated with Y2t but uncor-
related with e1t, then we could produce a predicted value of Y2t by running 
an OLS regression with Y2t as a function of the instrumental variable(s). 
The fitted value YN2t will be uncorrelated with e1t (because it was produced 
using variables that are uncorrelated with e1t), so if we substitute YN2t for Y2t 
on the right side of Equation 14.16, then we’ll no longer violate Classical 
Assumption III.
This approach avoids the violation of Classical Assumption III, but it 
doesn’t give us any insight into where to find appropriate instrumental 
variables (sometimes called instruments). How do we systematically find 
variables that are highly correlated with the endogenous variable but uncor-
related with the error term? For simultaneous equations systems, there’s a 
straightforward answer. We use Two-Stage Least Squares.
What Is Two-Stage Least Squares?
Two-Stage Least Squares (2SLS) is a method of avoiding simultaneity bias 
by systematically creating variables to replace the endogenous variables where 
they appear as explanatory variables in simultaneous equations systems. The 
simplest form of 2SLS does this by running an OLS regression on the reduced 
form of every right-side endogenous variable and then using the YN  (or fitted 
value) from the reduced-form estimated equation in place of the endogenous 
variable where it appears on the right side of a structural equation.
Why does 2SLS do this? Every predetermined variable in the simultane-
ous system is a candidate to be an instrumental variable for every endog-
enous variable, but if we choose only one instrumental variable, then we’ll 
be throwing away information. To avoid this, 2SLS uses a linear combina-
tion of all the predetermined variables. We form this linear combination 
by running a regression for a given endogenous variable as a function of 
all the predetermined variables in the reduced-form equation to generate a 


423
  Two-Stage Least Squares (2SLS)
predicted value of the endogenous variable. Thus the 2SLS two-step estima-
tion procedure is:
STAGE ONE: Run OLS on the reduced-form equations for each of the endog-
enous variables that appear as explanatory variables in the structural equations 
in the system.
Since the predetermined (exogenous plus lagged endogenous) variables 
are uncorrelated with the reduced-form error term, the OLS estimates of the 
reduced-form coefficients (the πN s) are unbiased. These πN s can then be used 
to calculate estimates of the endogenous variables:
	
YN1t = πN 0 + πN 1X1t + πN 2X2t	
(14.18)
	
YN2t = πN 3 + πN 4X1t + πN 5X2t	
(14.19)
These YNs then are used in place of the Ys on the right-hand side of the struc-
tural equations.
STAGE TWO: Substitute the reduced form YNs for the Ys that appear on the 
right side (only) of the structural equations, and then estimate these revised 
structural equations.
That is, stage two consists of estimating the following equations with OLS:
	
Y1t = β0 + β1YN2t + β2X1t + u1t	
(14.20)
	
Y2t = α0 + α1YN1t + α2X2t + u2t	
(14.21)
Note that the dependent variables are still the original endogenous variables 
and that the substitutions are only for the endogenous variables where they 
appear on the right-hand side of the structural equations. This procedure 
produces consistent estimates of the coefficients of the structural equations.
Be careful! If second-stage equations such as Equations 14.20 and 14.21 
are estimated with OLS, the SE1βN 2s will be incorrect, so be sure to use your 
computer’s 2SLS estimation procedure.
This description of 2SLS can be generalized to any number of simultane-
ous structural equations. Each reduced-form equation has as explanatory 
variables every predetermined variable in the entire system of equations. 
The OLS estimates of the reduced-form equations are used to compute the 


424
Chapter 14  Simultaneous Equations
estimated values of all the endogenous variables that appear as explanatory 
variables in the structural equations. After substituting these fitted values for 
the original values of the endogenous independent variables, OLS is applied 
to each stochastic equation in the set of structural equations.
The Properties of Two-Stage Least Squares
1.	 2SLS estimates still are biased. The expected value of a βN  produced by 
2SLS is not equal to the true β, but the expected bias due to 2SLS usu-
ally is smaller than the expected bias due to OLS. One cause of the 2SLS 
bias is any remaining correlation between the YNs produced by the first-
stage reduced-form regressions and the es. As the sample size gets larger, 
the 2SLS bias falls, but it is always non-zero in a finite sample.
	
  To illustrate these properties,5 let’s return to the Monte Carlo example 
of Section 14.2. If we estimate the equation with 2SLS, we get a mean βN 1 
of roughly -1.25. This isn’t equal to the true β1 of -1.00, but it’s much 
closer than the OLS mean βN 1 of around -0.37. If we then expand the 
number of observations in each sample from 20 to 50 and re-estimate 
the equation with 2SLS for the 5,000 samples, the mean of the sam-
pling distribution of βN 1 moves to -1.06, which is even closer to the true 
value of -1.00.
2.	 If the fit of the reduced-form equation is poor, then 2SLS will not rid the 
equation of bias. Recall that an instrumental variable is supposed to be 
highly correlated with the endogenous variable. To the extent that the 
fit of the reduced-form equation is poor,6 then the instrumental vari-
ables aren’t highly correlated with the original endogenous variable, 
and there is no reason to expect 2SLS to be effective. As the fit of the 
reduced-form equation increases, the usefulness of 2SLS will increase.
3.	 2SLS estimates have increased variances and SE(βN )s. While 2SLS does an 
excellent job of reducing the amount of bias in the βN s, there’s a price to pay 
for this reduced bias. This price is that 2SLS estimates tend to have higher 
variances and SE(βN )s than do OLS estimates of the same equations.
5. Under certain circumstances, for example, if only one instrument is used to produce the 
predicted values of the endogenous variable, then the population mean of the instrumental 
variable estimator is undefined, and the bias is not defined.
6. See J. Stock and M. Yogo, “Testing for Weak Instruments in Linear IV Regression,” in D.W.K. 
Andrews, Identification and Inference for Econometric Models (New York: Cambridge University 
Press, 2005), pp. 80–108. They develop a test of the fit of the reduced-form equation that is a 
version of the F–test, not R2. A rough rule of thumb is that F should be greater than 10.


425
  Two-Stage Least Squares (2SLS)
On balance, then, 2SLS will almost always be a better estimator of the 
coefficients of a simultaneous system than OLS will be. The major exception 
to this general rule is when the fit of the reduced-form equation in question 
is poor.
An Example of Two-Stage Least Squares
Let’s work through an example of 2SLS, a naive linear Keynesian macroeco-
nomic model of the U.S. economy. We’ll specify the following system:
	
 Yt = COt + It + Gt + NXt
	
(14.22)
	
 COt = β0 + β1YDt + β2COt-1 + e1t	
(14.23)
	
 YDt = Yt - Tt
	
(14.24)
	
 It = β3 + β4Yt + β5rt-1 + e2t
	
(14.25)
where:	
Yt
 = Gross Domestic Product (GDP) in year t
	
COt = total personal consumption in year t
	
It
 = total gross private domestic investment in year t
	
Gt  = government purchases of goods and services in year t
	
NXt = net exports of goods and services (exports minus imports) 
in year t
	
Tt
 = taxes (actually equal to taxes, depreciation, corporate prof-
its, government transfers, and other adjustments necessary 
to convert GDP to disposable income) in year t
	
rt
 = the interest rate in year t
	
YDt = disposable income in year t
All variables are in real terms (measured in billions of 2000 dollars) except 
the interest rate variable, which is measured in nominal percent. The data for 
this example are from 1976 through 2007 and are presented in Table 14.1.
Equations 14.22 through 14.25 are the structural equations of the system, 
but only Equations 14.23 and 14.25 are stochastic (behavioral) and need to 
be estimated. The other two are not stochastic, as can be determined by the 
lack of an error term in the equations.
Stop for a second and look at the system. Which variables are endogenous? 
Which are predetermined? The endogenous variables are those that are jointly 
determined by the system, namely, Yt, COt, YDt, and It. To see why these four 
variables are simultaneously determined, note that if you change one of them 
and follow this change through the system, the change will get back to the 
original causal variable. For instance, if It goes up for some reason, that will 
cause Yt to go up (through Equation 14.22), which will feed right back into It 
again (through Equation 14.25). They’re simultaneously determined.


426
Chapter 14  Simultaneous Equations
Table 14.1  Data for the Small Macromodel
YEAR
Y
CO
I
G
YD
r
1975
NA
2876.9
NA
NA
NA
  8.83
1976
  4540.9
3035.5
  544.7
1031.9
3432.2
  8.43
1977
  4750.5
3164.1
  627.0
1043.3
3552.9
  8.02
1978
  5015.0
3303.1
  702.6
1074.0
3718.8
  8.73
1979
  5173.4
3383.4
  725.0
1094.1
3811.2
  9.63
1980
  5161.7
3374.1
  645.3
1115.4
3857.7
11.94
1981
  5291.7
3422.2
  704.9
1125.6
3960.0
14.17
1982
  5189.3
3470.3
  606.0
1145.4
4044.9
13.79
1983
  5423.8
3668.6
  662.5
1187.3
4177.7
12.04
1984
  5813.6
3863.3
  857.7
1227.0
4494.1
12.71
1985
  6053.7
4064.0
  849.7
1312.5
4645.2
11.37
1986
  6263.6
4228.9
  843.9
1392.5
4791.0
  9.02
1987
  6475.1
4369.8
  870.0
1426.7
4874.5
  9.38
1988
  6742.7
4546.9
  890.5
1445.1
5082.6
  9.71
1989
  6981.4
4675.0
  926.2
1482.5
5224.8
  9.26
1990
  7112.5
4770.3
  895.1
1530.0
5324.2
  9.32
1991
  7100.5
4778.4
  822.2
1547.2
5351.7
  8.77
1992
  7336.6
4934.8
  889.0
1555.3
5536.3
  8.14
1993
  7532.7
5099.8
  968.3
1541.1
5594.2
  7.22
1994
  7835.5
5290.7
1099.6
1541.3
5746.4
  7.96
1995
  8031.7
5433.5
1134.0
1549.7
5905.7
  7.59
1996
  8328.9
5619.4
1234.3
1564.9
6080.9
  7.37
1997
  8703.5
5831.8
1387.7
1594.0
6295.8
  7.26
1998
  9066.9
6125.8
1524.1
1624.4
6663.9
  6.53
1999
  9470.3
6438.6
1642.6
1686.9
6861.3
  7.04
2000
  9817.0
6739.4
1735.5
1721.6
7194.0
  7.62
2001
  9890.7
6910.4
1598.4
1780.3
7333.3
  7.08
2002
10048.8
7099.3
1557.1
1858.8
7562.2
  6.49
2003
10301.0
7295.3
1613.1
1904.8
7729.9
  5.67
2004
10675.8
7561.4
1770.2
1931.8
8008.9
  5.63
2005
10989.5
7791.7
1873.5
1939.0
8121.4
  5.24
2006
11294.8
8029.0
1912.5
1971.2
8407.0
  5.59
2007
11523.9
8252.8
1809.7
2012.1
8644.0
  5.56
Source: The Economic Report of the President, 2009. Note that T and NX can be calculated 
using Equations 14.22 and 14.24.
Datafile = MACRO14


427
  Two-Stage Least Squares (2SLS)
What about interest rates? Is rt an endogenous variable? The surprising 
answer is that, strictly speaking, rt is not endogenous in this system because 
rt-1 (not rt) appears in the investment equation. Thus, there is no simultane-
ous feedback through the interest rate in this simple model.7
Given this answer, which are the predetermined variables? The predeter-
mined variables are Gt, NXt, Tt, COt-1, and rt-1. To sum, the simultaneous 
system has four structural equations, four endogenous variables, and five pre-
determined variables.
What is the economic content of the stochastic structural equations? The 
consumption function, Equation 14.23, is a dynamic model consumption 
function of the kind we analyzed in Chapter 12. We discussed this exact equa-
tion in Section 12.2, going so far as to estimate Equation 14.23 with OLS on 
data from Table 14.1, and the reader is encouraged to reread that analysis.
The investment function, Equation 14.25, includes simplified multiplier 
and cost of capital components. The multiplier term β4 measures the stimulus 
to investment that is generated by an increase in GDP. In a Keynesian model, 
β4 thus would be expected to be positive. On the other hand, the higher the 
cost of capital, the less investment we’d expect to be undertaken (holding 
multiplier effects constant), mainly because the expected rate of return on 
marginal capital investments is no longer sufficient to cover the higher cost of 
capital. Thus β5 is expected to be negative. It takes time to plan and start up 
investment projects, though, so the interest rate is lagged one year.8
Stage One: Even though there are four endogenous variables, only two of 
them appear on the right-hand side of stochastic equations, so only two 
reduced-form equations need to be estimated to apply 2SLS. These reduced-
form equations are estimated automatically by all 2SLS computer estimation 
programs, but it’s instructive to take a look at one anyway:
YDt = -258.55 + 0.78Gt - 0.37NXt + 0.52Tt + 0.67COt-1 + 37.63rt-1
10.222    10.162       10.142   10.092             19.142
t =   3.49    - 2.30           3.68       7.60                  4.12
	
(14.26)
8
7. Although this sentence is technically correct, it overstates the case. In particular, there are a 
couple of circumstances in which an econometrician might want to consider rt-1 to be part of 
the simultaneous system for theoretical reasons. For our naive Keynesian model with a lagged 
interest rate effect, however, the equation is not in the simultaneous system.
8. This investment equation is a simplified mix of the accelerator and the neoclassical theories 
of the investment function. The former emphasizes that changes in the level of output are the 
key determinant of investment, and the latter emphasizes that user cost of capital (the opportu-
nity cost that the firm incurs as a consequence of owning an asset) is the key.


428
Chapter 14  Simultaneous Equations
Note that we don’t test any hypotheses on reduced forms, nor do we con-
sider dropping a variable9 that is statistically and theoretically irrelevant. The 
whole purpose of stage one of 2SLS is not to generate meaningful reduced-
form estimated equations but rather to generate YNs to use as substitutes for 
endogenous variables in the second stage. To do that, we calculate the YNts and 
YDts for all 32 observations by plugging the actual values of all 5 predeter-
mined variables into estimated reduced-form equations like Equation 14.26.
Stage Two: We then substitute these YNts and YDts for the endogenous 
variables where they appear on the right sides of Equations 14.23 and 14.25. 
For example, the YDt from Equation 14.26 would be substituted into 
Equation 14.23, resulting in:
	
COt = β0 + β1YDt + β2COt-1 + e1t	
(14.27)
If we estimate Equation 14.27 and the other second-stage equation given the 
data in Table 14.1, we obtain the following 2SLS10 results:
	
COt = -  209.06 + 0.37YDt + 0.66COt-1	
(14.28)
10.132      10.142
2.73           4.84
N = 32    R2 = .999    DW = 0.83
	
INt = -  261.48 + 0.19YNt - 9.55rt-1	
(14.29)
10.012 111.202
15.82   - 0.85
N = 32    R2 = .956    DW = 0.47
8
8
8
8
8
8
9. Our recommendation to use every predetermined variable in the simultaneous system as an 
instrumental variable in the first stage of 2SLS is a simplification that we think is appropriate 
given the level of this text. Experienced econometricians will test each potential instrumental 
variable to measure the extent to which the variable is highly correlated with the endogenous 
variable and uncorrelated with the error term. Only those variables that meet these criteria 
should then be used as valid instruments in the first stage. For an approachable discussion of 
the topic of checking instrument validity, see James Stock and Mark Watson, Introduction to 
Econometrics (Boston: Pearson, 2015), pp. 442–448.
10. The 2SLS estimates in Equations 14.28 and 14.29 are correct, but if you were to estimate 
those equations with OLS (using YNs and YDs generated as in Equation 14.26) you would 
obtain the same coefficient estimates but a different set of estimates of the standard errors 
(and t-scores). This difference comes about because running OLS on the second stage alone 
ignores the fact that the first stage was run at all. To get accurate estimated standard errors and 
t-scores, the estimation should be done with a 2SLS program.
8


429
  Two-Stage Least Squares (2SLS)
If we had estimated these equations with OLS alone instead of with 2SLS, 
we would have obtained:
	
COt = -266.65 + 0.46YDt + 0.56COt-1	
(14.30)
10.102      10.102
4.70           5.66
N = 32    R2 = .999    DW = 0.77
	
INt = -267.16 + 0.19Yt - 9.26rt-1	
(14.31)
10.012 111.192
15.87   - 0.83
N = 32  R2 = .956  DW = 0.47
Let’s compare the OLS and 2SLS results. At first glance, there doesn’t seem to 
be much difference between them. If OLS is biased, how could this occur? 
When the fit of the stage-one reduced-form equations is excellent, as in 
Equation 14.26, then Y and YN  are virtually identical, and the second stage of 
2SLS is quite similar to the OLS estimate.
Also, take a look at the Durbin–Watson statistics. DW is well below the dL 
of 1.31 (one-sided 5-percent significance, N = 32, K = 2) in all the equa-
tions despite DW’s bias toward 2 in the consumption equation (because it’s 
a dynamic model). Consequently, positive serial correlation is likely to exist 
in the residuals of both equations. Applying GLS to the two 2SLS-estimated 
equations is tricky, however, especially because, as mentioned in Section 
12.3, serial correlation causes bias in an equation with a lagged dependent 
variable, as in the consumption function.
Finally, what about nonstationarity? We learned in Chapter 12 that time-
series models like these have the potential to be spurious in the face of non-
stationarity. Are any of these regressions spurious? Well, as you can guess 
from looking at the data, quite a few of the series in this model are, indeed, 
nonstationary. Luckily, the interest rate is stationary. However, it turns out that 
the consumption function is reasonably cointegrated, so Equations 14.28 
and 14.30 probably can stand as estimated. Unfortunately, the investment 
equation suffers from nonstationarity that almost surely results in an inflated 
t-score for GDP and a low t-score for rt-1 (because rt-1 is stationary when all 
the other variables in the equation are nonstationary). Given the tools covered 
so far in this text, however, there is little we can do to improve the situation.
These caveats aside, this model has provided us with a complete example 
of the use of 2SLS to estimate a simultaneous system. However, the applica-
tion of 2SLS requires that the equation being estimated be “identified,” so 
before we can conclude our study of simultaneous equations, we need to 
address the problem of identification.
8


430
Chapter 14  Simultaneous Equations
14.4   The Identification Problem
Two-Stage Least Squares cannot be applied to an equation unless that equa-
tion is identified. Before estimating any equation in a simultaneous system, 
you therefore must address the identification problem. Once an equation is 
found to be identified, then it can be estimated with 2SLS, but if an equation 
is not identified (underidentified), then 2SLS cannot be used no matter how 
large the sample. Such underidentified equations can be estimated with OLS, 
but OLS estimates of underidentified equations are difficult to interpret. It’s 
important to point out that an equation being identified (and therefore capa-
ble of being estimated with 2SLS) does not ensure that the resulting 2SLS 
estimates will be good ones. The question being asked is not how good the 
2SLS estimates will be but whether the 2SLS estimates can be obtained at all.
What Is the Identification Problem?
Identification is a precondition for the application of 2SLS to equations in 
simultaneous systems; a structural equation is identified only when enough 
of the system’s predetermined variables are omitted from the equation in 
question to allow that equation to be distinguished from all the others in the 
system. Note that one equation in a simultaneous system might be identified 
and another might not.
How can we have equations that we cannot identify? To see how, let’s 
consider a supply and demand simultaneous system in which only price and 
quantity are specified:
	
QDt = α0 + α1Pt + eDt  (demand)	
(14.32)
	
QSt  = β0 + β1Pt + eSt   (supply)	
(14.33)
where: 	
QDt = QSt
Although we’ve labeled one equation as the demand equation and the other 
as the supply equation, the computer will not be able to identify them from 
the data because the right-side and the left-side variables are exactly the same 
in both equations; without some predetermined variables included to dif-
ferentiate these two equations, it would be impossible to distinguish supply 
from demand.
What if we added a predetermined variable like weather (W) to the supply 
equation for an agricultural product? Then, Equation 14.33 would become:
	
QSt = β0 + β1Pt + β2Wt + eSt	
(14.34)


431
  The Identification Problem
In such a circumstance, every time W changed, the supply curve would shift, 
but the demand curve would not, so that eventually we would be able to col-
lect a good picture of what the demand curve looked like.
Figure 14.3 demonstrates this. Given four different values of W, we get four 
different supply curves, each of which intersects with the constant demand 
curve at a different equilibrium price and quantity (intersections 1–4). These 
equilibria are the data that we would be able to observe in the real world and 
are all that we could feed into the computer. As a result, we would be able 
to identify the demand curve because we left out at least one predetermined 
variable. When this predetermined variable changed, but the demand curve 
didn’t, the supply curve shifted so that quantity demanded moved along the 
demand curve and we gathered enough information to estimate the coef-
ficients of the demand curve. The supply curve, on the other hand, remains 
as much a mystery as ever because its shifts give us no clue whatsoever about 
its shape. In essence, the demand curve was identified by the predetermined 
variable that was included in the system but excluded from the demand 
equation. The supply curve is not identified because there is no such 
excluded predetermined variable for it.
Even if we added W to the demand curve as well (which wouldn’t make 
sense from a theoretical point of view), that would not identify the supply 
curve. In fact, if we had W in both equations, the two would be identical 
again, and although both would shift when W changed, those shifts would 
0
1
3
2
4
Q
D
S1
P
S3
S2
S4
Figure 14.3  A Shifting Supply Curve Allows the Identification of the  
Demand Curve
If the supply curve shifts but the demand curve does not, then we move along the  
demand curve, which allows us to identify and estimate the demand curve (but not the 
supply curve).


432
Chapter 14  Simultaneous Equations
give us no information about either curve! As illustrated in Figure 14.4, the 
observed equilibrium prices and quantities would be almost random inter-
sections describing neither the demand nor the supply curve. That is, the 
shifts in the supply curve are the same as before, but now the demand curve 
also shifts with W. In this case, it’s not possible to identify either the demand 
curve or the supply curve.
The way to identify both curves is to have at least one predetermined vari-
able in each equation that is not in the other, as in:
	
QDt = α0 + α1Pt + α2Xt + eDt	
(14.35)
	
QSt = β0 + β1Pt + β2Wt + eSt	
(14.36)
Now when W changes, the supply curve shifts, and we can identify the 
demand curves from the data on equilibrium prices and quantities. When X 
changes, the demand curve shifts, and we can identify the supply curve from 
the data.
To sum, identification is a precondition for the application of 2SLS to 
equations in simultaneous systems. A structural equation is identified only 
when the predetermined variables are arranged within the system so as to 
allow us to use the observed equilibrium points to distinguish the shape of 
the equation in question. Most systems are quite a bit more complicated than 
0
1
3
2
4
Q
S1
D1
P
S3
S2
S4
D3
D2
D4
Figure 14.4  If Both the Supply Curve and the Demand Curve Shift, Neither 
Curve Is Identified
If both the supply curve and the demand curve shift in response to the same variable, 
then we move from one equilibrium to another, and the resulting data points identify 
neither curve. To allow such an identification, at least one predetermined variable must 
cause one curve to shift while allowing the other to remain constant.


433
  The Identification Problem
the previous ones, however, so econometricians need a general method by 
which to determine whether equations are identified. The method typically 
used is the order condition of identification.
The Order Condition of Identification
The order condition is a systematic method of determining whether a par-
ticular equation in a simultaneous system has the potential to be identified. 
If an equation can meet the order condition, then it is identified in all but a 
very small number of cases. We thus say that the order condition is a neces-
sary but not sufficient condition of identification.11
What is the order condition? Recall that we have used the phrases endog-
enous and predetermined to refer to the two kinds of variables in a simultane-
ous system. Endogenous variables are those that are jointly determined in 
the system in the current time period. Predetermined variables are exogenous 
variables plus any lagged endogenous variables that might be in the model. 
For each equation in the system, we need to determine:
1.	 The number of predetermined (exogenous plus lagged endogenous) 
variables in the entire simultaneous system.
2.	 The number of slope coefficients estimated in the equation in question.
11. A sufficient condition for an equation to be identified is called the rank condition, but most 
researchers examine just the order condition before estimating an equation with 2SLS. These 
researchers let the computer estimation procedure tell them whether the rank condition has 
been met (by its ability to apply 2SLS to the equation). Those interested in the rank condition 
are encouraged to consult an advanced econometrics text.
THE ORDER CONDITION: A necessary condition for an equation to be 
identified is that the number of predetermined (exogenous plus lagged endog-
enous) variables in the system be greater than or equal to the number of slope 
coefficients in the equation of interest.
In equation form, a structural equation meets the order condition if:
The number of predetermined variables Ú The number of slope coefficients 
(in the simultaneous system)               (in the equation)


434
Chapter 14  Simultaneous Equations
Two Examples of the Application of the Order Condition
Let’s apply the order condition to some of the simultaneous equations sys-
tems encountered in this chapter. For example, consider once again the cola 
supply and demand model of Section 14.1:
	
QDt = α0 + α1Pt + α2X1t + α3X2t + eDt	
(14.37)
	
QSt  = β0 + β1Pt + β2X3t + eSt
	
(14.38)
	
QSt  = QDt
	
(14.39)
Equation 14.37 is identified by the order condition because the number of 
predetermined variables in the system (three, X1, X2, and X3) is equal to the 
number of slope coefficients in the equation (three: α1, α2, and α3). This 
particular result (equality) implies that Equation 14.37 is exactly identified by 
the order condition. Equation 14.38 is also identified by the order condition 
because there are still three predetermined variables in the system, but there 
are only two slope coefficients in the equation; this condition implies that 
Equation 14.38 is overidentified. 2SLS can be applied to equations that are 
identified (which includes exactly identified and overidentified), but not to 
equations that are underidentified.
A more complicated example is the small macroeconomic model of 
Section 14.3:
	
Yt
 = COt + It + Gt + NXt
	
(14.22)
	
COt = β0 + β1YDt + β2COt-1 + e1t	
(14.23)
	
YDt = Yt - Tt
	
(14.24)
	
It
 = β3 + β4Yt + β5rt-1 + e2t
	
(14.25)
As we’ve noted, there are five predetermined variables (exogenous plus lagged 
endogenous) in this system 1Gt, NXt, Tt, COt-1, and rt-12. Equation 14.23  
has two slope coefficients 1β1 and β22, so this equation is overidentified 
15 7 22 and meets the order condition of identification. As the reader can 
verify, Equation 14.25 also turns out to be overidentified. Since the 2SLS 
computer program did indeed come up with estimates of the βs in the 
model, we knew this already. Note that Equations 14.22 and 14.24 are iden-
tities and are not estimated, so we’re not concerned with their identification 
properties.


435
  Summary
14.5   Summary
	 1.	 Most economic and business models are inherently simultaneous 
because of the dual causality, feedback loops, or joint determination 
of particular variables. These simultaneously determined variables are 
called endogenous, and nonsimultaneously determined variables are 
called exogenous.
	 2.	 A structural equation characterizes the theory underlying a particular 
variable and is the kind of equation we have used to date in this text. 
A reduced-form equation expresses a particular endogenous variable 
solely in terms of an error term and all the predetermined (exogenous 
and lagged endogenous) variables in the simultaneous system.
	 3.	 Simultaneous equations models violate Classical Assumption III that 
the error term is uncorrelated with the explanatory variables. This 
occurs because of the feedback effects of the endogenous variables. 
For example, an unusually high observation of an equation’s error 
term works through the simultaneous system and eventually causes 
a high (with positive coefficients) value for the endogenous variables 
that appear as explanatory variables in the equation in question, thus 
violating Classical Assumption III.
	 4.	 If OLS is applied to the coefficients of a simultaneous system, the 
resulting estimates are biased and inconsistent. This occurs mainly be-
cause of the violation of Classical Assumption III; the OLS regression 
package attributes to explanatory variables changes in the dependent 
variable actually caused by the error term (with which the explanatory 
variables are correlated).
	 5.	 Two-Stage Least Squares is a method of estimating simultaneous 
equations systems. It works by systematically using the reduced-form 
equations of the system to create substitutes for the endogenous 
variables that are independent of the error terms. It then estimates 
the structural equations of the system with these substitutes replac-
ing the endogenous variables where they appear as explanatory 
variables.
	 6.	 Two-Stage Least Squares estimates are consistent but biased. Luckily, 
the expected bias due to 2SLS usually is smaller than the expected 
bias due to OLS. If the fit of the reduced-form equations is poor, then 
2SLS will not work very well.


436
Chapter 14  Simultaneous Equations
	 7.	 2SLS cannot be applied to an equation that’s not identified. A neces-
sary (but not sufficient) requirement for identification is the order 
condition, which requires that the number of predetermined vari-
ables in the system be greater than or equal to the number of slope 
coefficients in the equation of interest. Sufficiency usually is deter-
mined by the ability of 2SLS to estimate the coefficients.
EXERCISES
(The answers to the even-numbered exercises are in Appendix A.)
	 1.	 Write the meaning of each of the following terms without referring 
to the book (or your notes), and compare your definition with the 
version in the text for each.
a.	endogenous variables (p. 412)
b.	exogenous variables (p. 412)
c.	 identification (p. 430)
d.	impact multipliers (p. 417)
e.	 instrumental variable (p. 421)
f.	 order condition (p. 433)
g.	predetermined variable (p. 413)
h.	reduced-form equations (p. 416)
i.	 simultaneity bias (p. 418)
j.	 structural equations (p. 413)
k.	Two-Stage Least Squares (2SLS) (p. 422)
	 2.	 Section 14.1 works through Equations 14.2 and 14.3 to show the 
violation of Classical Assumption III by an unexpected increase in e1. 
Show the violation of Classical Assumption III by working through 
the following examples:
a.	a decrease in e2 in Equation 14.3
b.	an increase in eD in Equation 14.4
c.	 an increase in e1 in Equation 14.23
	 3.	 The word recursive is used to describe an equation that has an impact 
on a simultaneous system without any feedback from the system to 
the equation. Which of the equations in the following systems are 
simultaneous, and which are recursive? Be sure to specify which vari-
ables are endogenous and which are predetermined:


437
Exercises
a.	 Y1t = β0 + β1Y2t + β2X1t + β3X2t-1 + e1t
	
Y2t = α0 + α1Y3t + α2Y1t + α3X4t + e2t
	
Y3t = Ω0 + Ω1X2t + Ω2X1t-1 + Ω3X4t-1 + e3t
b.	Zt = β0 + β1Xt + β2Yt + β3Ht + e1t
	
Xt = α0 + α1Zt + α2Pt-1 + e2t
	
Ht = Ω0 + Ω1X2t + Ω2Bt + Ω3CSt + Ω4Dt + e3t
c.	 Y1t = β0 + β1Y2t + β2X1t + β3X2t + e1t
	
Y2t = α0 + α1Y3t + α2X5t + e2t
	 4.	 Determine the identification properties of the following equations. 
In particular, be sure to note the number of predetermined variables 
in the system, the number of slope coefficients in the equation, and 
whether the equation is underidentified, overidentified, or exactly 
identified.
a.	Equations 14.2–14.3
b.	Equations 14.13–14.14
c.	 part a of Exercise 3 (assume all equations are stochastic)
d.	part b of Exercise 3 (assume all equations are stochastic)
	 5.	 As an exercise to gain familiarity with the 2SLS program on your 
computer, take the data provided for the simple Keynesian model in 
Section 14.3, and:
a.	Estimate the investment function with OLS.
b.	Estimate the reduced form for Y with OLS.
c.	 Substitute the YN  from your reduced form into the investment func-
tion and run the second stage yourself with OLS.
d.	Estimate the investment function with your computer’s 2SLS pro-
gram (if there is one) and compare the results with those obtained 
in part c.
	 6.	 Suppose that a fad for oats (resulting from the announcement of the 
health benefits of oat bran) has made you toy with the idea of becom-
ing a broker in the oat market. Before spending your money, you 
decide to build a simple model of supply and demand (identical to 
those in Sections 14.1 and 14.2) of the market for oats:
QDt = β0 + β1Pt + β2YDt + eDt
QSt  = α0 + α1Pt + α2Wt + eSt
QDt = QSt


438
Chapter 14  Simultaneous Equations
where:	
QDt = the quantity of oats demanded in time period t
	
QSt  = the quantity of oats supplied in time period t
	
Pt
 = the price of oats in time period t
	
Wt  = average oat-farmer wages in time period t
	
YDt = disposable income in time period t
a.	You notice that no left-hand-side variable appears on the right 
side of either of your stochastic simultaneous equations. Does this 
mean that OLS estimation will encounter no simultaneity bias? 
Why or why not?
b.	You expect that when Pt goes up, QDt will fall. Does this mean 
that if you encounter simultaneity bias in the demand equation, 
it will be negative instead of the positive bias we typically associ-
ate with OLS estimation of simultaneous equations? Explain your 
answer.
c.	 Carefully outline how you would apply 2SLS to this system. How 
many equations (including reduced forms) would you have to esti-
mate? Specify precisely which variables would be in each equation.
d.	Given the following hypothetical data,12 estimate OLS and 2SLS 
versions of your oat supply and demand equations.
e.	 Compare your OLS and 2SLS estimates. How do they compare 
with your prior expectations? Which equation do you prefer? 
Why?
12. These data are from the excellent course materials that Professors Bruce Gensemer and 
James Keeler prepared to supplement the use of this text at Kenyon College.
Year
Q
P
W
YD
  1
50
10
100
15
  2
54
12
102
12
  3
65
  9
105
11
  4
84
15
107
17
  5
75
14
110
19
  6
85
15
111
30
  7
90
16
111
28
  8
60
14
113
25
  9
40
17
117
23
10
70
19
120
35
Datafile = OATS14


439
Exercises
	 7.	 Simultaneous equations make sense in cross-sectional as well as time-
series applications. For example, James Ragan13 examined the effects of 
unemployment insurance (hereafter UI) eligibility standards on unem-
ployment rates and the rate at which workers quit their jobs. Ragan 
used a pooled data set that contained observations from a number of 
different states from four different years (requirements for UI eligibility 
differ by state). His results are as follows (t-scores in parentheses):
QUi = 7.00 + 0.089URi - 0.063UNi - 2.83REi - 0.032MXi
10.102    1 - 0.632      1 - 1.982  1 - 0.732
+ 0.003ILi  - 0.25QMi + g
10.012     1 - 0.522  
URi = - 0.54 + 0.44QUi + 0.13UNi + 0.049MXi
11.012       13.292       11.712
+ 0.56ILi  + 0.63QMi + g
12.032       12.052
where:	
QUi = the quit rate (quits per 100 employees) in the ith state
URi  = the unemployment rate in the ith state
UNi  = union membership as a percentage of nonagricul-
tural employment in the ith state
REi  = average hourly earnings in the ith state relative to 
the average hourly earnings for the United States
ILi  = dummy variable equal to 1 if workers in the ith 
state are eligible for UI if they are forced to quit a 
job because of illness, 0 otherwise
QMi = dummy variable equal to 1 if the ith state maintains 
full UI benefits for the quitter (rather than lowering 
benefits), 0 otherwise
MXi  = maximum weekly UI benefits relative to average 
hourly earnings in the ith state
a.	Hypothesize the expected signs for the coefficients of each of the 
explanatory variables in the system. Use economic theory to justify 
your answers. Which estimated coefficients are different from your 
expectations?
8
8
13. James F. Ragan, Jr., “The Voluntary Leaver Provisions of Unemployment Insurance and Their 
Effect on Quit and Unemployment Rates,” Southern Economic Journal, Vol. 15, No. 1, pp. 135–146.


440
Chapter 14  Simultaneous Equations
b.	Ragan felt that these two equations would encounter simultaneity bias 
if they were estimated with OLS. Do you agree? Explain your answer. 
(Hint: Start by deciding which variables are endogenous and why.)
c.	 The actual equations included a number of variables not docu-
mented earlier, but the only predetermined variable in the system 
that was included in the QU equation but not the UR equation was 
RE. What does this information tell you about the identification 
properties of the QU equation? The UR equation?
d.	What are the implications of the lack of significance of the endog-
enous variables where they appear on the right-hand side of the 
equations?
e.	 What, if any, policy recommendations do these results suggest?
14.6   Appendix: Errors in the Variables
Until now, we have implicitly assumed that our data were measured accu-
rately. That is, although the stochastic error term was defined as including 
measurement error, we never explicitly discussed what the existence of such 
measurement error did to the coefficient estimates. Unfortunately, in the real 
world, errors of measurement are common. Mismeasurement might result 
from the data being based on a sample, as are almost all national aggregate 
statistics, or simply because the data were reported incorrectly. Whatever the 
cause, these errors in the variables are mistakes in the measurement of the 
dependent variable and/or one or more of the independent variables that are 
large enough to have potential impacts on the estimation of the coefficients. 
Such errors in the variables might be better called “measurement errors in the 
data.” We will tackle this subject by first examining errors in the dependent 
variable and then moving on to look at the more serious problem of errors in 
an independent variable. We assume a single equation model. The reason we 
have included this topic here is that errors in explanatory variables give rise to 
biased OLS estimates very similar to simultaneity bias.
Measurement Errors in the Data for the Dependent Variable
Suppose that the true regression model is
	
Yi = β0 + β1Xi + ei	
(14.40)
and further suppose that the dependent variable, Yi, is measured incorrectly, 
so that Yi* is observed instead of Yi, where
	
Yi* = Yi + vi	
(14.41)


441
APPENDIX: ERRORS IN THE VARIABLES
and where vi is an error of measurement that has all the properties of a clas-
sical error term. What does this mismeasurement do to the estimation of 
Equation 14.40?
To see what happens when Yi* = Yi + vi, let’s add vi to both sides of Equa-
tion 14.40, obtaining
	
Yi + vi = β0 + β1Xi + ei + vi	
(14.42)
which is the same as
	
Yi* = β0 + β1Xi + ei*	
(14.43)
where ei* = 1ei + vi2. That is, we estimate Equation 14.43 when in reality 
we want to estimate Equation 14.40. Take another look at Equation 14.43. 
When vi changes, both the dependent variable and the error term ei* move 
together. This is no cause for alarm, however, since the dependent variable 
is always correlated with the error term. Although the extra movement will 
increase the variability of Y and therefore be likely to decrease the overall sta-
tistical fit of the equation, an error of measurement in the dependent variable 
does not cause any bias in the estimates of the βs.
Measurement Errors in the Data for an Independent Variable
This is not the case when the mismeasurement is in the data for one or more 
of the independent variables. Unfortunately, such errors in an independent 
variable cause bias that is quite similar in nature (and in remedy) to simul-
taneity bias. To see this, once again suppose that the true regression model is 
Equation 14.40:
	
Yi = β0 + β1Xi + ei	
(14.40)
But now suppose that the independent variable, Xi, is measured incorrectly, 
so that Xi* is observed instead of Xi, where
	
Xi* = Xi + ui	
(14.44)
where ui is an error of measurement like vi in Equation 14.41. To see what 
this mismeasurement does to the estimation of Equation 14.40, let’s solve 
Equation 14.44 for Xi (obtaining Xi = Xi* - ui) and substitute Xi back into 
Equation 14.40, giving us:
	
Yi = β0 + β11Xi* - ui2 + ei	
(14.45)
which can be rewritten as:
	
Yi = β0 + β1Xi* + 1ei - β1ui2	
(14.46)
or
	
Yi = β0 + β1Xi* + ei**	
(14.47)


442
Chapter 14  Simultaneous Equations
where ei** = 1ei - β1ui2. In this case, we estimate Equation 14.47 when we 
should be trying to estimate Equation 14.40. Notice what happens to Equa-
tion 14.47 when ui changes, however. When ui changes, the stochastic error 
term ei** and the independent variable Xi* move in opposite directions; they 
are correlated! Such a correlation is a direct violation of Classical Assumption 
III in a way that is remarkably similar to the violation (described in Sec-
tion 14.1) of the same assumption in simultaneous equations. Not surpris-
ingly, this violation causes the same problem, bias, for errors-in-the-variables 
models that it causes for simultaneous equations. That is, because of the 
measurement error in the independent variable, the OLS estimates of the 
coefficients of Equation 14.47 are biased and inconsistent. Interestingly, 
the estimated coefficient β1 is biased toward zero. This is because if β1 is neg-
ative, e** will be positively correlated with X*, creating upward bias, while if 
β1 is positive, e** will be negatively correlated with X*, creating downward 
bias.14
In order to rid an equation of the bias caused by measurement errors in 
the data for one or more of the independent variables, it’s logical to use 
the instrumental variables (IV) approach of Section 14.3. However, the IV 
approach is only rarely applied to errors in the variables problems for two 
reasons. First, while we may suspect that there are measurement errors, it’s 
unusual to be sure that they exist. Second, even if we know that there are 
errors, it’s difficult to find an instrumental variable that is both highly cor-
related with X and uncorrelated with e. In fact, X* often is about as good an 
instrument as we can find, so no action is taken. If the mismeasurement in X 
is known to be large, of course, some remedy is required.
To sum, an error of measurement in one or more of the independent vari-
ables will cause the error term of Equation 14.47 to be correlated with the 
mismeasured independent variable, causing bias that’s similar to simultaneity 
bias.15
14. See William H. Greene, Econometric Analysis (Upper Saddle River, NJ: Prentice Hall, 1999), 
pp. 375–381.
15. If measurement errors exist in the data for the dependent variable and one or more of the 
independent variables, then both decreased overall statistical fit and bias in the estimated coef-
ficients will result. Indeed, a famous econometrician, Zvi Griliches, warned that errors in the 
data coming from their measurement, usually computed from samples or estimates, imply 
that the fancier estimating techniques should be avoided because they are more sensitive to 
data errors than is OLS. See Zvi Griliches, “Data and Econometricians—the Uneasy Alliance,” 
American Economic Review, Vol. 75, No. 2, p. 199. See also, B. D. McCullough and H. D. Vinod, 
“The Numerical Reliability of Econometric Software,” Journal of Economic Literature, Vol. 37, 
pp. 633–665.
