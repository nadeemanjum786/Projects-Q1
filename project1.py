def mad_libs():
    adjective1 = input("Enter an adjective: ")
    plural_noun = input("Enter a plural noun: ")
    noun1 = input("Enter a noun: ")
    adverb1 = input("Enter an adverb: ")
    number = input("Enter a number: ")
    past_tense_verb1 = input("Enter a past tense verb: ")
    est_adjective = input("Enter an adjective ending in -est: ")
    past_tense_verb2 = input("Enter another past tense verb: ")
    adverb2 = input("Enter another adverb: ")
    adjective2 = input("Enter another adjective: ")
    
    story = f"""
    Today, my fabulous camp group went to a(n) {adjective1} amusement park. 
    It was a fun park with lots of cool {plural_noun} and enjoyable play structures. 
    When we got there, my kind counselor shouted loudly, "Everybody off the {noun1}." 
    We all pushed out in a terrible hurry. My counselor handed out yellow tickets, and we scurried in. 
    I was so excited! I couldn't figure out what exciting thing to do first. 
    I saw a scary roller coaster I really liked so, I {adverb1} ran over to get in the long line that had about {number} people in it. 
    When I finally got on the roller coaster I was {past_tense_verb1}. 
    In fact, I was so nervous my two knees were knocking together. 
    This was the {est_adjective} ride I had ever been on! 
    In about two minutes I heard the crank and grinding of the gears. 
    That’s when the ride began! When I got to the bottom, I was a little {past_tense_verb2}, but I was proud of myself. 
    The rest of the day went {adverb2}. 
    It was a(n) {adjective2} day at the fun park.
    """
    
    print(story)
    
mad_libs()