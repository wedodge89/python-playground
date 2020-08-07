# Best Practices

## Variables
- snake_case
    - 👍: user_iq
    - 👎: userIq (this is called "camel case")
- Start with lowercase letter or underscore
    - 👍: user_iq
    - 👎: User_iq
- Letters, numbers, underscores only
    - 👍: user_iq
    - 👎: user_iq!
- Case sensitive
    - 👍: user_iq == user_iq
    - 👎: user_IQ =/= user_iq
- Don't overwrite keywords
    - 👍: user_iq
    - 👎: print
- Variable names should be descriptive without being overly verbose
    - 👍: user_iq
    - 👎: number, the_iq_of_the_person_taking_this_specific_test

## Commenting
- Should add valuable information.
- Should help other developers, or you in the future, to understand what the code is doing, especially in more complicated functions.
- Good commenting cannot replace good code. Make sure your code is clear and functional, and that comments just elaborate.
- Comments should not repeat what is obvious to average developer reading the code. 