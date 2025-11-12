# Chapter 15: Forecasting

**Pages:** 463-484

---

443
Chapter 15
Forecasting
15.1  What Is Forecasting?
15.2  More Complex Forecasting Problems
15.3  ARIMA Models
15.4  Summary and Exercises
Of the uses of econometrics outlined in Chapter 1, we have discussed fore-
casting the least. Accurate forecasting is vital to successful planning, so it’s 
the primary application of many business and governmental uses of econo-
metrics. For example, manufacturing firms need sales forecasts, banks need 
interest rate forecasts, and governments need unemployment and inflation 
rate forecasts.
To many business and government leaders, the words econometrics and 
forecasting mean the same thing. Such a simplification gives econometrics a 
bad name because many econometricians overestimate their ability to pro-
duce accurate forecasts, resulting in unrealistic claims and unhappy clients. 
Some of their clients would probably applaud the nineteenth century New 
York law (luckily unenforced but apparently also unrepealed) that provides 
that persons “pretending to forecast the future” shall be liable to a $250 fine 
and/or six months in prison.1 Although many econometricians might wish 
that such consultants would call themselves “futurists” or “soothsayers,” 
it’s impossible to ignore the importance of econometrics in forecasting in 
today’s world.
The ways in which the prediction of future events is accomplished are 
quite varied. At one extreme, some forecasters use models with thousands of 
1. Section 899 of the N.Y. State Criminal Code: the law does not apply to “ecclesiastical bodies 
acting in good faith and without personal fees.”


444
Chapter 15  Forecasting
equations.2 At the other extreme, quite accurate forecasts can be created with 
nothing more than a good imagination and a healthy dose of self-confidence.
Unfortunately, it’s unrealistic to think we can cover even a small portion 
of the topic of forecasting in one short chapter. Indeed, there are a number 
of excellent books and journals on this subject alone.3 Instead, this chapter 
is meant to be a brief introduction to the use of econometrics in forecast-
ing. We will begin by using simple linear equations and then move on to 
investigate a few more complex forecasting situations. The chapter concludes 
with an introduction to a technique, called ARIMA, that calculates forecasts 
entirely from past movements of the dependent variable without the use 
of any independent variables at all. ARIMA is almost universally used as a 
benchmark forecast, so it’s important to understand even though it’s not 
based on economic theory.
15.1   What Is Forecasting?
In general, forecasting is the act of predicting the future; in econometrics, 
forecasting is the estimation of the expected value of a dependent variable 
for observations that are outside the sample data set. In most forecasts, the 
values being predicted are for time periods in the future, but cross-sectional 
predictions of values for countries or people not in the sample are also 
common. To simplify terminology, the words prediction and forecast will be 
used interchangeably in this chapter. (Some authors limit the use of the word 
forecast to out-of-sample prediction for a time series.)
We’ve already encountered an example of a forecasting equation. Think 
back to the weight/height example of Section 1.4 and recall that the pur-
pose of that model was to guess the weight of a male customer based on his 
height. In that example, the first step in building a forecast was to estimate 
Equation 1.19:
	 Estimated weight = 103.40 + 6.38 # Height (inches over five feet)	 (1.19)
That is, we estimated that a customer’s weight on average equaled a base of 
103.40 pounds plus 6.38 pounds for each inch over 5 feet. To actually make 
2. For an interesting comparison of such models, see Ray C. Fair and Robert J. Shiller, “Comparing 
Information in Forecasts from Econometric Models,” American Economic Review, Vol. 80, No. 3, 
pp. 375–389.
3. See, for example, G. Elliott, C. W. J. Granger, and A. G. Timmermann, Handbook of Economic 
Forecasting (Oxford, UK: North-Holland Elsevier, 2006), and N. Carnot, V. Koen, and B. Tissot, 
Economic Forecasting (Basingstoke, UK: Palgrave MacMillan, 2005).


445
  What Is Forecasting?
the prediction, all we had to do was to substitute the height of the individual 
whose weight we were trying to predict into the estimated equation. For a 
male who is 6′1″ tall, for example, we’d calculate:
	
Predicted weight = 103.40 + 6.38 # (13 inches over five feet)	
(15.1)
or
	
103.40 + 82.90 = 186.3 pounds
The weight-guessing equation is a specific example of using a single linear 
equation to predict or forecast. Our use of such an equation to make a fore-
cast can be summarized into two steps:
1.	 Specify and estimate an equation that has as its dependent variable the item 
that we wish to forecast. We obtain a forecasting equation by specifying 
and estimating an equation for the variable we want to predict:
	
YNt = βN 0 + βN 1X1t + βN 2X2t  1t = 1, 2, c, T2	
(15.2)
	
Such specification and estimation have been the topics of the first 14 
chapters of this book. The use of 1t = 1, 2, c, T2 to denote the sam-
ple size is fairly standard for time-series forecasts (t stands for “time”).
2.	 Obtain values for each of the independent variables for the observations for 
which we want a forecast and substitute them into our forecasting equation. 
To calculate a forecast with Equation 15.2, this would mean finding 
values for period T + 1 for X1 and X2 and substituting them into the 
equation:
	
YNT+1 = βN 0 + βN 1X1T+1 + βN 2X2T+1	
(15.3)
	
