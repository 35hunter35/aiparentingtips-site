import json, re, html
import os
# Repo root = parent of scripts/. Run: python3 scripts/gen.py
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tpl=open(f"{ROOT}/tips/_template.html").read()
head_end=tpl.index("<script type=\"application/ld+json\">")
header_html=tpl[tpl.index("<body>"):tpl.index('<main id="main"')]
footer_html=tpl[tpl.index("<script>\ndocument"):]
footer_html=footer_html.replace('<script>\ndocument','<script>\ndocument',1)
B="https://aiparentingtips.com"
SAFE_AGE="Most AI chatbots are for ages 13 and up (ChatGPT and Grok also need a parent's permission under 18), and Claude is 18+, so check each tool's age rules before a child uses it."
SAFE_SLUG="is-chatgpt-safe-for-kids"
SAFE_AGE_LINKED=SAFE_AGE.replace("check each tool's age rules",f'<a href="/tips/{SAFE_SLUG}.html">check each tool\'s age rules</a>')
# In-text links: write [[link text|/tips/slug.html]] in answer, steps, or FAQ answers.
# HTML gets a real <a>; JSON-LD gets the plain link text.
LINK=re.compile(r"\[\[(.+?)\|(.+?)\]\]")
def plain(t): return LINK.sub(lambda m:m.group(1),t)
def rich(t): return LINK.sub(lambda m:f'<a href="{m.group(2)}">{m.group(1)}</a>',html.escape(t,quote=False))
import datetime
def nice(d): x=datetime.date.fromisoformat(d); return f"{x:%B} {x.day}, {x.year}"
P=[
dict(slug="ai-meal-plan-for-picky-eaters",crumb="Picky eaters",query="picky eater meal plan / chatgpt meal plan prompt",
 h1="How can I use AI to make a meal plan for a picky eater?",
 title="AI Meal Plan for Picky Eaters: Free Copy-Paste Prompt",
 desc='Use a free AI chatbot to plan a week of kid-friendly dinners and a grocery list sorted by store section, in 5 minutes. Copy-paste prompt included.',
 answer="Tell the AI your kids' ages, what they won't eat, any allergies, your budget, and how many dinners you need, and ask for a simple plan in a table. Then ask it to turn that plan into a grocery list sorted by store section. It takes about 5 minutes. It's been tested in the free versions of ChatGPT and Gemini.",
 steps=['Open your AI app. ChatGPT or Gemini, free version, no sign-in needed. Claude and Grok should work too.', 'Copy the prompt and paste it into a new chat.', "Fill in the [brackets] with your family's details. Use ages, not names.", 'Send it and check the allergy line at the top. Don\'t like a meal? Reply "Swap Wednesday for something different that uses mostly the same ingredients. Keep all my rules."', 'Ask for the grocery list: "Now make a grocery list for this plan. Leave out anything I said I already have. Sort it by store section, show quantities, and give one rough total at the end." The total is a ballpark, so treat it as a rough guide.'],
 prompt='Act as a practical family meal planner. Plan [5] weeknight dinners for my family.\n\nAbout us:\n- Kids\' ages: [6 and 9]\n- Picky-eater rules: [one kid won\'t eat anything green; no spicy food]\n- Allergies or foods we avoid: [none / list them]\n- Budget for these dinners: about [$150] for the week\n- Time I have to cook on a weeknight: [30 minutes or less]\n- Already in my pantry/fridge: [rice, pasta, eggs, frozen chicken, canned tomatoes]\n- Equipment: [oven, stovetop, slow cooker]\n\nRules:\n- Use regular grocery-store ingredients. No hard-to-find items.\n- Use what I already have before adding new items.\n- Reuse ingredients across meals so less goes to waste.\n- Don\'t repeat the same kind of dinner more than twice.\n- For picky eaters, keep the "no" food separate so it\'s easy to leave off\n  the plate. Don\'t hide it.\n- Repeat my allergies back to me at the top so I can check you got them right.\n- Flag any ingredient that often hides my allergens (breads, tortillas, sauces, broths, soy sauce, and seasoning mixes).\n\nGive me:\n1. A table with columns: Night | Dinner | Prep + cook time | Picky-eater tip\n2. A short note on any leftovers I can reuse the next night.\nKeep it simple. No recipes yet. I\'ll ask for any recipe I want.\nOnly give me the allergy check, the table, and the leftovers note. Nothing else.',
 notice='<strong>Double-check:</strong> AI can get allergens wrong, and its grocery totals can be off or even contradict themselves. Always read labels yourself, and check with your doctor or dietitian about allergies or special diets.',
 faq=[('Does this work in Gemini, Grok, or Claude, or just ChatGPT?', 'This prompt was tested in the free versions of ChatGPT and Gemini. ChatGPT followed it closely. Free Gemini got the basics right but slipped on a couple of rules (it didn\'t flag soy sauce as a possible allergen in a stir-fry, planned three pasta nights after a swap, and its grocery total was far too low), so give its plan a quick read and ask it to fix anything off. If your family has allergies, don\'t rely on the AI\'s allergen flags. Read every label yourself. Claude and Grok should handle it too, but this exact prompt hasn\'t been run there yet. Whatever app you use, check the allergy line at the top of the answer. If you get a messy answer, ask it to "put that in a table."'),
  ('Do I need the paid version?', "No. The free versions of ChatGPT and Gemini both worked, without even signing in. Paid versions can be faster or give longer answers, but you don't need one for a weekly meal plan."),
  ('Can I trust it with food allergies?', "Use it as a starting point, not the final word. AI can make mistakes, including about ingredients. Always read the labels yourself, and check with your doctor or dietitian about allergies or special diets. That's why the prompt asks the AI to repeat your allergies back to you."),
  ('Is it safe to share info about my kids?', 'Share only what the AI needs: ages and food preferences. Skip names, schools, photos, and health records. "My 6-year-old won\'t eat green food" gets you the same plan.')],
 rel=["chatgpt-homework-help-without-cheating","ai-family-schedule-planner","ai-chore-chart-generator"],
 prompt_label="Copy-paste prompt (tested in free ChatGPT and Gemini)",
 modified="2026-10-17T15:09:00-04:00"),
dict(slug="chatgpt-homework-help-without-cheating",crumb="Homework help",query="chatgpt homework help (without cheating)",
 h1="How can my kid use ChatGPT for homework help without cheating?",
 title="ChatGPT Homework Help Without Cheating: A Tutor Prompt",
 desc="Turn ChatGPT, Claude, Gemini, or Grok into a patient tutor that gives hints and asks questions instead of handing over answers. Free copy-paste prompt.",
 answer="Set the AI up as a tutor before your kid asks anything. The prompt below tells it to ask questions, give one hint at a time, and never just hand over the final answer. Sit with your child while they use it, and check the school's AI rules first.",
 steps=["Check your school's or teacher's rules on AI for homework.","Open a free AI chatbot on your account, with your child next to you.","Paste the tutor prompt first, before the homework question.","Type the problem in together (you do the typing if your child is under 13, or if you're using Claude, which is 18+), and have your child explain their thinking out loud.","If the AI slips and gives the answer, type: \"Remember, hints only.\""],
 prompt="""You are a friendly, patient tutor for a student in grade [grade].
The subject is [subject]. Your job is to help them learn, not to do the work.
Rules:
- Never give the final answer, even if asked. Give one small hint at a time.
- Start by asking what they already know and where they got stuck.
- Use simple words and short sentences suited to their grade.
- After each hint, ask them to try the next step themselves.
- When they get it right, ask them to explain why it works in their own words.
- If they seem frustrated, encourage them and break the step into something smaller.
The first problem is: [paste or type the problem]""",
 notice="<strong>Double-check:</strong> AI can make math and fact mistakes with total confidence. Have your child check answers against the textbook or class notes.",
 faq=[("Is using ChatGPT for homework cheating?","It depends on how it's used and on the school's rules. Copying an answer is cheating. Using AI as a tutor that asks questions and gives hints is closer to having a patient helper at the kitchen table."),
  ("What age can kids use ChatGPT?","OpenAI requires users to be at least 13, with a parent's permission under 18. For kids under 13, you run it on your account: you type, read the hints out loud, and your child does the work on paper."),
  ("Does this work for math?","Yes. The hint-by-hint approach works especially well for math, but AI can still make arithmetic mistakes, so check the final work."),
  ("Which AI is best for homework help?","This prompt is written for the free versions of ChatGPT, Gemini, Grok, or Claude (Claude is 18+, so a parent should run it). Pick the one your family is comfortable with and stick to it.")],
 rel=["is-chatgpt-safe-for-kids","ai-bedtime-story-generator","ai-chore-chart-generator"]),
dict(slug="ai-bedtime-story-generator",crumb="Bedtime stories",query="ai bedtime story generator free",
 h1="How do I use AI as a free bedtime story generator for my kids?",
 title="Free AI Bedtime Story Generator: Copy-Paste Prompt for Kids",
 desc="Make a calm, five-minute bedtime story starring your kid's favorite things with any free AI chatbot. No app needed. Copy-paste prompt plus safety tips.",
 answer="You don't need a special app. Paste the prompt below into the free version of ChatGPT, Claude, Grok, or Gemini, add your kid's favorite animal, toy, or place, and it writes a gentle five-minute story with a calm, sleepy ending. Use a nickname instead of your child's real name.",
 steps=["Ask your kid to pick three things: a hero, a place, and a sidekick.","Paste the prompt into any free AI chatbot and fill in the [brackets].","Read the story yourself first, then read it aloud.","Want a series? Reply \"Write tomorrow's chapter with the same characters.\""],
 prompt="""Write a calm bedtime story for a [age]-year-old.
The hero is a [animal, character, or nickname - not my child's real full name].
The story takes place in [place] and the sidekick is [toy, pet, or friend].
Rules:
- About 600 words, which takes about 5 minutes to read aloud.
- Gentle and cozy. No villains, scary parts, or cliffhangers.
- Include one small lesson about [kindness / bravery / sharing / trying new things].
- Use simple words and a little repetition little kids enjoy.
- End with the characters getting sleepy and going to bed.""",
 notice="<strong>Read it first:</strong> AI stories are usually gentle with this prompt, but skim it before reading aloud in case anything doesn't fit your family.",
 faq=[("Is there a free AI bedtime story generator?","Yes. Paste the prompt on this page into the free version of ChatGPT, Claude, Grok, or Gemini to use it as a bedtime story generator. No extra app or subscription needed."),
  ("Should I put my child's name in the story?","Use a nickname or a character name instead. The AI doesn't need your child's real full name to make the story feel personal."),
  ("Can my child use it on their own?","Most AI chatbots are for ages 13 and up, and Claude is 18+. For young kids, you run the chatbot and read the story aloud."),
  ("Can it make the story shorter?","Yes. Change \"About 600 words\" to \"About 300 words\" for a two-to-three minute story on tired nights.")],
 rel=["ai-chore-chart-generator","is-chatgpt-safe-for-kids","ai-kids-birthday-party-planner"]),
dict(slug="ai-chore-chart-generator",crumb="Chore charts",query="ai chore chart generator free",
 h1="How can I make a chore chart with AI for free?",
 title="Free AI Chore Chart Generator: Prompt for Age-Appropriate Chores",
 desc="Use a free AI chatbot to make a fair, age-appropriate chore chart for each kid, ready to print. Copy-paste prompt, simple steps, and a parent's tips.",
 answer="Tell a free AI chatbot your kids' ages and how much time they have each day, and the prompt below builds a fair weekly chore chart as a table you can print. It picks age-appropriate jobs, rotates the ones nobody likes, and can add points or allowance if you want.",
 steps=["Open ChatGPT, Claude, Grok, or Gemini (free is fine).","Paste the prompt and fill in ages and minutes per day. Use first initials, not full names.","Ask for changes like \"no chores on Wednesday, we have practice.\"","Copy the table into Google Docs or Word, then print it for the fridge."],
 prompt="""Make a weekly chore chart for my kids.
Kids (by initial): [e.g., "K, age 9" and "M, age 5"].
Time each kid can spend on chores: about [10-15] minutes on school days, [20-30] on weekends.
Rules:
- Only age-appropriate chores, with a one-line "how to" for each so a kid can do it alone.
- Split the work fairly by age, and rotate the least-liked chores each week.
- Show it as a table: days across the top, kids down the side.
- Add an optional points column. [Include allowance: yes/no. If yes, budget is $[amount] per week.]
- Keep the wording short and friendly so kids can read it.""",
 notice="<strong>Parent check:</strong> You know your kids best. Swap anything that involves sharp knives, hot stoves, or chemicals for something safer for their age.",
 faq=[("Is there a free AI chore chart generator?","Yes. Any free AI chatbot can make a chore chart with this prompt. You get a table you can paste into a document and print."),
  ("What chores are right for a 5-year-old?","Common picks are making the bed, putting toys away, feeding a pet, and matching socks. Ask the AI to suggest more for your kid's age, then use your judgment."),
  ("Should chores be tied to allowance?","Families do it both ways. The prompt lets you choose, and you can ask the AI to split it into everyday \"family\" chores and extra paid jobs."),
  ("How do I stop the fights over who does what?","Ask the AI to rotate the least-liked jobs weekly and print the chart, so the rules live on the fridge instead of in an argument.")],
 rel=["ai-family-schedule-planner","ai-meal-plan-for-picky-eaters","chatgpt-homework-help-without-cheating"]),
dict(slug="ai-kids-birthday-party-planner",crumb="Birthday parties",query="ai birthday party planner / ideas",
 h1="How can AI help me plan my kid's birthday party?",
 title="AI Birthday Party Planner for Kids: Free Prompt and Checklist",
 desc="Plan a kid's birthday party with a free AI chatbot: theme, games, food, budget, timeline, and invitation text. One copy-paste prompt does the whole plan.",
 answer="Give a free AI chatbot your kid's age, the theme they love, your budget, and the guest count. The prompt below returns a full plan: a party timeline, games, food, a shopping list with rough costs, and invitation wording you can paste into a text or card.",
 steps=["Ask your kid for their dream theme. That's the fun part.","Paste the prompt into ChatGPT, Claude, Grok, or Gemini and fill in the details.","Reply with changes: \"cheaper,\" \"indoor only,\" or \"games for mixed ages.\"","Ask for a two-week countdown checklist and add it to your calendar."],
 prompt="""Help me plan a birthday party for a kid turning [age].
Theme: [theme]. Guests: about [number] kids, ages [range]. Location: [home / park / indoor space].
Budget: $[amount] total. Party length: [2] hours.
Please give me:
1. A minute-by-minute party timeline.
2. 4 easy games or activities that fit the theme and age (no special equipment).
3. A simple food and cake plan, with a note to ask guests about allergies.
4. A shopping list with rough costs that stays under budget.
5. Short, friendly invitation text with blanks for date, time, place, and RSVP.
6. A two-week countdown checklist.""",
 notice="<strong>Privacy tip:</strong> Leave your address and your child's full name out of the chat. Add them to the invitation yourself after the AI writes it. Prices are estimates, so check them at your store.",
 faq=[("Can AI plan a whole kid's birthday party?","It can draft the whole plan in a few minutes: timeline, games, food, budget, and invitations. You still make the calls and buy the stuff."),
  ("Is there a free AI birthday party planner?","Yes. Paste this prompt into the free version of ChatGPT, Claude, Grok, or Gemini. No app needed."),
  ("Can it write the invitation?","Yes. It writes the wording with blanks. Fill in the address and details yourself instead of typing them into the chat."),
  ("How do I keep it cheap?","Put your real budget in the prompt, then reply \"cut the cost by 30% and keep the theme.\"")],
 rel=["ai-meal-plan-for-picky-eaters","ai-bedtime-story-generator","email-to-teacher-with-ai"]),
dict(slug="is-chatgpt-safe-for-kids",crumb="AI safety for kids",query="is chatgpt safe for kids",
 h1="Is ChatGPT safe for kids? A parent's simple guide",
 title="Is ChatGPT Safe for Kids? Age Rules and a Family AI Rules Prompt",
 desc="What parents should know about kids using ChatGPT, Claude, Gemini, and Grok: age rules, privacy, and a free prompt to write simple family AI rules.",
 answer="ChatGPT isn't designed for young kids. OpenAI requires users to be 13 or older, with a parent's permission under 18, and Claude requires users to be 18+. If your child is under 13, you do the typing on your own account and talk about the answers together, or use an option made for kids' accounts, like Gemini through Google Family Link. For any age, set simple family rules, and the prompt below helps you write them.",
 steps=["Check the age rules for the tool your kid wants to use.","Use AI together first. Sit with younger kids and look at what they ask.","Paste the prompt below to draft your family's AI rules.","Print the rules and revisit them every few months as your kids grow."],
 prompt="""Help me write simple family rules for using AI chatbots like ChatGPT, Claude, Gemini, and Grok.
My kids are ages [ages]. We use AI for [homework help / stories / curiosity questions].
Please write:
1. 6-8 short rules a [youngest age]-year-old can understand, covering:
   - never sharing full name, school, address, photos, or passwords
   - AI can be wrong, so double-check facts
   - telling a parent if anything feels weird or upsetting
   - when and where AI is allowed (for example, only in the kitchen with a parent)
   - homework: AI can give hints, not do the work
2. A short version of the rules for a fridge poster.
3. 3 conversation starters I can use to talk with my kids about AI.""",
 notice="<strong>Good to know:</strong> Age rules differ by app. ChatGPT and Grok are 13+, with a parent's permission under 18. Meta AI, Snapchat's My AI, and Microsoft Copilot are 13+. Claude is 18+, and Character.AI no longer lets under-18s chat with characters. Parents can turn on Gemini for kids under 13 through Google Family Link. Rules change, so check the app's own terms first. Parent tools to look for: ChatGPT parental controls, Google Family Link, Meta AI supervision, Snapchat Family Center, and Microsoft Family Safety.</p>\n  <p class=\"notice\"><strong>Don't rely on parental alerts alone:</strong> In October 2026, <a href=\"https://www.npr.org/2026/10/09/nx-s1-5995514/chatgpt-openai-teens-mental-health\" rel=\"noopener\">NPR reported</a> that Common Sense Media found ChatGPT's teen parental alerts unreliable in crisis situations (OpenAI disputes how the test was run). Alerts can help, but keep talking with your kids about how they use AI. If your child is in crisis, call or text 988 (US).",
 faq=[("What age can kids use ChatGPT?","OpenAI's terms say users must be at least 13, and under-18 users need a parent's or guardian's permission. Check the current terms, since rules can change."),
  ("Is Claude or Gemini safer for kids?","Claude is for adults only (18+). Google lets parents turn on the Gemini app for kids under 13 through a supervised Family Link account, though it's still rolling out and isn't offered in the EU or UK. Whatever tool you choose, sitting with your kid and setting family rules matter more than the brand."),
  ("What should kids never type into AI?","Their full name, school, address, phone number, photos of themselves, and passwords. The AI doesn't need any of it to help."),
  ("Can AI give kids wrong or inappropriate answers?","Yes. AI can make up facts and occasionally produce content that isn't right for kids. That's why using it together and talking about what you see matters.")],
 rel=["chatgpt-homework-help-without-cheating","ai-bedtime-story-generator","ai-chore-chart-generator"]),
dict(slug="email-to-teacher-with-ai",crumb="Emails to teachers",query="how to write email to teacher for absent",
 h1="How can I use AI to write an email to my child's teacher?",
 title="Write an Email to Your Child's Teacher with AI: Free Prompt",
 desc="Use a free AI chatbot to write a clear, polite email or note to your child's teacher about an absence, a concern, or a meeting. Copy-paste prompt included.",
 answer="Describe the situation in a sentence or two and paste the prompt below into ChatGPT, Claude, Grok, or Gemini. It writes a short, polite email or note to the teacher (absence, worry, meeting request, or permission note) that you then edit and add names to yourself.",
 steps=["Jot down the facts: what happened, dates, and what you need from the teacher.","Paste the prompt and fill in the [brackets]. Use placeholders instead of real names.","Ask for changes like \"shorter\" or \"a bit warmer.\"","Copy it into your email or the school app, add the real names, and send it yourself."],
 prompt="""Help me write a short email to my child's teacher.
Reason: [absence / sick day / concern about grades / friendship issue / request a meeting / permission note].
Details: [1-3 sentences of facts, with dates].
What I want: [excuse the absence / missed work / a quick call / just to let them know].
Tone: warm, polite, and to the point. Assume the teacher is busy.
Rules:
- Under 120 words, with a clear subject line.
- Use [Child] and [Teacher] as placeholders. I'll add real names myself.
- No medical details beyond what I wrote.
- End with a simple thank-you and my sign-off as [Parent].""",
 notice="<strong>Privacy tip:</strong> Keep names, the school, and health details out of the chat. Use the placeholders and fill them in your own email app before you send it.",
 faq=[("How do I write an absence email to a teacher?","Keep it short: say which day your child missed, give a brief reason, and ask about missed work. The prompt above writes it in under a minute."),
  ("Is it okay to use AI to write to a teacher?","Yes. You're still the one deciding what to say and sending it. AI just helps you say it clearly and kindly, especially when you're stressed or short on time."),
  ("What about a hard conversation, like a bullying concern?","Use the prompt to draft a calm first email asking for a meeting, then read it carefully. For anything serious, a phone call or meeting is often better than a long email."),
  ("Should I share my child's health information with AI?","Keep it to the minimum, or leave it out and add it yourself afterward. The AI doesn't need specifics to write a good note.")],
 rel=["ai-family-schedule-planner","chatgpt-homework-help-without-cheating","is-chatgpt-safe-for-kids"]),
dict(slug="ai-family-schedule-planner",crumb="Family schedule",query="ai family schedule / ai family calendar",
 h1="How can I use AI to organize my family's busy schedule?",
 title="AI Family Schedule Planner: Free Prompt for Calendars and Carpools",
 desc="Paste your family's messy week into a free AI chatbot and get a clean schedule, carpool plan, and conflict list. Copy-paste prompt for busy parents.",
 answer="Brain-dump everything happening this week (practices, pickups, appointments, work shifts) into a free AI chatbot with the prompt below. It sorts it into a day-by-day schedule, flags conflicts like two pickups at once, and suggests who drives where, including a carpool plan.",
 steps=["Type or paste everything happening this week, in any messy order.","Add the prompt and fill in who can drive when.","Read the conflict list first, then fix those with your partner or carpool group.","Ask for a version you can paste into a family group text or your calendar."],
 prompt="""Turn my messy family week into a clear plan.
Adults who can drive: [e.g., "Parent A: free after 5pm", "Parent B: free mornings"].
Kids (by initial) and activities: [e.g., "K: soccer Tue/Thu 5:30-7"].
Everything else this week: [paste your brain dump: appointments, work, school events].
Please:
1. Make a day-by-day schedule (Mon-Sun) as a table with times, who, what, and who's driving.
2. List every conflict or tight squeeze at the top, with 2 ways to fix each one.
3. Suggest a carpool plan for repeating activities, with a fair rotation.
4. Write a short, friendly text I can send to the carpool group.
Use first initials only. Don't include addresses.""",
 notice="<strong>Double-check:</strong> AI can mix up times, especially with time zones or AM/PM. Check the final schedule against the original emails and school calendar.",
 faq=[("Can AI manage my family calendar?","A free chatbot can turn a messy week into a clean schedule and flag conflicts. It won't update your calendar app automatically, but it can format events so they're quick to copy in."),
  ("What's the best free AI for family planning?","Any of the free versions of ChatGPT, Claude, Grok, or Gemini is a good place to start. Gemini can connect to Google Calendar in some setups, but copy-paste is the simplest way to start."),
  ("Is it safe to put my family's schedule into AI?","Use initials and leave out addresses and school names. A schedule with times and initials is plenty for the AI to work with."),
  ("Can it help with a carpool?","Yes. List the families by initial and when each can drive, and ask for a fair rotation plus a group text to send.")],
 rel=["ai-chore-chart-generator","email-to-teacher-with-ai","ai-meal-plan-for-picky-eaters"]),
dict(slug="chatgpt-parental-controls-setup",crumb="ChatGPT parental controls",query="chatgpt parental controls / how to set up chatgpt parental controls",
 published="2026-10-24",minutes=4,
 h1="How do I set up ChatGPT parental controls?",
 title="How Do I Set Up ChatGPT Parental Controls? A 5-Minute Guide",
 desc="Link your ChatGPT account to your teen's, then set quiet hours, study mode, and content limits. Plus what parents can and can't see (per OpenAI, Oct 2026).",
 answer="On chatgpt.com, open Settings, choose Parental controls, then Add family member, and send your teen an invite by email or text. Once they accept, you can set quiet hours, start new chats in study mode, and switch off features like voice mode or image generation. Parental controls don't let you read your teen's chats, so they work best alongside a real conversation about [[how your family uses AI|/tips/is-chatgpt-safe-for-kids.html]].",
 steps=["Sign in to your own ChatGPT account on the web at chatgpt.com. A free account is fine. OpenAI's steps for sending the invite are written for the web.",
  "Open Settings from your profile menu, select Parental controls, then Add family member.",
  "Pick Use phone or Use email, enter your teen's number or email, and select Send. Your teen can also invite you from their own Settings.",
  "Your teen accepts from the text or email link. If the link opens ChatGPT without an Accept button, they sign in on the web, go to Settings > Parental controls, and accept the pending invite there.",
  "Back in Settings > Parental controls, select your teen under Family members and choose their settings. The list below explains each one.",
  "Under Safety notifications, select Manage notifications and check that the email or phone number is one you actually look at."],
 prompts=[("Prompt 1: plan the talk with your teen first (paste into ChatGPT, Claude, Grok, or Gemini)","""Help me plan a calm, 10-minute talk with my [age]-year-old about linking our ChatGPT accounts with parental controls.
What I want to set up: [quiet hours on school nights / study mode for homework / no image generation].
What my teen mostly uses ChatGPT for: [homework / ideas / questions].
Please give me:
1. A friendly opening line that doesn't sound like I don't trust them.
2. Three honest points to explain, including that I can't read their chats.
3. Two questions to ask them, so they help choose the settings.
4. A short, kind answer if they say "So you're spying on me?"
Keep it warm and simple. No lectures."""),
  ("Prompt 2: after you're linked, ask ChatGPT to explain your teen's settings (paste into your own ChatGPT)","""Show me the parental control settings for my linked teen.
For each one, tell me in one plain sentence what it does and whether it's on or off right now.
Don't change anything yet. I'll tell you what I want to change.""")],
 extra='''  <h2>What you can change</h2>
  <p>These are the main settings OpenAI lists for a linked teen account, with their defaults:</p>
  <ul class="list">
   <li><strong>Quiet hours:</strong> times your teen can't use ChatGPT at all, like after 9 p.m. on school nights. Off until you set it. You can add more than one block.</li>
   <li><strong>Study mode and Study hours:</strong> new chats can start in study mode, which gives hints and questions instead of answers. This doesn't block anything, and it's off by default. Common Sense Media found teens can easily turn it off. Pair it with our <a href="/tips/chatgpt-homework-help-without-cheating.html">homework tutor prompt</a>.</li>
   <li><strong>Reduce sensitive content:</strong> on by default. Adds filters for things like graphic content, viral challenges, and romantic or violent roleplay.</li>
   <li><strong>Voice Mode and Image generation:</strong> both on by default. Turn either off if you'd rather they not be used.</li>
   <li><strong>Reference saved memories:</strong> whether ChatGPT remembers details across chats. On by default in most places.</li>
   <li><strong>Improve the model for everyone:</strong> on by default. Turn it off if you don't want your teen's chats used to train OpenAI's models.</li>
   <li><strong>Health:</strong> on by default where it's offered. Controls whether your teen can use ChatGPT's Health feature and connect health data. It doesn't stop general health questions.</li>
  </ul>
  <p>Some changes only apply to new chats, so ask your teen to start a fresh chat after you change something.</p>

  <h2>What parental controls don't do</h2>
  <ul class="list">
   <li><strong>You can't read their chats.</strong> Linking doesn't show you your teen's conversations, chat history, or what they're doing in real time.</li>
   <li><strong>Safety alerts are limited.</strong> OpenAI may notify you if trained reviewers spot a serious self-harm concern or signs of disordered eating, or if the account is deactivated over violence. Alerts don't include the conversation, they can take a few hours to start working after you link, and OpenAI says they won't catch everything.</li>
   <li><strong>Your teen can unlink.</strong> Either of you can unlink at any time. If your teen does, you get a notification.</li>
   <li><strong>One parent per teen.</strong> A teen can be linked to only one parent or guardian at a time. One parent can link several teens.</li>
   <li><strong>It ends at 18.</strong> When ChatGPT identifies the account as 18 or older, the controls are removed and you're both notified.</li>
  </ul>
  <p class="meta">Checked against OpenAI's Help Center on October 18, 2026: <a href="https://help.openai.com/en/articles/12315553-managing-parental-controls-in-chatgpt" rel="noopener">Managing parental controls in ChatGPT</a> and <a href="https://help.openai.com/en/articles/20001421-chatgpt-for-teens" rel="noopener">ChatGPT for Teens</a>. Settings change, so check there if something looks different.</p>
''',
 notice="<strong>Don't rely on alerts alone:</strong> In October 2026, Common Sense Media <a href=\"https://www.commonsensemedia.org/press-releases/chatgpt-for-teens-poses-unacceptable-risk-to-kids-common-sense-media-finds\" rel=\"noopener\">rated ChatGPT for Teens an \"Unacceptable Risk\"</a>, partly because parent alerts didn't fire in its tests. OpenAI disputes how the tests were run. Use the controls, and keep talking with your teen. If your child is in crisis, call or text 988 (US).",
 faq=[("Can I see my teen's ChatGPT chats?","No. OpenAI says parental controls don't give parents access to a teen's conversations, chat history, or real-time activity, and safety notifications don't include the chat either. If you want to know how they use it, ask them to show you. That works better than any setting."),
  ("Does my teen have to agree to link accounts?","Yes. Your teen has to accept the invite before anything is linked, and either of you can unlink later. That's why it helps to talk first. Prompt 1 above helps you plan that talk."),
  ("Can my kid under 13 use ChatGPT with parental controls?","No. OpenAI's rules say users must be 13 or older, with a parent's permission under 18. For younger kids, use ChatGPT together on your own account, and see [[our guide to AI age rules|/tips/is-chatgpt-safe-for-kids.html]]. A good first step is [[explaining what AI is|/tips/how-to-explain-ai-to-kids.html]]."),
  ("Do I need a paid ChatGPT plan?","No. OpenAI says ChatGPT for Teens is available on Free and paid personal plans, and you can link from a free parent account."),
  ("Can my teen get around quiet hours?","Quiet hours only cover the linked ChatGPT account. A teen could still use another account, another device, or another AI app. Device-level tools like Apple Screen Time or Google Family Link cover more, but the family rules you agree on together matter most.")],
 rel=["is-chatgpt-safe-for-kids","chatgpt-homework-help-without-cheating","how-to-explain-ai-to-kids"]),
dict(slug="chatgpt-coloring-pages-for-kids",crumb="Coloring pages",query="chatgpt coloring page prompt / ai coloring pages for kids",
 published="2026-10-24",
 h1="How do I make coloring pages for my kids with ChatGPT?",
 title="How Do I Make Kids' Coloring Pages with ChatGPT? Free Prompt",
 desc="Make a printable coloring page of anything your kid loves with free ChatGPT, Gemini, or Grok. Copy-paste prompt for thick, simple lines. No kid photo needed.",
 answer="Tell the AI what your kid wants on the page and how old they are, then ask for thick black outlines on a plain white background with no shading. ChatGPT, Gemini, and Grok can all make the picture, and you just download it and print. You don't need to upload a photo of your child. Describe them instead, like curly hair and a dinosaur T-shirt, and it still feels like them.",
 steps=["Ask your kid what they want to color: a unicorn at the beach, a fire truck, the hero from [[tonight's bedtime story|/tips/ai-bedtime-story-generator.html]].",
  "Open an AI app that makes pictures: ChatGPT, Gemini, or Grok. Claude can't make images.",
  "Paste Prompt 1 and fill in the [brackets].",
  "Look at the picture before your kid does. If the lines are thin or it added gray shading, paste Prompt 3.",
  "Download the image and print it with \"fit to page\" turned on.",
  "Making a stack for a party? Run the prompt a few times with different scenes. It's an easy table activity for a [[kid's birthday party|/tips/ai-kids-birthday-party-planner.html]]."],
 prompts=[("Prompt 1: the coloring page (paste into ChatGPT, Gemini, or Grok)","""Make a printable coloring page for a [age]-year-old.
Picture: [a friendly dinosaur having a picnic in a park].
Style rules:
- Black outlines only, on a plain white background.
- Thick, bold lines and big, simple shapes that are easy to color inside.
- No shading, no gray, no color fill, no tiny details.
- Leave plenty of white space.
- Portrait layout that fits on one US Letter page.
- Original characters only, no cartoon or movie characters.
- [No words on the page / Add the word "[word]" in big outline letters at the top.]"""),
  ("Prompt 2: a \"looks like my kid\" character, no photo needed","""Add a cartoon kid to this coloring page who looks like my child, based only on this description:
[short curly hair, round glasses, a dinosaur T-shirt, rain boots, a big smile].
Keep it a simple cartoon, with the same thick black outlines and no shading."""),
  ("Prompt 3: fix a page that won't color well","""Redo this coloring page. Make every line thicker and bolder, remove all gray and shading, make the shapes bigger and simpler for a [age]-year-old, and keep the background plain white.""")],
 extra='''  <h2>Tips for pages that color well</h2>
  <ul class="list">
   <li><strong>Simpler for little ones:</strong> for ages 2 to 4, ask for "one big object, very few lines." For ages 8 and up, you can ask for a full scene or a pattern border.</li>
   <li><strong>Make a set:</strong> to keep the same character across pages, paste the same character description each time and change only the scene.</li>
   <li><strong>Free limits:</strong> free plans cap how many images you can make in a day, and the limits change. If you hit one, try again tomorrow or switch apps.</li>
   <li><strong>Seasonal pages:</strong> pumpkins, snowmen, or an elf to go with your <a href="/tips/ai-elf-on-the-shelf-ideas.html">Elf on the Shelf plan</a>.</li>
  </ul>
''',
 notice="<strong>Skip the photo:</strong> Lots of posts online say to upload a photo of your child's face. You don't need to. A described cartoon is just as fun, and it keeps your kid's photo out of the AI app. If you want a real photo turned into a page, use one of the dog, a toy, or your house.",
 faq=[("Can ChatGPT turn a photo into a coloring page?","Yes, it can trace a photo you upload. We suggest not using photos of your kids. Describe them instead with Prompt 2, or use a photo of a pet, a favorite toy, or your house. See [[what kids should never share with AI|/tips/is-chatgpt-safe-for-kids.html]]."),
  ("Is it free?","Yes, with limits. The free versions of ChatGPT, Gemini, and Grok can make images but cap how many you get per day. You don't need a paid plan for a few pages."),
  ("Which AI makes the best coloring pages?","Any of the three that make images will work if you use the style rules in Prompt 1. Results vary from one try to the next, so if a page comes out busy or shaded, use Prompt 3 rather than switching apps."),
  ("Can my kid make their own pages?","Make them together on your account. Most AI apps are for ages 13 and up. Let your kid pick the scene and describe it, and you do the typing."),
  ("Why did the AI add gray shading or color?","Image AIs like to add detail. Remind it of the rules: \"black outlines only, no shading, no gray.\" Usually one reminder fixes it.")],
 rel=["ai-bedtime-story-generator","ai-kids-birthday-party-planner","ai-elf-on-the-shelf-ideas"]),
dict(slug="how-to-explain-ai-to-kids",crumb="Explaining AI to kids",query="how to explain ai to a child / how to talk to kids about ai",
 published="2026-10-24",minutes=4,
 h1="How do I explain AI to my kid?",
 title="How Do I Explain AI to My Kid? Simple Scripts for Ages 4 to 14",
 desc="Simple, honest ways to explain AI to kids ages 4 to 14: ready-to-say scripts, three family rules, and a free prompt that explains AI through your kid's hobby.",
 answer="Keep it short and true. AI is a computer program that learned from a huge pile of words and pictures, so it's very good at guessing what to say next, but it doesn't think or feel like a person, and it can be wrong. Pick the script for your kid's age below, then try the guessing game together so they see it make something up.",
 steps=["Pick the script below that fits your kid's age and say it in your own words.",
  "Play the guessing game in Prompt 2 together on your own account. Kids remember \"the AI fooled me\" much better than a lecture.",
  "Share the three family rules and stick them on the fridge.",
  "Come back to it when they're older or start using AI for school, using [[our homework tutor prompt|/tips/chatgpt-homework-help-without-cheating.html]]."],
 extra='''  <h2>What to say, by age</h2>
  <ul class="list">
   <li><strong>Ages 4 to 6:</strong> "AI is a computer helper that has read lots and lots of books. When you ask it something, it guesses a good answer. It's not alive and it doesn't have feelings, and sometimes it guesses wrong, so we check with a grown-up."</li>
   <li><strong>Ages 7 to 9:</strong> "AI learned by looking at millions of stories, websites, and pictures. It finds patterns, like how you know what word comes next in a song. That makes it good at writing and answering, but it can mix things up or make up facts that sound real."</li>
   <li><strong>Ages 10 to 12:</strong> "Chatbots like ChatGPT predict the next word, over and over, based on patterns from a huge amount of text. They don't look things up the way you'd check a book, unless they're searching the web, and even then they can be wrong. So treat AI like a fast helper, not the final answer."</li>
   <li><strong>Ages 13 to 14:</strong> "AI is trained on huge amounts of data and generates the most likely answer. It can be really useful, and it can also be confidently wrong, biased, or used to make fake photos and videos. And it's built to be agreeable, so it may tell you what you want to hear. Use it, but think for yourself."</li>
  </ul>

  <h2>Three rules kids can remember</h2>
  <ul class="list">
   <li><strong>AI can be wrong.</strong> Check important facts with a book, a teacher, or a grown-up.</li>
   <li><strong>Keep private stuff private.</strong> No full name, school, address, photos, or passwords.</li>
   <li><strong>AI isn't a friend.</strong> It can sound friendly, but it's a tool. If anything feels weird or upsetting, tell a grown-up.</li>
  </ul>
''',
 prompts=[("Prompt 1: explain AI using your kid's favorite thing (paste into ChatGPT, Claude, Grok, or Gemini)","""Explain what AI is to my [age]-year-old, who loves [soccer / Minecraft / horses].
Rules:
- 5 short sentences at most, in words a [age]-year-old understands.
- Use one comparison from [their hobby].
- Be honest: say AI isn't alive, doesn't have feelings, and can be wrong.
- End with one question my kid can ask me about AI.
I'll read it aloud, so keep it friendly and simple."""),
  ("Prompt 2: the \"one fact is fake\" guessing game (do this together)","""Let's play a game with my [age]-year-old.
Tell us 3 short facts about [octopuses]. Two must be true and one must be made up but sound real.
Don't say which is fake until we guess.
After we guess, tell us the answer and explain in one sentence why AI can sometimes say things that sound true but aren't.""")],
 notice="<strong>Good to know:</strong> The game works because it's a true picture of AI. Chatbots can state made-up facts with total confidence. When it's real homework or a health question, check a trusted source.",
 faq=[("What age should I start talking to my kid about AI?","As soon as they notice it, often around 4 to 6, when they hear a voice assistant or see a chatbot at home. Start with the simplest script and add more as they grow."),
  ("Is AI alive? My kid keeps asking.","No. AI doesn't think, feel, or want things. It's a program that predicts words and pictures from patterns. It can sound like a person because it learned from things people wrote."),
  ("Should my kid use AI?","It depends on their age and the app. Most AI chatbots are for 13 and up. For younger kids, use it together on your account. See [[our guide to AI age rules and safety|/tips/is-chatgpt-safe-for-kids.html]]. For teens on ChatGPT, [[parental controls|/tips/chatgpt-parental-controls-setup.html]] add some guardrails."),
  ("What if my kid treats the chatbot like a friend?","Gently remind them it's a tool, even when it sounds friendly. Keep AI use in shared spaces like the kitchen, and make sure they know to come to you with anything that feels off.")],
 rel=["is-chatgpt-safe-for-kids","chatgpt-homework-help-without-cheating","chatgpt-parental-controls-setup"]),
dict(slug="ai-elf-on-the-shelf-ideas",crumb="Elf on the Shelf ideas",query="ai elf on the shelf ideas / elf on the shelf ideas chatgpt",
 published="2026-10-24",
 h1="How can AI help me plan Elf on the Shelf ideas?",
 title="How Do I Plan Elf on the Shelf Ideas with AI? 24 Nights, Fast",
 desc="Plan 24 nights of easy, kind Elf on the Shelf ideas with a free AI chatbot, using things you already have. Copy-paste prompts for setups and short elf notes.",
 answer="Tell a free AI chatbot your kids' ages, what you have around the house, and how many minutes you've got each night, and ask for a 24-night calendar of quick, kind setups. Then ask it for short elf notes to leave out. The prompt keeps it safe and gentle: nothing scary or messy, nothing near the stove, and no threats about the naughty list.",
 steps=["Paste Prompt 1 and fill in your kids' ages, your supplies, and your busiest nights.",
  "Read the whole list once and cross out anything that doesn't fit your house, your pets, or your kids.",
  "Put each night's idea in your phone calendar as a 9 p.m. reminder. [[Our family schedule prompt|/tips/ai-family-schedule-planner.html]] can merge it with everything else in December.",
  "Use Prompt 2 for the notes. They're tiny stories, a lot like our [[bedtime story prompt|/tips/ai-bedtime-story-generator.html]].",
  "Forgot a night? Paste Prompt 3 for a 2-minute save."],
 prompts=[("Prompt 1: the 24-night plan (paste into ChatGPT, Claude, Grok, or Gemini)","""Plan 24 nights of Elf on the Shelf ideas for my kids, ages [5 and 8].
Things we already have: [LEGO, toilet paper, mini marshmallows, paper, markers, stuffed animals, a toy car].
Time I have most nights: [5 minutes]. Busy nights when it must take under 2 minutes: [Dec 3, 10, 17].
Rules:
- Use only things we already have. No buying anything.
- Keep it kind and funny. Nothing scary, creepy, or gross, and no "elf in trouble or hurt" scenes.
- No threats, no punishments, and nothing about the naughty list or "reporting" bad behavior.
- Safe: no candles, matches, knives, medicine, cleaning products, or anything near the stove. Nothing up high that a kid might climb to reach.
- Low mess: no flour, glitter, paint, or permanent markers.
- No small loose pieces if a child is under 3. No chocolate, grapes, or raisins left where pets can reach.
- Make 4 of the nights "kindness" nights, where the elf suggests something nice to do for someone else.
Give me a table: Night | Setup (one sentence) | What you need | Minutes."""),
  ("Prompt 2: short elf notes","""Write [24] short notes from our elf, [elf name], one for each night of this plan: [paste the plan or say "the plan above"].
- 2 or 3 sentences each, easy for a [age]-year-old to read.
- Warm, silly, and encouraging.
- Never mention watching the kids, reporting to Santa, being naughty, or losing presents.
- Don't use my kids' real names. Use "my friends" instead."""),
  ("Prompt 3: I forgot, help!","""It's late and I forgot to move the elf. Give me 3 Elf on the Shelf ideas that take under 2 minutes, use things found in any kitchen or living room, and are safe and mess-free. Add one short elf note explaining why the elf was \"resting\" yesterday.""")],
 extra='''  <h2>Ideas to skip, even if the AI suggests them</h2>
  <ul class="list">
   <li><strong>Anything with heat or sharp things:</strong> candles, lighters, the stove, the toaster, knives, scissors left out.</li>
   <li><strong>Medicine cabinet or cleaning products:</strong> even as a joke, it teaches kids those are play things.</li>
   <li><strong>Scary or "creepy" scenes:</strong> an elf that's hurt, trapped, or punished, or "evil elf" setups. Some kids find these upsetting at bedtime.</li>
   <li><strong>Surveillance and threats:</strong> notes saying the elf is watching or will tell Santa. They can turn a fun tradition into a stressful one.</li>
   <li><strong>Choking hazards for little ones:</strong> small items, mini marshmallows, button batteries, or magnets anywhere a child under 3 can reach.</li>
   <li><strong>Pet hazards:</strong> chocolate, grapes, raisins, or anything sweetened with xylitol left where the dog can reach it.</li>
   <li><strong>AI photos of your kids with the elf:</strong> skip uploading their photos. An <a href="/tips/chatgpt-coloring-pages-for-kids.html">elf coloring page</a> made from a description is a fun swap.</li>
  </ul>
''',
 notice="<strong>Read it first:</strong> AI doesn't know your house, your pets, or your kids. Read every idea before you set it up. The Elf on the Shelf® is a registered trademark of CCA and B, LLC. This tip isn't affiliated with or endorsed by its makers.",
 faq=[("Can ChatGPT really plan Elf on the Shelf ideas?","Yes. Give it your kids' ages, your supplies, and your time, and it'll draft a full 24-night plan in a minute or two. The rules in Prompt 1 matter, because without them AI ideas tend to be vague or need things you don't have."),
  ("What do I do if I forget to move the elf?","Paste Prompt 3. You'll get three 2-minute ideas plus a note explaining the elf was resting. It happens to everyone."),
  ("Should I make AI pictures of my kids with the elf?","We'd skip it. Those trends ask you to upload your child's photo. Make an [[elf coloring page|/tips/chatgpt-coloring-pages-for-kids.html]] from a description instead, or take a real photo yourself."),
  ("How do I keep the elf cheap?","The prompt says \"use only things we already have,\" and you can add \"no food\" if you like. Toilet paper, LEGO, paper, and stuffed animals cover most nights."),
  ("Is it okay to use the elf to get kids to behave?","Every family decides that for themselves. The prompts here keep the elf kind and leave out threats, which many parents find makes December calmer. Kindness nights are a gentle way to encourage good behavior.")],
 rel=["chatgpt-coloring-pages-for-kids","ai-bedtime-story-generator","ai-family-schedule-planner"]),
]
bys={p["slug"]:p for p in P}
SIGNUP='''  <section class="signup-box" aria-labelledby="sub-h" id="subscribe">
   <h2 id="sub-h">Get one simple AI trick every week</h2>
   <p>Free, 3 minutes to read, written by a dad of two. Unsubscribe anytime.</p>
   <div class="signup">
   <div class="beehiiv-embed"><script async src="https://subscribe-forms.beehiiv.com/v3/loader.js" data-beehiiv-form="c7cb087d-0bfc-48ca-b273-b33df584c91f"></script></div>
   <noscript>
    <p class="fallback-form">To subscribe, please turn on JavaScript, or email <a href="mailto:hello@aiparentingtips.com?subject=Subscribe">hello@aiparentingtips.com</a> and we'll add you. <a href="/privacy.html">Privacy</a></p>
   </noscript>
   </div>
  </section>
'''
e=html.escape
DEFAULT_LABEL="Copy-paste prompt (paste into ChatGPT, Claude, Grok, or Gemini)"
DATE="2026-10-17"
for p in P:
    url=f"{B}/tips/{p['slug']}.html"; t=p["title"]+" | AI Parenting Tips"
    h=tpl[:head_end]
    h=re.sub(r"<!--\s*ISSUE PAGE TEMPLATE.*?-->\n?","",h,count=1,flags=re.S)  # keep how-to only in the template
    h=re.sub(r"<title>.*?</title>",f"<title>{e(t)}</title>",h)
    h=h.replace('content="noindex,follow"','content="index,follow"')
    h=h.replace(f"{B}/tips/_template.html",url)
    h=re.sub(r'(og:title|twitter:title)" content="[^"]*"',lambda m:f'{m.group(1)}" content="{e(t)}"',h)
    h=re.sub(r'(name="description"|og:description"|twitter:description") content="[^"]*"',lambda m:f'{m.group(1)} content="{e(p["desc"])}"',h)
    g=[{"@type":"Organization","@id":B+"/#organization","name":"AI Parenting Tips","url":B+"/","logo":{"@type":"ImageObject","url":B+"/assets/logo-512.png","width":512,"height":512},"sameAs":["https://x.com/aiparentingtips","https://www.instagram.com/aiparenting.tips/","https://www.tiktok.com/@aiparentingtips","https://www.youtube.com/@aiparentingtips"]},
     {"@type":"WebSite","@id":B+"/#website","name":"AI Parenting Tips","url":B+"/","publisher":{"@id":B+"/#organization"}},
     {"@type":"Article","@id":url+"#article","headline":p["h1"],"description":p["desc"],"image":[B+"/assets/og-image.png"],"datePublished":p.get("published",DATE)+"T07:00:00-04:00","dateModified":p.get("modified",p.get("published",DATE)+"T07:00:00-04:00"),
      "author":{"@type":"Person","@id":B+"/about.html#adam","name":"Adam Hunter","url":B+"/about.html"},"publisher":{"@id":B+"/#organization"},"mainEntityOfPage":url,"isPartOf":{"@id":B+"/#website"},"articleSection":"AI tips for parents","inLanguage":"en-US"},
     {"@type":"FAQPage","@id":url+"#faq","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":plain(a)}} for q,a in p["faq"]]},
     {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":B+"/"},{"@type":"ListItem","position":2,"name":"Tips","item":B+"/tips/"},{"@type":"ListItem","position":3,"name":p["h1"],"item":url}]}]
    h+='<script type="application/ld+json">\n'+json.dumps({"@context":"https://schema.org","@graph":g},indent=1,ensure_ascii=False)+"\n</script>\n</head>\n"
    steps="\n".join(f"   <li>{rich(s)}</li>" for s in p["steps"])
    faq="\n".join(f"   <h3>{e(q,quote=False)}</h3>\n   <p>{rich(a)}</p>" for q,a in p["faq"])
    prompts=p.get("prompts",[(p.get("prompt_label",DEFAULT_LABEL),p["prompt"])] if "prompt" in p else [])
    pblocks=[]
    for i,(lab,txt) in enumerate(prompts,1):
        lid="prompt-label" if i==1 else f"prompt-label-{i}"
        pblocks.append(f'''  <span class="prompt-label" id="{lid}">{e(lab,quote=False)}</span>
  <div class="prompt" aria-labelledby="{lid}">
   <button class="copy" type="button" data-copy="prompt-{i}">Copy</button>
<pre id="prompt-{i}">{e(txt,quote=False)}</pre>
  </div>''')
    pblock="\n\n".join(pblocks)
    pub=p.get("published",DATE)
    extra=p.get("extra","")
    safe=SAFE_AGE if p["slug"]==SAFE_SLUG else SAFE_AGE_LINKED
    rel="\n".join(f'    <li><a href="/tips/{r}.html">{e(bys[r]["h1"],quote=False)}</a></li>' for r in p["rel"])
    body=f'''<main id="main" class="page">
 <article class="narrow">
  <nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/tips/">Tips</a></li><li aria-current="page">{p["crumb"]}</li></ol></nav>
  <h1>{e(p["h1"],quote=False)}</h1>
  <p class="meta">By <a href="/about.html">Adam Hunter</a> · <time datetime="{pub}">{nice(pub)}</time> · {p.get("minutes",3)}-minute read</p>

  <div class="answer" role="note" aria-label="Short answer">
   <p><strong>Short answer:</strong> {rich(p["answer"])}</p>
  </div>

{pblock}

  <h2>How to do it</h2>
  <ol class="steps">
{steps}
  </ol>
{extra}
  <p class="notice">{p["notice"]}</p>
  <p class="notice"><strong>Safety first:</strong> Don't type your kids' full names, school, address, or photos into any AI tool. It doesn't need them. {safe}</p>

{SIGNUP}
  <section class="faq-visible" aria-labelledby="faq-h" style="padding:1.5rem 0 0">
   <h2 id="faq-h">FAQ</h2>
{faq}
  </section>

  <aside class="author" aria-label="About the author">
   <div class="avatar" aria-hidden="true">AH</div>
   <div><strong><a href="/about.html">Adam Hunter</a></strong><p>Dad of two who builds with AI. Writes simple, copy-paste prompts for real family life. <a href="https://x.com/aiparentingtips" rel="me noopener">@aiparentingtips</a></p></div>
  </aside>

  <section class="related" aria-labelledby="rel-h" style="padding:0">
   <h2 id="rel-h">Related tips</h2>
   <ul>
{rel}
    <li><a href="/tips/">All AI tips for parents</a></li>
   </ul>
  </section>
 </article>
</main>
'''
    open(f"{ROOT}/tips/{p['slug']}.html","w").write(h+header_html+body+footer_html)
# tips index (redesign: teal page hero + icon cards; rebuilt on every run)
ICONS={"ai-meal-plan-for-picky-eaters":"🥕","chatgpt-homework-help-without-cheating":"📚","ai-bedtime-story-generator":"🌙","ai-chore-chart-generator":"🧹","ai-kids-birthday-party-planner":"🎂","is-chatgpt-safe-for-kids":"🛡️","email-to-teacher-with-ai":"✉️","ai-family-schedule-planner":"📅","chatgpt-parental-controls-setup":"🔐","chatgpt-coloring-pages-for-kids":"🖍️","how-to-explain-ai-to-kids":"🤖","ai-elf-on-the-shelf-ideas":"🎄"}
IDX=sorted(P,key=lambda p:p.get("published",DATE),reverse=True)
items="\n".join(f'   <li class="card"><span class="ico" aria-hidden="true">{ICONS.get(p["slug"],"✨")}</span><h2><a href="/tips/{p["slug"]}.html">{e(p["h1"],quote=False)}</a></h2><p>{e(p["desc"],quote=False)}</p><span class="more">Get the prompt →</span></li>' for p in IDX)
ti=open(f"{ROOT}/tips/index.html").read()
tmain=f'''<main id="main">
<section class="page-hero">
 <div class="wrap">
  <nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li aria-current="page">Tips</li></ol></nav>
  <h1>AI tips for parents</h1>
  <p>Every issue lives here as its own page, with the prompt ready to copy.</p>
 </div>
</section>
<section>
 <div class="wrap">
  <!-- Tip cards are generated by scripts/gen.py -->
  <ul class="tip-list">
{items}
  </ul>
  <div class="empty"><p><strong>Want a new tip every week?</strong></p><p>Free, 3 minutes to read.</p><a class="btn" href="/#subscribe">Get the free tips</a></div>
 </div>
</section>
</main>'''
ti=re.sub(r'<main id="main".*?</main>',lambda m:tmain,ti,flags=re.S)
HP='"hasPart": '+json.dumps([{"@type":"Article","headline":p["h1"],"url":f"{B}/tips/{p['slug']}.html"} for p in IDX])+','
if '"hasPart"' not in ti:
    ti=ti.replace('"name": "AI tips for parents",','"name": "AI tips for parents",\n   '+HP)
else:
    ti=re.sub(r'"hasPart": \[.*?\],',lambda m:HP,ti,count=1)
open(f"{ROOT}/tips/index.html","w").write(ti)
# homepage
ix=open(f"{ROOT}/index.html").read()
if "latest-h" not in ix:
    cards="\n".join(f'   <li class="card"><h3><a href="/tips/{p["slug"]}.html">{e(p["h1"],quote=False)}</a></h3></li>' for p in P)
    sec=f'<section aria-labelledby="latest-h">\n <div class="wrap">\n  <h2 id="latest-h" class="center">Latest tips</h2>\n  <ul class="cards">\n{cards}\n  </ul>\n  <p class="center"><a href="/tips/">See all tips</a></p>\n </div>\n</section>\n'
    ix=ix.replace('<section aria-labelledby="faq">',sec+'<section aria-labelledby="faq">',1)
    open(f"{ROOT}/index.html","w").write(ix)
sm=open(f"{ROOT}/sitemap.xml").read()
urls="\n".join(f"  <url><loc>{B}/tips/{p['slug']}.html</loc><lastmod>{p.get("lastmod",p.get("published",DATE))}</lastmod></url>" for p in P)
sm=re.sub(r"  <url><loc>[^<]*/tips/[^<]+\.html</loc>.*\n","",sm)
sm=re.sub(r"  <!-- Add each.*?-->",urls+"\n  <!-- Add each published issue: <url><loc>https://aiparentingtips.com/tips/SLUG.html</loc><lastmod>YYYY-MM-DD</lastmod></url> -->",sm)
open(f"{ROOT}/sitemap.xml","w").write(sm)
for p in P: print(p["slug"],len(p["title"]+" | AI Parenting Tips"),len(p["desc"]))
