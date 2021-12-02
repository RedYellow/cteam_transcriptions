# Parsing rules

The theme song takes about a minute -- remove everything before the end from the subtitle files and replace it with the saved text file

- might have to make sure that it is actually played in each episode, I don't know if there are any like this but could be possible
- anyway it would be good to keep the code modular and reusable

# Standard formatting rules for data

- Leave the timestamps in as much as possible
  - except when line with the timestamp would be blank after corrections

## Format

02:26:42,170 --> 02:26:51,440
\dm Here are some instructions
\pc Blah blah blah

Named characters should be registered in a central readable file for reusablility

# Character Registry

Each shortname should be unique
The shortname is what should be used as the dialogue tag in the text source
e.g. A character registered with shortname "walnut" should appear as \walnut: in the text source and will appear as \walnutspeaks in the LaTeX code

If a character name is not in the registry, it should be treated as a DMPC

Character names should be preceded by a backslash (\) in the source text files, to distinguish between a their dialogue and someone just saying their name.

Character names should appear in smallcaps in the final transcript.

How should the DM be handled? May be several different people.

How should the actual players be handled?

- probably just have them not show up in the cast but register their information anyway

## Example

shortname: walnut

&ensp;fullname: Walnut Dankgrass

&ensp;race: Wood Elf

&ensp;class: Druid

&ensp;description: Reppin the natural world

&ensp;playername: Trystan Falcone

# Text formatting syntax

Generally use `_text_` for writing italics and `**text**` for bold. Markdown will read \*\*\_ and \_\_ both as bold, and \_ and \_ both as italics, but better to keep them separated for better readability.

# TODO:

- Include arc names (multiple episode storylines)
