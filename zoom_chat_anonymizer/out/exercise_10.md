**14:15:39**, *Student 0*: yes

**14:34:01**, *Student 0*: yes

**14:34:01**, *Student 1*: yes

**14:43:37**, *Student 2*: These practical exercises are really awesome - probably my favourite part of the lecture. Nevertheless, are they - and if so, to what extent - relevant for the exam?

**14:48:11**, *Student 3*: @Student 2: similar to other practical exercises, tools, commands, and techniques are not relevant. But the concepts behind those are. For example, last exercise about malware we played a bit with repackaging of Android apps with arbitrary malicious payloads. We expect you to understand what is repackaging, what are its dis/advantages, why is it used to implement malware, why is it possible to repackage apps, etc. But you won't be asked: which tool can be used to disassemble or decompile an Android app? Or what does this command do?

**14:49:35**, *Student 2*: Alright, thanks!

**14:49:36**, *Student 3*: ... here's maybe a rule of thumb: questions that you might be asked in a job interviews are irrelevant to the exam. We're operating on a more conceptual level. :)

**15:08:25**, *Student 3*: Yup

**15:08:30**, *Student 1*: 1fps yes

**15:14:04**, *Student 2*: On the lecture slides it was stated that “Resilience is an important quality attribute of detection algorithms”. Against what (which attacks?) should they be resilient? Simply against variations of malicious activities (<-> obfuscation & evasion techniques)?

**15:20:59**, *Student 3*: @Student 2: I would personally say that "resilience" in this context refers t
o the ability of the detection algorithm to withstand attacks against the algori
thm itself. For example, let us say you overwhelm the algorithm with network tra
ffic to analyze and look through it pursuit of anomalous behavior, would it cras
h? would it be so slow that an attack can go through? how would the algorithm an
d its process recover, if at all? etc.

**15:21:45**, *Student 3*: ... the ability to detect different variations is more of a "generalization" property and is concerned with attacks against the system being monitored rather than the detection algorithm itself.

**15:21:54**, *Student 3*: Does it make any sort of sense?

**15:22:50**, *Student 2*: It’s slightly different to what I had in mind, but it definitely makes sense as well.

**15:24:29**, *Student 3*: @Student 2: I am looking at it from the perspective of adversarial ML. But resilience is usually context-specific. So, we'll get back to you after checking what Thomas thinks.

**15:24:47**, *Student 2*: Thanks a lot!

