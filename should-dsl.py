# This is a temporary file!!
    * all_of
    * any_of
    * be
    * ended_with
    * equal # Documentação errada. O certo é equal_to ou be_equal_to
    * equal_to_ignoring_case
    * greater_than_or_equal_to
    * greater_than
    * in_any_order
    * into
    * kind_of
    * less_than_or_equal_to
    * less_than
    * like
    * throw
    * thrown_by

# should be (b)
${1:actual} |should_be| ${2:expected}
$0

# should not be (nb)
${1:actual} |should_not_be| ${2:expected}
$0

# Should have (h)
${1:collection} |should_have| ${2:items}
$0

# Should not have (nh)
${1:collection} |should_not_have| ${2:items}
$0

# Should be into (i)
${1:items} |should_be| into(${2:collection})
$0

# Should not be into (ni)
${1:items} |should_not_be| into(${2:collection})
$0

# Should be equal to (et)
${1:actual} |should_be| equal_to({2:expect})
$0

# Should not be equal to (net)
${1:actual} |should_not_be| equal_to({2:expect})
$0

# Should have all of (allof)
${1:collection} |should_have| all_of({2:items})
$0

# Should not have all of (nallof)
${1:collection} |should_not_have| all_of({2:items})
$0

# Should have any of (anyof)
${1:collection} |should_have| any_of({2:items})
$0

# Should not have any of (nanyof)
${1:collection} |should_not_have| any_of({2:items})
$0

# Should be ended with (ew)
${1:string} |should_be| ended_with({2:substring})
$0

# Should not be ended with (new)
${1:string} |should_not_be| ended_with({2:substring})
$0

# Should be greater than (g)
${1:bigger} |should_be| greater_than({2:smaller})
$0

# Should not be greater than (ng)
${1:bigger} |should_not_be| greater_than({2:smaller})
$0

# Should be greater than or equal to (ge)
${1:bigger} |should_be| greater_than_or_equal_to({2:smaller})
$0

# Should not be greater than or equal to (nge)
${1:bigger} |should_not_be| greater_than_or_equal_to({2:smaller})
$0

# Should be kind of (ko)
${1:instance} |should_be| kind_of({2:class})
$0

# Should not be kind of (nko)
${1:instance} |should_not_be| kind_of({2:class})
$0

# Should be less than (l)
${1:smaller} |should_be| less_than({2:bigger})
$0

# Should not be less than (nl)
${1:smaller} |should_not_be| less_than({2:bigger})
$0

# Should be less than or equal to (le)
${1:smaller} |should_be| less_than_or_equal_to({2:bigger})
$0

# Should not be less than or equal to (nle)
${1:smaller} |should_not_be| less_than_or_equal_to({2:bigger})
$0

# Should be equal to ignoring case (etic)
${1:actual} |should_be| equal_to_ignoring_case({2:expect})
$0

# Should not be equal to ignoring case (netic)
${1:actual} |should_not_be| equal_to_ignoring_case({2:expect})
$0

# Should have in any order (anyorder)
${1:collection} |should_have| in_any_order({2:items})
$0

# Should not have in any order (nanyorder)
${1:collection} |should_not_have| in_any_order({2:items})
$0

# should be like (bl)
${1:string} |should_be| like(${2:regex})
$0

# should not be like (nbl)
${1:string} |should_not_be| like(${2:regex})
$0

# should throw (t)
${1:raiser} |should| throw(${2:exception})
$0

# should not throw (nt)
${1:raiser} |should_not| throw(${2:exception})
$0

# should be throw by (t)
${1:exception} |should_be| throw_by(${2:raiser})
$0

# should not be throw by (nt)
${1:exception} |should_not_be| throw_by(${2:raiser})
$0

