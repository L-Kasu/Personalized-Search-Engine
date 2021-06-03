# tf-idf script for scrum presentation
# version: alpha1.1
# author: Niklas Munkes

import tf_idf.tf_idf_main as main


doc_dicts = [
    {"I" : 0,
     "W" : ['work', 'story', '1971', 'edit', 'detail', 'country', 'spit', 'howev', '1876', 'dewey', 'provid', 'brief', 'publ', 'abroad', 'appear', 'first', 'ful', 'describ', 'healthy', 'eighteen', 'nev', 'grow', 'long', 'biograph', 'system', 'pres', 'spur', 'libr', 'class', 'attempt', 'lif', 'nee', 'fut', 'decim', 'ddc', 'hist', 'continu', 'told', 'study']},
    {"I" : 1,
     "W" : ['doubt', 'period', 'wid', 'technolog', 'colleagu', 'way', 'ev', 'or', 'kingdom', 'rath', 'also', 'less', 'collect', 'org', 'receiv', 'tak', 'desk', 'proport', 'person', 'aspect', 'unit', 'report', 'act', 'analys', 'visit', 'rely', 'handbook', 'libr', 'stil', 'particul', 'rar', 'whol', 'contact', 'cur', 'sci', '104', 'inform', '6300', 'restrict', 'outsid', 'docu', 'peopl', 'situ', 'maj', 'techn', 'on', 'pattern', 'channel', 'regul', 'transfer', 'account', 'transf', 'us']},
    {"I" : 2,
     "W" : ['satisfact', 'writ', 'story', 'claim', 'simply', 'record', 'famili', 'way', 'obtain', 'els', 'bibliograph', 'inevit', 'contain', 'gre', 'org', 'along', 'discuss', 'form', 'certain', 'deal', 'simpl', 'control', 'slog', 'rel', 'mankind', 'ent', 'knowledg', 'inform', 'stock', 'much', 'sens', 'storeh', 'pow']},
    {"I" : 3,
     "W" : ['quest', 'although', 'provok', 'way', 'bas', 'new', 'parry', 'man', 'also', 'commit', 'provid', 'attitud', 'est', '267', 'serv', 'ugc', 'nat', 'best', 'endors', 'academ', 'aspect', 'report', 're-examination', 'nin', 'chang', 'lack', 'object', '1960', 'libr', 'gen', 'difficul', 'method', 'stressed', 'mad', 'long-established', 'inform', 'repot', 'nee', 'high', 'univers', 'remain', 'stim', 'research', 'purpos']},
    {"I" : 4,
     "W" : ['explod', 'comput', 'decad', 'handl', 'larg', 'milit', 'although', 'develop', 'disciplin', 'wid', 'technolog', 'rec', 'unavail', 'poss', 'complex', 'expery', 'man', 'caus', 'thing', 'many', 'numb', 'wom', 'model', 'gam', 'adv', 'first', 'train', 'soph', 'vary', 'war', 'school', '1956', 'simpl', 'well-developed', 'hundr', 'spread', 'mathem', 'eith', 'profess', 'year', 'sint', 'cours', 'method', 'mad', 'today', 'class', 'real', 'field', 'becom', 'widespread', 'level', 'introduc', 'tim', 'rapid', 'techn', 'origin', 'trac', 'on', 'electron', 'men', 'educ', 'main', 'calc', 'sim', 'prim', 'involv', 'last', 'dang', 'us']},
    {"I" : 5,
     "W" : ['work', 'full-time', 'writ', 'volunt', 'edit', 'abstract-publishing', 'many', 'publ', 'brief', 'contain', 'espec', 'stor', 'typ', 'benefit', 'instruct', 'part-time', 'aspect', 'standard', 'analys', 'reward', 'libr', 'stat', 'pleas', 'becom', 'tre', 'characteristc', 'exampl', 'devot', 'emphas', 'suppl', 'comput', 'computer-prepared', 'top', 'exerc', 'detail', 'discuss', 'evalu', 'gradu', 'program', 'effect', 'includ', 'extract', 'stud', 'nee', 'avail', 'effort', 'prep', 'conceiv', 'hist', 'contribut', 'study', 'chapt', 'develop', 'key', 'sent', 'index', 'cal', 'car', 'deserv', 'past', 'vary', 'school', 'act', 'unit', 'mat', 'believ', 'method', 'sect', 'inform', 'expend', 'how-to-do-it', 'know', 'industry', 'research', 'find', 'opportun', 'autom', 'us', 'text', 'import', 'gre', 'extend', 'receiv', 'increas', 'seg', 'abstract', 'appendix', 'select', 'profess', 'gen', 'cours', 'produc', 'much', 'on', 'understand']},
    {"I" : 6,
     "W" : ['remodel', 'book', 'solv', 'import', 'new', 'avoid', 'cas', 'build', 'ident', 'evalu', 'ellswor', 'enlarg', 'architect', 'structures', 'unsuccess', 'pres', 'success', 'ex', 'libr', 'exceiv', 'mistak', 'repres', 'don', 'attempt', 'mason', 'colleg', 'univers', 'problem', 'plan', 'fac', 'yal', 'mak', 'brown', 'show', 'exampl', 'study']},
    {"I" : 7,
     "W" : ['work', 'overlook', 'writ', 'const', 'not', 'apt', 'belles-letter', 'many', 'interest', 'publ', 'attitud', 'collect', 'presid', 'guy', 'concern', 'admir', 'poetry', 'cont', 'libr', 'thorough', 'port', 'fel', 'insist', 'contemp', 'book', 'good', 'review', 'lit', 'acquaint', 'felt', 'respect', 'world', 'contin', 'nee', 'colleg', 'engend', 'sign', 'keep', 'perhap', 'memb', 'prim', 'wel', 'lin', 'impress', 'develop', 'disciplin', 'manifest', 'way', 'acquir', 'thrust', 'staff', 'fict', 'respons', 'scholarship', 'mat', 'cross', 'admonit', 'lov', 'research', 'upon', 'admin', 'counsel', 'us', 'substitut', 'most', 'import', 'must', 'read', 'build', 'individ', 'facul', 'oblig', 'appr', 'profess', 'crit', 'gen', 'knowledg', 'though', 'mind', 'on', 'dealt']},
    {"I" : 8,
     "W" : ['valu', 'work', 'definit', 'idea', 'scholar', 'tradit', 'larg', 'approach', 'affect', 'bas', 'comp', 'untut', 'less', 'interest', 'addit', 'gre', 'est', 'democr', 'org', 'benef', 'read', 'unresolv', 'data-gathering', 'follow', '1890', 'vary', 'ar', 'meant', 'intellect', 'resist', 'survey', 'op', 'includ', 'analys', '1970', 'loc', 'object', 'libr', 'opin', 'gen', 'profess', 'princip', 'method', 'self-realization', 'cur', 'direct', 'confirm', 'class', 'guid', 'prom', 'nee', 'evid', 'soc', 'shelf', 'self-education', 'held', 'assum', 'polit', 'conceiv', 'access', 'consid', 'docu', 'questionnair', 'exhaust', 'problem', 'brows', 'instru', 'av', 'research', 'cit', 'find', 'left', 'self-indulgence', 'study', 'rel', 'us']},
    {"I" : 9,
     "W" : ['satisfy', 'feat', 'focus', 'period', '48', 'improv', 'medicin', 'cent', 'develop', 'confin', 'cov', 'poss', 'bas', 'exclud', 'acquir', 'recommend', 'design', 'aug', 'long-range', 'collect', 'stor', 'serv', 'journ', 'follow', 'nat', 'evalu', 'form', 'academ', 'subject', 'perc', 'us', 'resourc', 'bulk', 'lit', 'comprehend', 'includ', 'request', 'system', 'mat', 'worthwhil', 'depend', 'irrespect', 'loan', 'libr', 'interlibr', 'mad', 'without', 'prim', 'phys', 'nee', 'avail', 'init', 'commun', 'rapid', 'access', 'plan', 'delivery', 'maj', 'consid', 'photocop', 'purpos', 'langu', 'study', 'artic', 'restrict']},
]

