Magic component design
=================

# Description 
  Casting event, that gives random chance of failure basing on the
  character traits and the spell difficulty.
  Has a set of strategic spells - decision driven major spells.
  Plus it allows of triggering casting events during the battle.
  

# Features 
_Planned and implemented_

  - [x] Mistcast events
  - [x] Main casting event: success or failure
  - [ ] Strategic decision triggered spells for basic lores (necromancy, chaos, fire, light, ice)
  - [ ] Common Battle Spell system: spells represented by spells special unit 
  - [ ] Special Battle Magic events: events for characters in-battle
  - [ ] Tactics for spell "troops" reflecting the common lore battle usage
  - [ ] Magic traits inheritance events
  - [ ] Art for basic lore (5 event gfx, traits)

# Dependencies
  - mutation events for failures
  - *on_actions* to trigger battle casting, magic inheritance and triggering battle spells
  - mutation events for failures
  - magic traits (four power traits + one trait for each lore)

# Inclusion



# Lores

**Ice**
Spells (strategic & battle)
 [ ] Blizzard - _strategic_, affect provinces makes it harder to travel
 [ ] Hailstorm - _strategic_, _siege spell_, affects the besieger army
 [ ] Biting Wind - _combat tactics_, triggers tactics
 [ ] Ice Walls - _strategic_, _siege spell_, creates ice walls that may defend in siege


Deadly Firestorm ("Pożoga śmierci") - chance to kill many characters
  