What is the meaning of this YNT+1? It is a prediction of the value that Y 
will take in observation T + 1 (outside the sample) based upon our 
values of X1T+1 and X2T+1 and based upon the particular specification 
and estimation that produced Equation 15.2.
To understand these steps more clearly, let’s look at two applications of 
this forecasting approach:
Forecasting Chicken Consumption: Let’s return to the chicken demand model, 
Equation 9.14 on page 288, to see how well that equation forecasts aggregate 
per capita chicken consumption:
	
YNt = 27.7 - 0.11PCt + 0.03PBt + 0.23YDt	
(9.14)
10.032      10.022      10.012
t = - 3.38     + 1.86    + 15.7
	
R2 = .9904    N = 29 1annual 1974920022    DW = 0.99


446
Chapter 15  Forecasting
where:	
Y
 = pounds of chicken consumption per capita
	
PC and PB = the prices of chicken and beef, respectively,  
per pound
	
YD
 = per capita U.S. disposable income
To make these forecasts as realistic as possible, we held out the last three 
available years from the data set used to estimate Equation 9.14. We’ll thus 
be able to compare the equation’s forecasts with what actually happened. 
To forecast with the model, we first obtain values for the three independent 
variables and then substitute them into Equation 9.14. For 2003, PC = 34.1, 
PB = 374.6, and YD = 280.2, giving us:
YN2003 = 27.7 - 0.11134.12 + 0.031374.62 + 0.231280.22 = 99.63	
(15.4)
Continuing on through 2005, we end up with:4
4. The rest of the actual values are PC: 2004 = 24.8, 2005 = 26.8; PB: 2004 = 406.5, 
2005 = 409.1; YD: 2004 = 295.17, 2005 = 306.16. Many software packages, including Stata 
and EViews, have forecasting modules that will allow you to calculate forecasts using equations 
like Equation 15.4 automatically. If you use that module, you’ll note that the forecasts differ 
slightly because we rounded the coefficient estimates.
5. For a summary of seven different methods of measuring forecasting accuracy, see Peter 
Kennedy, A Guide to Econometrics (Malden, MA: Blackwell, 2008), pp. 334–335. 
Year
Forecast
Actual
Percent Error
2003
  99.63
  95.63
4.2
2004
105.06
  98.58
6.6
2005
107.44
100.60
6.8
How does the model do? Well, forecasting accuracy, like beauty, is in the 
eye of the beholder, and there are many ways to answer the question.5  
The simplest method is to take the mean of the percentage errors (in absolute 
value), an approach called, not surprisingly, the mean absolute percentage 
error (MAPE) method. The MAPE for our forecast is 5.9 percent.
The most popular alternative method of evaluating forecast accuracy is the 
root mean square error criterion (RMSE), which is calculated by squaring 
the forecasting error for each time period, averaging these squared amounts, 
and then taking the square root of this average. One advantage of the RMSE 
is that it penalizes large errors because the errors are squared before they’re 
added together. For the chicken demand forecasts, the RMSE of our forecast is 
5.97 pounds (or 6 percent).


447
  What Is Forecasting?
As you can see in Figure 15.1, it really doesn’t matter which method you 
use, because the unconditional forecasts generated by Equation 9.14 track 
quite well with reality. We missed by around 6 percent.
Forecasting Stock Prices: Some students react to the previous example by 
wanting to build a model to forecast stock prices and make a killing on 
the stock market. “If we could predict the price of a stock three years from 
now to within six percent,” they reason, “we’d know which stocks to buy.” 
0
2003
2004
2005
Time
Forecasted
Actual
Consumption of Chicken
Pounds
per
Capita
100
75
50
25
0
1
3
2
4
Time
Forecasted
Actual
Kellogg’s Stock Price
$
30
25
20
15
10
5
Figure 15.1  Forecasting Examples
In the chicken consumption example, the equation’s forecast errors averaged around  
6 percent. For the stock price model, even actual values for the independent variables 
and an excellent fit within the sample could not produce an accurate forecast.


448
Chapter 15  Forecasting
To see how such a forecast might work, let’s look at a simplified model of the 
quarterly price of a particular individual stock, that of the Kellogg Company 
(maker of breakfast cereals and other products):
PKt = -  7.80 + 0.0096DJAt + 2.68KEGt + 16.18DIVt + 4.84BVPSt
10.00242   
12.832     122.702    11.472
t = 3.91         0.95        0.71         3.29
R2 = .95    N = 35    DW = 1.88	
(15.5)
where:	
PKt
 = the dollar price of Kellogg’s stock in quarter t
	
DJAt  = the Dow Jones industrial average in quarter t
	
KEGt  = Kellogg’s earnings growth (percent change in annual 
earnings over the previous five years) that quarter
	
DIVt  = Kellogg’s declared dividends (in dollars) that quarter
	
BVPSt = per-share book value of the Kellogg corporation that quarter
The signs of the estimated coefficients all agree with those hypothesized 
before the regression was run, R2 indicates a good overall fit, and the 
Durbin–Watson test indicates that the hypothesis of no positive serial corre-
lation cannot be rejected. The low t-scores for KEG and DIV are caused by 
multicollinearity 1r = .9852, but both variables are left in the equation 
because of their theoretical importance. Note also that most of the variables 
in the equation are nonstationary, surely causing some of the good fit.
To forecast with Equation 15.5, we collected actual values for all of the 
independent variables for the next four quarters and substituted them into 
the right side of the equation, obtaining:
8
Quarter
Forecast
Actual
Percent Error
1
$26.32
$24.38
  8.0