qry_dicts = [
    {"I" : 0,
     "W" : ['mak', 'retriev', 'autom', 'relev', 'artic', 'concern', 'problem', 'describ', 'approxim', 'involv', 'us', 'cont', 'difficul', 'titl']},
    {"I" : 1,
     "W" : ['request', 'ref', 'dat', 'autom', 'inform', 'retriev', 'entir', 'oppos', 'act', 'respons', 'pertin', 'artic']},
    {"I" : 2,
     "W" : ['poss', 'inform', 'giv', 'sci', 'definit']},
    {"I" : 3,
     "W" : ['valu', 'work', 'definit', 'idea', 'scholar', 'tradit', 'larg', 'approach', 'affect', 'bas', 'comp', 'untut', 'less', 'interest', 'addit', 'gre', 'est', 'democr', 'org', 'benef', 'read', 'unresolv', 'data-gathering', 'follow', '1890', 'vary', 'ar', 'meant', 'intellect', 'resist', 'survey', 'op', 'includ', 'analys', '1970', 'loc', 'object', 'libr', 'opin', 'gen', 'profess', 'princip', 'method', 'self-realization', 'cur', 'direct', 'confirm', 'class', 'guid', 'prom', 'nee', 'evid', 'soc', 'shelf', 'self-education', 'held', 'assum', 'polit', 'conceiv', 'access', 'consid', 'docu', 'questionnair', 'exhaust', 'problem', 'brows', 'instru', 'av', 'research', 'cit', 'find', 'left', 'self-indulgence', 'study', 'rel', 'us']},
    {"I" : 4,
     "W" : ['encount', 'inform', 'spec', 'nee', 'retriev', 'man', 'system', 'train', 'prop', 'problem', 'us', 'lik', 'unobstruct', 'ordin', 'businessm', 'research']},
]


main.main(doc_dicts, qry_dicts)