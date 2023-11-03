
## Principles
1. Human safety first, robot safety second
2. Leave the robot as you would want to find it (be aware of who is next, and try to leave it as they would prefer it)
3. Know what to do, before you have to do it
4. Be prepared for things that can come up
5. Maintaining the robot is part of using it
6. Understanding the robot is key to using it safely
7. The operator is responsible for bystanders
	1. Do not assume that bystanders understand the robot - make them aware
8. Share your experiences so we all learn from them
9. Think as a community of robot users


## Rules

Each rule should be actionable - but also have a rationale/intent (so it can be interpreted later).
Bold for "decisions to think about"

1. The spot should not be touched (even taken out of the box, or moved if its out of the box) unless an "authorized operator" is present.
	1. Some one who understand the robot - and what can go wrong, and how to deal with the contingencies - should be present in case something happens.
	2. It is important that someone who knows not only the "robot" (how to operate it safely) but also our protocols (how to be polite to future users, how to care for the battery,) is there to make sure the protocols are followed
	3. Even if the robot is powered off, there is the possibility for danger to people (pinch points when carrying it), the robot (banging it, caring for the battery)
	4. **What happens when we need to move the robot and no one is around (it is on the floor, and we need to use the space for something else)**
2. There should always be two people present when the spot is used. (only one needs to be an authorized operator)
	1. Some things (putting the spot into the box, moving it while powered off) require two people
	2. If something happens (someone gets hurt) we need someone to get help
	3. **Exceptions - allow for uses with 1 person, when doesn't require moving robot**
3. Every use of the spot should be logged
	1. We need to keep track of usage so we can account for it, and we need to be able to trace back to when things were OK to figure out when problems occured.
4. When you begin a spot session, the operator should inspect the robot to make sure there is no damage. (**this is probably in the BD startup procedures - maybe this should be "follow the BD procedures"** - BD steps are too general) - make sure we have set procedures
	1. don't use robot without must have written (hard copy) procedures handy which includes "cheat sheet" 
5. The batteries must be removed at the end of the session. **look into - maybe it's OK to leave on shore power**
	1. This is very critical- batteries can be ruined by leaving them in the robot.
	2. "I am leaving it in the robot because I expect to come back in a few minutes" leads to problems if you get interrupted and don't come back to it. 
6. At the end of the session, the spot should be ... ??? 
	1. **I don't know this answer to this, but we should have a policy**
	2. Put back in the box? 
		1. pro: the next person might want to move it, in which case it will be an unpleasant surprise; and they might not have a helper to help with boxing; because it takes 2 people to take it out of the box, it helps enforce #2; keeps the lab clean; keeps dust/dirt out of the robot.
		2. con: it's more effort for the next usage, which will mean things get used less; it's wear and tear lifting it; lifting it is a "dangerous operation" (easy to bang people or robot); nice to have the robot out as a showpiece
	3. Put in a "good" floor location?
	4. Only leave the spot out if you expect the next user to want it out in that location, and within the next 36 hours **???**
	5. **Look ahead at the schedule**
7. At the end of the session, the batteries should be...
	1. **I am not sure - but we need to decide when to recharge. It is bad to come to the robot and find the batteries too low for use, but I am not sure we want to keep cycling them**
	2. **The policy should also involve taking the batteries off charge when it done**
8. At the end of the session, the controller should be recharged. ~~if it has less than 3 hours of battery life left. It is the responsibility of the person of the user not only to charge the battery when they are done, but also to take the controller off charging when it is done charging (or confirming that the next user has done so).~~
	1. When someone comes to use the robot, they should expect the controller to be charged enough to outlast the robot batteries.
9. **We need to consider scheduling - reserving the robot and priorities**
10. **Follow the official BD guidance**
11. All operators are required to stay "current" with announcements in the "spot" slack channel. 
12. Do not make software updates unless you are explicitly authorized to do so. If you do make updates, schedule it at a time that works well for others - do not do it in the midst of an experiment (so that different parts of an experiment are done with different software versions). (exceptions for things that are urgent)
13. **We need to think about how to "maintain" the batteries (make sure they get recharged periodically)**
14. Even if you use one battery, be sure to check the other as well.
15. If you "modify" the robot (attach a payload, hook something to the gripper, ...) - **should you take it off or not**
	1. understanding who is using it next, and leave the robot how they are likely to want it
16. Don't use the robot unless you have enough time to "clean up" properly 
17. Operators are allowed (encouraged?) to become part of the BD online support community, however, someone should not make an "official support request" unless "authorized". If you make a support request, inform the channel.
	1. We have had problems in the past where multiple communications with a vendor got things confused. If you want to ask them something, (1) make sure that someone else hasn't already asked (2) let everyone else know that you have asked and (3) keep everyone else informed.
18. You should understand the 2 meter rule well enough to know why/when it is OK to violate it.

Return tools to spot
Have spot tools

Things that are probably 

The reality of the 2 meter rule...
BD says "stay 2 meters away". This is often impractical. A more realistic rule: a person should only be within 2 meters of the robot if they are paying close attention to it. They should only be closer to it if they are pretty confident they know what the robot will do (and are paying close attention). This is still not "safe" - since the robot could decide it needs to take a few quick steps to rebalance itself at any time. But if you have knowledge of the robot "i understand it's rebalancing" and what it is doing "it's just standing there" and awareness "but I'm still keeping my eyes on it to make sure it doesn't decide to step towards me" - it's probably OK.

## Notes for the BD Stuff
1. Preparing for Spot
2. As an operator, you should know the pinch points (and other safety things)
3. The roll over stuff still applies with the arm - it's just that the robot goes on its side, not completely on its back
4. The "battery maintanance section" is not "optional" (but it is OK to skim - be aware)
5. With the readings we should distinguish "read carefully", "be aware of" and "optional"


Because Spot batteries are Lithium Ion (access the [Spot Battery Safety Data Sheet (SDS)](https://support.bostondynamics.com/s/article/Spot-Battery-SDS) here) we recommend developing battery safety, charging and storage policies that align with the local and state regulations regarding batteries of this type. If your business has a Safety Officer, this may be a good place to start.

You may want to consider assigning a designated area for battery charging and overnight storage. Here, you could clearly post your policies around battery charging, safety and storage for the benefit of your team and those working within your facility. More information on battery safety and storage will follow in this _Getting Started with Spot_ series.

Read this again:
Always remove the battery when Spot is not in use unless the robot is connected to shore power or sitting on a powered Spot Dock (even if the robot is powered off). Batteries left in the robot while not in use will continue to discharge, even when the robot is powered off. Batteries left in a robot for more than 24 hours may be damaged beyond repair.

