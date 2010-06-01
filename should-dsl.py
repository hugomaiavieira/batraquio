#this is a temporary
    * all_of
    * any_of
    * be
    * ended_with
    * equal
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

# Should be equal (sbe)
${1:actual} |should| be_equal({2:expect})
$0

# Should not be equal (snbe)
${1:actual} |should_not| be_equal({2:expect})
$0

# Should have all of (shall)
${1:collection} |should_not_have| all_of({2:items})
$0

# Should not have all of (snhall)
${1:collection} |should_not_have| all_of({2:items})
$0

# Should have any of (shall)
${1:collection} |should_not_have| any_of({2:items})
$0

# Should not have any of (snhall)
${1:collection} |should_not_have| any_of({2:items})
$0

# Should be ended with (sbew)
${1:sequence} |should| be_ended_with({2:element})
$0

# Should not be equal (snbew)
${1:sequence} |should_not| be_ended_with({2:element})
$0

