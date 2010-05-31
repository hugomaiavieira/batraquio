# Temporary file!!!

# should be (sb)
${1:actual} |should| be(${2:expected})
$0

# should not be (snb)
${1:actual} |should_not| be(${2:expected})
$0

# Should have (sh)
${1:collection} |should| have(${2:items})
$0

# Should not have (snh)
${1:collection} |should_not| have(${2:items})
$0

# Should not be into (sbi)
${1:items} |should_not| be_into(${2:collection})
$0


- all_of
- any_of
* be
- ended_with
- equal
- equal_to_ignoring_case
- greater_than_or_equal_to
- greater_than
- in_any_order
* into
- kind_of
- less_than_or_equal_to
- less_than
- like
- throw
- thrown_by

