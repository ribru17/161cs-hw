# 1

Prove equivalence between $P \Rightarrow \lnot Q, Q \Rightarrow \lnot P$ and $P
\Leftrightarrow \lnot Q, (P \land \lnot Q) \lor (\lnot P \land Q)$

We use $P \Rightarrow Q \equiv \lnot P \lor Q$ and $P \Leftrightarrow Q \equiv
(P \Rightarrow Q) \land (Q \Rightarrow P)$

**Pair 1**

| $P$ | $Q$ | $\lnot P \lor \lnot Q$ | $\lnot Q \lor \lnot P$ |
| --- | --- | ---------------------- | ---------------------- |
| F   | F   | T                      | T                      |
| F   | T   | T                      | T                      |
| T   | F   | T                      | T                      |
| T   | T   | F                      | F                      |

Thus they are equivalent due to the commutative property!

**Pair 2**

| $P$ | $Q$ | $(\lnot P \lor \lnot Q) \land (Q \lor P)$ | $(P \land \lnot Q) \lor (\lnot P \land Q)$ |
| --- | --- | ----------------------------------------- | ------------------------------------------ |
| F   | F   | F                                         | F                                          |
| F   | T   | T                                         | T                                          |
| T   | F   | T                                         | T                                          |
| T   | T   | F                                         | F                                          |

Thus these pairs are equivalent as well!

# 2

**1.**

$(Smoke \Rightarrow Fire) \Rightarrow (\lnot Smoke \Rightarrow Fire)
\longrightarrow (\lnot Smoke \lor Fire) \Rightarrow (Smoke \lor Fire)
\longrightarrow \lnot(\lnot Smoke \lor Fire) \lor (Smoke \lor Fire)
\longrightarrow (Smoke \land \lnot Fire) \lor (Smoke \lor Fire) \longrightarrow
(Smoke \lor Smoke \lor Fire) \land (\lnot Fire \lor Smoke \lor Fire)
\longrightarrow (Smoke \lor Fire) \land (True) \longrightarrow Smoke \lor Fire$

| Smoke | Fire | $Smoke \lor Fire$ |
| ----- | ---- | ----------------- |
| F     | F    | F                 |
| F     | T    | T                 |
| T     | F    | T                 |
| T     | T    | T                 |

Thus the sentence is neither unsatisfiable nor valid.

**2.**

$(Smoke \Rightarrow Fire) \Rightarrow ((Smoke \lor Heat) \Rightarrow Fire)
\longrightarrow (\lnot Smoke \lor Fire) \Rightarrow (\lnot (Smoke \lor Heat)
\lor Fire) \longrightarrow \lnot(\lnot Smoke \lor Fire) \lor (\lnot (Smoke \lor
Heat) \lor Fire) \longrightarrow (Smoke \land Fire) \lor ((\lnot Smoke \land
\lnot Heat) \lor Fire) \longrightarrow (\lnot Smoke \land \lnot Heat) \lor Fire$

| Smoke | Fire | Heat | $(\lnot Smoke \land \lnot Heat) \lor Fire$ |
| ----- | ---- | ---- | ------------------------------------------ |
| F     | F    | F    | T                                          |
| F     | F    | T    | F                                          |
| F     | T    | F    | T                                          |
| F     | T    | T    | T                                          |
| T     | F    | F    | F                                          |
| T     | F    | T    | F                                          |
| T     | T    | F    | T                                          |
| T     | T    | T    | T                                          |

This sentence is also neither unsatisfiable nor valid.

**3.**

$((Smoke \lor Heat) \Rightarrow Fire) \Leftrightarrow ((Smoke \Rightarrow Fire)
\lor (Heat \Rightarrow Fire)) \longrightarrow (\lnot (Smoke \lor Heat) \lor
Fire) \Leftrightarrow (\lnot Smoke \lor Fire\lor \lnot Heat) \longrightarrow
(\lnot(\lnot (Smoke \lor Heat) \lor Fire) \lor (\lnot Smoke \lor Fire\lor \lnot
Heat)) \land (\lnot(\lnot Smoke \lor Fire\lor \lnot Heat)\lor (\lnot (Smoke \lor
Heat) \lor Fire)) \longrightarrow (Smoke \land Heat) \lor (\lnot Smoke \land
\lnot Heat) \lor Fire$

| Smoke | Heat | Fire | $(Smoke \land Heat) \lor (\lnot Smoke \land \lnot Heat) \lor Fire$ |
| ----- | ---- | ---- | ------------------------------------------------------------------ |
| F     | F    | F    | T                                                                  |
| F     | F    | T    | T                                                                  |
| F     | T    | F    | F                                                                  |
| F     | T    | T    | T                                                                  |
| T     | F    | F    | F                                                                  |
| T     | F    | T    | T                                                                  |
| T     | T    | F    | T                                                                  |
| T     | T    | T    | T                                                                  |

This sentence is neither unsatisfiable nor valid.

# 3

- Mythical: $A$
- Mortal: $B$
- Mammal: $C$
- Horned: $D$
- Magical: $E$

$A \Rightarrow \lnot B, \lnot A \Rightarrow B \land C, (\lnot B \lor C)
\Rightarrow D, D \Rightarrow E$

$\lnot A \lor \lnot B, A \lor (B \land C), (B \land \lnot C) \lor D, \lnot D
\lor E$

$(\lnot A \lor \lnot B) \land (A \lor B) \land (A \lor C) \land ((B \land \lnot
C) \lor D) \land (\lnot D \lor E)$

$(\lnot A \lor \lnot B) \land (A \lor B) \land (A \lor C) \land (B \lor D) \land
(\lnot C \lor D) \land (\lnot D \lor E)$

Examining the first two clauses of this knowledge base we see $(\lnot A \lor
\lnot B) \land (A \lor B)$ which is an XOR gate meaning a unicorn is mythical
only when it is immortal, and if it is immortal it is not mythical. The unicorn
can be proven to be magical if it is horned. It is horned if it is immortal or a
mammal.

# 4

- Figure 1
  - Decomposable? Yes: all `AND` gates are fed clauses of independent variables
    that don't overlap
  - Deterministic? No: All **CHILD** `OR` gates are deterministic, however the
    **root** `OR` node **CAN** have both branches of the `OR` evaluate to true
    thus it is not deterministic overall.
  - Smooth? No: Some of the child `OR`s have inputs of different variables, e.g.
    one `OR` gate has input $C$ and then $\lnot C \land \lnot D$
- ## Figure 2
  - Decomposable? Yes: All `AND` gates are fed clauses of independent variables
    that don't overlap
  - Deterministic? No: Not every `OR` node has children that are inconsistent
  - Smooth? Yes: Every `OR` gate has children that are made up of the same set
    of variables

# 5