2
  27.37
  22.38
22.3
3
  27.19
  23.00
18.2
4
  27.13
  21.88
24.0
How did our forecasting model do? Even though the R2 within the sample 
was .95, even though we used actual values for the independent variables, 
and even though we forecasted only four quarters beyond our sample, the 
model was something like 20 percent off. If we had decided to buy Kellogg’s 
stock based on our forecast, we’d have lost money! Since other attempts to 
forecast stock prices have also encountered difficulties, this doesn’t seem like 
a reasonable use for econometric forecasting.
The poor performance of forecasting in the stock market can be explained 
by an economic theory called the efficient markets hypothesis, which suggests 


449
  More Complex Forecasting Problems
that accurate predictions of stock prices are practically impossible. The efficient 
markets hypothesis theorizes that “security prices fully reflect all available 
information.”6 Thus, forecasting stock prices becomes a game of chance to 
the extent that markets are efficient and current prices reflect the available 
information. Although an investor who has inside information (or who 
perhaps invents a superior forecasting approach) has an opportunity to cre-
ate better than average stock price forecasts, the use of insider information is 
illegal in most equity markets.
15.2   More Complex Forecasting Problems
The forecasts generated in the previous section are quite simple, however, and 
most actual forecasting involves one or more additional questions. For example:
1.	 Unknown Xs: It’s unrealistic to expect to know the values for the inde-
pendent variables outside the sample. For instance, we’ll almost never 
know what the Dow Jones industrial average will be in the future when 
we are making forecasts of the price of a given stock, and yet we as-
sumed that knowledge when making our Kellogg price forecasts. What 
happens when we don’t know the values of the independent variables 
for the forecast period?
2.	 Serial Correlation: If there is serial correlation involved, the forecasting 
equation may be estimated with GLS. How should predictions be 
adjusted when forecasting equations are estimated with GLS?
3.	 Confidence Intervals: All the previous forecasts were single values, but 
such single values are almost never exactly right. Wouldn’t it be more 
helpful if we forecasted an interval within which we were confident 
that the actual value would fall a certain percentage of the time? How 
can we develop these confidence intervals?
4.	 Simultaneous Equations Models: As you saw in Chapter 14, many eco-
nomic and business equations are part of simultaneous models. How 
can we use an independent variable to forecast a dependent variable 
when we know that a change in the value of the dependent variable will 
change, in turn, the value of the independent variable that we used to 
make the forecast?
Even a few questions like these should be enough to convince you that 
forecasting is more complex than is implied by Section 15.1.
6. http://www.morningstar.com/InvGlossary, 10/20/15. For more, see Burton Malkiel, A Random 
Walk down Wall Street (London: W. W. Norton, 2007).


450
Chapter 15  Forecasting
Conditional Forecasting (Unknown X Values  
for the Forecast Period)
A forecast in which all values of the independent variables are known with 
certainty can be called an unconditional forecast, but, as mentioned previ-
ously, the situations in which one can make such unconditional forecasts are 
rare. More likely, we will have to make a conditional forecast, for which 
actual values of one or more of the independent variables are not known. We 
are forced to obtain forecasts for the independent variables before we can use 
our equation to forecast the dependent variable, which makes our forecast of 
Y conditional on our forecast of the Xs.
One key to an accurate conditional forecast is accurate forecasting of 
the independent variables. If the forecasts of the independent variables are 
unbiased, then using a conditional forecast will not introduce bias into the 
forecast of the dependent variable in a linear model. Anything but a perfect 
forecast of the independent variables will contain some amount of forecast 
error, however, and so the expected error variance associated with conditional 
forecasting will be larger than that associated with unconditional forecasting. 
Thus, one should try to find unbiased, minimum variance forecasts of the 
independent variables when using conditional forecasting.
To get good forecasts of the independent variables, take the forecastability 
of potential independent variables into consideration when making specifi-
cation choices. For instance, when deciding which of two redundant variables 
should be included in an equation to be used for forecasting, you should 
choose the one that is easier to forecast accurately. When you can, you should 
choose an independent variable that is regularly forecasted by someone else 
(an econometric forecasting firm, for example) so that you don’t have to 
forecast X yourself.
The careful selection of independent variables can sometimes help you 
avoid the need for conditional forecasting in the first place. This opportunity 
can arise when the dependent variable can be expressed as a function of lead-
ing indicators. A leading indicator is an independent variable whose move-
ments anticipate movements in the dependent variable. The best known 
leading indicator, the Index of Leading Economic Indicators, is produced 
each month.
For instance, the impact of interest rates on investment typically is not 
felt until two or three quarters after interest rates have changed. To see this, 
let’s look at the investment function of the small macroeconomic model of 
Section 14.3:
	
It = β0 + β1Yt + β2rt-1 + et	
(15.6)


451
  More Complex Forecasting Problems
where I equals gross investment, Y equals GDP, and r equals the interest rate. 
In this equation, actual values of r can be used to help forecast IT+1. Note, 
however, that to predict IT+2, we need to forecast rT+1. Thus, leading indica-
tors like r help us avoid conditional forecasting for only a time period or two. 
For long-range predictions, a conditional forecast is usually necessary.
Forecasting with Serially Correlated Error Terms
Recall from Chapter 9 that pure first-order serial correlation implies that the 
current observation of the error term et is affected by the previous error term 
and an autocorrelation coefficient, ρ:
	
