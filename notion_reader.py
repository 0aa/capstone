from notion_client import Client
from config import load_config

def fetch_notion_knowledge():
    config = load_config()
    notion_token = config["notion_token"]
    page_id = config["notion_page_id"]

    notion = Client(auth=notion_token)
    blocks = notion.blocks.children.list(block_id=page_id)

    content = []

    for block in blocks['results']:
        block_type = block.get("type", "")
        block_data = block.get(block_type, {})

        # Many types like paragraph, heading_1, etc. have 'rich_text'
        rich_text = block_data.get("rich_text", [])
        for rt in rich_text:
            plain = rt.get("plain_text", "")
            if plain:
                content.append(plain)

    return "\n".join(content)