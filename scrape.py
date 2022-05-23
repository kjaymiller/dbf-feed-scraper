import feedparser
from markdownify import markdownify
from pathlib import Path
from slugify import slugify

url = "https://feeds.simplecast.com/5nKJV82u"
output_folder = Path("./content")
output_folder.mkdir(exists_ok=True)


feed = feedparser.parse(url)

for entry in feed.entries:
    # Get the content of the post
    for content in entry["content"]:
        if content["type"] == "text/html":
            shownotes = "\n\n".join(
                (
                    f"# {entry.title}",
                    markdownify(content["value"]),
                    f"_published: {entry.published}_",
                )
            )

    episode = slugify(f"{entry.title} - {entry.published}") + ".md"
    Path(output_folder / episode).write_text(shownotes)