et = ρet-1 + ut
where ut is a non–serially correlated error term. Also recall that when serial 
correlation is severe, one remedy is to run Generalized Least Squares (GLS) as 
noted in Equation 9.21:
	
Yt - ρYt-1 = β011 - ρ2 + β11X1t - ρX1t-12 + ut	
(9.21)
Unfortunately, whenever the use of GLS is required to rid an equation of 
pure first-order serial correlation, the procedures used to forecast with that 
equation become a bit more complex. To see why this is necessary, note that 
if Equation 9.21 is estimated, the dependent variable will be:
	
Y*t = Yt - ρNYt-1	
(15.7)
Thus, if a GLS equation is used for forecasting, it will produce predictions of 
Y*T+1 rather than of YT+1. Such predictions thus will be of the wrong variable.
If forecasts are to be made with a GLS equation, Equation 9.21 should first 
be solved for Yt before forecasting is attempted:
	
Yt = ρYt-1 + β011 - ρ2 + β11Xt - ρXt-12 + ut	
(15.8)
We now can forecast with Equation 15.8 as we would with any other equation. 
If we substitute T + 1 for t (to forecast time period T + 1) and insert estimates 
for the coefficients, ρs and Xs into the right side of the equation, we obtain:
	
YNT+1 = ρNYT + βN 011 - ρN2 + βN 11XN T+1 - ρNXT2	
(15.9)
Equation 15.9 thus should be used for forecasting when an equation has 
been estimated with GLS to correct for serial correlation.7
7. If ρN is less than 0.3, many researchers prefer to use the OLS forecast plus ρN times the lagged 
residual as their forecast instead of the GLS forecast from Equation 15.9.


452
Chapter 15  Forecasting
We now turn to an example of such forecasting with serially correlated 
error terms. In particular, recall from Chapter 9 that the Durbin–Watson 
statistic of the chicken demand equation used as an example in Section 15.1  
was 0.99, indicating significant positive first-order serial correlation. As a 
result, we estimated the chicken demand equation with GLS, obtaining 
Equation 9.25:
	
YNt = 28.5 - 0.08PCt + 0.016PBt + 0.24YDt	
(9.25)
10.042    10.0212      10.022
t =      -2.13      + 0.74     + 13.12
R2 = .963    N = 29    ρN = 0.56
Since Equation 9.25 was estimated with GLS, Y is actually Y*t , which equals 
Yt - ρNYt-1, PCt is actually PC*t , which equals PCt - ρNPCt-1, and so on. Thus, 
to forecast with Equation 9.25, we have to convert it to the form of Equation 
15.9, or:
	
YNT+1 = 0.56YT + 28.511 - 0.562 - 0.081PC T+1 - 0.56PC T2	
(15.10)
+ 0.0161PBT+1 - 0.56PBT2 + 0.241YDT+1 - 0.56YDT2
Substituting the actual values for the independent variables into Equation 15.10, 
we obtain:
Year
Forecast
Actual
Percent Error
2003
  97.57
  95.63
2.0
2004
101.02
  98.58
2.5
2005
102.38
100.60
1.8
The MAPE of the GLS forecasts is 2.1 percent, far better than that of the 
OLS forecasts. In general, GLS usually will provide superior forecasting per-
formance to OLS in the presence of serial correlation.
Forecasting Confidence Intervals
Until now, the emphasis in this text has been on obtaining point (or single- 
value) estimates. This has been true whether we have been estimating 
coefficient values or estimating forecasts. Recall, though, that a point esti-
mate is only one of a whole range of such estimates that could have been 
obtained from different samples (for coefficient estimates) or different 
independent variable values or coefficients (for forecasts). The usefulness of 
such point estimates is improved if we can also generate some idea of the 


453
  More Complex Forecasting Problems
variability of our forecasts. The measure of variability typically used is the 
confidence interval, which was defined in Section 5.5 as the range of values 
that contains the true value of the item being estimated a specified percent-
age of the time. This is the easiest way to warn forecast users that a sampling 
distribution exists.
Suppose you are trying to decide how many hot dogs to order for your 
city’s Fourth of July fireworks show and the best point forecast is that you’ll 
sell 24,000 hot dogs. How many hot dogs should you order? If you order 
24,000, you’re likely to run out about half the time! A point forecast is usu-
ally an estimate of the mean of the distribution of possible sales figures; 
you will sell more than 24,000 about as frequently as you will sell less than 
24,000. It would be easier to decide how many dogs to order if you also had 
a confidence interval that told you the range within which hot dog sales 
would fall 95 percent of the time. The usefulness of the 24,000 hot dog fore-
cast changes dramatically depending on the confidence interval; an interval 
of 22,000 to 26,000 would pin down the likely sales, but an interval of 4,000 
to 44,000 would leave you virtually in the dark about what to do.
The decision as to how many hot dogs to order would also depend on 
the costs of ordering the wrong number. These costs may not be the same 
per hot dog for overestimates as they are for underestimates. For example, if 
you don’t order enough, then you lose the entire retail price of the hot dog 
minus the wholesale price of the dog (and bun) because your other costs, 
like hiring employees and building hot dog stands, are essentially fixed. On 
the other hand, if you order too many, you lose the wholesale cost of the 
dog and bun minus whatever salvage price you might be able to get for 
day-old buns, etc. As a result, the right number to order would depend on 
your profit margin and the importance of nonreturnable inputs in your total 
cost picture.
The same techniques we use to test hypotheses can also be adapted to 
create confidence intervals. Given a point forecast, YNT+1, all we need to gener-
ate a confidence interval around that forecast are tc, the critical t-value (for 
the desired level of confidence), and SF, the estimated standard error of the 
forecast:
	
