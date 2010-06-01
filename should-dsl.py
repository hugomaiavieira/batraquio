# This is a temporary file!!
    * all_of # Erro! Está fazendo o matcher ao contrário. Retorna True quando deveria ser False e False quando deveria ser True
    * any_of
    * be
    * ended_with
    * equal # Documentação errada. O certo é equal_to ou be_equal_to
    - equal_to_ignoring_case
    * greater_than_or_equal_to
    * greater_than
    - in_any_order
    * into
    * kind_of
    * less_than_or_equal_to
    * less_than
    - like
    - throw
    - thrown_by

# should be (b)
${1:actual} |should| be(${2:expected})
$0

# should not be (nb)
${1:actual} |should_not| be(${2:expected})
$0

# Should have (h)
${1:collection} |should| have(${2:items})
$0

# Should not have (nh)
${1:collection} |should_not| have(${2:items})
$0

# Should not be into (i)
${1:items} |should_not| be_into(${2:collection})
$0

# Should be equal to (et)
${1:actual} |should| be_equal_to({2:expect})
$0

# Should not be equal to (net)
${1:actual} |should_not| be_equal_to({2:expect})
$0

# Should have all of (allof)
${1:collection} |should_have| all_of({2:items})
$0

# Should not have all of (nallof)
${1:collection} |should_not_have| all_of({2:items})
$0

# Should have any of (anyof)
${1:collection} |should_not_have| any_of({2:items})
$0

# Should not have any of (nanyof)
${1:collection} |should_not_have| any_of({2:items})
$0

# Should be ended with (ew)
${1:string} |should| be_ended_with({2:substring})
$0

# Should not be ended with (new)
${1:string} |should_not| be_ended_with({2:substring})
$0

# Should be greater than (g)
${1:bigger} |should| be_greater_than({2:smaller})
$0

# Should not be greater than (ng)
${1:bigger} |should_not| be_greater_than({2:smaller})
$0

# Should be greater than or equal to (ge)
${1:bigger} |should| be_greater_than_or_equal_to({2:smaller})
$0

# Should not be greater than or equal to (nge)
${1:bigger} |should_not| be_greater_than_or_equal_to({2:smaller})
$0

# Should be kind of (ko)
${1:instance} |should| be_kind_of({2:class})
$0

# Should not be kind of (nko)
${1:instance} |should_not| be_kind_of({2:class})
$0

# Should be less than (l)
${1:smaller} |should| be_less_than({2:bigger})
$0

# Should not be less than (nl)
${1:smaller} |should_not| be_less_than({2:bigger})
$0

# Should be less than or equal to (le)
${1:smaller} |should| be_less_than_or_equal_to({2:bigger})
$0

# Should not be less than or equal to (nle)
${1:smaller} |should_not| be_less_than_or_equal_to({2:bigger})
$0

