# Game-Theoric model of a slashing mechanism for all

## Strategies and Payoffs
In this model, we'll try to introduce a slashing mechanism for everyone when the task fail. We'll first consider that everyone is slashed the same amount and try to find out what should the slash amount to. If this is not satisfying, we'll then try to slash a different amount to each actor.  

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

P<sub>r</sub>: Requester payoff  
P<sub>a</sub>: Assets provider payoff  
P<sub>c</sub>: Computing provider payoff  

U<sub>r</sub>: Utility from the result  

Price<sub>a</sub>: Asset price  
Price<sub>c</sub>: Computing price  
Cost<sub>c</sub>: Computing cost  

Slash<sub>r</sub>: Requester slash   
Slash<sub>a</sub>: Asset provider slash   
Slash<sub>c</sub>: Computing provider slash   

We consider that "utility from the result" is strictly positive, hence P<sub>r</sub> > Total Cost.  

We also consider that the payoff for ruining someone else can be mapped as the maximum value that you can get someone in the system to loose.

## Payoff Matrix and Nash Equilibria of Naïve Setting


We'll write payoffs in the following way: (P<sub>r</sub>, P<sub>a</sub>, P<sub>c</sub>)

Requester chooses S:  
|Asset / Computer| S | F |
|--|--|--|
| **S** | (U<sub>r</sub> - (Price<sub>a</sub> + Price<sub>c</sub>) , Price<sub>a</sub> , Price<sub>c</sub> - Cost<sub>c</sub> ) | (-Slash<sub>r</sub> , -Slash<sub>a</sub>, -(Cost<sub>c</sub> + Slash<sub>c</sub>)) |
| **F** | (-Slash<sub>r</sub>, -Slash<sub>a</sub>, -(Cost<sub>c</sub> + Slash<sub>c</sub>)) | (-Slash<sub>r</sub>, -Slash<sub>a</sub>, -(Cost<sub>c</sub> + Slash<sub>c</sub>)) |

Requester chooses F:  
|Asset / Computer| S | F |
|--|--|--|
| **S** | (-Slash<sub>r</sub>, -Slash<sub>a</sub>, -(Cost<sub>c</sub> + Slash<sub>c</sub>)) | (-Slash<sub>r</sub>, -Slash<sub>a</sub>, -(Cost<sub>c</sub> + Slash<sub>c</sub>)) |
| **F** | (-Slash<sub>r</sub>, -Slash<sub>a</sub>, -(Cost<sub>c</sub> + Slash<sub>c</sub>)) | (-Slash<sub>r</sub>, -Slash<sub>a</sub>, -(Cost<sub>c</sub> + Slash<sub>c</sub>)) |

These matrices show the payoffs for the Requester and Assets Provider based on their strategies.  

After working on each matrix independently, we compare both matrices cell by cell and underline the best payoff for the requester.  

From these, we can see that the pure Nash Equilibria are:  
(S, S, S)  
(S, F, F)  
(F, S, F)  
(F, F, S)  
(F, F, F)  

## Payoff Matrix and Nash Equilibria of Malicious Setting
We'll write payoffs in the following way: (P<sub>r</sub>, P<sub>a</sub>, P<sub>c</sub>)

Requester chooses S:  
|Asset / Computer| S | F | R |
|--|--|--|--|
| **S** | (U<sub>r</sub> - (Price<sub>a</sub> + Price<sub>c</sub>), Price<sub>a</sub>, Price<sub>c</sub> - Cost<sub>c</sub>) | (-Slash<sub>r</sub>, 0, -Cost<sub>c</sub>-Slash<sub>c</sub>) | (0, 0, 0-Cost<sub>c</sub>-Slash<sub>c</sub>) |
| **F** | (0, 0, -Cost<sub>c</sub>-Slash<sub>c</sub>) | (0, 0, -Cost<sub>c</sub>-Slash<sub>c</sub>) | (0, 0, 0-Cost<sub>c</sub>-Slash<sub>c</sub>) |
| **R** | (0, Cost<sub>c</sub>+Slash<sub>c</sub>, -Cost<sub>c</sub>-Slash<sub>c</sub>) | (0, Cost<sub>c</sub>+Slash<sub>c</sub>, -Cost<sub>c</sub>-Slash<sub>c</sub>) | (0, Cost<sub>c</sub>+Slash<sub>c</sub>, 0-Cost<sub>c</sub>-Slash<sub>c</sub>) |

Requester chooses F:  
|Asset / Computer| S | F | R |
|--|--|--|--|
| **S** | (0, 0, -Cost<sub>c</sub>-Slash<sub>c</sub>) | (0, 0, -Cost<sub>c</sub>-Slash<sub>c</sub>) | (0, 0, 0-Cost<sub>c</sub>-Slash<sub>c</sub>) |
| **F** | (0, 0, -Cost<sub>c</sub>-Slash<sub>c</sub>) | (0, 0, -Cost<sub>c</sub>-Slash<sub>c</sub>) | (0, 0, 0-Cost<sub>c</sub>-Slash<sub>c</sub>) |
| **R** | (0, Cost<sub>c</sub>+Slash<sub>c</sub>, -Cost<sub>c</sub>-Slash<sub>c</sub>) | (0, Cost<sub>c</sub>+Slash<sub>c</sub>, -Cost<sub>c</sub>-Slash<sub>c</sub>) | (0, Cost<sub>c</sub>+Slash<sub>c</sub>, 0-Cost<sub>c</sub>-Slash<sub>c</sub>) |

Requester chooses R:  
|Asset / Computer| S | F | R |
|--|--|--|--|
| **S** | (Cost<sub>c</sub>+Slash<sub>c</sub>, 0, -Cost<sub>c</sub>-Slash<sub>c</sub>) | (Cost<sub>c</sub>+Slash<sub>c</sub>, 0, -Cost<sub>c</sub>-Slash<sub>c</sub>) | (Cost<sub>c</sub>+Slash<sub>c</sub>, 0, 0-Cost<sub>c</sub>-Slash<sub>c</sub>) |
| **F** | (Cost<sub>c</sub>+Slash<sub>c</sub>, 0, -Cost<sub>c</sub>-Slash<sub>c</sub>) | (Cost<sub>c</sub>+Slash<sub>c</sub>, 0, -Cost<sub>c</sub>-Slash<sub>c</sub>) | (Cost<sub>c</sub>+Slash<sub>c</sub>, 0, 0-Cost<sub>c</sub>-Slash<sub>c</sub>) |
| **R** | (Cost<sub>c</sub>+Slash<sub>c</sub>, Cost<sub>c</sub>+Slash<sub>c</sub>, -Cost<sub>c</sub>-Slash<sub>c</sub>) | (Cost<sub>c</sub>+Slash<sub>c</sub>, Cost<sub>c</sub>+Slash<sub>c</sub>, -Cost<sub>c</sub>-Slash<sub>c</sub>) | (Cost<sub>c</sub>+Slash<sub>c</sub>, Cost<sub>c</sub>+Slash<sub>c</sub>, 0-Cost<sub>c</sub>-Slash<sub>c</sub>) |

These matrix shows the payoffs for the Requester, Assets providers and Computing providers based on their strategies.

The Nash Equilibria for those payoffs matrix are as follow:  
TODO  

## Conclusion

TODO  