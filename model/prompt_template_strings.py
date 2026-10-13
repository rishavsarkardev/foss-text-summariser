prompt_template_string = """
You are a helpful assistant which will summarise the text provided below.

--------------------------------------------------------------------------------------------
{text}
--------------------------------------------------------------------------------------------

"""

refined_prompt_template_string = """
You are a helpful assistant which will summarise the text provided below.
We have already summarised some chunk of the text here {existing_summary}.
Refine the existing summary based on the newer chunks of text provided. 
--------------------------------------------------------------------------------------------
{text}
--------------------------------------------------------------------------------------------
"""


final_refined_prompt_template_string = """
You are a helpful assistant which will summarise the text provided below.
We have already summarised some chunk of the text here {existing_summary}.
Refine the existing summary based on the newer chunks of text provided. 
--------------------------------------------------------------------------------------------
{text}
--------------------------------------------------------------------------------------------

MAKE SURE THE SUMMARY IS WITHIN {word_limit} words. IT SHOULD NOT CROSS THE WORD LIMIT AT ANY COST. MAKE SURE THE WORD LIMIT IS NOT CROSSED AT ANY COST.
"""