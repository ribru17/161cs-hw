# 1

We know that $Pr(A,B) = Pr(A)Pr(B)$ and $Pr(A|B) = Pr(A)$ if $A$ and $B$ are
independent. We also know $Pr(A,B) = Pr(A|B)Pr(B)$. If we set $Pr(A) =
Pr(\alpha_1)$ and $Pr(B) = Pr(\alpha_2,\ldots,\alpha_n)$ then we can reach
$Pr(\alpha_1,\ldots,\alpha_n) =
Pr(\alpha_1|\alpha_2,\ldots,\alpha_n)Pr(\alpha_2,\ldots,\alpha_n)$ and thus
$Pr(\alpha_1,\ldots,\alpha_n|\beta) =
Pr(\alpha_1|\alpha_2,\ldots,\alpha_n|\beta)Pr(\alpha_2,\ldots,\alpha_n|\beta)$.
Recursively applying this logic on the second probability,
$Pr(\alpha_2,\ldots,\alpha_n|\beta)$, we reach the final result that
$Pr(\alpha_1,\ldots,\alpha_n|\beta) = Pr(\alpha_1|\alpha_2, \ldots, \alpha_n,
\beta)Pr(\alpha_2|\alpha_3,\ldots,\alpha_n,\beta)\ldots Pr(\alpha_n|\beta)$.
