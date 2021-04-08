**14:14:00**, *Student 0*: yes

**14:14:01**, *Student 1*: ping

**14:14:02**, *Student 2*: ping

**14:14:03**, *Student 3*: works

**14:14:04**, *Student 4*: pong

**14:17:59**, *Student 5*: y

**14:21:00**, *Student 6*: Will there by programming assignments? Or hacking experiences?

**14:21:11**, *Student 0*: will Solutions of exercises be published as pdf?

**14:21:40**, *Student 7*: The solutions are already on moodle

**14:21:44**, *Student 8*: Yes, there will be hands-on exercises, in which you get to hack vulnerable systems.

**14:22:02**, *Student 8*: +1: The solutions will be posted online.

**14:22:12**, *Student 8*: Along with a recording of the tutorial.

**14:23:51**, *Student 9*: Can you please a lot upload the chat log (as some questions asked in chat are answered as text), thus it doesn’t appear in video recordings. I am referring both to lecture as well as tutorial session.

**14:24:41**, *Student 8*: I think you can save the chat log.

**14:24:42**, *Student 10*: The lecture Chats are on moodle

**14:25:35**, *Student 8*: There's a button on the top-right corner of your typing space that allows you to (a) send files, and (b) save chat. And the lecture chats should be on moodle, as well. :)

**14:26:14**, *Student 11*: would privacy not also deal with misuse of personal data by the data processor? like an app using personal data in a way the user did not consent to? (not necessary leaking it)

**14:26:19**, *Student 12*: Ignore the file, I tried to save the chat :D

**14:27:13**, *Student 13*: Isn't a Confidentiality violation also a Privacy violation? e.g if my password is violated, chances are that also my personal data will be violated

**14:28:20**, *Student 8*: @Student 11 + Student 13: Yes, sure. The moral of this comparison is to make the distinction between confidentiality and privacy in terms of their relation to your "personal" data.

**14:28:43**, *Student 8*: For example, your address or gender are more related to "private" information.

**14:28:57**, *Student 8*: However, leaking them is indeed a matter of violating confidentiality.

**14:29:13**, *Student 8*: So, there's a decent overlap between both concepts when it comes to the secrecy of information.

**14:29:52**, *Student 8*: But the primary distinction we attempt to make is vis-a-vis their relationship to the user.

**14:30:03**, *Student 8*: Does it make sense?

**14:30:28**, *Student 14*: If I say that both safety and security want to keep a harmless condition, but they work in two different directions(one is inside--> outside, the other the opposite), is it correct?

**14:30:29**, *Student 15*: what is vis-a-vis?

**14:30:33**, *Student 16*: would this be a satisfactory answer for Question b):

Difference: Security is about preventing attacks from outside the systems (external). Safety is about preventing faulty behavior from within the system.
 Similarity: Both try to prevent unintended behavior of a system and the potentially resulting harmful consequences. Both try to protect the
integrity of the system.

**14:30:34**, *Student 13*: I think so,
Privacy is related to personal data, while Confidentiality to information relative to the user

**14:31:01**, *Student 8*: @Student 13: Correct.

**14:31:14**, *Student 8*: @Student 15: vis-a-vis == with regard to

**14:32:01**, *Student 8*: @Student 14 + Student 16: The main difference here is having an adversary/attacker that deliberately attacks the system.

**14:32:27**, *Student 8*: The Boeing 737 MAX issues were faults == related to safety.

**14:32:54**, *Student 8*: But if someone deliberately crashes a plane (e.g., German wings crash), that's security.

**14:33:13**, *Student 8*: Defending both issues sometimes overlap. But the difference is in the intention, so to speak.

**14:38:32**, *Student 17*: Typo, “now” used instead of “know”.

**14:38:52**, *Student 8*: @Student 17: Thanks :)

**14:40:54**, *Student 7*: does it not also depend on the user of the system? and as humans are involved, the uncertainty will always prevail ?

**14:42:45**, *Student 5*: y

**14:42:45**, *Student 2*: ping

**14:42:45**, *Student 1*: yes

**14:42:46**, *Student 15*: <

**14:43:38**, *Student 8*: @Student 7: It absolutely does, good point. Hence, it can never be 100% secure.

