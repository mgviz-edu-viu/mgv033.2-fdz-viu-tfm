# mgv033.2-fdz-viu-tfm
TFM Francisco Dominguez
# FPLC (Fast Protein Liquid Chromatography) Protein Purification
## **Goal:** get enough amount of protein, with at least a minimum % purity, that allows a post-purification experiment

## Steps:

  - Protein design

  - Protein induction

  - Chromatography purification

    3.1. Capture
    
	    3.1.1. If protein contains SUMO, cleave after capture

    3.2. Intermediate

    3.3. Refinement

# 1. Protein Design

  Generate the amino acid sequence of the structure (protein + tags)
  Add a His-tag (or 6xHis) so that protein is captured in Capture Purification (see later)
  His-tag does not normally interfere with post-purification experiments
  His-tag can be N- or C-terminal (determined by experience in purification, post-purification purposes, etc)

  Add SUMO-tag? 
  SUMO helps to keep protein soluble, but it has to be removed (it can interfere with some experiments)

  Get protein characteristics

  Add protein sequence to https://protcalc.sourceforge.net/
  Theoretical Molecular Weight → protein band when we run a gel (see later)
  pI → isoelectric point, pH at which net charge is 0. Work always at least 1 log away in pH, or protein can precipitate 
  Charge at different pHs → i.e. pI 5.03 and pH7 -13.6? → protein is (-) charged in a pH8.5 buffer (see later)

# 2. Protein Induction

  Transform bacteria cells with plasmid, seed a Petri dish with selectable marker…
  Once reached Optical Density (O.D.) (~amount of bacteria):
  Set temperature for induction
  Collect an aliquot (non-induced)
  Add an inducer to make bacteria produce protein
  Pick one colony, to a growth medium (volume, shaking, 37C)
  Wait for several hours
  Collect an aliquot (induced)
  Transfer medium to a bottle 
  Centrifuge to collect pellet
  Measure pellet weight

  Some cells work better with some specific proteins
  We want bacteria to make proteins soluble in the cytoplasm → for example, too high temperature, too rich medium, too high O.D. can lead to bacteria making large amounts of some proteins, but more insoluble

# 3. Chromatography Purification

  Lysate cells (pellet) in appropriate buffer → think about pH, ionic strength, solubility of protein
  Centrifuge to get rid of debris → aliquots for gel (see later) to confirm that our protein is in the supernatant (Lysate, Supernatant and Pellet)
  Load protein into a chromatography column → our protein should stick to the column
  Wash column with buffer to remove unbound material
  Apply a gradient wash buffer - elution buffer to elute our protein
  Collect everything in fraction collection tubes

## 3.1. Capture

  First capture protein from all pellet (bacterial proteins, nucleic acids, etc)
  Our proteins are all His-tagged. Histidine has affinity for Ni2+ ions → always use an Immobilized Metal Affinity  Chromatography (IMAC) column charged with Ni2+
  Elute protein with a buffer containing imidazole (chemical with high affinity for Ni2+ and, therefore, competes with our protein)
  Monitor the purification → proteins absorb at 280 nm (UV-light)

## 3.1.1. SUMO cleavage

  If protein contains SUMO-tag, we cleave after IMAC
  To separate:
  Load in an IMAC column → theoretically, our protein would go through the column, and 6xHis-SUMO would be attached
  But some proteins can get sticked to the column and we lose a lot of protein
  Better → go to Intermediate purification with an Ion Exchange column, as total charge of SUMO is normally different from total charge of our protein (see later)

## 3.2. Intermediate

  IMAC purification is frequently not enough
  Ion exchange chromatography (IEX) separates molecules by their total charge → know theoretical net charge of our protein at the pH of the buffer!!!
  Steps:
   Dilute protein to a low ionic strength (i.e. 20 mM NaCl)
   Load protein to the column
   Wash with low-moderate ionic strength buffer
   Elute with gradient with a high ionic strength buffer (1M NaCl)

## 3.3. Refinement

  It is normally the last purification step
  It is often a Size Exclusion Chromatography (SEC) purification → it gives powerful separation from small number of contaminants 
  It separates by size (~molecular weight)
  

![image](https://github.com/mgviz-edu-viu/mgv033.2-fdz-viu-tfm/assets/167875/7d5a3cc0-3780-4d90-870d-a65e6c517488)
