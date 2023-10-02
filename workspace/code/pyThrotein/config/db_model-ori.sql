-- Table: IEX
CREATE TABLE IF NOT EXISTS IEX (
    date_IEX TEXT -- date IEX was performed
    column_IEX TEXT CHECK(column_IEX IN ('Q', 'S')) /* type of IEX column. (-)-charged protein binds to (+)-charged column (Q), (+)-charged protein binds to (-)-charged column (S) */
    column_volume_IEX TEXT CHECK(column_volume_IEX IN ('5', '6', '1')) -- volume (ml) of IEX column. Approximately related to maximum protein-bound capacity: 5 (max. 275 mg, type HP), 6 (max. 240 mg, type Resource), 1 (max. 45 mg, type Resource)
    purity_IEX INTEGER -- % protein purity compared to contaminants in an SDS-PAGE
    mg_IEX REAL -- protein yield (mg) after IEX
    PRIMARY KEY ( date_IEX column2)
);

-- Table: IMAC
CREATE TABLE IF NOT EXISTS IMAC (
    date_IMAC TEXT -- date IMAC was performed
    wash_IMAC TEXT CHECK(wash_IMAC IN ('mild', 'moderate', 'harsh', 'urea')) /* Type of wash in IMAC. Mild (low ionic strength, 200-500 mM NaCl), moderate (high ionic strength, 1 M NaCl), harsh (1 M NaCl plus LiSO4 and Bicine), urea (hard wash, denatures protein) */
    buffer_IMAC TEXT CHECK(buffer_IMAC IN ('T8.5', 'T8.0', 'T7.5', 'Ph7.5', 'Ph7.0', 'Ph6.8')) -- Type of buffer at which protein is eluted. T (Tris-HCl, pH 8.5, 8.0, 7.5), Ph (Na phosphate, pH 7.5, 7.0, 6.8)
    purity_IMAC INTEGER -- % protein purity compared to contaminants in an SDS-PAGE
    mg_IMAC REAL -- protein yield (mg) after IMAC
);

-- Table: Induction
CREATE TABLE IF NOT EXISTS Induction (
    date_ind TEXT -- date induction was performed
    cells TEXT CHECK(cells IN ('Star', 'Rosetta', 'pLEMO', 'Lobstr')) -- type of bacteria used to generate protein
    medium TEXT CHECK(medium IN ('2xYT', 'M9', 'P', 'Terrific_broth')) -- type of medium used to grow bacteria. According to nutrients richness/composition: Terrific_broth(extra-rich), 2xYT (rich), M9 (moderate), P (rich in phosphate)
    volume REAL -- Volume of medium used to grow bacteria
    OD REAL -- optical density at which protein is induced
    temp INTEGER -- temperature (Celsius) at which bacteria grow during induction
    hours INTEGER -- time (hours) that protein is being induced (from start of induction to pellet collection)
    pellet REAL -- pellet obtained (grams)
);

-- Table: Prot
CREATE TABLE IF NOT EXISTS Prot (
    exp_id INTEGER -- experiment identification number
    id TEXT -- step conditions identification number. One number each indicating a particular set of experimental conditions for each experiment performed 
    Protein TEXT -- protein name
    Species TEXT CHECK(Species IN ('mammal', 'CHIKV', 'VEEV', 'SARS_CoV_2')) -- mammal or virus species
    His_tag TEXT CHECK(His_tag IN ('N', 'C')) -- His-tag location in protein. N-terminal (N) or C-terminal (C)
    SUMO_tag TEXT CHECK(SUMO_tag IN ('TRUE', 'FALSE')) -- Contains (TRUE), or not (FALSE), SUMO-tag
    MW REAL -- molecular weight
    pI REAL -- isoelectric point, pH at which protein has no net charge. Values between 0 and 14
    Charge_pH7 REAL -- protein charge at pH7. Values between 0 and 14
);

-- Table: SEC
CREATE TABLE IF NOT EXISTS SEC (
    date_SEC TEXT -- date SEC was performed
    column_SEC TEXT CHECK(column_SEC IN ('superdex', 'superdex_highload')) -- type of SEC column. Related to maximum sample volume that can be loaded. Superdex (max. 0.45 ml), superdex_highload (max. 4.5 ml)
    column_unit_SEC TEXT CHECK(column_unit_SEC IN ('75200')) -- type of SEC column according to MW of contaminants to discard. 75 (for small MW contaminants), 200 (for high MW contaminants)
    purity_SEC INTEGER -- % protein purity compared to contaminants in an SDS-PAGE
    mg_SEC REAL -- protein yield (mg) after SEC
    peak_SEC INTEGER -- volume (ml) at which protein elutes in a SEC purification. Related to MW
);

-- Table: SUMO
CREATE TABLE IF NOT EXISTS SUMO (
    date_SUMO TEXT -- date SUMO cleavage was performed
    perc_cleaved_SUMO INTEGER -- percentage of protein cleaved in an SDS-PAGE
    mg_SUMO REAL -- protein yield (mg) after SUMO cleavage
);

