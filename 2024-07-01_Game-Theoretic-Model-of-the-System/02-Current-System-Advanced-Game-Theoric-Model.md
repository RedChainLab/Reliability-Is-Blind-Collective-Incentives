# Advanced Game-Theoretic Model for the current system

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

## Payoff Matrix
We'll write payoffs in the following way: (P<sub>r</sub>, P<sub>a</sub>, P<sub>c</sub>)

<u>Requester chooses S:</u>  
|Asset / Computer| S | F | R |
|--|--|--|--|
| **S** | (<u>U<sub>r</sub> - (Price<sub>a</sub> + Price<sub>c</sub>)</u>, <u>Price<sub>a</sub></u>, <u>Price<sub>c</sub> - Cost<sub>c</sub></u>) | (0, 0, <u>-Cost<sub>c</sub>-Slash<sub>c</sub></u>) | (0, 0, <u>0-Cost<sub>c</sub>-Slash<sub>c</sub></u>) |
| **F** | (0, <u>0</u>, -Cost<sub>c</sub>-Slash<sub>c</sub>) | (0, <u>0</u>, <u>-Cost<sub>c</sub>-Slash<sub>c</sub></u>) | (0, <u>0</u>, <u>0-Cost<sub>c</sub>-Slash<sub>c</sub></u>) |
| **R** | (0, <u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, -Cost<sub>c</sub>-Slash<sub>c</sub>) | (0, <u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, <u>-Cost<sub>c</sub>-Slash<sub>c</sub></u>) | (0, <u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, <u>0-Cost<sub>c</sub>-Slash<sub>c</sub></u>) |

<u>Requester chooses F:</u>  
|Asset / Computer| S | F | R |
|--|--|--|--|
| **S** | (0, <u>0</u>, -Cost<sub>c</sub>-Slash<sub>c</sub>) | (0, <u>0</u>, -Cost<sub>c</sub>-Slash<sub>c</sub>) | (0, <u>0</u>, <u>0-Cost<sub>c</sub>-Slash<sub>c</sub></u>) |
| **F** | (0, <u>0</u>, -Cost<sub>c</sub>-Slash<sub>c</sub>) | (0, <u>0</u>, -Cost<sub>c</sub>-Slash<sub>c</sub>) | (0, <u>0</u>, <u>0-Cost<sub>c</sub>-Slash<sub>c</sub></u>) |
| **R** | (0, <u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, -Cost<sub>c</sub>-Slash<sub>c</sub>) | (0, <u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, -Cost<sub>c</sub>-Slash<sub>c</sub>) | (0, <u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, <u>0-Cost<sub>c</sub>-Slash<sub>c</sub></u>) |

<u>Requester chooses E:</u>  
|Asset / Computer| S | F | R |
|--|--|--|--|
| **S** | (Cost<sub>c</sub>+Slash<sub>c</sub>, <u>0</u>, -Cost<sub>c</sub>-Slash<sub>c</sub>) | (<u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, <u>0</u>, -Cost<sub>c</sub>-Slash<sub>c</sub>) | (<u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, <u>0</u>, <u>0-Cost<sub>c</sub>-Slash<sub>c</sub></u>) |
| **F** | (<u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, <u>0</u>, -Cost<sub>c</sub>-Slash<sub>c</sub>) | (<u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, <u>0</u>, -Cost<sub>c</sub>-Slash<sub>c</sub>) | (<u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, <u>0</u>, <u>0-Cost<sub>c</sub>-Slash<sub>c</sub></u>) |
| **R** | (<u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, <u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, -Cost<sub>c</sub>-Slash<sub>c</sub>) | (<u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, <u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, -Cost<sub>c</sub>-Slash<sub>c</sub>) | (<u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, <u>Cost<sub>c</sub>+Slash<sub>c</sub></u>, <u>0-Cost<sub>c</sub>-Slash<sub>c</sub></u>) |

These matrix shows the payoffs for the Requester, Assets providers and Computing providers based on their strategies.

## Nash Equilibria
TODO