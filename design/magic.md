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
  - [x] Casting event 
  - [ ] Strategic spells events for basic lores (necromancy, chaos, fire, light, ice)
  - [x] Casting decisions for basic lores
  - [ ] Magic traits inheritance events

# Dependencies: 
  - mutation events for failures
  - *on_actions* to trigger battle casting
  - mutation events for failures
  - magic traits (four power traits + one trait for each lore)
