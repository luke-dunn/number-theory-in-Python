# Modular Symmetry and Primitive Roots – 2025-05-07

## 1. Initial Observations

### 1.1. Simple Modulo Behavior
- Noted that \( 8^k \mod 7 = 1 \) for all \( k \), since \( 8 \equiv 1 \mod 7 \)
- Observed that \( 9 \mod 7 = 2 \), so \( 9^k \mod 7 = 2^k \mod 7 \)

### 1.2. Power Cycles
- Created tables and visualizations of power cycles for bases mod 7
- Noticed full-cycle behavior for some bases (like 3 and 5 mod 7)
- Identified repeating sequences and their lengths

---

## 2. Primitive Roots

### 2.1. Definition
A **primitive root mod \( p \)** (where \( p \) is prime) is a number \( r \) such that:
\[
r^k \mod p \text{ for } k = 1 \text{ to } p-1
\]
produces **all nonzero residues mod \( p \)**.

### 2.2. Findings for mod 7
- Primitive roots: **3 and 5**
- Other residues: form smaller, repeating subgroups
- Verified this visually and numerically

---

## 3. Visualizations

### 3.1. Polar Plots
- Polar graphs showed symmetry in primitive root cycles
- Full cycles drew perfect n-gons
- Subgroup elements created broken orbits or short loops

### 3.2. Cayley Graphs
- Built directed graphs showing residue mappings under \( x \mapsto rx \mod m \)
- Primitive roots gave single long cycles
- Non-roots led to fragmented graphs

---

## 4. Mathematical Structure

### 4.1. Euler’s Theorem
\[
a^{\phi(n)} \equiv 1 \mod n \quad \text{for } \gcd(a,n)=1
\]
- When \( n \) is prime, \( \phi(n) = n-1 \)
- This generalizes Fermat’s Little Theorem

### 4.2. Growth of \( \phi(n) \)
- \( \phi(n) \) grows slower than \( n \)
- Composite numbers have **smaller** \( \phi(n) \), meaning **fewer coprime residues**

---

## 5. Primitive Root Conditions

### 5.1. Primitive Roots Exist Only For:
\[
n = 2,\ 4,\ p^k,\ 2p^k \quad \text{(with odd prime } p)
\]
- Primes like 7, 11, 13 → Yes
- Composites like 8, 10, 12, 15 → No

### 5.2. Importance
- Primitive roots show **cyclic group** structure
- Foundation for cryptography and group theory

---

## 6. Hamiltonian Tours and Orbits

### 6.1. Hamiltonian ≠ Primitive
- Noted that many Hamiltonian tours exist
- Only some come from **power sequences**
- Others are permutations, not group generators

---

## 7. Almost Roots

### 7.1. Defined as:
\[
a^{k} \equiv 1 \mod n \quad \text{with } k = \phi(n) - 1
\]
- “Almost primitive roots” get close but don’t complete the group
- Useful for studying subgroup structure and testing limits of cyclicity

### 7.2. Your Code Evolution
- Initial function checked for full residue sets
- Improved version now tracks **order of appearance**
- Helps identify almost roots and visualize orbit length

---

## 8. Composite Moduli

### 8.1. Challenges
- \( \mathbb{Z}_n^\times \) is not always cyclic
- Use **Carmichael function \( \lambda(n) \)** instead of \( \phi(n) \)

### 8.2. Behavior
- Some composites (like \( 9, 25, 49 \)) have primitive roots
- Most do not
- Groups may decompose into smaller cyclic components

---

## 9. Philosophical Insights

- Modular arithmetic shows **hidden symmetry in finite sets**
- Primitive roots act like **rotors**, generating entire systems from one seed
- Subgroups and almost roots express **internal tensions** in these systems
- There’s aesthetic satisfaction in watching a modular orbit close perfectly
- This is not just number theory—it’s **structured motion in arithmetic space**

---

## 10. Next Steps

- Explore more visuals of modular spirals and group actions
- Build a markdown notebook of residue patterns, orbits, and orders
- Investigate discrete logarithms and cryptographic implications
- Study Carmichael lambda function in more detail
- Reflect on group theory and cyclicity from abstract algebra viewpoint

