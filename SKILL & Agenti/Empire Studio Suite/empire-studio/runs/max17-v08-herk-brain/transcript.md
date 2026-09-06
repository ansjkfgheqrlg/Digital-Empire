
[00:00:00] Today, I'm going to explain the
[00:00:00] different levels of building your own AI
[00:00:02] second brain. You can see here we have a
[00:00:04] visual of three very different types of
[00:00:07] data. This one is where we have our
[00:00:08] context really starting to form and
[00:00:10] we're starting to see some relationships
[00:00:12] and we're starting to see some different
[00:00:13] nodes and entities form. And then as we
[00:00:15] continue to scale this up, add more
[00:00:17] knowledge, more knowledge, more
[00:00:18] relationships, we start to get something
[00:00:20] that looks a little bit more like this
[00:00:21] where we have clearly different clusters
[00:00:23] and inside of all of these nodes we can
[00:00:24] see how they relate to each other. And
[00:00:26] then over here we're taking all of those
[00:00:27] relationships a step farther and we're
[00:00:29] able to then start to see how everything
[00:00:31] really pieces together rather than just
[00:00:32] having files that sort of link back to
[00:00:34] each other. This is relationship
[00:00:37] mapping. And so really the idea of an AI
[00:00:39] second brain has blown up because we're
[00:00:41] all trying to get as much information
[00:00:42] out of our heads into our systems as
[00:00:45] possible. That's the true value. Your
[00:00:47] moat is your data, it's your IP. But the
[00:00:49] process of organizing that into a system
[00:00:51] so that you can use it with a bunch of
[00:00:52] different AI models and so that it can
[00:00:54] actually recall things in a way that
[00:00:56] makes sense rather than just
[00:00:57] hallucinating or spending a bunch of
[00:00:58] your time and tokens trying to look
[00:01:00] through everything. That's the issue. So
[00:01:02] clearly all of this is my real data and
[00:01:04] this is what the actual project looks
[00:01:05] like. It is my Hercule project. I have a
[00:01:07] bunch of folders and files here and at
[00:01:08] the end of the day that's basically all
[00:01:10] it is. It is markdown files that are
[00:01:12] organized in a way that I understand and
[00:01:13] that my agents understand. And so yes,
[00:01:15] I'm going to walk you guys through what
[00:01:16] I have here and how it works, but I also
[00:01:18] have this other project where I'm going
[00:01:19] to show you if you're starting from
[00:01:20] scratch or if you feel like maybe you're
[00:01:23] in between level two and three, how we
[00:01:24] can actually look at the differences and
[00:01:26] what it might look like to scale up your
[00:01:28] own systems and start to add context in
[00:01:30] different ways. So super excited to dig
[00:01:32] into this today and I don't want to
[00:01:33] waste any of you guys' time, so let's
[00:01:35] just start looking at these five levels
[00:01:36] and how they differ. All right, so every
[00:01:39] level of a Claude Code second brain and
[00:01:41] I'm going to be obviously kind of
[00:01:42] referring to Claude Code a lot, but keep
[00:01:43] in mind this can be used with any AI
[00:01:46] model. I use my second brain all the
[00:01:47] time with Codex as well. I use it with
[00:01:48] Hermes Agent. This can be used by
[00:01:50] different agent harnesses because it's
[00:01:52] just files and folders. So, what is the
[00:01:55] actual job of a second brain? A lot of
[00:01:57] people probably define this differently,
[00:01:58] but the way that I think about it is
[00:01:59] that it's a place for me to save notes,
[00:02:02] meeting recordings, ClickUp threads,
[00:02:04] stuff like that. I can save it there,
[00:02:06] and then it helps me basically ingest it
[00:02:08] and get it into the right spots so that
[00:02:10] it can actually find it later. And so
[00:02:12] that's really the thing to think about
[00:02:13] is can your agent find it again, and
[00:02:16] could you find it again? Because if the
[00:02:17] answer is no, then you probably don't
[00:02:19] have the right routing or folder
[00:02:20] architecture set up, which is what I'm
[00:02:22] here to talk about today. And one other
[00:02:24] sort of mindset thing that I want to get
[00:02:26] out there before we dive into these five
[00:02:28] levels is that
[00:02:29] you kind of have to work backwards. You
[00:02:30] want to reverse engineer based on the
[00:02:33] question. So this will start to make
[00:02:34] more sense as we get into it, but really
[00:02:36] what you should be thinking about is how
[00:02:38] do I want to use this data in the
[00:02:39] future? Because how it's going to be
[00:02:42] accessed and recalled determines the way
[00:02:44] that you put it in in the first place.
[00:02:46] For example, a basketball hoop and a
[00:02:48] basketball. We know what shape the hoop
[00:02:51] is, and we know that the ball needs to
[00:02:52] go through. So why would we ever design
[00:02:54] the ball to be a giant square? Because
[00:02:58] it just wouldn't fit through the hoop,
[00:02:59] so that would make no sense. So you need
[00:03:00] to start with the end in mind a little
[00:03:02] bit. Once again, I will show you exactly
[00:03:04] what I mean by that as we continue on.
[00:03:06] Because remember, we're trying to get to
[00:03:07] the point where your second brain knows
[00:03:10] everything about your business, about
[00:03:11] you, your relationships. It knows
[00:03:13] everything to the point where
[00:03:14] it probably can recall stuff better than
[00:03:16] you can because it has a better memory,
[00:03:18] and it can search through things way
[00:03:19] faster than you can. So we've got five
[00:03:21] different levels to talk about, and they
[00:03:23] each kind of have different questions.
[00:03:25] So level one is, can you find the file
[00:03:27] or the info by looking for an exact word
[00:03:29] or name? Level two is, can you pull
[00:03:31] everything on a certain topic together?
[00:03:33] Level three is, I search for different
[00:03:35] words than I wrote, so semantic search,
[00:03:37] you're searching for meaning rather than
[00:03:38] an exact word match. And then trace
[00:03:41] relationship chains. Can you ask about
[00:03:44] topic X, and then trace that all the way
[00:03:46] back to topic A? And then level five is
[00:03:49] just kind of making this whole second
[00:03:50] brain thing super autonomous to the
[00:03:52] point that you don't even have to think
[00:03:53] about it. And by the way, this isn't me
[00:03:55] saying that number five is best. I have
[00:03:57] some arguments about why I do not
[00:03:59] currently sit on level five. The point
[00:04:00] I'm trying to make here is each level is
[00:04:02] different and you want to find the
[00:04:04] simplest level or the lowest level that
[00:04:06] actually fits your needs. If you don't
[00:04:08] have a pain point in your system, then I
[00:04:10] don't really think there's a need to go
[00:04:12] experiment or develop a new sort of, you
[00:04:15] know, architecture. If there's not pain,
[00:04:17] then why create more? Okay, so level one
[00:04:20] is pretty simple and this is where you
[00:04:22] always start. So you start with a
[00:04:23] claw.md or if you're using codex or
[00:04:25] something, you would start with an
[00:04:26] agents.md.
[00:04:28] But you start with a claw.md which is
[00:04:29] kind of, you know, that gets loaded up.
[00:04:31] That's almost like the system prompt for
[00:04:32] that session for that project. And then
[00:04:34] you've just got a bunch of folders and
[00:04:35] files. But the key part there is the
[00:04:37] claw.md is kind of treated as a router.
[00:04:39] So yes, you've got some, hey, this is
[00:04:41] your role, here is what's important, but
[00:04:43] you also have routing rules. If you ever
[00:04:45] need to find information about me
[00:04:46] personally, look in this folder. If you
[00:04:48] need information about our quarter one
[00:04:49] priorities, look in this folder. Because
[00:04:51] if you've ever had a point where you ask
[00:04:52] Claude to do something and then it asks
[00:04:54] you, hey, can you give me more info? I
[00:04:56] don't know what you're talking about,
[00:04:57] but you know there's files and folders
[00:04:58] in your project, then you probably just
[00:05:00] didn't give Claude the knowledge to go
[00:05:03] look there. It's not just going to go
[00:05:04] search your entire code base
[00:05:06] automatically. I mean, you wouldn't want
[00:05:07] it to do that cuz it's going to waste
[00:05:08] your time and your tokens. So if it
[00:05:10] doesn't know if something lives
[00:05:11] somewhere, then it's probably not going
[00:05:13] to be able to find it. So when this is
[00:05:14] properly set up, you will stop having to
[00:05:16] re-explain things, you will talk to it
[00:05:18] and it will just know where to go look
[00:05:19] and why. But the problems with this is
[00:05:21] that if it grows too big, it can start
[00:05:23] to get messy and feel ignored. And this
[00:05:25] is typically more of like an exact words
[00:05:27] type of search depending on the way that
[00:05:29] you route. So if I open up my um example
[00:05:32] project here, let's open up level one.
[00:05:34] So in level one, what you can see,
[00:05:35] pretend this is its own Claude project,
[00:05:37] we've got a claw.md. So let me click
[00:05:39] into that. We can see here it says, this
[00:05:41] file loads automatically every time you
[00:05:43] open Claude Code in this folder. It is
[00:05:44] the one file that tells the AI who you
[00:05:46] are, how you work, and where things
[00:05:47] live. At level one, this file plus a few
[00:05:49] folders is your entire second brain. So,
[00:05:51] here's kind of like that basic
[00:05:52] knowledge, and then right here, it's
[00:05:53] this simple, where things live. In the
[00:05:55] context folder, always true background
[00:05:58] about you and how you work, read this
[00:05:59] first. Projects, decision log, and
[00:06:01] that's basically it. So, right here you
[00:06:03] can see there's a context folder, we
[00:06:04] have an about me file, which you could
[00:06:06] grow. We have stack and conversations
[00:06:08] file. We have decisions, so this is a
[00:06:10] decision log where you can have your
[00:06:11] Claude at MD always append new decisions
[00:06:14] and dates whenever you make a big change
[00:06:16] to your project or to your life or to
[00:06:17] your business. And then we have
[00:06:19] projects, so this is where you could
[00:06:20] have a markdown file or even folders
[00:06:22] within the projects for all of your
[00:06:23] ongoing projects, all of your ongoing
[00:06:25] clients, whatever it is, however you
[00:06:26] want to organize it, that's where you
[00:06:28] can have some projects. And you can even
[00:06:29] start to organize these things by dates
[00:06:31] if you want. So, if you want to just
[00:06:32] have one that's for like May, and then
[00:06:34] you have all of those stuff, and you
[00:06:35] have one for June. The thing that I
[00:06:36] really want to stress here with level
[00:06:37] one, and the thing that I answer a lot
[00:06:39] in my community in the comments, is that
[00:06:42] there is not yet a standard way that has
[00:06:44] been proven the best way to set up your
[00:06:46] projects or your second brain besides
[00:06:48] some of the most common things like your
[00:06:49] contexts and your Claude at MD and your,
[00:06:51] you know, whatnot. But, the point I'm
[00:06:52] trying to make there is
[00:06:55] don't see what I do and think that
[00:06:57] that's the right way, or see what
[00:06:58] someone else you watch does and think
[00:06:59] that that's the only right way.
[00:07:02] All that matters is
[00:07:03] do you have proper routing in place, and
[00:07:06] does it make sense to you, and does it
[00:07:08] make sense to your AI? Okay, so let's
[00:07:09] say I have my Hercule project right
[00:07:11] here, and I need to find something in
[00:07:13] here, but I can't ask AI for some
[00:07:14] reason. What I need to find is easy
[00:07:16] because I understand the drill downs.
[00:07:18] You know, I understand my base folders,
[00:07:20] and let's say I'm looking for the HTML
[00:07:21] slide deck I built for my
[00:07:24] ranking Claude code features video. I
[00:07:26] would come into here and I say, okay, I
[00:07:27] know that's a project, so I'll go there.
[00:07:29] Within my projects, I've got another
[00:07:30] project for YouTube videos, I'll open
[00:07:32] that up. And now I know I made this
[00:07:34] video right here, May 30th Claude code
[00:07:37] top 50 features. In here, I have the
[00:07:39] actual tier list deck, and when I open
[00:07:41] that up, now I have the slide deck, and
[00:07:43] not only can I find it easily, but my
[00:07:44] agent can find it because it all makes
[00:07:46] sense and I have routing rules. Real
[00:07:47] quick, guys, if you're watching this
[00:07:49] video, you're probably interested in
[00:07:50] building your own AI operating system.
[00:07:52] Lucky for you, I have a full free course
[00:07:54] on that in my free school community. The
[00:07:55] link for that is down in the
[00:07:56] description. Join the free school
[00:07:57] community, hop in here, take the 7-day
[00:07:59] challenge, build your own AI operating
[00:08:01] system, and apply these principles into
[00:08:03] building your second brain, which will
[00:08:04] make your AI operating system even more
[00:08:06] powerful. So, link's in the description.
[00:08:07] Let's get back to the video. Awesome.
[00:08:08] Okay, so that is how you start. Now, as
[00:08:11] you move up to level two, you might be
[00:08:13] able to start to work in some things
[00:08:14] like the LLM Wiki, which is what I've
[00:08:16] got set up for a few different things.
[00:08:18] This is the whole Karpathy LLM Wiki,
[00:08:20] which I did make a full video about if
[00:08:21] you want to check that out. I'll tag
[00:08:22] that right up here. But, this is when
[00:08:24] you start to have more files and and
[00:08:26] they start to take a bit of a different
[00:08:27] shape, and you want to organize them
[00:08:29] together in a bit of a different way.
[00:08:31] So, it could be really good for
[00:08:32] researching all on a certain project. It
[00:08:34] could be really good for, you know, a
[00:08:35] few of the ones that I've got set up is
[00:08:36] my YouTube transcripts all live in their
[00:08:38] own Wiki. I've got all of like my
[00:08:40] meeting transcripts that live in their
[00:08:41] own Wiki. So, for example, this is the
[00:08:43] Obsidian view of my Wiki for all of my
[00:08:45] YouTube video transcripts. You can see
[00:08:47] here if I go to Wiki, you can see
[00:08:49] there's main concepts like agentic
[00:08:50] workflows, AI coding market, context
[00:08:53] window. And all of these in here start
[00:08:55] to relate back to other tools and
[00:08:57] concepts and videos and stuff like that.
[00:08:59] So, we've got the sources, we've got
[00:09:00] platforms, we've got um context
[00:09:02] management techniques. And all of this
[00:09:04] was auto-created by our Claude code when
[00:09:08] I told it to ingest this YouTube
[00:09:09] transcript into our Wiki. So, I'm not
[00:09:11] going to dive super super deep into all
[00:09:12] of this right now, but definitely check
[00:09:13] out that YouTube video I linked. Now,
[00:09:15] what else is cool about this is this
[00:09:17] transcript Wiki actually lives within my
[00:09:20] main Herc 2 project. So, here's Herc 2.
[00:09:22] If I go right here to Other Worlds, and
[00:09:24] then I go down to YouTube OS, and I
[00:09:26] click into the transcript Wiki right
[00:09:28] here, this is what we were just looking
[00:09:30] at in Obsidian. We could see the
[00:09:32] concepts, we could see the comparisons,
[00:09:33] we could see the sources, techniques.
[00:09:35] This is what we were looking at in
[00:09:36] Obsidian. So, all Obsidian is is it
[00:09:38] basically just visualizes your markdown
[00:09:41] files. You see here, wiki, concepts,
[00:09:43] comparisons, techniques. This is what we
[00:09:44] were just looking at. All we get now is
[00:09:47] we just get a visual view of all that.
[00:09:48] And so, the reason I wanted to bring
[00:09:49] that up as well is because I think a lot
[00:09:51] of people obviously get pretty
[00:09:53] infatuated by that visual view. And
[00:09:55] obviously, I started the video with that
[00:09:57] because I think that's what hooks a lot
[00:09:58] of people in. But, all that really
[00:10:00] matters is can your system grab that and
[00:10:02] give it to you? If you are a visual
[00:10:03] person and you really want that view,
[00:10:06] then by all means, install Obsidian and
[00:10:08] set it up. It's super easy. But, I'm
[00:10:09] saying that you don't always need that
[00:10:11] visual layer if it's not beneficial to
[00:10:13] you. I hardly ever open Obsidian, just
[00:10:14] to be honest, because I know that it all
[00:10:16] lives here and I know that my second
[00:10:18] brain and my OS can find all of that.
[00:10:20] So, anyways, in level two here, let's
[00:10:21] look at this. It's very similar in shape
[00:10:24] to level one. It's just building on top
[00:10:26] of it because now we have our claw.md,
[00:10:28] which starts to route to some other
[00:10:29] things because it routes to the wiki and
[00:10:31] it still routes to contexts, projects,
[00:10:33] decisions, but it's also routing to
[00:10:35] references and memory.md. So, we're just
[00:10:37] starting to add a bit more of these
[00:10:39] routing rules inside of the claw.md.
[00:10:41] We can grow the context, we can grow the
[00:10:43] decisions, we can grow projects and
[00:10:44] references, and we can also start to get
[00:10:47] this idea of memory. And what's really
[00:10:48] cool about this is you can turn on auto
[00:10:50] memory in Claude Code. And the AI will
[00:10:52] basically start to write this file and
[00:10:54] update it on its own. So, you don't have
[00:10:55] to think about it. If you come in here
[00:10:57] and you do {slash} memory, it'll say
[00:10:58] auto memory on or off. And if it's off,
[00:11:01] if you want to turn that on, just turn
[00:11:02] it on. And now, one thing to think about
[00:11:03] is I mentioned earlier that we want to
[00:11:05] make our second brains tool agnostic.
[00:11:08] And this is one thing that's pretty
[00:11:10] specific about Claude Code is it uses
[00:11:11] claw.md and it uses this memory.md and
[00:11:14] it keeps that updated on its own. So, if
[00:11:16] you wanted to move this over to Codex,
[00:11:18] what you would do is you would first of
[00:11:19] all transition your claw.md. You'd make
[00:11:21] a copy of it called agents.md. As you
[00:11:23] can see here in my Herc 2, I've got my,
[00:11:25] if I scroll down, claw.md right here,
[00:11:28] and then I've got agents.md right here.
[00:11:29] And they're essentially the exact same
[00:11:30] file. Just so Codex can read this one
[00:11:32] and Claude code can read this one. But
[00:11:33] because Claude code keeps that auto
[00:11:35] memory, all you need to do is make sure
[00:11:37] you have that memory.md file and just
[00:11:39] tell Codex, "Hey, by the way, for
[00:11:41] memories, look in our memory.md file."
[00:11:43] It's all about the routing there.
[00:11:44] Anyways, just felt like that was
[00:11:45] important to throw out. But at a certain
[00:11:47] point, when you have these, you know,
[00:11:48] wikis, they do start to degrade a little
[00:11:50] bit. Because what's what's great about
[00:11:52] them is that they have indexes, right?
[00:11:53] So, when your AI starts to look in the
[00:11:56] wiki, it knows, "Okay, if the user's
[00:11:58] asking about a genetic workflow, I'm
[00:12:00] probably going to start here. And then
[00:12:01] from here, I'm going to drill down and
[00:12:03] read this to see what else is important
[00:12:05] to them." Maybe they're asking about the
[00:12:07] WATC framework, and then I can drill
[00:12:08] into that. And maybe from there, I need
[00:12:10] to learn a little bit more about the
[00:12:11] Claude at MD system prompt, and then I
[00:12:13] will drill into that. So, there are
[00:12:14] relationships here a little bit, but
[00:12:16] this isn't the same as like semantic
[00:12:19] relationships or knowledge graph
[00:12:21] relationships that have more meaning.
[00:12:22] This is more about just actually
[00:12:24] following a trail and reading the page
[00:12:26] in its entirety. And I'll be fully
[00:12:28] honest with you guys,
[00:12:30] I pretty much sit my entire PERC 2
[00:12:32] project in this level, in level two.
[00:12:34] Because this has been working really
[00:12:36] well for me. Like I mentioned earlier, I
[00:12:37] haven't felt a pain yet big enough to
[00:12:40] switch over to level two. And here's
[00:12:41] what I meant by that. My wiki has links,
[00:12:43] isn't that a knowledge graph? Not
[00:12:44] exactly. Because this doesn't have
[00:12:48] connections of how they are related,
[00:12:49] like this is endorsed by this or this
[00:12:51] has cron to here. These just have
[00:12:54] connections because it's like a a see
[00:12:56] also. It's like backlinks. So, they're
[00:12:58] very similar, and yes, they can achieve
[00:13:00] a similar effect, but it's still a
[00:13:02] little bit different. Anyways, let's
[00:13:04] take a look at level three, which is
[00:13:05] where you start to do things like
[00:13:06] semantic search. Whether you do that in
[00:13:08] Obsidian, whether you do that with Pine
[00:13:10] Cone or Supabase, however you start to
[00:13:12] grab the actual semantic search,
[00:13:15] that is what level three is. And so,
[00:13:17] just as a quick visual for you guys,
[00:13:19] let's take a look at this quadrant
[00:13:21] cluster of images. So, every one of
[00:13:23] these vector points is an image. And
[00:13:26] what we see in here is the payload is
[00:13:28] stuff like the file name, the URL, the
[00:13:30] name of the author or the artist, and
[00:13:32] the URL. But, we don't actually see like
[00:13:34] what's in the image. We don't get a
[00:13:35] description. So, what we have to do is
[00:13:37] we have to organize these images by
[00:13:39] meaning or by similarity. So, when I
[00:13:41] open up this graph and we start to
[00:13:42] visualize the stuff here, what you see
[00:13:44] is that we have this main image, these
[00:13:46] owls, these kind of like I don't even
[00:13:48] know. Um it's a very trippy style, like
[00:13:51] hallucinogenic style. Anyways, then this
[00:13:53] one is kind of similar, right? It's got
[00:13:55] those colors, it's got the paints. This
[00:13:56] one is also similar, but they're not the
[00:13:58] same. They just share similarities. And
[00:14:01] as we start to expand these more and
[00:14:02] more, we can start to get into different
[00:14:04] styles. So, this one has like some
[00:14:06] creepy eyes and mushrooms or whatever.
[00:14:07] This one is kind of more down that
[00:14:09] fantasy lane. And as we start to build
[00:14:11] out more of these relationships and
[00:14:12] meanings, we can expand and grow away
[00:14:15] from them. And so, Quadrant really just
[00:14:16] gives you a visualization here. I mean,
[00:14:18] it's a it has clusters and vector store.
[00:14:21] But, [snorts] the reason I pulled this
[00:14:22] up as a demo is just because we start to
[00:14:23] see the actual relationships form here
[00:14:26] based on meaning. And that's what's
[00:14:28] important about semantic search is that
[00:14:29] we're no longer doing keyword matching,
[00:14:31] we're searching based on meaning. So,
[00:14:33] here in my YouTube transcript second
[00:14:35] brain, if I go to the smart lookup over
[00:14:38] here, this is very different from just
[00:14:40] the regular search. So, for example, if
[00:14:42] I search here for um
[00:14:45] feedback, let's say. We're actually
[00:14:47] doing a match on the word feedback, and
[00:14:49] it's only showing me where that word
[00:14:51] actually appears inside of our second
[00:14:54] brain. But, if I come over here in the
[00:14:56] smart lookup and I search for feedback,
[00:14:58] we are getting matches that have things
[00:15:00] in here that mean feedback. So, live
[00:15:02] test results, cloud code skills, which
[00:15:04] was uh talking about evaluations and
[00:15:05] stuff. So, there's a big difference
[00:15:07] between keyword matching and semantic
[00:15:09] search, you know, similarity matching.
[00:15:11] This one over here is saying X equals X,
[00:15:13] and this one is saying X is similar to
[00:15:15] X, Y, and Z. And so, this all just goes
[00:15:17] back to vector databases. I've talked
[00:15:19] so, so much about vector databases, so
[00:15:21] I'm not going to dive super deep in.
[00:15:22] I've got so many resources on my
[00:15:24] channel. But basically, what it is is we
[00:15:26] take a document, so let's just say
[00:15:28] YouTube transcript, we chunk it up, and
[00:15:30] then each chunk is ran through an
[00:15:32] embeddings model. And the embeddings
[00:15:33] model puts that chunk of text onto like
[00:15:36] a three-dimensional space where space is
[00:15:39] related to meaning. And so it decides,
[00:15:41] okay, this chunk is about a company, so
[00:15:42] we're going to put it up here. This
[00:15:44] chunk is about finances, so it's going
[00:15:45] to go here. And we start to see these
[00:15:47] vectors form near other similar vectors.
[00:15:50] Now, do you guys remember how I said
[00:15:51] earlier, like you want to think about
[00:15:53] how is the data going to be used? What
[00:15:54] type of questions are you going to ask?
[00:15:56] This is a reason why that's so
[00:15:57] important. So think about this. Let's
[00:15:59] say I put my meeting transcript of March
[00:16:02] 5th meeting into my second brain. And I
[00:16:05] put those in as, you know, vectorized
[00:16:07] chunks. So let's say when I vectorize
[00:16:08] that meeting, we actually get, you know,
[00:16:11] like
[00:16:12] 20 chunks. It actually creates 20
[00:16:14] chunks, or however many that is. And
[00:16:15] then when I say, "Hey, Mr. AI agent, can
[00:16:17] you summarize the meeting on March 5th?"
[00:16:20] It will basically search for March 5th
[00:16:22] meeting summary, and it will pull chunks
[00:16:24] that are similar to March 5th meeting
[00:16:26] summary. And then even if it gets the
[00:16:28] right chunks, it's going to only
[00:16:29] summarize those five chunks. It's not
[00:16:31] able to look at the entire meeting
[00:16:33] summary, or sorry, like meeting
[00:16:35] transcript in entirety. So it doesn't
[00:16:37] really know a summary. It might be
[00:16:38] missing a lot of key information. Now
[00:16:40] yes, there are things you can start to
[00:16:41] play with there like metadata and other
[00:16:42] things like that to make these results
[00:16:44] better, but at the end of the day,
[00:16:47] people kind of assumed that a vector
[00:16:48] database was some magic solution where
[00:16:50] it could always pull back what you need,
[00:16:52] but that is very false. And I mean,
[00:16:53] think about it like this. Let's say we
[00:16:55] have a table, and we say, "Hey, which
[00:16:56] week did we have the highest sales?"
[00:16:58] Okay, the agent looks for highest sales,
[00:17:00] it maybe grabs this chunk outlined in
[00:17:02] gray of data, and then it looks at,
[00:17:04] "Okay, week six here was the highest
[00:17:06] sales, so that must be the answer." But
[00:17:08] in reality, you can see week 14 was
[00:17:10] higher, week 19 was higher. So when you
[00:17:12] need something that has actual full
[00:17:15] context,
[00:17:16] then you can't do the vector database
[00:17:18] chunking. That's where you'd rather just
[00:17:19] have a markdown file of March 5th, and
[00:17:22] then all this agent would have to do is
[00:17:23] read that entire markdown file and then
[00:17:26] give you a summary. And that's just
[00:17:27] going to be more accurate. So, in this
[00:17:29] project, if we open up level three, you
[00:17:31] can see it's very similar because you
[00:17:32] can still have context files, decision
[00:17:34] files, you can still have all that, and
[00:17:36] then you might identify, "Okay,
[00:17:38] actually, this one specific unit of my
[00:17:40] business, maybe my YouTube transcripts,
[00:17:42] maybe I want just that to be a vector
[00:17:44] database, but I still want my context
[00:17:46] and my projects and my decisions to be
[00:17:48] markdown files."
[00:17:49] So, another point I'm trying to make
[00:17:50] here is
[00:17:51] just because you have a second brain,
[00:17:53] and just because you have a massive, you
[00:17:54] know, folder here with a bunch of
[00:17:56] folders and files, doesn't mean that the
[00:17:58] whole folder needs to be one style. It
[00:18:01] doesn't mean that everything needs graph
[00:18:02] rack. It doesn't mean that everything is
[00:18:04] just LLM Wiki. It means that you're able
[00:18:05] to decide, based on the type of data and
[00:18:07] the way you use it, how can you
[00:18:09] structure this specific folder in the
[00:18:11] way you want it. So, here we have a
[00:18:12] vector index folder, and we click on the
[00:18:14] house search works. It works by
[00:18:15] chunking, embedding, search, hybrid,
[00:18:18] re-ranking. There's some things you can
[00:18:20] get really, really nitty-gritty on when
[00:18:21] it comes to semantic search. But what
[00:18:23] vector retrieval is really, really good
[00:18:25] at is looking at tons and tons of data,
[00:18:27] typically just like a lot of text, and
[00:18:29] when you need a very specific answer,
[00:18:31] something that's very similar. So, if
[00:18:32] you had a thousand rules that you needed
[00:18:34] to store, and you basically said, "Hey,
[00:18:37] um can you remind me what rule 17 was?"
[00:18:39] That might be a really good use case for
[00:18:41] vector search because it's able to
[00:18:43] search for rule 17, pull in those
[00:18:44] chunks, and just give you a little
[00:18:45] snippet because it would be a waste of
[00:18:47] time and tokens for your agent to read
[00:18:49] the entire markdown file of all 1,000
[00:18:51] rules if you just needed rule 17. So,
[00:18:54] that's kind of the difference there.
[00:18:54] Like I said, I've got so many videos on
[00:18:56] vector stuff on my channel, but really
[00:18:59] you could say, "Hey,
[00:19:00] to your cloud code agent, I have this
[00:19:01] data. Here's how I want to use it. Do
[00:19:03] you think this would be better for now
[00:19:04] as markdown files, or should I do
[00:19:06] semantic search? Like what would
[00:19:08] actually make more sense here?" And it
[00:19:09] will help walk you through the way that
[00:19:10] you should actually set that up. So, now
[00:19:12] I hope you guys are starting to
[00:19:13] understand why I said, you know, moving
[00:19:16] up on or I'm sorry, like moving up on
[00:19:18] levels, moving down doesn't necessarily
[00:19:19] mean better. It's all about figuring out
[00:19:21] what is the pain point with what you're
[00:19:23] currently doing and where would a
[00:19:24] different level help you out and fix
[00:19:27] that pain point. Okay, so now let's take
[00:19:28] a look at level four. This is where we
[00:19:30] start to get into like knowledge graphs
[00:19:32] and relationship graphs, which typically
[00:19:34] are going to be the most complex and
[00:19:35] sometimes the most expensive as well. If
[00:19:37] you're doing it on a certain platform,
[00:19:38] you could always use open source
[00:19:39] software, but anyways, knowledge graphs.
[00:19:42] And I also want to be up front. I've
[00:19:43] played with these a lot, but I do not
[00:19:45] actually use these on the day-to-day
[00:19:47] because I found out just other ways to
[00:19:49] use routing files and wikis that fit my
[00:19:52] needs. Now, my work is very different
[00:19:53] than what a lot of you guys' work may
[00:19:55] be. Mine is very project-based and it is
[00:19:57] very, you know, content-heavy. I don't
[00:19:59] have a massive CRM to manage with a
[00:20:01] bunch of different businesses and
[00:20:03] clients, you know? And if I did, maybe a
[00:20:05] knowledge graph would make a lot more
[00:20:06] sense and it probably would. But
[00:20:08] typically, the cool part about that is
[00:20:10] if you identify that you needed a
[00:20:11] knowledge graph, let's say for all your
[00:20:13] projects, you needed you wanted to put
[00:20:15] all of this in a knowledge graph,
[00:20:16] the data probably already exists here.
[00:20:19] And that's the thing about building out
[00:20:20] these relationships in your knowledge
[00:20:23] graph is that the system, whatever
[00:20:24] software you use, is typically going to
[00:20:26] be pretty good at embedding that and
[00:20:27] creating that. But the problem that you
[00:20:29] have to solve is you have to give it
[00:20:30] enough data. And so, one thing that I
[00:20:32] really like to do is I like to have
[00:20:33] these brainstorm sessions, as you can
[00:20:34] see. And what I do with these brainstorm
[00:20:37] sessions is I use a skill called Grill
[00:20:38] Me. So, if you see here, I have a skill
[00:20:40] called Grill Me, which I originally got
[00:20:42] from Matt Pocock. I customize it a
[00:20:43] little bit. I'll leave the skill for
[00:20:46] Grill Me in my free school community.
[00:20:47] The link for that is down in the
[00:20:48] description. All you have to do is hop
[00:20:49] in here, go to classroom, click on all
[00:20:51] YouTube resources, and you can find all
[00:20:53] the skills and everything like that. But
[00:20:55] the skill, what that does, is it
[00:20:56] basically just grills me. It interviews
[00:20:58] me relentlessly about a certain topic
[00:21:00] and it creates a brainstorm file here.
[00:21:02] It only stops when it knows everything
[00:21:03] about it. So, if you wanted to start
[00:21:05] building up a knowledge graph for all
[00:21:06] your clients and businesses, just say
[00:21:08] "Grill me about client A. Grill me about
[00:21:10] client B. Grill me about business A."
[00:21:12] And it would just ask you questions and
[00:21:13] you can feed it files. You can give it
[00:21:15] stuff. You can feed it in transcripts.
[00:21:16] You can feed it in, you know, contracts,
[00:21:18] whatever it is. And that's how you can
[00:21:19] start to form a lot of data.
[00:21:22] Hey guys, me again. Real quick, I'm
[00:21:23] editing this video and I realized that I
[00:21:24] needed to throw out one thing here,
[00:21:26] which is that obviously, if you're
[00:21:29] putting all of this data and you're
[00:21:30] sending it all to Anthropic, to Claude
[00:21:32] models, then
[00:21:33] that's not private. So, if you feel
[00:21:36] comfortable with that, that's fine. I am
[00:21:37] putting a lot of my data in there and it
[00:21:39] is my business stuff and
[00:21:41] that's what I'm doing. But, if you don't
[00:21:43] feel comfortable with that or you, you
[00:21:44] know, don't want to send client data, of
[00:21:45] course you don't, then maybe you want to
[00:21:48] do that through open-source models and
[00:21:49] maybe Claude code isn't where you have
[00:21:50] the second brain that has every single
[00:21:52] piece of information about you and your
[00:21:54] business and your client's business. So,
[00:21:56] the point I'm trying to make here is
[00:21:57] just this is what I'm doing. I'm
[00:21:58] obviously aware of the fact that my data
[00:22:01] goes to Anthropic when I process it
[00:22:03] through Claude. And if you guys are
[00:22:04] doing that, then you should also be
[00:22:06] aware of that. But, there are other
[00:22:07] options if you can't do that. So, I
[00:22:08] wanted to throw that out there. I am
[00:22:10] planning to make a ton of videos here
[00:22:11] soon about local AI and open-source
[00:22:13] models and all this stuff cuz it's a
[00:22:15] really, really exciting space that I
[00:22:16] think is going to start becoming bigger
[00:22:18] and bigger. So, yeah, keep that in mind.
[00:22:20] Back to the video. I think sometimes
[00:22:22] that's a misconception about how I got
[00:22:25] here and how people build their own AI
[00:22:27] OS or second brain is that
[00:22:29] they think the problem is the system not
[00:22:31] retrieving it great, which sometimes it
[00:22:33] is, but sometimes it seems like the
[00:22:34] bigger problem is getting everything out
[00:22:36] of your brain into the system. So,
[00:22:38] before you blame AI, take a look at your
[00:22:42] folders and files and say, "Is this
[00:22:43] actually holistic? Is this Does this
[00:22:46] have all the nuance that I have in my
[00:22:47] brain?" Anyways, from there, when you
[00:22:49] open up level four, you can see that
[00:22:50] it's it's, you know, very similar still.
[00:22:52] We're just adding on a few things. You
[00:22:53] can see here we've added an agents.md,
[00:22:55] which is the exact same as the
[00:22:56] claude.md. And what else is cool is you
[00:22:58] can literally just reference inside of
[00:22:59] your claude.md at agents.md and then you
[00:23:01] can delete all this because this
[00:23:03] basically just like injects that file
[00:23:05] into here. But I just wanted to show
[00:23:06] that. But anyways, you can see we're
[00:23:08] still following the same principles. We
[00:23:09] have a wiki. We've also added a
[00:23:11] knowledge graph layer. We've still got
[00:23:13] the same where things live with the
[00:23:14] routing with all these just regular
[00:23:16] folders and boring markdown, but boring
[00:23:18] is beautiful. You can see that our
[00:23:19] memory is still here. It's starting to
[00:23:21] grow, and we just keep building on top
[00:23:23] of this. So what one thing we added here
[00:23:25] as you can see was our knowledge graph
[00:23:26] folder. And so what happens here is we
[00:23:28] get different entities, right? So like
[00:23:29] we can see okay Jordan is a person. Acme
[00:23:31] is a company. And then we can start to
[00:23:33] form relationships between all these
[00:23:34] things. So Jordan works at Acme. Acme is
[00:23:38] endorsed by Postpilot. Postpilot is a
[00:23:40] competitor of Cadently. And it starts to
[00:23:42] build out not only these entities, but
[00:23:43] it shows you how they're all related.
[00:23:45] And so that's why when I said that I
[00:23:47] really like using, you know, this um
[00:23:49] what's it called? LLM Wiki is because I
[00:23:52] have enough of that feel of all these
[00:23:54] relationships because I've put so much
[00:23:55] time and effort into ingesting these in
[00:23:58] the right way and giving it context. The
[00:24:00] thing about this one is that it has to
[00:24:02] read every single file it wants. Maybe
[00:24:04] it was looking at AI video production
[00:24:06] and all it needed to know was
[00:24:07] ElevenLabs, it still would have read
[00:24:09] this entire file first. And so that's
[00:24:12] where sometimes the knowledge graph is
[00:24:13] actually more lightweight in that sense.
[00:24:16] And this is the example I showed at the
[00:24:17] beginning of the video where we have
[00:24:18] Lightrag. And forgive me, I'm going to
[00:24:20] have to blur some of this stuff out
[00:24:21] because this is like legitimately my
[00:24:23] entire second brain in our business. But
[00:24:24] as I really zoom in here and this kind
[00:24:26] of slows down my computer because
[00:24:27] there's so much. But what you'll notice
[00:24:29] is that we actually start to get
[00:24:31] relationships. I probably shouldn't have
[00:24:32] done this with so much data, but you can
[00:24:34] see like we have this collaborates with
[00:24:36] that. We have this builds that. And so
[00:24:39] if I really started to open up all of
[00:24:41] these little
[00:24:42] you know, circles, we could see what was
[00:24:45] going on and how they're all related. We
[00:24:46] could see that our 7-day AI challenge it
[00:24:48] was provided from YouTube. It connects
[00:24:52] to the onboarding process of AIS Plus.
[00:24:54] It was developed by Aiden. And so we can
[00:24:56] basically follow around these
[00:24:57] relationships, as you see. And even
[00:24:59] though it's pretty much the same data
[00:25:00] that you see here in Obsidian, we're not
[00:25:02] getting that same level of relationships
[00:25:03] between these different entities. So,
[00:25:05] anyways, if you guys want to see, you
[00:25:06] know, a full breakdown video on
[00:25:08] something like Logseq or um Graphir or
[00:25:10] all the other solutions that there are
[00:25:11] out there for more of a knowledge graph
[00:25:13] relationship graph, then let me know.
[00:25:14] But, that is kind of the difference
[00:25:16] there. So, if you don't need those sort
[00:25:17] of relationship chains, and you're not
[00:25:19] worried about that semantic type of
[00:25:21] relationships, then you probably don't
[00:25:22] need to use something like a knowledge
[00:25:25] graph. And then, level five, we have
[00:25:26] more of the always-on Brain OS, and
[00:25:29] something like Gbrain. Garry Tan, CEO of
[00:25:32] Y Combinator, he created this thing
[00:25:34] called Gbrain, which pairs really well
[00:25:35] with G stack. But, Gbrain is kind of the
[00:25:37] idea of everything we've talked about
[00:25:39] here. Wikis, routing, relationships,
[00:25:41] tools. But, Gbrain has kind of that
[00:25:44] always-on element, because it is like
[00:25:45] constantly syncing and refreshing
[00:25:48] memories and adding more stuff. So,
[00:25:49] adding in Gbrain to something like a
[00:25:51] Hermes agent would be really, really
[00:25:52] good. You could still do it in cloud
[00:25:54] code, but you'd have to handle those
[00:25:55] crons and get all that stuff set up,
[00:25:57] which is why I don't currently run
[00:25:58] Gbrain at the moment, but I have been
[00:25:59] playing around with it with my Hermes
[00:26:01] agent. So, anyways, the point here is
[00:26:02] that it's very similar to everything
[00:26:04] else we've just talked about. It's just
[00:26:05] having that auto-updating feel, more of
[00:26:08] the autonomous, always-on feel.
[00:26:10] But, I will say, another thing that I
[00:26:12] kind of that kind of scares me about
[00:26:13] that is you have this whole dilemma of,
[00:26:16] you know,
[00:26:17] when do you have too much context? And
[00:26:19] when does it get to the point where it's
[00:26:20] actually doing more damage than it's
[00:26:22] doing good? And the reason I bring that
[00:26:23] up is because I am in complete control
[00:26:25] of what my second brain ingests. I will
[00:26:28] run a skill to go grab all of my meeting
[00:26:30] transcripts from the week. I will say,
[00:26:31] "Hey, here's something. Help me figure
[00:26:33] out like how many brains are about this,
[00:26:35] and then let's ingest it together." And
[00:26:36] for me, I really like being in that
[00:26:37] control, because in my mind, there's a
[00:26:39] big difference between a few types of
[00:26:41] data. If you guys remember in my like AI
[00:26:43] OS videos, I've talked about the four
[00:26:44] C's. So, context, connections,
[00:26:46] capabilities, and cadence. And for the
[00:26:47] second brain, I mainly think about it as
[00:26:49] just these first two. So, context and
[00:26:51] connections. And so, when I think of
[00:26:53] context, that's stuff like, you know,
[00:26:55] what my business has done. So, if I come
[00:26:56] into here, into my my second brain, and
[00:26:59] you can see here if I go to
[00:27:01] um up at OTAs. So, OTAs are basically
[00:27:03] just our projects for the quarter. And
[00:27:05] so, here I can see all the Q1 ones,
[00:27:06] right? I can look at all those and I can
[00:27:08] click at them and see decisions that
[00:27:09] we've made in the statuses. And I can
[00:27:11] also see Q2 OTAs. So, I can see what's
[00:27:12] going on here. And my second brain's
[00:27:14] able to see that because that has been
[00:27:16] basically those are locked in decisions.
[00:27:17] This is what we're doing this quarter,
[00:27:19] and then I'm updating the statuses of
[00:27:20] that stuff. So, that's like context.
[00:27:22] That's what's going on in the business.
[00:27:23] But when it comes to connections, if I
[00:27:25] go back to this, this is more of like
[00:27:27] the real data that isn't as evergreen.
[00:27:29] This is stuff that changes. This is like
[00:27:31] Slack threads. This is emails. This is a
[00:27:33] customer data. And that type of data you
[00:27:35] don't want to ingest into a second brain
[00:27:37] because that's just noise then. Then you
[00:27:39] have to go back every month and like
[00:27:41] delete old stuff. So, the way that I
[00:27:43] like to think about my actual second
[00:27:44] brain is stuff that I'm not going to
[00:27:45] delete. This is stuff that is like,
[00:27:47] okay, in a year, will it be good for me
[00:27:49] to have this memory in here? Yes.
[00:27:51] Otherwise, it's just adding noise. So,
[00:27:53] when you're adding data into your
[00:27:54] project, think about it like the context
[00:27:57] and connections. Think about if this is
[00:27:58] kind of like more evergreen, holistic
[00:28:00] data, or if this is more things that are
[00:28:02] going to change next week. So, you
[00:28:04] probably shouldn't pull it in, but you
[00:28:05] should make sure that your second brain
[00:28:07] has access to go grab it. So, that way
[00:28:09] if I said to my second brain, "Hey, can
[00:28:11] you just take a look real quick at what
[00:28:13] John and I were talking about last week
[00:28:14] about, you know, OTA number seven?" It
[00:28:17] would first go to our OTA file, and it
[00:28:19] would search through there and it it
[00:28:20] would try to find it there. If it
[00:28:21] couldn't find it there, it would look
[00:28:22] through the Wiki and it would look
[00:28:23] through meeting transcripts and see what
[00:28:25] we talked about there. And if it
[00:28:26] couldn't find it there, it would finally
[00:28:27] go to ClickUp itself, pull real data in
[00:28:29] from me and John's conversations, and
[00:28:31] see if the answer lived there. And so,
[00:28:33] that in my mind is still a second brain
[00:28:34] because I'm able to ask a vague
[00:28:36] question, and the second brain knows
[00:28:37] exactly where to look in what order to
[00:28:39] find that real-time data, and then give
[00:28:41] me back the answer that I need. That's
[00:28:42] the question I ask myself is, "Does this
[00:28:44] thing understand where my data lives and
[00:28:46] where to look, and can to give me
[00:28:47] accurate answers. So, as far as finding
[00:28:49] your level, remember your whole project
[00:28:51] doesn't fit into one level. Maybe this
[00:28:53] folder's level two, maybe this folder's
[00:28:54] level four, maybe this folder's level
[00:28:56] three. Here's some things to think
[00:28:57] about. If you were re-explaining your
[00:28:59] setup and you need to find things by
[00:29:00] exact words or files, look at level one.
[00:29:03] If you have 30 plus notes and you keep
[00:29:04] forgetting what's in them, look at level
[00:29:06] two. That's where you sort of like
[00:29:07] ingest them and get that wiki with
[00:29:08] relationships. If your project is just
[00:29:10] completely whiffing on notes that you
[00:29:11] know exist and your routing isn't
[00:29:13] working, then maybe you want to look for
[00:29:15] something more like a semantic search
[00:29:16] that doesn't rely on an exact word level
[00:29:19] match. If you're looking for
[00:29:20] relationships and to be able to follow
[00:29:22] chains of questions and thoughts, then
[00:29:24] you probably want to look for something
[00:29:25] like a knowledge graph. you're running
[00:29:26] agents offline and you've got so much
[00:29:27] data and you want to sync up a bunch of
[00:29:29] Hermes agents together, then you
[00:29:30] probably are looking for something like
[00:29:31] level five, something like G brain. And
[00:29:34] another topic that I get some questions
[00:29:35] about, which I'm not going to fully
[00:29:36] address in this video, but I will
[00:29:38] briefly bring up is the fact that you
[00:29:40] are building your own second brain OS.
[00:29:43] So are other people on your team. The
[00:29:45] next question is, how do you actually
[00:29:46] make sure that everyone's data is
[00:29:48] syncing together and how do you have
[00:29:49] more of like your team second brain?
[00:29:51] There's a lot of different ways to solve
[00:29:52] that. I think once again, it's not an
[00:29:54] issue of, oh, do we use Google Drive or
[00:29:56] Notion or GitHub or cloud plugins? I
[00:29:59] think the issue to figure out with your
[00:30:01] team is how do we actually make sure
[00:30:03] that we all have it shift so that this
[00:30:05] stuff is actually useful and not just
[00:30:07] noise. How do we make sure that process
[00:30:09] owners are updating their docs and
[00:30:10] syncing their stuff there? How do we
[00:30:12] make sure that other people are pulling
[00:30:13] from that rather than always just
[00:30:15] pinging the same people for questions
[00:30:17] and answers all the time? I think the
[00:30:18] adoption and the change management
[00:30:19] question is the bigger one. The tech and
[00:30:21] the way it actually functionally rolls
[00:30:23] out is a little bit less. But what I do
[00:30:26] know is that you getting set up with
[00:30:28] your own first and understanding how it
[00:30:30] works, how you should route, how you
[00:30:31] should make the decisions of where the
[00:30:32] data should live, that's the first
[00:30:34] hurdle. You can only solve the team-wide
[00:30:36] problem once you feel comfortable about
[00:30:38] the way you run it every single day and
[00:30:40] then it works for you. That is going to
[00:30:41] do it for today. Like I said, you guys
[00:30:42] can grab all the skills and everything
[00:30:44] that you need from this free community.
[00:30:47] description. I will also include the
[00:30:48] slide deck if you guys are interested in
[00:30:49] flipping through. So, if you guys
[00:30:51] enjoyed the video or you learned
[00:30:52] something new, please give it a like. It
[00:30:53] helps me out a ton. And as always, I
[00:30:54] appreciate you guys making it to the end
[00:30:56] of the video, and I will see you all in
[00:30:57] the next one.
[00:30:58] Thanks, guys.
