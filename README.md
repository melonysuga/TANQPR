### Termination Analysis of Nondeterministic Quantum Programs Revisited

#### Introduction

Verifying quantum programs has attracted a lot of interest in recent years. In this paper, we consider the termination problem of quantum programs
with nondeterminism.
To analyze termination effectively, we over-approximate the reachable set of quantum program states by the reachable subspace,
which has an explicit algebraic structure.
Compared with the counterpart in existing literature, our reachable subspace is more precise and can be computed in polynomial time.
We illustrate the algebraic method via a running example --- the quantum Bernoulli factory protocol.
Moreover, we study the set of divergent states from which the program terminates with probability zero under some scheduler. By exploiting the algebraic structure of the divergent set, we develop an effective approach using the existential theory of the reals.
The complexity is shown, for the first time, to be in exponential time.

​	This repository is the Python implementation for algorithms introduced in "Termination Analysis of NondeterministicQuantum Programs Revisited". The prototypes of Algorithms have been implemented in the Wolfram language on Mathematica 11.3 with Intel Core i5-10700 CPU at 2.90GHz.  All the functions required  for analyzing the termination of a nondeterministic quantum program are listed as follows.

- **Initialization.nb**

  initializes a nondeterministic program with given information about super-operators, projective measurement and an input state by the example in the paper "Termination Analysis of Nondeterministic Quantum Programs Revisited";

- **ReachableSpaceI.nb**

  computes the I-reachable subspace w.r.t. an input state and return an orthonormal basis of that subspace of Hilbert space;

- **ReachableSpaceII.nb**

  computes the II-reachable subspace w.r.t. an input state and return a linearly independent basis of that subspace of Hermitian operators on Hilbert space;

  	+ **LinearIndepHerm**
  	
    checks whether a Hermitian operator can be linearly expressed by the current linearly independent basis;

- **DivergentSet.nb**

  computes the set of pure divergent states from which the given nondeterministic quantum program terminates with probability zero under some scheduler;
  
   + **SpaceUnionNull** checks whether the union of subspaces is null;
   + **SpaceUnionEqual**  checks whether two unions of subspaces are equal;
   + **PDSpace**  computes the subspace of all pure divergent states under a given scheduler;
   + **ISpaceIntersectEmpty**  (resp.  **IISpaceIntersectEmpty**) checks whether the I-reachable (resp. II-reachable) subspace is disjoint with the set of pure divergent states.

​        After fixing the dimension of the Hilbert space, a nondeterministic quantum programs, and an input state, one can invoke the algorithms by calling the above functions respectively.

​       Generally, the functions in the files **ReachableSpaceI.nb** and **ReachableSpaceII.nb**  are efficient as their theoretical complexity is **PTIME**. They take time 16ms, 15ms and space 104.40MB, 103.51MB, respectively on the running example. Those in the file **divergentSet.nb**  may be inefficient (in the worst case), due to the fact that the quantifier elimination and the derivation of the pure divergent set by a tree construction are both  **EXPTIME**. However, it fortunately takes time 2797ms and space 105.91MB on the running example.

**How to replicate the example?**

We have provided Wolfram Mathematica 12.0 with a graphical interface in the VM. Our code supports mathematica 11.3 and above.

If you have Wolfram Mathematica for windows, you can directly operate the .nb files provided in wolframcode file. 

Note that the code of windows and linux versions are slightly different in the position of storing initial data.

frontend

1. Calculate I-type Reachable Space:

    Open the file  ``` /home/vmcai/Desktop/TANQPR/wolf/ReachableSpaceI.nb```, selcet the content in the first cell (if confused, see detailed in wolfram language) and run it (shift+enter), then the result is displayed at the end of the file.

2. Calculate II-type Reachable Space:

    Open the file ```/home/vmcai/Desktop/TANQPR/wolf/ReachableSpaceII.nb```, selcet the content in the first cell (if confused, see detailed in wolfram language) and run it (shift+enter), then the result is displayed at the end of the file.

3. Calculate Pure Divergent Set:

   Open the file ```/home/vmcai/Desktop/TANQPR/wolf/DivergentSet.nb```, selcet the content in the first cell (if confused, see detailed in wolfram language) and run it (shift+enter), then enter the basis of subspace according to the output. The example input in the paper is as follows.
   
   Round 1: For actions  \alpha_1, enter the basis:

   ```mathematica
   {{0, 0, 0, 1}, {1/Sqrt[2], 0, -(1/Sqrt[2]), 0}}
   ```

   Round 2: For actions  \alpha_2, enter the basis:

   ```mathematica
   {{1, 0, 0, 0}, {0, 0, 1/Sqrt[2], 1/Sqrt[2]}}
   ```

   Round 3: For actions \alpha_1\alpha_1, enter the basis:

   ```mathematica
   {{0, 0, 0, 1}, {1/Sqrt[2], 0, -(1/Sqrt[2]), 0}}
   ```

   Round 4: For actions  \alpha_1\alpha_2, enter the basis:

   ```mathematica
   {{-1, 0, Sqrt[2]/Sqrt[3], Sqrt[2]/Sqrt[3]}}
   ```

   Round 3: For actions  \alpha_2\alpha_2, enter the basis:

   ```mathematica
   {{1, 0, 0, 0}, {0, 0, 1/Sqrt[2], 1/Sqrt[2]}}
   ```

   Then the run ends, and the result is displayed at the end of the file.
   