**14:44:16**, *Student 12*: But is it a system flaw if a user leakes for example a password?

**14:44:29**, *Student 12*: I would say no

**14:45:16**, *Student 8*: @Student 12: Good question. That depends on what you define as a system. If you include users in this, then the "system" is not secure. Usually, you try to accommodate for such scenarios.

**14:45:39**, *Student 8*: But at some point, you cannot do a lot to maintain the security of the system. It just turns into "damage control"

**14:46:14**, *Student 8*: If your admin goes rogue and decides to drop your databases, maybe you can try to do backups and give access to different admins.

**14:46:23**, *Student 8*: If all of them go rogue, we're screwed! :D

**14:49:18**, *Student 12*: The slides seem to be cut off on the right, or is it just me?

**14:49:25**, *Student 18*: Same for me

**14:49:25**, *Student 15*: true

**14:49:28**, *Student 19*: can confrim

**14:49:31**, *Student 13*: Slightly on the bottom too

**14:51:13**, *Student 20*: How are Fail-Safe Defaults and Implicit Deny related? I don’t see why they are combined in one principle

**14:51:16**, *Student 13*: If a database transaction fails/is interrupted and is "restored" to a default, is that considered a fail-safe default?

**14:53:06**, *Student 15*: khoa

**14:53:08**, *Student 17*: Why: Negative Example: Blacklisting of ports/websites, where we implicitly deny some ports being open instead of by default being open ?

**14:53:08**, *Student 15*: oops

**14:53:53**, *Student 8*: @Student 20: "The Principle of Fail-Safe Defaults states that, unless a subject is given explicit access to an object, it should be denied access to that object." == implicit deny.

**14:54:53**, *Student 8*: @Student 13: Nope, it's basically implicity deny said in a confusing manner, I have to admit.

**14:55:25**, *Student 12*: Isn’t blacklisting explicit deny?

**14:55:49**, *Student 8*: @Student 17: Blacklisting is explicit deny .. yup, exactly Korbinian.

**14:56:29**, *Student 8*: With blacklisting, you have to always add new things to block and you cannot cope. It does not scale.

**14:56:54**, *Student 8*: It's easier to say, block everything unless I allow them, which should be much smaller in number than the other way around.

**14:57:06**, *Student 8*: It's a paranoid approach. But works alright. :)

**14:57:27**, *Student 21*: So economy of mechanism tend to be beneficial for users instead of system itself?

**14:58:26**, *Student 8*: @Student 21: For both. For developers: it makes it easier to understand the system and decreases the chances of getting something wrong and maybe less secure.

**14:58:34**, *Student 7*: isn't fail-safe defaults about starting a system in a secure state and return to a secure default state in case of failures?

**14:59:08**, *Student 8*: For users: if the mechanism interfaces with users, then it should be simple == usable (e.g.,password reset module).

**15:00:26**, *Student 22*: Can you give another example for Least Common Mechanism? I'm still not sure if I understand it correctly

**15:00:44**, *Student 8*: @Student 7: I get the point. It literally sounds like that. But I actually think it is not.

**15:02:20**, *Student 8*: @Student 22: consider password policies. The harder it is, the more secure against brut-force attacks it is. But eventually users will write passwords down because they are complex, effectively undermining the security of their accounts and maybe the system.

**15:02:57**, *Student 8*: Simply put, "economy of mechanism" means that a security mechanism should be as simple as possible.

**15:04:07**, *Student 19*: @alei could you let Patrick now about the cut off slides? he could just go into presentation mode

**15:04:25**, *Student 8*: @Student 19: sure. Let me raise my hand. :)

**15:07:28**, *Student 19*: thanks

**15:07:36**, *Student 8*: Sure thing

**15:09:36**, *Student 23*: Could you please give another example for Least common mechanism, apart from 2FA as given in the solution

**15:09:37**, *Student 16*: What is "hearbleed" (p.26)?

**15:09:45**, *Student 19*: +1

