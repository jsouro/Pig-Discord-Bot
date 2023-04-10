import discord
import requests
import random
import praw
from keep_alive import keep_alive
keep_alive()
intents = discord.Intents.default()
intents.message_content = True
pigJokes = ["Did you hear about the piglets who wanted to do something special for Mother’s Day? They threw a sowprize party.", "What do you call a laundromat for pigs? Hogwash.", "I saw a pig with laryngitis. He was disgruntled.", "What do you call a pig thief? A hamburglar.", "Why should you never rob a bank with a pig? They always squeal.", "How do pigs get to the hospital? In ham-bulances.", "How do pigs write top-secret messages? With invisible oink!", "Why do pigs make awful football players? They don’t like playing with the ‘pig skin.’", "Why are pigs awful basketball players? They hog the ball.", "What do you get when you cross a pig and a cactus? A porky-pine.", "Why did the piglet yell at his sibling at the dinner table? She was hogging the food.", "Walking through the farm and a group of pigs jumped out of a tree on me. It was a hambush.", "What do you call a Spanish pig? Porque.", "What kind of work do pigs do after school? Hamwork.","What do you get when you cross a pig with a centipede? Bacon and Legs.", "What’s it called when a bunch of pigs compete in athletic games? The Olympigs", "Why did the pig go to the casino? To play the slop machine!", "What do you give a sick pig? Oinkment.", "What do you call a pig who does karate? A pork chop.", "What did Papa Pig shout at his kids in the car? ‘Stop swining! We’re nearly there.’", "How does a young pig hit on someone? They invite them over to Netflix and swill.", "What does an obstinate piglet always say to his mama. ‘Sow what?’", "What did one pig say to the other? Let’s be pen pals.", "What do you get if you cross a dinosaur with a pig? Jurassic Pork.", "Did you hear about the pig who opened a pawn shop? He called it ‘Ham Hocks’", "A local farmer has trained his pigs to perform ballet. I’m going to see their production of swine lake.", "Why was the piglet whining. He was boared out of his brains.", "What do you call a pig that does a lot of charity work? Philanthropig.", "What did the pig say on the warm summer’s day? ‘I’m bacon.’", "I read a story about pig anatomy. It was all straightforward until I found a twist in the tale.", "What happened when the pig pen broke? They had to use the pig pencil.", "What do you call a pig that plays basketball? A ball hog.", "What do you give a pig with an itch? Oinkment.", "What do you call a pig with no legs? A groundhog.", "Why did the pig break up with her boyfriend? Because he was a boar.", "What do you get when you cross a pig and a tortoise? A slow-pork.", "What happens when you play tug-of-war with a pug? Pulled pork!", "Why was the pig given a red card at the football game? For playing dirty.", "A pig just won the lottery. What do you call him? Filthy rich.", "What did the little piglet want from the swine? A piggyback ride home.", "What do you call a pig that gets the test answer wrong? Mistaken bacon.", "Where do flying pigs go? Hogwarts, of course!", "What do you call a pig that drives around recklessly? A road hog.", "What is the most common Halloween outfit for a pig to dress up as? Frankenswine.", "What did the pig exclaim when the wolf grabbed its tail? ‘That’s the end of me!’", "How do pigs greet their family and friends? With hogs and kisses.", "What do pigs do on the evening of February 14th? They have a valenswines dinner.", "What do you call a pig with three eyes? A piiig!", "What do you get when you cross a pig and superman? The Man of Squeal.", "What do you call a pig who can’t mind his own business? A nosey porker!", "Knock, knock! Who’s there? Pig… Pig who? Pig on someone your own size!", "What do you call a guinea pig that has become a member of the mafia? A hamster", "In the 5th month of every year, my aunt lets her pigs in the field… It’s mayham!", "Did you hear about the pig that ran the Post Office? He was the first Porkmaster General.", "How do pigs get to the hospital? A hambulance.", "What do you call it when a beautiful woman tries to trick you into giving her a pig? A bae con.", "What do you get when you pick a pig’s nose? Ham boogers.", "Did you hear the horse and the pig are dating? They’re in a stable relationship.", "What kind of ice cream do pigs like best? Hoggin Daz!", "What do you have left after a pig eats a watermelon? Pork rinds.", "Why did it take the teen pig so long to get ready for school in the morning? She was very piggy when it comes to choosing what to wear!", "What did the introverted pig say when asked why they don’t like socializing? ‘I’m not a people porcine.’", "What advice did the grandpa pig have for his kids? ‘Don’t take anything for grunted.’"]

pigJokes = pigJokes.copy()
client = discord.Client(intents=intents)
reddit = praw.Reddit(
    client_id='CLIENT_ID',
    client_secret='CLIENT_SECRET',
    username='REDDIT_USERNAME',
    password='REDDIT_PASS',
    user_agent='Oink!'
)
def getImgUrl(term):
    load_dotenv()
    key = "YOUR_GOOGLE_TOKEN"
    _url = "https://www.googleapis.com/customsearch/v1"
    offset = random.randint(1,50)
    _params = {'key':key,'q':term,'num':'1','start':offset,'searchType':"image",'cx':"4426fb15ed7f0c118"}
    r = requests.get(url=_url, params=_params)
    data = r.json()
    imgLink = data['items'][0]['link']
    return imgLink

piggie = "pig"

@client.event
async def on_message(message):
    print('hi')
    if message.content.startswith('!subreddit'):
        subreddit_name = message.content.split()[1]
        subreddit = reddit.subreddit(subreddit_name)      
        recent_post = None
        for post in subreddit.new():
            if post.url.endswith(('.jpg', '.jpeg', '.png', '.gif', '.mp4', '.gifv')):
                recent_post = post
                break
        
        if recent_post:
            response = f"Oink, here's the recent post from r/{subreddit_name}, Oink! : {recent_post.url}\nOink: {recent_post.shortlink}"
            await message.channel.send(response)
          
        else:
            await message.channel.send('Oink, I was unable to find anything, Oink!')   
    elif "!joke" in message.content:
        await message.channel.send(random.choice(pigJokes))
    elif message.content.startswith('pig'):
         embedImage = discord.Embed()
         pigUrl = getImgUrl(piggie)
         embedImage.set_image(url=pigUrl)
         await message.channel.send(embed=embedImage)
        
        
client.run("YOUR_DISCORD_BOT_TOKEN")
