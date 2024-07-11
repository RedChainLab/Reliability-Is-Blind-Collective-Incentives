# Advanced Game-Theoric Model for the current system

## Strategies and Payoffs
In this model, we'll try to introduce 1 new strategie which will be complementary to the Failure strategie. This strategie will simulate an actor being malicious and wanting to ruin another actor. As so, the payoff will not be the money that this actor can earn but the money that he can make someone loose. For that purpose we will consider that his payoff will be equal to the biggest lost among the other actors.

* **S**: Successful and honest task completion (Financial Payoff)
  * P<sub>r</sub> = U<sub>r</sub> - (Price<sub>a</sub> + Price<sub>c</sub>)
  * P<sub>a</sub> = Price<sub>a</sub>
  * P<sub>c</sub> = Price<sub>c</sub> - Cost<sub>c</sub>
* **F**: Failing task honestly
  * P<sub>r</sub> = 0
  * P<sub>a</sub> = 0
  * P<sub>c</sub> = -(Cost<sub>c</sub> + Slash<sub>c</sub>)
* **R**: Failing task to ruin another actor (Strategic Payoff)
  * P<sub>r</sub> = |min(P<sub>a</sub>, P<sub>c</sub>)|
  * P<sub>a</sub> = |min(P<sub>r</sub>, P<sub>c</sub>)|
  * P<sub>c</sub> = |min(P<sub>r</sub>, P<sub>a</sub>)| - (Cost<sub>c</sub> + Slash<sub>c</sub>)

U<sub>r</sub>: Utility from the result
P<sub>r</sub>: Requester payoff  
P<sub>a</sub>: Assets provider payoff  
P<sub>c</sub>: Computing provider payoff  
Slash<sub>c</sub>: Computing provider slash   
Price<sub>a</sub>: Asset price  
Price<sub>c</sub>: Computing price  
Cost<sub>c</sub>: Computing cost  

We consider that "utility from the result" is strictly positive, hence P<sub>r</sub> > Total Cost.  

We also consider that the payoff for ruining someone else can be mapped as the maximum value that you can get someone in the system to loose.

## Payoff Matrix and Nash Equilibria
We'll write payoffs in the following way: (P<sub>r</sub>, P<sub>a</sub>, P<sub>c</sub>)

<u>Requester chooses S:</u>  
|Asset / Computer| S | F | R |
|--|--|--|--|
| **S** | (<u>U<sub>r</sub> - (Price<sub>a</sub> + Price<sub>c</sub>)</u>, <u>Price<sub>a</sub></u>, <u>Price<sub>c</sub> - Cost<sub>c</sub></u>) | (0, 0, -Cost<sub>c</sub>-Slash<sub>c</sub>) | (0, 0, 0-Cost<sub>c</sub>-Slash<sub>c</sub>) |
| **F** | (0, 0, <u>-Cost<sub>c</sub>-Slash<sub>c</sub></u>) | (0, 0, <u>-Cost<sub>c</sub>-Slash<sub>c</sub></u>) | (0, 0, <u>0-Cost<sub>c</sub>-Slash<sub>c</sub></u>) |
| **R** | (0, <u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, <u>-Cost<sub>c</sub>-Slash<sub>c</sub></u>) | (0, <u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, <u>-Cost<sub>c</sub>-Slash<sub>c</sub></u>) | (0, <u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, <u>0-Cost<sub>c</sub>-Slash<sub>c</sub></u>) |

<u>Requester chooses F:</u>  
|Asset / Computer| S | F | R |
|--|--|--|--|
| **S** | (0, 0, <u>-Cost<sub>c</sub>-Slash<sub>c</sub></u>) | (0, 0, <u>-Cost<sub>c</sub>-Slash<sub>c</sub></u>) | (0, 0, <u>0-Cost<sub>c</sub>-Slash<sub>c</sub></u>) |
| **F** | (0, 0, <u>-Cost<sub>c</sub>-Slash<sub>c</sub></u>) | (0, 0, <u>-Cost<sub>c</sub>-Slash<sub>c</sub></u>) | (0, 0, <u>0-Cost<sub>c</sub>-Slash<sub>c</sub></u>) |
| **R** | (0, <u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, <u>-Cost<sub>c</sub>-Slash<sub>c</sub></u>) | (0, <u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, <u>-Cost<sub>c</sub>-Slash<sub>c</sub></u>) | (0, <u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, <u>0-Cost<sub>c</sub>-Slash<sub>c</sub></u>) |

<u>Requester chooses R:</u>  
|Asset / Computer| S | F | R |
|--|--|--|--|
| **S** | (Cost<sub>c</sub>+Slash<sub>c</sub>, 0, <u>-Cost<sub>c</sub>-Slash<sub>c</sub></u>) | (<u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, 0, <u>-Cost<sub>c</sub>-Slash<sub>c</sub></u>) | (<u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, 0, <u>0-Cost<sub>c</sub>-Slash<sub>c</sub></u>) |
| **F** | (<u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, 0, <u>-Cost<sub>c</sub>-Slash<sub>c</sub></u>) | (<u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, 0, <u>-Cost<sub>c</sub>-Slash<sub>c</sub></u>) | (<u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, 0, <u>0-Cost<sub>c</sub>-Slash<sub>c</sub></u>) |
| **R** | (<u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, <u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, <u>-Cost<sub>c</sub>-Slash<sub>c</sub></u>) | (<u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, <u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, <u>-Cost<sub>c</sub>-Slash<sub>c</sub></u>) | (<u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, <u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, <u>0-Cost<sub>c</sub>-Slash<sub>c</sub></u>) |

These matrix shows the payoffs for the Requester, Assets providers and Computing providers based on their strategies.

The Nash Equilibria for those payoffs matrix are as follow:  
(S, S, S)  
(R, R, S)  
(R, R, F)  
(R, R, R)  

A few questions persist:  
* Cost<sub>c</sub>+Slash<sub>c</sub> > Price<sub>a</sub> ?
* Cost<sub>c</sub>+Slash<sub>c</sub> > U<sub>r</sub> - (Price<sub>a</sub> + Price<sub>c</sub>) ?

These inequalities do not change the Nash equilibria. However, they make the R strategy a strictly dominant strategy for both Requesters and Asset providers.

## Conclusion

This system clearly shows that:  
* For honest players, the successful strategy is still Pareto superior if the inequalities are incorrect. While they may occasionally make mistakes with the F strategy, these strategies are not viable in the long term and should shift to an S strategy over time. It's important to note that there is no immediate incentive to switch quickly from an F strategy to an S strategy, as Requesters and Asset providers do not incur losses. 
* For malicious players, there is no risk in maintaining an R strategy. This strategy could even become a dominant strategy depending on the payoffs (see previous inequalities).
* For computing providers, the S strategy is weakly dominant as it always provides a payoff at least as high as other strategies or even higher when everyone is choosing S.