Confidence interval = YNT+1 ± SFtc	
(15.11)
or, equivalently,
	
YNT+1 - SFtc … YT+1 … YNT+1 + SFtc	
(15.12)
The critical t-value, tc, can be found in Statistical Table B-1 (for a two-tailed 
test with T - K - 1 degrees of freedom). The standard error of the forecast, SF, 


454
Chapter 15  Forecasting
for an equation with just one independent variable, equals the square root of 
the forecast error variance:
	
SF = Bs2c1 + 1>T + 1XN T+1 - X22n a
T
t = 1
1Xt - X22d 	
(15.13)
where	
s2
 = the estimated variance of the error term
	
T
 = the number of observations in the sample
	
XN T+1 = the forecasted value of the single independent variable
	
X
 = the arithmetic mean of the observed Xs in the sample
Note that Equation 15.13 implies that the forecast error variance decreases 
the larger the sample is, the more X varies within the sample, and the closer 
XN  is to its within-sample mean. An important implication is that the farther 
the X used to forecast Y is from the within-sample mean of the Xs, the 
wider the confidence interval around the YN  is going to be. This can be seen in 
Figure 15.2, in which the confidence interval actually gets wider as XN T+1 is far-
ther from X. Since forecasting outside the sample range is common, research-
ers should be aware of this phenomenon. Also note that Equation 15.13 
is for unconditional forecasting. If there is any forecast error in XN T+1, then 
the confidence interval is larger and more complicated to calculate. Finally, 
Equation 15.13 should not be used in conjunction with HC standard errors.
As mentioned, Equation 15.13 assumes that there is only one independent 
variable. The equation to be used with more than one variable is similar but 
more complicated. Equation 15.13 is valid whether Yt is in the sample period 
or outside the sample period, but it applies only to point forecasts of individ-
ual Yts. If a confidence interval for the expected value of Y, E1Yt2, is desired, 
then the correct equation to use is:
	
S*F = 3s231>T + 1XN T+1 - X22> a 1Xt - X224	
(15.14)
Forecasting with Simultaneous Equations Systems
As you learned in Chapter 14, most economic and business models are actu-
ally simultaneous in nature; for example, the investment equation used in 
Section 15.2 was estimated with 2SLS as a part of our simultaneous macro-
model in Chapter 14. Since GDP is one of the independent variables in the 
investment equation, when investment rises, so will GDP, causing a feedback 
effect that is not captured if we just forecast with a single equation. How 
should forecasting be done in the context of a simultaneous model? There 
are two approaches to answering this question, depending on whether there 


455
  More Complex Forecasting Problems
are lagged endogenous variables on the right side of any of the equations in 
the system.
If there are no lagged endogenous variables in the system, then the 
reduced-form equation for the particular endogenous variable can be used 
for forecasting because it represents the simultaneous solution of the 
system for the endogenous variable being forecasted. Since the reduced-form 
equation is the endogenous variable expressed entirely in terms of the prede-
termined variables in the system, it allows the forecasting of the endogenous 
variable without any feedback or simultaneity impacts. This result explains 
why some researchers forecast potentially simultaneous dependent variables 
with single equations that appear to combine supply-side and demand-side 
predetermined variables; they are actually using modified reduced-form 
equations to make their forecasts.
If there are lagged endogenous variables in the system, then the approach 
must be altered to take into account the dynamic interaction caused by the 
lagged endogenous variables. For simple models, this sometimes can be done 
0
95% Conﬁdence Interval
Estimated Regression
Line
YT+1
XT+1
X
Y
N
Figure 15.2  A Confidence Interval for yNt+1
A 95 percent confidence interval for YNT+1 includes the range of values within which the 
actual YT+1 will fall 95 percent of the time. Note that the confidence interval widens as 
XT+1 differs more from its within-sample mean, X.


456
Chapter 15  Forecasting
by substituting for the lagged endogenous variables where they appear in the 
reduced-form equations. If such a manipulation is difficult, however, then a 
technique called simulation analysis can be used. Simulation involves fore-
casting for the first postsample period by using the reduced-form equations 
to forecast all endogenous variables where they appear in the reduced-form 
equations. The forecast for the second postsample period, however, uses the 
endogenous variable forecasts from the last period as lagged values for any 
endogenous variables that have one-period lags while continuing to use 
sample values for endogenous variables that have lags of two or more peri-
ods. This process continues until all forecasting is done with reduced-form 
equations that use as data for lagged endogenous variables the forecasts from 
previous time periods. Although such dynamic analyses are beyond the scope 
of this chapter, they’re important to remember when considering forecasting 
with a simultaneous system.8
15.3   ARIMA Models
The forecasting techniques of the previous two sections are applications of 
familiar regression models. We use linear regression equations to forecast the 
dependent variable by plugging likely values of the independent variables 
into the estimated equations and calculating a predicted value of Y; this bases 
the prediction of the dependent variable on the independent variables (and 
on their estimated coefficients).
ARIMA (the name will be explained shortly) is an increasingly popular 
forecasting technique that completely ignores independent variables in 
making forecasts. ARIMA is a highly refined curve-fitting device that uses 
current and past values of the dependent variable to produce often accurate 
short-term forecasts of that variable. While a traditional econometric model 
attempts to describe and estimate a variable’s underlying structure (like a 
consumption function or a money demand function), an ARIMA model 
takes these structures as “black boxes” and simply analyzes the correlation 
pattern of a variable’s movements over time in order to forecast it. Examples 
of such ARIMA forecasts are stock market price predictions created by 
brokerage analysts based entirely on past patterns of the movement of the 
stock price.
8. For more on this topic, see Chapters 12–14 in Robert S. Pindyck and Daniel L. Rubinfeld, 
Econometric Models and Economic Forecasts (New York: McGraw-Hill, 1998).


