
english_stops = set(stopwords.words('english'))
# Retain alphabetic words: alpha_only
alpha_only = [t for t in lower_tokens if t.isalpha()]
# Remove all stop words: no_stops
no_stops = [t for t in alpha_only if t not in english_stops]

from collections import Counter
line_text = """Officer was unable to carry out an internal patrol due to not being able to unset the alarm 
Officer reported there were staff on site who had  dealt with the alarm 
Officer was unable to reset the alarm 
Officer reported that the alarm code did not work and the alarm was not set on arrival 
Attending officer advised that there still aren t any keys held for site
Officer had to put the ground bolts in as the doors have been made into electrical doors and without the bolts you can open the door from the outside 
Officer reported they were unable to set alarm due to comms loss and their fob Is no longer working with the panel as it does not respond to the fob  
Officer advised the fob would not open the doors on level 2 so they could not patrol that area 
Attending officer advised that the gates were left unlocked upon arrival
Attending officer has noted that the fencing is still broken on site  Has been reported previously 
Attending officer made an observation that the exterior gate is broken  please find photo of broken gate within job report 
Client not ready for lock up    Client will lock up later left site with static guard as instructed
Attending officer advised that no keys are held for site
The attending officer reported that on arrival he met with staff on site 
Attending officer has advised that the doors to the swimming pool and tennis courts are both broken  They ve also noted that the fire door mechanism doesn t work either 
SP carried out the SS  but staff wouldn t provide the alarm code  They advised we needed to go through Mitie 
Attending officer could not carry out the vacant property search due to the keypress where the keys are held being completely empty upon arrival
The attending officer reported that there was staff on site 
Officer reported the branch is under refurbishment 
Officer advised they were unable to unset the alarm 
Attending officer was advised by BT to only carry out external patrols 
The guard advised they were unable to secure the main door as the code to lock it was not working at first  The alarm panel show s 55 activations 
Our officer reported the alarm panel appeared to be unresponsive 
On arrival the attending officer met with staff on site 
Attending officer couldn t set alarm 
Attending officer has advised that the panel needs to be reset due to a communication loss  The alarm fob needs replacing as it has been reported broken 
The internal doors within the premise wouldn t lock/engage with the magnetic locks
The guard advised that unit 47B shutter is not fully secured  It is open about 2 5ft from the ground 
Attending officer made an observation that the rear carpark is currently fenced off  please find pictures related to this incident report on the full job report 
Attending officer made an observation that the alarm panel was showing  fault  on screen
Officer was unable to set the alarm 
Attending officer advised that the fencing is still damaged  has already been reported 
Attending officer couldn t secure the outer gate  BT was advised  Please find related picture  on job report 
The officer reported he was unable to lock the door 
Officer reported the rear loading bay was wide open upon arrival 
Attending officer had issues with access for the side gate to this premise
Attending officer reported the internal gate missing a padlock  external gates were still secure with padlocks 
Key not ready for collection 
Member of staff on site 
Officer waited  but no contractor arrived on site 
Officer spoke to David Ormsby  who advised it was the site in London that required attendance   Incorrect attendance 
The service partner has fed back that access is not needed until 4th march  scaffolding contractor called Jean who deals with any issues and said we should he coming on the 4th  not the 3rd but our job was booked in on the 3th  
The service partner attended to site but the third party was a no show  The service partner locked up and stood down
No new fob on site when officer arrived  Staff advised that they needed the old fob to reprogramme 
The service partner reports back that the hall lights are not working
The attending officer was stood down 3mins before arriving at the site  and he drove 55mins to the site 
Officer was instructed by BT security to carry out an external check only 
The guard advised that the front door handle is not returning to the correct position to close so the alarm was not setting  BT set the alarm remotely so entering the building wasn t required
The guard advised that there were staff on site 
Attending officer arrived on site to find the main gate already open 
The guard advised that the main car park gates right-hand side wheel is broken 
Attending officer has made a note that the doors censor should have a range of 2-3cms and that an engineer should be booked to fix this
The attending officer was stood down 2mins prior to arriving at site 
Officer was unable to set the alarm 
Attending officer found damaged fencing above ski
Attending officer could not leave site and secure as there was an on-site guard who stays on the premise over night
The officer reported that the third party did not arrive on site 
The officer reported that there are tools and ladders on site but no contractors were present upon arrival 
Staff working on site 
The attending officer advised that the provided code for the alarm 10717 is incorrect and the alarm cannot be set 
Our officer advised the lock up was not carried out due to staff being onsite for a meeting 
"DTE/O2 had booked this job at the wrong site 
The officer attended as the job was booked  however the on site security would not allow access 
DTE identified their error and the officer was requested to attend alternative store"
"Attending Officer to attend and check if the gate is locked and secure 
Gate to stay closed until further notice "
On arrival the attending officer met on site with Lisa the duty manager  and she advised that there was no need for our officer to attend 
"Attending Officer was unable to secure part of one gate due to known issue 
Please see photo of broken gate "
The attending Officer required a reset code 
when The officer arrived they met a security guard who had been checking the that the premises were secure when he was checking the managed to pull open the stage door and activate the alarm
"Some of the ceiling and the light fixture in the men s bathroom has fallen down 
Please see a picture of the issue "
Gate wheel is broken can be moved however scrapes across the ground leaving a gouge and needs to be replaced
"Attending Officer reported the main gates open on arrival 
Officer stated that this is the second night that the gates have been left open "
Staff on site 
The Officer has reported that Staff onsite until 0600hrs 
The attending officer arrived at site and found workers who set off the fire alarm even though it was on test on arrival  The attending officer spoke with the contractors but couldn’t find the security officer who was supposed to be on site looking after the contractors  the attending officer had a look around but couldn’t find him/her 
Attendung officer advised that there s about an inch of water found within the basement  please find picture within  no action  
Officer reported damage to gates  and are not securing
Attending Officer was unable to secure the right hand side of gate due to a faulty lock 
The guard advised there were staff on site 
"Attending Officer reported that the shutter at Kingsfield House was left open 
Please see photo "
Attending officer couldn t secure back gates due to the padlock being faulty
The officer is reporting that the door was being held open by a bin with the alarm sounding on his arrival 
Attending officer found two unauthorized vehicles in the car park
Attending Officer left the alarm unset at the instruction of BT SCC 
"Attending Officer reported:
Gates unlocked on arrival 
Damaged fencing behind a skip  known issue "
The attending officer had an issue with the mobile app while he was trying to complete the job 
The attending Officer has reported that the Cable was stacked up 
Attending officer has reported a leakage on site  please refer to pictures within job report for reference to this incident 
Offcer reported the leak that was reported by staff was a lot worse upon the patrol today 
The officer is reporting that the main gates had been left open by staff when they arrived
The officer is reporting that the copper storage gate was left open 
The attending Officer has reported that whilst conducting the Internal on the ground floor  the basement was flooded with water 
Staff and cleaners on site  External patrol only due to Covid restrictions  Car park gate is still in need of maintenance this has been reported to BT SCC
Officer reported the gates were unlocked upon arrival and there was insecure copper left on the ground 
"The guard advised that the fence panel is missing on the perimeter 
Please see the attached picture of the issue "
The attending Officer has reported that there was damaged roofing on the underpass next to the main entrance of the building 
Attending Officer was unable to secure the date due to known faulty padlock issue 
Attenidng officer made note of a faulty padlock  refer to picture in job report 
Attending officer had made the observation that large quantities of cable found outside the cable cages
Officer advised they could not secure the front gates as there is no padlock on the gates 
The attending Officer has reported that there was a guard onsite 
The officer has reported that the lock was not required as the staff on site  Sharon  advised site would be locked by staff 
The officer contacted the engineer who was unaware he was supposed to be attending the site  the engineer gave the officer a reset over the phone and confirmed the set signal at 18:55
Concierge on-site advised no action required and site is safe and secure 
Report is FYI: Staff present on arrival 
The report is to advise that by the time the job was cancelled we were almost at site 
The attending officer has reported the engineer did not turn up to site 
The attending officer has reported the contractors did not turn up to site 
On arrival the attending officer met with staff on site  and the alarm was set 
Due to current restrictions  the gate remains closed
Report is FYI - Darren Underhill  staff  on site
The revolving door is still broken and is to be left as found 
"Attending Officer was unable to secure part of one gate due to known issue 
Please see photo of broken gate "
On attending site for fire tests attending officer noticed pigeon droppings and feathers on site and on stairs   Also  heard a pigeon roosting in roof space above stairs 
Attending Officer was unable to lock site as staff were still on the radio 
"Attending Officer was unable to gain access into shopping centre 
Site security could not be reached "
Attending Officer phoned Engineer for Quote code 2850 on panel 
Attending Officer reported a bin on the 2nd floor has overflown with waste 
Attending Officer left the alarm unset at the instruction of BT SCC 
Attending Officer was unable to set the alarm as there is currently 24/7 Static Guard precense on site 
"Attending Officer reported:
Gates unlocked on arrival 
Cable left on the ground 
Damaged fencing behind a skip  known issue "
The operative advised that the barrier is broken 
"Attending Officer to conduct an External check of site 
Keys for site were left with the Static Guard on 09 02 2021  job reference J13370262  "
"Attending Officer reported some of the old boarding on one of the rear windows had been removed/damaged 
Please see photo "
Officer was unable to lock the site  as a district nurse on site 
On arrival at site - we spoke with Steve Wine   SECOM confirmed they had booked the job on the wring site 
"The attending officer reported that he was unable to find the property  He drove down the road that was on our system but couldn’t find a BT site there  
Provided address - Gedling ATE  Cavendish Road  Nottingham  Nottinghamshire  NG4 3YZ"
Mark smith on-site on arrival 
Maintenance work on the road around the building 
The attending Officer has reported that there was no Guard or Staff onsite 
The attending Officer has reported that there was no Guard or Staff onsite 
"Attending Officer to attend and check if the gate is locked and secure 
Gate to stay closed until further notice "
"Attending Officer to conduct an External check of site 
Keys for site were left with the Static Guard on 09 02 2021  job reference J13370262  "
Officer was unable to set and unset alarm panel 
Attending Officer advised that the Manager is on site and is dealing with alarm 
The Service Partner Control Room advised that an Internal check could not be completed due to the comms issues on site 
Officer attending reported there was copper cable on the ground and the front gate was unlocked  Damaged fencing on-site as previously reported 
Attending Officer was unable to secure barrier due to known issue 
No issues  Only external patrol required 
Attending Officer reported cleaners on site fogging building on arrival 
Attending Officer switched off the lights on the 1st and 2nd floors 
The operative advised that  receptionist and contractors  were already on site and had reset the alarm 
Officer advised police on site but could not find any intruder on site
"Attending Officer found that alarm was caused by a faulty sensor 
Panel would not reset "
Attending Officer had trouble locating the area of activation 
"While the officer was completing an internal patrol the fire alarm went off  
It was triggered by a neighbour carrying out building work  Unit 54  bakery "
The attending Officer has completed the Internal and external and found no signs of breaking or forced entry 
On arrival  there was a line fail for the alarm   The attending officer disarmed the alarm on arrival 
Officer attending site reported there was a health and safety issue of hand rail risk on the staircase
"Attending Officer to attend and check of gate is locked and secure 
Gate to stay closed until further notice "
The alarm fob held is not working 
The attending Officer has reported that there was a Mitie Security oniste supervising cleaners 
The attending Officer has reported that the current alarm code is incorrect and was therefore unable to unset the alarm 
"Attending Officer advised that Dr  Sue Levi was on site on arrival 
Dr  Levi stated she would be on site until approximately 0000 hours "
External gates have been locked and secured only 
The operative reported that he found 2 windows left open on arrival 
The operative was stood down as no contractor arrived 
The attending Officer has reported that the Copper gate was left open arrival 
"Attending Officer reported:
Damaged fencing behind skip - known issue 
Gates unlocked on arrival 
Cable left on ground 
Rubbish scattered over site  please see photo "
Officer advised the gates are broken and are unable to be secured 
Attending Officer was unable to secure the gates due to known fault 
The attending Officer has reported that the barrier would not go up  previously reported  but the site is still secure 
"Attending Officer was unable to gain entry past the green gates 
Officer stated that someone has left the gate pins down and they have down frozen to the ground due to the low temperature "
Issue raised in error 
The operative advised that staff were on site 
The alarm it came up with fail to set  CHUBB was contacted  
Officer arrived onsite and waited for 20 min and no one showed up  Officer also contacted AON security before leaving site 
The attending officer has reported broken panels from the ceiling of the property  The officer does not believe this is related to a break in 
No issues  Housekeeper was inside the house and was not informed that we coming for house check  External checks only 
The attending officer reported that on arrival there was staff on site 
On arrival the attending officer met with Sam the caretaker for the letting company  school 360  is on site along with other staff and security  They triggered the intruder alarm when they entered the site  Sam advised the officer that he tried to put the code many times  but the alarm was making some kind of problem and didn t accept the code or fob 
The guard advised they spoke with BT security who advised them to only do an external patrol of the site 
The panel would not allow set due to the zone being a fire door  had to call secom for an engineer 
Officer reported the gates were open upon arrival 
Unable to lock the site as security on site all night 
The attending officer advised that they did only an external patrol as they have keys for the site  but no fob or alarm codes for the alarm  Therefore  if they enter the property they will trigger the alarm and will not be able to set it 
Officer advised the padlocks for the gates are missing 
Officer was unable to reset the alarm
The guard advised that 2 contractors from Brent & Leighton were on site cleaning the extractor fans until 06:00 
Officer reported they only lock the external gates 
Officer advised they only carried out an external patrol of this site 
Officer arrived onsite for routine patrol and the fire alarm was sounding and all doors were insecure because of this  Officer had trouble setting the fire alar m at first 
Officer advised of an ongoing issue whereby the fencing is damaged 
Officer advised the gates are broken and are unable to be secured 
The guard advised that they had to apply force to secure the fire exit door at access D 
Officer advised spare keys don t open some doors 
On-site security advised that a manager had already been on site and reset the alarm 
Officer advised their alarm ode was not working 
The attending officer had been on site for over three hours waiting for an ADT engineer  He was advised by ADT that the engineer would start at 17:00 so the officer could not wait on site further 
The guard advised that they do not hold a key to reset the fire alarm panel 
The attending officer reported that there is a static security staff and have been posted on site for a 12-hour shift  They have locked and secured the building 
The attending officer reported that the main entrance barrier is damaged 
The attending officer reported that on arrival he spoke to NOC  however  they were not aware of the alarm activation and stood him down 
Attending officer found evidence from previous leakages  None of which are still running now  please find related pictures on job report 
The attending officer reported that the master key doesn t work for the maintenance cupboard 
The attending officer had an issue with the mobile app he uses to complete the reports 
The attending officer reported that there is no power to panel as work is being carried out in shop 
The attending officer reported that there is a problem with the alarm fob 
The attending officer reported that the main car park gate RHS wheel is broken 
On arrival the attending officer met with BT staff on site - Simon and Allan 
The attending officer reported that the alarm fob needs to be replaced as it is taking too long to deactivate and activate the alarm 
The attending officer was required a password from the alarm company in order to reset the alarm panel  however  our password is outdated or invalid  therefore the alarm company didn t authorize the officer 
The attending officer reported that there is staff on site working on vehicles in the unit and the roller shutter is open 
The guard advised that they had an issue with the phone camera so they were unable to take photos of the site 
The guard advised the engineer did not have ID on them 
"Attending Officer reported:
Gates unlocked on arrival 
Cable left on the ground 
Damaged fencing behind a skip  known issue "
Unable to secure the gate as its broken 
Officer advised there are building materials left in the yard 
The attending officer reported that on arrival there was staff on site 
Officer carried out an external patrol only due to it being an external cctv activation
Officer had issues trying to reset the alarm as they do not have a fob nor codes 
Officer reported there was no engineer on site to provide access to 
The attending officer found a homeless man at the doorway which has previously been reported  please find attached photos on the job report 
Unable to lock due to staff still being present on site
"Officer advised the security said they were told by mitie that another contractor was coming and they would want a key pick up around 1900 
Mitie did not inform us of this "
Attending officer had already completed a key audit so they didn t complete another today
Officer advised when he arrived on site staff were not aware of the job 
Officer advised the key was not ready to collect and would be ready for collection next week 
Officer advised the contractors did not show up for access
Officer advised the contractor did not show up for the job 
Officer advised the contractors did not show up 
Officer advised the roof has a leak which set off the fire alarm 
Officer advised he received a very hostile reception from staff on site and advised this happens every time he attends site when staff are there 
Officer advised there was a staff member who remained on site by the name of John Collier
The service partner did attend to site but they did not have the keys with them so were only able able to carry out an external patrol 0n this occasion 
The attending officer raised the incident report in error 
Office advised the padlock to managers room code has been changed and he was unaware of the new code  Also there was a fault showing on the fire pan 
Unable to secure the site due to a static officer onsite until 0700
"Attending Officer was unable to secure part of one of the car park gates due to known damage 
Please see photo "
Officer reported they were unable to locate the site and had to leave due t a fire alarm 
The attending officer reported that the main gate RHS wheel is broken 
1017 intruder W/H rear R FX first fire exit door on right hand side of second warehouse door- above door sensor is broken
The attending officer reported that there is an issue with the rear fire door - the frame come away from the wall 
The attending officer reported that there is external power outage and the main electric gates remain open 
The guard advised that there are damaged fencing on-site as previously reported  There was also rubbish on the floor outside the building 
The attending officer reported that the main gates on site are broken 
The attending officer reported that the main entrance gate was not repaired yet  It is wide open and any intruder can enter the building perimeters 
The guard advised they had to move the gate manually as it has a technical problem 
Officer reported a health and safety issue where there was an obstruction in block A on the second floor corridor 
The attending officer attended the site and waited for the engineer s arrival  however  the engineer did not arrive 
Contractors issued officer with 4 new shutter fobs 
Staff are still working on site 
Branch was closed upon the officers arrival 
The officer has reported that we do not hold an alarm fob for the store  keys however do provide access 
The officer has reported that the proxy cards were not available for collection and will be made available on Monday 1st March for collection 
The attending officer reported that there is static guard on site until 07:00 AM 
"The attending officer reported that they have no assignment instructions for the property 
There are also windows left open on site "
The guard advised that there were staff on site 
The attending officer reported that the assignment instructions did not advise about the door alarm needed to be turned off when entering the site 
The attending officer advised that there are contractors on site until 04:00 AM 
The attending officer reported that the gates are damaged 
The attending officer reported that the main grates are broken 
The guard advised that the gates on-site are broken 
The guard advised that the padlock that is for the main gate is not big enough to correctly lock 
The attending officer reported that there is excess water on the floor in the downstairs men s toilet which appears to be coming from the toilet cistern  The officer also reported that the alarm was not set and was in an alarm mode on arrival 
Officer reported the lock on the gate is broken so unable to secure the gate 
Officer reported there were unauthorised private vehicles parked on site 
The guard advised that there was a broken barrier on site  The lights on the van with the Reg LF19 ZRN were left on 
Officer report padlock missing on gate  and copper on  ground
Officer advised the wire in the bin is overflowing 
Officer advised the gates were unlocked and alarm was not set upon arrival 
The attending officer reported that there are contractors on site bailing flood water out of the basement 
officer advised the alar was not set upon arrival 
The attending officer reported that his access card is not registered for this site  they also have incorrect pin for card so unable to validate for remote access  There is also staff working on site 
The attending officer reported that on arrival he met with staff working on site - Craig and Sean
Officer advised that there is copper pipe left in the car park not secure on trailers and the main car park gate wide open so anyone could have stolen the vehicle
The attending Officer has reported thta the main gates were Unlocked on arrival 
The attending officer reported that there is an issue with the drain 
The attending officer reported that the staff left all gates unsecured before they left 
The guard had to leave the gate open due to an AA driver still been on site 
"Attending Officer advised there is a large puddle inside the door and throughout the car park 
Gates unlocked on arrival 
Cable left on ground "
The attending officer reported that the padlock on the gate is faulty  therefore the gates were left unlocked and the officer is unable to lock them 
The attending officer reported that the padlock is faulty  therefore he was unable to secure the site as per the assignment instructions 
officer advised there is a flood in the basement areas 
"The service partner does not have keys for this site 

Every attendance is still being booked as an Internal Patrol 

BT are aware the service partner carry s out an external patrol only "
The attending officer reported that their swipe access card is not active for the site  the pin code is incorrect and they were unable to validate for a remote access  There is also staff on site 
The attending officer reported that on arrival the gates were left open 
The attending officer has reported a fault on the gates 
officer reported there is n padlock on the gate so they are unable to secure the gate 
On-site security unaware of the survey and refused admittance to site 
Staff present on arrival 
Locksmith was a now show 
The report is FYI only  No zone information displayed on the panel 
The contractor was a no show 
Alarm activated by staff entering property 
"Attending Officer left revolving door unlocked as instructed by Client 
Door is currently broken "
"Attending Officer confirmed that there was a fire outside of the Next store 
Please see photos "
"Attending Officer was unable to secure the main gate 
Main gate stuck open "
Our officer reported there were new tenants on site so the check was not required 
The attending officer didn t access the premise as there aren t any alarm codes held for the premise and didn t want to trigger the alarm once entering the site 
"Attending Officer was unable to close the RHS of the Main Car Park due to known issue with broken wheel 
Please see photo "
Attending Officer to conduct an Exernal check of site for movement on CCTV 
"Attending Officer reported flooding from the river overflowing 
Flooding remains in basement 
Water is now receeding but more rain is due tonight "
Officer reported the perimeter fencing is broken  Copper cable was let on the ground 
The guard advised that the barrier is broken  This has been reported before 
The attending officer has reported travellers in the car park on site 
Attending Officer advised that there was no Guard or staff on site on arrival 
For Health & Safety officer advise due to lockdown the gate is to stay locked 
External patrol only  service partner do not hold the keys for BT site 
Officer on site reported heating is causing issues with the alarm system 
"Attending Officer was unable to close the RHS of the Main Car Park due to known issue with broken wheel 
Please see photo "
The officer had a problem with his phone and all photos from the attendance were lost 
Officer cannot secure the door as the catch will not bolt into the hole properly 
Mrs Anning asked for the alarm to be left unset her son Nick will sort on Tuesday 
"Attending Officer reported flooding from the river overflowing 
Flooding on outside of site  ground floor and basement 
Water is now receeding "
"Attending Officer reported:
Gates unlocked on arrival 
Cable left on the ground 
Damaged fencing behind a skip  known issue "
Attending Officer was unable to secure barrier due to known damage 
Attending officer did not have the codes to reset the alarm panel 
Gate open at the back  Fire door to the rear of building was open with a fire extinguisher 
Operative carried out full external as advised by BT and there were no issues at site 
The attending officer has reported staff member Mr Richard Crowk was working on site 
Security officer on site until 07 00 o clock 
External patrol only due to it being a communication fault 
"Attending Officer was unable to lock down site 
Static Guard on duty until 0630 hours "
"Attending Officer was unable to secure part of one of the car park gates due to known damage 
Please see photo "
The attending officer has reported doors 5 and 7 are chained from the inside so locking was not required 
"Attending Officer was unable to close the RHS of the Main Car Park due to known issue with broken wheel 
Please see photo "
"Attending Officer reported that a bolt had been left down on the door in question 
The area was very windy and the wind likely rocked the door "
"Attending Officer advised that there is a rodent problem on site 
There are droppings and chewed boxes "
Fire door 27A was left open 
The attending Officer has reported that the Copper-gate was left open but was secured by the Officer 
Attending Officer reported that the car park gates were open and the lights were on inside the building on arrival 
"Attending Officer reported:
Gates unlocked on arrival 
Cable left on the ground 
Damaged fencing behind a skip  known issue "
Attending Officer was unable to secure barrier due to known damage 
"The attending Officer has reported that there was no Intruder Alarm on arrival and the Fire panel was showing no obvious faults 
There was also no information of activation showing on the panel behind the reception 
The current code held  1234  for the on the assignment instructions is incorrect 
Several people were seeing in GF Offices coming in and out for cigarette break "
The attending Officer has reported that on the assignment instructions it says that an Alarm Fob is required to unset the alarm  but no Fob is held 
Attending Officer reported that the rear door was open on arrival 
Officer attending report fob does not work for all common areas   Service partner does not hold fobs for the common area 
The operative advised that the premises were already open as members of staff were on site 
The attending officer has reported a bad leak from a burst water pipe 
The operative advised that the contractor said he was unable to carry out the works as the job requires 2 people 
officer reported no contractor arrived on site  officer waited on site for over 1hr 
The attending Officer has reported that there was no power to the doors 
VSG unset the alarm for the officer 
Officer done a full external of site as officer with keys  had an issue with the vehicle
"Attending Officer was unable to secure part of one of the car park gates due to known damage 
Please see photo "
"Attending Officer was unable to close the RHS of the Main Car Park due to known issue with broken wheel 
Please see photos "
Tops of the metal posts missing 
"Attending Officer advised that Zone 1032 Goods in r/s in order to set alarm 
There are good stacked against the shutter that has most likey knocked the sensor "
Attending Officer advised that the Contractor was not on site on arrival 
Attending Officer was unable to locate any Guard or persons on site 
Attending Officer advised that no padlocks were on the gates 
"Attending Officer reported an issue with the 3rd floor ladies toilet sink tap 
Tap was found running and Officer stated that it is very hard to stop the water flow 
Please see photo and note "
Attending Officer found the ground floor Fire Exit door ajar on arrival  please see photo 
Officer attending site found a cooper cable on the ground  Officer also reported the padlock was jammed 
"Attending Officer reported:
Gates unlocked on arrival 
Cable left on ground 
Damaged fencing behind skip  known issue "
Attending Officer was unable to secure main gate due to ongoing fault issue 
Attending Officer reported that the alarm was not set on arrival 
Holes in the dry stone wall   On arrival  the main gate was wide open and there was a cable role on the ground 
Officer arrived on site and called next security who stood down the alarm as alarm had reset no further action needed
The attending officer has reported the fire door in auditorium six was blown open by the wind causing the alarm to activate 
The attending officer has reported the Chubb engineer had already attended site as contractors were on site doing refurbishment 
Officer unable to reset alarm as contractor knocked a sensor and now system needs an engineer reset 
Our officer reported that on arrival he found staff on site working 
Staff member James Rennie was on site 
Attending officer advised the main gates were open upon arrival 
The officer has reported that there is a small amount of water in the disabled toilet upstairs  the officer is unable to determine the source of the water   The officer also reports there is a fault on the fire panel  displaying Auditorium 2  low output 
"The attending officer reported the following issues on site:
- The coke machine is not working 
- No hot water in the kitchen 
- The roof is leaking a little 
- The fire panel is showing faults "
Coke machine not working 
Coke machine is not working and there is no hot water  Faults also showing on the fire panel 
Water leak from ceiling 
The attending officer has advised there is a leak in the back of house area 
All drinks finished in coke machine
attending officer arrived on site to find one of the alarm panels showing general faults 
The officer reported the coke towers were not required to run as per their assignement instructions  there was no water in the taps  there were faults on the fire alarm panel which ABCA are aware of  the code provided does not work for the door attached in the photo  there is no hot water in the tap located in the toilet in the screens area and the water pressure is low 
The operative was unable to verify if the CCTV is working 
The operative advised that the beverage machine was not working and the intruder panel was faulty 
The attending officer discovered major leaks on the top floor which has proceeded to go further down on to the lower floors  he stated the lower floors had wet carpets but the top floor has water filling  up to about ankle-high
Officer advised they were unable to set alarm as they believed the system lost power 
The attending officer reported that the internal glass panel is broken
The attending officer reported that he is required to lock the external doors only 
Officer advised he had to take a fob from the keysafe in order to leave the site and that there was one building that they were unable to gain access to as they do not have an alarm code for it 
Officer advised the alarm went into tamper and required engineers assistance to reset 
The attending officer reported that the door is stuck open 
The attending officer reported that he was sent to the wrong property 
The attending officer waited on-site for 30 minutes with no sign of contractor arriving on-site
Attending officer came across a cat inside school grounds  Wasn t entirely sure if the cat belonged to the school or not  Could be the reason behind the activation
The guard advised that one of the glass panel s on the door was shattered  as seen pictured  
Attending officer reporting major water leak on the top level  water is leaking through via the roof with the level of water near to ankle height causing damage to the floor below 
The officer reported that the engineer required access to another site  not the site it was booked for 
officer done full external no issues to report
The attending officer advised that there is static security officer M  Ahmed  Badge number : 1014583374865992  On site until 07:00AM 
Officer reported staff on site
The officer could not gain access to the key box in his van 
"Attending Officer was unable to enter site due to known health and safety issues with black mould and a roof collapse 
Black mould was reported in December 2020 "
The attending officer reported that the alarm fob does not work 
The attending officer reported that he cannot set alarm and engineer cannot resolve the issue over the phone and will have to attend during working hours 
Officer reported they only lock the external gates for the site 
Ongoing issue with floor fives door still being sealed off so cannot access floor to set alarm 
Officer reported this site is now closed down 
The attending officer reported that the alarm panel does not give him the option for set up 
As previously reported the fence is damaged and there is copper cable left unsecured on the ground 
Officer reported the main gates are still broken therefore unable to seure 
The attending officer reported that on site is a car that is not usually there LM18EPO 
Engineer accidentally set of the fire alarm 
The officer has reported that they were unable to secure the property as staff is working on site 
Our officer reported the engineer turned up this morning while staff were already on site 
The officer has reported that no third party arrived on site 
No keys are held for site
The guard advised that staff member Charlie Stanman was on site 
The officer attended to site  yet there was a static guard on site until 04 00am 
The guard advised that staff were on-site stacking shelves 
On arrival the attending officer met with staff on site 
The guard advised that they did not know which of the 9 buildings had the activation 
The attending officer reported that the main front door is very hard to open and even harder to close on leaving site 
The attending officer advised that on arrival he was unable to set the panel 
Attending Officer reported that the main gates are stuck open  this is a known issue 
Attending Officer was unable to secure the entrance gates as they are currently stuck open 
Fire fault 1 to 14 input disabled 5th floor 
"Attending Officer reported that a portion of the perimeter fence has bent - please see photo 
Car in lot has broken down and is awaiting a tow - please see details on photo 
Cable left on ground "
There is a flood in the basement
Officer reported the alarm panel would not accept the alarm code to set 
The main gates was unlocked  There was copper cable left in the cable trailer 
Attending Officer reported gates unlocked on arrival 
Ongoing issue of damaged fencing by the skip
The gate unlocked on the arrival of the officer  2 males were in the rear parking area 
Our officer advised the alarm panel was not set upon arrival and there were no staff members onsite 
Officer reported the panel ws not set upon arrival and there were no staff onsite 
Officer reported the rear entrance door was open upon arrival 
Officer reported they were unable to reset the intruder alarm  
The attending officer reported that the edge of the gate is damaged 
The service partner was unable to secure the site as the gates are broken
Attending Officer reported gates open and Internal maintenance being conducted on arrival 
The service partner attended to site and was instructed not to enter building until further notice due to the site being staffed 24hrs and building access restricted due to covid
"Attending Officer was unable to secure the gate located on Fleet Street 
Padlock and chain are missing from gate 
Officer advised BT SCC 
Also reported was gates unlocked on arrival and cable left on trailer "
Our officer reported the roof access bottom bolt lock has come off of the door however the door is still secure 
Officer reported a Tesco s trolley had been fly-tipped next to the main gate at the rear of the site  Rear Window not Latched so you can gain access to the building  No keys held for the site 
On arrival  the main gate was unlocked  Copper cable was left on cable trailer 
Officer reported signs of fly tipping  someone has dumped a fridge onsite at the main entrance 
Attending Officer reported the panel in alarm on arrival 
The attending officer reported that there is no padlock on the main gates  therefore the property was not secured on arrival 
Officer reported they are unable to secure the gates as there is no padlock 
Officer reported no issues on site but chase app not working on job
Service partner does not hold keys
The guard advised that a security officer was on site due to building works going on overnight 
"Officer reported the site is a building site and they were unable to gain access into the building and that there were builders onsite 

Officer then called back shortly to report findings of a smashed window onsite so had suspicions about there being a potential break in on site "
The attending officer reported that on arrival there was staff on site 
The attending officer advised that they have an incorrect codes for the managers  office 
Service Partner waited on site for 30 minutes for the contractor but they did not attend 
The officer has reported that the keys work but the swipe card for the internal doors does not 
Officer reported there was no engineer onsite to allow access to 
No issue on site  The guard advised that the application used to complete reports crashed 
Officer advised they entered the wrong alarm code on the panel so it started beeping 
Staff were on site doing check ups 
The guard advised that staff were on-site doing some work 
Officer reported they have been unable to removed the padlock from the pedestrian gate for some time now as the key no longer works 
The officer has attended to site and spoken with the CYB - There is no sign of damage or  intrusion   all power to site is out - There is no power to ATM s  Some of the internal lights are out and there are some street lights out 
The attending officer advised that the barriers on site are damaged/broken 
Officer arrived on-site  completed all tasks but came across a leakage coming from the ceiling above the milkshake counter
The attending officer has reported a drip leak coming from the roof in the stairwell fire exit area 
Officer advise there was no alarm on the premises 
Oficer reported the power supply unit fault is still present  Trinity to come out tomorrow Monday 15th
The officer attended to site and called ADT who say the alarm contract was cancelled in 2018 therefore they couldn t help us 
Officer advised of a damaged door on site 
Officer reported there is a water leak which is coming from the roof and exit doors 
Officer advised there was no one on site upon arrival 
Officer reported the alarm panel required  managers reet 
Officer reported they are unable to secure the padlock to the site as it does not fit 
Officer advised they were unable to set the alarm 
Officer reported the left side of the gate is broken and is on the floor 
"Attending Officer reported the following issues on site:
Gates unlocked on arrival
Cable left on the ground
Damaged fencing behind skip  known issue "
As previously reported the barrier is still broken 
Officer reported the inner automatic-double glass doors are not opening so they were unable to gain internal access 
Office reported the razor wires coming off the gate and may be dangerous to people in and out of the site 
Officer reported they were unable to gain access to the first floor as the lift was not operating and there was no access from the fire escape stairs 
The officer has reported that we have carried out an external patrol of the Portakabin areas and no persons or issues can be seen on the site 
"Secom engineer called at 16:02 arrived on site at 17:00 didn’t replace the contact just isolated the issue as he said it would take too long to do now and said he would contact site to revisit and replace the shutter contact

Engineer was D Curran both left site at 17:36"
The officer reported that the third party was not ready for the premises to be locked at the time of the booking 
The guard advised that staff were on-site so they were unable to get the capture panel reading 
The officer has reported that the officer was unable to open the gates and the alarm fob held did not work on the panel in #26  The officer had to use the alarm code from #25 
Attending officer has arrived on site today and yesterday for an unlock as requested by the client  But no one has turned up on both occasions 
Attending officer arrived on site and waited for the engineer for around an hour before being stood down  No answer from Adrian Jones
Due to covid restrictions  only an external check could be carried out  as requested from security on site 
Attending Officer advised that there was no Guard or staff on site on arrival 
"Attending Officer to conduct a patrol to ensure that barrier is locked and secure 
No unlock during current situation "
Attending Officer reported scheduled electric works inside building on arrival 
The attending Officer has met Keyholder  James Davies  on site  who advised that the alarm has been reset 
The attending Officer has reported that the padlock was frozen 
"Attending Officer was unable to secure part of one gate due to known issue 
Please see photo "
The fire alarm could not be reset on exit as no code held for the fire panel 
EE requested External patrol only  the officer to close the key box outside of the building 
"Attending Officer reported that the fencing is not secure enough to keep pedestrians out of the site 
Please see photos "
"Attending Officer found a chain had been cut on arrival 
Officer noted that site has been broken into recently "
The alarm will keep reactivating as the door closer doesn t have enough pressure to close the door 
Attending Officer has left the alarm unset as instructed by BT SCC 
"Attending Officer found the gates left open on arrival 
Officer also found the door at the rear of the car park left open 
Please see photo "
"Attending Officer reported:
Gates unlocked on arrival
Cable left on the ground
Damaged fencing behind skip  known issue "
The attending officer reported the main barrier is broken  Please see photo s attached to report 
The back gate was open on arrival 
The back gate was open on arrival 
Officer unable to identify the area of the activation 
In park hall block C at the loading bay  there is a broken pipe 
The attending officer has advised there is no power in the area 
Contractor Andy from Quadrant flooring still onsite working and would not be finishing until 4pm
Site is open and operational  Officer was denied entry as there are vaccinations being carried out on site 
The officer attended to complete the unlock for the property however after an hour no staff member or contractors arrived onsite 
The attending officer has reported staff member Corrina was on site 
The officer was unable to complete the mobile report as there was an issue with the application crashing  The Officer attended the property and was met on site by the homeowners who advised they had inputted the code incorrectly a few times setting the alarm off but disabled the alarm not long after it activated 
The attending officer has reported a water spill on the 3rd floor 
The attending Officer was unable to activate/deactivate the alarm panel as Fob/Code is not held 
The attending Officer has accidentally left his Keys inside the Office 
Attending Officer reported Contractors on site on arrival 
The attending officer had experienced issues with the shutter remote 
The officer does not know who was meant to be on-site or not as the site is Public storage  Unitholders on site 
The attending officer has advised the rear shutter number 1 is not closing 
Tamper on the alarm panel  The code provided to the service partner was unable to clear the tamper 
Re-activation of zone 33 changing room 3 door 
Attending Officer reported a Fire Exit Door had been left open 
The attending officer reported that the main gate metal bar top screw missing  Full external carried out everything else safe and secure 
"Attending Officer reported:
Gates unlocked on arrival
Cable left on ground
Damaged fencing behind skip  known issue "
Electric charging point screen damaged  No issues with the building 
"Attending Officer was unable to secure Main Gate due to broken barrier 
Known issue "
The attending officer has reported a broken pipe which is leaking water at the rear of the site  Officer was unable to turn off the water valve 
Car with registration number WF02 0BD left at the front entrance 
Site under refurbishment and it is locked 
The alarm not set on arrival 
Rushhish left on 2nd floor stairwell 
The attending officer has reported there is a water leak on site in the loft area  All the water inside the tanks are frozen and one of the indect pipes has been disconnected 
Alarm would not reset 
The officer attended the property and was on site for 2 hours  the landlord never arrived for the access meet
The guard advised that the store manager was already on site when the guard arrived to give access to the engineers 
Unable to set alarm 
No staff on site  Officer unable to collect keys 
Staff present on arrival 
Attending Officer reported possible staff on site as a Blue Audi  KW70WFG  was found parked in car park 
Officer reported he was unable to lock the site as staff were onsite by the name of Emma 
"Attending Officer found a roller shutter open on arrival 
Officer advised that this was not related to the Zone of activation "
"Attending Officer was unable to secure the RHS of the Main car park gate due to known damage 
Please see photo "
Attending Officer was unable to enter site as site is currently derelict 
"Attending Officer was unable to set the alarm panel on Floor 5 due to the sealed Entrance door 
Known issue "
"Attending Officer reported:
Gates unlocked on arrival 
Cable left on ground 
Lock found left on ground 
Damaged fencing behind skip  known issue "
The attending officer reported the main barrier is broken  Please see photo s attached to report 
Attending Officer found the padlock from the gates broken on the floor  please see photo 
"Attending Officer advised that tennanets are complaining about a Toyota Prius  LM18EPO  that has been parking in car park 
Please see photo "
Attending Officer was unable to lock Units 12 and 17 as staff were still working on site 
Site was already unlocked due to scheduled booking 
Officer unable to set the alarm and secure site due to staff present on site 
The attending officer has advised the site closed at 13:00 so new keys were not able to be collected 
The attending officer required an alarm reset 
The operative advised that no-one turned up despite waiting for 40 minutes 
The attending officer did not collect a swipe card as the staff member at reception advised it is GR8 Security who will be doing the patrols and keyholding 
The attending Officer has reported that the Lock on the padlock was frozen and the Key was stuck inside and may require to be replaced as its not weather resistant 
The attending officer unlocked only the external gates on site 
Officer  reported  static guard on site all night  and contractors are still working
Attending Officer was unable to secure inbound gate due to known damage  please see photo 
sp advised to no engineer on site   only cleaners who confirmed no engineer is on site or attended the site
Roof leaking badly on external staircases  This has been reported on previous attendances 
Officer reported that when we attend the above site we have to take metre readings which are in the cellar and the for the past couple of months we have been raising it as an issue which are that the cellar door is stuck and the amount of condensation and mould in the cellar it is a health and safety hazard
"Attendance stood down by Lee at Secom 
Officer was already on site  outside  "
Attending Officer advised that the door lock on the 3rd floor was not securing due to weather conditions 
Attending Officer reported no new signs of travellers in area 
"Attending Officer reported:
Gates unlocked on arrival
Cable left on ground
Damaged fencing behind skip  known issue "
Officer reported the main gates have technical issues 
Exit gate has technical problem  remains open night and day since Monday February 8th  2021 
The operative advised that the exit gate has a technical problem and wouldn t close 
"Attending Officer advised that site has no corridors and contains individual units 
Officer secured Entrance gate but left Exit gate open as 2 units still have staff working on site "
"Attending Officer reported that the Fire Exit door has been left open 
Please see photo "
The officer does not know who was meant to be on-site or not as the site is Public storage 
The officer was not able to set the alarm 
The officer attended the property to secure the building however staff were still working at the time of the request  so the officer left site with staff 
The operative advised that staff were on site 
External patrol only as it was a CCTV activation 
The attending officer had contacted engineer Scott Davis who was due to be on site  Scott advised he would not be attending site today 
Tina at Sodexo advised the engineer would not be turning up to site 
The engineer did not turn up to site 
Officer reported the guard he met onsite for the lock up was not onsite for the unlock this morning 
Officer advised he believes there is a fault with the alarm as he has attended this site on 5 occasions over the past 3 nights 
Officer reported the height restriction barrier is severely damaged 
Staff onsite advised they asked for the attendance to be stood down  however a guard still attended site 
Attending officer arrived on site but only an external patrol could be achieved due to no keys being held
Attending officer arrived on site to find the inbound gate damaged so the gate couldn t be closed
Attending officer found an oven left on in the basement kitchen
Officer advised he was unable to set the intruder alarm 
Officer advised external gate only locked
Attending officer couldn t gain access with the keys held
Attending officer couldn t leave site secure as staff were on site late
Attending officer arrived on site to find a van in the yard that was still running
Attending officer found damaged fencing which has already been reported
Attending officer couldn t secure site as it is broken
Attending officer couldn t secure the exit gate as there is a technical problem
Service partner arrived on-site  reported that the main exit gate has technical problems
Officer reported the main gates have technical issues 
Attending officer arrived on site but the access card didn t work for this location
Attendance to site had been severyley delayed as the officer with the keys was stuck on a distant alarm call 
On arrival the attending officer met with the static guard from Oak Security who was at the car park 
Attending officer was stood down by security on site as there wasn t supposed to be an attendance today
Attending officer arrived on site but could not complete an internal patrol as the site is under refurbishment and is locked
Attending officer couldn t gain entry due to the access key missing from the keypress
The attending officer advised that the padlock to the rear car park gate is faulty 
The attending officer reported that the black fob does not work  therefore the officer was unable to set the panel 
The attending officer reported that the engineer did not turn up on site 
The attending officer advised that no one has turned up to collect the keys  therefore he didn t want to leave them in the letter box 
The attending officer attended for a replacement of their fob  however  on arrival the store was closed 
Engineer did not come to site 
officer reported shutter switch one is not working
No alarm codes held for site 
officer carried out external only around the perimeter of the site
The service partner did not enter the building as the alarm was a communication fail
The service partner spoke to the client directly James Luetchford who advised them not to attend site - the client had checked CCTV and did not require attendance 
Officer reported main entrance barrier lower gate hinge is damaged   please see photo of issue
The attending officer reported that the electricity on-site is turned on at the moment 
This report is for FYI purposes only  Keys have been hand-delivered to the property instead of being posted back  attached is a copy of the key receipt with recipients signature and access card serial number 
Our service partners advised that they do not hold keys for this site 
Service partner has reported they do not have keys for this site to be able to carry 9ut this request 
Officer reported broken wheel on rhs gate   Please see photo
officer reported staff on site   Heidi Meena
Internal patrol not possible due health & safety  Building site
Officer done internal and external no issues on site
Officer reported no manager has turned up to assist with alarm
Officer reported no issues on site
Officer was unable to lock the padlocks on the car park gates as they are frozen shut 
officer locked external gates only
officer  done full external  and internal of building  - panel reading office
Ongoing issue whereby the alarm on the 5th floor can not be set as the door has been sealed off 
The operative advised that there is a leak in the basement area beyond the heating chamber as there is about 1 inch of water 
Officer reported he fell down the step  Photo provided
"Attending Officer reported that the main gates are stuck open 
Known issue "
The attending officer reported the main gate and rear gate would not close 
no signs of travellers on site
Officer reported the gate is unable to secure 
"Attending Officer reported the leak in the basement is still present 
Officer also reported gates unlocked on arrival and the cable chamber door unlocked "
The service partner has advised BT of this previous flood in the basement 
The attending officer was unable to lock the main gate padlock due to the cold weather 
Officer advised it is very slippery by gate
Officer reported damage to the perimeter fencing   please see photo
The attending officer was conducting his external patrol when he found 3 unknown people near the rear gate  The people were told to leave and the officer continued with his patrol 
Officer reported  padlock  is missing from gate  as photo
Attending officer found gate missing a padlock so the site couldn t be fully secured
Ongoing issue - Officer reported padlock is missing from the gate  Please see the photo 
Officer reported cable on cable trailer
Officer reported cable on cable trailer 
"Attending Officer was unable to gain access into site 
The lock barrel has been frozen due to the weather  please see photo "
Officer reported they were unable to set the alarm and so was ARC 
Officer reported there is a key stuck in the keyhole of the rear car park gate 
officer reported bicycle entry door was left opened
Officer reported he was unable to unset the alarm system as the fob for the alarm panel was not working 
Officer reported contractors on site advised they will set the alarm on departure 
Officer reported key were not ready on time quoted
Officer attended site for a key check  the keys now have been separated for both units  C and 14
Officer reported that contractors did not show up
The officer attended the site to allow access as booked  On arrival  the staff were outside ready to provide access to contractors 
The officer has reported that both they and a secom engineer were on site but no keys available 
Attending officer arrived for unlock  whilst checking the alarm panel 39 faults appeared on the display
"The officer has reported that a patrol was completed but site was left unlocked  as per the clients instruction  Due to a complete heating failure on site we have been forced to close the office starting tomorrow 

Please can I ask the following happens regarding the unlock starting tomorrow:

Unlock: Complete the morning patrol as usual  but leave the site locked  main entrance and kitchen  and arm the intruder alarm upon exit 
Lock Up: Unlock the doors disarm the intruder  perform the patrol and leave site locked and armed "
Attending officer couldn t set alarm as there was a power failure
Attending officer arrived on site but the SP that attended doesn t hold keys for site so only external patrol could be achieved
Attending officer arrived on site to complete all job tasks  when trying to set the alarm there were some issues around the panel not being fitted properly so the keypad wasn t working 
Attending offcer arrived on site to complete external patrol
Attending officer arrived on site for an alarm call due to a power failure
Officer reported that on arrival the main gate was open 
Attending officer arrived on site but the wrong key was brought to unlock access point so only an external patrol could be achieved
Attending officer arrived on-site to complete external patrol  as required
Attending officer arrived on-site  underwent completing the tasks   Found a door that wouldn t  lock so the site couldn t be left completely secure
Attending officer arrived on site when entering the premise the sensor for the main lights didn t activate so the internal patrol had to be completed using torches  Alarm pad was also faulty so they had to contact BT for a remote set
Attending officer couldn t gain access to site due to not having the access card
Officer arrived on site to complete an external and found this issue on site  look at the incident picture 
Attending officer arrived on site and found one of the gates was broken
Officer advised the main gates have technical issues 
Attending officer arrived but the access card hasn t been updated yet so only an external patrol could be achieved
Attending officer arrived on site but couldn t gain access of site due to not holding any keys
Attending officer arrived on site but the key held in the keypress was missing so only an external patrol could be achieved
Attending officer arrived on site  underwent completing all the job tasks  He came across a door with a broken handle  please see the picture under issue  Door was left secured
Attending officer arrived on site to complete all tasks 
The attending officer met with the ISS guard on site who will remain there until further instructions 
The officer has reported that the North wing cannot be secured as there is an ISS static guard on-site due to an issue with doors   Lock not required 
The officer has reported that the alarm code held did not unset the alarm 
The guard advised that the contractors did not turn up for the access meeting 
The guard advised that they could not enter the site as there were contractors on-site removing scaffolding 
Officer reported no guard or staff on site
The guard advised that there were several staff on-site stacking shelves 
officer unlocked site
Officer reported Mr Darking on site to collect lorry
Attending officer arrived on site
Officer arrived on site to lock up the main gate which had been left unlocked 
Attending officer found key left inside the lock of the canteen door 
Officer advised the alarm code 2580  did not work 
Attending officer arrived on site for an alarm call  no alarm codes are held to deactivate
Office report alarm ringing inside building on external patrol
Attending officer arrived onsite  The alarm had already been reset by staff onsite
Officer reported one part of the building at the top end of the site is smelling of gas
Officer reported an ongoing issue whereby the barrier is broken 
Officer reported no issues onsite
Officer arrived onsite to complete an external patrol as requested
Attending officer arrived onsite to complete alarm call  Mr Dan O Sullivan had advised the officer to stand down
On attendance  the person locked in had already been released 
The guard advised that staff were on-site so they could not take the alarm panel reading 
The guard advised that they were unable to locate site with the address given 
The attending officer advised that on arrival there was staff on-site - Mr  Karamat Sha 
The guard advised that staff were on-site so they could not take the alarm panel reading 
"Attending Officer to conduct a check of the barrier to ensure it is locked and secure 
No unlock needed during this time "
The attending officer reported that the door handle from one of the external doors is missing  The handle is missing on the internal side if the door and no one can enter from the outside 
The attending officer advised that one of the door handles on-site is broken 
The key warden advised that they could not see the guard on site  The key warden knocked on all doors and called the number that is displayed on the door 
"Attending Officer was unable to gain access into site 
Main door has been blocked  please see photo 
Known issue "
Attending Officer advised that the main gates would not close 
The officer attended and was unable to unlock the padlock as it appears faulty  the officer contacted SECOM and advised them of the issue 
Attending Officer has left alarm unset as instructed by BT SCC 
"Attending Officer reported:
Gates unlocked on arrival
Cable left on ground
Damaged fencing behind skip  known issue "
The entry barrier is broken so cannot be closed  This is a known issue and reported previously
Attending Officer advised that the Guard was not on site on arrival 
The attending officer has reported staff were on site at the time of attendance therefore the site was unable to be left locked 
Sean Woods had requested an unlock to his office  Everyday Resources   When the attending officer arrived  Sean was not on site 
The third party did not turn up to site 
"Attending Officer was unable to gain entry into site 
Officer advised that there is no M-F Daytime response for this site; and as such  the access card/fob are locked away "
The service partner has advised their current instruction is not to leave the barrier open 
The guard advised that the bottom pins on the right-hand side fire doors are not aligned properly 
"Attending Officer reported the Fire Alarm panel showed an activation in the Sub Basement  Back Staircase  Lobby 
Officer was unable to gain access into the Coffee 1 shop  no keys held for this shop "
"Attending Officer was unable to gain access into site 
Ploughed snow has been piled up in front of hte entry gates 
No keys held for the goods gates "
"Attending Officer was unable to gain entry into site 
Key is working fine  but door appears bolted from the inside "
Attending Officer found site already locked on arrival 
"Attending Officer found unit owners on site on arrival 
Site has 24/7 access options for storage unit owners "
The Officer has again reported that the Padlock is too small for the gate 
The Officer has reported that the Bin is over flowing  please see photo  
The Officer has reported the issue with Barrier as its broken  known issue  
The Officer has reported the alarm was not set on arrival 
The attending officer has reported staff were on site 
The attending officer arrived on site to find the engineer was still working and so the site was unable to be locked at the booked time 
Green topped key no longer operational on the padlocked entry gate 
Staff on-site 
The attending officer has reported contractors were not on site when he arrived 
The attending officer was requested by contractors to leave the keys with them 
The attending officer has reported the person/s access was required for did not turn up 
Attending Officer found staff on site on arrival 
The attending officer has reported unit staff were on site 
"Attending Officer to conduct an External check to make sure barrier is locked and secure 
Barrier to remain locked until further notice due to current situtation "
Attending Officer advised that the gates and barriers were already open on arrival 
Attending Officer advised that Club Secretary Steve Drewery was on site on arrival 
Attending Officer to conduct an External check for a CCTV comms fail 
The attending Officer has reported that there was no perimeter fence 
Service partner stated  No running water in the toilets and they won t flush  No water running from taps in the toilets  The prep area has still got water running  
Pipe has burst in the cleaner s room by the rear exit and the room has flooded 
The guard advised that a manager was on site when they arrived 
The attending officer has reported the Coca Cola machine was not working and was therefore was unable to run the tower 
"The attending officer reported the following issues on site:
-Code for managers office does not work so unable to check fire alarm and CCTV 
-No water in taps in concession area 
-Disabled Toilet in Screens area  No warm water in tap  The water pressure is low 
-First time in all visits this light is found on 
-There is a small water puddle in the middle of the foyer area "
"Attending Officer was unable to enter the site due to known health and safety issues 
Officer also advised that he has issues uploading photos due to a phone error "
Attending Officer instructed by EE to conduct an External check of site and secure the key box 
"Attending Officer was unable to gain entry into site 
Officer advised that the door may be locked from the inside "
Attending Office conducted an external check and made sure that barrier is locked and secure 
Officer  returned to site to lock up as staff were not ready at 21 00
"Attending Officer unable to set the alarm for Floor 5 due to sealed entrance door on same floor 
Known issue "
Attending Officer was unable to secure site as staff were still working 
The padlock that has been provided is too small to lock the gate as required properly 
"Attending Officer reported the Ground Floor Fire Exit ajar on arrival 
Please see photos "
"Attending Officer reported:
Gates unlocked on arrival
Cable left on ground
Damaged fencing behind skip  known issue "
There is an Unmarked Van parked out the front of the compound with a large amount of cabling between 3 drums next to it van REG : YG69 RHY 
The officer whilst completing his patrol of the property found the rear fire door open  the officer contacted Mitec who advised the officer to enter the property to check  Full internal patrol conducted no signs of entry  The officer is unable to secure the door as no keys are held and reports a large number of rough sleepers located near the back of the property 
Attending Officer reported that a ground floor window has been left open 
Attending Officer unable to lock site as staff were still on site on arrival 
"Attending Officer reported staff member Ollie Canham on site in arrival 
Please see photo of ID 
Ollie on site measuring for refit "
Attending Officer was unable to lock site as staff were stil working on arrival 
Attending Officer reported staff on site on arrival 
Officer completed site survey
Officer spoke to staff member   Samantha Brown  who advised there were no keys available for collection
Issue with the alarm panel was showing quote coded to sodexo helpdesk for the next steps 
The engineer who access was provided to required the fire alarm to be put on test 
The attending officer has reported he does not hold keys for the side entrance which a staff member has advised is required 
"Attending Officer to conduct an External check of area to ensure the barrier is secure 
Barrier to stay locked during this time "
The attending officer has reported staff member Gloria was on site 
Met Mr Assad  school manager  on site 
The attending officer has reported flooding from toilets and feces on site 
The officer could not enter the property due to COVID signs posted with no entry
Officer attended for the second unlock request by Mitec due to maglocks not working  Site left with staff member Taylor 
The attending Officer has reported a fault with the maglocks as its stuck open and has advised the site is vulnerable until Staff attend 
The attending Officer has reported that the site was already Open on arrival 
There was an issue with the mobile application so no information could be added to the report 
The attending Officer has reported that the EE Store is inside a secure Shopping Centre which the Officer is unable to gain entry 
The attending Officer has reported that the Fob held does not allow access to the 1st Floor Studio as the lights have been left on 
The attending Officer had Keys for the site but a Fob or an alarm Code is not held to silence the alarm 
The attending Officer has reported the current Fob held for the alarm is invalid 
The attending Officer was unable to secure the site as Contractors were present for a construction work 
The attending Officer has reported that the external gates were left safe and secure 
The attending Officer has reported that there was no keys in the Safebox when he arrived to site to complete the Lockup 
"Attending Officer unable to set alarm on floor 5 as the floor 5 entrance door is sealed 
Please see photo 
Known issue "
The attending Officer has reported that the door sensors are not working  which will allow anyone to walk in and out through the building 
No keys are held for this property as this was an ad-hoc patrol request 
The attending Officer has reported that the padlock is not big enough for the lock on the gate 
The attending officer has reported the fencing on site is broken  Please see the photo attached  Vehicle unlocked  reg  plate FM16 RUV  
Attending Officer unable to secure gates due to ongoing maintenance issue 
Attending Officer was unable to enter site due to signs restricting entrace due to Covid situation 
Attending Officer reported water leaking near alarm panel 
"Attending Officer was unable to locate site; Officer advised that Secom and TKC are aware of issue 
Site Survey has been scheduled "
The attending officer has reported staff were on site at the time of attendance therefore the site was unable to be left locked on departure 
The attending officer has reported staff were on site working therefore the site could not be locked on departure 
Attending officer reporting alarm panel showing 34 faults and may need to attention of an engineer  areas causing issue appear to be front door and basement kitchen door 
The attending officer has reported he was unable to leave the site unlocked due to high tide 
Attending officer reporting unlock not required due to COVID lockdown 
The officer has reported that the site was locked upon arrival 
The guard advised that they are unable to enter the site as they do not have the correct PPE and need the be escorted by Railway Network as it to get access you need to go over the railway line 
The guard advised that the site will need to be re-surveyed as the zones are marked incorrectly and the handles need fitting to doors 
cctv activation   full external done  -  no person seen on site
The guard stated that the wooden door to the reception on the 2nd floor has a damaged hinge and part of it has fallen off 
The guard advised there is no issue on-site  they only lock the gates 
The guard advised that staff are on site until 06:00 so the locking of the building could not be completed 
The guard advised that staff are on site until 06:00 
The guard advised that there were no keys in the safebox when he arrived to site 
The guard advised that there were staff on site 
The guard advised that door number 1450 was insecure when they arrived 
Attending officer arrived on site but no keys are held 
The guard advised that the gates on-site are broken 
"Attending Officer reported that the main gates are stuck open 
Known issue "
Attending Officer advise there are 2 lifts are not working  Main Gate is still out of order 
The officer found standing water on the main staircase of the site 
Attending officer arrived but no keys are held for the site so only an external patrol can be achieved
"Attending Officer some items left outside  please see photo 
Officer also found gates unlocked on arrival "
Attending officer arrived on-site to complete an external patrol as there aren t keys held of site currently
The officer found that whilst patrolling the property a window had been left open on the main staircase this due to the weather has caused standing water on the staircase creating a possible safety hazard
Officer reported there is rubbish overflowing 
Attending officer arrived on site but no keys are held for site currently
Attending officer arrived on site to complete an external patrol as there aren t keys held currently
Attending officer reporting alarm unset on arrival  also Copper cabling left unsecure on site 
The attending officer reported the main gates had a missing padlock  Please see attached photo 
"Attending Officer reported:
Gates unlocked on arrival 
Flooding in basement - known issue"
The attending officer has reported the fencing on site is broken  Please see photo attached
The Officer has reported that the Entrance and rear gates were Unlocked 
The guard advised that one side of the gate is missing so they are unable to secure the gates completely 
Attending officer reporting potential signs of travellers in the area 
"Attending Officer reported that the bottom runner on the gate is damaged  please see photo 
Previously reported "
Attending officer reporting they were unable to secure the gates due to them being broken 
Officer reported the issue with the gates being insecure is still ongoing 
The guard advised that the exit gates had technical problems 
Attending Officer found gates open on arrival 
Officer reported padlock missing on main gate
The Officer has reported that there was no padlock to secure the gate 
Attending Officer reported cable left on trailer 
The attending Officer has reported that the cable was left on the trailer 
The Officer has reported that there was rain water coming through the Windor 
The attending officer advised that on arrival he met with cleaner staff on site 
Attending officer reporting upon arrival to site Mitie security and engineer present carrying out works 
Attending officer reporting they were unable to secure site due to staff member Chris Morgan still present  he will secure upon leaving 
Officer reported staff on site
Attending officer reporting they were unable to locate site to complete patrols 
Staff were on site working when patrolled 
Job amended last minute and Service Partner not made aware in time 
Attending officer reporting they were unable to complete the key collection as requested due to not being verified upon arrival to site 
The guard stated that staff were on-site so they could not do an internal patrol 
Attending Officer reported a cracked window on site 
The key warden advised there is a static guard on site who refused the key warden entry 
"The attending officer has reported several issues:
- No signal on the CCTV screen
- No power to drinks towers so the officer was unable to run them through
- There is mould growing on the carpets leading to screen 1"
The guard advised they were unable to add pictures to the job due to an issue with the operative s phone 
No issue on-site the guard only has to do an external patrol 
As previously reported the fence is damaged and there is copper cable left on-site unsecured 
The attending officer reported that the gate on-site is damaged 
Attending officer reporting while patrolling site they identified damaged to fencing and a smashed window 
The attending officer advised that there was no need to enter the buildings as only an external patrol is required for a communication loss 
The attending officer reported that the magnetic doors do not close as per instructions and there is no access to the reception to do an alarm reset 
The attending officer advised that on his last visit to this site fob would not unset the alarm  There is a house next to the health centre and this is a loud alarm 
The attending officer advised that there is an issue with the alarm  the same contact/pir keeps activating 
The attending officer advised that they do not have the codes for the alarm panel 
The attending officer states that they were required to complete only external patrol on site 
The attending officer reported that there is an issue with the gate to the cable compound 
Attending Officer was unable to locate the officer on site to complete the Welfare Check 
The guard stated that the padlock is not big enough for the lock on the gate 
The guard found the door next to unit 26 left open 
As previously reported the fence on-site is damaged and there is copper cable left on the ground unsecured 
On arrival  the attending officer found the back gate left wide open 
The attending officer reported that he could not close the back gate 
The guard stated that there is a security officer on site 
Thea attending officer only conducted an external as instructed by BT  Site is safe and secure 
The service partner was unable to lock as there was security and contractors on site working through the night 
The officer reported that we were unable to reset the panel due to the tamper alarm  which required an engineer s reset code  The officer called the alarm company and two engineers called our officer back  The officer advised that both engineers did not have the required reset code 
The officer has reported that staff were on-site upon arrival   Mr  Golden from nova south security company
The officer has reported that the alarm activation was caused by a staff member Justyna who was on site upon arrival  The officer has advised the alarm was reset upon arrival also 
The officer has reported that the alarm codes held do not work 
Staff on-site on arrival  Unable to access premises due to covid restrictions 
The officer has reported that an external patrol was carried out 
The officer has reported that it was noted that the Ground Floor main entrance has been left open on arrival 
The attending officer advised that the padlock on the gate chain is missing 
Attending officer reporting they were unable to set alarm before leaving due to Dr Sue Levi working late 
The attending officer reported that staff are on site therefore  unable to conduct lock 
The attending officer reported that staff are on site therefore  unable to conduct lock 
The attending officer reported both car park barriers were open with the light flashing on arrival  Please see attached photo 
The attending officer reported he was unable to complete the lock due to staff being on site  Staff will lock the site once they leave site 
The attending officer reported the cable chamber door was open and water flowing down cable making quite big puddles 
The attending officer has reported the main gate to members of public are open and copper gate full of copper is also wide open  Full external carried out 
The attending officer has reported the fencing on site is broken  Please see photo atteached
The attending officer could not secure the site due to the barriers being broken  Please see pictures attached  
The attending officer reported main gates are not electronically working  so they can t be locked properly 
The attending officer has reported four ground floor windows left open  Patients records door unlocked and open upon arrival 
The engineer was a no show 
Alarm was already unset by Manuel on site 
"Attending Officer to conduct an External check to ensure the gate is locked and secured 
Gate to stay secured during current situation "
"Attending Officer to conduct an External check of site 
No Internal checks due to current situation "
Attending Officer advised that a Static Guard from Bold Security will be on site until 0700 hours 
"Attending Officer advised that staff were on site testing the sprinkler system 
Staff advised that they notified the monitoring station "
"Attending Officer was unable to gain access into site 
Entrance blocked as shown in photo "
"Attending Officer reported the CO2 Extinguisher is missing its black seal  
Located next to desk B3 12 & B3 15 by black fire exit door "
"Attending Officer unable to find location of alarm panel 
Only the Fire Panel is located behind the desk  as shown in photo "
The attending Officer has reported that water leaking from roof 
Staff onsite 
The attending Officer has reported that he was having issues resetting the alarm 
Attending Officer advised that the closing hours for this site may be changing due to Passport and Home Office moving into building 
The attending Officer has reported that the Copper-gate was left wide-open 
Attending Officer was unable to secure gate due to known damage 
External patrol completed and found all in order 
The attending Officer has reported that he was unable to Secure the gates properly as right hand gate comes off its runner 
Staff present on arrival  Lock therefore not required 
"Attending Officer reported water leaking from the celing in front of the reception area 
Please see photos "
Attending Officer advised that the ADT Engineer did not arrive to site 
Attending Officer reported staff on site on arrival 
Service Partner called away to fire alarm but unlocked site for BT Engineers  Static guard was present during the absence of the officer 
The contractors were a no show 
Attending Officer reported that the codes and key were not avaialble on the day of the Site Survey 
Whilst the officer was completing the external patrol the site manager arrived and told our officer to leave and our service is not required  the officer left
There is water leaking through the ceiling as reported last night however it appears over the night more damage has happened and the water is now leaking on to the printer 
The Internal door next to the elevator is insecure and cannot be locked 
The operative advised that the store manager Katrina Haggie was on site 
The officer attended the property and on departure tried to get a set signal from CHUBB however the reset password held was outdated 
"Attending Officer reported water leaking from roof 
Please see photo "
The attending Officer has reported that the engineer  Michael  was still onsite and has advised he is working until 0600am 
The officer is reporting that the shutter to basement unit B4 was open on arrival  this has never been open on previous attendances so was making note of this fact 
Water dripping through the celling in to the main reception  Located a holes in the celling 
"Attending Officer reported a leak in the roof  as shown in photos 
Officer also advised that the leak is near the light switches "
Officer advised they were unable to check the CCTV as there is no power to the system 
The guard advised that staff were on site when they arrived 
"Attending Officer reported a wet patch on the floor near the rear fire exit door 
Please see photo "
The guard advised there were 2 homeless people sleeping in the doorway so they were unable to carry out the checks 
The officer has reported that there is a weather-related leak on the top floor stairwell in the top floor office 
"Attending Officer was able to secure door by using hammer like tool on bottom corner 
Please see photos "
"Attending Officer unable to secure half of gate due to broken wheel 
Known issue "
"External patrol done  no sign of damage to the property  All doors are closed and no windows or grills damaged 

The apparatus room has been patrolled  All appears in order  Site secure and alarmed "
The padlock is missing on the main gate so is open and insecure
"Attending Officer to conduct an External check of site 
It has been reported that the Client has vacated site "
Attending Officer was advised by ISS Officer that there is a night shift on tonight 
Attending Officer was advised by the ISS Officer that there is a night shift on tonight 
Attending Officer was unable to set the alarm for Unit 27 due to known issue with back door 
"Attending Officer reported celing tile damage from water leak 
Please see photo "
Attending Officer to conduct External check of site as Dog unit is posted at site 
Attending Officer left alarm unset as instructed by BT SCC 
There is no issue with the property however the officer was unable to complete the mobile report due to an issue with the application
The attending Officer has reported that AA Staff were present onsite 
"Attending Officer reported:
Damaged fencing behind skip - known issue 
Cable left on ground 
Gates unlocked on arrival "
The Officer has reported that the Barrier is broken  ongoing issue  
Following the AI s the officer contacted BT to set the alarm  BT was unable to set the alarm due to loss of power 
The attending Officer has reported that there was holes in the fence 
Unable to do lock up as staff still on site
Attending Officer was unable to get past the grey doors as they were locked on arrival 
Officer advised he met a member of staff named Alexis in the car park who said that the panel stated the activation came from the greenhouse double doors and that no reason for activation could be found 
Staff present on arrival  Job not required 
Staff onsite 
Staff onsite 
Officer arrive on site and was advised by security guard that  he will not let hem in without the contractor  Officer waited but Contractor didn t show up 
Staff with keys already onsite
Contractors failed to show up for unlock 
Report is FYI only  could not leave site unlocked due to the new rules in place during lockdown 
The attending Officer has reported loose cables and water contaminated on the floor 
Roller shutter was jammed so internal patrol couldn t be completed 
No issue with the site  however  officer unable to complete the report on the mobile application 
Officer reported park gates stuck open
Officer reported that  TBI Solicitors are working from this site
No site survey done
The attending Officer was oniste for an hour and there was no signs of any Contractors oniste 
"Attending Officer reported that the padlock has been removed from gate 
Please see photo "
Attending Officer reported that the ISS Guard is on site 
Attending Officer reported that an ISS Guard is on site 
"Attending Officer unable to set alarm on floor 5 due to the sealed door on same floor 
Known issue "
"Attending Officer advised that AA staff working on site on arrival 
Officer also reported cable left on ground and gates unlocked "
The attending Officer has reported a damaged fence 
The Officer has reported that the barrier is broken  previously reported  
The attending Officer has reported that Vagrants were present onsite 
The contractor did not turn up to site on time and the officer was not able to remain on site to wait 
The operative advised that a member of staff  Bob  was on site 
The Engineer failed to attend 
The operative arrived on site and spoke with Oliver who was unaware of collection  No fob was ready for collection and Oliver contacted his manager who was also unaware 
Gate to stay locked with the current situation
Officer reported slider is jammed on one side of the gate   photo taken of issue
The officer is reporting a rough sleeper has been sleeping in the doorway of costa coffee 
Attending Officer to conduct an External check of site as gate has been observed unsecure via CCTV 
Officer reported they could not get to the site due to road being closed
The attending Officer has reported that the building was locked and secured by Clive Crossman 
Basit from BT security on site overnight due earlier activation alarm would not reset
Internal patrol of the building not required  site secure on arrival BT informed 
"Attending Officer was unable to set alarm due to sealed door on floor 5 
Previously reported - known issue "
Attending Officer was unable to unset alarm panel with code held  7191 Enter 
The attending officer reported signs of fly tipping on site  A fish tank  book shelf over flowing bin was seen on the grounds  Please refer to the attached photo
The attending Officer has reported that the gate s damaged 
The attending officer has reported that the gates were found damaged on arrival 
As previously reported by the service partner  the gates are damaged for a couple of weeks now 
Attending Officer reported standing water on the Ground Floor leading to Fire Exit Door 005 
Attending Officer reported staff on site during patrol 
"Attending Officer was unable to gain entry into site due to an active comms fail on the entrance door 
Known issue  BT SCC are aware 
Officer also found gates unlocked on arrival "
"Attending Officer was unable to gain entry into site due to an active comms fail on the entrance door 
Known issue  BT SCC are aware 
Officer also found gates unlocked on arrival "
"Attending Officer reported damage to the white gate  please see photo 
Known issue "
The attending Officer has reported that the gates are broken  ongoing issue  
The attendinf Officer has reported that the basement area is flooded  previously reported  
The attending officer reported that there is a mattress dumped on the ground 
Attending Officer advised that the rubbish bin is full 
The attending officer has reported a member of staff was on site at the time of the patrol  For this reason  the site could not be secured 
Panel from perimeter fencing missing previously reported
The attending officer reported that the trash bins on site are full 
The Officer has reported that the exit gates have technical problems as it won’t close automatic 
The attending Officer has reported that the alarm was already set on arrival 
Attending Officer reported staff on site during patrol 
Attending Officer reported that the gates were not secure on arrival 
The guard advised that there were some lights left on inside the building 
The Officer has reported that the wall is still not repaired 
The Officer has reported that the gates will not lock with Key lever stuck inside of gate 
The attending Officer has reported that there was no padlock to the gate 
This site is for external patrol only  no access for an internal 
Attending Officer was unable to load photos due to a phone error 
Attending Officer reported that the far cable chamber flood alarm has activted for Zone 2 
"Attending Officer reported that one side of the main gate has been removed - previously reported - known issue 
Please see photo "
The attending officer reported that staff are on site 
Attending Officer reported that the padlock on the rear carpark gate  Caxton Street  is faulty 
The operative was not able to lock-up as the contractors had not completed the works at site yet 
The operative advised that staff were on site 
The operative advised that there was a cleaner on site 
The operative advised that staff were on site working 
Attending Officer confirmed that all access cards are working with no issues 
Mick Blanchflower was not aware of the site survey so this was not carried out 
No codes held for alarm 
The attending officer advised that the door is to remain locked as of the current situation 
The guard advised they could not unlock the exit gate as it had frozen over 
Attending officer reporting patrols completed but site left secured due to current lockdown 
The attending officer advised that on arrival there was staff on-site stacking the shelves 
"The attending officer advised that they do not have the access code for the alarm panel 
They only have the code for the keysafe "
The guard advised they were unable to enter site due to there being no dog handler to let them in 
The attending Officer has reported that there was a Constrcution hole infront of the gate 
On arrival the attending officer met with security who was locking up the venue  he has set the alarm and advised the officer that the is locking the site from Friday until Monday night 
The attending officer advised that on arrival everything was okay and there was nothing on the panel 
Officer reported the padlock had frozen due to freezing conditions
This issue is reported multiple times to BT 
Officer was unable to secure the gate as it is faulty 
Officer reported cadent had forced entry into unit 18 and 42 due to gas leaks coming from the cylinders 
Officer done external only   no site survey   due to Covid restrictions on site and not permitting external visitors 
Officer reorted the alarm panel was unresponsive 
The officer has advised that no persons were seen on-site during the external patrol  External only as we do not hold keys 
The officer has reported that they attended the site and carried out an internal patrol and confirmed there is no power to the building and the alarm is not working 
The officer carried out an external patrol of the premises to investigate persons see on site 
The service partner has key and fob  but no alarm codes  he met an  NHS IT engineer  Peter on site  as they were having issues remotely   Due to COVID our officer was not allowed on site  This job should have been booked as a third party access
Attending officer reporting contractors had already attended site upon arrival and fixed the door issue 
The attending officer advised that there is no guard or staff on-site and there are bad weather conditions 
The attending officer reported that the front door is kicked and therefore he was unable to gain access 
The attending officer advised that on arrival the service yard gates were wide open 
The service partner advised that yesterday s guard unlocked the car park but selected the wrong job on chase  so they locked the site up using the unlock job he missed 
Officer reported gas and water main cannot be located
The guard stated that there was a static guard on-site so the lock was not required 
Officer advised the alarm was unable to set as a tamper signal kept activating 
Door contact 2103 on fire exit next to room GF-78 then securing on the door frame  Door contact has been put in place so the alarm can be set 
Officer reported there was an issue with the alarm system 
Officer advised they do not hold the code/key for the padlock on the gate
"The service partner attended to this lock up earlier than booked as staff had informed of an early departure 
The officer believes they have rearmed the alarm but there is a temporary building in front of the building where they check the armed bleeps from so could not hear them  Attempts were made on 3 occasions to call the alarm company/ monitoring station Kestrel but there was no response "
There is an ongoing issue of damaged fencing and copper left on the ground unsecured 
Officer was unable to secure the gate as the padlock is missing 
"Attending Officer reported fly tipping at main door  please see photo 
Previously reported "
The service partner does not hold keys for this site so could only complete an external patrol
The officer has reported that the bar is jammed internally on fire exit 008 at the rear of the front entrance  The officer has reported we are unable to secure the door  Also  we were unable to gain entry and were buzzed in by BT security  this meant the alarm was unset and nothing was displayed on the panel 
The officer has reported that the fob held does not work  The officer typed in code and the alarm unset but the alarm did not switch off 
No guard arrived to hand keys over to 
Staff working on site 
The officer has reported that the boarding/ cover has come away from the window to the rear of the property  and the site is not secure 
Attending officer reporting issues with the door  unable to secure 
On arrival  the attending officer met with Mitie staff on site and they advised him that the job was not required 
The guard stated that the main gate is inoperable 
The guard stated that Dr Sue was on site when they arrived to do the lock 
The attending officer reported that he has found 2 males on-site sleeping 
Attending Officer has left alarm unset as instructed by BT SCC 
The guard stated that staff are on-site due to flooding 
The operatives phone crashed and were unable to take photos on site 
The attending officer reported that the padlock on the rear gate was not attached to the chain  As previously reported the gates were left unlocked  the fence is damaged and there is unsecured copper cable left on the ground 
The guard stated that the front gare is broken 
The guard stated that there was some cable left on the side of the site 
The guard advised that some windows were left open on-site 
The officer has reported that the boarding/ cover has come away from the broken rear window of the property and the site is not secured 
The service partner attended to site   A door sensor near the tennis courts activated  the door was not securing  Secom were updated and the officer returned to site to meet with he keyholder and they both secured the door 
Staff were on site when carrying out the internal check 
Staff were on site when patrol was carried out 
The officer has reported that there were staff on-site upon arrival 
"Secom insisted that this alarm was attended to  
The officer entered this property and the client was self isolating post a visit from France "
The service partner attended to site to provide access for the landlord team to carry out works
The service partner attended to provide access  the third party did not attend
The attending officer reported that the metal sheeting securing the window was pulled back and windows behind it were smashed 
Officer advised the alarm panel was unable to unset due to zone 73 being active 
Officer advised the site is manned 24/7
Officer advised there is a static guard onsite 
The officer advised there was a leak in the ceiling and caused the damage that is in the photo s attached 
Officer advised there was onsite security 
Officer advised there was security staff on site 
Officer reported the rear entry door was found ajar upon arrival 
Officer advised the site had already been locked and alarmed upon arrival 
Officer advised staff had already dealt with the alarm and were securing the site as he arrived 
The guard stated that contractors were on-site due to flooding 
Ongoing issue of damaged fencing 
Officer reported the issue with the broken barrier is still ongoing 
Officer reported the internal card locks were all flashing green upon arrival 
Officer advised the fob still does not work to unset the alarm so they were unable to carry out an internal patrol 
The guard stated that a window was left partially open on the ground floor 
Operative s phone went flat which meant he was unable to complete the job on Chase until back at office 
Cannot secure building as staff are on site working 
Attending Officer to confirm barrier is secure as site is not to be unlocked until further notice 
The attending Officer has reported that the lighting strip has become loose near Unit 45A 
The attending Officer has reported that on arrival Cleaners were onsite 
External patrol conducted only as Site Survey has not been completed for the site 
Attending Officer advised that staff are on site 24/7 
"Attending Officer advised that the card reader for door in photo was green and the door could be opened at will 
Most likely the door was overridden for contractos working on site "
Officer was unable to locate the CCTV 
Please find attached pic of the damaged frige as requested 
No water running on-site to flush toilets or taps 
Cannot run coke through dispenser as machine is not working 
Buckets holding water following previous leak are now full 
The officer was unable to add photos or fill out the mobile application report due to an error  full patrol completed no issues raised
The attending officer reported that the automatic gates are faulty  It is not locking correctly when the auto gates close  the gates don’t meet  This has been reported previously  This is an ongoing issue 
The Officer has reported that the Fire exit door was left open and so as the Office doors 
Report is FYI only  Site secured on arrival 
The Officer has reported that the front gates not closing and its now permanently open 
Unable to set alarm on the 5rh floor due to the area being sealed off 
Alarm set off in error by new employee at Blue Groove  Please note code C1784X not working however this code does work on the female toilets 
The attending officer has reported that the main barrier is broken 
The attending officer reported no key/access cards held for this site also  an old mattress was found near the main gates 
On arrival to site it was noted that a window was left open  The external doors left on auto and unlocked  Many light s left on all over building internal coded doors left on latches 
"The attending officer reported staff members on site alarm is unset 

Activation was from cable Chambers  internal patrol with staff member Lee Denyer all in order "
Attending Officer to conduct External of site  ensuring the barrier is locked and secure 
"Attending Officer was unable to enter site due to known health and safety issues with black mould 
This was reported in December 2020 "
"Attending Officer was unable to gain access into site 
Officer advised that the roller shutter was jammed and could not be lifted "
Attending Officer was unable to gain access into the shopping centre where the site is located 
The attending officer reported that the automatic gates are faulty 
The attending Officer has reported that a new padlock is required 
The attending officer was unable to complete the lock due to staff on site 
The attending officer was unable to complete the lock due to staff on site 
The Officer has reported that there was contractors working onsite 
Attending Officer to conduct an External check of site while dog unit is stationed inside 
The attending officer could not secure the padlock when leaving site due to the key not turning in the lock  Please see photo attached  
The attending officer reported that there is staff on site  they will lock the main gates when they leave 
"Attending Officer reported:
Damaged fencing behind skip - known issue 
Cable left on ground 
Gates unlocked on arrival "
The attending officer arrived on site and found the main barriers broken  Please see attached photos
The attending officer reported fly-tipping found on site  please see attached photo 
Staff onsite all night due flooding 
The attending officer was unable to complete the lock due to staff being on site  Tim the gardener will lock when finished
Attending Officer was advised by BT SCC Advisor Ilona to conduct an External check of site as it has been confirmed that staff are on site 
The attending officer has reported that the padlock to the rear carpark gate is not working
Maglocks on doors to floors switched off  Unable to secure door and one on 2nd floor keeps opening 
Staff onsite 
The attending officer reported that staff are still working on site 
The operative advised that no access was required as Vodafone requested an alarm check 
Site left locked as no 3rd party turned up 
Attending Officer to conduct an External check of site and make sure that barrier gate is locked 
Attending Officer advised that staff were on site on arrival 
Attending Officer reported that the service gates were found open on arrival  please see photo 
The attending officer reported that the front folding doors were very stiff to open  he had to barge his way in  on exit he was very nearly locked inside  His colleague has also had problems with this door 
"Attending Officer was unable to gain entry into shopping centre 
Shutte for centre down  locked and secured "
"Attending Officer advised that contractors from Amida Fire and Security were on site working on the security system 
Static Guard also on site 
Please see photos of ID s "
The Officer has reported that Contractors are working onsite all night 
"Attending Officer advised that the panel on the 5th floor cannot be set as the door to area is sealed 
Known issue "
Attending Officer was unable to secure the side gate  please see photo 
The attending officer reported the gates are broken 
The guard stated that the gate is broken on site 
Attending Officer reported that the Main vehicle gate is broken and cannot be automatically or manually operated 
Attending Officer reported fly tipping at back gate  please see photo 
The attending officer reported that the gate has a padlock missing 
Attending Officer to conduct an External check on site while Dog unit is stationed inside 
The attending officer reported that he was unable to set the alarm because the system is not accepting his PIN 
The attending officer initially completed the job with incorrect on/off times from site 
The attending officer has reported there is a flooded area  He was also unable to secure the main gate
The attending officer advised that the cable chamber is flooded 
Officer reported the panel was set on arrival confirmed by BT ref Leah
Attending Officer advised that the panel was unset on arrival 
The attending officer advised that the card reader is not working 
The attending officer reported that there is fly-tipping on site 
The attending officer reported the fire door exit was left opened  He has secure the door 
Attending officer reporting while patrolling site they found several internal doors had been left open  fire alarm panel was not set either 
The attending officer reported a rough sleeper in front of the building
"Attending Officer reported:
Damaged fencing behind skip - known issue 
Cable left on ground 
Gates unlocked on arrival "
Officer advised the rubbish dump is overflowing 
The guard stated that the bin is full on-site 
"Attending Officer advised that the gate has been secured with zip ties 
Please see photo "
Officer reported alarm was not set on arrival
Attending Officer reported staff on site 
The attending officer reported that half of the gate was missing 
The attending officer reported that half of the gate was missing 
"Attending Officer reported that the bottom runner on the gate is damaged  please see photo 
Previously reported "
Attending Officer unable to secure barrier due to ongoing issue 
"Due to current Covid conditions  Attending Officer to conduct an External check of site 
Site is staffed 24 hours "
The guard stated that the gate was open with no padlock on it 
Officer reported there is a flood in the basement 
Officer reported a Tesco s trolley had been fly tipped next to the main gate at the rear of the site 
The Officer has reported that some Wood was missing from the Fence panel at the back of the yard 
Officer advised Howard house alarm is unable to be set 
On arrival on site  the officer found the site gates open  After a check of the site  no staff was found 
The attending officer reported a missing padlock on the main gates 
Attending Officer reported cable left on trailer 
Attending Officer reported cable left on trailer 
Attending Officer unable to secure main gate due to fault 
The operative advised that the padlock to rear gates on Caxton Street are not working so the gate cannot be locked 
The operative advised that a member of staff and cleaner were on site working 
The operative advised that the staff didn t have any keys to handover available 
The operative advised no guard turned up for them to give access 
The officer was onsite to complete the access  however  no contractors showed at the agreed time 
The attending officer has reported that no one had shown and up 
The service partner attended to site and reported to collect keys from point of Air gate house   he was told by security the barrier will remain locked until further notice 
The operative reported that there was a member of staff on site 
Keys no longer held at provided address  Previously reported 
"The officer has reported the following issues noted on the VPC; 
Intruder alarm - panel displaying engineer reset is required  Tamper Key 22  the officer was able to override and set the alarm but engineer may need to attend if required  
Fire alarm the panel is showing a fault -  Zone 16  may require an engineer  
Puddle of water when the main shutter raised   no sign of a leak  possibly due to snow "
Attending Officer to conduct an External check for CCTV activation 
The officer has reported that water is on the floor under the sinks on the 1st floor ladies toilets  It appears that the out let pipe may have a small leak 
Attending Officer advised that Static Guard Sardar with Expeditious Security was posted at entrance to site 
Damaged fence has previously been reported  Staff on site
"Client previously multiple times reported 

Secondary fence line hole that has been reported by other officers"
There is a big hole in fence on main road on high elms site
The attending officer has reported  that staff on site required a later lock up than booked as they were still working 
The officer is reporting that the door does not close full  no sign of intrusion  Staff will be contacting NHS Property services to arrange for an engineer to attend to fix the door 
No staff or guard arrive at the site 
The beach barrier is to stay closed until further notice
Officer arrived on site and was met by a static guard no patrol needed as authorized by Darren at RVR
The attending officer has reported a new breach in the fence line 
"The main gates to the entrance are unable to be locked due to roadworks 
The service yard gates were locked but the dominos staff opened and left them wide open"
The attending officer was unable to complete the lock due to barriers around a hole in front of the gate is blocking him from closing the gate 
The attending officer attended site and reported that the main shutter window was found slightly shattered  Please see photo s attached to the job 
The service partner holds no keys foe this site  Unable to gain access  All appears secure
Mitie booked this third party access with no notice and when the ADT engineer was on site to attend to an alarm issue  By the time the officer had arrived on site the ADT engineer had left site and booked to return at 23 00 
"Basement room number PDK DB07 large flooded area  
This has previously been reported to Bizspace  
Water looks as if it is coming through a wall - officer unable to turn off water or stop dripping in  not a flow of water  it is a drip "
The attending officer reported that the fence line by the skip at the rear the site is damaged 
The attending officer has reported that the gate was found broken 
The officer reported a ground floor window has been left open
Virgin media security team who advised staff rear door open external patrol completed no internal Patrol as internal was alarmed secured staff door advice to stand down alarm set site secure on departure
"Officer in attendance did not hold the keys for the site  Was only carrying out an external patrol before an officer with keys could attend at a later point   
Capita cancelled the attendance before the key holder could attend "
No  staff arrived for this unlock
The guard stated that staff were on site 
The guard stated that the site was closed and no staff turned up for the drop off 
This unlock has been booked when it is  high tide when the gate is to stay closed
Right hand side fence line has been cut  this has previously been reported -snipped the whole fence all the way down the perimeter of the right hand side These hole cannot be driven through but an intruder could gain entry by the tree line  
The attending officer raised the issue in error 
The service partner attended to site  The police had already visited and left the site  The police gave the all clear to the NHS   The service partner spoke to NHS who advised the alarm had reset so there was no need to enter the site 
Letter box not sealed  damaged windows  signs of a water leak and loss of power  refer to photos for more information 
"Attending Officer reported:
Lock broken on Main Entrance door - unable to be locked 
Handle on Door 5 broken - unable to close or lock 
Tree fallen onto fence line "
The officer has reported this several times- They are unable to secure the main entrance gate as the wheel on the gate is broken and the gate cannot be lifted  All other gates can be secured 
The guard stated that the padlock and chain to lock the barrier is missing 
Staff on site  system already reset by manager 
The attending officer locked and secured the external gates only
The guard stated that both doors in the pictures attached were left unlocked 
The  silver doors  no entry cannot go in -that door had been left wide open
The attending guard has reported that the padlock on the main gate is broken 
The attending officer has reported that the main gate was found broken 
The attending guar was unable to access site due to snow and ice on the road  Please see picture attcahed 
The guard advised that the side fencing has been cut as seen in the picture attached 
The attending officer reported that the fence is cut in several places  photo of the issue attached  
Officer arrived to site on time  but nobody came on site from ADT 
Adt engineer failed to arrive  Contra charge for 1 5hrs on site and associated parking costs as per image attached
Service partner has advised  this was not an intruder is was staff on site 
Attending Officer reported staff on site on arrival 
Officer advised they were unable to unlock the building due to high tide 
Officer advised they are unable to complete the unlock as the site is closed 
Officer was instructed to carry out an external patrol only by Finn at BT seurity 
Our officer was unable to reset the alarm 
Officer advised the site was already secured upon arrival and no contractors onsite 
Officer advised the guard onsite was not well and police were called to site and the guard had to be taken to the hospital 
Ground works are being carried out   so officer unable to close gates
Officer was unable to set the alarm 
Officer advised they are unable to secure the front and back gates as works are bing carried out at the front and drivers are still onsite 
The old damage  previously reported in the street side of the double glazed window is now more damaged than before and requires attention 
BT informed the officer that they only wanted him to carry out an external patrol
Canteen Door is not shutting completely  it s a magnet door and magnet is not working  It shuts but doesn t require door release for it to work 
Unable to lock the site as a guard is onsite due to contractors working 
The officer attended to site and staff were still there 
Staff member onsite by the name of DR Greggson had already dealt with the alarm and advised they had called TKC to stand this alarm down 
staff were onsite upon arrival 
Attending officer reporting a burst water pipe at the junction of Motram Road which leads in to the car park has caused an ice patch running right down from the junction to the car park 
The pedestrian and loading bay gates are not securing  Engineer required 
Officer whilst on site spoke to BT Security in relation to previously reported damage and advised of a vehicle which was unlocked on site
Officer was unable to secure the gate as it is faulty 
An internal patrol had been booked  but there is no building to patrol this is a compound  All site appears secure 
"Job stood down as SP arrived at site  Unfortunately  not enough notice was given to cancel the job 

Reason for cancelled was that the engineer was unable to attend "
The attending officer advised that on arrival there was staff on site 
Could not leave site secured as staff were still on site working  
The attending officer called to advise that BskyB will not grant him access as the alarm has been cancelled 5 minutes later after it was booked on at 09:58  The officer was stuck in the snow on the road and called at 10:23 to advise that he will be delayed for 1 5hr - at 10:23 Mitie have been informed of the issue  however  no one told us that the attendance has been cancelled 
The entry door has dropped  making the door very difficult to unlock and lock
The attending officer attached the picture by mistake when he was finishing the job on site 
Officer advised there are staff onsite until 0400
Officer reported there is a water leak onsite which may be the cause for actvation 
Officer had a issue trying to reset the alarm due to a faulty panel 
Officer reported the gate is still faulty so unable to secure 
Attending officer reporting they were unable to secure site due to delivery drivers still present 
Officer reported a fault with the security tag detector as it kept flashing intermittently 
Officer was unable to secure the site as there are staff onsite until 0600
Officer reported there are staff onsite until 0600 so they are unable to secure the site 
Officer reported the issue with the fob setting the alarm is still ongoing so they are still unable to reset the panel 
Office reported there are AA staff onsite 
Ongoing issue of damaged fencing by the skip 
Officer reported there are no gates to secure 
Officer reported travellers have now left site however have dumped rubbish 
Attending officer reporting they were unable to secure site as staff still present who advised they will secure site upon leaving  Marcus Day  facilities management  preent 
Attending officer reporting youths have been hanging around on site  they clear off during patrols but keep returning once our officers leave site 
The officer has reported that there are cleaners on the site  Monday to Friday in the days and evenings  The officer did not secure the site upon departure due to cleaners being on site 
The attending officer reported that on arrival a cleaner was working on site 
The officer has reported that the staff advised they were not ready when attendance was made 
The officer reported that they did not attend with keys due to an admin error and could only carry out an external patrol 
The attending officer advised that there is a contractor on site
The attending officer advised that the contractors failed to attend 
The attending officer advised that the alarm panel needed an engineer reset 
The attending officer advised that there was staff on-site  however  the engineer failed to attend at the requested time 
The officer has reported that staff was on-site on arrival  The officer spoke with the receptionist 
On arrival  the attending officer met with the office manager Karen Pugh 
Attending Officer advised that site is not opening today 
Fire alarm panel in fault - Final report on building   Include pictures of area  : all taps and toilets run building secure
The attending Officer has reporetd that Mitie Staff onsite this week until Friday 
"The attending Officer has completed both Internal/external patrol and found no issues to report 
However the Officer has advised the Road work outside the building could be the reason for the activation "
Attending Officer conducted an External check for a CCTV activation 
Attending Officer advised that staff will be on site until 0600 hours 
Attending Officer advised that staff will be on site until 0600 hours 
"Attending Officer advised that cleaner Mariah was leaving site on arrival 
Mariah advised that the alarm activated as she entered site "
Damaged fencing behind skip - known issue 
Attending Officer unable to secure gates due to known damage 
The officer has reported that a Static Guard was onsite 
The attending Officer has reported that there was a Static Guard onsite 
"Attending Officer was unable to locate the alarm panel in the Humanities Block 
AI s state it should be located in the electric cupboard RHS of entry door "
"Attending Officer reported broken fencing at the rear of the site 
Please see photo "
The attending officer advised the alarm fob does not unset the alarm 
Attending Officeradvised that the main keypad in reception is worn and needs replaced 
Alarm booked in error by KHC
Staff member Chris was on site working with 3 other persons 
The service partner could only do an external patrol due to the alarm system been in communications failure 
Attending officer has reported contractors were on site  Possible power outage in customer service area on site
No 3rd party arrived at site for admittance 
Temporary security officer located at site  He is unaware of the location of the keys  Unable to carry out tasks required 
The attending officer has reported a leak in the basement 
As per the client s request to check all external doors  and the site is set up for external response only   No internal was carried out 
The attending Officer has reported a water leak on the stairs entrance premises 
The attending Officer has reported Staff onsite  Guide Singh  
"Attending Officer was unable to lock site 
Dominos delivery drivers still on site 
The coded padlock has also been changed  updated code needed "
Attending Officer advised that contractors from PHSP Dixon were on site conducting testing 
"Attending Officer reported a water leak on site 
Please see photo "
Staff onsite 
staff onsite
"Attending Officer reported damaged to the fencing  please see photo 
Officer noted this may be old damage "
Attending Officer advised that the electronically controlled entrance gate is open 
Attending Officer reported that staff member Saleh Ahmed advised the officer that a meeting was currently in progress 
"Attending Officer reported signs of fly tipping on site 
Please see photo "
Attending Officer to conduct External check of site while dog unit is posted at site 
The operative advised that staff were on site 
Officer advised the alarm panel was not showing anything upon arrival 
Attending Officer advised that a fire alarm activated and all were told to keep a minimum safe distance 
External patrol completed and found all in order 
Officer reported the cable chamber had been flooded 
The basement has flooded  the officer updated BT Security when on site  This restricted the officer s access to patrol the building    basement e by the entrance stairwell 
The attending Officer has reported that there was a Van onsite with the lights on 
Attending Officer has left alarm unset as instructed by BT SCC 
The attending Officer has reported that a bird was seen on the 4th floor 
"Attending Officer reported:
Damaged fencing behind skip - known issue 
Gates unlocked on arrival 
Cable left on ground "
The main front gate can’t slide back  however there is an onsite security 
Attendig Officer reported a static guard on site on arrival 
The Officer has reported that the panel was in  Alarm  mode 
The officer who was completing his patrols has noticed the rear double doors of the property as being left open quite often  the officer is concerned as the doors lead out to the car park which would make access easy for anyone trying to gain entry into the site 
The black pedestrian gate lock does not always secure properly on leaving  lock needs attention by BT maintenance  WD40 and elbow grease required
The Officer has reported that the bin was over flowing 
The attending Officer has reported that the portables Fires left on yet again in Staff area 
Attending Officer unable to secure gate because there is no padlock  known issue 
Unable to secure the main gates as there is no padlock 
Attending Officer advised that rear Fire Door  GFO 014  was not securing 
Attending Officer was unable to load photo due to phone error 
Attending Officer unable to take photos due to phone error 
Attending Officer reported cable left outside of the bays 
Attending Officer reported he was unable to load photos due to phone error 
The attending Officer has reported that Vagrants were seen onsite 
The Officer has reported a smashed rear window 
Attending officer reporting they were unable to secure site due to staff present 
The guard stated that they could not find the stop cock on site 
The attending officer has reported the water is switched off in the shopping centre so taps cannot be run/toilets cannot be flushed 
Attending Officer advised that site is currently closed 
Attending Officer advised that the alarm was found unset on arrival 
The attending officer has reported a leak from the ceiling  A container had already been placed to catch water 
Site has been sealed and boarded up  No access for inspection 
Attending Officer advised that a smoke cloak activated as he was walking to the panel for unset 
"Attending Officer reported vandalism in the male toilets 
None of the porceline has been damaged "
"Attending Officer to conduct an External check for an external gate seen open on CCTV 
Officer found manual gate open on arrival "
"Attending Officer advised:
Damaged fencing behind skip - known issue 
Cable left on ground "
Attending Officer advised that both fire escapes have been boarded up and has caused an activation on the panel 
"There are contractors working on site  removing the hoardings  They have managed to unset and reset the intruder alarm  
Our officer noted the codes for the alarm system we hold are outdated"
Our officer reported the static guard was not on site 
The operative advised that there was water leaking at the back of the building on the back wall 
"Attending Officer reported a water leak at the back of the site 
This may pose a hazard if the water freezes "
The attending officer has reported the homeowners were on site and therefore could not carry out any checks 
The operative reported that the hot water tap was left running and they used the mop to clear the water 
The operative reported that door 301 would not close properly 
"Attending Officer advised that the red internal shutter is open  no power to shut shutter 
Main metal shutter  in front of red one  is locked and secured "
Attending Officer found Unit 12A open on arrival 
The operative advised that the automatic doors were not working 
The operative advised that there were signs of travellers 
The attending Officer has reported the damage to the fencing on site as previously reported 
Attending Officer unable to secure gate due to ongoing gate issue 
"Attending Officer unable to set alarm due to staff on site 
Also reported that the back gate open on arrival and will not close "
Attending Officer confirmed that the hole in the fencing has not been repaired yet 
Attending Officer confirmed that the hole in the fencing has not been repaired yet 
The officer has reported that the alarm code we currently hold is invalid 
Our officer arrived and found that staff were already on site   Ben Demolli 
"This job is booked in as an unlock  however  the service partner attends to make sure the day guard has arrived and unlocked 
The day guard had not arrived by 06 15   The officer did not unlock the site and had to leave for a Fire alarm elsewhere 
There was a member of staff on site  name not given  who was waiting in their car to gain access "
The operative advised that there was water leaking at the back of the building on the back wall 
The officer attended to site but the service partner has no assignment instruction s   they do have keys but they have never completed a site survey  they called the client to establish where the alarm panel was  unusually it was outside of the building 
Attending officer reporting they were unable secure the main shutters due to 3 staff members still present  they advised they will secure upon leaving site 
Attending officer reporting they were not required to complete internals of site 
Attending officer reporting on going issue with being unable to set the 5th floor alarm due to the door being sealed off 
Attending officer reporting they were unable to complete due to staff requesting they return at 2030 
The service partner attended to site and there was no power to the property or alarm panel  ABCA organised an engineer to attend who could not reeolve due to lack of power 
Attending officer reporting several issues including gates unsecure  damaged fencing  unsecure copper cabling on site and 2 vehicle left unlocked 
Attending officer reporting hole in perimeter fencing  issue reported previously 
Attending officer reporting on going issue with hole in perimeter fencing 
test property
Geoff Power was on-site when the guard arrived and advised that we should not be attending after 06:00 
The attending officer reported that there is an issue with the alarm system 
Attending officer reporting internals not required 
Attending officer reporting they were unable to complete unlock due to site being closed 
Attending officer reporting they were unable to complete internal patrols of site due to the remote not opening the shuttering 
The main door is not operating and in need of attention 
The guard stated that there is no padlock for the chain on the gate 
Attending officer reporting they were unable to complete internal patrols of site as not requested by BT 
"The service partner has reported this issue on two previous occasions 

The staff are exiting the building through Fire Exits  They are not securing the exits correctly  there fore the site is open and vulnerable prior to the service partner attending to lock up  Thus repeated alarm activations "
Attending officer reporting internals of site not required 
Attending officer reporting they were unable to secure site due to contractors/guard present until 6am 
Attending officer reporting 1st floor entry door lock is becoming difficult/problematic to lock  maintenance recommended 
Attending officer reporting they were unable to secure entrance due to Maglock broken 
Attending officer reporting several issues including vehicle left unlocked on site  damaged to perimeter fencing and gates  copper cabling also left unsecure on site 
Attending officer reporting hole in perimeter fencing  issue reported previously 
Attending officer reporting site locked and secure upon arrival 
Attending officer reporting they were unable to secure site due to Mitie guard present on site  Alarm also triggered by contractors working on the 3rd floor 
Attending officer reporting they were unable to complete internal patrols of site due to staff present 
Attending officer reporting they were unable to service the alarm panel due to no information held 
The waste pipe has a water leak in the cupboard under the microwave in the kitchen  The service partner cleaned up leak as best as they could 
Our officer reported that the padlock was frozen solid and was unable to rotate the numbers to complete the unlock 
"The officer attended to site and forgot the keys 
This job has been completed as an External Patrol  yet the officer returned to the site later and everything is ok on site"
no water running on site to flush toilets or taps 
Attending officer reporting water leakage outside the ladies toilets  images attached 
Leak on site  Ceiling has fallen in as result  Please see photos 
The officer has reported that the fire alarm is in fault and is constantly beeping  The officer has no access to the panel/key in order to stop the sounding 
The officer has reported an ongoing issue with the fire alarm panel  Advised fire alarm zone 12 was sounding 
"The officer has reported a number of issues on site  
1  The officer could not enter the manager s room   
2  Constant loud beeping in the battery room  
3  Machine in the Switch room  projector area beeping loudly
4  Not hot water in WC toilet  in screens area  Water pressure too low 
5  No water in taps may have been turned off from the stop cock "
The attending Officer has reported that the Coke machines were switched off and there was a leak near the Coke machine 
Attending Officer reported that the water has been shut off to the building 
Fire alarm system has been disabled so unable to see if system working  Drink dispensers are on an electronic system with no swipe card 
Attending officer reporting issues closing box 1 rear shuttering 
Attending officer reporting they were unable to complete internal patrols of site due to power cut  no access beyond the shuttering 
Attending officer reporting they were unable to complete lock up of site due to contractors working until 6am 
Attending officer reporting while patrolling site they found one of the toilet roll holders had been vandalized and knocked off the wall 
The guard stated that a Dog unit is on-site and did not allow access to the guard 
Attending officer reporting copper cabling left unsecure on site and also the handle to the gate is missing 
The guard stated that there is damage to the fencing on site as previously reported  Also  the vehicle in the picture was unlocked 
Attending officer reporting they were unable to secure the gates due to staff present  gates also broken 
Attending officer reporting they were unable to secure the gates on site due to them requiring repair 
Attending officer reporting reporting both entry and exit gates have technical faults preventing them from closing 
Attending officer reporting reporting both entry and exit gates have technical faults preventing them from closing 
Attending officer reporting they were unable to provide requested access due to contractors already completing works upon arrival 
Attending officer reporting they identified several water leaks on site  images attached 
Attending officer reporting they were unable to provide requested access due to engineer no show 
Access given  no issue  Report is FYI only 
The attending officer reported that on arrival the main gate was open  Also  the door handle for the warehouse is broken  The officer stated that he is unable to set the alarm panel due to a fault 
The attending officer advised that upon arrival he met with the site guard who advised him that the engineer has already completed his tasks and left the property 
Set alarm twice  however it keeps reactivating due to contractors drilling next door which sets off the vibration alarm 
The attending officer reported water spillage over one of the machines on site  The officer also had an issue with the alarm panel and he could not set it properly 
Service partner attended site however contractor had left  Partner contacted contractor directly who advised they would not be returning 
The attending officer advised that he was on site from 08:20 to 09:18  The engineer did not arrive and was not contactable on the number provided 
The attending officer advised that the site is fully operational and there is staff in the building  therefore he was unable to lock the property 
The guard stated that the 5th-floor door was not locked when they arrived 
Officer advised the alarm is in fault so they were unable to carry out an internal patrol 
Officer reported the inner door s magnetic lock is faulty 
Officer reported upon arrival there was an AA driver onsite by the name of Rob who was dropping the van back 
Officer reported an ongoing issue whereby the gate is faulty 
The guard set the alarm from the outside panel 
Officer advised of an issue whereby th4e gate is broken/damaged
Officer advised staff were leaving site upon arrival 
Officer reported he was unable to set/reset the alarm with the code given  when he entered the alarm code the panel was unresponsive 
Officer advised the site was eft unlocked due to iss technical staff being onsite and an iss guard 
Attending officer reporting while patrolling site he identified a window which had been left open  image attached 
Officer had an issue with trying to set the alarm 
Officer reported an ongoing issue of damaged fencing 
Attending officer reporting they were unable to secure the gate  the engineer who attended site to repair it advised it requires specialist attention 
Attending officer reporting they were unable to secure main entrance gate due to them requiring repair 
Officer reported the unit next door to Hyva is vacant with an unlocked gate that you can follow around that leads to an unlocked fire exit gate to Hyva 
Officer reported an issue with trying to reset the alarm
The front door maglock is not engaging which has caused alarm to activate  Site is still secure as the large sliding wooden door is still fine but this could possibly cause further activations if not fixed
Officer attended site and contacted ADT to find update about the engineer  ADT advised that no engineer was booked to attend 
staff on site accessed fire door due to same issues as yesterday 
The attending Officer has reported no one was onsite and therefore the Unlock was not completed 
Site is not open so unlock was not required
Builders working above store  whilst on site can feel floor vibrating
The officer is unable to secure the small pedestrian gate due to the padlock being missing
Attending officer reporting they found the main gate open upon arrival 
The security officer is reporting that the alarm for this site does not get set 
"Attending Officer reported that the ground was quite icy and should be salted 
Please see photo "
Officer is reporting panel of fencing is still missing from the site
The Officer reported that there is a small leak in the toilet on the 4th floor 
Attending officer reporting a leak in the lady toilets on the 2nd floor  Officer also unable to reset alarm 
Attending officer reporting signs of travellers within the local area 
Attending officer reporting reason for activation was due to staff leaving one of the doors open 
Whilst completing the external patrol the officer was reporting a large amount of cable outside of the cable compound and staff onsite
Attending Officer reported that the alarm was not set on arrival 
Our officer advised he was unable to set the alarm 
"Attending Officer found a door unlock during the External patrol 
Please see photo "
The officer reported that the gates on site are normally closed and on this occasion they were open
Attending Officer advised that workers were on site on arrival 
The entry gate is broken  unable to sure site 
Attending officer reporting they were unable to complete internal patrols of site due to staff present  Officer also reports gate needs repairing 
Attending Officer reported that the Front Main Gate has jammed and would not slide closed 
The main gate cannot be secured as it will not move back into the closed position appears to be a technical issue
The officer is reporting that the toilet appears to be clogged causing it to flow out of the toilet 
The officer is unable to secure the entry gate as there is no padlock
Officer was unable to secure the gates as there was no padlock 
Attending officer reporting cabling has been left unsecure on site 
Officer attended to hand keys over  no one attended to collect the keys 
Attending Officer advised that the doors on the 5th floor were not locked 
Attending Officer advised that there was an active tamper fault for the stairs 
Attending Officer advised that the maglock is not working on the front entrance door 
Attending Officer reported that Rear Shutter 1 would not open 
Ceiling panels have fallen in the staff changing room  Panels are now dry  however  staining shows that it has been caused by water damage  Currently no leaking water 
The Officer has reported that the pedestrian gate is on free access next to the loading bays 
Damaged fencing behind the skip  ongoing issue  
The Officer has reported that the gate is still broken 
The Officer has reported an issue with the entrance gate as it stays open 
No alarm codes or site details held 
The operative advised that no staff turned up for the unlock 
The operative was unable to reset the alarm panel as a manager reset was required 
Thrid party was a no show 
No alarm active 
The attending Officer has reported that Staff or onsite Security were present onsite 
Site not open 
Site not open
"Attending Officer was unable to gain entry into site for an Internal check 
Dog unit on site 
Gate locked and chained "
Attending Officer advised that the yard needs gritting - black ice present 
"Damaged fencing behind the skip  ongoing issue  
Cable left on ground "
Attending Officer unable to secure gate as it is still broken 
"Attending Officer unable to secure front gate 
Front gate faulty 
Advised BT SCC of the same "
Attending Officer was unable to read the padlock numbers as the lock was facing inwards 
Officer advised the site was not to be opened 
Attending Officer reported that he was unable to get through to the control centre on arrival 
The officer arrived at site to complete the unlock but no staff or onsite security arrived 
Site was not due to be opened 
officer found a leak on arrival  see photo
"Attending Officer to conduct an External check of site 
BT SCC authorised an External check due to CCTV activation "
external gates only closed
officer reported all ok on site
Attending Officer reported no active signs of travellers in area 
Officer is unable to add photos to the mobile application due to an issue with the phone
"Attending Officer reported:
Damaged fencing behind the skip - known issue 
Cable left on ground "
Attending Officer unable to secure gate as it is still broken 
"Attending Officer unable to secure front gate 
Front gate faulty 
Advised BT SCC of the same "
Attending Officer reported site locked and secure on arrival 
"Attending Officer to conduct External check of site until Site Survey can be completed 
Site Manager was off when Site Survey was scheduled; staff on site were not willing to conduct survey without manager "
Attending officer advised the lock for the shutter door is broken 
Officer advised the unlock was not required today 
Officer reported no iss officer turned up to site 
Attending officer advised the alarm fob does not work 
No staff on site so the site was unable to be left unlocked/unsecured 
Officer reported they are unable to lock the revolving doors as the panel for the fob does not work 
Attending officer reporting no requirements to complete internals 
Our officer reported no one was onsite 
Attending officer reporting upon arrival to site over the last few days the site has needed to be locked and alarmed  jobs booked only as external patrols at present 
Officer reported there fencing to the rear of the site by the skip is damaged 
The service partner attended to site  a site survey has not yet been carried out or keys provided for this site  The service partner reported there are 2 windows open ant the top of the glass entrance to this site 
Attending officer reporting they were unable to complete the unlock due to engineer requiring access not present 
The attending officer reported that he waited from 08:00 until 09:30 on site  but no one arrived 
Attending officer was advised by concierge that the site was not meant to be unlocked at all over festive period 
The attending officer advised that there was no need to unlock the site as the request was for site patrol only 
The attending officer raised the issue because the mobile app requested a photo from the internal patrol of the property  however they are required to unlock only the external gates and therefore the issue was raised 
Alarm codes incorrect  Unable to unset/reset alarm 
The attending officer advised that on arrival the building was unlocked and the alarm was disarmed  He reported that there might be staff that came in earlier 
"Attending Officer conducted an External check of site 
No keyholder on site for escort "
Attending Officer reported that the locks were frozen due to the weather 
Attending Officer unable to locate student 
Officer only has keys to unlock external gates 
The attending officer reported that on arrival there was staff on site 
Attending Officer reported no active signs of travellers in area 
"Attending Officer reported:
Damaged fencing behind skip - known issue 
Cable left on ground "
officer was unable to secure the gate as it is broken 
Officer reported they are unable to secure the gates due to technical issues 
Attending Officer reported that both entrance and exit gates are having technical issues 
Officer reported the site was already locked on arrival 
Officer reported he had to force open the front door a sit gets stuck on the lock 
Staff and Parents were on site
Officer reported the intruder alarm was going off on the 5th floor to which thy have no access to as no codes or fobs held 
Officer reported there is a new padlock on the gate to which they do not have a code for so they had to jump over the gate however the alarm fob was not working to unset the alarm 
The operative advised that there was a leak coming from the roof 
Officer reported this was a telephone welfare check only 
Attending officer reporting the padlock for the main gate is becoming harder to open the colder the weather gets  officer reports they are struggling to open the gate to the point they are worried the key is going to break in the padlock 
The heaters are coming on and blowing the round signs that read   New 2020   
Thee area is blocked by 4 police cars due to a big fire in the area  The client  s building has been entered by the fire brigade so they can go on the rooftop and use the fire extinguisher 
Officer reported there were no keys in the keysafe for unit 19 only no 17 
Attending officer reporting they were not required to complete internals due to store manager Dan Bell being present upon arrival 
Attending officer reporting no internals required due to fail to set activation with panel being accessible externally 
Officer reported the shutter located inside the compound wont come down however the site is secure  It appears to be frozen from snow 
Attending officer reporting they were not required to complete internal patrols of site due to access only due to locked out from property 
Attending officer reporting they were initially unable to close the loading bay shuttering 
Officer reported one of the storage buildings door was left open  the lock is locked so unable to release it to secure it 
Attending officer reporting they were unable to set alarm when leaving due to not required 
Attending officer reporting signs or travellers in the local area 
As previously reported the gates were unlocked and the fence is damaged  Also  there is a copper cable left unsecured 
Attending officer reporting while patrolling site he identified unsecure copper cabling left on site 
No site survey carried out  Officer unable to enter property 
An engineer found working on site 
Attending officer reporting upon arrival they found site had not been locked from the day before 
Attending officer reporting they were unable to securely lock the front barrier due to it being damaged  Officer also advised the service yard was left open by Domino s 
Officer reported the alarm wont set and this is an ongoing issue  Officer also reported the automatic door fob reader is not working internally and they were unable to lock the revolving door as it was the only entry point to the site 
Officer reported the door would not secure 
Office reported they were unable to secure the gate
Officer reported he was unable to secure the back gate as the padlock is broken 
Officer reported unit 10 was left open 
Officer reported the fence posts next to the entrance have been bent 
Attending officer reporting they were unable to set alarm before leaving site due to staff present 
Attending Officer was unable to reach the site for this scheduled patrol due to icy road conditions 
Our officer reported he was unable to secure the main gates due to a fault 
Officer was unable to set the alarm 
officer reported the alarm was not set on arrival
Attending officer reporting they were unable to complete internal patrols of site due to swipe card not allowing access  officer also reports due to tech issues they were unable to take images 
Attending officer reporting several ongoing issues on site including unsecure gate  damaged perimeter fencing and Copper cabling left on site  Officer also advised vehicle left unlocked on site  image of vehicle attached 
Attending Officer unable to set alarm as staff member Garry Bonnet 391499P was on site 
Attending officer reporting signs of travellers in the local area 
Please see photos of gates
officer was unable to secure the gates due to there being no padlock 
The officer reported that staff was on-site upon arrival  KHC did receive a call from Mitie to cancel the alarm due to staff being on the site but the SP was already there 
Officer reported the building has no alarm - staff were onsite  they patrolled the whole building and no keys fit the doors 
The attending officer reported that the site was closed earlier and the site is locked 
Officer reported they were advised by a resident living above the bank that they have no electricity and this has affected the electricity within the bank
The attending officer updated KHC regarding the issue  The officer is with the engineer - the alarm is split into 2 areas A & B the engineer has rectified area A  but they cannot set area B 
Attending Officer reported no staff or guard present 
"Attending Officer advised that no guard on site 
Site closed today "
The officer has reported that we were unable to set the alarm 
Attending Officer reported that no staff or guard present on arrival 
The officer attended to site following an alarm activation - zone 8 not restoring  the officer called BT security whilst on site and BT advised that they were unsure as to why we were asked to attend
Attending Officer advised that staff member Mr  Tom was on site on arrival 
"Attending Officer to conduct an External check for CCTV activation 
Officer noted that the entrance way had been blocked  please see photo "
Attending officer has advised there is no alarm panel on site 
"Attending Officer reported damaged fencing and a broken window on the entrace door to site 
Please see photos "
Attending Officer reported a spider at the PIR stairs is the likely cause of alarm 
Attending Officer reported vandalism and damage to the toilets on arrival for his regular lock up of site 
Attending Officer reported some pictures had fallen off the wall causing the alarm 
"Attending Officer reported a water leak on the third floor 
Please see photo "
Attending Officer did not set alarm as instructed by BT SCC 
Damaged fence behind skip  ongoing issue  
Attending Officer reported the car park gates locked on arrival 
"Attending Officer reported a leaky roof on the second floor due to the storm 
There are a few wet patches of carpet 
Basement storage corridor door found unbolted "
"Attending Officer locked the second floor atrium 
Officer advised that this area is being used as a smoking area "
The attending Officer has reported that Staff were present on arrival 
The service partner has attended to site  there is no need for an alarm engineer - it was noted that 2 zones have been omitted  But more importantly  there is a water leak in the mens toilet near the office 
Attending Officer reported that the site was closed 
Internal door hanging off of the hinges  This has been previously reported to BT
"Attending Officer unable to gain entry into site 
Confirmed power loss in area"
"Attending Officer reported the gates open on arrival 
The padlock has also been damaged 
Please see photo "
Attending officer advised zone 4068 activated but there is no zone map and no description on the alarm panel  Officer could not access nursery or beauty area as the access codes do not undo the maglocks 
"Attending Officer advised that the wind is causing multiple false alarms at site 
Site has an external intrusion system "
"Attending Officer reported staff on site on arrival 
Staff member Mr  Malik will be on site until 0600 hours  works with the homeless "
Attending Officer to conduct an External check of site until a risk assessment and route access are completed 
"Attending Officer was unable to enter site 
Entrance door has been turned into a collection point 
Please see photo "
Attending Officer reported that homeowners were on site on arrival 
Attending Officer to conduct an External check of site as it is still mobilising 
Attending Officer advised that photography is not allowed on site 
"Attending Officer to conduct an External check of site 
Key for front door does not allow access "
Attending Officer advised that the padlock loop has not been repaired yet 
The attending officer reported that he cannot set the alarm  On exit the fob reader is not working on the automatic side door  the revolving door isn t gonna be locked due to the fob reader on the automatic door not working and it  s the only exit point 
Officer struggled to find site with post code and site description provided 
"Attending Officer to leave alarm unset as per instruction from BT SCC 
Gates found unlocked on arrival "
The attending Officer has conducted an external patrol and found all in order 
Attending Officer noted the following: window open 1st floor no  5 and 2nd floor no  4
"Attending Officer reported the following:
Leak in glass ceiling on second floor 
Leak on inside of doorway Fire Exit by B250 
Middle roof door between B and A found open  but secured by padlock   High winds is likely cause "
The Officer has reported that the current alarm fob held does not work 
Staff did not show up to site so it was unable to be left unlocked 
The officer has reported that staff did not arrive on site for the scheduled unlock as booked 
The officer has reported that the keys held do not work  they also tried the front shutter  left and right side   The officer also reported that no third party arrived on site  please note this activity was clicked in error  The officer also reported that we do not hold an alarm fob/ code for this site 
Officer advised a key was left in the padlock for the gate This was left in the harris fencing near the main gate and that  the main entry point was blocked off with gates/ pallets
"Attending Officer advised that the ISS Guard was not on site on arrival 
Guard is starting late today due to holiday "
No ISS officer on-site 
This job was not unlocked as the site was closed and the Land Registry had not cancelled the job on CHASE
"Attending Officer reported that the eye loop that the padlock secures to has been damaged  looks like it has broken off during the night 
Padlock is intact "
The officer has reported that we do not hold an alarm code  or have an alarm fob on the keys held 
lose handle on the door 5 
The Officer was unable to reset the alarm panel as Mangers reset was required 
The London Fire Brigade were in attendance and they had found the red call point broken and were unable to repair it  Fire alarm silenced but the officer was unable to reset 
This has been raised for information only  the Land Registry have not cancelled the schedule unlock and locks for the Christmas close down
"Attending Officer advised that the padlock is missing from the gate 
Please see photo  previously reported "
"Attending Officer reported:
Damaged fence behind skip  previously reported - known issue 
Cable left on ground "
The attending officer had reported he had found two males and two females on site  Persons refused to identify themselves  Officer reported a strong smell of cannabis and an ashtray was removed from the garden once they left  They were from unit 219 
Attending Officer reported that the shutter for the main entrance/exit had been left raised 
Basement door is open but I don  t have a key to lock it
"Attending Officer was unable to access padlock to gain entry into site 
Padlock was ice cold and would not turn "
Attending officer advised there is water leaking through top floor  Ground floor main entrance is flooded 
The attending officer has advised the fob held is not working 
Officer will not go in the property without keyholder 
The attending officer has reported the site could not be left unlocked as no one was on site 
The attending officer has reported the alarm had activated when he arrived on site
The operative advised they only unlocked the gates as the staff had not turned up to the site 
Site not to be opened on Christmas day 
The operative advised they only unlocked the gates as the staff had not turned up to the site 
The operative advised they only unlocked the gates as the staff had not turned up to the site 
Site not open on Christmas day 
Fault with alarm system  Multiple activations 
The attending officer has reported the building at the address provided does not correspond to the site which was due to be attended 
Attending officer was given instruction not to enter the premises unless for a visible emergency 
Our officer reported staff were on site working 
Attending Officer confirmed that the door on floor 5 is still sealed off and cannot be accessed 
Attending Officer to conduct an External check of site for car park CCTV activation 
"Attending Officer reported: 
Damaged fencing behind skip  known issue 
BT Van left unlocked with keys inside 
Cable left on ground "
The operative advised staff were on site 
"Attending Officer advised that it is the same issue on the Fire Exit causing these false alarms 
It is a mechanism issue rather than a sensor issue 
Secom was advised last night as well "
Officer who attended did not have keys to enter  so only external carried out  Keys are still held by our service partner 
No fire alarm details are held 
Main Gate is locked and no sounding of Alarm from the building  External Patrols done  All in order 
Our officer reported the contractor did not attend
The operative advised staff were on site as he spoke to the receptionist via the intercom 
Officer advised there is a water leak onsite 
Officer reported the alarm was sounding upon arrival 
Officer reported staff had left the office door open 
The officer has reported ongoing issues with no water to the site  so we are unable to flush toilets and run taps  Also  CCTV is not working 
Invalid codes for staff area 
Officer reported he is unable to check the cctv monitoring as it has been turned off 
Toilets backed up and flooding the area to the left of the main entrance   cleaner required urgently   also unable to flush coke towers as no nozzle left out
Unable to run coke mechines  as they are not switched on 
Attending officer reporting they were unable to secure a fire exit door due to sensor being loose and preventing the door being closed  images attached 
Officer had trouble trying to reset the alarm as the alarm stated the activation came from the spa to which our partner does not hold an access card for
The attending officer reported that there is a water leak coming in under fire exit door on the ground floor 
The attending officer reported that on arrival an engineer was working in the engine room 
The attending officer reported that they do not have any codes or AI s to reset the panel 
The attending officer reported that the coded padlock is missing 
The attending officer reported that the alarm was not set on arrival 
The attending officer reported that the fence is still damaged as previously reported and the gates were open on arrival  Also  there is copper cable left unsecured on the ground 
The manager on site asked the guard to re-attend 24/12/20 
The on-site security did not give our driver permission to take photos of the panel 
The guard advised they could only complete an external patrol as another officer who had the keys was stuck on another site 
The guard advised that the engineer did not turn up to the meet 
The guard stated that staff were on site when they arrived 
Police had secured the site before our guard arrived 
Officer advised when he returned to unlock the site he had found the padlock on the floor  he believes staff may have left the gate open 
Officer advised when he holds the fob to the alarm panel it makes no noise and reckons this may be the beginning of a potential fault 
The attending officer reported that they do not have any assignment instructions for the property so unable to complete full internal patrols 
The attending officer has found damage to the window at the rear - unsure if this a new or old damage 
The attending officer reported that full external patrol has been carried out as per the assignment instructions 
Attending officer reporting they were unable to complete internal patrols of site due to staff present on site 
The attending officer reported there is a water leak in the men s toilet and he is unable to locate where it s coming from 
Attending officer reporting signs of travellers in the area 
The attending officer reported that the main gates were open on arrival 
Attending officer reporting on going issues on site including damage to perimeter fencing  unsecure copper cabling left on site and gates not locked 
The attending officer reported that the gate has been broken and the staff was on-site on arrival 
The attending officer reported that the fire door is an access door  anyone can open it but they cant set the alarm panel  No Ai s held for the alarm  the officer spoke with SECOM who advised him to contact KHC as AI s should have been updated when the survey was done but KHC has no information for the alarm codes  The officer also reported there are still people on site 
The guard stated that staff were on site  This job was raised incorrectly 
The guard stated that the smoke detector on-site is faulty 
This job was cancelled while the guard was on site 
The attending officer advised they were unable to locate the site 
The guard advised that Chris Hughes was not expecting them until 04/01/21 
The attending officer advised that there was no staff on-site due to the Tier-4 COVID restrictions 
Mark Jones was on site who advised we do not set the alarm 
Officer reported that the fob for the access doors was not working on the exit doors so he had to exit the site via the revolving doors 
The attending officer reported that on arrival there was staff on site 
The attending officer reported that the window on the ground floor was left open 
The attending officer reported that the main gate was not closed 
Officer reported the main entrance vehicle gate is broken 
"Attending Officer reported a leak at the Exchange Room window 
Please see photo "
"Attending Officer confirmed that there is still standing water on the ground floor and 1st floor 
Officer aslo reported cable left on ground 
Please see photos "
Officer reported the fencing by the skip is damaged 
The attending officer reported that on arrival there was a sign of travellers on site 
The attending officer advised that on arrival he met staff on site and they advised him that they will lockup on departure  Officer also reports that there is copper cable left unsecured on the ground 
Attending officer reporting signs of travellers in the area 
Attending Officer reported gate damage  please see photos 
officer reported they detected a water leak in the tank room 
officer reported the gates are unable to secure due to a fault 
Attending officer reporting they were unable to secure main shutters due to them being broken  also unable to reset alarm before leaving site 
Officer was unable to lock the gates due to a missing padlock 
Officer reported cable had been left outside the cages in large quantities 
Officer reported they had found an external door open on arrival however no signs of tampering or damage was found to the building 
The attending officer reported that the door  photo attached  was not shut properly 
Officer went to site and got turned away - client on site informed him that they are in dispute with Secom due to Secom not coming out to fix the alarm system - client does not want any more bills for site and refused to show us around 
Officer went to site to conduct the site survey - officer was told that the person who was meant to show him around was not on site as they work in Norwich - he was turned away from site
unable to locate alarm panel  site was un-alarmed  found staff member on site an the don  t know where panel is
Officer has reported that we do not hold codes for access  on the site survey the cinema manager did not provide codes  and the officer was advised these areas should be unlocked  not suitable for lockdown  on 2 previous VPC s they have reported issues with access to the site 
Operative attended site but was no allowed to take photos due to court in session 
Staff present  No further action required 
Officer advised he was unable to gain access through the main door as it appears they have had a new swipe system installed and the fob would not read against it 
Officer reported the outer gates coded padlock is still missing 
Officer reported there is no alarm panel on this site  however there was an alarm sounding at a building called hays recruitment but they do not cover this site 
Officer advised he had to set the alarm panel with faults as he has no master code for a full reset 
Leak coming from the roof of room 8 up stairs  disabled waiting area 
Officer reported the coded padlock is still missing so unable to lock the outer gate 
The attending officer reported that they have an ongoing issue with the site  where the staff is running late up to an hour and a half for the lockup 
Ongoing issue of damaged fencing by the skip 
The attending officer reported that there is an issue with the alarm system and they don t have assignment instructions for the site 
The officer has reported both the contractor and static guard were not on-site on arrival  the site was left unmanned/ unarmed  and lights on 
Officer advised the shutter would not close and the fire panel buzzer was sounding 
The officer has reported that the site is not secure  believed to be from a previous attendance  as windows have been broken 
The officer has reported that no member of staff arrived on-site to collect keys at 11:30  as booked 
The officer reported that no one was on the site upon arrival 
The officer has reported that no staff arrived on site for the scheduled unlock between 06:30 - 07:00 
Attending Officer advised no staff or guard on site 
The officer has reported that no staff arrived on the site for the unlock  as scheduled 
The officer has reported that the door automatic locking system is not working 
Attending Officer was unable to reach the Duty Manager for escort into site 
"Attending Officer advied that homeowners were on site on arrival 
Officer instructed to complete an External check of site "
Attending Officer advised that staff on site were having an Christmas party 
"Attending Officer advised that the site is currently undergoing renovation 
Appears to be no stock on site 
Builders equipment on site "
Padlock is missing from site chain however is still present  the officer closed the gates and wrapped the chain around to appear secured 
Attending Officer left alarm unset as instructed by BT SCC 
"Attending Officer reported:
Lock not attached to chain on green gate 
Damaged fencing behinid skip   Known issue 
Cable left on ground "
Attending Officer reported shelving left outside studio 2 03 
"Attending Officer found a door left open on arrival 
Please see photo "
No keys held for site and signs of an attempted break in  Two metal grates forced from windows  Alarms in two of the buildings still sounding when operative left site 
Attending Officer found staff member Miss Natacha on site on arrival 
Attending Officer found staff on site on arrival 
Staff on site
No one arrived to carry out the maintenance work 
Attending officer reporting they were unable to requested access due to no staff/contractors arriving on site 
Attending officer reporting they were unable to complete full internal patrols of site due to site security present  contractors on site 
Attending officer reporting boarding to site is damaged  image attached 
Attending officer reporting the panel was reading  CCT25  for reason for activation but officer was unable to locate the cause 
Attending officer reporting internals not completed due to external CCTV activation 
Attending officer reporting they were unable to complete lock up due to staff present on site 
Attending officer reporting while patrolling site they found one of the fire doors to be loose/wobbly which may being causing activations due to high winds 
Attending officer reporting while patrolling site they found a door had been left open 
Attending officer reporting while patrolling site they identified a flood in the basement area 
Attending officer reporting ongoing issues including damaged perimeter fencing  gates not secure and unsecure cabling left on site 
Attending officer reporting they were unable to complete internal patrols of site due to staff working throughout the night 
Attending officer reporting several issues found on site including hole in the fence front right from the road side still not repaired  Roller cable still at the rear of building  House pipe fell down from both side of the building 
Attending officer reporting they were unable to complete site survey due to being unable to locate site with the address provided 
Attending officer reporting they were unable to complete internal patrols of site due to being stood down by BSkyB on arrival 
"Attending Officer reported that the Fire Exit door was not secured properly 
Door is currently being secured by a bike chain lock "
"Attending Officer reported staff on site on arrival 
Staff started shift just before midnight "
"Attending Officer advised that the student had already been let into his flat 
Student stated that he had a fob issue and maintenance had been dispatched to repair issue "
Attending Officer advised that a new alarm system is currently being installed by North Alarm Systems 
The attending Officer has reported that the alarm fob is not working 
"Attending Officer confirmed that the door on floor 5 is still sealed off and cannot be accessed 
Please see photo "
The attending Officer has reported that there was a dog unit onsite and the gate was locked and chained 
Attending Officer reported a green door found open during the patrol 
The Officer conducted an external patrol and found all in order 
"Attending Officer confirming previously reported damaged fencing behind skip 
Wire also left on the ground 
Please see photos "
Attending Officer reported staff member Mark Beadle on site on arrrival 
Attending Officer advised that the site had already been locked and armed by the ISS Guard on duty 
Attending Officer advised that staff are staying late on site and will secure the gate on departure 
The operative advised that there was no point of contact at site 
Person on site  Mr Gilbert   was unable to give the information  The person who is responsible for the site was on furlough 
Attending officer reporting they were unable to complete site survey due to Mr Gilbert advising he is unable to provide the relevant information to complete the job  Officer also states the site manager is requesting the spare key to be sent by Secom as they do not hold one currently 
Attending officer reporting while patrolling site they found the perimeter fence to be unsecure  images attached 
Officer reported no show of contractors
Officer called engineer went he got to site   engineer informed he gained entry by staff who were checking fire alarm
Alarm code that we hold for the property doesn t work 
No keys held for site  having been returned Cleaners were on -site on arrival 
Attending Officer reported that the door on the 5th floor was not locked on arrival 
External gates Unlocked 
The attending Officer has reported that the alarm code held does not work 
Officer reported staff on site
The operative was unable to access the CCTV as the computer had a password lock on it 
The officer is unable to lock the gate as the gate has dropped from it position meaning it does not line up
Unable to secure the property as staff are still working on site
Officer unable to secure the building as staff are on site 
Damage to the fire escape doors on the roof  The door is only attached to the frame by one hinge 
The officer is reporting that staff are still working inside unit 22 of court 2 until late
The officer is unable to find which unit activated  patrol of communal areas completed no signs of intrusion
Internal patrol was not completed as requested by BT after the officer confirmed all gates are secure 
Officer reported no issues on site
Officer report vehicle on site unlocked
Officer was unable to secure the gate as its broken  issue raised previously
Officer reported digi code on keypad does not work
Attending Officer advised that the Access Card was not ready for collection 
The officer has reported that there were builders present on the site 
Contractors did not attend site 
Attending officer reporting they were unable to complete site survey  officer advised there is no alarm installed at site and staff were expecting alarm monitoring rather than response 
The officer reported that the alarm code was not working  and was stood down by Mitie 
The officer has reported that the site survey was unsuccessful  due to the site manager not being informed of the survey/ key collection 
Attending officer reporting they were unable to complete internal patrols of site due to staff present  site security present also 
Officer reported  some people onsite have more than one unit which has been setting the alarm off as they are moving in-between units
The guard advised they have no AI s for this site so they could not enter  There are no AI s on our system either 
The guard was unable to access the site due to a large car meet close to the store 
The guard advised they found the door open and on automatic 
Officer was unable to secure the site as staff were still onsite  An iss technical support van was seen in the car park 
Officer was unable to complete the lock up as staff were still working onsite There was an ISS technical support van in the car park 
The guard stated that the electric shutter would not closed 
The guard stated that the postcode we have been provided is incorrect 
The guard advised there was a leak on the second-floor bathroom 
Thr guard stated there is a dog unit on-site who denied them access 
The guard stated the site was already locked when they arrived 
Attending Officer advised that the site was unlocked at 0500 hours 
The guard has reported that there is damage to the perimeter fencing as previously reported 
Officer was unable to secure the gate as its damaged 
The guard advised there is damage to the right side of the building as seen in the photo attached 
The officer has reported that the alarm system is not working/ installed yet as ADT has not taken over the contract  SP advised he has been given a key and access card but will need to re-attend when the alarm system is in place to complete survey 
Officer reported they had to leave the barrier closed due to high tide 
Officer could not locate the room where the zone had activated 
Officer was unable to set the alarm as it was showing engineer mode and the code 5709A is invalid 
Unable to set the alarm due to a tamper on zone 1014 
Unable to lock the site as staff onsite until 0600
Unable to lock the site as staff onsite until 0600
Attending officer reporting they were unable to secure the back gates due to the padlock missing  padlock usually located in the care takers office but officer was unable to find it 
middle gates opening and shutting BT security are aware of this situation and someone is coming out in 4 hours to fix them
Officer reported the mens urinals are overflowing 
Officer reported the self storage shutter would not close 
The officer is unable to secure the brown gates by the main entrance as they are unable to unlock the padlock with keys held 
Officer was unable to secure the gate as its broken 
Officer reported BT were unable to reset the alarm 
The officer is unable to add photos to the mobile report due to an issue with their phone
Ongoing issue of damaged fencing behind the skip 
The officer is unable to add photos to the mobile report 
Officer reported staff were stlll logged as on site but he was unable to locate them 
Officer reported the main gate is damaged 
Officer advised there is no padlock on the gate so they were unable to lock it 
"Attending Officer unable to secure green gate as padlock is missing 
Known issue - previously reported "
The main gate is broken which now has made it that the general public are using the site as a carpark
Attending officer reporting internals not required  also copper cabling left unsecure on site 
Attending officer reporting they were unable to complete internal patrols of site due to not required  officer also reports cabling left unsecure on site 
The officer is reporting that cable drums have been left in the yard outside of the secure cable cages
Site was locked on arrival  Unable to collect fob 
Officer advised no staff/contractors turned up 
sp reported barrier closed due to  high tide
Officer advise the fencing to the property has been damaged
Unable to use chase app on phone due to torrential rain affecting use of screen  unable to use paper map of property due to same issue  External of all accessible areas carried out 
officer advised activation coming from pool area   -
The guard has stated that the perimeter fencing on-site is damaged as seen in the pictures attached 
Attending officer reporting they were unable to secure the main gates due to them being broken  on going issue 
Attending officer reporting  the manager of the store requested only an external patrol of site 
The external panel as seen on the picture has been billed off 
The attending officer reported lots of water on the factory floor  the officer advised that this might be activating the sensors 
The officer has reported that the code held did not unset the alarm upon arrival  so the officer waited for the alarm to stop sounding  Police arrived on site shortly after and carried out an internal patrol  The officer noted that there was a window open in the basement and the police officer secured this window 
The attending officer reported that there is an issue with the alarm 
The officer arrived on site on time  waiting 45 minutes to provide 3rd party access  yet no third party attended- no show
The attending officer called KHC from the site and concluded that this should have been booked as an unlock job instead of third party access as there is a lockup later today  KHC called OCS for a guard update - OCS advised that no guard is scheduled on their system  and to tell contractors to leave and stand down  Officer provided access for Engie contractors to collect their tools at the premises 
The service partner attended to site and called Bt when they were carrying out the External patrol   BT advised them they did not need to enter site as they had been updated that now no doors were open  
Attending officer reporting  barrier to remain locked until 18/12/2020 due to high tide 
There is a water leak at the Men s 1st floor toilet  There does not  appear to be any water running but a pool of water on the floor
Attending officer reporting they were unable to complete internal patrols of site due to CCTV activation  not requested by BT 
The officer has reported that the site is no longer vacant and is occupied with cars present 
The officer has reported that the code held did not work and we were unable to unset the alarm 
Attending officer reporting while patrolling site they found a leak in the basement area  images attached 
The fence damaged  padlock is missing on back gate for several weeks -bt advised on every patrol
Attending officer reporting upon arrival to site no one was present in the building 
External patrol completed  Persons not found but site is secure 
Secom have been informed that their is a bird in the quad building which they could not get out
The alarm in shed one is being armed by staff  There is a bird which can not be got out of this shed so then activates alarm  the service partner was told last week to secure but not arm this shed 
The unlock and lock times have changed post lockdown 2  the monitoring station has not been informed by client  of this change therefore daily  a lock overdue alarm is activated  also  no unlock/lock have been booked by client
The alarm activated 3 times this am  The service partner attended to site and was unable to gain access to the history to establish which sensor had activated  The officer carried out a full patrol no evidence as to where the  activation occurred  Both an engineer and another keyholder attended and were unable to gain engineer admin information but were able to arm alarm 
The contractor was a no show 
The attending officer advised that everything is in order and there is staff on site 
Officer done unlock sucessfully
The service partner spoke to Christine at Secom who advised it was their own staff on site and an external patrol was only necessary
Post lock down times for closing have been changed  The shop staff have reported this change to the officer yet none of the bookings have been changed  the officer is complying to times requested by staff but the bookings need to be updated by client to reflect this  in addition Securitas the monitoring station need to be updated with these times in order for them to cease reporting close overdue/ fail to set alarms  Also  it appears Sunday unlock and locks have not been booked yet completed by service partner
The officer has reported the site was not secured upon departure due to being an open retail park 
The officer has reported that door no  5  the main studio cabin handle is broken and requires reparation 
The attending officer advised that he has no alarm codes for the site 
The attending officer advised that he was unable to set the alarm panel as it was showing system alerts 
Staff present on arrival  Advised they will lock on departure 
Attending officer reporting while patrolling site they found a damaged door handle on a ground floor door  images attached 
The attending officer reported that they were unable to gain access due to COVID restrictions on site 
The attending officer advised that he was unable to set the alarm panel 
The attending officer advised that the door to the main building was open 
The attending officer advised that the codes for the site have been changed and he was unable to gain access 
Keys held are non-operational 
The attending officer reported that the alarm fob held doesn t work  Officer waited for keyholder during an internal patrol with site keyholder they found a fire exit open that had not been locked by staff site secured on departure 
The attending officer reported staff were on site 
The contractor did not turn up to the site 
The contractor did not turn up 
Attending Officer advised that there were no keys available for collection on arrival 
Site contact not present  unable to collect keys 
Attending officer has reported there were staff on site  No issues to report 
Our officer reported staff on site on arrival 
Attending officer reporting they were unable to complete internal patrols of site due to as not required by BT 
Staff were on site 
Contractors on-site so lock was not completed
The officer is reporting a panel of the fencing missing  this issue has been reported previously
Leek on 4th floor staircase 1 
Fon is non-operatinal 
Staff on site Brandon Mohan
the Intruder alarm panel has been removed from the site  That is according to the decorator/contractor  Mr Modestas from MNS Depot  I  ve spoken to  who was in the building when I arrived  He mentioned that the alarm system has been moved to another site
ADT engineer did not attend site
We were refused entry for this key check as branch were unaware of the visit 
ADT Engineer did not turn up to site
No keys handed to the officer  they was advised they will be provided at a later date
Our service partners advised that the key audit has been already completed 
Our service partners advised that all keys have been returned to the site as the site is terminated 
Attending Officer to liase with on site security regarding a missing padlock on the gate 
Attending officer reporting they were unable to complete the flush test in all toilets and staff rooms due to water currently not on 
Attending officer reporting they were unable to complete the flush of the Coke tower due to no power or nozzles 
The officer has reported that the coke machine was leaking and there was water on the floor 
"Attending Officer reported the audible intruder alarm active on arrival 
Advised Mitec of the alarm sounding "
"Attending Officer conducted an External check of site - all secure 
Officer was unable to retrieve keys in a timely mannar due to a vehicle break down "
The attending Officer has reported that the door to the right of Unit 26 was left open 
"Attending Officer to conduct External check of site 
Site is under Covid restriction "
"Attending Officer reported a possible water leak outside Unit 46 
Please see photo"
"Attending Officer noted that the alarm activated upon exiting the site 
Advised BT SCC of the same "
The attending Officer has reported a damage to the fence 
Operative did not set alarm as staff were on site 
"Attending Officer found one door not bolted on arrival 
Please see photo "
5th floor door was not locked
cleaners on site  when doing external on building
The building does not have an alarm panel so unable to fulfil requirement to check alarm
Ground Flood Alarm
"Attending Officer reported that the automatic entrance gates are not working 
Gates currenly open 
Please see photo "
Officer attended site for unlock however no engineer attended 
"Attending Officer reported that this alarm has activated several times 
Officer spoke to Argos delivery driver who confirmed that tinsel has been placed near one of the sensors 
The tinsel if being blown by the air conditioning "
Attending Officer reported that the ISS Guard will be on site tonight for contractor work 
"Attending Officer reported that the ISS Guard would be on site throughout the night 
Contractors working "
Attending Officer to conduct an External check of site for a CCTV activation 
"Attending Officer confirmed that the door on floor 5 is still sealed off 
Please see photo "
Attending Officer reported both gates were left open by staff 
Attending Officer reported that there are no signs of travellers in the area 
"Attending Officer reported:
damaged fencing behind skip
cable left on ground
padlock missing from gate 
All previously reported - known issues "
"Attending Officer confirmed that the front gates are still broken and cannot be secured 
Previously reported - known issue "
Attending Officer advised that  SECOM SAID THAT SOMEONE HAD ENTERED THE BUILDING AND RESET THE ALARM WITHOUT CALLING TO INFORM THEM  NO NEED FOR ME TO ENTER THE BUILDING  
The attending Officer reported that the Fire exit door was left unlocked on the first floor 
Attending Officer was unable to lock site as staff member Sofia Sandullo was still working 
Attending Officer reported that the contractor did not attend the meet 
Officer reported there is a water leak from the water fountain 
Attending Officer reported that the site was locked on arrival 
Front door was not locked alarm needs resetting  has secured the door and the alarm has reset
New member of taff on-site and was unsure how to set alarm 
Officer reported his alarm fob did not work to set/unset the alarm 
officer reported openreach crew  on site
external gates only closed
Attended to a fail to close  The toy shop was open on arrival as all smyths toy shops are open until 22 00 Monday - Friday  Spoke with the Deputy manager Craig Lawton who said he had already received a call from the keyholding company and explained this to them 
Upon arrival the alarm was sounding 
Key card is non-operational 
Attending officer reporting while patrolling site they found a leak on the 1st floor 
officer report fence damage by skip
"Attending Officer noted a blue Fiat parked along side of building down side road  reg no EA53CCU 
Officer spoke with the gentleman inside car who advised that he was waiting to go to work at RAMS across the road 
As driver was parked on a public road  Officer left driver   Officer noted that he drove off as Officer was locking gate "
Attending Officer reported that there are no signs of travellers in area 
Attending Officer reported that there are no signs of travellers in area 
officer reported no issues on site but was unable to take photos as his phone would not allow him
The attending officer advised that they are not instructed or trained to set the alarm panel on site 
officer reported no travellers on site
Basement drainage is blocked 
"Attending Officer to conduct an External check of site 
Site currently manned 24/7 by on site Security "
Officer advised there was a staff member  Dave Jackson  on site who advised he will be there for 2-3 hours so he was unable to secure the site 
The officer is reporting that there is no padlock to secure the entry gates
Attending officer reporting they were unable to complete internal patrols of site due to no access  Officer also reports Copper cabling left unsecure on site  images attached 
officer reported no issues on site but was unable to take photo on phone
The officer was unable to add photos to complete the mobile patrol report
Staff onsite 
Officer reported staff on site who will lock up when finished
Staff were on site upon arrial 
Unable to secure the site as contractors on site
No key held for site 
The officer completed this job on 06/12/20 instead of 07/12/20 
Officer reported they saw a truck and trailer towards the back of the yard and there was no lighting at all to the site 
Officer reported the fob for the alarm did not unset or set the panel 
Officer reported they could smell strong cigarette smoke in the building 
The guard advised the fence is still damaged 
Unable to secure the gate as its broken 
Officer attended site following a CCTV activation and found staff on site and the building open 
The attending officer advised that they have no assignment instructions for the site 
The attending officer reported that the manager has changed the code and is unable to gain access 
The attending officer reported that the contractor did not turn up 
Service Partner arrived on site  contractors were not on site to meet 
officer reported batteries flat in remote
The guard stated that a staff member was on site 
Officer advised the pedestrian gate behind the AA workshop his insecure without a padlock
Officer reported the customer had already left the site by the time he arrived 
officer done internal patrol all good
officer reported door was open
no issues reported
officer report padlock to gate lock  unable to unlock due to padlock frozen
Ongoing issue of damaged fencing by the skip 
Officer advised they have no fobs for the site 
On arrival  the attending officer met with staff who advised him that they will lockup when leaving 
Officer advised upon arrival staff were onsite and had already dealt with the alarm
Job not carried out correctly by SP  Job rebooked  and key collection raised 
The attending officer met with staff on-site Mr  John 
Officer advised the contractor did not turn up 
Officer advised the 11th floor door card is missing however the door was open upon arrival 
The attending officer reported that he does not have the code for the door to the back of the shop
Officer advised the set keys do not work
Officer reported the plant room door was open and light was on upon arrival 
The guard stated that there was a loose power cable hanging from the ceiling 
Guard on site W Sander who advised no alarm activated
The guard stated they had trouble securing the site as the automatic doors would not secure 
officer reported  they could not find location of site
Officer report owners of site on site
Officer reported staff on site
officer reported fault on system
Top stairs window opened need security key to close building
external gates only lock
officer reported 5th floor sealed
SP does not hold keys for this until it goes live on 07/12/20
officer unable to take photos on site due to chase app issues
Ongoing issue of damaged fencing by the skip
The attending officer reported that staff was on site and the site was open as usual so therefore engineer is not required on-site  therefore the engineer has not turned up 
Officer called Tony Anderson who access was for  he advised he is currently on annual leave and CBRE are no longer contracted to this site
Contractor did not show up 
Officer advised the engineer did not turn up 
Manager was not site   to do site survey with officer    staff at branch did not know of visit
The attending officer reported that the contractor didn t turn up and he was unable to get in touch with the client to confirm if the job was canceled 
This site has  battery powered camera s on a tower   owned by Protector  and intruders have damaged the tower and stolen the camera s and the batteries  An engineer was on site yesterday repairing the camera s unsuccessfully  The building is secure  Mitie have been informed
officer found door insecure   please see photo of door 
Job cancelled while the officer was on site 
officer reported ongoing faults on alarm  suggest engineer to take a look
officer met cleaner
Officer reported cleaner on site
Officer was requested by the control TL to complete only external patrol on-site - the alarm was not sounding 
external only done
Officer attended site and when speaking to BT  Nadine  they advised the issue had resolved itself and the officer was not needed to enter site
Officer reported 5th floor door sealed
SP advised that they are no longer looking after this site 
SP has reported that he cant activate the alarm  the alarm asking for a reset  The Key has snapped off into the lock of the shutter 
The attending officer advised that the contractors didn t show up  and they had no phone number for the engineers  Manuk the VUEmanager has been called and doesn t have any info about the job or contractors 
Officer was unable to set the alarm 
Officer report lock was snapped please see below photo
no issues to report on site
Fencing is damaged
officer reported gates are broken completely
The attending officer reported that the engineer didn t need access at 03 12 20 
client hasn  t turned up at time indicated

all fine no issues
No one on site to complete the survey with  no info on alarm   no keys or fobs colletced either  site will be live for external checks only until further notice  unsuccessful survey
The attending officer reported that they struggled to find the site  as there are many industrial sites on Manor Road 
no contractor turned up for unlock
No alarm fob available fos us  we got to get one from secom
The operative has advised they were unaware the job was not meant to be attended in person 
officer complete external only
The attending officer reported that there was no water leak on site 
no issues
Staff on-site on arrival  Spoke to Janet 
Fob is non-operational fr site 
The service partner has advised that a site survey has not been completed on this site 
Officer could not complete the lock up as static guard on site all night
Site was fully locked on arrival 
The attending Officer has reported that there was a fault on the rear door but was secured on departure 
Officer was having issues with the mobile application so was unable to add photos and details to the report
Fire Exit Door was left open
The attending Officer has reported that he was unable to gain access into the room where the alarm is situated as the current Access card held is not activated 
Site was open on arrival 
Staff present on arrival  No further action required 
The attending officer has reported the cash machines were not secured properly on to the wall and this may have triggered the activation 
external gate only
There is a Guard onsite until 06:00 due to contractors 
The attending Officer has reported that there is a Guard onsite until 06:00 due to Contractors 
The officer is reporting damage to the fencing  previously reported
Staff onsite 
The attending Officer has reported that the ADT engineer has not arrived 
Staff onsite 
external gates only
Full check of area believed to be area 1 but limited information on site no issues found
water and electricity is still connected and blinds have been removed from front windows inside of premises the only Graffiti is on either side of the front which has been there  before no further Graffiti added

Officer reported indoor glass panel broken
external only
Raised for information only - Guard on site - Unlock not required
Raised for information only- a security guard was on site with the contractors until 06 00am
Officer found a Bunch of  keys had been left on front counter 

Officer reported they are  unable to secure gate metal bar has been bent and cannot close gates
Officer reported gate broken
Leak on the top floor 
Officer was unable to set the alarm 
Officer is reporting that the fencing panel is still missing
"Attending Officer made the following observation during the check:  AX68 UWD silver transit sized van parked in front of gates on arrival with 1 white Male standing outside of the van maybe having a cigarette may be nothing when I arrived and pulled up he got in the van and left 
BT SCC advised of the same "
Officer reported The main front gate cannot slide back to lock itself  tech problem
all fine  on site  officer reported an error when attaching photos of building to job report
The officer is reporting that there is no padlock on the main gate
Exit gates were left open
SP advised the person who showed him around did not have alarm contract number  contact details or new alarm code  Current fob held does not work as it is outdated now due to alarm system change
Staff was on site
The attending officer has reported there was a package on site that appeared to have been tampered with 
Previously reported - there is water leakage in the basement stairwell 
The Officer has reported that the building has not been surveyed 
officer reported store opened for trading
Deadbolt on back of gate was down so officer could not gain access to site   Person from council jumped the fence to undo deadbolt so we could gain access  This is the only access we have to site and recommend not using the bolt in future
Attending officer reporting they were unable to reset alarm before leaving site due to panel issues  on going issue over the last 2 nights 
Attending officer reporting they were unable to complete internal patrols of site due to CCTV activation  not requested by BT 
Officer reported they struggled opening the door 
Attending officer reporting signs of travellers in the area 
Attending officer reporting ongoing issues including unsecured gate due to no padlock  Copper cabling left on site and the perimeter fencing is damaged 
Officer was unable to secure the gate as is broken
Officer reported a key is needed for the new inner door 
Officer reported the fob does not wrork 
Officer was unabl t locate the fire panel to reset it as there is no information on the asset information on where to find it 
Officer reported the door code for the communal door does not work however the key does 
The guard was unable to enter the site as they do not hold any entry procedures for this site 
The attending officer has reported new tenants have moved in to building 1359 Ashwood house 
As previously reported our service partners still dont have the new codes for the secom alarm panel - sp unable to set the panel 
ongoing issue with fire door maglock
Officer reported the fencing behind the skip is damaged 
Attending officer reporting cleaner failed to attend at agreed time due to a mix up with timings 
Attending officer reporting they were unable to provide the requested access due to engineer no show  engineer was apparently in the vicinity but uncontactable 
The service partner has advised the alarm system has faults  They have also reported a padlock is missing on the gates to the premises 
The officer has reported that staff  Jack  was on-site upon arrival 
Alarm fob not working 
Officer reported they do not hold a key for the padlock on the main gate and their fob did not work on the alarm panel 
The attending officer advised that there was staff on-site - Dr Sue and therefore he could not set the alarm 
Attending officer reporting internals not required
The attending officer reported that the mobile app crashed during his patrol and he was unable to process the job as normal 
Attending officer reporting while patrolling site they found the cable compound had been left unlocked 
Attending officer reporting upon arrival to site he found the main gates had been left wide open 
Signs of travellers on site 
The attending officer reported an issue with our mobile app  he could not attach the picture from the site 
Attending officer reporting ongoing issues including unsecured gate due to no padlock  Copper cabling left on site and the perimeter fencing is damaged 
Officer was unable to secure the site as the gate is broken 
Attending officer reporting they were unable to fully secure site due to one of the external shutters not closing fully due to a fault 
Attending officer reporting issues with the fob for site 
Contractor was a no show 
Staff present on arrival 
The officer who had the keys was stuck on another alarm callout so an officer was sent to carry out an external patrol 
The attending officer reported that there is an issue with the cupboard detector and wasn t correctly set 
The attending officer reported that a survey has not been carried on the buildings 
Officer reported the alarm panel displayed systems alert engineer reset 
Attending officer reporting they were unable to complete internal patrols of site due to store manager Laura and staff present 
The attending officer reported that he wasn t able to find the location of the site  he patrolled the whole area and he could not hear any alarms sounding  Please provide us with any alternative information for the location of the site 
Attending officer reporting the 5th floor door is sealed so unable to reset alarm on that floor 
Attending officer reporting internals not required 
Officer reported he was unable to reset the alarm 
Attending officer reporting they were unable to capture image s while patrolling site due to technical issues 
Attending officer reporting ongoing issues including unsecured gate due to no padlock  Copper cabling left on site and the perimeter fencing is damaged 
The officer has reported that staff was on-site upon arrival  probation staff  who advised they will secure the building upon departure  Staff Name Lyndsey Frith 
The officer has reported that Matt Miller  a staff member  and security offer were on-site upon arrival  Our officer was advised that they had the keys and fob and the lock-up was no longer required 
Staff on-site  lock not required 
The guard was unable to secure the door due to the access card reader been removed and no locks on the doors for a key 
Gate is jammed and cannot open due to ice  Contractor Sean unable to gain access  Concrete bollards are also too close to the gates and are iced  this may cause an injury 
Staff were at site 
SP on site longer than the 30 minutes agreed 
ADT contractor did not attend 
Staff present on arrival 
The guard stated that the alarm was sounding upon arrival 
The guard stated the alarm fob held did not work to silence the alarm 
Toilets and taps not flushing or turning on 
The guard was unable to check the coke machine as you need an access code to use it  The alarm panel is still displaying faults 
Attending officer reporting flush test was completed but they were unable to check CCTV due to screens off  no power or nozzles to run Coke through and historical fault on the alarm resulting in it beeping 
The attending officer reported that the CCTV is not working  Need reset with call manager but fire panel is faulty can t set it
Alarm was not set when officer arrived on site  Also the fence on the 2nd main floor was left open 
The attending Officer has reported that there was a puddle of water infront of the Coke Vending machine 
Fire panel has 30 faults
SP advised that they are no longer looking after this site 
The officer has reported that there is a fault on the Fire panel  - Zone 0099 Main panel Earth Monitor Voltage  The officer has also reported coke machines switched off  One which is switched on won t dispense and requires a login which we do not have 
Drink dispensers require a code that we do not hold 
Attending officer reporting they were unable to secure site when leaving due to contractors from Glenfield Electrical working on site 
The attending Officer has reported that a Camera has been removed from the site and is half way up the stairs on the hill to it 
Secom Engineers on site they will call when they are ready for the lock
The officer is reporting that the fire exit is broken  the door is secure
The alarm does not get set for this site 
Attending officer reporting ongoing issues including unsecure gate due to no padlock  Copper cabling left on site and the perimeter fencing is damaged 
Attending officer reporting no issues raised but was unable to complete full internals of site due to no keys held  attendance was to escort site manager while K9 unit responded 
External only due to faulty alarm
Alarm panel located in the manager s office  however no  code had been provided for access  As a result  when entering the manager s office  the smoke band had been deployed  setting off the fire alarm for the whole shopping centre  Alarm code provided 12345* did not work 
Engineer reset was required for alarm
Site is empty and all power is off  No intruder alarm present and the fire alarm has no power to it  ADT engineer could not complete works 
alarm reader outside not working
The atending Officer reported a water leak due to ongoing building works 
Attending officer reporting they were unable to complete internal patrols of site due to no access  Officer also found door unsecure which has been reported to BT who will dispatch maintenance to resolve 
Staff found to be present while conducting internal Patrol  staff members name is Erika
Attending officer reporting a water leak on site  images taken and attached 
Attending officer reporting no requirement to complete internals of site 
Attending officer reporting the alarm for site does not set 
Attending officer reporting they were unable to secure site due to AA contractors present who secure upon leaving site 
Attending officer reporting several issues including gates not secure  unsecure fencing and Copper cabling left on site 
Contactor already attended and left site  Center security provided access 
Staff on site and alarm engineer working on the alarm triggered the alarm probably forgot to put it on test 
 House keeper and PA Maria on site  they will do the locking up when they leave
The store manager was unaware this attendance was due to take place and therefore did not pass on any keys or codes to the operative  
Westfield shopping centre refused access to ADT engineers
No engineer turned up
Digi-code that was given does not work for the left door  Unable to conduct water flushes 
Keys do not work
Staff and contractors on site
Alarm code doesn t work  Luckily there was staff on site or we wouldn t be able to set/unset the panel
Officer reported leak on site
No access to promenades  External completed
unable to unset alarm using fob as it is incorrect  We hold master code which only unsets alarm after it goes off 
External gate has been locked only 
Staff onsite 
External patrol conducted and found no signs of forced entry  The Officer has reported that the Fire alarm was sounding upon arrival 
Contractor on-site had left the door ajar 
Officer is reporting damage to the site fencing 
Officer was unable to add photos to the job report on the mobile application
The attending Officer has reported that the leak from the roof on the bath tub was half full 
Attending officer reporting on going issue due to a leak through the roof on the top floor 
The sink water tap in female toilets  being used by male staff  needs repair as it won t turn fully off
Only external patrol of buildings on site  Copper cable left unsecured 
Attending officer reporting they were unable to capture images of the patrol due to technical issues with the app 
The attending Officer has reported that the building was occupied by the NHS for COVID and also the current fob was not working 
Test
Contractors had left site so the property no longer needed unlocking 
The service partner has advised that there are no gates on site
No keys  alarm codes etc available on site survey  Limited info given 
The officer attended to site to carry out the site survey  There were no staff aware of the survey and no management on site 
The service partner attended to site and advised the G4S have instructed him not to hand over any keys until; he is instructed to do so by them 
The service partner attended to site and was advised that this company no longer exists  The service partner spoke to Cushman and Wakeman who advised them to raise an issue
No engineer turned up
staff on site on arrival
Site did not have any keys to hand over 
The officer arrived on site  the alarm was unset and there were no staff on site
Leeds Combined court satff on site  I met Mr Sonny Sarr- Security Supervisor he said everything is fine here  it was the false fire alarm
Fob held is not activating the shutters
Unable to complete full internal patrol as back door code is missing from AIs
Fob required for the alarm
Officer advised that site is not being monitored by CCTV company we have on file and they were unable to enter site as signs indicate that PPE must be worn 
The attending Officer has reported that alarm code is not held for the site 
"The Mitie officer attended completed the job report incorrectly 
He was actually on site from 23 23 and off site at23 33pm"
Client called Service Partner directly to report 4 intruders after call from CCTV operator  Client and SP arrived at 2037 and Police and Police dogs arrived at 2038   External patrol was carried out  Police dogs picked up a scent but could not track it  Client reported that security barrier that was supposed to be at the main road was not there  It was later found in a field  Building was secure 
Officer reported the warehouse door was left unsecured 
Officer reported intruder tampered with the batteries in the camera 
Staff - head distiller - on site
Bottom lock is not unlocking
Contractor still on site so unable to lock up
Nobody on site to give access to 
Trader on site serving food  pig roast  - The woozy pig
No guard turned up to the property 
Building occupied by the NHS
Staff onsite 
Officer advised he could hear the fridges making noise 
Attending officer reporting while patrolling site they identified a sensor beeping from within site which they thought may be a fire alarm 
The attending officer reported that he spoke to a gentleman on arrival that was leaving the car park  claiming to be a manager in furlough driving a blue seat reg LT52  He claims the ops manager has not received reports regarding recent activations  Rear warehouse door left unsecured 
Officer reported confirmed break-in  the door has been smashed and police are on site  transferred SP to mercury control 
As previously reported - the padlock missing off the rear gate so unable to secure it 
Staff and Security are on site
"Service partner has attended site  no keys to access therefore only able to carry out an external patrol  Site appears secure 

Service partner has reported that alarm appears to be sounding  resetting and then triggering again "
The guard stated that staff was on site 
The guard stated that the Christmas lights were left on over night  Possible fire hazard 
The key warden stated the guard did not arrive on site 
SP advised no break in - mistake made when filling out app
Officer was unable to lock the site as staff were still onsite 
Officer only locks/unlocks the external gates of the site 
The attending officer reported that the door is sealed 
Our service partner advised tha the attending officer s phone stuck after calling the KHC  however  they confirmed that the site is secured and all is in order 
The attending officer reported that there is still staff on-site working 
Attending officer reporting padlock missing off rear gate so unable to secure 
Officer unable to secure the gate as its broken 
The attending officer reported that the warehouse door is being left open again - it can easily be closed securely but is being left open by staff each day 
The officer has reported that the alarm fob held does not unset the alarm 
The officer has reported that the site was unlocked and staff was on-site upon arrival 
The officer has reported that the site is shut due to a confirmed case of COVID-19 
The officer has reported tha staff James Roche was on site and the alarm was unset upon arrival  The officer also reported that the fob we hold is invalid 
The officer has reported that the first floor was left unalarmed upon arrival to carry out an unlock  KHC did not complete the lock up the night before as not booked with KHC 
ATM machine extremely loose  Possible attempt to remove from wall  Could be removed with enough force applied 
The attending officer reported that he cannot gain access to rear of building no key for rear access yard and code is needed to get access internally 
The attending officer reported that there is an issue with the alarm system 
Attending officer reporting while patrolling site they identified on the 7th floor the fire point had been pushed in and was beeping 
Attending officer reporting internals not required 
The attending officer advised that when he arrived on site he spoke to Mr  Austin and he advised him that there is no need for him to enter the site as Mr  Austin is already on-site and he waved at the officer from the house 
The attending officer reported that the 5th-floor door is sealed 
The attending officer was unable to set the alarm panel 
The attending officer reported that there was an issue with the alarm panel 
Attending officer reporting  upon arrival to site they found the main gates had been left open 
Attending officer reporting while patrolling site they found the pedestrian gate was opening/closing on its own 
Attending officer reporting flush test and cleaners attendance completed but the locksmith was cancelled 
Attending officer reporting they were unable to provide requested access due to cleaners not booked until 840pm instead of 6pm 
The officer has reported that Interserve is currently on-site until15:00 and cannot carry out the required lock up 
Staff on-site  manager spoke to  Sue Dalton
The officer has reported that they returned to secure the premises after unlocking for cleaners this morning  as booked  However  there is staff on site who advised they will be remaining and would secure the premises when finishing  Member of staff spoken with was Tom Wood 
The officer has reported that no one arrived on site for third party access 
Attending officer reporting the FOB is not working  alarm was triggered upon entering site 
No alarm system on site
The guard stated that no engineer arrived to meet them on site 
The attending officer reported that the alarm panel is saying that the access is denied - picture attached 
The officer has reported that there were staff on-site upon arrival and the site was open 
 unable to check CCTV due to having password to access PC  all other checks is ok 
No keys held or site 
Attending officer reporting upon arrival to site they spoke to EE who informed this job was booked against the wrong property 
SP called to advise that he was unable to set the alarm panel 
The guard has advised there is damaged fencing near the skip as seen in the attached pictures 
The attending officer reported that the gate is broken - pictures attached 
SP advised they are unable to reset the panel and the engineer is needed  OCS advised and are aware of the issue  engineers attended yesterday and today but could not fix the panel - needs specialist 
Staff are on site until 21:00 and they will lock when they leave 
The guard stated that contractors are on site stripping the site 
Officer asked for the manager  The staff made a few calls and advised the officer that this is not a site that needs cover  as it has 24hr security 
Jack Hyde advised he only wants external patrols done on site and that we don t need keys or alarm codes as Robinsons can remotely reset alarm 
Staff would not assist officer to carry out site survey 
Officer reported there is high tide 
Officer struggled to find site with address provided on chase 
The officer has reported that we were unable to secure the premises upon departure as staff were on site  contact name Erika 
Main entry lock appears to blocked  could be glue   Unable to access site 
Job was cancelled by Mitec however officer had already made his was towards site at time of cancellation
The officer is reporting that the padlock for the front gate is missing
the padlock is missing for the gate
A panel of fencing is missing
Main gate is broken 
Gate is still broken and will not slide back to its locked position 
Photos of the building are to not be taken as requested by the client
Site open and staff present  Our attendance is not required 
The officer has reported that he was unable to obtain alarm codes as the site manager Holly advised these could not be released to KHC  Holly has contacted Lynn Jones  who advised the contract changes on the 7th of December and they are unable to issues codes or keys until this date 
Fob is non-operational for alarm panel 
Store Manager present on arrival with an engineer working on the aircon 
Officer reported high tide 
For information only - the security on site would not allow access to the officer due to covid restrictions but confirmed the cleaners had set the alarm off in error 
Officer reported staff on site on arrival 
Officer reported main door was not locked and left open 
Bt security called on arrival  they advised as the alarm was now set there was no need to enter site and to just complete an external patrol
The officer is reporting the door to the right of unit 26 was left open
The officer is reporting that no cleaners arrived to be allowed entry
Officer reported he found a staff member onsite by the name of mullings or cullings however he covered his I D badge and also a female was present onsite who was not a bt employee 
The attending officer reported that he could not gain access as they are still waiting for an access card 
The attending officer reported that they hold no keys for this site 
Attending officer reporting upon arrival to site the alarm was sounding 
Attending officer reporting they were unable to complete internal patrols of site due to not required  comms issue with site 
Attending officer reporting while patrolling site they found a cracked window  image attached 
Officer reported alarm does not set 
The officer is reporting a missing panel of fencing this has been reported previously 
The officer is reporting that the building has a leak in the second and third floor  these leaks have been reported previously 
The attending officer reported that the yard gate was left open and unsecured 
Officer advised both entrance gates were insecure and he found a male in a van reg: BK68WWZ inside the yard who advised he was parking 
Car park gates are still waiting on repairs 
The officer has found graffiti on the site 
The operative advised that there is water leaking by electrical source 
The main gate cannot be closed as will not slide back to its locked position 
Engineer had left the entry gate open and could not be closed
Entrance cannot be secured as locks are broken
The officer is unable to secure the main gate as no padlock could be located
The guard stated that there is no padlock on the main gate 
The guard stated that the gates on site were left unlocked when they arrvied 
Upon arrival  the attending Officer has reported that the fire door was open 
Officer unable to ascertain which unit is in alarm office and fire doors checked no signs of intrusion
Staff on site  John Morton 
Gate stays locked due to high tide
No fob
No staff arrived on site today
No staff arrived on site
One of the letters in the sign fell off and has been placed in the foyer 
Officer reported there is a water leak from the ceiling  coming along the wall to the alarm panel and  flooding the area 
The officer is reporting this is the 4th night that warehouse door has not been closed properly leaving site insecure and alarm difficult to set
Nigel Doe  project manager on site  advised that Omni Channel Fulfilment have now taken over this site 
Officer reported alarm panel could not be located 
"The attending Officer who was responding to a “fail to set” has reported that upon arrival the cleaner who was at the entrance door has refused the Officer entry  even with the ID Security badge shown to inform the cleaner that the he was responding for a Keyholding job 
Our Officer felt very disrespected as the cleaner was very rude to him "
A panel of fencing is missing reported previously
Alarm fob/code not held
Possible cause of activation is due to chains for opening the shutters left loose and not tied up
The attending officer has reported no one showed up to site  Officer had to depart due to other scheduled jobs in place 
Barrier to stay locked due to high tide
Fob reader not working
officer reported Zone 43 warehouse fire door 7 left unsecured and away from the atheist 3rd consecutive night
Officer reported  staff still working on site 
SP reported part of the fencing is damaged already reported
Painters on site until 1700
The engineer didn  t turn up
staff activated all ok
The attending officer has reported there was no one on site  Site could not be left unlocked as it would be unsecure 
Attending officer reporting they were unable to unlock site due to no security or staff present 
Issue with phone unable to take photos
Attending officer reporting we have that ADT as contract but its SMS  we require the password when doing resets or discussing and issues to do with alarm/monitoring 
Dr Sue Levi not ready to leave another job booked for return visit on  J13197360
Attending officer reporting no requirement to carry out internals of site 
Attending officer reporting they were initially unable to reset the alarm 
The officer has reported that the Warehouse door has not yet been fixed or closed properly which is making it difficult to set the alarm and may impact us being able to set the alarm in the future 
Attending officer reporting while patrolling site they found a window had been left open on the ground floor  image attached 
Attending officer reporting while patrolling site they identified damaged fencing behind the skip  unsecure Copper cabling left on site  overflowing skip and gates open on arrival 
The officer has reported that there was no unit number provided but the site office is secure 
The officer has reported that the central area officer door knob requires fixing  It is lockable but needs to be screwed tight 
The officer has reported that we do not currently hold assignment instructions for the site   So an external patrol was completed 
Premises locked  no staff on site
The officer has reported that Kurt Geiger no longer holds the lease for this store  Capco will contact KHC to arrange key collection/ new contract  Alarm booked on the client portal by Custodian 
The officer has reported that we contacted Howard Waudby as requested and were advised this job had been cancelled with Secom the previous day and would not be attending the site 
The officer reported that he contacted Vodafone who advised him that there were not any issues and there is an engineer on site 
Officer Could access the site due to covid regulations  he is not cleared by management to enter the building
The officer was unable to secure the premises upon completion of the internal patrols as an ADT engineer was present on site 
Officer reported the top office would not unlock with the swipe card 
Officer has no internal access and unlocks the external gates only 
The officer reported that the site was already locked and alarm upon arrival to carry out lock up 
Attending officer reporting they were unable to complete internal patrols of site due to alarm code not working 
The officer has reported that there are still signs of mice on the property and ongoing issues with the Fire exit door contacts which is not closing properly making it difficult to reset the alarm panel 
Officer has no internal access 
The officer reported that a member of staff was on site and was going to be late 
Officer reported the roof doors are insecure 
Damaged fencing reported behind the skip
Attending officer reporting they were unable to locate site  he travelled up and down Aston Lane  asked locals but was unable to locate this farm 
The officer has reported that we are unable to reset the alarm because at the time of the survey there was no working alarm on-site and were not provided with fob or codes  The officer has also noted this alarm has come through the same time over the last few days and may possibly be user error upon the lock-up of the premises 
The attending officer reported that the fob does not work 
Officer reported that upon arriva to site a fire door that was securedhad been opened  also internal doors that were closed have also been opened  site appears to of been entered 
The lock was canceled by the client during the unlock  the site was already unlocked on arrival and staff were on site 
Officer reported they had to leave the barrier closed due to high tide 
Officer reported the 5th floor door was not locked 
Officer advised the building still has not been surveyed 
Officer reported the coke machines have ben turned off due to COVID-19 
Coke machine needs a password that officer does not hold 
"The concession room sink is blocked and water is coming out of the drain 

The internal door code for the Managers Office is incorrect"
Drinks towers have been turned off so cannot be run to flush 
No code held for managers office 
The officer has reported that the coke machines is showing all drinks empty and cannot completed the running through of the coke machines as requested in the job task 
Attending officer reporting they were unable to complete the drinks system flush due to no nozzles attached  unable to check CCTV or the fire alarm/sprinkler system due to the screens not in operation  The panel was also showing faults with the fault buzzer sounding on arrival 
Drinks dispenser cannot be unlocked with a key as it is now coded and SP does not hold code 
Attending officer reporting they were unable to complete the Coke flush due to no Coke machines available 
The attending officer has reported the water supply was turned off and therefore they could not run taps 
Attending officer reporting they were unable to secure site due to staff working late till roughly 1am 
Attending officer reporting staff present upon arrival 
Attending officer reporting internals not required 
Whilst conducting the lock  the guard was unable to set the alarm due to a sealed door  Everything else in order
Officer reported the key will not turn in the padlock so they were unable to lock the gates 
Ongoing issue of damaged fencing behind the skip 
Officer advised they were unable to carry out an internal patrol as they have not been provided with alarm codes 
The officer has reported a leak in the basement  photos included 
The attending officer reported that he waited on-site until 10:45 as requested  but no one attended 
The service partner arrived on site and no one was there to meet   so the site survey was not carried out
The guard advised that when he got to site  staff was on site 
The attending officer reported that the site is now secure alarm code reset - door is damaged but it is secure  the fire brigade had reset the panel before the service partner arrived so didn t know what set it off  The fire brigade then set off the intruders - confirmed on both fire exits - engineer did attend and reset the intruder alarm  The door that is damaged is the rear fire exit - small of the 2 doors in the rear - groundfloor office near parking space 31 
Officer reported staff had left the 5th floor door open 
Officer advised the building has not been surveyed yet 
Attending officer reporting while patrolling site he found plaster which has fallen from the ceiling potentially being the cause of this and recent activations 
Attending officer reported that there was no issue with the site  The closing signal was received at 11:44 by ADT 
"Attending Officer reported severe damp inside the building 
Officer reported:
The water is off in the building  but the electricity is still on 
Water is coming down a wall and staircase  point of origin is unknown but suspect water is coming from the roof 
Walls are mouldy and the building feels and smells  damp  
Please see photos "
Attending officer reporting they were not required to complete internals die to external CCTV activation 
Attending officer reporting they were unable to initially reset the alarm due o the fob not working 
Officer advised the building has not been surveyed yet 
Whilst conducting the lock  the guard was unable to set the alarm due to a sealed door  Everything else in order
Attending officer reporting while patrolling site the found a window had been left open on the first floor  image attached 
Officer reported there was a van left with the internal lightss on 
Attending officer reporting upon arrival to site they found the gates left unlocked  damaged to perimeter fencing  unsecure Copper cabling and an overflowing skip 
Guard arrived to site to unlock however  no one turned up therefore  site was not unlocked 
Staff on-site  Danny Cropper  They are unaware of the alarm activating 
Officer reported no one was onsite with the codes for the panel so the job will need to be rebooked
SP called to advise that staff on-site was not aware of him going today for the Site Survey and therefore the access was denied 
The attending officer reported that the left-hand window appears to have been boarded up after the window was broken 
Fob does not unset alarm  Officer unable to unset alarm 
No workman arrived on site 
Insecure door found on external patrol 
Officer is reporting that a new padlock for the site is required
Unable to let student in as they was not answering their phone and not located outside their room
"Attending Officer confirmed that the door on the 5th floor is still sealed 
Ongoing issue "
Attending Officer reported a faulty smoke detector  Zone 18  Detector 32  top floor store room  
"Attending Officer reported standing water on the floor - ground floor corridor 
No active leak present 
Officer also noted wire left on the ground 
Please see photos "
Attending officer reporting  while patrolling site they identified a high level window had been left open  officer unable to close as door to room locked  door number FD 2 07 
As previously reported there is a flood in the cellar 
Fencing panel is missing reported previously 
Officer was unable to secure the exit gate as the main lock is broken and no code held for the padlock 
Officer reported there is no padlock on the main gate 
Officer reported door to the flood area was left open 
"Attending Officer to conduct an External check of site as NHS has occupied the building and covid restrictions are in place 
Fob for entry was deprogrammed when NHS became active at site "
site closed
Cleaners already on site - no access was required
Manager  new  on site did not have the managers code to be able to reprogram the fobs
No keys held
SP advised that the store was closed but lights were on inside
Manager  mike  on site - issue with panic alarm  Mike advised he will contact alarm company
site closed
SP was directed to collect keys from an alternative address by Mr Tom Linstead
Attending officer reporting they were unable to complete site survey with staff requesting to book an appointment with facilities team before attending 
No-one turned up to the site despite the operative waiting for 30 minutes 
External patrol conducted and found no issues to report 
Issue with resetting alarm due to power fault 
Officer reported part of fencing is damaged and skip is overflowing with rubbish 
Attending Officer reported a full cleaning crew on site on arrival 
= Spoken to EC  she has booked the job mistakenly for 8th instead for Monday the 9th  EC has checked email and confirmed mistake by her side  = Spoken to EC  she has booked the job mistakenly for 8th instead for Monday the 9th  EC has checked email and confirmed mistake by her side 
Staff member  Charmaine  was on site 
Attending Officer reported that the Third Party did not arrive for access 
No guard or staff turned up 
Door left open
"Attending Officer to conduct an External check of site as warehouse door needs realigned 
Officer stated he may not be able to reset alarm 
Reported on earlier attendance "
Attending Officer to conduct an External check of site for CCTV activation 
"Attending Officer reported that Warehouse Fire Door 7 is in need of a realignment 
Sensors are not aligned properly and staff are leaving the door slightly ajar due to cross bar issues 
Please see photos "
Attending officer reporting they were unable to complete internal patrols of site due to staff present upon arrival  officer spoke with property manager  A Barnas  who advised it was the fire alarm not the intruder alarm which was activated 
The attending officer has advised there were staff on site 
Staff were on site 
The attending officer has reported the fire door was found unlocked 
no guard on site
External only as the fire exit door was left unlocked 
Front door has been kicked   but not broken through  door is still secure   Police responded and have advised that the manager phone 101 in the morning to report this   No entry made into store and door is
BT SCC advised Officer to conduct an External check of site as activation was in the skip area 
"Attending Officer reported that a M A N Commercial officer was on site at the entrance waiting for an Engineer 
Entrance open "
"Attending Officer reported the lights on in the warehouse 
This is the fourth activation tonight  may need an Engineer to check the sensor "
Attending Officer set alarm via key at front door 
Attending Officer reported lights on in the warehouse 
Panel of the perimeter fence missing  issue reported previously  Officer also advising that the skip is now overflowing 
"Attending Officer to conduct an External check of site 
No Assignment Instructions for alarm process "
Service Partner attended to site and staff were on site
Shutter was down and the site was closed
This site survey needs to be rebooked - the client was not on site- unable to carry out
Alarm call attended to  yet there was a security guard on site 
 Client needs an Appointment booking & a Form completed & returned before allowed on site  I am waiting for form which I will complete & return
"The service partner was advised by staff on site that this unlock and lock were not required as staff were on site 
KHC spoke to Secom and KDH and were advised to still attend as the job had not been formally cancelled by the client "
The attending officer has reported the fire brigade have broken in through the fire exit door as the fire alarm was activated that s why the intruder alarm activation was sent checked the fire panel fire panel showing projection room  Officer checked the projection room  No signs of fire
The job was cancelled while the service partner was on site 
Alarm is not in use due to construction works being carried out on site 
Officer reported alarm needs engineer to service alarm
Possible attempted break-in  as door forced or found open  not sure due to lighting   Police on site 
Service required for external gates only 
Staff still on site 
Officer was unable to reset the alarm as no alarm codes held 
Barb wire coming out of place 
Signs of travellers reported by attending officer 
Damaged fencing  previously reported
"Our officer reported a number of issues on site 

Officer reported he was informed by workers on a neighbouring unit that electricians attended site and called locksmiths to open the door  they used force to open the internal shutter  They drilled through the lock and replaced it 

Police were onsite however had left without taking any action  Our officer also advised the fire alarm was in fault and he could not gain access t the store through the internal shutter as there was no power to it  Officer was also unable to set the Intruder alarm 

Mitie engineer was present but unable to assist"
Officer advised he spoke with staff member Marian Cooper who advised they were unaware of the survey so were unable to assist 
Our officer reported he spoke with Karen Hewitt who as unaware of the survey and unable to assist 
The Service Partner attended to carry out the site survey  yet the shop was closed 
Officer reported the survey was unable to go ahead due to covid restrictions  he spoke with Sharon Jenkins 
Officer reported he arrived onsite and the staff had to contact an authorised person who was not onsite due to covid  Our officer spoke with Simon Peters who suggested that we email him the details 
This site was locked/ closed - Unable to carry out site survey
Officer reported they had no access for the survey as the site appeared to be empty 
Officer reported the client has asked to book in a key test and collection for after the ky transfer as they have a new key for the outbuilidng and would like all keys to be tested 
Officer reported they were unable to carry out the survey as there was no available personnel with the required knowledge of what was needed to pursue the survey 
Officer reported there was nobody on site to carry out the site survey 
Unable to complete site survey as an appointment needs to be booked with Joanne 
Officer reported the client was not available for the survey as they were unaware 
Officer advised staff refused him entry to the site as they were unaware of the survey 
Officer advised staff refused him entry to the site as they were unaware of the survey 
Officer went to main entrance and called the numbers but no answer  Keys have not been collected 
external only done - no issues
Officer reported the damage outside of unit6 is now more noticeable 
Main gate lock needs to be repaired as it is faulty 
Attending officer reporting alarm triggered by unit tenants who are present on site 
Site was already locked when officer arrived on site 
Attending officer reported that he found mould and graffiti on site 
Reporter on site covering the US Election 
Attending officer reporting  ongoing issue where they are unable to set alarm on 5th floor due to sealed door 
Attending officer reporting internals of site not required 
Attending officer reporting they were unable to secure the green gates on site due to padlock missing  reported previously 
Can t secure the site as gate is broken 
Attending officer reporting while patrolling site the found the gate inside the compound had been left unlocked 
Signs of travellers reported by attending officer 
Attending officer reporting while patrolling site they identified damage to perimeter fencing  Copper cabling left unsecure  an overflowing skip and the gates unlocked on arrival 
Gate broken 
Staff on site  lock-up not carried out  Must be re-booked for later 
Officer reported the lights were on inside the building 
Attending officer reporting they were unable to complete internal patrols of site due to Covid-19 restrictions currently in place 
Attending officer reporting they were unable to provide requested due t the 3rd party not showing up 
The attending officer advised that the staff was unaware of the attendance and the site survey has to be rearranged 
Attending officer reporting they were unable to complete sit survey due to job being rescheduled for 18/11/2020 
Attending officer reporting they were unable to provide requested access due to engineer not showing 
The attending officer advised that the staff was unaware of the attendance and the site survey has to be rearranged 
Attending officer reporting they were unable to complete survey of site due to client being unaware of the visit 
Client has requested a key test once transferred as he believes Securitas have never attended this site 
Attending officer reporting the client thinks alarm fob no longer works so will require a key test ASAP after transfer 
Attending officer reporting they were unable to complete survey of site due to site contact in self isolation due to COVID-19 
The attending Officer has dropped the keys to Tony Leighton for Sims Metal in Smethwick instead of posting them 
Attending officer reporting they were unable to complete survey of site due to client being unaware of the visit expecting the survey to be carried out on the 22/11/2020 
Attending officer reporting  the site manager was unaware of survey taking place so was not happy for the officer to continue before he was notified 
The attending officer advised that the building was closed due to covid  The site survey has to be rearranged 
Attending officer reporting they were unable to complete site survey due to store manager unaware of the visit and has requested it be rescheduled  for the following week 
Attending officer reporting they were unable to complete survey of site due to manager being unaware of the visit requesting to be rescheduled to a later date due to COVID 
Attending officer reporting they were unable to complete due to site staff being unaware the visit was to take place 
Attending officer reporting they were unable to complete survey due to site closed following COVID-19 lockdown 
Attending officer reporting client advises they were not aware of the survey and does not use external security company advising her neighbor is the keyholder 
Attending officer reporting they were unable to complete survey of site due to no staff management present upon arrival 
The site manager advised the keys were due to be collected on Thursday 
Attending officer reporting site manager insisted they collect the keys due to COVID lockdown approaching 
Attending officer reporting they were unable to complete internal patrols of site due to staff present on arrival who reported a false alarm  staff present - Joan Watkin 
Attending officer reporting internals were not completed due to key handover and unlock approaching 
Staff member already on site - Mr Ryan
Attending officer reporting they were unable to complete full internal patrols of site due to some of the flats being occupied 
Attending officer reporting staff present on arrival 
Attending officer reporting they were unable to locate site  postcode directs officer to a church 
Attending officer reporting no requirement to carry out internals of site 
Inter building   security guard was on site  Officer introduced himself and showed I d  informed him I  m here for intruder alarm he didn t allow the officer to do an internal check  was very rude and he escorted him off site 
Attending officer reporting they were not required to complete internals due to CCTV activation 
Attending officer reporting they were not required to complete internal patrols of site due to CCTV activation 
Attending officer reporting they were unable to complete internal patrols of site due to fob not working on alarm panel 
Attending Officer confirmed that there is still no power to the premises 
Staff found on site 
external patrol only as requested by BT security
Officer reported the building is still yet to be surveyed 
Officer reported the upstairs ladies middle tap was left running 
Officer advised contractors had just arrived onsite and advised the lock up is meant to be for 2200 so asked our guard to reattend 
The guard stated that the gates on site are broken 
Attending officer reporting signs of travellers in the area 
Office reported damaged fencing above the skip 
Officer was unable to secure the gate as its broken 
Officer advised staff wee still onsite upon arrival and asked him to reattend 
Attending officer reporting the gates and doors on site are not fully secure  they are chained but access is possible due to the chains being slack 
Officer reported there was no one onsite to let in 
Reporters FYI only: staff present on arrival no further action required 
Report is FYI only: staff present until 18:30 today 
Attending officer reporting they were unable to collect keys due to site now closed  lease expired 
Site manager requested we return Thursday to collect keys 
Keys not collected as Manager Fred requested to re-schedule the survey/key collection for 05/11/2020 
Officer was unable to unset the alarm as the fob held does not work 
Ryan Maeri advised staff would be visiting the property throughout lockdown and that they will not be hanging over the keys 
Ticket #430519 sent to sp for more info regarding issue
Operative was unable to carry out survey as the manager was in a meeting 
The operative advised there was no response from the property when he got to site 
The operative advised that there was no-one at site to collect keys from 
Engineers was a no show 
Site supervisor Isabel was unaware that a site survey was due to take place and did not allow the operative to proceed 
The operative was unable to carry out survey as the caretaker was on another job  The receptionist also advised that the alarm panel was not fully installed yet 
Gabby on site was unaware of the visit so the operative was unable to proceed with the survey 
The operative advised that the lock on the front door is damaged and insecure 
Attending officer reporting no requirement to complete internals of site 
Attending officer reporting they were unable to complete internal patrols of site due to staff present on arrival 
Attending officer reporting they were unable to complete internal patrols of site due to not required by BT  CCTV activation 
Officer reported he found the window shattered for the first floor kitchen upon his patrol 
Officer could not locate the stopcock 
Alarm cannot be reset  s it s asking for engineer reset code 
Officer reported the building is still yet to be surveyed 
Attending officer reporting they were unable to provide the requested access due to the engineer advising visit no longer required 
Attending officer reporting they were unable to complete internal patrols of site due to BT engineer Phil Savage present and working through the night 
Site already locked due to COVID 19 
Officer reported the alarm was sounding upon arrival 
Staff on site 
The guard advised they could not enter site due to a comms fail 
The guard stated that they could not enter site due to comms fail 
Attending officer reporting while patrolling site they identified damaged fencing behind the skip  unsecure Copper cabling left on site  overflowing skip and gates open on arrival 
Attending officer reporting signs of travellers in the area 
Signs of travellers reported by officer 
Attending Officer reported Engineers on site on arrival 
Gate not closing properly  ref RO 1080500 
Attending officer reporting ongoing with the main gates requiring repair resulting in them being unsecure 
"Attending Officer reported an auto lock issue on the front door 
BT Security are aware and BT Security are aware of front door insecure issue  ref:38071
BT staff on site "
"Attending Officer was unable to secure the front door due to the ongoing auto lock issue 
BT SCC aware of issue "
Officer advised the exit gates have technical problems and cannot slide back
Attending officer reporting they were unable to secure the gates of site due to technical problems preventing the gate from closing 
Entry gate cannot be secured as locking mechanism is broken  When you insert key and turn the lock does not move    The additional prongs that are part of the locking mechanism are stuck in the outward position –
Officer was unable to upload photos of the site 
Site cannot be secured as there is no padlock for the front gate 
Cannot secure site as padlock is missing 
Door does not close properly 
Attending officer reporting they were unable to complete internal patrols of site due to staff present upon arrival 
Attending officer reporting they were unable to secure site as staff were present working late who will lock up and set alarm when leaving 
Miss G Brice was present on-site  site had a leak causing issue with PIR
The attending officer reported that Mr Christopherson the Security officer advised that there was a fire test which activated the alarm 
Sp was awaiting additional information for the alarm panel from ADT in order to complete the site survey 
Our service partner advised that on arrival he met staff on-site - Mr  Midelton 
The attending officer advised that the building is insecure due to the boards ripped off 
"Attending Officer reported staff member Angel Velasqez  kitchen staff  onsite on arrival 
Officer also noted that the entry procedure needs a re-survey as there is no door currently marked staff entry "
Attending Officer phoned Mitie but they were unable to verify this call out 
"Attending Officer found the padlock open on the LHS gates  from the main entrance reception  
Please see photo 
Officer noted that while on site  the alarm for the Sports Centre activated 
We do not hold access/alarm information for the Sports Centre "
The attending officer reported that construction works are taking place on-site  Officer also advised that they hold no keys for the site 
The glass door at the outside of the bt building was not locked on arrival  There is shutter on the inside of glass door which is down  Doesn  t appear to be any intrusion
Unable to gain access to the site as Fob/Code for the Intruder alarm is not held 
Unable to gain access to the site as Fob/Code for the Intruder alarm is not held 
Upon arrival the Officer has found Unit 26 F8 Studio door open but secured before departure 
The attending Officer has advised that there was signs of travellers but not active 
Officer reported part of fence is damaged and rubbish skips are overflowing 
Officer reported the cable gates are damaged as a result of a previous intrusion 
Staff onsite 
The Officer reported that the grey doors were locked from inside 
Officer reported closed chamber door found open 
Officer reported an ongoing issue whereby they are unable to access the 5th floor a the door is sealed off 
External patrol completed   No persons found on site 
No site survey completed for this site 
Unable to set alarm with fob
On-site security advised building has suffered a power outage  No health and safety provisions in the basement such as lights and no fire alarm coverage 
Officer advised that people on site working
On site security informed that day patrols have been cancelled due to power shut down for maintenance  accoeding to them  they have already informed their HQ
Building occupied as previously reported  Fob is also non-operational 
 issue with tags  patrol conducted 
"Attending Officer reported that staff on site are using a bike chain to secure the Fire Exit 
Please see photo 
This causes a health and safety issue "
External only due to no power in the building 
The Officer has reported that the power is back onsite and attempted to reset the alarm  However  the Officer had to wait for an engineer to call with for assistance 
The attending Officer has codncuted with no issues reported 
Officer reported electrical engineers working on site all night 
Officer reported alarm was set by client at 20:10 as confirmed by  UK monitoring on arrival 
The attending Officer has advised that due to bad weather the gate was seen damaged  however no signs of anyone been onsite 
The Officer has advised the padlock would not secure the unlocked gate 
Attending officer reported damaged fencing behind skip  and rubbish overflowing  skip 
The attending Officer has advised he was unable to set the alarm due to no power going to the panel 
Officer reported staff were on site 
SP was advised by staff that engineer was on site when alarm went off
The keys held will not give access
On site security advised patrols not required as maintenance going on
Attending Officer advised that no guard or staff were on site 
Attending Officer advised that there was no guard or staff on site 
Unable to gain entry to manor house as wont open with key
Unable to gain access
Site occupied by NHS and fob not working
"Attending Officer reported that he would not gain entry into the manor house 
Key held is not working 
Officer also reported that  although it is locked and secure there is a large gap in the contact sensor in the fire escape door in main block leading to playground  
Please see photo "
Due to faulty system  SP is unable to unset/reset panel 
The attending Officer has reported that due to no power to the building  the Officer was unable to gain access as the keypad on the main doors had no power 
Officer reported chase had a problem and was unable to process job 
Attending Officer reported no signs of travellers in area 
"Attending Officer reported:
Damaged fencing behind skip 
Rubbish overflowing at skip 
Cable left on ground 
Known issues "
The attending officer has reported staff were still on site 
Officer reported staff were on site 
Officer reported keys were not ready for pickup 
The school was locked up and no-one was at site 
The attending officer has reported the client was unaware of the survey and was on her way out and therefore did not want the survey to go ahead 
The attending officer reported staff were on site  No panel information recorded or internal patrol required 
The operative was unable to gain access as the code held for the door doesn t work 
Manager on site is self isolating- Staff advised SP  Ian Claver 
The school was closed for half term and there was no-one at site 
The attending officer was unable to carry out the survey as an appointment is required 
Attending Officer reported an active power failure in the building on attendance for the unlock 
The attending officer has reported water was found on the floor 
Officer reported note posted on the entrance with information site locked due to Welsh firebreak lockdown 
The attending officer has reported he was unable to unset the panel as the fob held does not work and there are no reset codes held in the assignment instructions 
Officer reported only external of the property is usually unlocked 
Attending officer has reported that there was no information provided for location of alarm activation 
Officer reported issues of a damaged roof  asbestos at the front  cracked windows and the gate and fence are damaged 
The officer has reported that a Mitie engineer did not arrive on the site to provide fob 
The service partner stated that attendance was made to the site following the receipt of keys by post on the 9th of November  The officer attended the site but has been advised by the site manager they have not been notified of the collection  Site manager is aware of the deep cleaning commencing tomorrow but was not aware the service partner was attending to collect the alarm code/ fob  The Key has been tested and working but no fob or code provided 
The attending Officer has reported that Staff were working onsite 
Due to no power onsite  the Officer has reported that the Manager  Kevin  will stay overnight 
Attending Officer to conduct an External check of site and secure site 
The attending Officer has reported the main gate was wide open and a member of Staff was seeing onsite 
Upon arrival  the Officer has reported that the door was unlocked 
The perimeter fence has damage above the skip  previously reported  
"Attending Officer unable to secure main gate as it is still broken 
Known issue "
Attending Officer to conduct an External check of site as Covid restrictions are in place 
Engineer on site testing the panel  did not inform monitoring station prior to alarm being triggered  Security officer on site confirmed all is ok and just a test
The attending officer has reported the site was closed presumably for half term  No one on site and no one answered calls on the number on the notice board 
The attending officer has reported there is dripping water from a ceiling on site 
The attending officer has advised the manager Jeremy Parsons was on site and refused the officer entry as he did not require the attendance 
The attending officer was advised that there were limited staff on site and the client was on a conference call 
 no covid risk assessment done it booked and the person to show around  number 6 and 12 on annual leave
Not booked at no covid risk assessments done  person to show round both number 6 and 12 on annual leave 
The attending officer reported the occupants of the house were not Mr and Mrs Clarke  They did not have access to all the information required and were unaware of the visit also 
This is the same issue as Brook Farm House  The occupants are not Mr and Mrs Clarke and the building is split into two  with another tenant in the flat to the rear  This needs some clarification  The tenants also have not received a letter 
The attending officer was refused access as site were unaware of visit 
site closed - sign on door advising they are only open on weekends 
The attending officer has reported the building was empty on attendance and no one was present on site for survey to be carried out 
The attending officer has reported the site is completely empty and the signs are taken down  No one on site 
The attending officer has reported the site was empty and no one was present to carry out a site survey 
Nobody on site who could help
SP advised that engineer has not  turned up 
The attending officer reported that on arrival the site was closed and therefore he was unable to collect the keys 
Water was turned off on arrival due to previous water damage   driver instructed not to turn the water back on in case of further damage 
The attending officer has reported the water mains were turned off and therefore he was unable to run taps 
SP unable to locate stopcock
Water is turned off 
The room with the stop cock was locked and the key was not found in the location it was meant to be 
No code held for store room where stop cock is located  No stop cock under sink in staff room  All toilets flushed 
Attending officer reporting activation was triggered by contractors who are working on site  images attached 
Attending officer reporting internals not completed as not required 
"Attending Officer was advised to arrive on site at 2000 hours for the key collection 
However; SP will not be available until 2200 hours "
Attending officer reporting while patrolling site they found a door had been left open 
Gates broken - BT security informed
Reported again to BT previously reported damage and unlocked vehicle
Gate broken
Attending officer reporting they were unable to secure the gates on site due to a technical problem resulting in them not closing 
Attending officer reporting they were unable to secure the main gates due to a tech fault resulting in the gates not closing 
Front yard fence has a big hole in it  previously reported to BT ongoing issue
Attending officer reporting they were unable to complete full internal patrols of site due to staff present upon arrival 
The guard could only complete an external patrol due to covid restrictions on site 
Attending officer reporting while patrolling site they found a fire exit door had been left unlocked 
Travellers near the site  photo of the caravans uploaded
Staff unaware of visit
SP was advised by the engineer that the job was supposed to be booked for tomorrow 29/10 
Site did not allow officer access to carry out site survey 
Client unable to do survey today and would like to re-schedule 
External only as flats are already occupied 
All parts of this site are now occupied by a Demolition Company 
Officer advised upon arrival the site security had already dealt with the alarm 
Attending officer reporting while patrolling site they found a door had been left open 
Attending officer reporting no information provided for location of alarm activation 
No issue found on site other then staff been on site until 21:00 so the officer could not get the alarm panel reading 
The perimeter fence has  damage above the skip - this has been reported- it is a section of fence which is at the top of a wall which has been pulled over - inside the site - outside edge public footpath but is 5 5 foot high and on the bt property side it is 7 foot high - the gates are left open
Operative was denied entry as the client was unaware of the visit 
Engineers on site working on a power shortage 
No authorisation letter received   Staff not allowing officer access 
The site cannot reopen due to modifications required with the air conditioning/ Covid health and safety and the officer is unable to complete the site survey 
Staff are on site and the premises are open 
Client did not allow access as had not received booking letter from Secom 
Site advised they are no longer using external security   All security is now dealt with in house  Officer spoke with manager Neil Lucas of Acheson and Acheson 
SP called to advise that Callum Robinson has not arrived on site  SP waited on site for 80 min 
Officer advised the alarm fob does not work and they were unable to set the alarm 
Our service partner advised that the front door lock is damaged 
Officer advised they were only able to patrol the customer area as the scramble lode code did not work for access 
Attending officer reporting while patrolling site they found the pane of a double glazed window had been broken  images attached   Officer also reports the alarm panel is showing an engineer reset is required due to a previous alarm activation on 24/10  Fire alarm is also in fault 
Officer advised he spoke with a man by the name of David who was onsite and advised he did not know where the activation came from 
Attending officer initially reporting issues accessing the alarm panel 
Attending officer reporting while patrolling site they found the door by unit 26 had been left open 
Attending officer reporting while patrolling site they identified maintenance needed on the fire exit door by unit 54  images attached 
Attending officer reporting internals not required 
Attending officer reporting while patrolling site they found the Harris fencing at the back of site had been knocked/pulled over  images attached 
Attending officer reporting signs of travellers in the area 
Attending officer reporting graffiti on the rear of the building  images attached 
"Attending Officer reported that the communal gate has no padlock 
Please see photo "
The attending Officer has reported a faulty padlock 
The attending Officer has reported a faulty padlock 
Attending officer reporting they were unable to secure the gates on site due to them being broken
Officer reported the fencing above the skip is damaged 
Attending officer reporting signs of travellers in the area 
"Attending Officer reported the side door open on arrival 
Please see photo "
Attending officer reporting a leak coming from the first floor gents toilets door number 218 
No Padlock on gate
The attending Officer has reported that there was no padlock on the main gates 
Officer advised he carried out an external patrol of the sit as staff were onsite awaiting an engineer to repair the main gate 
Flood water/ Sewerage Leak  was discovered in the basement- this has been previously reported to BT - The officer did not call BT security as there was staff on site  Staff on site aware of leak
Officer reported the padlock that they don t use was missing from the gate 
Attending officer reporting while patrolling site the found a fire exit door had been left unlocked 
Staff were unaware of the visit and thought it would be next week  Keys were unavailable for pickup 
Half term  the school is closed  therefore the survey could not be carried out 
SECOM engineer carrying out works on site advised that staff are all working from home 
Officer reported that the handle of door number 10 has not been repaired 
Officer could not complete the key check as he was supposed to attend a different site  but was not informed 
Officer reported that the contractor did not show up 
Staff on site  cleaner set the alarm off 
As previously reported -the pipes are still leaking
External patrol only completed as per clients instructions
Attending officer reporting they were unable to set the alarm before leaving site due to new panel which n codes/fobs are held 
Key handed over to dog handler  Only external check is carried out 
Attending officer reporting they were unable secure the main gates of site due to them being broken 
Attending officer reporting they were unable to complete internal patrols of site due to security dog unit on site and access was denied 
Officer reported he found the ground floor window had appeared to of been pried open for an attempted break in 
Officer reported he had found the door to the right of unit 26 had been left open upon arrival 
Officer advised they were unable to set the alarm 
Attending officer reporting signs of travellers in the area 
Ongoing issue of damaged fencing by the skip  Reported numerous times 
Unable to secure the site as site being used by the NHS and staff were onsite 
Our service partner advised that they have not carried out a site survey  therefore they cannot gain access 
The attending officer advised that the door is not opening properly - the staff on site opened it properly 
The officer has reported we only are required to carry out an external patrol 
The attending officer advised that there is no power on site 
Staff on site  site already unlocked 
The attending officer advised that one of the double doors have a maglock issue and is not working  The main door is open manually 
Previously reported - Attending officer reported that one of the double doors on site is not working  the main door is opened manually - maglock issue 
ISS officer not on site 
The attending officer was unable to reset the panel - advised that it needs engineer reset 
on arrival the signage is now moda so this needs looking into to see if the building has been sold
Officer has noticed a water leak in the main lobby area KPMG control called to inform them of the issue
Officer reported door was left open at the bottom of stairs 
Attending Officer advised that the alarm panel does not get set for this site 
Officer reported a leak in the roof 
Officer reported the fencing is still damaged 
contractors on site working until 18:00
Staff room windows open but secure
Open office windows x2 at the back  Second set of gates in carpark  padlock cannot be opened 
ISS Officer advised attending Officer that the unlock is not needed today as staff are not working 
Attending Officer reported no Guard or staff on site today 
Attending Officer advised that ISS Officer and staff are not working today 
As reported previously  the building is in use by the NHS  Our fob is also non-operatinal 
Attending Officer reported that the alarm reactivated upon exit 
Officer reported staff were on site arrival 
fire door by unit 54  push baar needs to be screwed
Upon arrival to site alarm was sounding  witnesses report 2x people on opposing rooftops throwing eggs towards passers-by on the street which connected with someone on the street  Hugo Boss window has had an egg hit it and caused cosmetic mess to window however its perfectly secure and no issues Externally  We cannot access the premises  no further action required
Contractors on site  Unable to secure building 
Staff were on site 
Engineer didn t turn up as business was open as usual 
Staff  Mr Akhtar  was on site 
The attending officer has reported he was requested by site contact Sharon Tyson to vacate the site and reschedule as site were not aware of visit 
Officer was denied access as the client was unaware of this job booking 
Staff were on site 
Officer advised the manager Julie Bentley was onsite and she advised she would lock up 
Operative was refused access as the client was unaware of the visit 
Homeowner did not allow access as they were unaware of this visit 
Staff were already on site 
Engineer told the operative he was required to remain on site with him  The engineer spoke to his manager who advised he could leave and this would be rearranged 
"Officer reported some tiles have fallen due to a leak in the roof  The leak was a slight drip on arrival 
Please see photo "
"Attending Officer reported a water leak in the foyer 
Please see photos "
Officer reported keys were handed over to Momo 
Fence  gate and roof tiles damaged   Asbestos and fly tipping at the front gate  Door panel has been ripped off and glass has been cracked  This has been reported previously 
youths on site  asked to move on  site secured no damage
The officer is rpeorting that the padlock for the main gate is missing
Attending Officer reported that the handle on the Fire Exit door by unit 54 is loose  please see photo 
"Attending Officer unable to set alarm because the door on floor 5 has been sealed 
This door cannot be opened for the alarm to be set 
Previously reported 
Please see photo "
Officer is reporting that the entry gate was left open on their arrival 
Officer is reporting that fire exit door is not closing properly and keeps jamming
Officer reported BT van on site
office secure  no information on unit number  as site is public storage space people on site
Attending Officer to conduct an External check of site as Covid restrictions are in place 
"Attending Officer reported Client Camilla Byrte on site with Fire Alarm contractor on arrival 
Contractor working on Fire Alarm "
The attending officer has reported there were contractors on site  Alarm was not sounding on attendance 
The attending officer has reported the site was not accepting any visitors due to Covid-19  Health and Safety Manager Trevor Strutton on site 
The attending officer has reported there was no one on site to complete the site survey with 
The attending officer reported the survey was not completed as no one at site was aware this was due to take place 
The attending officer was unable to complete site survey as staff were not aware of attendance  There was no one available to escort the officer as the site is a school 
The attending officer was unable to complete the site survey as the site were unaware of his attendance 
The Interserve engineer did not turn up
"Attending Officer unable to unlock green gate 
New padlock has been fitted  please see photo 
Previously reported "
Attending Officer reported unit holders on site on arrival 
Officer reported there is no power to the coke towers so the coke towers could not be flushed as requested 
Officer is reporting that during their patrol they found a door open and this was secured before their departure 
"Attending Officer reported that the alarm was set on arrival 
Officer triggered the alarm on entry 
Main door was unlocked on arrival "
Officer reporting staff onsite working late 
Officer reported no issues on site
"Attending Officer reporting previousl issues:  overflowing skip  damaged fence behind skip  cable left on ground 
Also reported a vehicle left unlocked on site  please see photo "
Officer reported alarm was not set on arrival 
Officer is reporting that the gate was found open on arrival and could not be secured
Sp is reporting that the hole in the fencing has not been repaired
"Officer reported a water leak in the old kitchen area 
Please see photo "
The officer advised this building has been handed back to the NHS and is in use 
Staff asked for this to be re-scheduled as only one set of keys at site
The alarm was activated by contractors on site - JB Concept  Access was restricted as they site/entrance was blocked with workman s vehicles   The site is difficult to access as it is off the main road up a dirt track   Identify of contractors was confirmed
Site unaware of any site survey
Nobody available on site to complete survey
Officer handed to keys to Momo
Attending officer reporting they were unable to complete internal patrols of site due to guests present upon arrival 
The officer contacted the engineer from the site and due to the officer not having a key to access the location of the fire alarm panel and the engineer being unable to remotely reset  it was the recommendation of the engineer to attend when the site is open 
As previously reported there is still no power to the premises and the alarm system is dead 
Attending officer reporting while patrolling site he identified an open unsecure door  image attached 
The officer has reported that the alarm fob held did not work against the alarm panel 
Officer was unable to set the alarm as the alarm fob needs updating and the codes are outdated 
Officer advised a new padlock has been fitted which they are unable to close 
Officer reported the door to the 5th floor has been sealed off so unable to access to set the alarm for the  floor 
The officer has reported that the Open reach civils depot compound was unlocked 
The officer has reported a damaged fence above the skip  this is an ongoing issue and has been reported previously 
The officer has reported that we are unable to secure the site as the gates are broken  This is an ongoing issue and has been previously reported to BT 
Officer not given access to property 
Mr Stephen Batt advised our officer an appointment needs to be booked for the survey to take place 
Officer unable to locate site 
Mr Stephen Batyty advised our officer that an appointment needs to be booked for the survey to take place 
Officer was unable to complete the lock up as when he arrived he was told by staff onsite that the lock up was meant t be for 1900 
staff on site  Mr Mike Day 
Officer advised when they arrived onsite no one was waiting to be given access 
n/a - contractor didn t show up for unlock so not required
Officer reported the internal door codes were not provided to them on the survey 
Officer advised the property was vacant and there was no one onsite to carry out the inspection 
Officer advised the client was reluctant to go ahead with the survey today 
The officer advised that there was no-one on site to accommodate the visit 
Officer reported no engineer showed up to the site 
Officer reported the Facilities manager Christine Cannon was unaware of the survey and was not prepared for it so they could not complete the survey 
Officer reported they were unable to carry out the survey as there was no managers on site  he spoke with Simon Baker who was unable to assist and refused entry 
Officer advised the subscriber was unaware of the survey so they were unable to carry it out 
Officer advised the point of contact for this survey was unaware of the appointment so they were unable to complete thw survey 
The site needs a more structured time to complete the site survey due to tasks on site 
Officer reported the company director Debbie advised Rob not to hand over any information to our partner as they did not know about the survey 
Officer reported they were unable to carry out the survey as there was no managers on site  he was advised to speak with Joanne Doran however she was off ill 
The site was locked and staff did not turn up 
Nobody on site
Attending officer reporting upon arrival the entry door on the 5th floor was already open  lights on and alarm unset 
Attending officer reporting the fob is not working correctly  the panel can be set but the alarm reactivates 
Attending officer reporting cleaner present on site upon arrival who triggered the alarm 
Attending officer reporting they were unable to complete internal patrols of site due to not required by BT due to CCTV activation 
Officer was unable to gain access to the cash office as they do not have a code for the digi lock 
The officer has reported that the door on unit 26 has been left open
Officer reported more cable has been left on the floor 
Attending officer reporting they were unable to complete internal patrols of site due to comms failure  officer also reports copper cabling left unsecure on site 
Attending officer reporting they were unable to complete internal patrols of site due to comms failure  BT advised external only 
Officer advised one bar has been removed from the fence behind the rear of the building 
Officer reported an issue with the front door as it could be closed and then opened without the use of the swipecard 
Attending officer reporting they were unable to complete internal patrols of site due to site in comms failure with only external requested by BT 
Officer reported damaged fencing above the skip 
Attending Officer confirms that there is no active signs of travellers 
Officer is reporting water is flowing out of the water pipe quite fast 
"Attending Officer reported a roof leak on the top floor 
Please see photos 
Also cable left on the ground "
The officer has reported that the front doors were open upon arrival  the officer used the card to try and shut it  tried closing it by hand/ manually but they were stuck 
19/10 - Chased SP by phone  twice  to confirm rear gate was secured and/ or BT informed 
Attending officer reporting external only patrols required 
Officer reported  internal patrol not required by BT 
The officer has advised the main gate is still broken and has been since the new year and still has not been fixed 
Attending officer reporting gate still broken on site 
The officer has reported that whilst carrying out an external patrol  2 teenagers were seen on the site 
Attending officer reporting while patrolling site they found a door unlocked 
Staff advised this site is no longer a SECOM customer 
Staff were unaware of visit 
The officer advised that there was no-one on site 
Manager Amber was unaware of visit 
Manager Jill did not allow access as not aware of Site Survey happening today 
Staff were unaware of visit and refused access 
The officer was unable  to conduct survey as the receptionist advised the people dealing with this will only be in the office tomorrow 
The officer was unable to locate the site 
William Peak  Director  has advised that their contract with Secom has been cancelled 
The officer has reported that the handle on the door for No 10 is damaged and requires repair  please see photos 
The guard stated that they do not hold alarm codes for this site 
The guard stated they do not hold the code the the alarm in the forge office 
Attending officer reporting they were unable to complete internal patrols of site due to no survey carried out as of yet 
Leaking from the top floor coming down via the stairs  due to heavy rainfall - No visible damage
The officer has reported that the building was locked and alarmed upon arrival  No signs of electricians on site 
Attending officer reporting they were not required to secure site due to site pen upon arrival 
The officer has reported Graffiti on the rear of the building during the patrol  photos included 
Ongoing issue where the fencing by the skip is damaged 
Officer reported when he arrived the door they use for access was already open and the alarm panel was dead  he managed to locate the second panel and spoke with ec simon who provided a code of 8801 which was used to turn the alarm off however it did not allow access to the log 
White door opposite site office still unlocked 
Bird inside the warehouse 
Contractor still on site needs more time and will call the officer when he s ready for lock-up 
External patrol only  Travellers nearby 
Mechanic engineer Paul is on site carrying works 
White door still unlocked to building opposite site office 
The guard stated that staff was on site when they arrived 
Site is open  so could not be secured 
Attending officer reporting they were unable to complete unlock of site due to no staff or ISS security present 
Attending officer reporting they were unable to complete unlock of site due to no staff or ISS security present 
Attending officer reporting they were unable to complete internal patrols of site due to NHS staff present and COVID-19 restrictions  Officer also reports FOB does not work if access was permitted 
The officer has reported water leaking from upstairs ladies toilets that require urgent attention 
The officer has reported that they were unable to locate the alarm panel from the assignment instructions held 
Attending officer reporting they were unable to complete lock up due to radio engineer present through the night  Malcom Pugh on site  
Attending officer reporting they were unable to complete internal patrols of site due to not required by BT due to CCTV activation 
Attending officer reporting while patrolling site the found a door next to unit 26 had been left open 
Ongoing issue of damaged fencing by the skip 
The guard stated that there is a new alarm system on site so the fob held 
The guard stated that the white door was still unlocked but the rest of the site was secure 
The guard advised no one showed up to site 
The guard stated that the alarm code changed  it was wrote on a piece of paper above the panel 
The guard stated that the white door was unlocked at the end of the building at the bottom of the yard  There is also a white door open to the building that is opposite the site office  He spoke to security  who will try and get someone down to secure it 
Attending officer reporting they were unable to complete the unlock due to no security officer or staff present 
No officer on site  site not unlocked 
Officer reported there is high tide 
Building in use  Fob non-operational as previously reported 
The officer has reported that they were unable to set the alarm panel   the alarm monks engineer I called he told me what to do and how to r=set and was aware of that alarm code that was showed up and said he had a =all earlier for it  All sorted alarm reset building locked and alarmed 
Attending Officer to conduct an External check for a CCTV activation 
Officer reported electricians were working on site 
Officer reported sensor on the 2nd floor office is loose 
Officer reported activation zone not known as premises has alarms in the units 
Officer reported site has not been surveyed 
Officer reported unable to unlock the single door on right hand side keys do not work  and no access gained 
Officer could not upload photos of the site due to an issue with the application at the time of completion 
Officer reported  part of fencing is still damaged and no padlock on the chain 
The attending Officer has reported that he was unable to reset the alarm due to the fob not working and also no Code is held 
The attending Officer has found the damaged fencing upon arrival  photos taken  which has been reported to BT 
The attending Officer has reported that there was no information displayed on the panel 
The engineer did not turn up 
The engineer did not turn up 
"Our officer has this afternoon conducted the scheduled weekly patrol on the site - as well as the below explanations  our officer has reported asbestos dumped on the grounds 

IMG_2876 / IMG_2878 - the roofing has been put through and exposes the building 
IMG_2879 - the boarding has been pulled off and the internal window smashed 
IMG_2880 - the brick roofing on the top of the building has been damaged 
IMG_2884 - dumped rubbish upon entrance / damaged fencing to the property"
As previously reported  the sensors on top of the second floor entrance door is damaged  The Officer has put a tape in order for the alarm to not trigger and has left the site safe and secure 
The Officer has reported that the fence panel is missing in outer fence line on the right hand side 
The Officer has reported that the door  right of Unit 15 and 26  were found open 
Officer reported site survey has not been carried out 
The attending officer has reported the alarm is under repair and therefore could not be set 
The attending Officer has reported that he was unable to take photos of the site with the Portal APP due to having technical issues 
"Attending Officer reported:
Damaged fencing behind skip
Copper left on ground
Rubbish overflowing at skip"
"Attending Officer reported the main doors found jammed open on arrival 
Please see photo "
The attending Officer has advised the site is in use by the NHS Staff 
No staff present on arrival to assist with resurvey 
Person on site unaware of visit
"Attending Officer was unable to complete a key check 
Officers notes:  spoke to gentlemen that lives in flat A who also owns the building as he was leaving - he said that he spoke to Charles Freeman and key check was supposed to be arranged with client  Client said he did not know of us coming to check keys today and is not happy for us to do it  He wants it to be agreed with some heads up!"
"Attending Officer was unable to complete a key check 
Officers notes:  spoke to gentlemen that lives in flat A who also owns the building as he was leaving - he said that he spoke to Charles Freeman and key check was supposed to be arranged with client  Client said he did not know of us coming to check keys today and is not happy for us to do it  He wants it to be agreed with some heads up!"
"Attending Officer was unable to complete a key check 
Officers notes:  spoke to gentlemen that lives in flat A who also owns the building as he was leaving - he said that he spoke to Charles Freeman and key check was supposed to be arranged with client  Client said he did not know of us coming to check keys today and is not happy for us to do it  He wants it to be agreed with some heads up!"
"Attending Officer was unable to complete a key check 
Officers notes:  spoke to gentlemen that lives in flat A who also owns the building as he was leaving - he said that he spoke to Charles Freeman and key check was supposed to be arranged with client  Client said he did not know of us coming to check keys today and is not happy for us to do it  He wants it to be agreed with some heads up!"
Site has been gutted and closed  Alarm system is non-operatinal 
Staff on-site on arrival  Job not required 
Keys and FOb isn  t ready
Officer reported site was already unlocked with lights on and alarm unset 
Staff on site
Officer reported the  third gate had already been opened by eon on arrival 
Officer is unable to turn off the aircon and is reporting that the heating is on and a large number of flys on site 
"Attending Officer unable to set alarm 
Sensor on 2nd floor still loose 
Previously reported - known issue "
Officer is reporting they found the door opposite unit 26 open door was closed and locked on departure 
Officer si reporting that the contact details of the student given was incorrect 
"FOB / REMOTE CONTROL FOR INTERNAL SHUTTER NOT FUNCTIONING / LOW BATTERY  CANNOT INVESTIGATE REAR OF SHOP  
OUTSIDE FOB READER NOT FUNCTIONING  IRREGULAR BEEPS AND NO LIGHTS  UNCLEAR IF ALARM IS SET OR UNSET"
"Attending Officer reported: gates unlocked on arrival  damaged fencing behind skip and wire left on ground 
All known issues  previoiusly reported "
Attending Officer reported client Dan Hayter on site on arrival 
Officer is reporting a hole in the outside fencing
"Attending Officer reported staff member S  Padgon on site on arrival 
S  Padgon advised that the alarm was accidently triggered "
Attending Officer advised that the third party  Garry Morgan  did not arrive to site 
The attending officer reported no one had turned up to site 
The attending officer has reported there is a new alarm system on site for which the service partner does not hold codes for  Officer advised by TSB to leave site as ISS officer will be attending 
key drop cancelled
The attending officer reported there was high tide and so the gates were to remain locked 
Attending Officer reported that the flats have been occupied 
"Attending Officer reported: 8 windows left open in total
2windows staff utility rooms
4 windows toilet rooms
2 windows office room 6"
Attending Officer advised that property owner was on site on arrival 
Site was un alarmed on arrival and rear door to site open  No damage on site
No power to site and the alarm panel is completely dead
Attending Officer to conduct an External check of site 
The attending officer has reported there is power loss in the building and therefore he was unable to set the alarm 
Officer is reporting that during their patrol they noticed a van parked in the no parking area on site 
Attending Officer reported no active signs of travellers in area 
Officer reported staff from CBRE on site working for Rivus and have been given site keys by site manager Harley
Officer is reporting that the perimeter fencing panel is still missing and need replacing 
Officer is reporting that the entry gate is broken to the site
Officer reported sports hall was open with a large crowd 
A member of staff named Mr Ian was on site 
The officer reported that the engineer did not turn up 
The officer advised that they met a member of staff called Sophie on site and she had already dealt with the alarm 
A member of staff named Mr Tom was inside the site 
External check was required
Attending officer reporting internals not required 
Attending officer reporting they were unable to complete internal patrols of site due to staff present upon arrival  Matthew Steel on site 
Attending officer reporting while patrolling site they identified 4 windows left open in total  1 window to staff utility room and 3 windows to toilet room 
Officer reported an ongoing issue whereby the door sensor on the second floor still does not work preventing them from setting the alarm 
The officer has reported that the door to unit 10 has been left open  this has been previously reported and is an ongoing issue  As advised we are unable to secure the door as we do not hold keys 
Attending officer reporting they were unable to identify which unit was activated 
Officer advised there is a sensor fault which did not allow them to reset the alarm
officer reported they ere unable to unset the alarm using the fob or codes held 
Attending officer reporting while patrolling site they identified unsecure copper cabling left on site 
The officer has reported that the main gates are broken 
Officer is reporting that there is a static officer on-site so the alarm was no set on departure 
The officer has reported a small water flood in the basement 
The officer reported that the site is in comms failure and only an external patrol is required 
The officer has reported a broken fence behind the skip  Please see photos  this has previously been reported 
Attending Officer advised that there are no signs of travellers near site 
Officer reported the front cover to the electrical box is missing 
Officer is reporting that the front cover of the electrical box is missing on site 
Officer reported the front cover of electric box is missing 
Officer advised a generator had been left outsode 
The attending Officer has reported no padlock to the gate 
Officer is reporting that there is water leaking into the basement cable chamber and is pooling next to cables 
The officer completed an external patrol only 
The officer has reported that there is a leaky ceiling that has caused flooding on the 4th floor 
Officer advised despite waitng onsite for 40 minutes no engineers turned up 
Officer reported there were staff onsite upon arrival who had already dealt with the alarm 
The guard stated that staff was on site when they arrived 
The officer has reported that there has been a power cut on-site  and the electric board is currently present  The engineers advised our officer they had spoken with the client who confirmed the guard could leave the site without securing  as they will be on-site all night 
Attending officer reporting internals not required 
Officer can t unset fire alarm as no codes held 
The officer has reported the alarm system is not reading the alarm fob and no codes are held 
The officer reported that the door on Unit 10 has been left wide open  The officer believes there is staff present  however  he could not locate staff in unit 10 and there was no response to his call outs  The officer reported that we do not hold keys and are unable to secure the door 
Signs of travellers reported on site 
The officer has reported damaged fencing behind the skip  photo taken  and copper cable left out 
First floor window found broken 
The guard stated that the site was in use by NHS staff members 
An attempt has been made at one of the rear windows but only metal has been pulled away  no damage underneath 
The service partner has been informed the activation was at the Dobson Building- the service partner has exetnal patrol across all of the campus and has been unable to identify the loading bay  site appears secure  No alarms sounding or obvious issues 
Codes for site needed 
SP advised they can only do an external due to the guard with the keys been 2 hours away and on another job  It is possibly cleaners on-site to have keys 
Both fob and codes for alarm did not work  Unable to unset the alarm 
The officer has reported that the vibration sensors may have the sensitivity set too high  The officer also reported that the keys held for the padlocked gate of The Royal Arcade do not work  however  on-site security provided access  The officer reported we are unable to reset the alarm  the officer called the alarm company but the contract number and password held are incorrect and they were unable to assist us with resetting the alarm 
Officer reported there was a flood in the basement 
Attending officer reporting while patrolling site he found a communal door unlocked 
Signs of travellers reported by attending officer 
Attending officer reporting ongoing issues on site including gates unsecure  copper cabling left on site and damage to fencing behind the skip 
Attending officer reporting the gates were found open upon arrival and they were also unable to be secured when leaving site due to them being broken 
The officer has reported that there are two cars parked on-site  the service partner has taken the registrations down  The officer has reported that they are possibly playing tennis 
Attending officer reporting they were unable to complete full internal patrols of site due to NHS staff present 
Officer called to advised that there was Staff on site 
Staff were on site - Sian Harrington - No Intruder
"The client was called unsuccessfully therefore service partner was dispatched 

The client was call on 020 7733 4409- call failed  07404 565 632 message left & 07507 848 804 call failed"
The unlock was to provide access for a static guard- no third party attended
Window open blowing blinds  Officer resolved the issue 
The service partner has no assignment instructions for this site
Attending officer reporting they were unable to complete unlock of site due to no static guard present 
Attending officer reporting they were unable to complete internal patrols of site due to NHS staff present 
Attending officer reporting they were not required to complete internals due to CCTV activation 
Attending officer reporting upon arrival to site staff were present 
Attending officer reporting external only patrols completed  Officer informed site is mostly barded up and they were not comfortable entering site 
Officer was unable to take pictures of the site due to problems with his mobile phone 
The officer has reported that we do not hold a fob for the alarm panel 
Attending officer reporting they were not required to complete internals due to CCTV activation 
Officer advised a sensor on the upstairs door is loose preventing the alarm panel from being set 
Attending officer reporting while patrolling site they found one of the unit s shutter had been left open potentially due to damaged shutter 
Attending officer reporting no requirement to complete internals of site 
Attending officer reporting staff on site upon arrival 
Officer reported there was nothing displayed on the panel 
Attending officer reporting they were unable to complete full internal patrols of site due to being unable to unset the alarm 
Ongoing issue whereby the door to the 5th floor has been sealed off so unable to access to set the alarm for the 5th floor 
Officer reported there were cleaners onsite upon arrival 
Attending officer reporting while patrolling site the found the gates unsecure  copper cabling left unsecure and damage to the perimeter fencing 
Unable to secure the site as NHS staff onsite 
Security guard present in site on arrival 
Steve Boyd on-site  lock not required 
Officer advised the job possibly was not meant to be booked for today 
Officer reported the alarm code they held did not work
Staff present on arrival  Report is FYI only  Activation on the 4th floor  alarm now unset and site left with staff 
No keys held for site 
Internal buildings has not been surveyed yet 
The attending Officer has reported that the current keys held provides access but the Fob is invalid 
The attending Officer does not have an alarm fob for the panel 
Officer reported fly tipping  on site and windows on roof ripped off 
The attending Officer has reported that alarm would not set 
The service partner was only able to complete an external patrol due to the re-survey of the site not having been completed yet 
Officer reported floor 5 entrance door is sealed so alarm cannot set 
Officer reported air condition was turned off in the comms room and room was very hot 
The guard stated that a dog unit was on site with the main gate padlocked and chained  They was refused access 
The attending Officer has reported that the vehicle on site was unlocked 
Staff on site  Mr  Sam Warren 
No engineer turned up
No engineer turned up
Contractors on site installing 5g mast  advised they will be present for 2 weeks 
Keys stuck in lock
The Officer was unable to check and confirm if all the Internal corridors  fire doors are closed as well as the kitchen been safe as the buildings have not been surveyed yet 
The Officer has reported that alarm code is not held for the building 
Workers on site all night - they have advised not to lock site
Mr Alan amin was contact once kw was on site  the client had decided he had been waiting too long and is staying at a hotel for the night and will return tomorrow to gain access from concierge
Officer attended site and found  security guard on site 
Unable to gain access to office as we do not hold key code or swipe card
Officer reported the entry door was difficult to lock 
Officer reported no survey has been carried out 
Officer reported person seen by the site with gates wide open but escaped when  approached 
Officer reported vehicle on site unlocked 
The Officer has reported that the front fences HRS has a large hole and is easily access-able  
The attending Officer has reported that Covid-19 restrictions are still in place 
Flat is occupied so only an external patrol has been completed 
car park gates only
Officer reported the lift is not working 
Officer reported five windows were left open in the staff utilities room and the toilets 
Officer got called to late close as staff could not reached by Uk Monitoring
Officer reported the alarm panel cannot set as it went into tamper 
The officer is reporting that there looks to have been a vehicle exhaust dumped by the shutter of the building 
The officer is reporting that one of the door contacts for the alarm system is loose and will need to be replaced as may fall off soon not allowing the alarm to be set 
The officer is reporting that there has been flooding in the basement of the site 
The officer is reporting that part of the fencing is missing 
Officer reported gate had not been repaired yet
"Attending Officer was unable to secure main and exit gates due to technical issues 
BT SCC aware of issue "
Officer reported that both gates front are rear have been repaired
Attending Officer conducted External check of site for monitored trouble alarm 
"Attending Officer advised that the alarm for this site has not been set in six months 
TSB aware "
Staff on site  Sam Fish   Alarm panel had already been reset when the officer arrived on site 
SP holds correct access keys but need an alarm fob from Kings Security
Store manager refused to give our officer the keys due to them not being informed by the client of our arrival 
Staff were on site 
Attending Officer reported staff on site on arrival 
Unable to gain access through any of the external gates  Possible fault on access control system  AI  s state that the gates would be open on arrival 
Attending Officer reported that he was unable to turn off the heater at the staff door  which was left on 
The Officer has advised the alarm panel required a remote reset 
The attending Officer has reported that the padlock on the bottom lock is missing 
The attending Officer has reported that the Fire exit door by Unit 54  the push bar screw was missing 
The front door was open upon arrival 
Officer reported dog unit on site gate padlocked and chained access denied
The Officer has reported that Scaffolding outside the building up to the roof 
The officer is reporting that the front gate is broken and there is a 24 hour static guard on site 
"Attending Officer reported: damaged fencing  please see photo ; cable left on ground  please see photo ; the handle on the main door has broken  please see photo  
Advised BT SCC of the issues "
site in total coms fail external only done
The officer has reported that the site communications are in failure 
Damage to fence
Attending officer reporting while patrolling site they identified leak from the disabled toilet on the 4th floor  small amount of water that appears to be coming from the Cistern behind the toilet 
The officer has reported that the main gates were open upon arrival and we were unable to secure them upon departure 
Attending officer reporting sign of travellers in the area 
Attending Officer was unable to gain access with the Swipe Card 
The Officer has reported that the main door frame was loose 
Officer advised no issues to report
The front door was open upon arrival 
Roof door open
"Attending Officer reported that the front door is unsecure again and can be pulled open 
Officer advised that some work was completed on the door and it was secure last night "
Attending officer reporting they were unable to fully secure site due to BT engineer present 
BT security informed control the patrol officer fell on the stairs and may have been injured 
Smashed external intercom phone 
Officer reported staff are still working on site 
Attending officer reporting while patrolling site they found the cable chamber doors had been left open 
Officer reported on patrol small leak on the 3rd Floor
"Attending Officer reported the padlock missing from gate 
Please see photo "
"Attending Officer reported no padlock on gate  please see photo 
Previously reported - known issue "
Internal patrol not required by BT 
Officer reported cable drum was left outside the cable cage 
Attending officer reporting no external lighting on site 
"Attending Officer reported:  The front gate destroyed and white van with 2 males parked up in the access road 
Looks like travelers one is in a orange high vis jacket;  Indian looking guy and the passenger ragged Caucasian male registration was given to a BT security operator over the phone this is the best image I can get inconspicuously "
Officer unable to tell which unit was in alarm  site is secure with no signs of forced entry
Officer is reporting staff on site on their arrival 
Staff on site  Mr Williamson  as well as contractors
Fob not working to set alarm
The officer has reported that the alarm was unset upon arrival and staff are on site 
The officer has reported that there is a security guard on the site 
The officer has reported that staff were on-site upon arrival 
New tenants in property
Attending officer reporting no requirement to carry out internals of site 
The officer advised that the keys and remote work but an alarm fob/ code is needed 
Attempted break-in  door forced and now jammed 
Flood in basement 
Signs of travellers reported on site 
Leak from flat roof 
Ongoing issue of damaged fencing by the skip 
Ongoing issue whereby the gate is broke and unable to secure 
Hole in the fence road side front right still not repaired  Small hole in the front reception glass door 
Major leak reported in the basement 
The officer has reported that the site is in use by NHS Staff 
Attending officer reporting upon arrival to site the glass door of the school entrance unlocked and opened  images attached 
Officer reported the site was already locked and alarmed upon arrival 
The officer has reported that there is a leak on the site and on-site security is present  Security will be on site until Monday 
The officer has reported that there are 400 units on the site and no information has been provided regarding the unit number or location 
The officer has reported that whilst on-site investigating the alarm  during the external patrol he found a perimeter fence that was unsecured 
Service Partner advised that the third party did not attend  No fob could be located as advised
no one on site
No ISS guard scheduled to work on site 
No guard or staff on site 
Site requires External only patrols 
Attending officer reporting upon arrival to site security guard was present in the store who is to remain on site throughout the night 
Attending officer reporting water leak from roof  slight drop running down wall facing onto Cecil street and puddle around landing on door facing Cecil street 
Attending officer reporting small water leak on ground floor main entry 
Window at front of the building left open 
Attending officer reporting  copper cabling left unsecure on site  damage to fencing behind the skip and the gates are missing the padlock 
Officer reported the gate is broken so unable to secure the gate 
Attending officer reporting windows at rear boarded up and building is secured but there is hole in the Fence from the front right which requires repair  issue reported previously 
Officer unable to secure the site as NHS staff working onsite 
The officer has reported the dripping of water from the ceiling  he has reported that it is minor dripping/ water ingress 
Only an external carried out as officer accidentally confused job with an external patrol   all in order 
Public on site viewing the building 
No security on site 
Officer could not close the shutter as staff were on site 
Attending officer reporting they were unable to complete internal patrols of site due to staff present upon arrival  staff triggered the alarm 
No letter box to be sealed 
Officer was unable to reset the alarm  Contacted Alarm Company for a remote reset but they were unable to help due to the password held being incorrect 
Internal Patrol not required for Welfare Check 
external only
Officer reported that the cameras had been moved by hand 
Signs of travellers reported on site 
Ongoing issue of damaged fencing behind the skip 
Officer reported the gate is broken so unable to lock 
Attending officer reporting they were unable to secure site gates due to staff requesting they be left open 
Attending officer reporting they were unable to secure site staff still present  spoke to Kieran Gillingham  site manager confirmed they would lock the site
Main gate was found broken laying on the ground 
Attending officer reporting they were unable to complete internal patrols of site due to NHS staff present 
The officer has reported that we are unable to gain full access as the gates have padlocks on which we do not hold keys/ codes 
Officer reported  staff on site on arrival and alarm panel was unset 
The officer has reported that staff was present on-site upon arrival 
The officer has reported damage to the front of the main building   photo taken  
The officer has reported that staff was on-site upon arrival 
Attending officer reporting they were unable to complete internals of site due to only the gates requiring unlocking 
Officer reported that a Virgin Media engineer was on site waiting for BT staff to arrive in order to run some tests
BT not aware of job booking  so asked officer to carry out External Patrol only 
Roof panels have been pulled off so water can enter as well as unwanted people
Concrete blocks across the gates are too close to the gate  officer has to climb onto them in order to access the padlock 
alarm code not working 
Front Reception Door was found wide open 
Alarm code held only takes officer through the engineer menu  but doesn t give the option to unset the alarm 
Floor 5 has been sealed off and cannot be opened for it to trigger the alarm 
Reception shutter not lowering all the way down and is stuck a foot from the top 
Officer reported they were unable to lock the gate a staff were still working onsite 
Attending officer reporting while patrolling site they found mud had been walked inside the building which has now set on the floor 
Leak detection panel showing general fault 
Attending officer reporting upon arrival to site they found the gates unlocked  copper cabling left unsecured on site  an overflowing skip and damage to the fencing behind the skip 
Officer reported that a Virgin Media engineer was on site waiting for BT staff to arrive in order to run some tests
Hole at rear of fence is fixed with plastic bands  however  the hole in front road side has not been repaired  Windows at rear are boarded up  Cable roller at rear of property needs to be moved inside  Main gate found open 
Issues locating the site as the location changes on a daily basis 
Officer reported the site had already been locked and alarmed by the onsite ISS guard 
alarm code not working
Fire alarm activation  Staff outside on arrival - they were waiting for fire brigade to arrive 
The officer has reported that they were delayed to the site and arrived at 12:45  The officer called the third party who advised they would not be on site until 14:30
The engineer did not turn up  Sodexo called who advised to stand down as they cannot get through to the engineer 
The officer has reported that the engineer did not turn up on site 
The officer has reported that the third party did not arrive on-site and the gate access code does not work for the gates 
The officer has reported that there was River Trust work staff on-site bricking pillar   Finlay   The alarm may go off again due to staff not having a fob  The officer also reported we do not hold keys for access 
No unlock too place as the building was already open
Attending Officer reported damage to the lock that controls the front door sensors 
Officer reported ongoing fault on the alarm and Sodexo is aware  Entering premises will cause more issues on the alarm 
arrived onsite for 05:00 lock up  Security onsite reported they have been told to work until 06:00 and leave when cleaners arrive onsite 
Attending Officer advised that BT SCC has requested an external only for a PIR on the stairs 
"Attending Officer reported the door towards the bottom of the gym blocked 
Please see photos "
"Attending Officer to conduct an External check of site while dog unit is stationed at site 
Gate chained and padlocked "
"Attending Officer completed External check of site 
Gates unlocked Security and Engineer currently on site "
Officer reported part of  fence is damaged 
Officer reported a hole in the front fence 
"Attending Officer was unable to secure the front and rear gates 
No locks on gates 
Please see photos "
"Attending Officer to conduct an External check of site 
Covid restrictions currently in place "
Whilst on site demolition team arrived  state cladding going up and site / rear carparks will soon be inaccessible as heavy renovation / demolition takes place  
"Attending Officer advised that the inner entry door mechanism is not working 
Previously reported "
"Attending Officer reported:
10 windows left open
1 window administration office
2 windows utility staff rooms
4 windows toilet rooms
3 windows office 4 room"
Attending Officer noted the main gate in repair during the External check 
Attending Officer reported a power outage on arrival due to works 
Found window open
"Attending Officer was unable to reset alarm panel 
Outdated alarm panel information held "
"Attending Officer to conduct an External check of site 
Dog unit on site  gate chained and padlocked "
Attending Officer was unable to access the lift lobby due to contractors laying new flooring 
"Attending Officer reported:
Fence damage behind skip 
Overflowing rubbish at skip 
Cable left on ground 
Please see photos "
The officer has reported that the gate is broken 
The front gate which has been open because of technical problem has been manually locked by the site manager Mr  Paul Brown 
external check completed
The attending Officer has reported that the Automatic main gate is not closing 
An ongoing fault with alarm  External patrol completed 
external check complete
"No power to the alarm panel  

Window left open "
Staff present on arrival 
Nobody on site to give access to for the unlock
Officer reported external gates are only unlocked 
Officer reported no keys held 
The attending Officer has reported that Staff arrived onsite 
Officer reported cleaners on site
office performed full external patrol all fine
The attending Officer has reported that the alarm Fob was not woking 
Officer reported staff on site
Attending Officer reported that the glue on the sensor for the 2nd floor entrance door has worn out 
external gates only locked
Gate locked as per instructions
Communication failure with alarm however requires engineer reset 
Officer reported padlock is still missing  photo taken
"Attending Officer reported the main gates unsecured on arrival 
Please see photo "
main site gate unsecured  lot  s expensive equipment in  the yard
"Attending Officer reported damage to one of the shutters on site 
Please see photo 
Previously reported "
The Officer has reported that the gate was left open by Staff
Current access card is invalid and the front gate seized will not close 
Roof flood/leak on site 
Full coms fail
"Attending Officer reported the first floor fire exit found open on arrival 
Officer also reported the break glass had been broken 
Please see photos "
Attending officer reporting green Ford Focus parked in front of main door  image attached 
"Attending Officer reported overflowing rubbish next to skip 
Cable left on ground 
Damaged fencing behind skip  previously reported  "
Large amount of surface water found in cable chamber on basement level 
The Officer has reported that there was water on the surface floor on the cable chamber 
Officer reported staff left gate opened
Cannot secure site as padlock is missing 
The Officer has reported that there were cables left outside of the Cable Cages 
"Attending Officer reported cable left on the ground 
Please see photo 
Officer also reported staff on site on arrival "
The Officer has reported that the building was occupied by the NHS Staff and the current held is also invalid 
"Attending Officer reported the door handle to the basement door broken 
Please see photo "
The Officer has reported that both gates were open upon arrival 
Static security on site
The attending Officer has reported that the Staff in the store have restored the panel 
Staff onsite 
The Officer has spoken to Sati upon arrival and then was advised to leave the site 
The Officer has spoken to Sati upon arrival and then was advised to leave the site 
Issue with communication failure with alarm panel for over a week
Contractor did not arrive
Officer reported only external gates are checked 
Officer advised gate is the process of being repaired
The attending Officer has reported that the current code held was invalid 
AIs not held - external conducted only
Michelle Izzo advised not set alarm
external only   as it was coms failure
Officer reported staff  arrived on site when he was leaving 
The attending Officer has reported that an employee has left their keys on the main gates 
"Attending Officer reported damaged fencing behind the skip  previously reported - known issue  
Officer also reported cable left on the ground 
Please see photos "
Attending Officer unable to secure front gate as it is still broken 
"Attending Officer was unable to gain entry onto site 
Entrance gates not working "
"I did not find any  broken  gates they all looked intact however one of the carpark gates has been left open  and was also open when I attended yesterday  
But again did not find anything broken "
officer reported gates are still broken
The attending officer has reported signs of vandalism on site as seen in images  Broken beer bottles  chairs and pizza boxes found to the rear of the site 
New alarm panel has been fitted
No keys or AIs held
The attending officer has reported the cause for the alarm activation was a door left open to the right of unit 26 
no guard or staff on site
Officer reported the alrm code held does not work so unable to carry out an internal patrol 
The attending officer reported that the main gates are being repaired 
Ongoing issue reported of damaged fencing by the skip 
As previously reported the main gate is broken 
The attending officer reported that the gates are not working 
Officer advised there was a guard with a dog on site carrying out a patrol 
Officer advised they found a leak in the ceiling on site  officer spoke with KBR who arranged for a plumber to attend site and fix the issue 
Unable to carry out an internal patrol due to nhs staff being onsite 
The officer has completed and external only  service van was seen on-site  no issues found on the site 
The attending officer has reported there were windows left open on site  Staff utilities room windows and toilet windows 
The officer arrived on site to secure the premises as booked but was advised works have not been completed 
Officer reported the gate was left open 
The officer was advised by BT Security not to enter the building 
staff on site - Kings Lee
The officer has reported that there is no ISS guard or staff on site today 
The officer has reported that there is no ISS guard or staff on site today 
The officer has reported that there is no ISS guard or staff on site today 
Our service partner advised that the 2nd-floor entrance doors are not working therefore alarm won t set 
Our service partner reported that the door was left open 
On arrival  our officer found a rough sleeper in front of Waterstones 
Our service partner is allowed to enter the site only with the site manager  therefore they were unable to gain access 
Our service partner was unable to gain access due to EE member not arriving on-site for escort 
The attending reported signs of travellers 
Officer reported there is a security guard onsite 
Officer reported there is no padlock on the chain 
The guard stated that the gate on site was broken 
The guard stated they was unable to complete an internal patrol as the main gains are still not repaired 
The guard stated that the site was locked with a Static guard on site who would not give them access 
Our service partner reported that on arrival there was NHS staff on site 
Gate not locked or closed 
The officer has reported that there was Henderson Insurance staff on site  Andrea Clarke advised she would secure the premises 
The officer has reported that staff was on-site upon arrival 
The officer has reported that they are unable to secure the premises as staff are on site 
Disc fob for office not programmed  No post for London Ops 
Staff at 47 Lower Belgrave Street said they had no keys to hand over and that all the keys for 28 Old Queen Street were given to the clients 
Officer advised the alarm went off when using the fob 
Door to the surgery was locked with staff on site who didn t allow access as the surgery is Appointments Only 
site not alarmed and rear door unit 1 found open
Officer reported the inner entry door mechanism is not working 
Only able to unlock the gates 
SP did not attend due to an accident on M25  He was stuck in traffic 
The service partner advised that phones were hanging from the ceiling and the heating from the cone was blowing them all over the place 
Our service partner was unable to gain access due to not being able to park near-site as all car parks were blocked off 
Attending officer reporting the reason for activation appears to be due to a power cut in the area  local traffic lights were while on route to site 
Wood and tiling appear to have been removed from the roof 
Attending officer reporting site already secured and alarmed upon arrival 
Attending officer reporting no requirement to complete internals on site 
The guard stated that staff was still on site 
Attending officer reporting they were unable to Alpha way shutter due to fault 
Attending officer reporting several issue while patrolling site including gates unlocked upon arrival  damaged fencing  unsecure cabling on site and an overflowing skip  Issues previously reported 
The guard stated that the gate on site is broken 
The guard stated that the internal electric doors were not locking 
Attending officer reporting issues with alarm panel on 2nd floor following entering the floor to carry out patrols  no codes held for 2nd floor panel 
The guard stated they could only do an external patrol due to Covid-19 restrictions in place 
The guard stated that staff was on site when they arrived 
The guard stated that staff was on site when they arrived 
No contractors arrived 
Service partner called EE who advised not to go inside 
School was open  teachers and cleaners were on site upon arrival 
Officer advised the panel was not set upon arrival and also the fob was not working for the gate 
Officer advised there was site security onsite 
Attending officer reporting while patrolling site they found rough sleepers outside the entrance to Waterstones 
Attending officer reporting due to contractor work taking place outside the premises the power to site has been turned off until 9am 
Attending officer reporting upon arrival to site and after speaking to BT it was established the job was booked for the wrong site 
Officer reported that on arrival staff were still on site 
As previously noted the entry points at site are unhygienic - possibly blood on doors 
Our service partner advised that the rear staff door was left open 
Our service partner advised that on arrival there was staff on site 
Officer reported there was a static guard onsite 
Attending officer reporting upon arrival to site the gates were unlocked  damage to the fencing behind the skip  copper cabling left unsecure and overflowing rubbish in the skip 
Our service partner advised that the main front gate has a technical problem 
Officer reported the front gate was broken 
Alarm activated by staff on site 
SP arrived on-site and he spoke to BT Security  they established that it was the staff who activated it and the alarm was reset by BT  BT advised no need to enter 
Our service partner was unable to set the alarm - panel says call installer 
The officer has reported that staff on site had already reset the alarm upon arrival as it was set off by staff 
The officer has reported that there were staff on-site upon arrival and the alarm had been reset 
Contractor not turned up  Staff present on site 
The officer has reported that they were unable to locate contact on-site 
The officer has reported that upon arrival staff was on-site with electricians   The officer spoke with Mr  Chris who confirmed the alarm would be off for 5 weeks 
No staff or contractor present to unlock for  Job was originally for 08:00 
The officer has reported that the caretaker was on site upon arrival  The officer also reported we do not hold current survey information and have recommended a resurvey 
The alarm was unset and the building unlocked as requested by the control room 
The officer has reported that the fob held did not unset the alarm panel 
The officer responded to a communications failure but has reported that the site is empty  no panels on-site and there are signs of contractors present 
"Attending Officer to conduct External check of site for comms fail 
No alarm codes held "
Officer advised there is no power to site
Officer reported alarm activated because of  loose contact sensor G62 
Officer reported Delta Way shutter not closing
"Attending Officer advised that the entrance gate has been chained due to a canine unit on site 
Please see photo "
Attending Officer reported the shutter at Alpha Way open 
"Attending Officer reported flytipping outside of Unit 22 
Please see photo "
Attending Officer reported staff on site on arrival 
Officer is reporting that there is damage to the perimeter fencing 
The engineer did not turn up to carry out the works 
The officer was refused access due to staff being unaware of visit 
The officer advised staff were on site and he couldn t take an image of panel due to covid restrictions 
"Attending Officer reported the alarm not set on arrival 
Also 12 windows had been left open "
"Attending Officer reported that the Fire Panel was automatically resetting after 5-6 seconds of alarm sounding 
No smoke or fire present "
Officer reported lockup cannot be completed as cleaner has left her bag on site and cleaning items left in the doorway and cleaners office door is open and the cleaner cannot be found on site 
Static guard on site
Officer reported two  windows on the the left hand side and rear side of building  on the 2nd floor have been smashed with holes in them 
Attending Officer advised that staff member Paul Linklater 414515P was on site on arrival 
Attending Officer to conduct External check of site as swipe card is not allowing access for Internal 
Attending officer reporting they were unable to complete internal patrols of site due to comms failure activation 
Attending officer reporting they were unable to complete internal patrols of site due to no requirement due to comms failure 
Attending officer reporting no issues found but wished to point out scaffolding to the exterior of building which is fenced off but may potential cause a security breach 
Officer is reporting that the sites roller shutter is broken so therefore cannot be secured 
Attending Officer reported that the roller shutter to the left hand side of the site is innoperable 
Officer unable to secure front gates due to a fault 
Our service partner advised that the site is in coms fail so he could not do internal patrol 
Officer done a full external patrol
Door to the P U P area is not locked/is broken and therefore is easily accessible 
Officer is reporting damage to the perimeter fencing 
As previously noted - site is in communication fail 
"Attending Officer reported a leak in the basement chamber 
Please see photo "
The attending officer reported that he found vehicle and main gates found wide open on arrival 
Officer reported the roof door was open and the top panel had been removed 
Service partner reported that the gate is locked in locked position keys not working 
Our service partner was unable to gain access due to the door panel not working 
Attending officer reporting front gate padlock missing so unable to secure gates 
Officer reported  body fluids on the floor at the front door and outside on the floor and on keypad 
Attending Officer reported that the main gates were stuck open 
On arrival  our service partner found the main gate wide open and the copper cable left unsafe 
Attending officer reporting while patrolling site they identified cabling left unsecure outside of the cable bay 
client did not turn up for unlock
No contactor at site
no keys/assignment instructions for site
site refused access as not booked in with them
No engineer on site
No AIs and no alarm code
Staff on site
Fire alarm goes off often on weekday mornings - nothing shown on panel - potential fault 
"Attending Officer reported staff on site on arrival 
Attendance cancelled on arrival "
Officer reported the drop bolt on the entry door at the visitors  centre does not connect 
 zone 19 reoccurring activation  mice found in fishing bait area near to this zone  zone also has sacks of hay and straw directly underneath most likely area for mice to be living  pictures in main report
The attending officer has reported structural issues with the flooring in the downstairs toilet 
Building shutter is not closing during lock up patrol
Staff on site
Officer reported part of the fencing is damaged 
Officer reported site in use with NHS
SP advised that unlock had not been booked with them so there was no need to lock 
The attending officer has reported a staff member on site - Ella Amos - had set off the alarm 
The officer advised that there were staff on site 
The officer was unable to carry an internal patrol as the security would not let him park his car on the premises unless it was booked in 
The officer advised that there are instructions held in regards to the fire panel 
The officer reported that the alarm fob doesn t work and Bob only arrived as the operative was about to leave 
No staff to unlock for
Officer attended for Unlock no ISS guard on site to handover to  site locked and left secured
Officer reported gates were open and the exit pool was in use 
code did not work
no alarm codes held
No access through wooden entry door  fob reader showed green light  but doors would not release  None of the keys held appeared to unlock the door either 
Our service partner attended to unlock  however  there was no staff or guard on site 
Unable to set alarm as no access to building 
Attending officer reporting they were unable to complete internal patrols of site due to staff present upon arrival 
Officer reported external patrol only carried out and back door secured and water damage noticed on the ceiling at the entry door and alarm cannot reset as no code held 
"The Keyholding Company received alarm activation from Custodian regarding unconfirmed intruder alarm    ec s were phoned and voice mails left on the following  contact nos
Pierre Siri  07401 255 800
Erica Siri   07401 166 900"
Attending officer reporting no requirement to carry out internal patrols of site  just secure main gates 
Officer reported damaged cars at the back of BizSpace -  3 cars smashing into each other one BMW and one Mercedes  VRN that show damage: HF64PHY  YK17SZP  BG17UAA 
Our service partner advised that there is a guard onsite overnight  therefore he is unable to secure the site 
The service partner advised that the alarm code is wrong 
Attending officer reporting while patrolling site he found a broken window in the ladies toilets  unit 1   image attached 
Attending officer reporting sign of travellers in the area 
Attending officer reporting gates unlocked upon arrival  copper cabling left unsecure  overflowing skip and damage to fencing behind skip 
Our service partner advised that the gate was locked and he couldn t get access 
Attending officer reporting windows at rear are now boarded up  The hole from the front side in the fence  road side  creating easy access to site and in need of repair  issue reported previously 
When our service partner arrived there was NHS staff on site 
Incident was raised for information only- workers were on site
Keith  the BT engineer whom required access  called the Partners to say that he has his own set of keys and he would be letting himself access to site – HE also CONFIRMED that he informed Marius from Sky of this yesterday  17th Sept   The Keyholding Company were not informed of the service not being required 
The service partner attended to site to provide a third party access  The third party did not show up  NO SHOW
The service partner raised issue for information only that the site was unarmed upon arrival
Officer advised the alarm was not set upon arrival 
Officer only has keys to unlock the external gates and not the building 
Attending officer reporting they were unable to complete internal patrols of site due to staff present upon arrival  staff member Leonard 
Officer advised they could not unset the alarm with the code held 
Roof falling in  Fence still damaged at front and gate  Fly tipping seen and site is over grown  making it hard to walk around property 
Attending officer reporting they were unable to unlock as requested due to no one turning up 
Officer advised they completed an external check only 
Attending officer reporting internals not required  external gates only to be secured 
Attending officer reporting while patrolling site they found the upstairs ladies balcony toilet tap left running 
Attending officer reporting they were unable to lock site as cleaners present who advised they will lock up when leaving 
Our service partner was unable to secure the site  as an overnight guard is working 
Attending officer reporting they were unable to complete internal patrols of site due to staff present upon arrival  staff advised they will leave site around 11pm 
Service partner advised that this is an ongoing issue - the Final set button still not working  therefore he could not set the alarm 
Attending officer reporting sign of travellers in the area 
officer reported  there is a security guard onsite 
Attending officer reporting gates unlocked upon arrival  damage to fencing behind the skip  overflowing skip and Copper cabling left unsecure on site 
Attending officer reporting windows at rear still not repaired  The hole from the front side in the fence  road side  creating easy access to site and in need of repair 
The guard stated that the attendance was cancelled as they arrived on site 
Full external patrol completed as we was stood down just as the guard arrived 
The guard stated that when they arrived on site Ms Sharon was on site 
Officer waited on site for 30 mins   No contractor showed up 
Officer only has keys to unlock the gates 
"Mag locks on 1st  2nd and 3rd floors aren  t working in the sense that the panels at the side of the doors constantly flash green and doors will not lock  Doors at each stairwells are the same 

Ground floor and front door are fine "
Our service partner was unable to reset the alarm by himself 
The officer has reported we only are required to carry out an external patrol 
Attending officer reporting they were unable to complete internal patrols of site as not required due to CCTV activation 
Keys not allowing access via the bottom lock
Our service partner was unable to set the alarm on entering  advised that it needs a manager reset 
Our service partner advised that in the disabled toilet unit the tap on the sink is snapped off 
Attending officer reporting door next to unit 26 left open again for second time this week  Security checked inside and secured 
Guard reported staff working onsite until 0630 by the name of hussain so was unable to complete the lock up 
Our service partner advised that the main gate was locked 
On arrival  there was an engineer working on the panel 
Attending officer reporting signs of travellers in the area 
Officer advised there is a static guard onsite 
Attending officer reporting gate found open upon arrival  skip overflowing with rubbish  Copper cabling left unsecure and also damaged fencing behind the skip 
Our service partner advised that on his arrival the main gate was left open 
Service partner was unable to set the alarm for the reception
The guard stated that staff was on site 
Staff on site 
The guard stated that no one met them while on site 
Attending officer reporting the alarm was not set upon arrival to site 
Attending officer reporting no requirement to unlock or carry patrols of building due to no keys held 
Attending officer reporting they were unable to complete internal patrols of site due to BT staff present upon arrival 
Attending officer reporting internal patrols were not required due to client present upon arrival 
Officer reported  there is no power to the premises 
Officer advised there was no power in the office  he checked all fuse boxes and they were all switched on and spoke with the onsite security who advised there is an electrical issue that UK network are investigating 
The main door was left unlocked and there was not staff on site 
On arrival  our service partner saw that the Window left open at room 3 he did not have any access/key for this room to go in and secure it
Officer advised there was no power to the alarm panel 
Officer was unable to secure the main gate as it wont lock 
Attending officer reporting signs of travellers in the area 
Guard on site upon arrival 
Attending officer reporting upon arrival to site they found the gates unlocked  copper cabling left unsecure on site  damage to fencing and an over flowing skip 
Our service partner advised that the gates were left open 
The guard stated that staff were on site when they arrived 
The guard stated that the staff was on site and was having trouble with alarm 
Staff present on arrival  store open 
Staff prison on arrival building already unlocked 
The Officer has reported that upon arrival the site was unlocked and unalarmed 
Officer unable to locate alarm panel 
Attending officer reporting they found a small broken window while patrolling site  image attached 
The attending Officer has reported an un-secure window on the ground-floor  which cannot be secured 
Door left open to right of unit 26  secuirty checked building and locked up
door slightly damaged reported to building service job no  R977107
The attending Officer has reported that site vehicle barrier is insecure 
Attending officer reporting while patrolling site they identified roller shutter to inner complex isn t within normal operational parameters causing a security issue 
Our service partner advised that the main gate was left open by staff 
On arrival the main gate was open 
Attending officer reporting while patrolling site they identified a leak in the 1st floor toilet which has leaked out in to the corridor 
Attending officer reporting activation due to cleaner leaving the door propped open while working on site 
Attending officer reporting they were unable to complete internal patrols of site due to what looks like body fluids on floor and front door outside and on keypad  images attached 
Attending officer reporting main gate was found left open upon arrival 
Officer is reporting the panel of fencing is still missing from site 
Officer unable to access site as no survey has been carried out 
Attending officer reporting they were unable to secure site due o staff present 
Unable to secure the main gates due to no padlock
Attending officer reporting they were unable to complete internal patrols of site due to BT only requiring external patrol 
Officer reported unable to complete internal patrols of site due to BT only requiring external patrol 
The Officer has reported large amount of cable left outside of cable cages 
Our service partner advised that cables were left outside unsecured 
Contractor present on-site  receptionist set off alarm in error 
alarm reset by BT
Staff present on arrival  No further action required 
Staff on site
Staff on site Pauline Walker 
Officer is reporting that the front barrier is still broken
Arrived on site address given at 23:12  I was unable to find the site  after calling KHC who passed me on to Mitec the site was 0 7 miles away  when arrived on site informed by control room the job was cancelled at 23:30
External only  Site secure 
BT advised the officer to not enter the site 
Site secuirty on site  all ok
Officer reported the fire door was found open 
Part of the fencing is missing as previously reported 
Officer reported a leak in the gents toilet coming  from the the cleaner s mop filling tap and sink 
Sales advisor Mrs Janet Norwood on site
Met caretaker on site - hockey game taking place - caretaker advised keys held are out of date
Unable to reset alarm  Tried contacting alarm company however details held not up to date  Contacted EMCS who advised they could not remote reset 
No digi code for entry door
no static guard on site
officer reported no guard on site
officer reported fault on alarm system
Officer reported a security guard is on site carrying out regular patrols 
Officer reported the site is in use by the NHS 
officer attending advised he doesnt have the alarm codes for this site which is why he will not be doing internal checks 
Issue setting alarm panel
The attending officer has reported a maintenance team were on site who had switched the mains off  This was the cause for the mains fail 
The attending officer reported staff were already on site and had reset the alarm by arrival 
The attending officer has reported there were staff on site who had accidentally set off the alarm  The officer was also having difficulty resetting the alarm 
The attending officer has reported the fob held does not work 
no static guard on site
no guard on site
FM on site today   Unlock should have been cancelled as client was scheduled to unlock themselves 
SP has been told by RAM security officers that patrols are not needed today
The attending Officer has reported that he was unable to gain access to the main reception from the left hand side gate specified in the assignment instructions as construction fencing is blocking the route 
Officer reported staff were on site on arrival and spoke with Jimmy Johnstone 
Security guard on site
Officer is reporting that part of the perimeter fencing is missing 
Ongoing issue with gate being broken
Officer reported premises currently in use by  NHS 
The attending officer advised there were staff still on site  He spoke to Jill who advised they had cancelled this down however this was not passed on to The Keyholding Company in time to cancel the job down with our service partner 
Our officer reported when he arrived to site we were informed the job had been cancelled 
Our officer reported that the engineer did not arrive 
The officer advised that the engineer did not turn up and staff were on site 
The officer has reported that the activation was caused by the cleaner who opened the basement door to take the rubbish outside without realising the alarm was armed 
Officer reported staff are back to work 
The officer has attended the site but was advised that the fob to be collected is in a locked room  that can only be collected during the day 
Our officer reported there were staff on site  they had been on all night 
Both alarm codes held are invalid  Officer could not unset the alarm"""

freq = Counter(line_text.split()).most_common()
print(freq)