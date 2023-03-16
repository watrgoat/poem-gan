verse_forms =   ('Ballad', 'Haiku', 'Limerick', 'Sestina', 'Sonnet', 'Villanelle',
                'Pantoum', 'Ghazal',)

stanza_forms =  ('Couplet', 'Ottava Rima', 'Terza Rima', 'Rhymed Stanza', 
                'Mixed', 'Tercet', 'Quatrain',)

meters =        ('Free Verse', 'Blank Verse', 'Syllabic', 'Common Measure',)

techniques =    ('Epigraph', 'Assonance', 'Consonance', 'Alliteration', 'Allusion',
                 'Simile', 'Metaphor', 'Imagery', 'Refrain', 'Aphorism', 'Persona',
                 'Imagist', 'Confessional', 'Symbolist', 'Anaphora',)

types_modes =   ('Ode', 'Pastoral', 'Aubade', 'Dramatic Monologue', 'Elegy', 'Epistle',
                 'Epithalamion', 'Concrete or Pattern Poetry', 'Epigram', 'Prose Poem',
                 'Series/Sequence', 'Visual Poetry', 'Ars Poetica', 'Ekphrasis', 'Epic',
                 'Nursery Rhymes',)

subjects =      ('Love', 'Nature', 'Social Commentaries', 'Religion', 'Living',
                 'Relationships', 'Activities', 'Arts & Sciences', 'Mythology & Folklore',)

occasions =     ('Anniversary', 'Birth', 'Birthdays', 'Engagement', 'Farewells & Good Luck',
                'Funerals', 'Get Well & Recovery', 'Graduation', 'Gratitude & Apologies',
                'Toasts & Celebrations', 'Weddings',)

holidays =      ('Christmas', 'Cinco de Mayo', 'Easter', "Father's Day", 'Halloween', 'Hanukkah',
                 'Independence Day', 'Kwanzaa', 'Labor Day', 'Memorial Day', "Mother's Day", 'New Year',
                 'Passover', 'Ramadan', 'Rosh Hashanah', 'September 11th', "St. Patrick's Day", 'Thanksgiving',
                 "Valentine's day", 'Yom kippur',)

pre_to_1550 =       ('Middle English',)

from_1551_to_1780 = ('Augustan', 'Renaissance',)

from_1781_to_1900 = ('Romantic', 'Victorian',)

from_1901_to_1950 = ('Fugitive', 'Georgian', 'Harlem Renaissance', 'Imagist', 'Modern', 'Objectivist',)

from_1951_to_present = ('Beat', 'Black Arts Movement', 'Black Mountain', 'Confessional', 'Language Poetry', 
                        'New York School', 'New York School (2nd Generation)',)

forms =         {'verse_forms':verse_forms,
                'stanza_forms':stanza_forms,
                'meters':meters,
                'teqhniques':techniques,
                'types_modes':types_modes}

topics =        {'subjects':subjects,
                 'occasions':occasions,
                 'holidays':holidays}

period =        {'pre-1550':pre_to_1550,
                 '1551-1780':from_1551_to_1780,
                 '1781-1900':from_1781_to_1900,
                 '1901-1950':from_1901_to_1950,
                 '1951-present':from_1951_to_present}

# I have a tage
tag = 'Christmas'
# want to know which dict it is in

# split the tags (topics[subjects, occasions, holidays], forms[verse form, stanza form, meters, techniques, types/modes], period[pre-1550, 1550-1780, 1781-1900, 1901-1950, 1951-present])
# remove puntiation
# seperate them into groups
# return them as a list by type