457
  ARIMA Models
Any forecasting technique that ignores independent variables also essen-
tially ignores all potential underlying theories except those that hypothesize 
repeating patterns in the variable under study. Since we have emphasized 
the advantages of developing the theoretical underpinnings of particular 
equations before estimating them, why would we advocate using ARIMA? 
The answer is that the use of ARIMA is appropriate when little or nothing is 
known about the dependent variable being forecasted, when the indepen-
dent variables known to be important really cannot be forecasted effectively, 
or when all that is needed is a one- or two-period forecast. In these cases, 
ARIMA has the potential to provide short-term forecasts that are superior 
to more theoretically satisfying regression models. ARIMA models are par-
ticularly well suited to forecast a system that has not undergone a profound 
structural change within the sample or forecasting period. In such a situation, 
a naïve ARIMA model often can beat a moderately sophisticated economet-
ric model in terms of forecasting outside the sample and has come close to 
the performance of state-of-the-art macro models in terms of forecasting key 
macro variables.9 In addition, ARIMA can sometimes produce better expla-
nations of the residuals from an existing regression equation (in particular, 
one with known omitted variables or other problems). This introduction to 
ARIMA is intentionally brief; a more complete coverage of the topic can be 
obtained from a number of other sources.10
The ARIMA approach combines two different specifications (called processes) 
into one equation. The first specification is an autoregressive process (hence the 
AR in ARIMA), and the second specification is a moving average (hence the MA).
An autoregressive process expresses a dependent variable Yt as a func-
tion of past values of the dependent variable. This is similar to the serial 
correlation error term function of Chapter 9 and to the dynamic model of 
Chapter 12. If we have p different lagged values of Y, the equation is often 
referred to as a “pth-order” autoregressive process.
A moving-average process expresses a dependent variable Yt as a func-
tion of past values of the error term. Such a function is a moving average of 
past error term observations that can be added to the mean of Y to obtain a 
moving average of past values of Y. If we used q past values of e, we’d call it a 
qth-order moving-average process.
9. Charles R. Nelson, “The Ex Ante Prediction Performance of the St. Louis and FRB-MIT-PENN 
Econometric Models and Some Results of Composite Predictors,” Journal of Money, Credit and 
Banking, Vol. 7, No. 1, pp. 1–32.
10. See, for example, Chapters 15–19 in Robert S. Pindyck and Daniel L. Rubinfeld, Econometric 
Models and Economic Forecasts (New York: McGraw-Hill, 1998).


458
Chapter 15  Forecasting
To create an ARIMA model, we begin with an econometric equation with 
no independent variables 1Yt = β0 + et2 and add to it both the autoregres-
sive and moving-average processes:
	
autoregressive process
	
Yt = β0 + θ1Yt-1 + θ2Yt-2 + g+ θpYt-p + et	
(15.15)
+ ϕ1et-1 + ϕ2et-2 + g+ ϕqet-q
	
moving-average process
where the θs and the ϕs are the coefficients of the autoregressive and moving-
average processes, respectively, and p and q are the number of past values 
used of Y and e, respectively.
Before this equation can be applied to a time series, however, it must be 
ensured that the time series is stationary, as defined in Section 12.5. If a series 
is nonstationary, then steps must be taken to convert the series into a station-
ary one before the ARIMA technique can be applied. For example, a nonsta-
tionary series can often be converted into a stationary one by taking the first 
difference of the variable in question:
	
Y*t = ∆Yt = Yt - Yt-1	
(15.16)
If the first differences do not produce a stationary series, then first differences 
of this first-differenced series can be taken.11 The resulting series is a second-
difference transformation:
	
Y t** = ∆Y*t = Y*t - Y*t-1 = ∆Yt - ∆Yt-1	
(15.17)
In general, successive differences are taken until the series is stationary. The 
number of differences required to be taken before a series becomes stationary is 
denoted with the letter d. For example, suppose that GDP is increasing by a fairly 
consistent amount each year. A plot of GDP with respect to time would depict 
a nonstationary series, but a plot of the first differences of GDP might depict a 
fairly stationary series. In such a case, d would be equal to 1 because one first 
difference was necessary to convert the nonstationary series into a stationary one.
The dependent variable in Equation 15.15 must be stationary, so the Y in that 
equation may be Y, Y*, or even Y**, depending on the variable in question.12 
11. For variables that are growing in percentage terms rather than absolute amounts, it often 
makes sense to take logs before taking first differences.
12. If Y in Equation 15.15 is Y*, then β0 represents the coefficient of the linear trend in the 
original series, and if Y is Y**, then β0 represents the coefficient of the second-difference trend 
in the original series. In such cases—for example, Equation 15.19—it’s not always necessary 
that β0 be in the model.
g
g


459
  Summary
