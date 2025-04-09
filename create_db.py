import sqlite3

conn = sqlite3.connect('songs.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    artist TEXT NOT NULL,
    genre TEXT NOT NULL,
    lyrics TEXT NOT NULL
)
''')

songs = [
    ("Shape of You", "Ed Sheeran", "pop", """The club isn't the best place to find a lover
So the bar is where I go (mmmm)
Me and my friends at the table doing shots
Drinking fast and then we talk slow (mmmm)
And you come over and start up a conversation with just me
And trust me I'll give it a chance now (mmmm)
Take my hand, stop, put Van The Man on the jukebox
And then we start to dance
And now I'm singing like

Girl, you know I want your love
Your love was handmade for somebody like me
Come on now, follow my lead
I may be crazy, don't mind me
Say, boy, let's not talk too much
Grab on my waist and put that body on me
Come on now, follow my lead
Come, come on now, follow my lead (mmmm)

I'm in love with the shape of you
We push and pull like a magnet do
Although my heart is falling too
I'm in love with your body
Last night you were in my room
And now my bedsheets smell like you
Every day discovering something brand new
I'm in love with your body

Oh I oh I oh I oh I
I'm in love with your body
Oh I oh I oh I oh I
I'm in love with your body
Oh I oh I oh I oh I
I'm in love with your body
Every day discovering something brand new
I'm in love with the shape of you

One week in we let the story begin
We're going out on our first date (mmmm)
You and me are thrifty, so go all you can eat
Fill up your bag and I fill up a plate (mmmm)
We talk for hours and hours about the sweet and the sour
And how your family is doing okay (mmmm)
And leave and get in a taxi, then kiss in the backseat
Tell the driver make the radio play
And I'm singing like

Girl, you know I want your love
Your love was handmade for somebody like me
Come on now, follow my lead
I may be crazy, don't mind me
Say, boy, let's not talk too much
Grab on my waist and put that body on me
Come on now, follow my lead
Come, come on now, follow my lead (mmmm)

I'm in love with the shape of you
We push and pull like a magnet do
Although my heart is falling too
I'm in love with your body
Last night you were in my room
And now my bedsheets smell like you
Every day discovering something brand new
I'm in love with your body

Oh I oh I oh I oh I
I'm in love with your body
Oh I oh I oh I oh I
I'm in love with your body
Oh I oh I oh I oh I
I'm in love with your body
Every day discovering something brand new
I'm in love with the shape of you

Come on, be my baby, come on
Come on, be my baby, come on
Come on, be my baby, come on
Come on, be my baby, come on
Come on, be my baby, come on
Come on, be my baby, come on
Come on, be my baby, come on
Come on, be my baby, come on

I'm in love with the shape of you
We push and pull like a magnet do
Although my heart is falling too
I'm in love with your body
Last night you were in my room
And now my bedsheets smell like you
Every day discovering something brand new
I'm in love with your body

Come on, be my baby, come on
Come on, be my baby, come on
I'm in love with your body
Come on, be my baby, come on
Come on, be my baby, come on
I'm in love with your body
Come on, be my baby, come on
Come on, be my baby, come on
I'm in love with your body
Every day discovering something brand new
I'm in love with the shape of you"""),
    ("Bohemian Rhapsody", "Queen", "rock", """Is this the real life?
Is this just fantasy?
Caught in a landslide
No escape from reality

Open your eyes
Look up to the skies and see
I'm just a poor boy, I need no sympathy
Because I'm easy come, easy go
Little high, little low
Any way the wind blows
Doesn't really matter to me, to me

Mama, just killed a man
Put a gun against his head
Pulled my trigger, now he's dead
Mama, life had just begun
But now I've gone and thrown it all away

Mama, ooh
Didn't mean to make you cry
If I'm not back again this time tomorrow
Carry on, carry on as if nothing really matters

Too late, my time has come
Sends shivers down my spine
Body's aching all the time
Goodbye, everybody, I've got to go
Gotta leave you all behind and face the truth

Mama, ooh (Any way the wind blows)
I don't wanna die
I sometimes wish I'd never been born at all

I see a little silhouetto of a man
Scaramouche, Scaramouche, will you do the Fandango?
Thunderbolt and lightning very, very frightening me
(Galileo) Galileo
(Galileo) Galileo
Galileo Figaro
Magnifico-o-o-o-o

I'm just a poor boy, nobody loves me
He's just a poor boy from a poor family
Spare him his life from this monstrosity

Easy come, easy go, will you let me go?
Bismillah! No, we will not let you go (Let him go!)
Bismillah! We will not let you go (Let him go!)
Bismillah! We will not let you go (Let me go!)
Will not let you go (Let me go!)
Never let you go (Never, never, never, never let me go)
Oh oh oh oh
No, no, no, no, no, no, no
Oh, mamma mia, mamma mia (Mamma mia, let me go)
Beelzebub has a devil put aside for me, for me, for me

So you think you can stone me and spit in my eye?
So you think you can love me and leave me to die?
Oh, baby, can't do this to me, baby
Just gotta get out, just gotta get right outta here

Ooh, ooh yeah, ooh yeah

Nothing really matters
Anyone can see
Nothing really matters
Nothing really matters to me

Any way the wind blows"""),
("Blinding Lights", "The Weeknd", "pop", """Yeah

I've been tryna call
I've been on my own for long enough
Maybe you can show me how to love, maybe
I'm going through withdrawals
You don't even have to do too much
You can turn me on with just a touch, baby

I look around and
Sin City's cold and empty (Oh)
No one's around to judge me (Oh)
I can't see clearly when you're gone

I said, ooh, I'm blinded by the lights
No, I can't sleep until I feel your touch
I said, ooh, I'm drowning in the night
Oh, when I'm like this, you're the one I trust
Hey, hey, hey

I'm running out of time
'Cause I can see the sun light up the sky
So I hit the road in overdrive, baby, oh

The city's cold and empty (Oh)
No one's around to judge me (Oh)
I can't see clearly when you're gone

I said, ooh, I'm blinded by the lights
No, I can't sleep until I feel your touch
I said, ooh, I'm drowning in the night
Oh, when I'm like this, you're the one I trust

I'm just calling back to let you know (Back to let you know)
I could never say it on the phone (Say it on the phone)
Will never let you go this time (Ooh)

I said, ooh, I'm blinded by the lights
No, I can't sleep until I feel your touch
Hey, hey, hey
Hey, hey, hey

I said, ooh, I'm blinded by the lights
No, I can't sleep until I feel your touch"""),
("Rolling In The Deep", "Adele", "pop", """There's a fire starting in my heart
Reaching a fever pitch, it's bringing me out the dark
Finally I can see you crystal clear
[Clean version:] Go 'head and sell me out and I'll lay your ship bare
[Explicit version:] Go 'head and sell me out and I'll lay your shit bare
See how I leave with every piece of you
Don't underestimate the things that I will do

There's a fire starting in my heart
Reaching a fever pitch
And it's bringing me out the dark

The scars of your love remind me of us
They keep me thinking that we almost had it all
The scars of your love, they leave me breathless
I can't help feeling
We could have had it all
(You're gonna wish you never had met me)
Rolling in the deep
(Tears are gonna fall, rolling in the deep)
You had my heart inside of your hand
(You're gonna wish you never had met me)
And you played it, to the beat
(Tears are gonna fall, rolling in the deep)

Baby, I have no story to be told
But I've heard one on you
And I'm gonna make your head burn
Think of me in the depths of your despair
Make a home down there
As mine sure won't be shared

(You're gonna wish you never had met me)
The scars of your love remind me of us
(Tears are gonna fall, rolling in the deep)
They keep me thinking that we almost had it all
(You're gonna wish you never had met me)
The scars of your love, they leave me breathless
(Tears are gonna fall, rolling in the deep)
I can't help feeling
We could have had it all
(You're gonna wish you never had met me)
Rolling in the deep
(Tears are gonna fall, rolling in the deep)
You had my heart inside of your hand
(You're gonna wish you never had met me)
And you played it, to the beat
(Tears are gonna fall, rolling in the deep)
We could have had it all
Rolling in the deep
You had my heart inside of your hand
But you played it, with a beating

Throw your soul through every open door (woah)
Count your blessings to find what you look for (woah)
Turn my sorrow into treasured gold (woah)
You'll pay me back in kind and reap just what you sow (woah)
(You're gonna wish you never had met me)
We could have had it all
(Tears are gonna fall, rolling in the deep)
We could have had it all
(You're gonna wish you never had met me)
It all, it all, it all
(Tears are gonna fall, rolling in the deep)

We could have had it all
(You're gonna wish you never had met me)
Rolling in the deep
(Tears are gonna fall, rolling in the deep)
You had my heart inside of your hand
(You're gonna wish you never had met me)
And you played it to the beat
(Tears are gonna fall, rolling in the deep)

We could have had it all
(You're gonna wish you never had met me)
Rolling in the deep
(Tears are gonna fall, rolling in the deep)
You had my heart inside of your hand
(You're gonna wish you never had met me)

But you played it
You played it
You played it
You played it to the beat."""),
("Umbrella", "Rihanna", "pop", """Uh-huh, uh-huh (Yeah, Rihanna)
Uh-huh, uh-huh (Good Girl Gone Bad)
Uh-huh, uh-huh (Take three, action)
Uh-huh, uh-huh (Hov)

No clouds in my stones
Let it rain, I hydroplane in the bank
Coming down with the Dow Jones
When the clouds come, we gone, we Roc-A-Fella
We fly higher than weather, in G5's or better
You know me (You know me)
In anticipation for precipitation, stack chips for the rainy day
Jay—Rain Man is back
With Little Miss Sunshine, Rihanna, where you at?

You have my heart
And we'll never be worlds apart
Maybe in magazines
But you'll still be my star
Baby, 'cause in the dark
You can't see shiny cars
And that's when you need me there
With you, I'll always share
Because

When the sun shine, we shine together
Told you I'll be here forever
Said I'll always be your friend
Took an oath, I'ma stick it out to the end
Now that it's raining more than ever
Know that we'll still have each other
You can stand under my umbrella
You can stand under my umbrella—ella—ella, eh, eh, eh
Under my umbrella—ella—ella, eh, eh, eh
Under my umbrella—ella—ella, eh, eh, eh
Under my umbrella—ella—ella, eh, eh, eh, eh, eh-eh

These fancy things
Will never come in between
You're part of my entity
Here for infinity
When the war has took its part
When the world has dealt its cards
If the hand is hard
Together we'll mend your heart
Because

When the sun shine, we shine together
Told you I'll be here forever
Said I'll always be your friend
Took an oath, I'ma stick it out to the end
Now that it's raining more than ever
Know that we'll still have each other
You can stand under my umbrella
You can stand under my umbrella—ella—ella, eh, eh, eh
Under my umbrella—ella—ella, eh, eh, eh
Under my umbrella—ella—ella, eh, eh, eh
Under my umbrella—ella—ella, eh, eh, eh, eh, eh-eh

You can run into my arms
It's okay, don't be alarmed
Come into me
There's no distance in between our love
So gon' and let the rain pour
I'll be all you need and more
Because

When the sun shine, we shine together
Told you I'll be here forever
Said I'll always be your friend
Took an oath, I'ma stick it out to the end
Now that it's raining more than ever
Know that we'll still have each other
You can stand under my umbrella
You can stand under my umbrella—ella—ella, eh, eh, eh
Under my umbrella—ella—ella, eh, eh, eh
Under my umbrella—ella—ella, eh, eh, eh
Under my umbrella—ella—ella, eh, eh, eh, eh, eh-eh

It's raining, raining
Ooh, baby, it's raining, raining
Baby, come here to me
Come into me
It's raining, raining
Ooh, baby, it's raining, raining
You can always come into me
Come into me
It's pouring rain
It's pouring rain
Come here to me
Come into me
It's pouring rain
It's pouring rain"""),
("Bad Romance", "Lady Gaga", "pop", """lyricsOh-oh-oh-oh-oh, oh-oh-oh-oh, oh-oh-oh
Caught in a bad romance
Oh-oh-oh-oh-oh, oh-oh-oh-oh, oh-oh-oh
Caught in a bad romance
Ra-ra-ah-ah-ah
Roma Roma-ma
Gaga, "Ooh la-la"
Want your bad romance
Ra-ra-ah-ah-ah
Roma, Roma-ma
Gaga, "Ooh la-la"
Want your bad romance

I want your ugly, I want your disease
I want your everything as long as it's free
I want your love
Love, love, love, I want your love, oh, ey
I want your drama, the touch of your hand (Hey!)
I want your leather-studded kiss in the sand
I want your love
Love, love, love, I want your love
(Love, love, love, I want your love)

You know that I want you
And you know that I need you
I want it bad
Your bad romance

I want your love, and I want your revenge
You and me could write a bad romance (Oh-oh-oh-oh-oh)
I want your love, and all your lover's revenge
You and me could write a bad romance
Oh-oh-oh-oh-oh, oh-oh-oh-oh, oh-oh-oh
Caught in a bad romance
Oh-oh-oh-oh-oh, oh-oh-oh-oh, oh-oh-oh
Caught in a bad romance

Ra-ra-ah-ah-ah
Roma-roma-ma
Gaga, "Ooh la-la"
Want your bad romance

I want your horror, I want your design
'Cause you're a criminal as long as you're mine
I want your love
Love, love, love, I want your love, uh
I want your psycho, your vertigo schtick (Schtick, hey!)
Want you in my rear window, baby, you're sick
I want your love
Love, love, love, I want your love
(Love, love, love, I want your love)

You know that I want you
And you know that I need you ('Cause I'm a free bitch, baby)
I want it bad
Your bad romance

I want your love, and I want your revenge
You and me could write a bad romance (Oh-oh-oh-oh-oh)
I want your love, and all your lover's revenge
You and me could write a bad romance
Oh-oh-oh-oh-oh, oh-oh-oh-oh, oh-oh-oh
Caught in a bad romance
Oh-oh-oh-oh-oh, oh-oh-oh-oh, oh-oh-oh
Caught in a bad romance

Ra-ra-ah-ah-ah
Roma-roma-ma
Gaga, "Ooh la-la"
Want your bad romance
Ra-ra-ah-ah-ah
Roma-roma-ma
Gaga, "Ooh la-la"
Want your bad romance

Walk, walk, fashion, baby
Work it, move that bitch crazy
Walk, walk, fashion, baby
Work it, move that bitch crazy
Walk, walk, fashion, baby
Work it, move that bitch crazy
Walk, walk, passion, baby
Work it, I'm a free bitch, baby

I want your love, and I want your revenge
I want your love, I don't wanna be friends
Je veux ton amour et je veux ta revanche
Je veux ton amour, I don't wanna be friends
(Oh-oh-oh-oh-oh, oh-oh-oh-oh, oh-oh-oh)
(I want you back) No, I don't wanna be friends
(Caught in a bad romance) I don't wanna be friends
Want your bad romance
(Caught in a bad romance) Want your bad romance

I want your love, and I want your revenge
You and me could write a bad romance (Oh-oh-oh-oh-oh)
I want your love, and all your lover's revenge
You and me could write a bad romance
Oh-oh-oh-oh-oh, oh-oh-oh-oh, oh-oh-oh
(Want your bad romance)
Caught in a bad romance (Want your bad romance)
Oh-oh-oh-oh-oh, oh-oh-oh-oh, oh-oh-oh
(Want your bad romance)
Caught in a bad romance

Ra-ra-ah-ah-ah
Roma, Roma-ma
Gaga, "Ooh la-la"
Want your bad romance"""),
("Criminal", "Britney Spears", "pop", """He is a hustler, he's no good at all
He is a loser, he's a bum, bum, bum, bum
He lies, he bluffs, he's unreliable
He is a sucker with a gun, gun, gun, gun
I know you told me I should stay away
I know you said he's just a dog astray
He's a bad boy with a tainted heart
And even I know this ain't smart

But mama, I'm in love with a criminal
And this type of love isn't rational, it's physical
Mama, please don't cry, I will be alright
All reason aside, I just can't deny, love the guy

He is a villain by the devil's law
He is a killer just for fun, fun, fun, fun
The man's a snitch and unpredictable
He's got no conscience, he got none, none, none, none
Oh, I know, should've let go, but no
'Cause he's a bad boy with a tainted heart
And even I know this ain't smart

But mama, I'm in love with a criminal
And this type of love isn't rational, it's physical
Mama, please don't cry, I will be alright
All reason aside, I just can't deny, love the guy

And he's got my name
Tattooed on his arm, his lucky charm
So I guess it's OK, he's with me
And I hear people talk (People talk)
Try to make remarks, keep us apart
But I don't even hear, I don't care

'Cause mama, I'm in love with a criminal
And this type of love isn't rational, it's physical
Mama, please don't cry, I will be alright
All reason aside, I just can't deny, love the guy

(Oh, I know, oh) Mama I'm in love with a criminal
(Should've let go) And this type of love isn't rational
(But no) It's physical
(Oh, I know, oh) Mama, please don't cry, I will be alright
(Should've let go) All reason aside
(But no) I just can't deny, love the guy"""),
("Drivers License", "Olivia Rodrigo", "pop", """I got my driver's license last week
Just like we always talked about
'Cause you were so excited for me
To finally drive up to your house
But today I drove through the suburbs
Crying 'cause you weren't around

And you're probably with that blonde girl
Who always made me doubt
She's so much older than me
She's everything I'm insecure about
Yeah, today I drove through the suburbs
'Cause how could I ever love someone else?

And I know we weren't perfect but I've never felt this way for no one
And I just can't imagine how you could be so okay now that I'm gone
Guess you didn't mean what you wrote in that song about me
'Cause you said forever now I drive alone past your street

And all my friends are tired
Of hearing how much I miss you but
I kinda feel sorry for them
'Cause they'll never know you the way that I do
Yeah, today I drove through the suburbs
And pictured I was driving home to you

And I know we weren't perfect but I've never felt this way for no one
Oh, and I just can't imagine how you could be so okay now that I'm gone
I guess you didn't mean what you wrote in that song about me
'Cause you said forever now I drive alone past your street

Red lights
Stop signs
I still see your face
In the white cars
Front yards
Can't drive past the places
We used to
Go to
'Cause I still fucking love you, babe

Sidewalks
We crossed
I still hear your voice
In the traffic
We're laughing
Over all the noise
God, I'm so blue
Know we're through
But I still fucking love you, babe

I know we weren't perfect but I've never felt this way for no one
And I just can't imagine how you could be so okay now that I'm gone
Guess you didn't mean what you wrote in that song about me
'Cause you said forever now I drive alone past your street
Yeah, you said forever now I drive alone past your street"""),
("Get Lucky", "Daft Punk", "pop", """Like the legend of the Phoenix
All ends with beginnings
What keeps the planets spinning (uh)
The force from the beginning

(Look)

We've come too far to give up who we are
So let's raise the bar and our cups to the stars

She's up all night to the sun
I'm up all night to get some
She's up all night for good fun
I'm up all night to get lucky

We're up all night to the sun
We're up all night to get some
We're up all night for good fun
We're up all night to get lucky

We're up all night to get lucky
We're up all night to get lucky
We're up all night to get lucky
We're up all night to get lucky

The present has no ribbon
Your gift keeps on giving,
What is this I'm feeling?
If you wanna leave I'm with it (ah)

We've come too far to give up who we are
So let's raise the bar and our cups to the stars

She's up all night to the sun
I'm up all night to get some
She's up all night for good fun
I'm up all night to get lucky

We're up all night to the sun
We're up all night to get some
We're up all night for good fun
We're up all night to get lucky

We're up all night to get lucky
We're up all night to get lucky
We're up all night to get lucky
We're up all night to get lucky

(We're up all night to get
We're up all night to get
We're up all night to get
We're up all night to get)

(We're up all night to get (together)
We're up all night to get (let's get funked again)
We're up all night to get lucky
We're up all night to get lucky)

(We're up all night to get lucky
We're up all night to get lucky
We're up all night to get lucky
We're up all night to get lucky)

(We're up all night to get lucky
We're up all night to get lucky
We're up all night to get lucky
We're up all night to get lucky)

We've (we're up all night to get lucky)
Come too far (we're up all night to get lucky)
To give up (we're up all night to get lucky)
Who we are (we're up all night to get lucky)
So let's (we're up all night to get lucky)
Raise the bar (we're up all night to get lucky)
And our cups (we're up all night to get lucky)
To the stars (we're up all night to get lucky)

She's up all night to the sun
I'm up all night to get some
She's up all night for good fun
I'm up all night to get lucky

We're up all night to the sun
We're up all night to get some
We're up all night for good fun
We're up all night to get lucky

We're up all night to get lucky
We're up all night to get lucky
We're up all night to get lucky
We're up all night to get lucky

We're up all night to get lucky
We're up all night to get lucky
We're up all night to get lucky
We're up all night to get lucky"""),
("Dark Horse", "Katy Perry", "pop", """Oh, no

[Juicy J:]
Yeah
Ya'll know what it is
Katy Perry
Juicy J, aha
Let's rage

[Katy Perry:]
I knew you were
You were gonna come to me
And here you are
But you better choose carefully
'Cause I, I'm capable of anything
Of anything and everything

Make me your Aphrodite
Make me your one and only
But don't make me your enemy, your enemy, your enemy

So you wanna play with magic?
Boy, you should know what you're falling for
Baby, do you dare to do this?
'Cause I'm coming at you like a dark horse

Are you ready for, ready for
A perfect storm, perfect storm?
'Cause once you're mine, once you're mine
There is no going back

Mark my words
This love will make you levitate
Like a bird
Like a bird without a cage
But down to earth
If you choose to walk away, don't walk away

It's in the palm of your hand now, baby
It's a "yes" or "no", no "maybe"
So just be sure before you give it all to me
All to me, give it all to me

So you wanna play with magic?
Boy, you should know what you're falling for
Baby, do you dare to do this?
'Cause I'm coming at you like a dark horse

Are you ready for, ready for
A perfect storm, perfect storm?
'Cause once you're mine, once you're mine (love trippin')
There's no going back

[Juicy J:]
Uh
She's a beast
I call her "Karma" (come back)
She eats your heart out
Like Jeffrey Dahmer (woo)
Be careful
Try not to lead her on
Shorty's heart is on steroids
'Cause her love is so strong

You may fall in love
When you meet her
If you get the chance you better keep her
She's sweet as pie but if you break her heart
She'll turn cold as a freezer
That fairy-tale ending with a knight in shining armor
She can be my Sleeping Beauty
I'm gon' put her in a coma
Woo!

Damn I think I love her
Shorty so bad, I'm sprung and I don't care
She ride me like a roller-coaster
Turned the bedroom into a fair (a fair!)
Her love is like a drug
I was tryna hit it and quit it
But lil' mama so dope
I messed around and got addicted

[Katy Perry:]
So you wanna play with magic?
Boy, you should know what you're falling for (you should know)
Baby, do you dare to do this?
'Cause I'm coming at you like a dark horse (like a dark horse)

Are you ready for, ready for (ready for)
A perfect storm, perfect storm (a perfect storm)?
'Cause once you're mine, once you're mine (mine)
There's no going back"""),
("Titanium", "Sia", "pop", """You shout it out, but I can't hear a word you say
I'm talking loud, not saying much
I'm criticized, but all your bullets ricochet
Shoot me down, but I get up

I'm bulletproof, nothing to lose
Fire away, fire away
Ricochet, you take your aim
Fire away, fire away

You shoot me down, but I won't fall
I am titanium
You shoot me down, but I won't fall
I am titanium

Cut me down, but it's you who'll have further to fall
Ghost town and haunted love
Raise your voice, sticks and stones may break my bones
I'm talking loud, not saying much

I'm bulletproof, nothing to lose
Fire away, fire away
Ricochet, you take your aim
Fire away, fire away

You shoot me down, but I won't fall
I am titanium
You shoot me down, but I won't fall
I am titanium
I am titanium
I am titanium

Stone hard, machine gun
Firing at the ones who run
Stone hard, as bulletproof glass

You shoot me down, but I won't fall
I am titanium
You shoot me down, but I won't fall
I am titanium
You shoot me down, but I won't fall
I am titanium
You shoot me down, but I won't fall
I am titanium
I am titanium"""),
("Price Tag", "Jessie J", "pop", """[Jessie J:]
Okay, Coconut Man, Moonhead and Pea
You ready?

Seems like everybody's got a price
I wonder how they sleep at night
When the sale comes first and the truth comes second
Just stop for a minute and smile
Why is everybody so serious?
Acting so damn mysterious?
Got your shades on your eyes
And your heels so high that you can't even have a good time

Everybody look to their left
Everybody look to their right
Can you feel that? Yeah
We're paying with love tonight

It's not about the money, money, money
We don't need your money, money, money
We just wanna make the world dance
Forget about the price tag
Ain't about the, uh, cha-ching, cha-ching
Ain't about the, yeah, ba-bling, ba-bling
Wanna make the world dance
Forget about the price tag

Okay
We need to take it back in time
When music made us all unite
And it wasn't low blows and video hoes
Am I the only one getting tired?
Why is everybody so obsessed?
Money can't buy us happiness
Can we all slow down and enjoy right now?
Guarantee we'll be feeling alright

Everybody look to their left (To their left)
Everybody look to their right (To their right)
Can you feel that? Yeah
We're paying with love tonight

It's not about the money, money, money
We don't need your money, money, money
We just wanna make the world dance
Forget about the price tag
Ain't about the, uh, cha-ching, cha-ching
Ain't about the, yeah, ba-bling, ba-bling
Wanna make the world dance
Forget about the price tag

[B.o.B:]
Yeah, yeah, well, keep the price tag and take the cash back
Just give me six strings (Six strings) and a half-stack (Half-stack)
And you can, can keep the cars, leave me the garage
And all I, yes, all I need are keys and guitars
And guess what? In thirty seconds, I'm leaving to Mars
Yeah, we leaping across these undefeatable odds
It's like this, man, you can't put a price on a life
We do this for the love, so we fight and sacrifice every night
So we ain't gon' stumble and fall, never
Waiting to see this in the sign of defeat, uh-uh
So we gon' keep everyone moving their feet
So bring back the beat and then everyone sing
It's not about the money

[Jessie J (B.o.B):]
It's not about the money, money, money
We don't need your money, money, money
We just wanna make the world dance
Forget about the price tag
Ain't about the, uh, cha-ching, cha-ching
Ain't about the, yeah, ba-bling, ba-bling
Wanna make the world dance
Forget about the price tag (Hey! Hey!)
It's not about the money, money, money (We don't need it)
We don't need your money, money, money (No, I don't, we don't need it)
We just wanna make the world dance (Dance, dance your ass off)
Forget about the price tag (Ah, ah)
Ain't about the, yea-yeah!, cha-ching, cha-ching
Ain't about the, woo!, ba-bling, ba-bling (It ain't about)
Wanna make the world dance (Yeah, yeah)
Forget about the price tag

[Jessie J:]
Ahh, ahh, ahh, ahh
Yeah, yeah, ahh, ooh-ooh, ahh
Forget about the price tag, heh"""),
("People You Know", "Selena Gomez", "pop", """You were running through me like water
Now the feeling's leaving me dry
These days we couldn't be farther
So how's it feel to be on the other side?

So many wasted nights with you
I still can taste it, I hate it
Wish I could take it back, 'cause

We used to be close, but people can go
From people you know to people you don't
And what hurts the most is people can go
From people you know to people you don't

We used to be close, but people can go
From people you know to people you don't
And what hurts the most is people can go
From people you know to people you don't

When it was good, we were on fire
Now I'm breathing ashes and dust
I always wanna get higher
I never know when enough is enough

So many wasted nights with you
I still can taste it, I hate it
Wish I could take it back, 'cause

We used to be close, but people can go
From people you know to people you don't
And what hurts the most is people can go
From people you know to people you don't

We used to be close, but people can go
From people you know to people you don't
And what hurts the most is people can go
From people you know to people you don't

(People you don't)
(People you don't)
From people you know to people you don't
From people you know to people you don't

We used to be close, but people can go
From people you know to people you don't
And what hurts the most is people can go
From people you know to people you don't

We used to be close, but people can go
From people you know to people you don't
And what hurts the most is people can go
From people you know to people you don't

From people you know to people you don't
From people you know to people you don't
From people you know to people you don't
From people you know to people you don't"""),
("Positions", "Ariana Grande", "pop", """Heaven sent you to me
I'm just hoping I don't repeat history

Boy I'm tryna meet your mama
On a Sunday
Then make a lotta love
On a Monday (Ah, ah)
Never need no (No)
No one else, babe
'Cause I'll be

Switchin' the positions for you
Cooking in the kitchen and I'm in the bedroom
I'm in the Olympics way I'm jumping through hoops
Know my love infinite nothing I wouldn't do
That I won't do, switching for you

Perfect, perfect
You're too good to be true (You're too good to be true)
But I get tired of running
Fuck it, now I'm running with you (with you)

Said boy I'm tryna meet your mama
On a Sunday
Then make a lotta love
On a Monday (Ah, ah)
Never need no (No)
No one else babe
'Cause I'll be

Switchin' the positions for you
Cooking in the kitchen and I'm in the bedroom
I'm in the Olympics way I'm jumping through hoops
Know my love infinite nothing I wouldn't do
That I won't do, switching for you
Cooking in the kitchen and I'm in the bedroom
I'm in the Olympics way I'm jumping through hoops
Know my love infinite nothing I wouldn't do (nothing)
That I won't do, switching for you

This some shit that I
Usually don't do (Yeah)
But for you I kinda
Kinda want to
'Cause you're down for me
And I'm down too
(And I'm down too)
Yeah I'm down too
Switchin' the positions for you

This some shit that I (Yeah)
Usually don't do (Don't do)
But for you I kinda
Kinda want to
'Cause you're down for me
And I'm down too
('Cause you're down for me)

Switchin' the positions for you
Cooking in the kitchen and I'm in the bedroom
I'm in the Olympics way I'm jumping through hoops (Jumping, jumping)
Know my love infinite nothing I wouldn't do
That I won't do, switching for you (Ooh whoa)
Cooking in the kitchen and I'm in the bedroom
I'm in the Olympics way I'm jumping through hoops
Know my love infinite nothing I wouldn't do (I wouldn't do)
That I won't do, switching for you"""),
("Locked Out Of Heaven", "Bruno Mars", "pop", """One, two, one, two, three

Oh, yeah, yeah,
Oh, yeah, yeah, yeah, yeah,
Ooh!
Oh, yeah, yeah,
Oh, yeah, yeah, yeah, yeah,
Ooh!

Never had much faith in love or miracles
Ooh!
Never wanna put my heart on the line
Ooh!
But swimming in your water is something spiritual
Ooh!
I'm born again every time you spend the night
Ooh!

'Cause your sex takes me to paradise
Yeah, your sex takes me to paradise
And it shows, yeah, yeah, yeah

'Cause you make me feel like I've been locked out of heaven
For too long, for too long
Yeah, you make me feel like I've been locked out of heaven
For too long, for too long

Oh, yeah, yeah, yeah, yeah,
Ooh!
Oh, yeah, yeah,
Oh, yeah, yeah, yeah, yeah,
Ooh!

You bring me to my knees, you make me testify
You can make a sinner change his ways
Open up your gates 'cause I can't wait to see the light
And right there is where I wanna stay

'Cause your sex takes me to paradise
Yeah, your sex takes me to paradise
And it shows, yeah, yeah, yeah

'Cause you make me feel like I've been locked out of heaven
For too long, for too long
Yeah, you make me feel like I've been locked out of heaven
For too long, for too long

Oh, oh, oh, oh, yeah, yeah, yeah
Can I just stay here?
Spend the rest of my days here?
Oh, oh, oh, oh, yeah, yeah, yeah
Can I just stay here?
Spend the rest of my days here?

'Cause you make me feel like I've been locked out of heaven
For too long, for too long
Yeah, you make me feel like I've been locked out of heaven
For too long, for too long

Oh, yeah, yeah, yeah, yeah,
Ooh!
Oh, yeah, yeah,
Oh, yeah, yeah, yeah, yeah,
Ooh!"""),
("The Way I Are", "Timbaland", "pop", """Remember the time baby

[Timbaland:]
I ain't got no money
I ain't got no car to take you on a date
I can't even buy you flowers
But together we can be the perfect soul mates
Talk to me girl

[Keri Hilson:]
Oh, baby, it's alright now, you ain't gotta flaunt for me
If we go Dutch, you can still touch my love, it's free
We can work without the perks just you and me
Thug it out 'til we get it right

[Keri Hilson (Timbaland):]
Baby if you strip, you can get a tip
'Cause I like you just the way you are
(I'm about to strip and I'm well equipped
Can you handle me the way I are?)
I don't need the Gs or the car keys
Boy I like you just the way you are
Let me see you strip, you can get a tip
'Cause I like, I like, I like

[Timbaland:]
I ain't got no Visa
I ain't got no Red American Express
We can't go nowhere exotic
It don't matter 'cause I'm the one that loves you best
Talk to me girl

[Keri Hilson:]
Oh, baby, it's alright now, you ain't gotta flaunt for me
If we go Dutch, you can still touch my love, it's free
We can work without the perks just you and me
Thug it out 'til we get it right

[Keri Hilson (Timbaland):]
Baby if you strip, you can get a tip
'Cause I like you just the way you are
(I'm about to strip and I'm well equipped
Can you handle me the way I are?)
I don't need the Gs or the car keys
Boy I like you just the way you are
Let me see you strip, you can get a tip
'Cause I like you just the way you are

[D.O.E.:]
Baby girl, I don't got a huge old house I rent a room in a house
Listen baby girl, I ain't got a motorboat but I can float your boat
So listen baby girl, once you get a dose of D.O.E. you're gon' want some more
So listen baby girl, when I make it I want you there, want you there, yeah"""),
("Smells Like Teen Spirit", "Nirvana", "rock", """Load up on guns, bring your friends
It's fun to lose and to pretend
She's over-bored and self-assured
Oh no, I know a dirty word

Hello, hello, hello, how low
Hello, hello, hello, how low
Hello, hello, hello, how low
Hello, hello, hello

With the lights out, it's less dangerous
Here we are now, entertain us
I feel stupid and contagious
Here we are now, entertain us
A mulatto, an albino
A mosquito, my libido

Yeah, hey, yay

I'm worse at what I do best
And for this gift, I feel blessed
Our little group has always been
And always will until the end

Hello, hello, hello, how low
Hello, hello, hello, how low
Hello, hello, hello, how low
Hello, hello, hello

With the lights out, it's less dangerous
Here we are now, entertain us
I feel stupid and contagious
Here we are now, entertain us
A mulatto, an albino
A mosquito, my libido

Yeah, hey, yay

And I forget just why I taste
Oh yeah, I guess it makes me smile
I found it hard, it's hard to find
Oh well, whatever, never mind

Hello, hello, hello, how low
Hello, hello, hello, how low
Hello, hello, hello, how low
Hello, hello, hello

With the lights out, it's less dangerous
Here we are now, entertain us
I feel stupid and contagious
Here we are now, entertain us
A mulatto, an albino
A mosquito, my libido

A denial, a denial
A denial, a denial
A denial, a denial
A denial, a denial
A denial"""),
("Too Sweet", "Hozier", "rock", """It can't be said I'm an early bird
It's ten o'clock before I say a word
Baby, I can never tell
How do you sleep so well?

You keep telling me to live right
To go to bed before the daylight
But then you wake up for the sunrise
You know you don't gotta pretend
Baby, now and then

Don't you just wanna wake up
Dark as a lake
Smelling like a bonfire
Lost in a haze?
If you're drunk on life, babe
I think it's great
But while in this world

I think I'll take my whiskey neat
My coffee black and my bed at three
You're too sweet for me
You're too sweet for me
I take my whiskey neat
My coffee black and my bed at three
You're too sweet for me
You're too sweet for me

I aim low
I aim true, and the ground's where I go
I work late where I'm free from the phone
And the job gets done
But you worry some, I know

But who wants to live forever, babe
You treat your mouth as if it's Heaven's gate
The rest of you like you're the TSA
I wish that I could go along
Babe, don't get me wrong

You know you're bright as the morning
As soft as the rain
Pretty as a vine
As sweet as a grape
If you can sit in a barrel
Maybe I'll wait
Until that day

I'd rather take my whiskey neat
My coffee black and my bed at three
You're too sweet for me
You're too sweet for me
I take my whiskey neat
My coffee black and my bed at three
You're too sweet for me
You're too sweet for me

I take my whiskey neat
My coffee black and my bed at three
You're too sweet for me
You're too sweet for me"""),
("Beggin'", "Måneskin", "rock", """Put your loving hand out, baby
'Cause I'm beggin'

I'm beggin', beggin' you
So put your loving hand out, baby
I'm beggin', beggin' you
So put your loving hand out, darlin'

Riding high when I was king
I played it hard and fast, 'cause I had everything
I walked away, you won me then
But easy come and easy go and it would end

So, anytime I bleed, you let me go
Yah, anytime I feed, you get me know
Anytime I seek, you let me know
But I planted that seed, just let me go
I'm on my knees when I'm beggin'
'Cause I don't wanna lose you
Hey, yeah, ra-ta-ta-ta!

'Cause I'm beggin', beggin' you
Uh, put your loving hand out, baby
I'm beggin', beggin' you, ah
And put your loving hand out, darlin'

I need you to understand
Tried so hard to be your man
The kind of man you want in the end
Only then can I begin to live again

An empty shell, I used to be
The shadow of my life was hangin' over me
A broken man that I don't know
Won't even stand the devil's dance to win my soul

What we doin'? What we chasin'?
Why the bottom? Why the basement?
Why we got good shit, don't embrace it?
Why the feel for the need to replace me?
You're the wrong way track from the good
I want to paint a picture tellin' where we could be at
Like a heart in the best way should
You can give it away, you had it and you took the pay
But I keep walkin' on, keep openin' doors
Keep hopin' for, now the door is yours
Keep also home
'Cause I don't want to live in a broken home, girl, I'm beggin'

Mmm, yeah-yeah, yeah, I'm beggin', beggin' you
So put your loving hand out, baby
I'm beggin', beggin' you
So put your loving hand out, darlin'

I'm fighting hard to hold my own
Just can't make it all alone
I'm holding on, I can't fall back
I'm just a calm, 'bout to fade to black

I'm beggin', beggin' you
Put your loving hand out, baby
I'm beggin', beggin' you
So put your loving hand out, darlin'
I'm beggin', beggin' you
So put your loving hand out, baby
I'm beggin', beggin' you
So put your loving hand out, darlin'

I'm beggin', beggin' you
So put your loving hand out, baby
I'm beggin', beggin' you
So put your loving hand out"""),
("I WANNA BE YOUR SLAVE", "Måneskin", "rock", """I wanna be your slave
I wanna be your master
I wanna make your heart beat
Run like rollercoasters
I wanna be a good boy
I wanna be a gangster
'Cause you can be the beauty
And I could be the monster
I love you since this morning
Not just for aesthetic
I wanna touch your body
So fucking electric
I know you scared of me
You said that I'm too eccentric
I'm crying all my tears
And that's fucking pathetic
I wanna make you hungry
Then I wanna feed ya
I wanna paint your face
Like you're my Mona Lisa
I wanna be a champion
I wanna be a loser
I'll even be a clown
Cause I just wanna amuse ya
I wanna be your sex toy
I wanna be your teacher
I wanna be your sin
I wanna be a preacher
I wanna make you love me
Then I wanna leave ya
'Cause baby I'm your David
And you're my Goliath

Because I'm the devil
Who's searching for redemption
And I'm a lawyer
Who's searching for redemption
And I'm a killer
Who's searching for redemption
I'm a motherfucking monster
Who's searching for redemption
And I'm a bad guy
Who's searching for redemption
And I'm a blond girl
Who's searching for redemption
I'm a freak that
Is searching for redemption
I'm a motherfucking monster
Who's searching for redemption

I wanna be your slave
I wanna be your master
I wanna make your heart beat
Run like rollercoasters
I wanna be a good boy
I wanna be a gangster
Cause you can be the beauty
And I could be the monster
I wanna make you quiet
I wanna make you nervous
I wanna set you free
But I'm too fucking jealous
I wanna pull your strings
Like you're my telecaster
And if you want to use me I could be your puppet

'Cause I'm the devil
Who's searching for redemption
And I'm a lawyer
Who's searching for redemption
And I'm a killer
Who's searching for redemption
I'm a motherfucking monster
Who's searching for redemption

I wanna be your slave
I wanna be your master"""),
("We Will Rock You", "Queen", "rock", """Buddy you're a boy make a big noise
Playin' in the street gonna be a big man some day
You got mud on yo' face
You big disgrace
Kickin' your can all over the place
Singin'

We will we will rock you
We will we will rock you

Buddy you're a young man hard man
Shoutin' in the street gonna take on the world some day
You got blood on yo' face
You big disgrace
Wavin' your banner all over the place

We will we will rock you
(Sing it out!)
We will we will rock you

Buddy you're an old man poor man
Pleadin' with your eyes gonna make you some peace some day
You got mud on your face
Big disgrace
Somebody better put you back into your place

We will we will rock you
(Sing it!)
We will we will rock you

(Everybody)

We will we will rock you
We will we will rock you

(Alright)"""),
("This I Love", "Guns N' Roses", "rock", """And now, I don't know why she wouldn't say goodbye
But then, it seems that I had seen it in her eyes
Though it might not be wise, I'd still have to try
With all the love I have inside, I can't deny
I just can't let it die, 'cause her heart's just like mine
And she holds her pain inside
So, if you ask me why she wouldn't say goodbye
I know somewhere inside
There is a special light still shining bright
And even on the darkest night, she can't deny

So, if she's somewhere near me, I hope to God she hears me
There's no one else could ever make me feel I'm so alive
I hoped she'd never leave me, please God, you must believe me
I've searched the universe and found myself within her eyes

No matter how I try, you say it's all a lie
So what's the use of my confessions to a crime
Of passions that won't die, in my heart?

So, if she's somewhere near me, I hope to God she hears me
There's no one else could ever make me feel I'm so alive
I hoped she'd never leave me, please God, you must believe me
I've searched the universe and found myself within her eyes

So, if she's somewhere near me, I hope to God she hears me
There's no one else could ever make me feel I'm so alive
I hoped she'd never leave me, please God, you must believe me
I've searched the universe and found myself within her eyes

So, now I don't know why she wouldn't say goodbye
It just might be that I had seen it in her eyes
And now, it seems that I gave up my ghost of pride
I'll never say goodbye"""),
("Everybody Wants To Rule The World", "Tears For Fears", "rock", """Welcome to your life
There's no turning back
Even while we sleep
We will find you

Acting on your best behaviour
Turn your back on mother nature
Everybody wants to rule the world

It's my own design
It's my own remorse
Help me to decide
Help me make the most

Of freedom and of pleasure
Nothing ever lasts forever
Everybody wants to rule the world

There's a room where the light won't find you
Holding hands while the walls come tumbling down
When they do I'll be right behind you

So glad we've almost made it
So sad they had to fade it
Everybody wants to rule the world

I can't stand this indecision
Married with a lack of vision
Everybody wants to rule the world
Say that you'll never never never never need it
One headline why believe it?
Everybody wants to rule the world

All for freedom and for pleasure
Nothing ever lasts forever
Everybody wants to rule the world"""),
("Money Talks", "BossMan Dlow", "hip-hop", """Yeah
(Ayo, Eli, what the fuck?)
Uh
Big Za

Old broke-ass nigga, where your cheese at? (Where your cheese at?)
Where the bad bitches? Come here, girl, I need that (Come here, girl)
Throw that ass back, I know it's fat, I'ma still catch it (I'ma still catch it)
Bad shit, super thick, real heavy (Real heavy)
Blue money, red bitches, gold bottles (Yeah)
He ain't get it, I'll spend it no problem (Yeah)
Money talk for me, I ain't even gotta say shit
I ain't one of them, baby, find a bitch to play with

Big Za pulled up, baby, you in trouble (You in trouble)
Every nigga hatin' on me, tell 'em I said fuck 'em (I said fuck 'em)
If you ain't got a check for me, baby, don't check me (Don't check me)
Tell the police I said, "Fuck you, catch me" (Gotta catch me)
Get out the house, girl, them rich niggas outside (Outside)
All this water on me like I just got baptized (Baptized)
If you're gettin' to the chicken, bitch, show somethin' (Show somethin')
Big Za chain hittin', home run (Home run)
Knock that pussy out the field, baby (Out the field, baby)
Red bottoms for your heels, baby (For your heels, baby)
You never seen a street nigga count a mil', baby (Count a mil', baby)
If you keep it real, I'll pay your bills, baby (Bills, baby)
Say you like rich niggas, come here, baby, what's up then? (What's up then?)
Street nigga courtside, nan' chain tucked in (Nan' chain tucked in)
Big Za on SportsCenter, trap nigga top ten (Top ten)
Fuck 12, real street nigga, know we locked in (Yeah)

Old broke-ass nigga, where your cheese at? (Where your cheese at?)
Where the bad bitches? Come here, girl, I need that (Come here, girl)
Throw that ass back, I know it's fat, I'ma still catch it (I'ma still catch it)
Bad shit, super thick, real heavy (Real heavy)
Blue money, red bitches, gold bottles (Yeah)
He ain't get it, I'll spend it no problem (Yeah)
Money talk for me, I ain't even gotta say shit
I ain't one of them, baby, find a bitch to play with"""),
("fukumean", "Gunna", "hip-hop", """(Ooh, Dunk Rock)

Fuck you mean?
Young Gunna Wunna back, callin' me splurge
Watch me jump right off the curb
Bentley Spur fly like a bird
Spin on the first and the third
Solid, I'm keepin' my word
Can't be my equal, I don't know what you heard
Crank up the foreign, I swerve
Keep me a stick if they purge

Ha, ha, ha, ha
Ha, ha, ha, ha

Fuck you mean?
Young Gunna Wunna, they workin' my nerves
I'm about to pour up some syrup
Fucking this bitch like a perv'
Smack from the back, grab her perm
Ice, the burr, uh, shittin' on all you lil' turds
Can't take that dick, wait your turn
In my own lane, we can't merge
Suck with no hands, you can learn
Let's see how much you can earn
Watch me go big like the Worm
And I ain't smokin' no sherm
I'm in this bitch with P Litty
QP, QP-ski
All of my bitches is pretty, they showin' they titties, it's up to the ceilin'
I let her run through a million, I rock with her really, let's fuck on a billion
I'ma get down to the gritty, then fuck up the city, the home of the villains
Ecstasy, wonderful feelin'
Smoke out the pound when I'm chillin'
Trappin', I made me a killin'
Look, I got everybody wishin'
I hope you play your position
I don't want nobody listenin'
I see the ho with precision
Get rich my only decision

Fuck you mean?
Young Gunna Wunna back, callin' me splurge
Watch me jump right off the curb
Bentley Spur fly like a bird
Spin on the first and the third
Solid, I'm keepin' my word
Can't be my equal, I don't know what you heard
Crank up the foreign, I swerve
Keep me a stick if they purge

Fuck you mean?
Fuck you mean?
Yeah
Yeah"""),
("Goosebumps", "Travis Scott", "hip-hop", """[Travis Scott:]
Yeah
7:30 in the night, yeah
Ooh-oooh, ooh

I get those goosebumps every time, yeah, you come around, yeah
You ease my mind, you make everything feel fine
Worried 'bout those comments
I'm way too numb, yeah, it's way too dumb, yeah
I get those goosebumps every time, I need the Heimlich
Throw that to the side, yeah
I get those goosebumps every time, yeah
When you're not around (Straight up)
When you throw that to the side, yeah (It's lit)
I get those goosebumps every time, yeah

7-1-3
Through the 2-8-1, yeah, I'm ridin', why they on me?
Why they on me? I'm flyin', sippin' low-key
I'm sippin' low-key in Onyx, rider, rider
When I'm pullin' up right beside ya
Pop star, lil' Mariah
When I text a cute game, wildness
Throw a stack on the Bible
Never Snapchat or took molly
She fall through plenty, her and all her ginnies, yeah
We at the top floor, right there off Doheny, yeah
Oh no, I can't fuck with y'all
Yeah, when I'm with my squad I cannot do no wrong
Yeah, saucin' in the city, don't get misinformed
Yeah, they gon' pull up on you (Brr, brr, brr)
Yeah, we gon' do some things, some things you can't relate
Yeah, 'cause we from a place, a place you cannot stay
Oh, you can't go, oh, I don't know
Oh, back the fuck up off me (Brr, brr, brr)

I get those goosebumps every time, yeah, you come around, yeah
You ease my mind, you make everything feel fine
Worried 'bout those comments
I'm way too numb, yeah, it's way too dumb, yeah
I get those goosebumps every time, I need the Heimlich
Throw that to the side, yeah
I get those goosebumps every time, yeah
When you're not around
When you throw that to the side, yeah
I get those goosebumps every time

[Kendrick Lamar:]
I want to press my like, yeah, I wanna press my
I want a green light, I wanna be like
I wanna press my line, yeah
I wanna take that ride, yeah
I'm gonna press my line
I want a green light, I wanna be like, I wanna press my—
Mama, dear, spare your feelings
I'm relivin' moments, peeling more residual
(I can) buy the building, burn the building
Take your bitch, rebuild the building just to fuck some more
(I can) justify my love for you
And touch the sky for God to stop, debating war
Put the pussy on a pedestal (Ayy)
Put the pussy on a high horse
That pussy to die for
That pussy to die for
Peter, piper, picked a pepper
So I could pick your brain and put your heart together
We depart the shady parts and party hard
The diamonds yours, the coupe forever
My best shots might shoot forever like (Brr)

[Travis Scott:]
I get those goosebumps every time, yeah, you come around, yeah
You ease my mind, you make everything feel fine
Worried 'bout those comments
I'm way too numb, yeah, it's way too dumb, yeah
I get those goosebumps every time, I need the Heimlich
Throw that to the side, yeah
I get those goosebumps every time, yeah
When you're not around
When you throw that to the side, yeah
I get those goosebumps every time"""),
("HIGHEST IN THE ROOM", "Travis Scott", "hip-hop", """I got room in my fumes (Yeah)
She fill my mind up with ideas
I'm the highest in the room (It's lit)
Hope I make it outta here (Let's go)

She saw my eyes, she know I'm gone (Ah)
I see some things that you might fear
I'm doin' a show, I'll be back soon (Soon)
That ain't what she wanna hear (Nah)
Now I got her in my room (Ah)
Legs wrapped around my beard
Got the fastest car, it zoom (Skrrt)
Hope we make it outta here (Ah)
When I'm with you, I feel alive
You say you love me, don't you lie (Yeah)
Won't cross my heart, don't wanna die
Keep the pistol on my side (Yeah)

Case it's fumes (Smoke)
She fill my mind up with ideas (Straight up)
I'm the highest in the room (It's lit)
Hope I make it outta here (Let's go, yeah)

We ain't stressin' 'bout the loot (Yeah)
My block made of quesería
This not the molly, this the boot
Ain't no comin' back from here
Live the life of La Familia
It's so much gang that I can't see ya (Yeah)
Turn it up 'til they can't hear (We can't)
Runnin', runnin' 'round for the thrill
Yeah, dawg, dawg, 'round my real (Gang)
Raw, raw, I been pourin' to the real (Drank)
Nah, nah, nah, they not back of the VIP (In the VIP)
Gorgeous, baby, keep me hard as steel
Ah, this my life, I did not choose
Uh, been on this since we was kids
We gon' stay on top and break the rules
Uh, I fill my mind up with ideas

Case it's fumes
She fill my mind up with ideas (Straight up)
I'm the highest in the room (I'm the highest, it's lit)
Hope I make it outta here"""),
("Mask Off", "Future", "hip-hop", """Call it how it is
Hendrix
I promise, I swear, I swear
You heard, spit it, yo

Percocets (Yah), molly, Percocets (Percocets)
Percocets (Yah), molly, Percocets (Percocets)
Rep the set (Yeah), gotta rep the set (Gang, gang)
Chase a check (Chase it), never chase a bitch (Don't chase no bitches)
Mask on (Mask off), fuck it, mask off (Ma—, excuse me?)
Mask on (Mask off), fuck it, mask off (Mask off)
Percocets ('Cets), molly, Percocets (Percocets)
Chase a check (Chase it), never chase a bitch (Don't chase no bitches)

Two cups (Cup), toast up with the gang (Gang, gang)
From food stamps to a whole 'nother domain, yah
Out the bottom (Yeah), I'm the livin' proof (Super)
Ain't compromisin', half a million on the coupe (Gang, gang)
Drug houses (Where?), lookin' like Peru (whoa-whoa-whoa)
Graduated (Crazy), I was overdue (I'm on due)
Pink molly (Molly), I can barely move (Barely move)
Ask about me ('Bout me), I'm gon' bust a move (ay, I'm provin')
Rick James (James), thirty-three chains (Thirty-three)
Ocean air (Air), cruisin' Biscayne (Big foreigns)
Top off (Yah), that's a liability (Big foreigns)
Hit the gas (Gas), boostin' my adrenaline (Big foreigns)

Percocets (Yeah), molly, Percocets (Big foreigns)
Percocets (Yeah), molly, Percocets (Big foreigns)
Rep the set (Yeah), gotta rep the set (Gang, gang)
Chase a check (Chase it) (Yeah), never chase a bitch (Don't chase no bitches) (Big foreigns)
Mask on (Mask off) (Yeah), fuck it, mask off (Ma—, excuse me?) (Big foreigns)
Mask on (Mask off) (Yeah), fuck it, mask off (Ma—, excuse me?) (Big foreigns)
Percocets (Yeah), molly, Percocets (Big foreigns)
Chase a check (Chase it) (Yeah, yeah), never chase a bitch (Don't chase no bitches)

Ford or Maybach (Ford or), I drive anything (Yeah)
Buy my Range (Yeah), make 'em go insane (Yeah)
(Oh my Lord, praise him be)
My guillotine, drank Promethazine (Drank prometh')
TEC and beams (Yah), go to those extremes (Aight, let's go, let's go)
Parliament (Parliament), calamari Wednesday (Yah)
Parlay in Vegas, we was in attendance (What's good, what's good?)
Before the business (Yeah), Theodore lenses
Theo-Dur prescriptions (Yeah), focus on the missions (Pour my four)
Intermission (Hold up), never take a break (We can pull up)
Switch states (Switch them), touch down, foreign plates (Switch)
Ain't no way, ain't no fuckin' way (No)
We call the play, we didn't come to play (No)
Rob the bank, we gon' rob the game (Again)
They gang, we gang (Gang)
But they are not the same (Freebandz)

Percocets (Yeah), molly, Percocets (Big foreigns)
Percocets (Yeah), molly, Percocets (Big foreigns)
Rep the set (Yeah), gotta rep the set (Gang, gang)
Chase a check (Chase it), never chase a bitch (Don't chase no bitches) (Big foreigns)
Mask on (Mask off) (Yeah), fuck it, mask off (Ma—, excuse me?) (Big foreigns)
Mask on (Mask off) (Yeah), fuck it, mask off (Ma—, excuse me?) (Big foreigns)
Percocets (Yeah), molly, Percocets (Big foreigns)
Chase a check (Chase it) (Yeah, yeah), never chase a bitch (Don't chase no bitches) (Big foreigns)

Mask on, fuck it, mask off
Mask on, fuck it, mask off
Mask on, fuck it, mask off
Gas gone, never nod off
(Cold chills, prison cells)
(Oh my Lord, praise him be)"""),
("See You Again", "Tyler, The Creator", "hip-hop", """Okay, okay, okay, okay, okay, okay, o—

You live in my dream state
Relocate my fantasy
I stay in reality
You live in my dream state
Any time I count sheep
That's the only time we make up, make up
You exist behind my eyelids, my eyelids
Now, I don't wanna wake up

20/20, 20/20 vision
Cupid hit me, Cupid hit me with precision
I wonder if you look both ways when you cross my mind
I said, I said
I'm sick of, sick of, sick of, sick of chasing
You're the one that's always running through my daydreams
I—I can only see your face when I close my eyes (Uh-huh)

Can I get a kiss?
And can you make it last forever?
I said, I'm 'bout to go to war (Uh-huh)
And I don't know if I'ma see you again

Can I get a kiss? (Can I?)
And can you make it last forever? (Can you?)
I said, I'm 'bout to go to war (I'm 'bout to)
And I don't know if I'ma see you again

Ugh, switch it up

I said, okay, okay, okay, okey-dokey, my infatuation
Is translating to another form of what you call it? (Love)
Oh yeah, oh yeah, oh yeah, I ain't met you, I've been looking
Stop the waiting 'fore I stop the chasing, like an alcoholic

"You don't understand me" What the fuck do you mean?
It's them rose-tinted cheeks, yeah, it's them dirt-colored eyes
Sugar-honey iced tea, bumblebee on the scene
Yeah, I'd give up my bakery to have a piece of your pie

Ugh!

20/20, 20/20 vision
Cupid hit me, cupid hit me with precision
I wonder if you look both ways when you cross my mind
I said, I said
I'm sick of, sick of, sick of, sick of chasing
You're the one that's always running through my daydreams
I—I can only see your face when I close my eyes
So

Can I get a kiss? (Can I get a kiss?)
And can you make it last forever? (Make it last forever)
I said I'm 'bout to go to war ('Bout to go to war)
I don't know if I'ma see you again (See you again)

Can I get a kiss? (Can I?)
And can you make it last forever? (Can you?)
I said I'm 'bout to go to war ('Bout to)
And I don't know if I'ma see you again

Okay, okay, okay, okay, okay, okay, okay, o—
La la, la la la la, la la
Okay, okay, okay, okay, okay, okay, okay, o—
La la, la la la, la la
Okay, okay, okay, okay, okay, okay, okay, o—
La la, la la la la, la la
La la, la la la la
One more time?"""),
("Lucid Dreams", "Juice WRLD", "hip-hop", """Enviyon on the mix
No, no, no, no
No-no, no, no, no
No, no, no, no, no
No, no, no, no

I still see your shadows in my room
Can't take back the love that I gave you
It's to the point where I love and I hate you
And I cannot change you so I must replace you (oh)
Easier said than done
I thought you were the one
Listening to my heart instead of my head
You found another one, but
I am the better one
I won't let you forget me
I still see your shadows in my room
Can't take back the love that I gave you
It's to the point where I love and I hate you
And I cannot change you so I must replace you (oh)
Easier said than done
I thought you were the one
Listening to my heart instead of my head
You found another one, but
I am the better one
I won't let you forget me

You left me falling and landing inside my grave
I know that you want me dead
I take prescriptions to make me feel a-okay
I know it's all in my head

I have these lucid dreams where I can't move a thing
Thinking of you in my bed
You were my everything
Thoughts of a wedding ring
Now I'm just better off dead
I'll do it over again
I didn't want it to end
I watch it blow in the wind
I should've listened to my friends
Leave this shit in the past
But I want it to last
You were made outta plastic (fake)
I was tangled up in your drastic ways
Who knew evil girls had the prettiest face
You gave me a heart that was full of mistakes
I gave you my heart and you made heart break

You made my heart break
You made my heart ache
(I still see your shadows in my room)
You made my heart break
You made my heart ache
(Can't take back the love that I gave you)
You made my heart break
(Were made outta plastic fake)
You made my heart ache
(I still see your shadows in my room)
You made my heart break again
(I was tangled up your drastic ways)
(Who knew evil girls had the prettiest face?)

I still see your shadows in my room
Can't take back the love that I gave you
It's to the point where I love and I hate you
And I cannot change you so I must replace you (oh)
Easier said than done
I thought you were the one
Listening to my heart instead of my head
You found another one, but
I am the better one
I won't let you forget me
I still see your shadows in my room
Can't take back the love that I gave you
It's to the point where I love and I hate you
And I cannot change you so I must replace you (oh)
Easier said than done
I thought you were the one
Listening to my heart instead of my head
You found another one, but
I am the better one
I won't let you forget me

Leave this shit in the past but I want it to last
You were made outta plastic (fake)
I was tangled up in your drastic ways
Who knew evil girls had the prettiest face?

Easier said than done
I thought you were the one
(Instead of my head)
I won't let you forget me"""),
("Star Shopping", "Lil Peep", "hip-hop", """Wait right here
I'll be back in the mornin'
I know that I'm not that important to you
But to me, girl, you're so much more than gorgeous
So much more than perfect (yeah)
Right now I know that I'm not really worth it
If you give me time, I could work on it
Give me some time while I work on it

Losin' your patience, and, girl, I don't blame you
The Earth's in rotation, you're waitin' for me
Look at my face, when I fuck on your waist
'Cause we only have one conversation a week

That's why your friends always hatin' on me
Fuck 'em though, I did this all by myself
Matter fact, I ain't never asked no one for help
And that's why I don't pick up my phone when it rings

None of my exes is over Lil Peep
Nobody flexin' as much as I be
That's why she text me and tell me she love me
She know that someday I'll be over the sea

Makin' my money and smokin' my weed
I think it's funny, she open up to me, get comfortable with me
Once I got it comin', I love her, she love me
I know that I'm nothing like someone her family want me to be
If I find a way, would you walk it with me?
Look at my face while you talkin' to me
'Cause we only have one conversation a week

Can I get one conversation at least?
Shout out to everyone makin' my beats, you helpin' me preach
This music's the only thing keepin' the peace when I'm fallin' to pieces

Look at the sky tonight, all of the stars have a reason
A reason to shine, a reason like mine and I'm fallin' to pieces
Look at the sky tonight, all of the stars have a reason"""),
("Lose Yourself", "Eminem", "hip-hop", """Look, if you had one shot, or one opportunity
To seize everything you ever wanted, in one moment
Would you capture it, or just let it slip?

Yo! His palms are sweaty, knees weak, arms are heavy
There's vomit on his sweater already: Mom's spaghetti
He's nervous, but on the surface he looks calm and ready
To drop bombs, but he keeps on forgetting
What he wrote down, the whole crowd goes so loud
He opens his mouth, but the words won't come out
He's choking, how? Everybody's joking now
The clock's run out, time's up, over, blaow!
Snap back to reality, ope there goes gravity, ope
There goes Rabbit, he choked, he's so mad but he won't
Give up that easy, no, he won't have it, he knows
His whole back's to these ropes, it don't matter, he's dope
He knows that but he's broke, he's so stagnant, he knows
When he goes back to this mobile home, that's when it's
Back to the lab again yo, this whole rhapsody
Better go capture this moment and hope it don't pass him, and

You better lose yourself in the music
The moment, you own it, you better never let it go
You only get one shot, do not miss your chance to blow
This opportunity comes once in a lifetime, yo
You better lose yourself in the music
The moment, you own it, you better never let it go
You only get one shot, do not miss your chance to blow
This opportunity comes once in a lifetime, yo
You better…

His soul's escaping through this hole that is gaping
This world is mine for the taking, make me king
As we move toward a New World Order
A normal life is boring; but superstardom's
Close to post-mortem, it only grows harder
Homie grows hotter, he blows, it's all over
These hoes is all on him, coast-to-coast shows
He's known as the Globetrotter, lonely roads
God only knows, he's grown farther from home, he's no father
He goes home and barely knows his own daughter
But hold your nose, 'cause here goes the cold water
These hoes don't want him no mo', he's cold product
They moved on to the next schmoe who flows
He nose-dove and sold nada, and so the soap opera
Is told, it unfolds, I suppose it's old, partner
But the beat goes on: da da dum da dum da da da da

You better lose yourself in the music
The moment, you own it, you better never let it go
You only get one shot, do not miss your chance to blow
This opportunity comes once in a lifetime, yo
You better lose yourself in the music
The moment, you own it, you better never let it go
You only get one shot, do not miss your chance to blow
This opportunity comes once in a lifetime, yo
You better…

No more games, I'ma change what you call rage
Tear this motherfuckin' roof off like two dogs caged
I was playin' in the beginning, the mood all changed
I've been chewed up and spit out and booed off stage
But I kept rhymin' and stepped right in the next cypher
Best believe somebody's payin' the Pied Piper
All the pain inside amplified by the
Fact that I can't get by with my 9-to-5
And I can't provide the right type of life for my family
'Cause man, these goddamn food stamps don't buy diapers
And there's no movie, there's no Mekhi Phifer, this is my life
And these times are so hard, and it's gettin' even harder
Tryna feed and water my seed, plus teeter-totter
Caught up between bein' a father and a prima donna
Baby mama drama, screamin' on her, too much for me to wanna
Stay in one spot, another day of monotony's
Gotten me to the point I'm like a snail, I've got
To formulate a plot or end up in jail or shot
Success is my only motherfuckin' option, failure's not
Mom, I love you, but this trailer's got
To go; I cannot grow old in Salem's Lot
So here I go, it's my shot: feet, fail me not
This may be the only opportunity that I got

You better lose yourself in the music
The moment, you own it, you better never let it go (go)
You only get one shot, do not miss your chance to blow
This opportunity comes once in a lifetime, yo
You better lose yourself in the music
The moment, you own it, you better never let it go (go)
You only get one shot, do not miss your chance to blow
This opportunity comes once in a lifetime, yo
You better…

You can do anything you set your mind to, man"""),
("Alright", "Kendrick Lamar", "hip-hop", """[Kendrick Lamar:]
Alls my life, I has to fight, nigga
Alls my life, I—
Hard times like, "Yah!"
Bad trips like, "Yah!"
Nazareth
I'm fucked up, homie, you fucked up
But if God got us, then we gon' be alright

[Pharrell Williams:]
Nigga, we gon' be alright
Nigga, we gon' be alright
We gon' be alright
Do you hear me, do you feel me? We gon' be alright
Nigga, we gon' be alright
Huh? We gon' be alright
Nigga, we gon' be alright
Do you hear me, do you feel me? We gon' be alright

[Kendrick Lamar:]
Uh, and when I wake up
I recognize you're looking at me for the pay cut
But homicide be looking at you from the face down
What MAC-11 even boom with the bass down?
Schemin', and let me tell you 'bout my life
Painkillers only put me in the twilight
Where pretty pussy and Benjamin is the highlight
Now tell my mamma I love her, but this what I like, Lord knows
Twenty of 'em in my Chevy, tell 'em all to come and get me
Reaping everything I sow, so my karma coming heavy
No preliminary hearings on my record
I'm a motherfucking gangster in silence for the record, uh
Tell the world I know it's too late
Boys and girls, I think I've gone cray
Drown inside my vices all day
Won't you please believe when I say

Wouldn't you know
We been hurt, been down before
Nigga, when our pride was low
Lookin' at the world like, "Where do we go?"
Nigga, and we hate po-po
Wanna kill us dead in the street for sure
Nigga, I'm at the preacher's door
My knees gettin' weak, and my gun might blow
But we gon' be alright

[Pharrell Williams:]
Nigga, we gon' be alright
Nigga, we gon' be alright
We gon' be alright
Do you hear me, do you feel me? We gon' be alright
Nigga, we gon' be alright
Huh? We gon' be alright
Nigga, we gon' be alright
Do you hear me, do you feel me? We gon' be alright

[Kendrick Lamar:]
What you want you, a house? You, a car?
Forty acres and a mule? A piano, a guitar?
Anything, see my name is Lucy, I'm your dog
Motherfucker, you can live at the mall
I can see the evil, I can tell it, I know it's illegal
I don't think about it, I deposit every other zero
Thinking of my partner, put the candy, paint it on the Regal
Digging in my pocket, ain't a profit big enough to feed you
Every day my logic get another dollar just to keep you
In the presence of your chico, ah!
I don't talk about it, be about it, every day I sequel
If I got it then you know you got it, Heaven, I can reach you
Pat Dawg, Pat Dawg, Pat Dawg, my dog, that's all
Bick back and Chad, I trap the bag for y'all
I rap, I black on track so rest assured
My rights, my wrongs; I write 'til I'm right with God

Wouldn't you know
We been hurt, been down before
Nigga, when our pride was low
Lookin' at the world like, "Where do we go?"
Nigga, and we hate po-po
Wanna kill us dead in the street for sure
Nigga, I'm at the preacher's door
My knees gettin' weak, and my gun might blow
But we gon' be alright

[Pharrell Williams:]
Nigga, we gon' be alright
Nigga, we gon' be alright
We gon' be alright
Do you hear me, do you feel me? We gon' be alright
Nigga, we gon' be alright
Huh? We gon' be alright
Nigga, we gon' be alright
Do you hear me, do you feel me? We gon' be alright

[Kendrick Lamar & Thundercat:]
I keep my head up high
I cross my heart and hope to die
Lovin' me is complicated
Too afraid of a lot of changes
I'm alright, and you're a favorite
Dark nights in my prayers

[Kendrick Lamar:]
I remembered you was conflicted
Misusing your influence, sometimes I did the same
Abusing my power, full of resentment
Resentment that turned into a deep depression
Found myself screamin' in the hotel room
I didn't wanna self-destruct
The evils of Lucy was all around me
So I went runnin' for answers"""),
("Runaway", "Kanye West", "hip-hop", """[Rick James and James Brown:]
Look at you, look at you, look at you, look at you
Look at you, look at you, look at you, look at you
Look at you, look at you, look at you, look at you
Look at you, look at you, look at you, look at you
(Ladies and gentlemen, ladies, ladies and gentlemen)

[Kanye West:]
And I always find, yeah, I always find something wrong
You been puttin' up with my shit just way too long
I'm so gifted at finding what I don't like the most
So I think it's time for us to have a toast

[Kanye West:]
Let's have a toast for the douchebags
Let's have a toast for the assholes
Let's have a toast for the scumbags
Every one of them that I know
Let's have a toast for the jerk-offs
That'll never take work off
Baby, I got a plan
Run away fast as you can

[Kanye West:]
She find pictures in my e-mail
I sent this bitch a picture of my dick
I don't know what it is with females
But I'm not too good at that shit
See, I could have me a good girl
And still be addicted to them hood rats
And I just blame everything on you
At least you know that's what I'm good at

[Kanye West:]
And I always find, yeah, I always find
Yeah, I always find something wrong
You been puttin' up with my shit just way too long
I'm so gifted at finding what I don't like the most
So I think it's time for us to have a toast

[Kanye West:]
Let's have a toast for the douchebags
Let's have a toast for the assholes
Let's have a toast for the scumbags
Every one of them that I know
Let's have a toast for the jerk-offs
That'll never take work off
Baby, I got a plan
Run away fast as you can

[Kanye West and Rick James:]
Run away from me, baby
Ah, run away
Run away from me, baby (Look at you, look at you, look at you)
Run away
When it starts to get crazy (Look at you, look at you, look at you)
Then run away
Babe, I got a plan, run away as fast as you can
Run away from me, baby
Run away
Run away from me, baby (Look at, look at, look at, look at, look at, look at, look at you)
Run away
When it starts to get crazy (Look at you, look at you, look at you, look at you)
Why can't she just run away?
Baby, I got a plan
Run away as fast as you can (Look at you, look at you, look at you)

[Pusha T:]
Twenty-four seven, three sixty-five, pussy stays on my mind
I-I-I-I did it, alright, alright, I admit it
Now pick your next move, you could leave or live with it
Ichabod Crane with that motherfuckin' top off
Split and go where? Back to wearing knock-offs?
Haha, knock it off, Neimans, shop it off
Let's talk over mai tais, waitress, top it off
Hoes like vultures, wanna fly in your Freddy loafers
You can't blame 'em, they ain't never seen Versace sofas
Every bag, every blouse, every bracelet
Comes with a price tag, baby, face it
You should leave if you can't accept the basics
Plenty hoes in the baller-nigga matrix
Invisibly set, the Rolex is faceless
I'm just young, rich, and tasteless, P

[Kanye West:]
Never was much of a romantic
I could never take the intimacy
And I know I did damage
'Cause the look in your eyes is killing me
I guess you knew of that advantage
'Cause you could blame me for everything
And I don't know how I'ma manage
If one day, you just up and leave

[Kanye West:]
And I always find, yeah, I always find something wrong
You been puttin' up with my shit just way too long
I'm so gifted at finding what I don't like the most
So I think it's time for us to have a toast

[Kanye West:]
Let's have a toast for the douchebags
Let's have a toast for the assholes
Let's have a toast for the scumbags
Every one of them that I know
Let's have a toast for the jerk-offs
That'll never take work off
Baby, I got a plan
Run away fast as you can"""),
("Never Lose Me", "Flo Milli", "hip-hop", """Never had a bitch like me in your life
You ain't never had a bitch like me in your life, uh
Never had a bitch like me in your life
You ain't never had a bitch like me in your life (Yeah)

He speed in the Wraith while his hand on my coochie (Yeah)
He touchin' Emilio Pucci (Uh)
Doin' good, bitch, I'm gucci (I'm good)
Fly to Asia, he feedin' me sushi (Ooh)
When we fuckin', it feel like a movie
Raw bitch, ain't never been a groupie
Stiff on a ho, I like my nigga bougie (Yeah)
Tell me you don't never wanna lose me

Tell me you don't never wanna lose me
Tell me you don't never wanna lose me
Tell me you don't never wanna lose me
Tell me you don't never wanna lose me
Tell me you don't never wanna lose me
Tell me you don't never wanna lose me (Lose me)
Tell me you don't never—

Keep me a Haitian, I love me a Zoe
I've been thinkin' 'bout you on the road
We havin' rich sex on a boat
He hit it back to back like it's dope (Like it's dope)
How you gon' prove you could treat me right?
You stole my heart like a thief in the night
Yeah, he my man, he was never your type
If you try me, ho, it's on sight
He totin' the Uzi, but he actin' real bougie (Bougie, yeah)
I like to fight over dick, ho, don't get hit with the two-piece (Two-piece)
You know you can call if you need me
Tell me you ain't never ever leavin' (No)
When I suck it, I look in your eyes (Yeah)
You better fuck me like you mean it (Fuck me like you mean it)

Tell me you don't never wanna lose me
Tell me you don't never wanna lose me
Tell me you don't never wanna lose me
Tell me you don't never wanna lose me
Tell me you don't never wanna lose me
Tell me you don't never wanna lose me (Lose me)
Tell me you don't never—

He speed in the Wraith while his hand on my coochie
Doin' good, bitch, I'm gucci
When we fuckin', it feel like a movie
Be stiff on a ho, I like my nigga bougie (Yeah)
Tell me you don't never wanna lose me"""),
("Unforgettable", "French Montana", "hip-hop", """[Swae Lee:]
It's not good enough for me, since I been with you
It's not gonna work for you, nobody can equal me (I know)
I'm gonna sip on this drink, when I'm fucked up
I should know how to pick up
I'm gonna catch the rhythm while she push up against me
Ooh, was she tipsy
I had enough convo for 24
I peeped you from across the room
Pretty little body, dancing like GoGo, aye

And you are unforgettable
I need to get you alone
Why not?
A fucking good time, never hurt nobody
I got a little drink but it's not Bacardi
If you loved the girl then I'm so, so sorry
I got to give it to her like we in a marriage

Oh, like we in a hurry
No, no, I won't tell nobody
You're on your level too
Tryna do what lovers do

[French Montana:]
Feelin' like I'm fresh out, Boosie
If they want the drama, got the Uzi
Ship the whole crew to the cruise ship
Doin' shit you don't even see in movies
Ride with me, ride with me, boss
I got a hard head but her ass soft
She want the last name with the ring on it
'Cause I pulled out a million cash,
Told her plank on it

[Swae Lee:]
And you are unforgettable
I need to get you alone
[French Montana:]
Now you wanna choose
Just pop the bubbly in the 'cuzi

[Swae Lee:]
It's not good enough for me, since I been with you, ooh
I'm gonna sip on this drink, when I'm fucked up
I should know how to pick up
I'm gonna catch the rhythm while she push up against me
Ooh, was she tipsy
I had enough convo for 24
I peeped you from across the room
Pretty little body, dancing like GoGo

And you are unforgettable
I need to get you alone
Why not?
A fucking good time, never hurt nobody
I got a little drink but it's not Bacardi
If you loved the girl then I'm so, so sorry
I got to give it to her like we in a marriage

Oh, like we in a hurry
No, no, I won't tell nobody
You're on your level too
Tryna do what lovers do

[French Montana:]
Oh oh, you ain't enough for me
Too much for you alone
Baby, go and grab some bad bitches, bring 'em home
Know the jet's on me
I'mma curve my best for you, you know
So pick up that dress for me
Leave the rest on
Too much convo 24 hours
When you stand next to 24 karats
She left her man at home
She don't love him no more
I want your mind and your body
Don't mind nobody
So, you don't ever hurt nobody
Baby girl work your body
Work your body

[Swae Lee:]
And you are unforgettable
I need to get you alone
[French Montana:]
Now you wanna choose
Just pop the bubbly in the 'cuzi

[Swae Lee:]
Why not?
Oh, like we in a hurry
No, no, I won't tell nobody
You're on your level too
Tryna do what lovers do"""),
("Super Rich Kids", "Frank Ocean", "hip-hop", """Too many bottles of this wine we can't pronounce
Too many bowls of that green, no Lucky Charms
The maids come around too much
Parents ain't around enough
Too many joy rides in daddy's Jaguar
Too many white lies and white lines
Super rich kids with nothing but loose ends
Super rich kids with nothing but fake friends

Start my day up on the roof
There's nothing like this type of view
Point the clicker at the tube
I prefer expensive news
New car, new girl
New ice, new glass
New watch, good times babe
It's good times, yeah
She wash my back three times a day
This shower head feels so amazing
We'll both be high, the help don't stare
They just walk by, they must don't care
A million one, a million two
A hundred more will never do

Too many bottles of this wine we can't pronounce
Too many bowls of that green, no Lucky Charms
The maids come around too much
Parents ain't around enough
Too many joy rides in daddy's Jaguar
Too many white lies and white lines
Super rich kids with nothing but loose ends
Super rich kids with nothing but fake friends

Real love, I'm searching for a real love
Oh, real love, I'm searching for a real love
Oh, real love

Close your eyes to what you can't imagine
We are the Xanny-gnashing
Caddy-smashing, bratty ass
He mad, he snatched his daddy's Jag
And used the shit for batting practice
Adamant and he thrashing
Purchasing crappy grams with half the hand of cash you handed
Panic and patch me up
Pappy done latch-keyed us
Toying with Raggy Anns and Mammy done had enough
Brash as fuck, breaching all these aqueducts
Don't believe us
Treat us like we can't erupt, yup

Polo sweats and Hermes blankets
Them label hoes be stealing my shit
And all their clothes revealing their tits
Pills, high enough to touch the rim in that bitch
We party in my living room
'Cause father is gone
And he left me this empire
That runs on its own
So all I got to do is whatever the fuck I want
All we ever do is whatever the fuck we want

We end our day up on the roof
I say I'll jump, I never do
But when I'm drunk I act a fool
Talking 'bout, do they sew wings on tailored suits
I'm on that ledge, she grabs my arm
She slaps my hand
It's good times, yeah
Sleeve rips off, I slip, I fall
The market's down like 60 stories
And some don't end the way they should
My silver spoon has fed me good
A million one, a million cash
Close my eyes and feel the crash

Too many bottles of this wine we can't pronounce
Too many bowls of that green, no Lucky Charms
The maids come around too much
Parents ain't around enough
Too many joy rides in daddy's Jaguar
Too many white lies and white lines
Super rich kids with nothing but loose ends
Super rich kids with nothing but fake friends

Real love, ain't that something rare
I'm searching for a real love, talking 'bout real love
Real love, yeah
Real love
I'm searching for a real love
Talking 'bout a real love"""),
("DILEMMA", "Central Cee", "hip-hop", """(ZEL, this shit crazy)
(Nathan)
Yo

Spotted a dime out the corner of my eye
She got nuff man on the line
Back just pokin' like a knife
Think she tryna get man lined
Demon with the angel eyes
Maybe I'm hypnotised
But why am I thinkin' twice? Yo

Two-man step, I got my ting on me, so don't even try that shit
Make it clap like I won a award, like I'm sat at the BRITs
Bro in the trap, Lyca SIM, no O2, settin' up shop in the Ritz
Before "Commitment Issues", I was sat with bro just plannin' a lick
Canada Goose on me, shiesty one when I go link that baddie
Check my rear just in case this bitch think she can drop the addy
Sweet one like my sugar is low, I think I need some candy
She keep on sayin', "I wanna be down," go listen to Brandy

Spotted a dime out the corner of my eye
She got nuff man on the line
Back just pokin' like a knife
Think she tryna get man lined
Demon with the angel eyes
Maybe I'm hypnotised
But why am I thinkin' twice? Yo (Alright)

We don't send them the addy, if they wanna come, then we send 'em a personal driver
I don't care if that bitch is a baddie if I know that girl is a liar (Nah)
She materialistic, I make her take this dick and work for designer
Said that she want 10K, but she ain't even worth it in naira (Nah)
I just spotted a dime, she decent, demon, she wanna sign a agreement (Uh-huh)
All of these bitches bookie, probably chattin' to guys I'm beefin' (Nah-uh)
They ain't got no morals, they see what I've got and they think about teefin'
I had to kick this bitch out the telly 'cause she tried takin' a pic of me sleepin' (Alright)
Jack-jack boys wanna try trap me with a female and pray that I slip up
The young G's don't take my advice and stay out the way at the mix-up
She was shakin' it on me and felt my nank pokin', and she thought I was bricked up (Brick)
I'm tellin' these women that we do the trickin' and none of these chicks can trick us
Try line man up, that's a myth, security guard at the front and the back of the crib
I'm prang, look back when I jump out the van, six man cramped up in the back of the whip (Nah)
If the car get spun, bro's back in the bin, and I slipped up once, it won't happen again
If I was them, would've given it up, if I keep it a buck, I ain't rappin' again

Spotted a dime out the corner of my eye
She got nuff man on the line
Back just pokin' like a knife
Think she tryna get man lined
Demon with the angel eyes
Maybe I'm hypnotised
But why am I thinkin' twice? Yo

She materialistic, I make her take this dick and work for designer
Said that she want 10K, but she ain't even worth it in naira"""),
("I Love Rock 'N Roll", "Joan Jett And The Blackhearts", "rock", """I saw him dancing there by the record machine
I knew he must have been about seventeen
The beat was going strong
Playing my favorite song
And I could tell it wouldn't be long till he was with me, yeah me
And I could tell it wouldn't be long till he was with me, yeah me

Singing, I love rock and roll
So put another dime in the jukebox, baby
I love rock and roll
So come and take your time and dance with me
Ow!

He smiled, so I got up and asked for his name
But that don't matter, he said, 'cause it's all the same
He said, "Can I take you home
Where we can be alone?"
And next we were moving on, he was with me, yeah me
Next we were moving on, he was with me, yeah me

Singing, I love rock and roll
So put another dime in the jukebox, baby
I love rock and roll
So come and take your time and dance with me
Ow!

He said, "Can I take you home
Where we can be alone?"
Next we're moving on, he was with me, yeah me
And we'll be moving on and singing that same old song, yeah with me

Singing, I love rock and roll
So put another dime in the jukebox, baby
I love rock and roll
So come and take your time and dance with me

I love rock and roll
So put another dime in the jukebox, baby
I love rock and roll
So come and take your time and dance with

I love rock and roll
So put another dime in the jukebox, baby
I love rock and roll
So come and take your time and dance with

I love rock and roll
So put another dime in the jukebox, baby
I love rock and roll
So come and take your time and dance with

I love rock and roll
So put another dime in the jukebox, baby
I love rock and roll
So come and take your time and dance with me"""),
("Born To Run", "Bruce Springsteen", "rock", """In the day, we sweat it out on the streets
Of a runaway American dream
At night, we ride through mansions of glory
In suicide machines
Sprung from cages out on Highway 9
Chrome wheeled, fuel injected and steppin' out over the line
Oh, baby this town rips the bones from your back
It's a death trap, it's a suicide rap
We gotta get out while we're young
'Cause tramps like us, baby we were born to run
Yes, girl, we were

Wendy let me in, I wanna be your friend
I want to guard your dreams and visions
Just wrap your legs 'round these velvet rims
And strap your hands across my engines
Together we could break this trap
We'll run till we drop, baby we'll never go back
Oh, will you walk with me out on the wire?
'Cause baby I'm just a scared and lonely rider
But I gotta know how it feels
I want to know if love is wild, babe
I want to know if love is real
Oh, can you show me?

Beyond the palace, hemi-powered drones
Scream down the boulevard
The girls comb their hair in rearview mirrors
And the boys try to look so hard
The amusement park rises bold and stark
Kids are huddled on the beach in a mist
I wanna die with you, Wendy, on the streets tonight
In an everlasting kiss

(1, 2, 3, 4) The highways jammed with broken heroes
On a last chance power drive
Everybody's out on the run tonight
But there's no place left to hide
Together, Wendy, we can live with the sadness
I'll love you with all the madness in my soul
Oh, someday girl, I don't know when
We're gonna get to that place
Where we really want to go, and we'll walk in the sun
But till then, tramps like us
Baby, we were born to run

Oh honey, tramps like us
Baby, we were born to run
Come on with me, tramps like us
Baby, we were born to run"""),
("Starman", "David Bowie", "rock", """Hey now, now
Oh, oh, oh

Didn't know what time it was, the lights were low
I leaned back on my radio
Some cat was laying down some rock 'n' roll
"Lotta soul," he said
Then the loud sound did seem to fade
Came back like a slow voice on a wave of phase
That weren't no DJ, that was hazy cosmic jive

There's a starman waiting in the sky
He'd like to come and meet us
But he thinks he'd blow our minds
There's a starman waiting in the sky
He's told us not to blow it
'Cause he knows it's all worthwhile
He told me
Let the children lose it
Let the children use it
Let all the children boogie

I had to phone someone so I picked on you
Hey, that's far out, so you heard him too
Switch on the TV, we may pick him up on channel two
Look out your window, I can see his light
If we can sparkle he may land tonight
Don't tell your poppa or he'll get us locked up in fright

There's a starman waiting in the sky
He'd like to come and meet us
But he thinks he'd blow our minds
There's a starman waiting in the sky
He's told us not to blow it
'Cause he knows it's all worthwhile
He told me
Let the children lose it
Let the children use it
Let all the children boogie

Starman waiting in the sky
He'd like to come and meet us
But he thinks he'd blow our minds
There's a starman waiting in the sky
He's told us not to blow it
'Cause he knows it's all worthwhile
He told me
Let the children lose it
Let the children use it
Let all the children boogie

La, la, la, la-la, la, la, la
La, la, la, la-la, la, la, la
La, la, la, la-la, la, la, la
La, la, la, la-la, la, la, la
La, la, la, la-la, la, la, la
La, la, la, la-la, la, la, la
La, la, la, la-la, la, la, la
La, la, la, la-la, la, la, la"""),
("Once In A Lifetime", "Talking Heads", "rock", """And you may find yourself living in a shotgun shack
And you may find yourself in another part of the world
And you may find yourself behind the wheel of a large automobile
And you may find yourself in a beautiful house, with a beautiful wife
And you may ask yourself, "Well, how did I get here?"

Letting the days go by, let the water hold me down
Letting the days go by, water flowing underground
Into the blue again after the money's gone
Once in a lifetime, water flowing underground

And you may ask yourself, "How do I work this?"
And you may ask yourself, "Where is that large automobile?"
And you may tell yourself, "This is not my beautiful house."
And you may tell yourself, "This is not my beautiful wife."

Letting the days go by, let the water hold me down
Letting the days go by, water flowing underground
Into the blue again after the money's gone
Once in a lifetime, water flowing underground

Same as it ever was, same as it ever was
Same as it ever was, same as it ever was
Same as it ever was, same as it ever was
Same as it ever was, same as it ever was

Water dissolving and water removing
There is water at the bottom of the ocean
Under the water, carry the water
Remove the water at the bottom of the ocean
Water dissolving and water removing

Letting the days go by, let the water hold me down
Letting the days go by, water flowing underground
Into the blue again, into the silent water
Under the rocks and stones, there is water underground
Letting the days go by, let the water hold me down
Letting the days go by, water flowing underground
Into the blue again after the money's gone
Once in a lifetime, water flowing underground

You may ask yourself, "What is that beautiful house?"
You may ask yourself, "Where does that highway go to?"
And you may ask yourself, "Am I right? Am I wrong?"
And you may say to yourself, "My God! What have I done?"

Letting the days go by, let the water hold me down
Letting the days go by, water flowing underground
Into the blue again, into the silent water
Under the rocks and stones, there is water underground
Letting the days go by, let the water hold me down
Letting the days go by, water flowing underground
Into the blue again after the money's gone
Once in a lifetime, water flowing underground

Same as it ever was, same as it ever was
Same as it ever was and look where my hand was
Time isn't holding up, time isn't after us
Same as it ever was, same as it ever was
Same as it ever was, same as it ever was
Same as it ever was, same as it ever was
Letting the days go by, same as it ever was
Here a twister comes, here comes the twister
Same as it ever was, same as it ever was (Letting the days go by)
Same as it ever was, same as it ever was (Letting the days go by)
Once in a lifetime (Let the water hold me down)
Letting the days go by (Water flowing underground)
Into the blue again"""),
("Rebel Girl", "Bikini Kill", "rock", """That girl thinks she's the queen of the neighborhood
She's got the hottest trike in town
That girl she holds her head up so high
I think I wanna be her best friend, yeah

Rebel Girl, Rebel Girl
Rebel Girl you are the queen of my world
Rebel Girl, Rebel Girl
I think I wanna take you home
I wanna try on your clothes, uh

When she walks, the revolution's coming
In her hips, there's revolution
When she talks, I hear the revolution
In her kiss, I taste the revolution

Rebel Girl, Rebel Girl
Rebel Girl you are the queen of my world
Rebel Girl, Rebel Girl
I know I wanna take you home
I wanna try on your clothes, uh

That girl thinks she's the queen of the neighborhood
I got news for you, she is!
They say she's a slut, but I know
She is my best friend, yeah

Rebel Girl, Rebel Girl
Rebel Girl you are the queen of my world
Rebel Girl, Rebel Girl
I think I wanna take you home
I wanna try on your clothes

Love you like a sister always
Soul sister, Rebel Girl
Come and be my best friend
Really Rebel Girl
I really like you
I really wanna be
Your best friend
Be my Rebel Girl"""),
("Where Is My Mind?", "Pixies", "rock", """Ooh—stop

With your feet on the air and your head on the ground
Try this trick and spin it, yeah (Yeah)
Your head will collapse, and there's nothing in it
And you'll ask yourself

Where is my mind?
Where is my mind?
Where is my mind?
Way out in the water, see it swimmin'

I was swimmin' in the Caribbean
Animals were hiding behind the rocks
Except the little fish
Bumped into me, I swear he was trying to talk to me, koi-koi

Where is my mind?
Where is my mind?
Where is my mind?
Way out in the water, see it swimmin'

With your feet on the air and your head on the ground
Try this trick and spin it, yeah
Your head will collapse, and there's nothing in it
And you'll ask yourself

Where is my mind?
Where is my mind?
Where is my mind?
Way out in the water, see it swimmin'

With your feet on the air and your head on the ground
Try this trick and spin it, yeah"""),
("Bring Me To Life", "Evanescence", "rock", """How can you see into my eyes like open doors?
Leading you down into my core where I've become so numb
Without a soul my spirit's sleeping somewhere cold
Until you find it there and lead it back home

(Wake me up)
Wake me up inside
(I can't wake up)
Wake me up inside
(Save me)
Call my name and save me from the dark
(Wake me up)
Bid my blood to run
(I can't wake up)
Before I come undone
(Save me)
Save me from the nothing I've become

Now that I know what I'm without
You can't just leave me
Breathe into me and make me real
Bring me to life

(Wake me up)
Wake me up inside
(I can't wake up)
Wake me up inside
(Save me)
Call my name and save me from the dark
(Wake me up)
Bid my blood to run
(I can't wake up)
Before I come undone
(Save me)
Save me from the nothing I've become

Bring me to life
(I've been living a lie, there's nothing inside)
Bring me to life

Frozen inside without your touch
Without your love, darling
Only you are the life among the dead

All this time I can't believe I couldn't see
Kept in the dark but you were there in front of me
I've been sleeping a thousand years it seems
Got to open my eyes to everything
Without a thought, without a voice, without a soul
Don't let me die here
There must be something more
Bring me to life

(Wake me up)
Wake me up inside
(I can't wake up)
Wake me up inside
(Save me)
Call my name and save me from the dark
(Wake me up)
Bid my blood to run
(I can't wake up)
Before I come undone
(Save me)
Save me from the nothing I've become

Bring me to life
(I've been living a lie, there's nothing inside)
Bring me to life"""),
("Super Lady", "(G)I-DLE", "k-pop", """[Romanized:]

I am the top, super lady (Oh)
I never lose, yeah ('Cause got a superpower)
I am a God, super lady (Oh)
I never die, bwatji? modu follow

Boy, boy, boy, geogi bikyeo eoseo
Urin love, love, love, ttawi hagin bappa
Yeogin war, war, war, jabi ttawin eopseo
Nal mangneundamyeon slay it (Lock it)
Namjadeurui ppeonhan gasik (Drop it)
Eok sori naneun geu sachi
Yeongungeun jogeumui heundeullil teum eopsi
Ready to shoot

Ipsuri da beonjyeodo
Geu eotteon nomboda meotjige (nuguboda meotjige)
Woah-oh-oh
Useo boiji deo geochilge
Dokada hae, that's my name
I never bow on my way, yeah

Lady, lady
Call me 'Super Lady'
Lady, lady
Follow, ladies (Uh-huh)
Onward, ladies (Uh-huh)
Super ladies (Uh-huh)
Hana dul set (Ah)

Mama said, "neon eonjenga sesangeul mangchil ak" (wae?)
Geu geobe jillin nunbitdo cham motdwaesseunikka
Oh, geu nunbicheun paewangsaek paegi yeowangui jajil the baddie
Baegimyeon baegi da gijeolhan gakseonge geommeogeun devil
Geurae boeneun ge eopgeodeun do you know-ow-ow?

Ipsuri da beonjyeodo
Geu eotteon nomboda meotjige (nuguboda meotjige)
Woah-oh-oh
Useo boiji deo geochilge
Dokada hae, that's my name
I never bow on my way, yeah

Lady, lady
Call me 'Super Lady'
Lady, lady
Follow, ladies (Uh-huh)
Onward, ladies (Uh-huh)
Super ladies (Uh-huh)
Let's go on, fearless, we came to take win

Back it up (Oh)
Back it up (Oh-oh)
Back it up (Oh)
Back it up
Everybody say

Nuga uril bureundamyeon yes, sir, super fast
Nuga uril mangneundamyeon yes, sir, supernatural
Nuga bwado urin yes, stronger than Superman
Yes, sir, I got superpower
Yes, sir, I'm a-

[Korean:]

I am the top, super lady (Oh)
I never lose, yeah ('Cause got a superpower)
I am a God, super lady (Oh)
I never die, 봤지? 모두 follow

Boy, boy, boy, 거기 비켜 어서
우린 love, love, love, 따위 하긴 바빠
여긴 war, war, war, 자비 따윈 없어
날 막는다면 slay it (Lock it)
남자들의 뻔한 가식 (Drop it)
억 소리 나는 그 사치
영웅은 조금의 흔들릴 틈 없이
Ready to shoot

입술이 다 번져도
그 어떤 놈보다 멋지게 (누구보다 멋지게)
Woah-oh-oh
웃어 보이지 더 거칠게
독하다 해, that's my name
I never bow on my way, yeah

Lady, lady
Call me 'Super Lady'
Lady, lady
Follow, ladies (Uh-huh)
Onward, ladies (Uh-huh)
Super ladies (Uh-huh)
하나 둘 셋 (Ah)

Mama said, "넌 언젠가 세상을 망칠 악" (왜?)
그 겁에 질린 눈빛도 참 못됐으니까
Oh, 그 눈빛은 패왕색 패기 여왕의 자질 the baddie
백이면 백이 다 기절한 각성에 겁먹은 devil
그래 뵈는 게 없거든 do you know-ow-ow?

입술이 다 번져도
그 어떤 놈보다 멋지게 (누구보다 멋지게)
Woah-oh-oh
웃어 보이지 더 거칠게
독하다 해, that's my name
I never bow on my way, yeah

Lady, lady
Call me 'Super Lady'
Lady, lady
Follow, ladies (Uh-huh)
Onward, ladies (Uh-huh)
Super ladies (Uh-huh)
Let's go on, fearless, we came to take win

Back it up (Oh)
Back it up (Oh-oh)
Back it up (Oh)
Back it up
Everybody say

누가 우릴 부른다면 yes, sir, super fast
누가 우릴 막는다면 yes, sir, supernatural
누가 봐도 우린 yes, stronger than Superman
Yes, sir, I got superpower
Yes, sir, I'm a-

[English translation:]

I am the top, super lady (Oh)
I never lose, yeah ('Cause got a super power)
I am a God, super lady (Oh)
Did you see I never die? Everyone, follow

Boy, boy, boy, get out of the way
We're busy talking about love, love, love
This is war, war, war, no mercy
If you stop me, slay it (Lock it)
Men's obvious pretense (Drop it)
That luxury that sounds like a million dollars
A hero has no room to waver
Ready to shoot

Even if my lipstick get smudged
Cooler than any other guy (Cooler than any other guy)
Oh-oh-oh
I smile more harshly
They say it's harsh, that's my name
I never bow on my way

Lady, lady
Call me 'Super Lady'
Lady, lady
Follow, ladies (Uh-huh)
Onward, ladies (Uh-huh)
Super ladies (Uh-huh)
One, two, three

Mama said, "You are the evil one who will ruin the world someday" (Why?)
Because those scared eyes are so mean
Those eyes are the fierce, spirit and qualities of a queen, The Baddie
If one hundred is one hundred, then one hundred is a devil who is frightened by the awakening of fainting
Yes, there is nothing to see, do you know-ow-ow?

Even if my lipstick get smudged
Cooler than any other guy (Cooler than any other guy)
Oh-oh-oh
I smile more harshly
They say it's harsh, that's my name
I never bow on my way

Lady, lady
Call me 'Super Lady'
Lady, lady
Follow, ladies (Uh-huh)
Onward, ladies (Uh-huh)
Super ladies (Uh-huh)
Let's go on, fearless, we came to take win

Back it up (Oh)
Back it up (Oh-oh)
Back it up (Oh)
Back it up
Everybody say

If someone calls us, yes, sir, super fast
If someone stops us, yes sir, supernatural
No matter who sees who we are, yes, stronger than Superman
Yes, sir, I got superpower
Yes, sir, I'm a-"""),
("HANN (Alone) (한 (一))", "(G)I-DLE", "k-pop", """[Romanized:]

Do you remember you remember
Remember what you said (said)
Neoneun naege mweodeun jul geotcheoreom mareul geonnetta (geonnetta)
Don't you remember you remember
Remember what you said (said)
Neoneun machi museun yageul meogeun manyang byeonhaetta

Deuriweojin Blue nae heuryeojineun nun
Jinjja Is this true huhoe an hanyago
Nae eojeye My boo boo boo
Lonely life joa
Da samkyeobeorin mul nan shigeobeorin deut
I want you to be ruined butjabji anha kkeut
Neon eojeye My boo boo boo
Lonely life jal ga

Chagapge nareul bonda namin deut doraseonda
Nan meonghani seoitta
Mollatteon neoreul bwatta geujeo useumman naonda
Nan ije neoreul molla

Neol ijeurira Woo woo woo
Jeori ga oji ma dorabojido mala
Neol jiurira Woo woo woo
Jeori ga oji ma dorabojido mala

Do you remember you remember
Remember what you said (said)
Naneun eotteon maldo mot haebon chae neoreul bonhaetta (bonhaetta)
Don't you remember you remember
Remember what you said (said)
Naneun machi museun yageul meogeun manyang byeonhaetta

Da byeonhaetta
Tto heunan sarangcheoreom bbeonhaetta
Gumjurin sajacheoreom neoneun nal neomu weonhaetta
Sonjitgwa geonnen mal
Geojitmarieottamyeon neon sesang jeil motdwaetda
Geureon geoji da ttokgatji
Eommaga hhaetteon mal jeonbu da majji
Sarangeun kkamage byeonhaetta dollil su eobge da taeweotta
Oneul nan nae gieok sogeseo neol eobsaetta

Chagapge nareul bonda namin deut doraseonda
Nan meonghani seoitta
Mollatteon neoreul bwatta geujeo useumman naonda
Nan ije neoreul molla

Neol ijeurira Woo woo woo
Jeori ga oji ma dorabojido mala
Neol jiurira Woo woo woo
Jeori ga oji ma dorabojido mala

Meongdeun nae mame heunjeogeul jiugo
Jeongdeun ne nune nae mameul bichujyo
Neomu chagaweo kkamjjak nollalji molla
Dashi nae ape doraonda haedo
Ijen badajul jariga eomneyo
Kkeuti nan geojyo nan ije neoreul molla

Neol ijeurira Woo woo woo
Jeori ga oji ma dorabojido mala
Neol jiurira Woo woo woo
Jeori ga oji ma dorabojido mala

[Korean:]

Do you remember you remember
Remember what you said (said)
너는 내게 뭐든 줄 것처럼 말을 건넸다 (건넸다)
Don't you remember you remember
Remember what you said (said)
너는 마치 무슨 약을 먹은 마냥 변했다

드리워진 Blue 내 흐려지는 눈
진짜 Is this true 후회 안 하냐고
내 어제의 My boo boo boo
Lonely life 좋아
다 삼켜버린 물 난 식어버린 듯
I want you to be ruined 붙잡지 않아 끝
넌 어제의 My boo boo boo
Lonely life 잘 가

차갑게 나를 본다 남인 듯 돌아선다
난 멍하니 서있다
몰랐던 너를 봤다 그저 웃음만 나온다
난 이제 너를 몰라

널 잊으리라 Woo woo woo
저리 가 오지 마 돌아보지도 말아
널 지우리라 Woo woo woo
저리 가 오지 마 돌아보지도 말아

Do you remember you remember
Remember what you said (said)
나는 어떤 말도 못 해본 채 너를 보냈다 (보냈다)
Do you remember you remember
Remember what you said (said)
나는 마치 무슨 약을 먹은 마냥 변했다

다 변했다
또 흔한 사랑처럼 뻔했다
굶주린 사자처럼 너는 날 너무 원했다
손짓과 건넨 말
거짓말이었다면 넌 세상 제일 못됐다
그런 거지 다 똑같지
엄마가 했던 말 전부 다 맞지
사랑은 까맣게 변했다 돌릴 수 없게 다 태웠다
오늘 난 내 기억 속에서 널 없앴다

차갑게 나를 본다 남인 듯 돌아선다
난 멍하니 서있다
몰랐던 너를 봤다 그저 웃음만 나온다
난 이제 너를 몰라

널 잊으리라 Woo woo woo
저리 가 오지 마 돌아보지도 말아
널 지우리라 Woo woo woo
저리 가 오지 마 돌아보지도 말아

멍든 내 맘의 흔적을 지우고
정든 네 눈에 내 맘을 비추죠
너무 차가워 깜짝 놀랄지 몰라
다시 내 앞에 돌아온다 해도
이젠 받아줄 자리가 없네요
끝이 난 거죠 난 이제 너를 몰라

널 잊으리라 Woo woo woo
저리 가 오지 마 돌아보지도 말아
널 지우리라 Woo woo woo
저리 가 오지 마 돌아보지도 말아"""),
("MANIAC", "Stray Kids", "k-pop", """[Romanized:]

Let's go
Jeongsangin cheok dadeul him jom ppae
Jitgo inneun misodeureun ssehae
Locki pullimyeon da ttokgatji
Nuneun nal mot sogyeo ho

Boncheneun pullyeonne
Jeongshineul ganshinhi jabji
Nun hanbeon kkamppagigo back
Dashi sesangi jeonghan
Jeongsangin koseupeure junbi ppow

Mash up, mind blown jeongshineun back up
Prototype nae sogeun eonjena freaky monster
Yuhaeng gateun chinjeolhameun cheori jina rotten
Nae tongsue da shiweonhage yokhaedo
Da meokgeum

Poppin'
Sunjinhageman bodaga keuge dachim
Hoiga gyesokdwemyeon gweolliin jul ane toxic
Ireoni dolji warning

MANIAC
Nasa ppajin geotcheoreom michyeo MANIAC
Pingping dorabeorigetji
MANIAC Frankensteincheoreom georeo
MANIAC MANIAC Haha

MANIAC (Oh)
Nasa ppajin geotcheoreom useo MANIAC
(You can't stop the smoke)
Pingping dorabeorigetji (Thick as fog)
MANIAC bijeongsangtuseongi jibdan
(We're MANIACS)
MANIAC MANIAC

Da teojin inhyeong shilbabcheoreom
Gyeolguk bonsaegi deureonaji
Pyeonhaji aneun i life
It ain't "live" it's "holding on" yeah

Jeongsangin cheok dadeul cheok jom ppae
Jitgo inneun miso no fresh hae
Locket pulmyeon dadeul ttokgatji
Nuneun nal mot sogyeo ho

Naega geonneun i georineun da jirwebat
Da eonje teojilji moreuneun dormant volcano
Yamjeonhaetteon baramdo eonje bakkwilji molla
Dadeul sumgin chae saraga like a sealed tornado

Poppin'
Sunjinhageman bodaga keuge dachim
Hoiga gyesokdwemyeon gwelliin jul ane toxic
Ireoni dolji warning

MANIAC
Nasa ppajin geotcheoreom michyeo MANIAC
Pingping dorabeorigetji
MANIAC Frankensteincheoreom georeo
MANIAC MANIAC Haha

MANIAC (Oh)
Nasa ppajin geotcheoreom useo MANIAC
(You can't stop the smoke)
Pingping dorabeorigetji (Thick as fog)
MANIAC bijeongsangtuseongi jibdan
(We're MANIACS)
MANIAC MANIAC

Gadeukhae du nuneun lunatic
Modeun gamgagi nal seo itji
Yeppeuge pojanghan daero maebeon gadweo noeuni
Heulleogada bomyeon gyeolguk deureonagetji
Sumgyeojin naemyeone geu moseubi yeah

MANIAC
MANIAC (MANIAC)
MANIAC
MANIAC MANIAC
You cannot stop with this feeling

MANIAC (Oh)
Nasa ppajin geotcheoreom useo MANIAC
(You can't stop the smoke)
Pingping dorabeorigetji (Thick as fog)
MANIAC bijeongsangtuseongi jibdan
(We're MANIACS)
MANIAC MANIAC

[Korean:]

Let's go
정상인 척 다들 힘 좀 빼
짓고 있는 미소들은 쎄해
Lock이 풀리면 다 똑같지
눈은 날 못 속여 ho

본체는 풀렸네
정신을 간신히 잡지
눈 한번 깜빡이고 back
다시 세상이 정한
정상인 코스프레 준비 ppow

Mash up, mind blown 정신은 back up
Prototype 내 속은 언제나 freaky monster
유행 같은 친절함은 철이 지나 rotten
내 통수에 다 시원하게 욕해도
다 먹금

Poppin'
순진하게만 보다가 크게 다침
호의가 계속되면 권리인 줄 아네 toxic
이러니 돌지 warning

MANIAC
나사 빠진 것처럼 미쳐 MANIAC
핑핑 돌아버리겠지
MANIAC Frankenstein처럼 걸어
MANIAC MANIAC Haha

MANIAC (Oh)
나사 빠진 것처럼 웃어 MANIAC
(You can't stop the smoke)
핑핑 돌아버리겠지 (Thick as fog)
MANIAC 비정상투성이 집단
(We're MANIACS)
MANIAC MANIAC

다 터진 인형 실밥처럼
결국 본색이 드러나지
편하지 않은 이 life
It ain't "live" it's "holding on" yeah

정상인 척 다들 척 좀 빼
짓고 있는 미소 no fresh 해
Locket 풀면 다들 똑같지
눈은 날 못 속여 ho

내가 걷는 이 거리는 다 지뢰밭
다 언제 터질지 모르는 dormant volcano
얌전했던 바람도 언제 바뀔지 몰라
다들 숨긴 채 살아가 like a sealed tornado

Poppin'
순진하게만 보다가 크게 다침
호의가 계속되면 권리인 줄 아네 toxic
이러니 돌지 warning

MANIAC
나사 빠진 것처럼 미쳐 MANIAC
핑핑 돌아버리겠지
MANIAC Frankenstein처럼 걸어
MANIAC MANIAC Haha

MANIAC (Oh)
나사 빠진 것처럼 웃어 MANIAC
(You can't stop the smoke)
핑핑 돌아버리겠지 (Thick as fog)
MANIAC 비정상투성이 집단
(We're MANIACS)
MANIAC MANIAC

가득해 두 눈은 lunatic
모든 감각이 날 서 있지
예쁘게 포장한 대로 매번 가둬 놓으니
흘러가다 보면 결국 드러나겠지
숨겨진 내면의 그 모습이 yeah

MANIAC
MANIAC (MANIAC)
MANIAC
MANIAC MANIAC
You cannot stop with this feeling

MANIAC (Oh)
나사 빠진 것처럼 웃어 MANIAC
(You can't stop the smoke)
핑핑 돌아버리겠지 (Thick as fog)
MANIAC 비정상투성이 집단
(We're MANIACS)
MANIAC MANIAC

[English translation:]

Let's go
Relax everyone, stop pretending to be normal
All of your smiles look weird
When the Lock is released, we're all the same
Your eyes can't fool me, ho

The real self has been released
Barely holding on
After blinking once, back
Again, back to cosplaying as what
Society defines normal to be ppow

Mash up, mind blown put my mind on back up
Prototype, on the inside I'm always a freaky monster
Kindness is no longer trending, now rotten
You can backbite me as much as you want
I'll ignore them anyway

Poppin'
If you think I'm just pure and innocent, you're wrong
When a favor continues, people think it's their right, toxic
This is what drives me crazy, warning

MANIAC
Going crazy, like I have a loose screw MANIAC
Spinning, going crazy
MANIAC Walk like Frankenstein
MANIAC MANIAC Haha

MANIAC (Oh)
Laugh like I have a loose screw MANIAC
(You can't stop the smoke)
Spinning, going crazy (Thick as fog)
MANIAC a MANIAC group
(We're MANIACS)
MANIAC MANIAC

Like the seam of a torn doll
Eventually, you'll expose your real self
In this not easy life
It ain't "live" it's "holding on" yeah

Relax everyone, stop pretending to be normal
All of your smiles no fresh
When the Locket is open, we're all the same
Your eyes can't fool me, ho

This street I'm walking on is a minefield
Like a dormant volcano, never know when it'll all explode
Never know when the calm winds will change
Everyone lives hiding themselves like a sealed tornado

Poppin'
If you think I'm just pure and innocent, you're wrong
When a favor continues, people think it's their right, toxic
This is what drives me crazy, warning

MANIAC
Going crazy, like I have a loose screw MANIAC
Spinning, going crazy
MANIAC Walk like Frankenstein
MANIAC MANIAC Haha

MANIAC (Oh)
Laugh like I have a loose screw MANIAC
(You can't stop the smoke)
Spinning, going crazy (Thick as fog)
MANIAC a MANIAC group
(We're MANIACS)
MANIAC MANIAC

Eyes filled with lunatic
All senses are tense
Locked up while wrapped up in that pretty package
As time goes by, it'll eventually be revealed
The inner self that was hidden yeah

MANIAC
MANIAC (MANIAC)
MANIAC
MANIAC MANIAC
You cannot stop with this feeling

MANIAC (Oh)
Laugh like I have a loose screw MANIAC
(You can't stop the smoke)
Spinning, going crazy (Thick as fog)
MANIAC a MANIAC group
(We're MANIACS)
MANIAC MANIAC"""),
("Thunderous (소리꾼)", "Stray Kids", "k-pop", """[Romanized:]

Oh sorireul jireuneun naega oh
Changbiniranda nae jarineun naega chwihanda
Taedoneun teopeuhage teuraek wireul
Pokjuhaneun gigwancha ey
Morachineun heorikeine dwijibeojin usan
Jansorikkune chwehu haha kkori jokuna

Namukkuneun eoseo doragashio yeogin namural dega eomne
Nabjakhaejil ri eomneun kottae mok pittaewa hamkke seun juttae
Hweolsshin deo ungjanghage naeneun gyeongjeok sori
Ppangppang ppangppang

Here they come
Akdang murie tteugeoun piga dora onmome beonjyeo
Somunnan kkundeure moime ssodajineun nunbicheun
Freezing cold but I know we'll burn forever
Haeboraneun taedo nan yeojeonhi
Hal mareul naebaetji twe twe twe

Sorikkun
Sorikkun (twe twe twe)
Sorikkun
Man I'm not sorry, I'm dirty

Ureureukwangkwangkwangkwang cheondung (pparababam)
Gureum tago dudung (pparababam)
Baramgwa hamkke deungjanghan kkun
BANG BANG BANG BOOM
Man I'm not sorry, I'm dirty
Keep on talking, we don't play by the rules

Geurae dadeul heossorisorisori
Igeojeogeo gwichanaseo doridori
Mari neomu mana jakku naseoji jom mara
Why you mad? Why you sad? Why you tiktiktik

Out of anjung
Eolleri kkolleri meoshinneun cheokdeuri angjeung
Balkkeutjochado ttaraoji mothae yeogin nae pandeul
Deureobwa (What's up?)
Jiltuga (nana bwa)
Jeonbu hanjjogeuro chiweonoko beoryeo

Here they come
Akdang murie tteugeoun piga dora onmome beonjyeo
Somunnan kkundeure moime ssodajineun nunbicheun
Freezing cold but I know we'll burn forever
Haeboraneun taedo nan yeojeonhi
Hal mareul naebaetji twe twe twe
Hahaha

Sorikkun
Sorikkun (twe twe twe)
Sorikkun
Man I'm not sorry, I'm dirty

Kkundeuri wasseoyo (huh)
Kkundeuri wasseoyo (bikyeora)
Narimyeon nalmada oneun nari anin oneul
Sorikkundeuri wasseoyo

Weollae ppittakhae sorineun ildangbaek
Mame an deulmyeon deul ttaekkaji maldaedabhae
Final warning dangjang back up
Baeteo
Sen cheok
Back off
Hal mareul naebaetji twe twe twe

Sorikkun
Sorikkun
Man I'm not sorry, I'm dirty

Ureureukwangkwangkwangkwang cheondung (pparababam)
Gureum tago dudung (pparababam)
Baramgwa hamkke deungjanghan kkun
BANG BANG BANG BOOM
Man I'm not sorry, I'm dirty
Keep on talking, we don't play by the rules

[Korean:]

Oh 소리를 지르는 내가 oh
창빈이란다 내 자리는 내가 취한다
태도는 터프하게 트랙 위를
폭주하는 기관차 ey
몰아치는 허리케인에 뒤집어진 우산
잔소리꾼의 최후 하하 꼴이 좋구나

나무꾼은 어서 돌아가시오 여긴 나무랄 데가 없네
납작해질 리 없는 콧대 목 핏대와 함께 세운 줏대
훨씬 더 웅장하게 내는 경적 소리
빵빵 빵빵

Here they come
악당 무리에 뜨거운 피가 돌아 온몸에 번져
소문난 꾼들의 모임에 쏟아지는 눈빛은
Freezing cold but I know we'll burn forever
해보라는 태도 난 여전히
할 말을 내뱉지 퉤 퉤 퉤

소리꾼
소리꾼 (퉤 퉤 퉤)
소리꾼
Man I'm not sorry, I'm dirty

우르르쾅쾅쾅쾅 천둥 (빠라바밤)
구름 타고 두둥 (빠라바밤)
바람과 함께 등장한 꾼
BANG BANG BANG BOOM
Man I'm not sorry, I'm dirty
Keep on talking, we don't play by the rules

그래 다들 헛소리소리소리
이거저거 귀찮아서 도리도리
말이 너무 많아 자꾸 나서지 좀 말아
Why you mad? Why you sad? Why you 틱틱틱

Out of 안중
얼레리 꼴레리 멋있는 척들이 앙증
발끝조차도 따라오지 못해 여긴 내 판들
들어봐 (What's up?)
질투가 (나나 봐)
전부 한쪽으로 치워놓고 버려

Here they come
악당 무리에 뜨거운 피가 돌아 온몸에 번져
소문난 꾼들의 모임에 쏟아지는 눈빛은
Freezing cold but I know we'll burn forever
해보라는 태도 난 여전히
할 말을 내뱉지 퉤 퉤 퉤
Hahaha

소리꾼
소리꾼 (퉤 퉤 퉤)
소리꾼
Man I'm not sorry, I'm dirty

꾼들이 왔어요 (huh)
꾼들이 왔어요 (비켜라)
날이면 날마다 오는 날이 아닌 오늘
소리꾼들이 왔어요

원래 삐딱해 소리는 일당백
맘에 안 들면 들 때까지 말대답해
Final warning 당장 back up
뱉어
센 척
Back off
할 말을 내뱉지 퉤 퉤 퉤

소리꾼
소리꾼
Man I'm not sorry, I'm dirty

우르르쾅쾅쾅쾅 천둥 (빠라바밤)
구름 타고 두둥 (빠라바밤)
바람과 함께 등장한 꾼
BANG BANG BANG BOOM
Man I'm not sorry, I'm dirty
Keep on talking, we don't play by the rules

[English translation:]

Oh so they call me, the one shouting oh
Changbin, I choose my own path
Attitude tough, like a runway train
Going recklessly down the track ey
By a fierce hurricane, umbrellas flip inside-out
The faultfinder's last day, Haha serves them right

Go back woodcutter, there's nothing to cut here
There's no way they can lower my ego, I stick to my jutdae
Horns get louder and grander
Honk honk

Here they come
Villains make my blood boil and circulate throughout my body
All eyes on the gathering of the famous Thunderous ones are
Freezing cold but I know we'll burn forever
I don't care how they look at me
I'll always say what I have to say, Ptui, Ptui, Ptui

Thunderous
Thunderous (Ptui, Ptui, Ptui)
Thunderous
Man I'm not sorry, I'm dirty

RUMBLE SNAP CRACK Thunder (Barababam)
Riding on the clouds, tada (Barababam)
The Thunderous one appears with the wind
BANG BANG BANG BOOM
Man I'm not sorry, I'm dirty
Keep on talking, we don't play by the rules

Yeah everybody's talking nonsense
Tired of this and that, SMH SMH
You talk too much, stop meddling
Why you mad? Why you sad? Why you ticking me off

I don't care at all
Neener-neener, your attempt to look cool is just cute
You don't even come close to me, this is my show
Listen (What's up?)
Jealous (Guess they are)
Push everything aside and throw it away

Here they come
Villains make my blood boil and circulate throughout my body
All eyes on the gathering of the famous Thunderous ones are
Freezing cold but I know we'll burn forever
I don't care how they look at me
I'll always say what I have to say, Ptui, Ptui, Ptui
Hahaha

Thunderous
Thunderous (Ptui, Ptui, Ptui)
Thunderous
Man I'm not sorry, I'm dirty

The Thunderous ones have arrived (huh)
The Thunderous ones have arrived (Get out of the way)
They don't come everyday
The Thunderous ones have arrived

I was born crooked, my voice can go against a hundred
If I don't like something, I'll talk back until I'm satisfied
Final warning, immediately back up
Spit it out
Act tough
Back off
I'll always say what I have to say, Ptui Ptui Ptui

Thunderous
Thunderous
Man I'm not sorry, I'm dirty

RUMBLE SNAP CRACK Thunder (Barababam)
Riding on the clouds, tada (Barababam)
The Thunderous one appears with the wind
BANG BANG BANG BOOM
Man I'm not sorry, I'm dirty
Keep on talking, we don't play by the rules"""),
("Supernova", "aespa", "k-pop", """[Romanized:]

I'm like some kind of supernova
Watch out

Look at me go
Jaemi jom bol
Bichui core
So hot, hot
Muni yeollyeo
Seoroui jonjaereul neukkyeo
Machi Discord
Nal daleun neo neo nuguya (Incoming; Drop)

Sageoneun dagawa ah, oh, ayy
Geosege keojyeoga ah, oh, ayy
That tick, that tick, tick bomb
That tick, that tick, tick bomb
Gamhi geondeuriji mothal geol
Nugudo mariya
Jigeum nae aneseon
Su-su-su-supernova

Nova
Can't stop hyperstellar
Woncho geugeol chaja
Bring the light of a dying star
Bulleonaen nae ujureul bwa bwa
Supernova

Ah, body bang (Bang, bang, bang, bang, bang, bang)
Make it feel too right

Hwipsseullin eneoji it's so special
Janinhan queen imyeo scene ija jonggyeol
Itorok geodaehan nae anui explosion
Nae modeun sepo byeollobuteo mandeureojyeo (Under my control, ah)

Jilmuneun gyesokdwae ah, oh, ayy
Urin eodiseo wanna oh, ayy
Neukkyeo nae aneseon (Huh)
Su-su-su-supernova

Nova
Can't stop hyperstellar
Woncho geugeol chaja
Bring the light of a dying star
Bulleonaen nae ujureul bwa bwa
Supernova

Boiji anneun himeuro
Nege son naemireo bolkka
Ganeunghan modeun ganeungseong
Muhan sogui neoreul manna
It's about to bang-bang
Don't forget my name

Su-su-su-supernova

Sageoneun dagawa ah, oh, ayy
Geosege keojyeoga ah, oh, ayy
Jilmuneun gyesokdwae ah, oh, ayy
Urin eodiseo wanna oh, ayy
Sageoneun dagawa ah, oh, ayy
Geosege keojyeoga ah, oh, ayy
Tell me, tell me, tell me, oh, ayy
Urin eodiseo wanna oh, ayy
Urin eodiseo wanna oh, ayy

Nova (Nova)
Can't stop hyperstellar (Hyperstellar)
Woncho geugeol chaja
Bring the light of a dying star (Light of a dying star)
Bulleonaen nae ujureul bwa bwa (All the way)
Supernova (Hey-huh)

Sageoneun dagawa ah, oh, ayy (New star)
Geosege keojyeoga ah, oh, ayy
Jilmuneun gyesokdwae ah, oh, ayy (Nova)
Urin eodiseo wanna oh, ayy
Sageoneun dagawa ah, oh, ayy (Yeah-yeah-yeah-yeah)
Geosege keojyeoga ah, oh, ayy (Nova)
Jilmuneun gyesokdwae ah, oh, ayy (Bring the light of a dying star)

Supernova

[Korean:]

I'm like some kind of supernova
Watch out

Look at me go
재미 좀 볼
빛의 core
So hot, hot
문이 열려
서로의 존재를 느껴
마치 Discord
날 닮은 너 너 누구야 (Incoming; Drop)

사건은 다가와 ah, oh, ayy
거세게 커져가 ah, oh, ayy
That tick, that tick, tick bomb
That tick, that tick, tick bomb
감히 건드리지 못할 걸
누구도 말이야
지금 내 안에선
Su-su-su-supernova

Nova
Can't stop hyperstellar
원초 그걸 찾아
Bring the light of a dying star
불러낸 내 우주를 봐 봐
Supernova

Ah, body bang (Bang, bang, bang, bang, bang, bang)
Make it feel too right

휩쓸린 에너지 it's so special
잔인한 queen 이며 scene 이자 종결
이토록 거대한 내 안의 explosion
내 모든 세포 별로부터 만들어져 (Under my control, ah)

질문은 계속돼 ah, oh, ayy
우린 어디서 왔나 oh, ayy
느껴 내 안에선 (Huh)
Su-su-su-supernova

Nova
Can't stop hyperstellar
원초 그걸 찾아
Bring the light of a dying star
불러낸 내 우주를 봐 봐
Supernova

보이지 않는 힘으로
네게 손 내밀어 볼까
가능한 모든 가능성
무한 속의 너를 만나
It's about to bang-bang
Don't forget my name

Su-su-su-supernova

사건은 다가와 ah, oh, ayy
거세게 커져가 ah, oh, ayy
질문은 계속돼 ah, oh, ayy
우린 어디서 왔나 oh, ayy
사건은 다가와 ah, oh, ayy
거세게 커져가 ah, oh, ayy
Tell me, tell me, tell me, oh, ayy
우린 어디서 왔나 oh, ayy
우린 어디서 왔나 oh, ayy

Nova (Nova)
Can't stop hyperstellar (Hyperstellar)
원초 그걸 찾아
Bring the light of a dying star (Light of a dying star)
불러낸 내 우주를 봐 봐 (All the way)
Supernova (Hey-huh)

사건은 다가와 ah, oh, ayy (New star)
거세게 커져가 ah, oh, ayy
질문은 계속돼 ah, oh, ayy (Nova)
우린 어디서 왔나 oh, ayy
사건은 다가와 ah, oh, ayy (Yeah-yeah-yeah-yeah)
거세게 커져가 ah, oh, ayy (Nova)
질문은 계속돼 ah, oh, ayy (Bring the light of a dying star)

Supernova

[English translation:]

I'm like some kind of supernova
Watch out

Look at me go
Have some fun
With the core of light
So hot, hot
Open the door
Feelin' each other's presence
Like a Discord
My lookalike, who are you? (Incoming; Drop)

Event's imminent ah, oh, ayy
Blowin' up crazy ah, oh, ayy
That tick, that tick, tick bomb
That tick, that tick, tick bomb
Won't dare touch it
No one ever will
Rightnow it's inside me
Su-su-su-supernova

Nova
Can't stop hyperstellar
Seek its origin
Bring the light of a dying star
Watch this universe I've brought out
Supernova

Ah, body bang (Bang, bang, bang, bang, bang, bang)
Make it feel too right

Swept-up energy, it's so special
Cruel queen and the scene, its finale
It's massive, this explosion within me
Every one of my cells are created from stars (Under my control, ah)

Questions keep comin' ah, oh, ayy
Where did we come from oh, ayy
Feel it in me (Huh)
Su-su-su-supernova

Nova
Can't stop hyperstellar
Seek its origin
Bring the light of a dying star
Watch this universe I've brought out
Supernova

With my invisible force
Should I reach out my hand to you
All the possible possibilities
Meeting you inside infinity
It's about to bang-bang
Don't forget my name

Su-su-su-supernova

Event's imminent ah, oh, ayy
Blowin' up crazy ah, oh, ayy
Questions keep comin' ah, oh, ayy
Where did we come from oh, ayy
Event's imminent ah, oh, ayy
Blowin' up crazy ah, oh, ayy
Tell me, tell me, tell me, oh, ayy
Where did we come from oh, ayy
Where did we come from oh, ayy

Nova (Nova)
Can't stop hyperstellar (Hyperstellar)
Seek its origin
Bring the light of a dying star (Light of a dying star)
Watch this universe I've brought out (All the way)
Supernova (Hey-uh)

Event's imminent ah, oh, ayy (New star)
Blowin' up crazy ah, oh, ayy
Questions keep comin' ah, oh, ayy (Nova)
Where did we come from oh, ayy
Event's imminent ah, oh, ayy (Yeah-yeah-yeah-yeah)
Blowin' up crazy ah, oh, ayy (Nova)
Questions keep comin' ah, oh, ayy (Bring the light of a dying star)

Supernova"""),
("Savage", "aespa", "k-pop", """[Romanized:]

Oh my gosh!
Don't you know I'm a Savage?

I'm a Killa neoreul kkael ae
Ajikdo garigo hwangageul pyeolchin neo
Paella We Holler
Duryeopji ana neo neo Hit you harder

Nal mireo neoheo Deep fake on me
Junbiga andwen mudaero
Moraneoheo Fake on me
Got everybody mock up to me
Suchireul neukkige mentaleul heundeureonwa
Ssaneulhan gwanjung muneojyeo ae
Deoneun neol mot chama Say No! Yeah yeah

Dugo bwa nan jom Savage
Neoye Dirty han Play
Deoneun dugo bol su eopseo
Nareul muneotteurigo shibeun
Ne hwangakdeuri jeomjeom
Neoreul guchukhal iyuga dwae
I'm a Savage
Neol bushyeo kkae julge Oh
I'm a Savage
Neol jitbalba julge Oh

Get me get me now
Get me get me now
(Zu Zu Zu Zu)
Jigeum nareul japa
Anim nan deo Savage
(Zu Zu Zu Zu)
Get me get me now
Get me get me now
(Zu Zu Zu Zu)
Ijen naega neoreul japa
Now I'm a Savage

Gimme gimme now
Gimme gimme now
(Zu Zu Zu Zu)
Neoye mari boyeo
Ne yakjeom Algorithm
(Zu Zu Zu Zu)
Gimi gimi na
Gimi gimi na
(Zu Zu Zu Zu)
MA ae SYNK banghae malgo
Kkeojyeo Savage
(Zu Zu Zu Zu)

Mmmh Everybody looks at me
Iksukhajanhni
Yangbohae chamayaman dwae
Eoreunseureopge
I'm locked up in the glass
Nan nolgo shibeunde
Neomu kkeumjjikhan gidae
Geureon hwangak teure nareul gadweo nwa

I'm going kwangyaro Game in
Mullichyeo gyomyohan iganjil
And my aerobuteo
Meoreojige mandeul
Hweshimchan ne Trick
We gone kwangyaro Game in
Beeobeoryeo nae biche geom
Demijireul ibeun nege
Injeongsajeong bol geot eomneun punch

Geugeot bwa nan jom Savage
Neoye jaesaengnyeokeul maga
Heuteureonwa ppaenwa
Ijji mara yeogin baro kwangya
Neoye shigongganeun nae tteuttaero
Make It break it
I'm a Savage
Neol bushyeo kkae julge Oh
I'm a Savage
Neol jitbalba julge Oh

Get me get me now
Get me get me now
(Zu Zu Zu Zu)
Jigeum nareul japa
Anim nan deo Savage
(Zu Zu Zu Zu)
Get me get me now
Get me get me now
(Zu Zu Zu Zu)
Ijen naega neoreul japa
Now I'm a Savage

Gimme gimme now
Gimme gimme now
(Zu Zu Zu Zu)
Neoye mari boyeo
Ne yakjeom Algorithm
(Zu Zu Zu Zu)
Gimi gimi na
Gimi gimi na
(Zu Zu Zu Zu)
MA ae SYNK banghae malgo
Kkeojyeo Savage
(Zu Zu Zu Zu)

Wigie ppajin nal jigyeojun geon neoyeosseo
My naevis we love U
My victory hanaye SYNK DIVE
Modu nega mandeureojun gihweran geo
I know your sacrifices Oh
My naevis we love U
Ara urin bandeushi
Ne gieokdeuleul chajajulge
Urin manna kkok buhwal geudaeum

Savage
Savage
Yeah

Get me get me now
Get me get me now
(Zu Zu Zu Zu)
Jigeum nareul japa
Anim nan deo Savage
(Zu Zu Zu Zu)
Get me get me now
Get me get me now
(Zu Zu Zu Zu)
Ijen naega neoreul japa
Now I'm a Savage

Gimme gimme now
Gimme gimme now
(Zu Zu Zu Zu)
Neoye mari boyeo
Ne yakjeom Algorithm
(Zu Zu Zu Zu)
Gimi gimi na
Gimi gimi na
(Zu Zu Zu Zu)
MA ae SYNK banghae malgo
Kkeojyeo Savage
(Zu Zu Zu Zu)

Ha ha, What?

[Korean:]

Oh my gosh!
Don't you know I'm a Savage?

I'm a Killa 너를 깰 ae
아직도 가리고 환각을 펼친 너
팰라 We Holler
두렵지 않아 너 너 Hit you harder

날 밀어 넣어 Deep fake on me
준비가 안된 무대로
몰아넣어 Fake on me
Got everybody mock up to me
수치를 느끼게 멘탈을 흔들어놔
싸늘한 관중 무너져 ae
더는 널 못 참아 Say No! Yeah yeah

두고 봐 난 좀 Savage
너의 Dirty 한 Play
더는 두고 볼 수 없어
나를 무너뜨리고 싶은
네 환각들이 점점
너를 구축할 이유가 돼
I'm a Savage
널 부셔 깨 줄게 Oh
I'm a Savage
널 짓밟아 줄게 Oh

Get me get me now
Get me get me now
(Zu Zu Zu Zu)
지금 나를 잡아
아님 난 더 Savage
(Zu Zu Zu Zu)
Get me get me now
Get me get me now
(Zu Zu Zu Zu)
이젠 내가 너를 잡아
Now I'm a Savage

Gimme gimme now
Gimme gimme now
(Zu Zu Zu Zu)
너의 말이 보여
네 약점 Algorithm
(Zu Zu Zu Zu)
김이 김이 나
김이 김이 나
(Zu Zu Zu Zu)
MA ae SYNK 방해 말고
꺼져 Savage
(Zu Zu Zu Zu)

Mmmh Everybody looks at me
익숙하잖니
양보해 참아야만 돼
어른스럽게
I'm locked up in the glass
난 놀고 싶은데
너무 끔찍한 기대
그런 환각 틀에 나를 가둬 놔

I'm going 광야로 Game in
물리쳐 교묘한 이간질
And my ae로부터
멀어지게 만들
회심찬 네 Trick
We gone 광야로 Game in
베어버려 내 빛의 검
데미지를 입은 네게
인정사정 볼 것 없는 펀치

그것 봐 난 좀 Savage
너의 재생력을 막아
흐트러놔 빼놔
잊지 말아 여긴 바로 광야
너의 시공간은 내 뜻대로
Make It break it
I'm a Savage
널 부셔 깨 줄게 Oh
I'm a Savage
널 짓밟아 줄게 Oh

Get me get me now
Get me get me now
(Zu Zu Zu Zu)
지금 나를 잡아
아님 난 더 Savage
(Zu Zu Zu Zu)
Get me get me now
Get me get me now
(Zu Zu Zu Zu)
이젠 내가 너를 잡아
Now I'm a Savage

Gimme gimme now
Gimme gimme now
(Zu Zu Zu Zu)
너의 말이 보여
네 약점 Algorithm
(Zu Zu Zu Zu)
김이 김이 나
김이 김이 나
(Zu Zu Zu Zu)
MA ae SYNK 방해 말고
꺼져 Savage
(Zu Zu Zu Zu)

위기에 빠진 날 지켜준 건 너였어
My naevis we love U
My victory 하나의 SYNK DIVE
모두 네가 만들어준 기회란 거
I know your sacrifices Oh
My naevis we love U
알아 우린 반드시
네 기억들을 찾아줄게
우린 만나 꼭 부활 그다음

Savage
Savage
Yeah

Get me get me now
Get me get me now
(Zu Zu Zu Zu)
지금 나를 잡아
아님 난 더 Savage
(Zu Zu Zu Zu)
Get me get me now
Get me get me now
(Zu Zu Zu Zu)
이젠 내가 너를 잡아
Now I'm a Savage

Gimme gimme now
Gimme gimme now
(Zu Zu Zu Zu)
너의 말이 보여
네 약점 Algorithm
(Zu Zu Zu Zu)
김이 김이 나
김이 김이 나
(Zu Zu Zu Zu)
MA ae SYNK 방해 말고
꺼져 Savage
(Zu Zu Zu Zu)

Ha ha, What?

[English translation:]

Oh my gosh!
Don't you know I'm a Savage?

I'm a Killa who will break you, ae
You're still hiding and hallucinating
Beat you up, We Holler
I'm not afraid of you, you, Hit you harder

Push me in, Deep fake on me
To the unprepared stage
Corner me in, Fake on me
Got everybody mock up to me
You shake me up so that I feel ashamed
Cold spectators are collapsed, ae
I can't stand you anymore, Say No! Yeah yeah

Wait and see, I'm a little Savage
Your Dirty Play
I can't stand it any longer
You want to break me
Your hallucinations are becoming
The reasons to construct you
I'm a Savage
I'll break you into pieces Oh
I'm a Savage
I'll crush you Oh

Get me get me now
Get me get me now
(Zu Zu Zu Zu)
Get me now
Or I'll become more Savage
(Zu Zu Zu Zu)
Get me get me now
Get me get me now
(Zu Zu Zu Zu)
Now I'm going to get you
Now I'm a Savage

Gimme gimme now
Gimme gimme now
(Zu Zu Zu Zu)
I can see your words
Your weakness Algorithm
(Zu Zu Zu Zu)
Steaming, it's steaming
Steaming, it's steaming
(Zu Zu Zu Zu)
MA ae SYNK
Don't bother me and bog off, Savage
(Zu Zu Zu Zu)

Mmmh Everybody looks at me
I'm used to it
I should take a step back,
I have to endure it like an adult
I'm locked up in the glass
I want to play
Such a horrible expectation
I'm locked up in that hallucination frame

I'm going to KWANGYA, Game in
Defeating a subtle alienation
And making me drift
Apart from my ae
Your satisfying Trick
We gone KWANGYA, Game in
Cut it down, my sword of light
To you who is damaged
It's a merciless punch

See? I'm a little Savage
I block your regenerative power
I distract you, I leave you out
Don't forget, this is KWANGYA
I control your time and space
Make It break it
I'm a Savage
I'll break you into pieces Oh
I'm a Savage
I'll crush you Oh

Get me get me now
Get me get me now
(Zu Zu Zu Zu)
Get me now
Or I'll become more Savage
(Zu Zu Zu Zu)
Get me get me now
Get me get me now
(Zu Zu Zu Zu)
Now I'm going to get you
Now I'm a Savage

Gimme gimme now
Gimme gimme now
(Zu Zu Zu Zu)
I can see your words
Your weakness Algorithm
(Zu Zu Zu Zu)
Steaming, it's steaming
Steaming, it's steaming
(Zu Zu Zu Zu)
MA ae SYNK
Don't bother me and bog off, Savage
(Zu Zu Zu Zu)

You are the one who protected me when I was in trouble
My naevis we love U
My victory, one SYNK DIVE
All the opportunities you've created
I know your sacrifices Oh
My naevis we love U
I know, we'll make sure
To find your memories
Let's meet surely after the resurrection

Savage
Savage
Yeah

Get me get me now
Get me get me now
(Zu Zu Zu Zu)
Get me now
Or I'll become more Savage
(Zu Zu Zu Zu)
Get me get me now
Get me get me now
(Zu Zu Zu Zu)
Now I'm going to get you
Now I'm a Savage

Gimme gimme now
Gimme gimme now
(Zu Zu Zu Zu)
I can see your words
Your weakness Algorithm
(Zu Zu Zu Zu)
Steaming, it's steaming
Steaming, it's steaming
(Zu Zu Zu Zu)
MA ae SYNK
Don't bother me and bog off, Savage
(Zu Zu Zu Zu)

Ha ha, What?"""),
("DDU-DU DDU-DU (뚜두뚜두)", "BLACKPINK", "k-pop", """[Romanized:]

BLACKPINK!
(Ah yeah, ah yeah!)
BLACKPINK!
(Ah yeah, ah yeah!)

Ayy, chakan eolgure geureochi mothan taedo (Huh)
Ganyeorin mommae sok garyeojin volumeeun du baero (Yah, yah, double up)
Geochimeopsi jikjin guji bojin anchi nunchi (Woo!)
Black hamyeon Pink urin yeppeujanghan Savage (BLACKPINK!)
Wonhal ttaen daenoko ppaetji (Uh)
Neon mwol haedo kallo mul begi (Uh)
Du sonen gadeukan fat check
Gunggeumhamyeon haebwa fact check
Nun nopin kkokdaegi
Mul mannan mulgogi
Jom dokae nan toxic
You hokae I'm foxy

Du beon saenggakae
Heunhan namdeulcheoreom chakan cheogeun mot hanikka
Chakgakaji ma
Swipge useojuneun geon nal wihan geoya
Ajigeun jal moreugetji
Guji wonhamyeon test me
Neon bul bodeusi ppeonhae
Manmanhan geol wonhaetdamyeon
Oh, wait 'til I do what I-

Hit you with that ddu-du, ddu-du, du
(Ah yeah, ah yeah!)
Hit you with that ddu-du, ddu-du, du
(Ah yeah, ah yeah!)
Ddu-du, du-du-du-du-du

(Hit you with that, hit you with that, hit you with that)
BLACKPINK!

Jigeum naega georeoganeun georin
BLACKPINK four-way sageori
Dongseonambuk sabangeuro run it
Neone beokitriseuteu ssak da I bought it
Neol danggineun geotdo meolli milchineun geotdo
Jemeotdaero haneun bad girl
Jokeon sileohageon nuga mwora hadeon
When the bass drop, it's another banger

Du beon saenggakae
Heunhan namdeulcheoreom chakan cheogeun mot hanikka
Chakgakaji ma
Swipge useojuneun geon nal wihan geoya
Ajigeun jal moreugetji
Guji wonhamyeon test me
Neon bul bodeusi ppeonhae
Manmanhan geol wonhaetdamyeon
Oh, wait 'til I do what I-

Hit you with that ddu-du, ddu-du, du
(Ah yeah, ah yeah)
Hit you with that ddu-du, ddu-du, du
(Ah yeah, ah yeah)
Ddu-du, du-du-du-du-du

What you gonna do when I
Come, come through with that, that, uh (Uh-huh)
What you gonna do when I
Come, come through with that, that, uh (Uh-huh)
Tteugeowo, tteugeowo, tteugeowo like fire (Fire)
(Ddu-du, du-du-du-du-du, ddu-du, du-du-du-du-du)
Tteugeowo, tteugeowo, tteugeowo like fire (Fire)
(Ddu-du, du-du-du-du-du, ddu-du, du-du-du-du-du)

BLACKPINK! (Hey!)
(Ddu-du, du-du-du-du, du-du-du-du)
(Ah yeah, ah yeah, ah yeah, ah yeah!)
Tteugeowo, tteugeowo, tteugeowo like fire (Hey!)
Tteugeowo, tteugeowo, tteugeowo like fire

Hit you with that ddu-du, ddu-du, du

[Korean:]

BLACKPINK!
(Ah yeah, ah yeah!)
BLACKPINK!
(Ah yeah, ah yeah!)

Ayy, 착한 얼굴에 그렇지 못한 태도 (Huh)
가녀린 몸매 속 가려진 volume은 두 배로 (Yah, yah, double up)
거침없이 직진 굳이 보진 않지 눈치 (Woo!)
Black 하면 Pink 우린 예쁘장한 Savage (BLACKPINK!)
원할 땐 대놓고 뺏지 (Uh)
넌 뭘 해도 칼로 물 베기 (Uh)
두 손엔 가득한 fat check
궁금하면 해봐 fact check
눈 높인 꼭대기
물 만난 물고기
좀 독해 난 toxic
You 혹해 I'm foxy

두 번 생각해
흔한 남들처럼 착한 척은 못 하니까
착각하지 마
쉽게 웃어주는 건 날 위한 거야
아직은 잘 모르겠지
굳이 원하면 test me
넌 불 보듯이 뻔해
만만한 걸 원했다면
Oh, wait 'til I do what I-

Hit you with that ddu-du, ddu-du, du
(Ah yeah, ah yeah!)
Hit you with that ddu-du, ddu-du, du
(Ah yeah, ah yeah!)
Ddu-du, du-du-du-du-du

(Hit you with that, hit you with that, hit you with that)
BLACKPINK!

지금 내가 걸어가는 거린
BLACKPINK four-way 사거리
동서남북 사방으로 run it
너네 버킷리스트 싹 다 I bought it
널 당기는 것도 멀리 밀치는 것도
제멋대로 하는 bad girl
좋건 싫어하건 누가 뭐라 하던
When the bass drop, it's another banger

두 번 생각해
흔한 남들처럼 착한 척은 못 하니까
착각하지 마
쉽게 웃어주는 건 날 위한 거야
아직은 잘 모르겠지
굳이 원하면 test me
넌 불 보듯이 뻔해
만만한 걸 원했다면
Oh, wait 'til I do what I-

Hit you with that ddu-du, ddu-du, du
(Ah yeah, ah yeah)
Hit you with that ddu-du, ddu-du, du
(Ah yeah, ah yeah)
Ddu-du, du-du-du-du-du

What you gonna do when I
Come, come through with that, that, uh (Uh-huh)
What you gonna do when I
Come, come through with that, that, uh (Uh-huh)
뜨거워, 뜨거워, 뜨거워 like fire (Fire)
(Ddu-du, du-du-du-du-du, ddu-du, du-du-du-du-du)
뜨거워, 뜨거워, 뜨거워 like fire (Fire)
(Ddu-du, du-du-du-du-du, ddu-du, du-du-du-du-du)

BLACKPINK! (Hey!)
(Ddu-du, du-du-du-du, du-du-du-du)
(Ah yeah, ah yeah, ah yeah, ah yeah!)
뜨거워, 뜨거워, 뜨거워 like fire (Hey!)
뜨거워, 뜨거워, 뜨거워 like fire

Hit you with that ddu-du, ddu-du, du

[English translation:]

BLACKPINK!
(Ah yeah, ah yeah!)
BLACKPINK!
(Ah yeah, ah yeah!)

I may look sweet, but I don't act like it (Huh)
My slender figure hides twice the volume (Yah, yah, double up)
I give it to them straight, I don't care what people think (Woo!)
If it's black, then it's pink, we are pretty savage (BLACKPINK!)
When we want, we'll steal outright (Uh)
Whatever you do, it's like cutting water with a knife (Uh)
Our hands are full with a fat check
If you're curious, fact check
Expectations higher
Just like fish in the water
I'm a little toxic
You've fallen for me, I'm Foxy

Think twice
I can't act nice like other people
Don't be mistaken
I only smile easily for myself
You may not know well yet
If you want, then test me
You're so predictable
If you wanted something easy
Oh, wait 'til I do what I-

Hit you with that ddu-du, ddu-du, du
(Ah yeah, ah yeah!)
Hit you with that ddu-du, ddu-du, du
(Ah yeah, ah yeah!)
Ddu-du, du-du-du-du-du

(Hit you with that, hit you with that, hit you with that)
BLACKPINK!

The path I walk now
BLACKPINK four-way intersection
North, South, East, West, all ways run it
All of your bucket list, I bought it
Pulling you and pushing you far away
I do it however I want because I'm a bad girl
Whether you like me or hate me or whatever anyone says
When the bass drop, it's another banger

Think twice
I can't act nice like other people
Don't be mistaken
I only smile easily for myself
You may not know well yet
If you want, then test me
You're so predictable
If you wanted something easy
Oh, wait 'til I do what I-

Hit you with that ddu-du, ddu-du, du
(Ah yeah, ah yeah!)
Hit you with that ddu-du, ddu-du, du
(Ah yeah, ah yeah!)
Ddu-du, du-du-du-du-du

What you gonna do when I
Come, come through with that, that, uh (Uh-huh)
What you gonna do when I
Come, come through with that, that, uh (Uh-huh)
Hot, hot, hot like fire (Fire)
(Ddu-du, du-du-du-du-du, ddu-du, du-du-du-du-du)
Hot, hot, hot like fire (Fire)
(Ddu-du, du-du-du-du-du, ddu-du, du-du-du-du-du)

BLACKPINK! (Hey!)
(Ddu-du, du-du-du-du, du-du-du-du)
(Ah yeah, ah yeah, ah yeah, ah yeah!)
Hot, hot, hot like fire (Hey!)
Hot, hot, hot like fire

Hit you with that ddu-du, ddu-du, du"""),
("BOOMBAYAH (붐바야)", "BLACKPINK", "k-pop", """[Romanized:]

BLACKPINK in your area
BLACKPINK in your area

Been a bad girl, I know I am
And I'm so hot, I need a fan
I don't want a boy, I need a man

Click-clack
Badda bing badda boom
Muneul bakchamyeon modu nal barabom
Gudi aesseo noryeok an haedo
Modeun namjadeuleun kopiga pangpangpang
Pangpang parapara pangpangpang
Jigeum nal wihan chukbaereul jjanjjanjjan
Hands up nae sonen
Bottle full o' henny
Nega malloman deuddeon gyaega naya Jennie

Chumchuneun bulbicheun nal gamssago done
Black to the pink
Eodiseodeun teukbyeolhae Oh yes
Chyeoda bodeun maldeun I wanna dance
Like ttaradaradanttan
Ttaradaradanttan ttudurubbau

Joha i bunwigiga joha
Joha nan jigeum nega joha
Jeongmal banhaesseo oneul bam
Neowa chumchugo sipeo

BOOMBAYAH
YAH YAH YAH BOOMBAYAH
YAH YAH YAH BOOMBAYAH
YAH YAH YAH YAH
BOOM BOOM BA BOOM
BOOM BA oppa
YAH YAH YAH YAH YAH YAH
YAH YAH YAH YAH
YAH YAH YAH YAH YAH YAH
YAH YAH YAH YAH oppa
YAH YAH YAH YAH YAH YAH
YAH YAH YAH YAH
YAH YAH YAH YAH YAH YAH
YAH BOOM BOOM BA
BOOMBAYAH

BLACKPINK in your area

Ije dallyeoyaji mwol eotteokhae
Nan cheol eobseo geob eobseo Man
Middle finger up, F U pay me
90s baby, I pump up the jam
Dallyeobwa dallyeobwa oppaya LAMBO
Oneuleun neowa na jeolmeumeul GAMBLE
Gamhi nal makjima hoksina nuga nal makado
I'm gonna go brrrr RAMBO

Ne soni nae heorireul gamssago done
Front to my back
Nae mommaeneun teukbyeolhae Oh yes
Ne nunbicheun I know you wanna touch
Like touch touch touch
Touch ttudurubbau

Joha i bunwigiga joha
Joha nan jigeum nega joha
Jeongmal meosisseo oneul bam
Neowa chumchugo sipeo

BOOMBAYAH
YAH YAH YAH BOOMBAYAH
YAH YAH YAH BOOMBAYAH
YAH YAH YAH YAH
BOOM BOOM BA
BOOM BOOM BA oppa
YAH YAH YAH YAH YAH
YAH YAH YAH YAH YAH
YAH YAH YAH YAH YAH
YAH YAH YAH YAH YAH oppa
YAH YAH YAH YAH YAH
YAH YAH YAH YAH YAH
YAH YAH YAH YAH YAH
YAH YAH BOOM BOOM BA
BOOMBAYAH

Oneuleun maen jeongsin ttawin beorigo
Haneuleul neomeoseo olla gal geoya
Kkeuteul moreuge ppalli dalligo sipeo
Let's go, let's go

Oneuleun maen jeongsin ttawin beorigo
Haneuleul neomeoseo olla gal geoya
Kkeuteul moreuge ppalli dalligo sipeo
Let's go, let's go

[Korean:]

BLACKPINK in your area
BLACKPINK in your area

Been a bad girl, I know I am
And I'm so hot, I need a fan
I don't want a boy, I need a man

Click-clack
Badda bing badda boom
문을 박차면 모두 날 바라봄
굳이 애써 노력 안 해도
모든 남자들은 코피가 팡팡팡
팡팡 파라파라 팡팡팡
지금 날 위한 축배를 짠짠짠
Hands up 내 손엔
Bottle full o' henny
네가 말로만 듣던 걔가 나야 Jennie

춤추는 불빛은 날 감싸고 도네
Black to the pink
어디서든 특별해 Oh yes
쳐다 보든 말든 I wanna dance
Like 따라다라단딴
따라다라단딴 뚜두룹바우

좋아 이 분위기가 좋아
좋아 난 지금 네가 좋아
정말 반했어 오늘 밤
너와 춤추고 싶어

BOOMBAYAH
YAH YAH YAH BOOMBAYAH
YAH YAH YAH BOOMBAYAH
YAH YAH YAH YAH
BOOM BOOM BA BOOM
BOOM BA 오빠
YAH YAH YAH YAH YAH YAH
YAH YAH YAH YAH
YAH YAH YAH YAH YAH YAH
YAH YAH YAH YAH 오빠
YAH YAH YAH YAH YAH YAH
YAH YAH YAH YAH
YAH YAH YAH YAH YAH YAH
YAH BOOM BOOM BA
BOOMBAYAH

BLACKPINK in your area

이제 달려야지 뭘 어떡해
난 철 없어 겁 없어 Man
Middle finger up, F U pay me
90s baby, I pump up the jam
달려봐 달려봐 오빠야 LAMBO
오늘은 너와 나 젊음을 GAMBLE
감히 날 막지마 혹시나 누가 날 막아도
I'm gonna go brrrr RAMBO

네 손이 내 허리를 감싸고 도네
Front to my back
내 몸매는 특별해 Oh yes
네 눈빛은 I know you wanna touch
Like touch touch touch
Touch 뚜두룹바우

좋아 이 분위기가 좋아
좋아 난 지금 네가 좋아
정말 멋있어 오늘 밤
너와 춤추고 싶어

BOOMBAYAH
YAH YAH YAH BOOMBAYAH
YAH YAH YAH BOOMBAYAH
YAH YAH YAH YAH
BOOM BOOM BA
BOOM BOOM BA 오빠
YAH YAH YAH YAH YAH
YAH YAH YAH YAH YAH
YAH YAH YAH YAH YAH
YAH YAH YAH YAH YAH 오빠
YAH YAH YAH YAH YAH
YAH YAH YAH YAH YAH
YAH YAH YAH YAH YAH
YAH YAH BOOM BOOM BA
BOOMBAYAH

오늘은 맨 정신 따윈 버리고
하늘을 넘어서 올라 갈 거야
끝을 모르게 빨리 달리고 싶어
Let's go, let's go

오늘은 맨 정신 따윈 버리고
하늘을 넘어서 올라 갈 거야
끝을 모르게 빨리 달리고 싶어
Let's go, let's go

[English translation:]

BLACKPINK in your area
BLACKPINK in your area

Been a bad girl, I know I am
And I'm so hot, I need a fan
I don't want a boy, I need a man

Click-clack
Badda bing badda boom
When I kick open the door, they all look at me
Even if I don't try that hard
All guys get nosebleeds, pangpangpang
Pangpang parapara pangpangpang
A toast for me right now, clink, clink, clink
Hands up, in my hands there's a
Bottle full o' henny
The girl you've always heard about, that's me, Jennie

The dancing light wraps around me
Black to the pink
Wherever I am, I'm special, oh yes
Don't care if you look or not, I wanna dance
Like ttaradaradanttan
Ttaradaradanttan ttudurubbau

I like it, I like this atmosphere
I like it, I like you right now
I'm falling for you tonight
I wanna dance with you

BOOMBAYAH
YAH YAH YAH BOOMBAYAH
YAH YAH YAH BOOMBAYAH
YAH YAH YAH YAH
BOOM BOOM BA BOOM
BOOM BA oppa
YAH YAH YAH YAH YAH YAH
YAH YAH YAH YAH
YAH YAH YAH YAH YAH YAH
YAH YAH YAH YAH oppa
YAH YAH YAH YAH YAH YAH
YAH YAH YAH YAH
YAH YAH YAH YAH YAH YAH
YAH BOOM BOOM BA
BOOMBAYAH

BLACKPINK in your area

Have to run now, what else would I do
I'm immature, I have no fear, man
Middle finger up, F U pay me
90s baby, I pump up the jam
Run, run, oppa LAMBO
Today, you and I are gambling with youth
Don't you dare stop me, even if someone tries
I'm gonna go brrrr RAMBO

Your hands wrap around my waist
Front to my back
My body is special oh yes
Your eyes say I know you wanna touch
Like touch touch touch
Touch ttudurubbau

I like it, I like this atmosphere
I like it, I like you right now
This night is awesome
I wanna dance with you

BOOMBAYAH
YAH YAH YAH BOOMBAYAH
YAH YAH YAH BOOMBAYAH
YAH YAH YAH YAH
BOOM BOOM BA
BOOM BOOM BA oppa
YAH YAH YAH YAH YAH
YAH YAH YAH YAH YAH
YAH YAH YAH YAH YAH
YAH YAH YAH YAH YAH oppa
YAH YAH YAH YAH YAH
YAH YAH YAH YAH YAH
YAH YAH YAH YAH YAH
YAH YAH BOOM BOOM BA
BOOMBAYAH

Let's not be sober today
We're going higher than the sky
I wanna go fast, without knowing the end
Let's go, let's go

Let's not be sober today
We're going higher than the sky
I wanna go fast, without knowing the end
Let's go, let's go"""),
("How You Like That", "BLACKPINK", "k-pop", """[Romanized:]

BLACKPINK in your area

Boran deushi muneojeosseo
Badageul ttulko jeo jihalkkaji
Ot kkeutjarak japgettago
Jeo nopi du soneul ppeodeobwado

Dashi kamkamhan igose Light up the sky
Ni du nuneul bomyeo I'll kiss you goodbye
Shilkeot biuseora kkoljoeunikka
Ije neohi hana dul set

Ha how you like that?
You gon' like that that that that that
That that that that
How you like that? (Barabim barabum bumbum)
How you like that that that that that
That that that that

Now look at you now look at me
Look at you now look at me
Look at you now look at me
How you like that
Now look at you now look at me
Look at you now look at me
Look at you now look at me
How you like that

Your girl need it all and that's a hundred
Baek gae junge baek nae mokseul weonhae
Karma come and get some
Ttakajiman eojjeol su eopjana
What's up, I'm right back
Bangaswereul cock back
Plain Jane get hijacked
Don't like me? Then tell me how you like that, like that

Deo kamkamhan igose Shine like the stars
Geu misoreul ttimyeo I'll kiss you goodbye
Shilkeot biuseora kkoljoeunikka
Ije neohi hana dul set

Ha how you like that?
You gon' like that that that that that
That that that that
How you like that? (Barabim barabum bumbum)
How you like that that that that that
That that that that

Now look at you now look at me
Look at you now look at me
Look at you now look at me
How you like that
Now look at you now look at me
Look at you now look at me
Look at you now look at me
How you like that

Nalgae ireun chaero churakaetteon nal
Eoduun nanal soge gacheo itteon nal
Geuttaejjeume neon nal kkeunnaeya haesseo
Look up in the sky it's a bird it's a plane

Bring out your boss bitch
BLACKPINK!

(Dumdumdum dururu dumdumdum dururu)
How you like that
(Dumdumdum dururu dumdumdum durururu)
You gon' like that
(Dumdumdum dururu dumdumdum dururu)
How you like that
(Dumdumdum dururu dumdumdum durururu)

[Korean:]

BLACKPINK in your area

보란 듯이 무너졌어
바닥을 뚫고 저 지하까지
옷 끝자락 잡겠다고
저 높이 두 손을 뻗어봐도

다시 캄캄한 이곳에 Light up the sky
니 두 눈을 보며 I'll kiss you goodbye
실컷 비웃어라 꼴좋으니까
이제 너희 하나 둘 셋

Ha how you like that?
You gon' like that that that that that
That that that that
How you like that? (Barabim barabum bumbum)
How you like that that that that that
That that that that

Now look at you now look at me
Look at you now look at me
Look at you now look at me
How you like that
Now look at you now look at me
Look at you now look at me
Look at you now look at me
How you like that

Your girl need it all and that's a hundred
백 개 중에 백 내 몫을 원해
Karma come and get some
딱하지만 어쩔 수 없잖아
What's up, I'm right back
방아쇠를 Cock back
Plain Jane get hijacked
Don't like me? Then tell me how you like that, like that

더 캄캄한 이곳에 Shine like the stars
그 미소를 띠며 I'll kiss you goodbye
실컷 비웃어라 꼴좋으니까
이제 너희 하나 둘 셋

Ha how you like that?
You gon' like that that that that that
That that that that
How you like that? (Barabim barabum bumbum)
How you like that that that that that
That that that that

Now look at you now look at me
Look at you now look at me
Look at you now look at me
How you like that
Now look at you now look at me
Look at you now look at me
Look at you now look at me
How you like that

날개 잃은 채로 추락했던 날
어두운 나날 속에 갇혀 있던 날
그때쯤에 넌 날 끝내야 했어
Look up in the sky it's a bird it's a plane

Bring out your boss bitch
BLACKPINK!

(Dumdumdum dururu dumdumdum dururu)
How you like that
(Dumdumdum dururu dumdumdum durururu)
You gon' like that
(Dumdumdum dururu dumdumdum dururu)
How you like that
(Dumdumdum dururu dumdumdum durururu)

[English translation:]

BLACKPINK in your area

I crumbled before your eyes
Hit rock bottom and sunk deeper
To grab onto the last bit of hope
I've tried to reach out with both of my hands

Again in this dark place, light up the sky
While looking into your eyes, I'll kiss you goodbye
Laugh all you want while you still can
Because it's about to be your turn 1, 2, 3

Ha how you like that?
You gon' like that that that that that
That that that that
How you like that?
How you like that that that that that
That that that that

Now look at you now look at me
Look at you now look at me
Look at you now look at me
How you like that
Now look at you now look at me
Look at you now look at me
Look at you now look at me
How you like that

Your girl need it all and that's a hundred
10 out of 10 I want what's mine
Karma come and get some
I feel bad but there's nothing I can do
Whats up I'm right back
Cock back the trigger
Plain Jane get hijacked
Don't like me? Then tell me how you like that, like that

In this even darker place shine like the stars
With a smile on my face I'll kiss you goodbye
Laugh all you want while you still can
Because it's about to be your turn 1, 2, 3

Ha how you like that?
You gon' like that that that that that
That that that that
How you like that?
How you like that that that that that
That that that that

Now look at you now look at me
Look at you now look at me
Look at you now look at me
How you like that
Now look at you now look at me
Look at you now look at me
Look at you now look at me
How you like that

The day I fell without my wings
Those dark days where I was trapped
You should've ended me when you had the chance
Look up in the sky it's a bird it's a plane

Bring out your boss bitch
BLACKPINK!

(Dumdumdum dururu dumdumdum dururu)
How you like that
(Dumdumdum dururu dumdumdum durururu)
You gon' like that
(Dumdumdum dururu dumdumdum dururu)
How you like that
(Dumdumdum dururu dumdumdum durururu)"""),
("Kill This Love", "BLACKPINK", "k-pop", """[Romanized:]

Yeah, yeah, yeah
BLACKPINK IN YOUR AREA!
Yeah, yeah, yeah

Cheonsa gateun Hi kkeuten akma gateun bye
Maebeon michildeushan High dwien baeteoya haneun Price
Igeon dabi eopsneun Test maebeon sokdeorado Yes
Ttakhan gamjeongui noye
Eoreo jugeul saranghae

Here I come kick in the door
Gajang dokhan geollo jwo
Ppeonhadi ppeonhan geu love
Deo naenwabwa give me some more
Araseo maedallyeo byeorang kkeute
Hanmadimyeon tto like hebeolle hae
Geu ttatteushan tteollimi saeppalgan seollemi
Machi heaven gatgessjiman
You might not get in it

Look at me, look at you nuga deo apeulkka?
You smart nuga? You are
Du nune pinunmul heureuge doendamyeon
So sorry nuga? You are
Na eotteokhae nayakhan nal gyeondil su eopseo
Aesseo du nuneul garin chae
Sarangui sumtongeul kkeunheoyagesseo

Let's kill this love!
Yeah, yeah, yeah, yeah, yeah
Rum, pum, pum, pum, pum, pum, pum
Let's kill this love!
Rum, pum, pum, pum, pum, pum, pum

Feelin' like a sinner
It's so fire with him I go boo hoo
He said you look crazy
Thank you baby
I owe it all to you
Got me all messed up
His love is my favorite
But you plus me sadly can be dangerous

Lucky me, lucky you
Gyeolgugen geojismal we lie
So what so what
Manyage naega neol jiuge
Doendamyeon So sorry
I'm not sorry
Na eotteokhae nayakhan nal gyeondil su eopseo
Aesseo nunmureul gamchun chae
Sarangui sumtongeul kkeunheoyagesseo

Let's kill this love!
Yeah, yeah, yeah, yeah, yeah
Rum, pum, pum, pum, pum, pum, pum
Let's kill this love!
Rum, pum, pum, pum, pum, pum, pum

We all commit to love
That makes you cry
We're all making love
That kills you inside

We must kill this love
Yeah, it's sad but true
Gotta kill this love
Before it kills you too
Kill this love
Yeah, it's sad but true
Gotta kill this love, gotta kill
Let's kill this love!

[Korean:]

Yeah, yeah, yeah
BLACKPINK IN YOUR AREA!
Yeah, yeah, yeah

천사 같은 "hi" 끝엔 악마 같은 "bye"
매번 미칠듯한 high 뒤엔 뱉어야
하는 price
이건 답이 없는 test
매번 속더라도 yes
딱한 감정의 노예
얼어 죽을 사랑해

Here I come kick in the door
가장 독한 걸로 줘
뻔하디 뻔한 그 love
더 내놔봐 give me some more
알아서 매달려 벼랑 끝에
한마디면 또 like 헤벌레 해
그 따뜻한 떨림이 새빨간 설렘이
마치 heaven 같겠지만
You might not get in it

Look at me, look at you
누가 더 아플까
You smart 누가 you are
두 눈에 피눈물 흐르게 된다면
So sorry 누가 you are
나 어떡해 나약한 날 견딜 수 없어
애써 두 눈을 가린 채
사랑의 숨통을 끊어야겠어

Let's kill this love!
Yeah, yeah, yeah
Rum, pum, pum, pum, pum, pum, pum
Let's kill this love!
Rum, pum, pum, pum, pum, pum, pum

Feelin' like a sinner
It's so fire with him I go boo hoo
He said you look crazy
Thank you baby
I owe it all to you
Got me all messed up
His love is my favorite
But you plus me
Sadly can be dangerous

Lucky me, lucky you
결국엔 거짓말 we lie
So what? So what?
만약에 내가 널 지우게
된다면 so sorry
I'm not sorry
나 어떡해 나약한 날 견딜 수 없어
애써 눈물을 감춘 채, eh
사랑의 숨통을 끊어야겠어

Let's kill this love!
Yeah, yeah, yeah, yeah, yeah
Rum, pum, pum, pum, pum, pum, pum
Let's kill this love!
Rum, pum, pum, pum, pum, pum, pum

We all commit to love
That makes you cry, oh oh
We're all making love
That kills you inside, yeah

We must kill this love (Yeah, yeah)
Yeah, it's sad but true
Gotta kill this love (Yeah, yeah)
Before it kills you too
Kill this love (Yeah, yeah)
Yeah, it's sad but true
Gotta kill this love, gotta kill
Let's kill this love!

[English translation:]

Yeah, yeah, yeah
BLACKPINK IN YOUR AREA!
Yeah, yeah, yeah

After a sweet "hi", there's always a bitter "bye"
After every crazy high, there's a price you have to pay
There's no answer to this test I'll always fall for it yes
I'm a slave to my emotions
Screw this heartless love

Here I come kick in the door
Give me the strongest one
So obvious, that love
Give me more, give me some more
Cling onto the edge of the cliff if you want
With just one word you're like starstruck again
That warm nervous feeling, extreme excitement
Felt like heaven but you might not get in it

Look at me, look at you, who will be in more pain?
You smart like who? You are
If you cry tears of blood from both eyes
So sorry like who? You are
What should I do, I can't stand myself being so weak
While I force myself to cover my eyes
I need to bring an end to this love

Let's kill this love!
Yeah, yeah, yeah, yeah, yeah
Rum, pum, pum, pum, pum, pum, pum
Let's kill this love!
Rum, pum, pum, pum, pum, pum, pum

Feelin' like a sinner
It's so fire with him I go boo hoo
He said you look crazy
Thank you baby
I owe it all to you
Got me all messed up
His love is my favorite
But you plus me
Sadly can be dangerous

Lucky me, lucky you
After all, in the end we lie
So what? So what?
If I end up forgetting you
So sorry
I'm not sorry
What should I do? I can't stand myself being so weak
While I force myself to hide my tears
I need to bring an end to this love

Let's kill this love!
Yeah, yeah, yeah, yeah, yeah
Rum, pum, pum, pum, pum, pum, pum
Let's kill this love!
Rum, pum, pum, pum, pum, pum, pum

We all commit to love
That makes you cry, oh, oh
We're all making love
That kills you inside, yeah

We must kill this love (Yeah, yeah)
Yeah, it's sad but true
Gotta kill this love (Yeah, yeah)
Before it kills you too
Kill this love (Yeah, yeah)
Yeah, it's sad but true
Gotta kill this love, gotta kill
Let's kill this love!"""),
("Forever Young", "BLACKPINK", "k-pop", """[Romanized:]

[Jennie:]
Tteonaji ma just stay
Jigeum I siganeul meomchun chae
Neowa hamkkeramyeon nan
I could die in this moment

[Rosé:]
Forever young
Forever young
Forever young
Forever young

[Jisoo:]
Neoui nune bichin naui moseubi
Neul cheoeum mannan geu nalman gatgil
Sori eopsi taoreuneun bulkkotgachi
Majimakcheoreom nae ip matchugil

[Rosé:]
Dalbit arae nae maeumeun seolle
Eunhasuro chumchureo gallae let's go
Jigeum let go

[Lisa:]
Oneuri gado huhoe eopge
Sigani uri dureul tteeo noeul su eopge
Sungani yeongwonhal su itge

[Jennie:]
Neon nae maeume bureul jilleojwo
Huhoe eomneun jeoleumi taoreuge

[Rosé:]
Jigeumcheoreom neowa hamkkeramyeon tonight
I could die in this moment

[Jennie:]
Forever young
Forever young
Forever young
Forever young

[Lisa:]
Maeilmaeil bam bam
I noraereul bulleo bulleo
Know we got that bomb bomb
Come again come again

[Jennie:]
Forever young boy so we ride or die
Kkeuchi eopseul geotcheoreom dallyeo neowa na
Bulgeun sunset arae neoneun jigeum nae yeope
Pinked out or murdered out like it ain't no thing
Da pillyo eopseo juingongeun uri
Say life's a bish? But mine's a movie
Nae Diamondcheoreom we'll shine together
Whenever wherever forever ever ever

[Jisoo:]
Jjarithage deo wiheomhage
Sesang jeo kkeutkkaji gabollae let's go
Jigeum let go

[Lisa:]
Oneuri gado huhoe eopge
Sigani uri dureul tteeo noeul su eopge
Sungani yeongwonhal su itge

[Rosé:]
Neon nae maeume bureul jilleojwo
Huhoe eomneun jeoleumi taoreuge

[Jennie:]
Sesang mueotdo duryeopji ana tonight
I could die in this moment

[Rosé:]
Forever young

[Rosé:]
Dari tteugo byeori tteumyeon chumchuneun body
Kkeuchi eopsi dallyeoboja we like to party
Dari tteugo byeori tteumyeon chumchuneun body
Kkeuchi eopsi dallyeoboja we like to party

[Lisa:]
Girls wanna have some fun
We go dumb dumb dumb
Girls wanna have some fun
What you want want want

Girls wanna have some fun
We go dumb dumb dumb
Girls wanna have some fun
We ain't done done done

Whatta bum bum whatta bum bum
Whatta bum bum whatta bum bum

[Korean:]

[Jennie:]
떠나지 마 just stay
지금 이 시간을 멈춘 채
너와 함께라면 난
I could die in this moment

[Rosé:]
Forever young
Forever young
Forever young
Forever young

[Jisoo:]
너의 눈에 비친 나의 모습이
늘 처음 만난 그 날만 같길
소리 없이 타오르는 불꽃같이
마지막처럼 내 입 맞추길

[Rosé:]
달빛 아래 내 마음은 설레
은하수로 춤추러 갈래 let's go
지금 let go

[Lisa:]
오늘이 가도 후회 없게
시간이 우리 둘을 떼어 놓을 수 없게
순간이 영원할 수 있게

[Jennie:]
넌 내 마음에 불을 질러줘
후회 없는 젊음이 타오르게

[Rosé:]
지금처럼 너와 함께라면 tonight
I could die in this moment

[Jennie:]
Forever young
Forever young
Forever young
Forever young

[Lisa:]
매일매일 밤 밤
이 노래를 불러 불러
Know we got that bomb bomb
Come again come again

[Jennie:]
Forever young boy so we ride or die
끝이 없을 것처럼 달려 너와 나
붉은 sunset 아래 너는 지금 내 옆에
Pinked out or murdered out like it ain't no thing
다 필요 없어 주인공은 우리
Say life's a bish? But mine's a movie
내 Diamond처럼 we'll shine together
Whenever wherever forever ever ever

[Jisoo:]
짜릿하게 더 위험하게
세상 저 끝까지 가볼래 let's go
지금 let go

[Lisa:]
오늘이 가도 후회 없게
시간이 우리 둘을 떼어 놓을 수 없게
순간이 영원할 수 있게

[Rosé:]
넌 내 마음에 불을 질러줘
후회 없는 젊음이 타오르게

[Jennie:]
세상 무엇도 두렵지 않아 tonight
I could die in this moment

[Rosé:]
Forever young

[Rosé:]
달이 뜨고 별이 뜨면 춤추는 body
끝이 없이 달려보자 we like to party
달이 뜨고 별이 뜨면 춤추는 body
끝이 없이 달려보자 we like to party

[Lisa:]
Girls wanna have some fun
We go dumb dumb dumb
Girls wanna have some fun
What you want want want

Girls wanna have some fun
We go dumb dumb dumb
Girls wanna have some fun
We ain't done done done

Whatta bum bum whatta bum bum
Whatta bum bum whatta bum bum"""),
("WANNABE", "ITZY", "k-pop", """[Romanized:]

Jansorineun Stop it araseo halge
Naega mwoga doedeun naega araseo hal tenikka jom
I do what I wanna
Pyeongbeomhage saldeun maldeun naebeoryeo dullae?
Eochapi naega sara nae insaeng naegeonikka
I'm so bad bad charari igijeogillae
Nunchi boneura chakan cheok sangcheobanneun geotboda baekbeon naa
I'm just on my way ganseobeun No No hae
Malhaebeoriljido molla neona jalharago

Nuga mwora haedo nan naya nan geunyang naega doego sipeo
I wanna be me, me, me
Guji mwonga doel pillyoneun eopseo nan geunyang nail ttae wanbyeokanikka
I wanna be me, me, me

I don't wanna be somebody
Just wanna be me, be me
I wanna be me, me, me
I don't wanna be somebody
Just wanna be me, be me
I wanna be me, me, me

Errbody errbody errbody teachin' me (All eyes on me)
Iraera jeoraera modu hanmadissik (Don't touch me)
Ah yeah yeah yeah yeah yeah nae apgarimeun naega hae
I'mma do my thang, Just do your thang
Cuz I'm the one & only
Saramdeureun nam mal hagireul joahae
Namui insaenge mwon gwansimi mana wae
Jeogi mianhajiman singyeong jom kkeojullaeyo

It's none of your business
I do my own business

Nuga mwora haedo nan naya nan geunyang naega doego sipeo
I wanna be me, me, me
Guji mwonga doel pillyoneun eopseo nan geunyang nail ttae wanbyeokanikka
I wanna be me, me, me

No matter if you love me or hate me
I wanna be me
One and only me
If you feel me, turn this beat up
I wanna be me, me, me

Nuga mwora haedo nan naya nan geunyang naega doego sipeo
I wanna be me, me, me
Guji mwonga doel pillyoneun eopseo nan geunyang nail ttae wanbyeokanikka
I wanna be me, me, me

I don't wanna be somebody
Just wanna be me, be me
I wanna be me, me, me
I don't wanna be somebody
Just wanna be me, be me
I wanna be me, me, me

[Korean:]

잔소리는 Stop it 알아서 할게
내가 뭐가 되든 내가 알아서 할 테니까 좀
I do what I wanna
평범하게 살든 말든 내버려 둘래?
어차피 내가 살아 내 인생 내거니까
I'm so bad bad 차라리 이기적일래
눈치 보느라 착한 척 상처받는 것보다 백번 나아
I'm just on my way 간섭은 No No 해
말해버릴지도 몰라 너나 잘하라고

누가 뭐라 해도 난 나야 난 그냥 내가 되고 싶어
I wanna be me, me, me
굳이 뭔가 될 필요는 없어 난 그냥 나일 때 완벽하니까
I wanna be me, me, me

I don't wanna be somebody
Just wanna be me, be me
I wanna be me, me, me
I don't wanna be somebody
Just wanna be me, be me
I wanna be me, me, me

Errbody errbody errbody teachin' me (All eyes on me)
이래라 저래라 모두 한마디씩 (Don't touch me)
Ah yeah yeah yeah yeah yeah 내 앞가림은 내가 해
I'mma do my thang, Just do your thang
Cuz I'm the one & only
사람들은 남 말 하기를 좋아해
남의 인생에 뭔 관심이 많아 왜
저기 미안하지만 신경 좀 꺼줄래요

It's none of your business
I do my own business

누가 뭐라 해도 난 나야 난 그냥 내가 되고 싶어
I wanna be me, me, me
굳이 뭔가 될 필요는 없어 난 그냥 나일 때 완벽하니까
I wanna be me, me, me

No matter if you love me or hate me
I wanna be me
One and only me
If you feel me, turn this beat up
I wanna be me, me, me

누가 뭐라 해도 난 나야 난 그냥 내가 되고 싶어
I wanna be me, me, me
굳이 뭔가 될 필요는 없어 난 그냥 나일 때 완벽하니까
I wanna be me, me, me

I don't wanna be somebody
Just wanna be me, be me
I wanna be me, me, me
I don't wanna be somebody
Just wanna be me, be me
I wanna be me, me, me

[English translation:]

The nagging, stop it I got this
Whatever I be it's up to me so please
I do what I wanna
Can you just leave me alone whether I live a normal life or not
It's me who lives this 'cause it's my life
I'm so bad bad, I'd rather be selfish
Hundred times better than
Pretending to be nice and getting hurt
I'm just on my way, don't interfere, no no
I might just say it, mind your own business

No matter what they say I'm me
I just want to be me
I wanna be me, me, me
I don't have to be anything because
I'm perfect when I'm myself
I wanna be me, me, me

I don't wanna be somebody
Just wanna be me, be me
I wanna be me, me, me
I don't wanna be somebody
Just wanna be me, be me
I wanna be me, me, me

Errbody errbody errbody teachin' me (All eyes on me)
Do this, do that, all are dishing out something (Don't touch me)
Ah yeah yeah yeah yeah yeah
It's me who takes care of myself
I'mma do my thang, just do your thang
Cuz I'm the one and only

People love to talk about others
Why do you care so much about others lives
Hey I'm sorry but could you leave me alone
It's none of your business
I do my own business

No matter what they say I'm me
I just want to be me
I wanna be me, me, me
I don't have to be anything because
I'm perfect when I'm myself
I wanna be me, me, me

No matter if you love me or hate me
I wanna be me, one and only me
If you feel me, turn this beat up
I wanna be me, me, me

No matter what they say I'm me
I just want to be me
I wanna be me, me, me
I don't have to be anything because
I'm perfect when I'm myself
I wanna be me, me, me

I don't wanna be somebody
Just wanna be me, be me
I wanna be me, me, me
I don't wanna be somebody
Just wanna be me, be me
I wanna be me, me, me"""),
("LOCO", "ITZY", "k-pop", """[Romanized:]

LOCO

Michindaneun mari ihae gandalkka
I'm gettin' LOCO LOCO
Oh gosh igeon dalkomhan dok gata
I'm gettin' LOCO LOCO

Chulgu eomneun bang ane sabangi neoran geouriya
Guji shwipge malhajamyeon
I feel like I was born to love ya

Oashiseu channeun Kitty nan ne juwireul maemdolji
Kongkkakji kkyeo beorin nae du nuneun Yellow
Kyeojweo ne soneuro bul kkeojin nae shimjang

It's too late, want you so bad neoreul gatgo shipeojeosseo
Molla ijen imi nan Blind kkeutkkaji gabollae

Neon nal banjjeum michige mandeureo
You got me like CRAY-CRAY-CRAZY in love
Daeche nega mweonde
Micheo nalttwieo gibuni Up & down
You got me like CRAY-CRAY-CRAZY in love
Nado naega Outta control

I'm gettin' LOCO LOCO
I'm gettin' LOCO LOCO

Naege daeche neon mweol weonhae
Michin i maeumeun da gatta peo jweodo I'm ok
Haruneun cheongugeul gatta watta gado
Narak kkeutkkaji nal mireobeoryeo
So dangerous, so so so dangerous, uh-oh
Nal deo manggatteuryeodo
Neol mideul su bakke eopge haejweo

Oashiseu chajeun Kitty nan ne yeop jaril neomboji
Break ttawin ijeosseo kkeutkkaji ga bollae

Neon nal banjjeum michige mandeureo
You got me like CRAY-CRAY-CRAZY in love
Daeche nega mweonde
Micheo nalttwieo gibuni Up & down
You got me like CRAY-CRAY-CRAZY in love
Nado naega Outta control

LOCO

I'm gettin' LOCO-LOCO-CO
I'm gettin' LOCO-LOCO-CO-oh-oh-oh
I'm gettin' LOCO-LOCO-CO
I'm gettin' LOCO-LOCO-CO-oh-oh-oh

Neon nal wanjeon michige mandeureo
You got me like CRAY-CRAY-CRAZY in love
Daeche nega mweonde
Michyeo nalttwieo gibuni Up & down
You got me like CRAY-CRAY-CRAZY in love
Nado naega Outta control

I'm gettin' LOCO LOCO
I'm gettin' LOCO LOCO

[Korean:]

LOCO

미친다는 말이 이해 간달까
I'm gettin' LOCO LOCO
Oh gosh 이건 달콤한 독 같아
I'm gettin' LOCO LOCO

출구 없는 방 안에 사방이 너란 거울이야
굳이 쉽게 말하자면
I feel like I was born to love ya

오아시스 찾는 Kitty 난 네 주위를 맴돌지
콩깍지 껴 버린 내 두 눈은 Yellow
켜줘 네 손으로 불 꺼진 내 심장

It's too late, want you so bad 너를 갖고 싶어졌어
몰라 이젠 이미 난 Blind 끝까지 가볼래

넌 날 반쯤 미치게 만들어
You got me like CRAY-CRAY-CRAZY in love
대체 네가 뭔데
미쳐 날뛰어 기분이 Up & down
You got me like CRAY-CRAY-CRAZY in love
나도 내가 Outta control

I'm gettin' LOCO LOCO
I'm gettin' LOCO LOCO

내게 대체 넌 뭘 원해
미친 이 마음은 다 갖다 퍼 줘도 I'm ok
하루는 천국을 갔다 왔다 가도
나락 끝까지 날 밀어버려
So dangerous, so so so dangerous, uh-oh
날 더 망가뜨려도
널 믿을 수 밖에 없게 해줘

오아시스 찾은 Kitty 난 네 옆 자릴 넘보지
Break 따윈 잊었어 끝까지 가 볼래

넌 날 반쯤 미치게 만들어
You got me like CRAY-CRAY-CRAZY in love
대체 네가 뭔데
미쳐 날뛰어 기분이 Up & down
You got me like CRAY-CRAY-CRAZY in love
나도 내가 Outta control

LOCO

I'm gettin' LOCO-LOCO-CO
I'm gettin' LOCO-LOCO-CO-oh-oh-oh
I'm gettin' LOCO-LOCO-CO
I'm gettin' LOCO-LOCO-CO-oh-oh-oh

넌 날 완전 미치게 만들어
You got me like CRAY-CRAY-CRAZY in love
대체 네가 뭔데
미쳐 날뛰어 기분이 Up & down
You got me like CRAY-CRAY-CRAZY in love
나도 내가 Outta control

I'm gettin' LOCO LOCO
I'm gettin' LOCO LOCO

[English translation:]

LOCO

Walked in, smooth operator hit your mark
I'm gettin' LOCO, LOCO
Oh gosh, pure shot of poison to my heart
I'm gettin' LOCO, LOCO

I'm trapped and there's no way out, surrounded
By my thoughts of ya, I think I'm a little obsessed
I feel like I was born to love ya

Oasis for this kitty Fresh like rain when I'm thirsty
Gon' lock you down I got my eye on you, yellow
Feeling the fuego tonight, come and fan the flame

It's too late, want you so bad, I decided not to fight it
Can't contain it anyway 'cause you got me blinded

Such a rush, you're making me lose my mind
You got me like CRAY-CRAY-CRAZY in love
What you're doing to me?
Can't get off this bad roller coaster ride
You got me like CRAY-CRAY-CRAZY in love
I'm addicted, outta control

I'm gettin' LOCO, LOCO
I'm gettin' LOCO, LOCO

So tell me what's your intention
I'm tripping when I know you playing with my emotions
I keep on going back and forth, it's hell then heaven
Pushing me right to the edge of broken
So dangerous, so so so dangerous, uh-oh
Ain't the type to risk it all
But you got me acting irrational

Oasis for this kitty So stay, I need you next to me
Break down my defences, I don't wanna fight it

Such a rush, you're making me lose my mind
You got me like CRAY-CRAY-CRAZY in love
What you're doing to me?
Can't get off this bad roller coaster ride
You got me like CRAY-CRAY-CRAZY in love
I'm addicted, outta control

LOCO

I'm gettin' LOCO-LOCO-CO
I'm gettin' LOCO-LOCO-CO-oh-oh-oh
I'm gettin' LOCO-LOCO-CO
I'm gettin' LOCO-LOCO-CO-oh-oh-oh

Love that rush, you're making me lose my mind
You got me like CRAY-CRAY-CRAZY in love
What you're doing to me?
Can't get off this bad rollercoaster ride
You got me like CRAY-CRAY-CRAZY in love
I'm addicted, outta control

I'm gettin' LOCO, LOCO
I'm gettin' LOCO, LOCO"""),
("What Is Love?", "TWICE", "k-pop", """[Romanized:]

TWICE!
What is love?

Maeilgati yeonghwa sogeseona
Chaek sogeseona deulama sogeseo
Sarangeul neukkyeo
Um sarangeul baewo
Nae ilcheoreom jakku gaseumi ttwieo
Dugeundugeungeoryeo seolleime bupureo olla
Um gunggeumhaeseo michil geotman gata

Ooh eonjengan naegedo
Ireon iri sirjero ireonalkka
Geuge eonjejjeumilkka? eotteon saramilkka?

I wanna know satangcheoreom dalkomhadaneunde
I wanna know haneureul naneun geot gatdaneunde
I wanna know know know know
What is love?
Sarangi eotteon neukkiminji
I wanna know haru jongil utgo issdaneunde
I wanna know sesangi da areumdabdaneunde
I wanna know know know know
What is love?
Eonjengan naegedo sarangi olkka

Jigeum ireon sangsangmaneurodo
Tteoollyeoman bwado
Gaseumi teojil geot gateunde
Um ireohge joheunde
Manil eonjenga jinjjaro naege
Sarangi ol ttae nan ureobeoriljido molla
Um jeongmal gunggeumhae michil geotman gata

Ooh eonjengan naegedo
Ireon iri sirjero ireonalkka
Geuge eonjejjeumilkka? eotteon saramilkka?

I wanna know satangcheoreom dalkomhadaneunde
I wanna know haneureul naneun geot gatdaneunde
I wanna know know know know
What is love?
Sarangi eotteon neukkiminji
I wanna know haru jongil utgo issdaneunde
I wanna know sesangi da areumdabdaneunde
I wanna know know know know
What is love?
Eonjengan naegedo sarangi olkka

Jigeum sesang eoneu gose salgo issneunji
Dodaeche eonjejjeum nawa mannage doelneunji
Eonje eotteohge uriui inyeoneun
Sijakdoelneunji moreujiman neukkimi eojjeonji
Jinjja joheul geot gata waenji
Yeonghwa deuramabodado deo meotjin
Sarangi ol geoya nae yegam eonjena majji
Eoseo natanabwa
Naneun da junbiga dwaessji ready

(Eodi isseulkka) chajanael geoya
(Eodi isseulkka) bogo sipeo juggesseo
Deo isang chameul su eopseul geotman gata

Satangcheoreom dalkomhadaneunde
Haneureul naneun geot gatdaneunde
I wanna know know know know
What is love?
Sarangi eotteon neukkiminji
Haru jongil usgo issdaneunde
Sesangi da areumdabdaneunde
I wanna know know know know
What is love?
Eonjengan naegedo sarangi olkka

I wanna know
I wanna know
I wanna know know know know
What is love?
I wanna know I wanna know
I wanna know
I wanna know
I wanna know know know know
What is love?
I wanna know

[Korean:]

TWICE!
What is love?

매일같이 영화 속에서나
책 속에서나 드라마 속에서
사랑을 느껴
Um 사랑을 배워
내 일처럼 자꾸 가슴이 뛰어
두근두근거려 설레임에 부풀어 올라
Um 궁금해서 미칠 것만 같아

Ooh 언젠간 내게도
이런 일이 실제로 일어날까
그게 언제쯤일까? 어떤 사람일까?

I wanna know 사탕처럼 달콤하다는데
I wanna know 하늘을 나는 것 같다는데
I wanna know know know know
What is love?
사랑이 어떤 느낌인지
I wanna know 하루 종일 웃고 있다는데
I wanna know 세상이 다 아름답다는데
I wanna know know know know
What is love?
언젠간 나에게도 사랑이 올까

지금 이런 상상만으로도
떠올려만 봐도
가슴이 터질 것 같은데
Um 이렇게 좋은데
만일 언젠가 진짜로 내게
사랑이 올 때 난 울어버릴지도 몰라
Um 정말 궁금해 미칠 것만 같아

Ooh 언젠간 내게도
이런 일이 실제로 일어날까
그게 언제쯤일까? 어떤 사람일까?

I wanna know 사탕처럼 달콤하다는데
I wanna know 하늘을 나는 것 같다는데
I wanna know know know know
What is love?
사랑이 어떤 느낌인지
I wanna know 하루 종일 웃고 있다는데
I wanna know 세상이 다 아름답다는데
I wanna know know know know
What is love?
언젠간 나에게도 사랑이 올까

지금 세상 어느 곳에 살고 있는지
도대체 언제쯤 나와 만나게 될는지
언제 어떻게 우리의 인연은
시작될는지 모르지만 느낌이 어쩐지
진짜 좋을 것 같아 왠지
영화 드라마보다도 더 멋진
사랑이 올 거야 내 예감 언제나 맞지
어서 나타나봐
나는 다 준비가 됐지 ready

(어디 있을까) 찾아낼 거야
(어디 있을까) 보고 싶어 죽겠어
더 이상 참을 수 없을 것만 같아

사탕처럼 달콤하다는데
하늘을 나는 것 같다는데
I wanna know know know know
What is love?
사랑이 어떤 느낌인지
하루 종일 웃고 있다는데
세상이 다 아름답다는데
I wanna know know know know
What is love?
언젠간 나에게도 사랑이 올까

I wanna know
I wanna know
I wanna know know know know
What is love?
I wanna know I wanna know
I wanna know
I wanna know
I wanna know know know know
What is love?
I wanna know

[English translation:]

TWICE!
What is love?

Every day, in a movie
In a book or in a drama, I feel love
Um- I learn about love
My heart keeps beating as if it's my own story
Makes my heart pound and swell with hope
Um- I want to know so bad

Ooh, maybe someday
Could it happen to me too?
When will it be? Who will it be?

(I wanna know) How it could be as sweet as candy?
(I wanna know) How it's like flying in the sky?
I wanna know know know know
What is love?
What love feels like?
(I wanna know) How it keeps you smiling all day?
(I wanna know) How the whole world turns beautiful?
I wanna know know know know
What is love?
Will love come to me someday?

Just imagining all of this
Just thinking about it
Almost makes my heart burst
Um- How good it feels?
If, one day, for real
Love does comes to me, I might just cry
Um- I really want to know how it feels

Ooh, maybe someday
Could it happen to me too?
When will it be? Who will it be?

(I wanna know) How it could be as sweet as candy?
(I wanna know) How it's like flying in the sky?
I wanna know know know know
What is love?
What love feels like?
(I wanna know) How it keeps you smiling all day?
(I wanna know) How the whole world turns beautiful?
I wanna know know know know
What is love?
Will love come to me someday?

Where in the world are you right now?
Just when will we get to meet each other?
When and how might our relationship starts?
I don't know right now, but somehow I feel
That it will be really good
Better than any movie or drama
The greatest love will come
My gut instinct is always right
C'mon, show yourself, i'm all set, Ready!

(Wonder where you are) I'm gonna find you
(Wonder where you are) I'm so dying to see you
I can't take it much longer

How it could be as sweet as candy?
How it's like flying in the sky?
I wanna know know know know
What is love?
What love feels like?
How it keeps you smiling all day?
How the whole world turns beautiful?
I wanna know know know know
What is love?
Will love come to me someday?

I wanna know
I wanna know
I wanna know know know know
What is love?
I wanna know I wanna know
I wanna know
I wanna know
I wanna know know know know
What is love?
I wanna know"""),
("Deja Vu", "ATEEZ", "k-pop", """[Romanized:]

Eum algo itji
Beoseonal sudo eopji
Jeomjeom ppajyeoga save me
Please don't leave me
Galmange mogi ta woah oh

Deopchil deuthan ikkeullime
Gamgangmajeo mudyeojyeo nan
Nunape inneun neon kkuminji
Hyeonsirinji hwansanginji

Kkumeseo kkumeul kkun deuthan geol
Oh nae mome jeonyuri neol
Gieokago inneun geot gata
I know you get Deja Vu

Michyeoga
Neowa nuni majuchin sungan
Meomchul suga eopji nan
Kkeuchi eomneun galjeungeul neukkyeo
Know you get Deja Vu

Da da da ra da da da ra da da da ra
Oh Deja Vu
Da da da ra da da da da ra da
Michyeoga I want you so bad oh

Jeogiyo jakkuman geureon nunbichimyeon
Naneun gollanhaeyo wait wait
Jeogiyo naega bon kkumeseon i daeum
Jangmyeoneun amado ppi
No way
Pihal su eopseumyeon play it
Michyeobeorin i sungan nan imi game set

Teojil geo gata so bad
Sonjiseun deo wiheomhae
Shoot it up shoot it up
Ppalgan hyanggiga taolla nal gusokae
Mwoga inneunji susahal ge ready
Chulbalhamyeon ttwieo gappajineun uri racing

Kkumeseo kkumeul kkun deuthan geol
Oh nae mome jeonyuri neol
Gieokago inneun geot gata
I know you get Deja Vu

Michyeoga
Neowa nuni majuchin sungan
Meomchul suga eopji nan
Kkeuchi eomneun galjeungeul neukkyeo
Know you get Deja Vu

Da da da ra da da da ra da da da ra
Oh Deja Vu
Da da da ra da da da da ra da
Michyeoga I want you so bad oh

Eoneu got eotteon sigan
Eotteon unmyeongi nal oh
Neoege kkeureodanggineun geonji

Ne sumi naege danneunda
Nae sumdo nege daeulkka
Nae sumi meonneunda haedo
Daeum kkumeseorado
Find you in my heart

Michyeoga
Neowa nuni majuchin sungan
Meomchul suga eopji nan
Kkeuchi eomneun galjeungeul neukkyeo
Know you get Deja Vu

Da da da ra da da da ra da da da ra
Oh Deja Vu
Da da da ra da da da da ra da
Michyeoga I want you so bad oh

Michyeoga urineun hayan dohwaji sok
Jjageul irwoga dekalkomani
Chakgaginji byeonginji hollanseureopji
Nae mami neol wonhaneun geon bonneungin geoya
I get Deja Vu

[Korean:]

음 알고 있지
벗어날 수도 없지
점점 빠져가 save me
Please don't leave me
갈망에 목이 타 woah oh

덮칠 듯한 이끌림에
감각마저 무뎌져 난
눈앞에 있는 넌 꿈인지
현실인지 환상인지

꿈에서 꿈을 꾼 듯한 걸
Oh 내 몸에 전율이 널
기억하고 있는 것 같아
I know you get Deja Vu

미쳐가
너와 눈이 마주친 순간
멈출 수가 없지 난
끝이 없는 갈증을 느껴
Know you get Deja Vu

Da da da ra da da da ra da da da ra
Oh Deja Vu
Da da da ra da da da da ra da
미쳐가 I want you so bad oh

저기요 자꾸만 그런 눈빛이면
나는 곤란해요 wait wait
저기요 내가 본 꿈에선 이 다음
장면은 아마도 삐
No way
피할 수 없으면 play it
미쳐버린 이 순간 난 이미 game set

터질 거 같아 so bad
손짓은 더 위험해
Shoot it up shoot it up
빨간 향기가 타올라 날 구속해
뭐가 있는지 수사할 게 ready
출발하면 뛰어 가빠지는 우리 racing

꿈에서 꿈을 꾼 듯한 걸
Oh 내 몸에 전율이 널
기억하고 있는 것 같아
I know you get Deja Vu

미쳐가
너와 눈이 마주친 순간
멈출 수가 없지 난
끝이 없는 갈증을 느껴
Know you get Deja Vu

Da da da ra da da da ra da da da ra
Oh Deja Vu
Da da da ra da da da da ra da
미쳐가 I want you so bad oh

어느 곳 어떤 시간
어떤 운명이 날 oh
너에게 끌어당기는 건지

네 숨이 내게 닿는다
내 숨도 네게 닿을까
내 숨이 멎는다 해도
다음 꿈에서라도
Find you in my heart

미쳐가
너와 눈이 마주친 순간
멈출 수가 없지 난
끝이 없는 갈증을 느껴
Know you get Deja Vu

Da da da ra da da da ra da da da ra
Oh Deja Vu
Da da da ra da da da da ra da
미쳐가 I want you so bad oh

미쳐가 우리는 하얀 도화지 속
짝을 이뤄가 데칼코마니
착각인지 병인지 혼란스럽지
내 맘이 널 원하는 건 본능인 거야
I get Deja Vu"""),
("Fly Me To The Moon", "Frank Sinatra", "jazz", """Fly me to the moon
Let me play among the stars
Let me see what spring is like
On a-Jupiter and Mars

In other words: hold my hand
In other words: baby, kiss me

Fill my heart with song
And let me sing for ever more
You are all I long for
All I worship and adore

In other words: please, be true
In other words: I love you

Fill my heart with song
Let me sing for ever more
You are all I long for
All I worship and adore

In other words: please, be true
In other words, in other words: I love you"""),
("Smooth Operator", "Sade", "jazz", """He's laughing with another girl
And playing with another heart
Placing high stakes, making hearts ache
He's loved in seven languages
Jukebox life, Diamond nights and ruby lights
High in the sky
Heaven help him when he falls

Diamond life lover boy
He moves in space with minimum waste and maximum joy
City lights and business nights
When you require streetcar desire for higher heights

No place for beginners or sensitive hearts
The sentiment is left to chance
No place to be ending but somewhere to start

No need to ask
He's a smooth operator
Smooth operator
Smooth operator
Smooth operator

Coast-to-coast, L.A. to Chicago: Western male
Across the North and South, to Key Largo: love for sale

Face-to-face, each classic case
We shadow box and double-cross
Yet need the chase

A license to love, insurance to hold
Melts all your memories and change into gold
His eyes are like angels; his heart is cold

No need to ask
He's a smooth operator
Smooth operator
Smooth operator
Smooth operator

Coast-to-coast, L.A. to Chicago: Western male
Across the North and South, to Key Largo: love for sale

Smooth operator
Smooth operator
Smooth operator
Smooth operator
Smooth operator
Smooth operator
Smooth operator"""),
("Just The Two Of Us", "Bill Withers", "jazz", """I see the crystal raindrops fall
And the beauty of it all
Is when the sun comes shining through
To make those rainbows in my mind
When I think of you sometime
And I want to spend some time with you

Just the two of us
We can make it if we try
Just the two of us
(Just the two of us)
Just the two of us
Building castles in the sky
Just the two of us
You and I

We look for love, no time for tears
Wasted water's all that is
And it don't make no flowers grow
Good things might come to those who wait
Not for those who wait too late
We gotta go for all we know

Just the two of us
We can make it if we try
Just the two of us
(Just the two of us)
Just the two of us
Building them castles in the sky
Just the two of us
You and I

Just the two of us
We can make it just the two of us
Just the two of us
We can make it just the two of us
Just the two of us
We can make it just the two of us
Just the two of us
We can make it just the two of us
Just the two of us
We can make it just the two of us
Just the two of us
We can make it just the two of us
Just the two of us
We can make it just the two of us
Just the two of us
We can make it just the two of us
Just the two of us
We can make it just the two of us

I hear the crystal raindrops fall
On the window down the hall
And it becomes the morning dew
And, darling, when the morning comes
And I see the morning sun
I want to be the one with you

Just the two of us
We can make it if we try
Just the two of us
(Just the two of us)
Just the two of us
Building big castles way on high
Just the two of us
You and I

(Just the two of us)
Yes, the two of us
(We can make it just the two of us)
Let's get it together, babe
(Just the two of us)
Yes, the two of us
(We can make it just the two of us
Just the two of us
We can make it just the two of us
Just the two of us
We can make it just the two of us
Just the two of us
We can make it just the two of us
Just the two of us
We can make it just the two of us
Just the two of us
We can make it just the two of us
Just the two of us
We can make it just the two of us
Just the two of us)"""),
("Good Morning, Heartache", "Billie Holiday", "jazz", """Good morning, heartache, you ole gloomy sight
Good morning, heartache, thought we'd said goodbye last night
I turned and tossed until it seemed you had gone
But here you are with the dawn
Wish I'd forget you
but you're here to stay
It seems I met you
When my love went away
Now everyday I start by saying to you
Good morning, heartache, what's new?

Stop haunting me now
Can't shake you, no how
Just leave me alone
I've got those Monday blues
Straight through Sunday blues

Good morning, heartache, here we go again
Good morning, hearache, you're the one who knew me when
Might as well get used to you hangin around
Good morning, heartache, sit down

Stop haunting me now
Can't shake you, no how
Just leave me alone
I've got those Monday blues
Straight through Sunday blues

Good morning, heartache, here we go again
Good morning, hearache, you're the one who knew me when
Might as well get used to you hangin around
Good morning, heartache, sit down"""),
("In A Sentimental Mood", "Duke Ellington", "jazz", """In a sentimental mood
I can see the stars come through my room
While your loving attitude
Is like a flame that lights the gloom

On the wings of every kiss
Drifts a melody so strange and sweet
In this sentimental bliss
You make my paradise complete

Rose petals seem to fall
It's all I could dream to call you mine
My heart's a lighter thing
Since you made this night a thing divine

In a sentimental mood
I'm within a world so heavenly
For I never dreamt that you'd be
Loving sentimental me

In a sentimental mood
I'm within a world so heavenly
For I never dreamt that you'd be
Loving sentimental me"""),
("Who Was That", "Kenny Wayne Shepherd", "blues", """I wanna know who, who was that while ago
I wanna know who, who was that while ago
You see when I came in, somebody ran out of my back door

Had his shoes in his pocket, overcoat in his hand
Tell me baby, who was that man
I wanna know who, who was that while ago
Well when I came in, somebody ran out of my back door

Ashes in the ashtray, I don't even smoke
Foot prints leading to my backdoor
I wanna know who, who was that while ago
Well when I came in, somebody ran out of my back door

When I went into the kitchen, dirty dishes in the sink
Two wine glasses on the table and I don't even drink
I wanna know who, who was that while ago
Well when I came in, somebody ran out of my back door

When I went into the bedroom, I could tell something wasn't right
Bed was all tore up like you'd been in a hell of a fight
I wanna know who, tell me who was that while ago
Well when I came in somebody ran out of my back door

I wanna know who, tell me what's going on
Tell me who, tell me what's going on
I believe to my soul somebody's been getting my love bone
Tell me who, who was that while ago
I wanna know who, who was that while ago

Who was that, who was that while ago
Who was that, who was that while ago
Who was that, who was that while ago
Who was that, who was that while ago
Who was that, who was that while ago
Who was that, who was that while ago

I wanna know baby, I want to know right now
Who was that while ago"""),
("Georgia On My Mind", "Ray Charles", "blues", """Georgia, Georgia
The whole day through (the whole day through)
Just an old sweet song
Keeps Georgia on my mind (Georgia on my mind)

I said Georgia, Georgia
A song of you (a song of you)
Comes as sweet and clear
As moonlight through the pines

Other arms reach out to me
Other eyes smile tenderly
Still in peaceful dreams I see
The road leads back to you

I said Georgia, oh Georgia
No peace I find (peace I find)
Just an old sweet song
Keeps Georgia on my mind (Georgia on my mind)

Other arms reach out to me
Other eyes smile tenderly
Still in peaceful dreams I see
The road leads back to you

Woah, Georgia, Georgia
No peace, no peace I find
Just an old, sweet song
Keeps Georgia on my mind (Georgia on my mind)

I said just an old sweet song
Keeps Georgia on my mind"""),
("Crying Shame", "The Teskey Brothers", "blues", """Oh, you're just plain mean to me, woman
And that's a crying, crying shame
You're just plain mean to me, woman
And that's a crying, crying shame
Since you gone away and left me, honey
I been crying with the pain

Oh, I'd do most anything
To feel your love just once again
Oh, I'd do most anything
To feel your love just once again
But that day never comes, babe
That's why I'm crying with the pain

Ooh, you're just like a little child, babe
And you treat love just like a game
You're just like a little child, babe
And you treat love just like your own game
But you never really loved me, honey
That's why I'm crying with the pain

Yeah, I'm crying with the pain
Most every night and every day
Yeah, I'm crying, crying, crying
Most every night and every day
It' was just three words I wanna hear from you, baby
And those are three words you never say"""),
("Give Me One Reason", "Tracy Chapman", "blues", """Give me one reason to stay here
And I'll turn right back around
Give me one reason to stay here
And I'll turn right back around
Said I don't want to leave you lonely
You got to make me change my mind

Baby I got your number, oh, and I know that you got mine
You know that I called you, I called too many times
You can call me baby, you can call me anytime
You got to call me

Give me one reason to stay here
And I'll turn right back around
Give me one reason to stay here
And I'll turn right back around
Said I don't want leave you lonely
You got to make me change my mind

I don't want no one to squeeze me, they might take away my life
I don't want no one to squeeze me, they might take away my life
I just want someone to hold me, oh, and rock me through the night

This youthful heart can love you, yes, and give you what you need
I said, This youthful heart can love you, oh, and give you what you need
But I'm too old to go chasing you around
Wasting my precious energy

Give me one reason to stay here
Yes and I'll turn right back around
Give me one reason to stay here
Ooh and I'll turn right back around
Said I don't want leave you lonely
You got to make me change my mind

Baby just give me one reason, Give me just one reason why
Baby just give me one reason, Give me just one reason why I should stay
Said I told you that I loved you
And there ain't no more to say"""),
("Dimples", "John Lee Hooker", "blues", """I love the way you walk
I love the way you talk
I love the way you walk
Love the way you talk
I got my eyes on you

I like the way you smile
Babe you really got style
I'd walk a thousand miles
For just one smile
I got my eyes on you
On you babe, yeah

Yeah, yeah
Yeah, yeah

(Take it again)

You got dimples in your jaw
Just makes me love you more
You got dimples in your jaw
Makes me love you more
I got my eyes on you

Well, I see you every day, yeah
I'm so glad you came my way
I took one look and I got hooked
I got my eyes on you
Eyes on you baby

Yeah, yeah
Yeah, yeah

I love the way you walk
I love the way you talk
I love the way you walk
I love the way you talk
I got my eyes on you

Yeah, I love the way you smile
Babe you really got style
I'd walk a thousand miles
For just one smile
I got my eyes on you

I'd walk a thousand miles
For just one of your smiles
I got my eyes on you

Hoohoohhooooh
Just took one look
Babe I got hooked
Yeah, yeah
Oh yeah
I'd walk a thousand miles
For just one smile
Oohoooohooooohoooh
You got me hooked
With just one look"""),
("Every Breath You Take", "The Police", "classic", """Every breath you take
And every move you make
Every bond you break
Every step you take
I'll be watching you
Every single day
And every word you say
Every game you play
Every night you stay
I'll be watching you

Oh, can't you see you belong to me?
How my poor heart aches with every step you take

Every move you make
And every vow you break
Every smile you fake
Every claim you stake
I'll be watching you

Since you've gone, I've been lost without a trace
I dream at night, I can only see your face
I look around, but it's you I can't replace
I feel so cold, and I long for your embrace
I keep crying baby, baby, please

Mm, mm, mm, mm
Mm, mm, mm

Oh, can't you see you belong to me?
How my poor heart aches with every step you take

Every move you make
And every vow you break
Every smile you fake
Every claim you stake
I'll be watching you
Every move you make
Every step you take
I'll be watching you

I'll be watching you

(Every breath you take)
(Every move you make)
(Every bond you break)
(Every step you take)
I'll be watching you

(Every single day)
(Every word you say)
(Every game you play)
(Every night you stay)
I'll be watching you

(Every move you make)
(Every vow you break)
(Every smile you fake)
(Every claim you stake)
I'll be watching you

(Every single day)
(Every word you say)
(Every game you play)
(Every night you stay)
I'll be watching you

(Every breath you take)
(Every move you make)
(Every bond you break)
(Every step you take)
I'll be watching you

(Every single day)
(Every word you say)
(Every game you play)
(Every night you stay)
I'll be watching you

(Every move you make)
(Every vow you break)
(Every smile you fake)
(Every claim you stake)
I'll be watching you

(Every single day)
(Every word you say)
(Every game you play)
(Every night you stay)
I'll be watching you"""),
("God Save The Queen", "Sex Pistols", "classic", """God, save the Queen
The fascist regime
They made you a moron
Potential H-bomb
God, save the Queen
She ain't no human being
There is no future
In England's dreaming

Don't be told what you want to want to
And don't be told what you want to need
There's no future, no future
No future for you

God, save the Queen
We mean it, man
We love our Queen
God, saves

God, save the Queen
'Cause tourists are money
And our figurehead
Is not what she seems
Oh, God, save history
God, save your mad parade
Oh, Lord, God, have mercy
All crimes are paid

When there's no future how can there be sin?
We're the flowers in the dustbin
We're the poison in your human machine
We're the future, your future

God, save the Queen
We mean it, man
We love our Queen
God, saves

God, save the Queen
We mean it, man
And there is no future
In England's dreaming

No future
No future
No future for you
No future
No future
No future for me
No future
No future
No future for you
No future
No future for you"""),
("London Calling", "The Clash", "classic", """London calling to the faraway towns
Now war is declared, and battle come down
London calling to the underworld
Come out of the cupboard, you boys and girls
London calling, now don't look to us
Phoney Beatlemania has bitten the dust
London calling, see we ain't got no swing
Except for the ring of that truncheon thing

The ice age is coming, the sun's zooming in
Meltdown expected, the wheat is growing thin
Engines stop running, but I have no fear
'Cause London is drowning, and I live by the river

London calling to the imitation zone
Forget it brother, you can go it alone
London calling to the zombies of death
Quit holding out, and draw another breath
London calling, and I don't wanna shout
But while we were talking, I saw you nodding out
London calling, see we ain't got no high
Except for that one with the yellowy eyes

The ice age is coming, the sun's zooming in
Engines stop running, the wheat is growing thin
A nuclear error, but I have no fear
'Cause London is drowning, and I, I live by the river

The ice age is coming, the sun's zooming in
Engines stop running, the wheat is growing thin
A nuclear error, but I have no fear
'Cause London is drowning, and I, I live by the river

Now get this...

London calling, yes, I was there too
And you know what they said? Well, some of it was true!
London calling at the top of the dial
And after all this, won't you give me a smile?
London calling...

I never felt so much alike alike alike alike..."""),
("Take Me To Church", "Hozier", "classic", """My lover's got humour
She's the giggle at a funeral
Knows everybody's disapproval
I should've worshipped her sooner

If the heavens ever did speak
She's the last true mouthpiece
Every Sunday's getting more bleak
A fresh poison each week

"We were born sick," you heard them say it

My church offers no absolutes
She tells me, "Worship in the bedroom"
The only heaven I'll be sent to
Is when I'm alone with you

I was born sick
But I love it
Command me to be well
Aaay. Amen. Amen. Amen

Take me to church
I'll worship like a dog at the shrine of your lies
I'll tell you my sins so you can sharpen your knife
Offer me that deathless death
Good God, let me give you my life
Take me to church
I'll worship like a dog at the shrine of your lies
I'll tell you my sins so you can sharpen your knife
Offer me that deathless death
Good God, let me give you my life

If I'm a pagan of the good times
My lover's the sunlight
To keep the Goddess on my side
She demands a sacrifice

Drain the whole sea
Get something shiny
Something meaty for the main course
That's a fine-looking high horse
What you got in the stable?
We've a lot of starving faithful

That looks tasty
That looks plenty
This is hungry work

Take me to church
I'll worship like a dog at the shrine of your lies
I'll tell you my sins so you can sharpen your knife
Offer me my deathless death
Good God, let me give you my life
Take me to church
I'll worship like a dog at the shrine of your lies
I'll tell you my sins so you can sharpen your knife
Offer me my deathless death
Good God, let me give you my life

No Masters or Kings
When the Ritual begins
There is no sweeter innocence than our gentle sin

In the madness and soil of that sad earthly scene
Only then I am human
Only then I am clean
Ooh oh. Amen. Amen. Amen

Take me to church
I'll worship like a dog at the shrine of your lies
I'll tell you my sins so you can sharpen your knife
Offer me that deathless death
Good God, let me give you my life
Take me to church
I'll worship like a dog at the shrine of your lies
I'll tell you my sins so you can sharpen your knife
Offer me that deathless death
Good God, let me give you my life"""),
("Istanbul (Not Constantinople)", "They Might Be Giants", "classic", """Istanbul was Constantinople
Now it's Istanbul, not Constantinople
Been a long time gone, Constantinople
Now it's Turkish delight on a moonlit night

Every gal in Constantinople
Lives in Istanbul, not Constantinople
So if you've a date in Constantinople
She'll be waiting in Istanbul

Even old New York was once New Amsterdam
Why they changed it I can't say
People just liked it better that way

So take me back to Constantinople
No, you can't go back to Constantinople
Been a long time gone, Constantinople
Why did Constantinople get the works?
That's nobody's business but the Turks

Istanbul (Istanbul)
Istanbul (Istanbul)

Even old New York was once New Amsterdam
Why they changed it I can't say
People just liked it better that way

Istanbul was Constantinople
Now it's Istanbul, not Constantinople
Been a long time gone, Constantinople
Why did Constantinople get the works?
That's nobody's business but the Turks

So take me back to Constantinople
No, you can't go back to Constantinople
Been a long time gone, Constantinople
Why did Constantinople get the works?
That's nobody's business but the Turks

Istanbul"""),
("Gangsta's Paradise", "Coolio", "classic", """As I walk through the valley of the shadow of death
I take a look at my life and realize there's nothin' left
'Cause I've been blastin' and laughin' so long, that
Even my momma thinks that my mind is gone
But I ain't never crossed a man that didn't deserve it
Me be treated like a punk, you know that's unheard of
You better watch how you talkin' and where you walkin'
Or you and your homies might be lined in chalk
I really hate to trip, but I gotta loc
As they croak, I see myself in the pistol smoke, fool
I'm the kinda G the little homies wanna be like
On my knees in the night, sayin' prayers in the streetlight

Been spendin' most their lives livin' in the gangsta's paradise
Been spendin' most their lives livin' in the gangsta's paradise
Keep spendin' most our lives livin' in the gangsta's paradise
Keep spendin' most our lives livin' in the gangsta's paradise

Look at the situation they got me facin'
I can't live a normal life, I was raised by the state
So I gotta be down with the hood team
Too much television watchin' got me chasin' dreams
I'm a educated fool with money on my mind
Got my ten in my hand and a gleam in my eye
I'm a loc'd out gangsta, set trippin' banger
And my homies is down so don't arouse my anger
Fool, death ain't nothin' but a heart beat away
I'm livin' life do or die, what can I say?
I'm 23 now, but will I live to see 24?
The way things is goin' I don't know

Tell me why are we so blind to see
That the ones we hurt are you and me?

Been spendin' most their lives livin' in the gangsta's paradise
Been spendin' most their lives livin' in the gangsta's paradise
Keep spendin' most our lives livin' in the gangsta's paradise
Keep spendin' most our lives livin' in the gangsta's paradise

Power and the money, money and the power
Minute after minute, hour after hour
Everybody's runnin', but half of them ain't lookin'
It's goin' on in the kitchen, but I don't know what's cookin'
They say I gotta learn, but nobody's here to teach me
If they can't understand it, how can they reach me?
I guess they can't, I guess they won't
I guess they frontin', that's why I know my life is out of luck, fool!

Been spendin' most their lives livin' in the gangsta's paradise
Been spendin' most their lives livin' in the gangsta's paradise
Keep spendin' most our lives livin' in the gangsta's paradise
Keep spendin' most our lives livin' in the gangsta's paradise

Tell me why are we so blind to see
That the ones we hurt are you and me?
Tell me why are we so blind to see
That the ones we hurt are you and me?"""),
("Scream And Shout", "Britney Spears", "classic", """Bring the action
When you hear this in the club
You gotta turn the shit up
You gotta turn the shit up
You gotta turn the shit up

When we up in the club
All eyes on us
All eyes on us
All eyes on us

See the boys in the club
They watching us
They watching us
They watching us

Everybody in the club
All eyes on us
All eyes on us
All eyes on us

I wanna scream and shout
And let it all out
And scream and shout
And let it out

We saying, oh, we oh, we oh, we oh
We saying, oh, we oh, we oh, we oh

I wanna scream and shout
And let it all out
And scream and shout
And let it out

We saying, oh, we oh, we oh, we oh
Rocking with
Will.i.am and Britney, bitch!

Ohh yeah. Ohh yeah. Ohh yeah.

Bring the action

Rock and roll, everybody let's lose control
On the bottom, we let it go
Going faster, we ain't going slow-low-low

Hear the beat, now let's hit the floor
Drink it up, and then drink some more
Light it up, and let's let it blow, blow, blow

Hey, yo, rock it out and rock it now
If you know what we talking 'bout
Turn it up, and burn down the house ha house

Hey, yo, turn it up, and go turn it down
Here we go, we go shake it
'Cause everywhere we go we
Bring the action

When you hear this in the club
You gotta turn the shit up
You gotta turn the shit up
You gotta turn the shit up

When we up in the club
All eyes on us
All eyes on us
All eyes on us

You see them girls in the club
They looking at us
They looking at us
They looking at us

Everybody in the club
All eyes on us
All eyes on us
All eyes on us

I wanna scream and shout
And let it all out
And scream and shout
And let it out

We saying, oh, we oh, we oh, we oh
We saying, oh, we oh, we oh, we oh

I wanna scream and shout
And let it all out
And scream and shout
And let it out

We saying, oh, we oh, we oh, we oh
Rocking with
Will.i.am and Britney, bitch!

Oh yeah, oh yeah, oh yeah.

It goes on, and on, and on, and on
When me and you party together
I wish this night would last forever
'Cause I was feeling down, now I'm feeling better

It goes on, and on, and on, and on
When me and you party together
I wish this night would last forever
Ever, ever, ever, ever

I wanna scream and shout
And let it all out
And scream and shout
And let it out

We saying, oh, we oh, we oh, we oh
We saying, oh, we oh, we oh, we oh

I wanna sream and shout
And let it all out
And scream and shout
And let it out

We saying, oh, we oh, we oh, we oh
We saying, oh, we oh, we oh, we oh

I wanna scream and shout
And let it all out
And scream and shout
And let it out

We saying, oh, we oh, we oh, we oh
Rocking with
Will.i.am and Britney, bitch!"""),
("Hey Jude", "The Beatles", "classic", """Hey, Jude, don't make it bad
Take a sad song and make it better
Remember to let her into your heart
Then you can start to make it better

Hey, Jude, don't be afraid
You were made to go out and get her
The minute you let her under your skin
Then you begin to make it better

And anytime you feel the pain,
Hey, Jude, refrain
Don't carry the world upon your shoulders
For well you know that it's a fool
Who plays it cool
By making his world a little colder

Nah, nah nah, nah nah, nah nah, nah nah

Hey, Jude, don't let me down
You have found her, now go and get her
Remember to let her into your heart
Then you can start to make it better

So let it out and let it in,
Hey, Jude, begin
You're waiting for someone to perform with
And don't you know that it's just you,
Hey, Jude, you'll do
The movement you need is on your shoulder

Nah, nah nah, nah nah, nah nah, nah nah yeah

Hey, Jude, don't make it bad
Take a sad song and make it better
Remember to let her under your skin
Then you'll begin to make it better, better, better, better, better... oh!

Nah, nah nah, nah nah, nah, nah, nah nah,
Hey, Jude
Nah, nah nah, nah nah, nah, nah, nah nah,
Hey, Jude
Nah, nah nah, nah nah, nah, nah, nah nah,
Hey, Jude (Jude)
Nah, nah nah, nah nah, nah, nah, nah nah,
Hey, Jude (yeah, yeah, yeah)
Nah, nah nah, nah nah, nah, nah, nah nah,
Hey, Jude
Nah, nah nah, nah nah, nah, nah, nah nah,
Hey, Jude (don't make it bad, Jude)
Nah, nah nah, nah nah, nah, nah, nah nah,
Hey, Jude (take a sad song and make it better)
Nah, nah nah, nah nah, nah, nah, nah nah,
Hey, Jude (oh, Jude)
Nah, nah nah, nah nah, nah, nah, nah nah,
Hey, Jude (Jude, hey, Jude, whoa)
Nah, nah nah, nah nah, nah, nah, nah nah,
Hey, Jude
Nah, nah nah, nah nah, nah, nah, nah nah,
Hey, Jude (ooh)
Nah, nah nah, nah nah, nah, nah, nah nah,
Hey, Jude
Nah, nah nah, nah nah, nah, nah, nah nah,
Hey, Jude
Nah, nah nah, nah nah, nah, nah, nah nah,
Hey, Jude
Nah, nah nah, nah nah, nah, nah, nah nah,
Hey, Jude
Nah, nah nah, nah nah, nah, nah, nah nah,
Hey, Jude [fade out]"""),
("How Deep Is Your Love?", "Calvin Harris", "electronic", """Ah-ooh, ooh, ah-ooh

I want you to breathe me in
Let me be your air
Let me roam your body freely
No inhibition, no fear

How deep is your love?
Is it like the ocean?
What devotion are you?
How deep is your love?
Is it like nirvana?
Hit me harder again
How deep is your love?
How deep is your love?
How deep is your love?
Is it like the ocean?
Pull me closer again
How deep is your love?

Ah-ooh, ah-ooh, ah-ooh
How deep is your love?
Ah-ooh, ah-ooh, ah-ooh

Open up my eyes again
Tell me who I am (Mm)
Let me in on all your secrets
No inhibition, no sin

How deep is your love?
Is it like the ocean?
What devotion are you?
How deep is your love?
Is it like nirvana?
Hit me harder again
How deep is your love?
How deep is your love?
How deep is your love?
Is it like the ocean?
Pull me closer again
How deep is your love?

Ah-ooh, ah-ooh, ah-ooh
How deep is your love?
Ah-ooh, ah-ooh, ah-ooh
How deep is your love?

So tell me, how deep is your love? Can it go deeper?
So tell me, how deep is your love? Can it go deep?
So tell me, how deep is your love? Can it go deeper?
So tell me, how deep is your love? Can it go deep?
How deep is your love?
So tell me, how deep is your love? Can it go deeper?
So tell me, how deep is your love? Can it go deep?
How deep is your love?
So tell me, how deep is your love? Can it go deeper?
Pull me closer again
So tell me, how deep is your love?
How deep is your love?

Ah-ooh, ah-ooh, ah-ooh
How deep is your love?
Ah-ooh, ah-ooh, ah-ooh
How deep is your love?
So tell me, how deep is your love? Can it go deeper?
So tell me, how deep is your love? Can it go deep?
How deep is your love?
So tell me, how deep is your love? Can it go deeper?
So tell me, how deep is your love? Can it go deep?"""),
("Faded", "Alan Walker", "electronic", """You were the shadow to my light
Did you feel us?
Another star
You fade away
Afraid our aim is out of sight
Wanna see us
Alight

Where are you now?
Where are you now?
Where are you now?
Was it all in my fantasy?
Where are you now?
Were you only imaginary?

Where are you now?
Atlantis
Under the sea
Under the sea
Where are you now?
Another dream
The monster's running wild inside of me
I'm faded
I'm faded
So lost, I'm faded
I'm faded
So lost, I'm faded

These shallow waters never met what I needed
I'm letting go a deeper dive
Eternal silence of the sea, I'm breathing
Alive

Where are you now?
Where are you now?
Under the bright but faded lights
You've set my heart on fire
Where are you now?
Where are you now?

Where are you now?
Atlantis
Under the sea
Under the sea
Where are you now?
Another dream
The monster's running wild inside of me
I'm faded
I'm faded
So lost, I'm faded
I'm faded
So lost, I'm faded"""),
("Give Me Everything", "Pitbull", "electronic", """[Pitbull:]
Me not working hard?
Yeah, right, picture that with a Kodak
Or, better yet, go to Times Square
Take a picture of me with a Kodak
Took my life from negative to positive
I just want y'all to know that
And tonight, let's enjoy life
Pitbull, Nayer, Ne-Yo, that's right

[Ne-Yo (Nayer):]
Tonight
I want all of you tonight
Give me everything tonight
For all we know
We might not get tomorrow, let's do it tonight
(Don't care what they say, or what games they play)
(Nothing is enough, 'til they handle love )
Let's do it tonight
(I want you tonight, I want you to stay)
(I want you tonight)
Grab somebody sexy, tell 'em, "Hey"

[Ne-Yo:]
(Hey) Give me everything tonight
(Hey) Give me everything tonight (Ooh-ooh)
(Hey) Give me everything tonight (Ooh-ooh)
(Hey) Give me everything tonight

[Pitbull:]
Take advantage of tonight (Yeah)
'Cause tomorrow I'm off to Dubai to perform for a princess
But tonight, I can make you my queen
And make love to you endless (Yeah)
It's insane, the way the name growing (Hey, hey)
Money keep flowing, hustlers move in silence (Hey, hey, hey, hey)
So, I'm tiptoeing, to keep flowing (Hey, hey, hey, hey)
I got it locked up like Lindsay Lohan (Hey, hey, woo)

Put it on my life, baby (Heh)
I'll make ya feel right, baby
Can't promise tomorrow
But I promise tonight
Dale (Woo)

Excuse me (Excuse me)
And I might drink a little more
Than I should tonight (I should tonight)
And I might take you home with me
If I could tonight (I could tonight)
And baby, I'ma make you feel
So good tonight (Good)
'Cause we might not get tomorrow, woo

[Ne-Yo (Nayer):]
Tonight
I want all of you tonight
Give me everything tonight
For all we know
We might not get tomorrow, let's do it tonight
(Don't care what they say, or what games they play)
(Nothing is enough, 'til they handle love)
Let's do it tonight)
(I want you tonight, I want you to stay)
(I want you tonight)
Grab somebody sexy, tell 'em, "Hey"

[Ne-Yo:]
(Hey) Give me everything tonight
(Hey) Give me everything tonight (Ooh-ooh)
(Hey) Give me everything tonight (Ooh-ooh)
(Hey) Give me everything tonight

[Pitbull:]
Reach for the stars
And if you don't grab them
At least you'll fall on top of the world
Think about it, 'cause if you slip
I'm gon' fall on top of your girl, hahahaha
What I'm involved with is deeper than the Mason's baby
Baby, and it ain't no secret
My family's from Cuba, but I'm an American idol
Getting money like Seacrest (Yeah)

Put it on my life, baby (Baby)
I'll make you feel right, baby (Baby)
Can't promise tomorrow (Nah)
But I promise tonight
Dale (Woo)

[Pitbull {Ne-Yo}:]
Excuse me (Excuse me)
And I might drink a little more
Than I should tonight (I should tonight)
And I might take you home with me
If I could tonight (I could tonight)
And, baby, I'ma make you feel
So good, tonight (Good)
'Cause we might not get tomorrow, woo {Ooh}

[Ne-Yo (Nayer):]
Tonight
I want all of you tonight
Give me everything tonight
For all we know
We might not get tomorrow, let's do it tonight
(Don't care what they say, or what games they play)
(Nothing is enough, 'til they handle love)
Let's do it tonight
(I want you tonight, I want you to stay)
(I want you tonight)
Grab somebody sexy, tell 'em, "Hey"

[Ne-Yo:]
(Hey) Give me everything tonight
(Hey) Give me everything tonight (Ooh-ooh)
(Hey) Give me everything tonight (Ooh-ooh)
(Hey) Give me everything tonight

[Pitbull {Ne-Yo}:]
Excuse me (Excuse me)
And I might drink a little more
Than I should tonight (I should tonight)
And I might take you home with me
If I could tonight (I could tonight)
And, baby, I'ma make you feel
So good, tonight (Good)
'Cause we might not get tomorrow, woo"""),
("We Found Love", "Rihanna", "electronic", """Yellow diamonds in the light
And we're standing side by side
As your shadow crosses mine
What it takes to come alive

It's the way I'm feeling I just can't deny
But I've gotta let it go

We found love in a hopeless place
We found love in a hopeless place
We found love in a hopeless place
We found love in a hopeless place

Shine a light through an open door
Love and life I will divide
Turn away 'cause I need you more
Feel the heartbeat in my mind

It's the way I'm feeling I just can't deny
But I've gotta let it go

We found love in a hopeless place
We found love in a hopeless place
We found love in a hopeless place
We found love in a hopeless place

Yellow diamonds in the light
And we're standing side by side
As your shadow crosses mine (mine, mine, mine)

We found love in a hopeless place
We found love in a hopeless place
We found love in a hopeless place
We found love in a hopeless place

We found love in a hopeless place
We found love in a hopeless place
We found love in a hopeless place
We found love in a hopeless place"""),
("Let Me Love You", "DJ Snake ft. Justin Bieber", "electronic", """I used to believe
We were burnin' on the edge of somethin' beautiful
Somethin' beautiful
Sellin' a dream
Smoke and mirrors keep us waiting on a miracle
On a miracle

Say, go through the darkest of days
Heaven is a heartbreak away
Never let you go, never let me down
Oh, it's been a hell of a ride
Driving the edge of a knife
Never let you go, never let me down

Don't you give up, nah-nah-nah
I won't give up, nah-nah-nah
Let me love you
Let me love you
Don't you give up, nah-nah-nah
I won't give up, nah-nah-nah
Let me love you
Let me love you
Oh, baby, baby

Don't fall asleep
At the wheel, we've got a million miles ahead of us
Miles ahead of us
All that we need
Is a rude awakening to know we're good enough
Know we're good enough

Say go through the darkest of days
Heaven is a heartbreak away
Never let you go, never let me down
Oh, it's been a hell of a ride
Driving the edge of a knife
Never let you go, never let me down

Don't you give up, nah-nah-nah
I won't give up, nah-nah-nah
Let me love you
Let me love you
Don't you give up, nah-nah-nah
I won't give up, nah-nah-nah
Let me love you
Let me love you
Oh, baby, baby

Never let you go, never let you go go
Never let you go, never let you go go
Never let you go, whoa
No, never let you go, whoa

Never let you go
Never let you go go
Never let you go
Never let you go go
Oh, no, no, no
No, never let you go
Yeah, yeah
No, never let you go

Don't you give up, nah-nah-nah
I won't give up, nah-nah-nah
Let me love you
Let me love you
Don't you give up, nah-nah-nah
I won't give up, nah-nah-nah
Let me love you
Let me love you"""),
("Oblivion", "Grimes", "electronic", """I never walk about, after dark
It's my point of view
'Cause someone could break your neck
Coming up behind you, always coming and you'd never have a clue

I never look behind, all the time
I will wait forever, always looking straight
Thinking, counting, all the hours you wait

See you on a dark night
See you on a dark night
See you on a dark night
See you on a dark night

And now another clue, I would ask
If you could help me out
It's hard to understand
'Cause when you're running by yourself
It's hard to find someone to hold your hand

And now it's good to be tough on me
But I will wait forever
I need someone else to look into my eyes and tell me
Girl you know you gotta watch your health

To look into my eyes and tell me
La la la la la
To look into my eyes and tell me
La la la la la
La la la la la
La la la la la"""),
("After Dark", "Mr.Kitty", "electronic", """I see you, you see me
How pleasant, this feeling
The moment you hold me
I missed you, I'm sorry
I've given what I have
I showed you I'm growing
The ashes fall slowly
As your voice consoles me

As the hours pass
I will let you know
That I need to ask
Before I'm alone
How it feels to rest
On your patient lips
To eternal bliss
I'm so glad to know
As the hours pass
I will let you know
That I need to ask
Before I'm alone
How it feels to rest
On your patient lips
To eternal bliss
I'm so glad to know

We're swaying to drum beats
In motion, I'm feeling
My patience controlling
The question, I won't speak
We're telling the stories
Our laughter, he knows me
We're leaving, we're talking
You're closer, it's calming

As the hours pass
I will let you know
That I need to ask
Before I'm alone
How it feels to rest
On your patient lips
To eternal bliss
I'm so glad to know
As the hours pass
I will let you know
That I need to ask
Before I'm alone
How it feels to rest
On your patient lips
To eternal bliss
I'm so glad to know

The night will hold us close and the stars will guide us home
I've been waiting for this moment, we're finally alone
I turn to ask the question, so anxious, my thoughts
Your lips were soft like winter, in your passion, I was lost

As the hours pass
I will let you know
That I need to ask
Before I'm alone
How it feels to rest
On your patient lips
To eternal bliss
I'm so glad to know
As the hours pass
I will let you know
That I need to ask
Before I'm alone
How it feels to rest
On your patient lips
To eternal bliss
I'm so glad to know

As the hours pass
I will let you know
That I need to ask
Before I'm alone
How it feels to rest
On your patient lips
To eternal bliss
I'm so glad to know
As the hours pass
I will let you know
That I need to ask
Before I'm alone
How it feels to rest
On your patient lips
To eternal bliss
I'm so glad to know"""),
("I'm An Albatraoz", "AronChupa", "electronic", """Mesdames et Messieurs
S'il vous plaît
Soyez prêt pour AronChupa et Albatraoz
C'est parti!

Let me tell you all a story
About a mouse named Lorry
Yeah, Lorry was a mouse
In a big brown house
She called herself the hoe
With the money money flow

But fuck that little mouse
'Cause I'm an albatraoz

I'm an albatraoz
So what?
I'm an albatraoz

Yeah, Lorry said she was a mouse
Smoked that cheesn’ like a baoz
Monilie money money hoe
Chinka chinka chingka-flow

Yeah, Lorry was a witch,
Yeah, a sneaky little bitch

So fuck that little mouse
'cause I'm an albatraoz

I'm an albatraoz
So what?
I'm an albatraoz

Mesdames et Messieurs
S'il vous plaît
Soyez prêt pour AronChupa et Albatraoz
C'est parti!

I got it!

Ooh, I see ya, ooh, I see ya, ooh, I see ya

I'm an albatraoz
So what?
I'm, I'm, I'm...
Stop!
I got it

I'm an albatraoz
This is albatraoz, yeah""")
]

c.executemany('''
INSERT INTO songs (title, artist, genre, lyrics)
VALUES (?, ?, ?, ?)
''', songs)

# Create users table
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

conn.commit()
conn.close()
