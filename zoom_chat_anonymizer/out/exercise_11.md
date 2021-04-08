**14:19:32**, *Student 0*: Not related to Fuzzing: Do we have to be able to perform a Padding Oracle Attack for the exam?

**14:31:31**, *Patrick Stöckle*: @Student 0: I haven’t thought about this so far but this is a nice idea for an exam exercise ;) Jokes aside: If we asked you to perform a POA, we would provide you with the necessary formulas. We don’t expect that you are able to derive the formula, i.e., $P_i[n] = \oplus P_i[n]' \oplus C_i[n]' \oplus C_{i-1}[n]$ we used to crack the plain text from the CBC definition and we don’t expect that you learn the formula by heart.

**14:34:01**, *Student 1*: Also not about fuzzing: Would you say that Single Sign On (e.g. google, Facebook, etc.) violates the security principle of Least Common Mechanism?

**14:35:06**, *Student 0*: Thanks!

**14:40:33**, *Patrick Stöckle*: @Student 1: I just looked up the original definition of the principle and based on this, I would say: yes, it’s violated by SSO. For SSO, I would argue with the principle that mechanisms have to be economically reasonable and the psycholog. In most of the cases

**14:42:32**, *Patrick Stöckle*: and the psychological acceptability. In most of the cases, it’s more economical to move the password handling and authorisation to the SSO provider instead of implementing — and maybe messing it up — by ourselves. Furthermore, it might be more acceptable for the users to sign in with their Google account instead of creating a new password. Does this answer your question?

**14:43:16**, *Student 1*: Absolutely, thanks for the effort!

**15:36:06**, *Student 0*: If you’re interested in Web App pentesting, definitely check out intercepting proxies like OWASP ZAP.

**15:36:28**, *Student 2*: please keep more space between last tutorial and exam in the future. I have exams today, tomorrow and so on already.

