**14:22:09**, *Student 0*: 4.1a) Why does obfuscation only protect against MATE attackers? If someone reverse engineers a protocol, doesn’t that make MITM attacks easier?

**14:23:57**, *Student 0*: Yes thank you

**14:36:19**, *Student 1*: just from a functionality point of view: you write code test whether the code does waht it is supposed to do then obfuscate it and then test again if the functionality is still given? Or do you only test the code after the obfuscation?

**14:37:43**, *Student 2*: @Student 1: Well, I would say you should test the version you ship out to customers. If that's the obfuscated version, then that's the one you should test, especially since we want to test whether obfuscated software undermines the stability/functionality of the software.

**14:38:31**, *Student 3*: but wouldn't a functionality Change after obfuscating the program hint a bug in your obfuscator? I mean in Theory it should create the exact same outcome

**14:38:31**, *Student 2*: You can also isolate the functionality of the software by testing it BEFORE obfuscation. But again that does not help much if your functionality works fine but after obfuscation it does not.

**14:39:27**, *Student 2*: @Student 3: Functionality should, theoretically, NOT change. Defining "functional equivalence" is tough, I think. But usually it is in terms of same inputs == same outputs.

**14:40:03**, *Student 2*: Or did I? :)

**14:40:23**, *Student 1*: yes thanks

**14:41:08**, *Student 4*: where did that | operator in the last slide come from? I've mistaken with the binary or operator in C

**14:41:19**, *Student 3*: is virtualization a common Approach? Does every cpu support virtualization by default

**14:42:28**, *Student 2*: @Student 4: I'll relay that to Sebastian.

**14:43:18**, *Student 2*: @Student 3: I think it is, because in this case, you are creating a new instruction set altogether which does not have standard. Effectively, you are forcing the attacker to understand your instruction sets.

**14:44:10**, *Student 2*: But, in my opinion, runtime analysis of the program bypasses all of that because at the end the instructions will have to be translated to the underlying architecture (e.g., AMD)

**14:44:49**, *Student 2*: So, just run the program and monitor, for example, the system/API calls it makes. Or even the instructions if you have to go that low-level.

**14:44:56**, *Student 3*: so Dumping the process from Memory would most likely get rid of virtualized instructions, unless they are re-encrypted after execution?

**14:45:40**, *Patrick Stöckle*: @Student 4: In this formula, $$|$$ was denoting the `is divisible by` operator. [https://en.wikipedia.org/wiki/Divisor](https://en.wikipedia.org/wiki/Divisor)

**14:46:00**, *Student 2*: @Student 3: depends on how and when the virtualized instructions are translated, I think. If it is Student 3ust-in-Time compilation, then maybe not.

**14:47:12**, *Student 4*: thanks!

**14:47:33**, *Student 2*: @Student 3: That is: in memory you'll have an instruction like "my_move register_1, 5" in memory which still needs to be translated to e.g. mov eax, 5

**14:47:56**, *Student 2*: Runtime analysis (i.e., right before or after the instruction has been executed) should bypass that.

**14:48:22**, *Patrick Stöckle*: @Student 4: $$3|x*(x + 1)*(x + 2), \forall x \in Z \Leftrightarrow x*(x + 1)*(x + 2) mod 3 \equiv 0, \forall x \in \mathbb{Z}$$

**14:49:20**, *Student 3*: yeah i guess you could also emulate the execution with something like the unicorn engine and analyze it? single stepping every instruction or hooking vm_exit (i think vmp uses it?) sounds like a hussle

**14:50:58**, *Student 2*: @Student 3: Well, the more sophisticated the obfuscation, the more sophisticated/annoying the RE. :)

**14:53:51**, *Student 5*: this looks like a very long exercise task. Could a task this long occur in the exam?

**14:54:19**, *Student 5*: regarding the virtualization obfuscation

**14:55:11**, *Student 2*: @Student 5: No, most probably not.

**14:58:39**, *Student 6*: question: since `f2` is only 4 slots long, and the 5th sloth in `f1` and `f3` is similar, why can't the 4th slots in T be `0xef`? **Answered by Sebastian**

**14:58:51**, *Student 4*: why can't `0xef` put in 4?

**14:59:02**, *Student 6*: some wrong index-names, sorry

**15:00:32**, *Student 7*: are there compilers/ tools that help optimizing functions for creating such a template? **Answered by Sebastian**

**15:01:44**, *Student 7*: yeah thanks

**15:16:21**, *Student 8*: is it plausible that a service like ob24 would charge depending on transaction values instead of some kind of monthly rate? **Answered by Patrick**

