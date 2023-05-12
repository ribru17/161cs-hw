# 1

1. $\theta = \{x / A, y / x, z / B\}$
2. This is not unifiable since we need $y / G(x, x)$ and $y / G(A, B)$. This
   would mean we need $x / A$ and $x / B$ which is not possible.
3. $\theta = \{x / B, y / A\}$
4. $\theta = \{x / y, y / John$
5. These expressions are not unifiable since we need $x / y$ and $x /
   Father(y)$. $Father(y)$ and $y$ are different expressions and thus $x$ cannot
   necessarily be both of them at the same time, so this is not a unifiable pair
   of sentences.

# 2

## 1.

- $\forall x : Food(x) \Rightarrow Likes(John, x)$
- $Food(Apple)$
- $Food(Chicken)$
- $\forall x \forall y : Eats(x, y) \land \lnot KilledBy(x, y) \Rightarrow
  Food(y)$
- $\forall x \forall y : KilledBy(x, y) \Rightarrow \lnot Alive(x)$
- $Eats(Bill, Peanuts) \land Alive(Bill)$
- $\forall x : Eats(Bill, x) \Rightarrow Eats(Sue, x)$

## 2.

First step

- $\forall x : \lnot Food(x) \lor Likes(John, x)$
- $Food(Apple)$
- $Food(Chicken)$
- $\forall x \forall y : \lnot(Eats(x, y) \land \lnot KilledBy(x, y)) \lor
  Food(y)$
- $\forall x \forall y : \lnot KilledBy(x, y) \lor \lnot Alive(x)$
- $Eats(Bill, Peanuts) \land Alive(Bill)$
- $\forall x : \lnot Eats(Bill, x) \lor Eats(Sue, x)$

Next step

- $\lnot Food(x) \lor Likes(John, x)$
- $Food(Apple)$
- $Food(Chicken)$
- $\lnot(Eats(x, y) \land \lnot KilledBy(x, y)) \lor Food(y)$
- $\lnot KilledBy(x, y) \lor \lnot Alive(x)$
- $Eats(Bill, Peanuts) \land Alive(Bill)$
- $\lnot Eats(Bill, x) \lor Eats(Sue, x)$

Next step

- $\lnot Food(x) \lor Likes(John, x)$
- $Food(Apple)$
- $Food(Chicken)$
- $\lnot Eats(x, y) \lor KilledBy(x, y) \lor Food(y)$
- $\lnot KilledBy(x, y) \lor \lnot Alive(x)$
- $Eats(Bill, Peanuts) \land Alive(Bill)$
- $\lnot Eats(Bill, x) \lor Eats(Sue, x)$

Done

## 3.

**TO PROVE:** $Likes(John, Peanuts)$

1. $\lnot Food(x) \lor Likes(John, x)$
2. $Food(Apple)$
3. $Food(Chicken)$
4. $\lnot Eats(x, y) \lor KilledBy(x, y) \lor Food(y)$
5. $\lnot KilledBy(x, y) \lor \lnot Alive(x)$
6. $Eats(Bill, Peanuts) \land Alive(Bill)$
7. $\lnot Eats(Bill, x) \lor Eats(Sue, x)$
8. $\lnot KilledBy(Bill, Peanuts)$ **FROM:** 5, 6
9. $Food(Peanuts)$ **FROM:** 4, 6, 8
10. $Likes(John, Peanuts)$ **FROM:** 1, 9

Done

## 4.

1. $\lnot Food(x) \lor Likes(John, x)$
2. $Food(Apple)$
3. $Food(Chicken)$
4. $\lnot Eats(x, y) \lor KilledBy(x, y) \lor Food(y)$
5. $\lnot KilledBy(x, y) \lor \lnot Alive(x)$
6. $Eats(Bill, Peanuts) \land Alive(Bill)$
7. $\lnot Eats(Bill, x) \lor Eats(Sue, x)$
8. $Eats(Sue, Peanuts)$ **FROM:** 6, 7

## 5.

Here we cannot prove what Sue eats, only that she eats something. We know this
at the very least since we know that Bill is alive, and if you don't eat you
die, and thus if you don't eat you are not alive. However Bill is alive thus it
is not the case that he doesn't eat, thus we know Bill does eat. However we no
longer know he eats peanuts so we know nothing about what he eats. We only know
$\exists x : Eats(Bill, x)$ and $\forall x : Eats(Bill, x) \Rightarrow Eats(Sue,
x)$ thus $\exists x : Eats(Sue, x)$.
