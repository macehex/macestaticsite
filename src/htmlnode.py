class HTMLNode:
    def __init__(
        self,
        tag: str = "",
        value: str = "",
        children: list["HTMLNode"] = None,
        props: dict[str, str] = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError(
            "Child classes will override this method to render themselves as HTML."
        )

    def props_to_html(self) -> str:
        # href="https://www.google.com" target="_blank"
        if not self.props:
            return ""
        return f'href="{self.props["href"]}" target="{self.props["target"]}"'

    def __repr__(self) -> str:
        return (
            f"HTMLNode tag: {self.tag}, "
            f"value: {self.value}, "
            f"children: {self.children}, "
            f"props: {self.props}"
        )