If a forecast of Y* or Y** is made, then it must be converted back into Y terms 
before its use; for example, if  d = 1, then
	
YNT+1 = YT + YN*T+1	
(15.18)
This conversion process is similar to integration in mathematics, so the “I” 
in ARIMA stands for “integrated.” ARIMA thus stands for AutoRegressive 
Integrated Moving Average. (If the original series is stationary and d therefore 
equals 0, this is sometimes shortened to ARMA.)
As a shorthand, an ARIMA model with p, d, and q specified is usually 
denoted as ARIMA (p,d,q) with the specific integers chosen inserted for p, d, 
and q, as in ARIMA (2,1,1). ARIMA (2,1,1) would indicate a model with two 
autoregressive terms, one first difference, and one moving-average term:
	
ARIMA12,1,12: Y*t = β0 + θ1Y*t-1 + θ2Y*t-2 + et + ϕ1et-1	
(15.19)
where Y*t = Yt - Yt-1.
It’s remarkable how very small values of p and q can model extremely rich 
dynamics.
15.4   Summary
	 1.	 Forecasting is the estimation of the expected value of a dependent 
variable for observations that are not part of the sample data set. Fore-
casts are generated (via regressions) by estimating an equation for the 
dependent variable to be forecasted, and substituting values for each 
of the independent variables (for the observations to be forecasted) 
into the equation.
	 2.	 An excellent fit within the sample period for a forecasting equation 
does not guarantee that the equation will forecast well outside the 
sample period.
	 3.	 A forecast in which all the values of the independent variables are 
known with certainty is called an unconditional forecast, but if one 
or more of the independent variables have to be forecasted, it is a 
conditional forecast. Conditional forecasting introduces no bias 
into the prediction of Y (as long as the X forecasts are unbiased), 
but increased forecast error variance is unavoidable with conditional 
forecasting.


460
Chapter 15  Forecasting
	 4.	 If the coefficients of an equation have been estimated with GLS (to 
correct for pure first-order serial correlation), then the forecasting 
equation is:
YNT+1 = ρNYT + βN 011 - ρN2 + βN 11XN T+1 - ρNXT2
	
	 where ρ is the autocorrelation coefficient rho.
	 5.	 Forecasts are often more useful if they are accompanied by a confi-
dence interval, which is a range within which the actual value of the 
dependent variable should fall a given percentage of the time (the 
level of confidence). This is:
YNT+1 ± SFtc
	
	 where SF is the estimated standard error of the forecast and tc is the 
critical two-tailed t-value for the desired level of confidence.
	 6.	 ARIMA is a highly refined curve-fitting technique that uses current 
and past values of the dependent variable (and only the dependent 
variable) to produce often accurate short-term forecasts of that vari-
able. The first step in using ARIMA is to make the dependent variable 
series stationary by taking d first differences until the resulting trans-
formed variable has a constant mean and variance. The ARIMA(p,d,q) 
approach then combines an autoregressive process (with θ1Yt-1 terms) 
of order p with a moving-average process (with ϕ1et-1 terms) of order 
q to explain the dth differenced dependent variable.
EXERCISES
(The answers to the even-numbered exercises are in Appendix A.)
	 1.	 Write the meaning of each of the following terms without referring 
to the book (or your notes), and compare your definition with the 
version in the text for each.
a.	ARIMA (p. 456)
b.	autoregressive process (p. 457)
c.	 conditional forecast (p. 450)
d.	forecasting (p. 444)
e.	 leading indicator (p. 450)
f.	 MAPE (p. 446)
g.	moving-average process (p. 457)
h.	RMSE (p. 446)
i.	 unconditional forecast (p. 450)


461
Exercises
	 2.	 Calculate the following unconditional forecasts:
a.	the median price (PR) of a new single-family house in 2014, given 
the fact that the U.S. GDP in 2014 was roughly $17,400 billion and 
the following equation:
PRt = 12,928 + 17.08GDPt
b.	the expected level of check volume at three possible future sites for 
new Woody’s restaurants, given Equation 3.4 and the following 
data. If you could only build one new eatery, in which of these 
three sites would you build (all else equal)?
Site
Competition
Population
Income
Richburgh
6
  58,000
38,000
Nowheresville
1
  14,000
27,000
Slick City
9
190,000
15,000
	 3.	 To understand the difficulty of conditional forecasting, use Equa-
tion 1.19 to forecast the weights of the next three males you see, using 
your estimates of their heights. (Ask for actual values after finishing.)
	 4.	 Some of the most interesting applications of econometric forecasting 
are in the political arena. Examples of regression analysis in politics 
range from part-time marketing consultants who help local candi-
dates decide how best to use their advertising dollars to a fairly rich 
professional literature on U.S. presidential elections.13
	
	   In 2008, Haynes and Stone14 added to this literature with an article 
that specified (among others) the following equation:
VOTEi = β0 + β1Pi + β21DUR*P2i + β31DOW*P2i + β41GROWTH*P2i
+ β51INFLATION*P2i + β61ARMY*P2i + β71SPEND*P2i + ei
	
	
(15.20)
13. See, particularly, the work of Ray Fair: “The Effect of Economic Events on Votes for President,” 
Review of Economics and Statistics, Vol. 60, pp. 159–173, and “Econometrics and Presidential 
Elections,” Journal of Economic Perspectives, Vol. 10, pp. 89–102.
14. Stephen Haynes and Joe Stone, “A Disaggregate Approach to Economic Models of Voting 
in U.S. Presidential Elections: Forecasts of the 2008 Election,” Economics Bulletin, Vol. 4, No. 28 
(2008), pp. 1–11.