**15:10:00**, *Student 5*: [https://heartbleed.com/](https://heartbleed.com/)

**15:10:51**, *Student 22*: Is Economy of Mechanism and Defense in Depth also okay as answer?

**15:11:02**, *Student 13*: Are there other possible answers to question d?

**15:11:08**, *Student 13*: Just a curiosity

**15:11:36**, *Student 12*: I would say Economy of Mechanism and Defense in Depth can create a conflict

**15:12:48**, *Student 8*: @ Student 22 + Student 12: I would say so too.

**15:13:02**, *Student 14*: aren't also least common and complete mediation incorporated?

**15:13:29**, *Student 8*: @Student 23: let me think of one example.

**15:13:51**, *Student 22*: Isn't Least common mechanism(all in one network so you can access all the resources in the same way) also one neglected principle?

**15:15:24**, *Student 8*: @Student 14: Just not to answer the wrong question. What do you mean by "incoporated". Like Least common include Complete mediation?

**15:15:52**, *Student 11*: could one not say that compartmentlaization is partially done, because wile the network is not split, duties are separated across servers? (different server for web and DB)

**15:17:28**, *Student 11*: and would "least common mechanism" not be violated as well, as both internal employees and users access over the same route + the mailserver intended for internal use is made publicly available?

**15:17:41**, *Student 14*:  @Alei I mean these two mechanisms incorporated into the system

**15:18:12**, *Student 22*: Feedback: Can Patrick Stöckle also please include the written questions? Not everyone has a microphone and I don't think you can answer the questions in Chat in an adequate and lengthy way, just because of the format

**15:21:16**, *Student 8*: @Student 11: Good point. Usually, mail servers are kept within the internal network rater than the DMZ. So, ideally, there should be separate servers to maintain the least common mechanism.

**15:22:40**, *Student 23*: It was least common mechanism

**15:24:11**, *Student 8*: @Student 14: Ah-a! Firewalls should represent complete mediation. Least common mechanism: as Felix discussed, maybe not always.

**15:24:20**, *Student 8*: @Student 23: Yup, sorry.

**15:25:21**, *Student 4*: Navy Seal Copypasta

**15:25:23**, *Student 18*: Hahaha

**15:25:27**, *Student 2*: is this a joke ?

**15:25:34**, *Student 5*: lmao

**15:25:37**, *Student 8*: Okay, I have no freaking idea what was that!! :D

**15:25:43**, *Student 4*: [https://knowyourmeme.com/memes/navy-seal-copypasta](https://knowyourmeme.com/memes/navy-seal-copypasta)

**15:25:51**, *Student 24*: mashallah brother

**15:26:06**, *Student 8*: @Student 4: thanks for the info :'D

**15:26:47**, *Student 25*: xD

**15:27:10**, *Student 23*: So if I got it right, least common mechanism is incorporated in the bank example as there are dedicated servers for the data, applications and mailing functionalities?

**15:27:34**, *Student 8*: It would be awesome if someone brute-forced this meeting's key an we're talking about "security"!

**15:28:51**, *Student 8*: @Student 23: right to a great extent. But as Felix mentioned, employees and external users using the same mailing server may violate this principle.

**15:29:28**, *Student 8*: @everyone: Obviously, this is a hypothetical architecture. So, feel free to point out any problems with it.

**15:31:13**, *Student 7*: how is compartmentalization diff from least common mechanism ?

**15:31:50**, *Student 24*: the eva articulations innit

**15:32:35**, *Student 14*: in the email, is it better to retrieve the exact name of the recipient, so that we can address the mail better and it sounds more realistic?

**15:33:17**, *Student 8*: @Student 7: Compartmentalization isolates processes/users/subjects on a need-to-know basis. So, you only have access to what you need and that's it.

**15:34:09**, *Student 8*: Least common is about access to the same resources. So, if we (as users) are perfectly isolated, there should be a wy thata we share the same resources.

**15:35:21**, *Student 8*: Obviously, users logged in to a single server share the same resources on the server (e.g., memory), but they cannot access one-another's sessions.

**15:37:05**, *Student 8*: @Student 14: Well, I guess it depends on who you're targeting. If you are targeting John Doe in particular, it would be better to include his name in he temail.

**15:37:37**, *Student 8*: Otherwise, a lot of users will be satisfied with a general email 'a la "Dear client, ... "

**15:37:49**, *Student 8*: Nowadays, automated emails are widely used anyway.

**15:39:08**, *Student 8*: Any other questions?