462
Chapter 15  Forecasting
where:	
VOTEi
 = the Democratic share of the popular two-
party presidential vote
	
Pi
 = 1 if the incumbent is a Democrat and -1 
if the incumbent is a Republican
	
DURi
 = the number of consecutive terms the 
incumbent party has held the presidency
	
DOWi
 = the annual rate of change in the Dow 
Jones Industrial Average between January 
and October of the election year
	
GROWTHi
 = the annual percent growth of real per cap-
ita GDP in the second and third quarters 
of the election year
	
INFLATIONi = the absolute value of the annualized infla-
tion rate in the two-year period prior to 
the election
	
ARMYi
 = the annualized percent change of the pro-
portion of the population in the armed 
forces in the two-year period prior to the 
election
	
SPENDi
 = the annualized percentage change in 
the proportion of government spending 
devoted to national security in the two-
year period prior to the election
a.	What kind of variable is P? Is it a dummy variable? If not, what is it?
b.	The authors specified their equation as a series of interaction vari-
ables between P and the other variables of interest. Look at the 
equation carefully. Why do you think that these interaction vari-
ables were required?
c.	 Using the data15 in Table 15.1 (datafile = ELECTION15) estimate 
Equation 15.20 for the years 1916–1996.
d.	Create and test appropriate hypotheses on the coefficients of your 
estimated equation at the 5-percent level. Do any of the coefficients 
have unexpected signs? Which ones?
e.	 Create unconditional forecasts for the years 2000 and 2004 and 
compare your forecasts with the actual figures in Table 15.1. How 
did you do?
15. These data are from Haynes and Stone, ibid., p. 10, but similar tables are available from a 
variety of sources, including: fairmodel.econ.yale.edu/vote2008/pres.txt.


463
Exercises
f.	 The authors wrote their article before the 2008 election. Create an 
unconditional forecast for that election using the data in Table 15.1. 
Who did the model predict would win? How did the model do?
Table 15.1  Data for the Presidential Election Exercise
YEAR
VOTE
P
DUR
DOW
GROWTH
INFLATION
ARMY
SPEND
1916
51.682
1
1
12.00
6.38
7.73
2.33
4.04
1920
36.119
1
2
-23.50
-6.14
8.01
-107.60
11.24
1924
41.756
-1
1
6.00
-2.16
0.62
-3.38
-23.05
1928
41.240
-1
2
31.30
-0.63
0.81
-0.48
10.15
1932
59.140
-1
3
-25.00
-13.98
10.01
-2.97
-37.56
1936
62.458
1
1
24.90
13.41
1.36
7.60
28.86
1940
54.999
1
2
-12.90
6.97
0.53
16.79
8.33
1944
53.774
1
3
9.00
6.88
1.98
53.10
17.16
1948
52.370
1
4
6.30
3.77
10.39
-38.82
-86.56
1952
44.595
1
5
-1.80
-0.34
2.66
43.89
71.59
1956
42.240
-1
1
2.40
-0.69
3.59
-9.93
-14.34
1960
50.090
-1
2
-13.90
-1.92
2.16
-4.10
-8.44
1964
61.344
1
1
15.80
2.38
1.73
-3.68
-5.88
1968
49.596
1
2
10.00
4.00
3.94
0.06
6.28
1972
38.210
-1
1
5.40
5.05
5.17
-11.91
-19.71
1976
51.050
-1
2
3.00
0.78
7.64
-2.56
-20.15
1980
44.697
1
1
12.40
-5.69
8.99
-1.37
-0.44
1984
40.830
-1
1
-6.90
2.69
3.68
-0.22
7.38
1988
46.070
-1
2
12.60
2.43
3.30
-1.58
-1.09
1992
53.455
-1
3
-0.90
1.34
3.15
-7.33
-10.11
1996
54.736
1
1
24.54
3.08
1.95
-5.62
-12.67
2000
50.265
1
2
-5.02
2.95
1.80
-2.00
1.83
2004
48.586
-1
1
-8.01
3.49
2.50
-0.51
14.91
2008
?
-1
2
30.70
2.10
3.70
-0.87
0.41
Source: Stephen Haynes and Joe Stone, “A Disaggregate Approach to Economic Models  
of Voting in U.S. Presidential Elections: Forecasts of the 2008 Election,” Economics Bulletin, 
Vol. 4, No. 8 (2008), p. 10.
Datafile = ELECTION15


464
Chapter 15  Forecasting
	 5.	 Suppose you have been given two different ARIMA (1,0,0) fitted time-
series models of the variable Yt:
Model A: Yt = 15.0 + 0.5Yt-1 + et
Model T: Yt = 45.0 - 0.5Yt-1 + et
where et is a normally distributed error term with mean 0 and stan-
dard deviation equal to 1.
a.	The final observation in the sample (time period 06) is  Y06 = 31. 
Determine forecasts for periods 07, 08, and 09 for both models.
b.	Suppose you now find out that the actual Y07 was equal to 33. 
Revise your forecasts for periods 08 and 09 to take the new infor-
mation into account.
c.	 Based on the fitted time series and your two forecasts, which model 
(model A or model T) do you expect to exhibit smoother behavior? 
Explain your reasoning.
